<h2>Design problem to generate a cityscape:</h2>

- My goal was to create a cityscape, in which designer can change the location of different districts, and based on that a city is generated with Grasshopper/ python script
- City being a complex system, to create a script that would capture even most of the relations between different parts is very difficult task
- I focused on a few different relations that affect the cityscape, to make it relatively realistic.


Solution:

- To divide the terrain generated in Grasshopper for different districts, I divided the point cloud (from which the terrain was made) into separate 
 lists of points, each of which represent their own district: 
  - list of industrial points,
  - center points, suburban points, forest points, etc.
- The location of the district points can be changed via grasshopper slider
- These lists are input for python script, and buildings/ road is generated with python algorithm. each point work as an insertion point for building, tree or as a start/end 
  for a road

Script structure:

The most important methods:
- ```def Roads(StartPoint, IsBranch)```:
  - This is the first method to be executed in the script. The Street network is generated randomly, following certain rules and 
     constraints:
     1) the road starts from the indicated starting point (StartPoint)
     2) If the ```IsBranch = True```, it means that the road generated is a branch 
        from main road. A Branch is generated with recursive computing principle: The method Roads is randomly called inside the method 
        itself, starting a new road (branch)
     3) The length of main road is 10 units, and branch is 5

