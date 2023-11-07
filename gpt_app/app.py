from flask import Flask
import ghhops_server as hs
import rhino3dm
import openai
from decouple import config
import json
import numpy as np

openai.api_key = config('API_KEY')

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/Generate_Geometry",
    name="GPT geometry",
    description=" Generate primitive geometry based on text input using chat GPT",
    inputs = [hs.HopsString("text", "G", "Geometry description"),
              hs.HopsString("description", "D", "Additional description"),
              ],
              
    outputs=[hs.HopsPoint("Vertex", "V", "corner vertices")],
)


def Generate_Geometry(text, description):

    def get_vertex_coordinates(X, Y, Z):

        np_X = np.array(X)
        np_Y = np.array(Y)
        np_Z = np.array(Z)
        flipped = np.dstack((np_X, np_Y, np_Z))

        return flipped.tolist()[0]

    function_descriptions = [
    {
        "name" : "get_vertex_coordinates",
        "description" : "provide a list the x, y z- coordinates of a geometry vertex",
        "parameters" : {
            "type" : "object",
            "properties" : {
                
                "X" : {
                    "type" : "number",
                    "description" : "all X-coordinates of a vertex as a list, e.g. [-1, 3, 5, 7] etc."
                },
                "Y" : {
                    "type" : "number",
                    "description" : "all Y-coordinates of a vertex as a list, e.g. [-1, 3, 5, 7] etc."
                },
                "Z" : {
                    "type" : "number",
                    "description" : "all Z-coordinates of a vertex as a list, e.g. [-1, 3, 5, 7] etc."
                }
            },
            "required" : ["X", "Y", "Z"]
        }
    }
]
    

    response_2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature = 0,
    messages=[
        
        {"role": "user", "content": text},
        {"role": "assistant", "content": description} 
    ],
    functions = function_descriptions,
    function_call="auto",
    )

    print(response_2)

    params = json.loads(response_2.choices[0].message.function_call.arguments)

    chosen_function = eval(response_2.choices[0].message.function_call.name)
    points =chosen_function(**params)

    P_list = []
    for p in points:
        P_list.append(rhino3dm.Point3d(p[0], p[1], p[2]))

    return P_list


if __name__ == "__main__":
    app.run(debug=True)