Design problem to generate a cityscape:

- My goal was to create a cityscape, in which designer can change the location of different districts, and based on that a city is generated with Grasshopper/ python script
- City being a complex system, to create a script that would capture even most of the relations between different parts is very difficult task
- I focused on a few different relations that affect the cityscape, to make it relatively realistic.


-To divide the terrain generated in Grasshopper for different districts, I divided the point cloud (from which the terrain was made) into separate 
lists of points, each of which represent their own district: 
  -list of industrial points,
  - center points, suburban points, forest points, etc.
-The location of the district points can be changed via grasshopper slider
-These lists are input for python script, and buildings/ road is generated with python algorithm. each point work as an insertion point for building, tree or as a start/end 
  for a road

