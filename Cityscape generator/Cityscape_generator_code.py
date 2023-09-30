
__author__ = "Ilmo_Kapanen95"
__version__ = "2021.05.07"
                
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random
        
a=[]
t_vectors  = []
Road_points_used = []
Road_lines = []

def main():
    Roads(Road_points[0], False)
    Roads(Road_points[100], False)
    Roads(Road_points[130], False)
    Roads(Road_points[160], False)
    center()
    suburban()
    industrial()
    forest()

def forest():
    list_of_building_lists = []
    list_of_building_lists.append(trees_1)
    list_of_building_lists.append(trees_2)
    list_of_building_lists.append(trees_3)
    list_of_building_points = []
    list_of_building_points.append(trees_p1)
    list_of_building_points.append(trees_p2)
    list_of_building_points.append(trees_p3)


    i = 0
    for p in forest_points:
        if IfOnRoad(p)==False:
            b = random.randint(0,2)
            rand_buildings = list_of_building_lists[b]
            building_center  = list_of_building_points[b]
            print p
            print building_center
            vec = p - building_center
            for building in rand_buildings:
                ob = rs.CopyObject(building,vec)
                random_height = 0.4 * random.randint(1, 3)
                re_scaled = rs.ScaleObject(ob, forest_points[i], [1, 1, random_height], False)
                a.append(re_scaled)
        i = i + 1


def industrial():
    list_of_building_lists = []
    list_of_building_lists.append(industrial_b1)
    list_of_building_lists.append(industrial_b2)
    list_of_building_points = []
    list_of_building_points.append(industrial_p1)
    list_of_building_points.append(industrial_p2)


    i = 0
    for p in industrial_points:
        if IfOnRoad(p)==False:
            b = random.randint(0,1)
            rand_buildings = list_of_building_lists[b]
            building_center  = list_of_building_points[b]
            print p
            print building_center
            vec = p - building_center
            for building in rand_buildings:
                ob = rs.CopyObject(building,vec)
                if IsNeighbourWith(industrial_points[i], suburban_points)==True:
                    random_height = 0.6 * random.randint(1, 3)
                    random_width = 0.6 * random.randint(1, 2)
                    random_depth = 0.6 * random.randint(1, 2)
                    re_scaled = rs.ScaleObject(ob, industrial_points[i], [random_depth, random_width, random_height], False)
                    angles = rs.Angle(p, center_center)
                    angle = angles[0]
                    rs.RotateObject(re_scaled, p, angle)
                    a.append(re_scaled)
                else:
                    if IsNeighbourWith(industrial_points[i], center_points)==True:
                        random_height = 0.5 * random.randint(1, 2)
                        random_width = 0.5 * random.randint(1, 2)
                        random_depth = 0.5 * random.randint(1, 2)
                        re_scaled = rs.ScaleObject(ob, industrial_points[i], [random_depth, random_width, random_height], False)
                        angles = rs.Angle(p, center_center)
                        angle = angles[0]

                        rs.RotateObject(re_scaled, p, angle)
                        a.append(re_scaled)
                    else:
                        random_height = 0.9 * random.randint(1, 2)
                        random_width = 0.6 * random.randint(1, 2)
                        random_depth = 0.6 * random.randint(1, 2)
                        re_scaled = rs.ScaleObject(ob, industrial_points[i], [random_depth, random_width, random_height], False) 
                        angles = rs.Angle(p, center_center)
                        angle = angles[0]
                        rs.RotateObject(re_scaled, p, angle)
                        a.append(re_scaled)
        i = i + 1





def center():
    list_of_building_lists = []
    list_of_building_lists.append(buildings)
    list_of_building_lists.append(buildings2)
    list_of_building_points = []
    list_of_building_points.append(building_p)
    list_of_building_points.append(building_2)


    i = 0
    for p in center_points:
        if IfOnRoad(p)==False:
            b = random.randint(0,1)
            rand_buildings = list_of_building_lists[b]
            building_center  = list_of_building_points[b]
            vec = p - building_center
            for building in rand_buildings:
                ob = rs.CopyObject(building,vec)
                if IsNeighbourWith(center_points[i], suburban_points)==True:
                
                    random_height = 0.6 * random.randint(1, 3)
                    random_width = 0.6 * random.randint(1, 2)
                    random_depth = 0.6 * random.randint(1, 2)
                    re_scaled = rs.ScaleObject(ob, center_points[i], [random_depth, random_width, random_height], False)
                    angles = rs.Angle(p, center_center)
                    angle = angles[0]
                    rs.RotateObject(re_scaled, p, angle)
                    a.append(re_scaled)
                    a.append(re_scaled)
                else:
                    if IsNeighbourWith(center_points[i], industrial_points)==True:
                        random_height = 0.75 * random.randint(1, 3)
                        random_width = 0.75 * random.randint(1, 2)
                        random_depth = 0.75 * random.randint(1, 2)
                        re_scaled = rs.ScaleObject(ob, center_points[i], [random_depth, random_width, random_height], False)
                        angles = rs.Angle(p, center_center)
                        angle = angles[0]
                        rs.RotateObject(re_scaled, p, angle)
                        a.append(re_scaled)
                        a.append(re_scaled)
                    else:
                        random_height = 0.90 * random.randint(1, 3)
                        random_width = 0.90 * random.randint(1, 2)
                        random_depth = 0.90 * random.randint(1, 2)
                        re_scaled = rs.ScaleObject(ob, center_points[i], [random_depth, random_width, random_height], False) 
                        angles = rs.Angle(p, center_center)
                        angle = angles[0]
                        rs.RotateObject(re_scaled, p, angle)
                        a.append(re_scaled)
                        a.append(re_scaled)
        i = i + 1


def suburban():
    list_of_building_lists = []
    list_of_building_lists.append(suburban_b1)
    list_of_building_lists.append(suburban_b2)
    list_of_building_points = []
    list_of_building_points.append(suburban_p1)
    list_of_building_points.append(suburban_p2)


    i = 0
    for p in suburban_points:
        if IfOnRoad(p)==False:
            b = random.randint(0,1)
            rand_buildings = list_of_building_lists[b]
            building_center  = list_of_building_points[b]

            print building_center
            vec = p - building_center
            for building in rand_buildings:
                ob = rs.CopyObject(building,vec)
                if IsNeighbourWith(suburban_points[i], center_points)==True:
                
                    random_height =  random.randint(1, 2)
                    random_width =  random.randint(1, 2)
                    random_depth = random.randint(1, 2)
                    re_scaled = rs.ScaleObject(ob, suburban_points[i], [random_depth, random_width, random_height], False)
                    angles = rs.Angle(p, center_center)
                    angle = angles[0]

                    rs.RotateObject(re_scaled, p, angle)
                    a.append(re_scaled)
                    a.append(re_scaled)
                else:
                    if IsNeighbourWith(suburban_points[i], industrial_points)==True:
                        random_height = 0.6 * random.randint(1, 2)
                        random_width = 0.6 * random.randint(1, 2)
                        random_depth = 0.6 * random.randint(1, 2)
                        re_scaled = rs.ScaleObject(ob, suburban_points[i], [random_depth, random_width, random_height], False)
                        angles = rs.Angle(p, center_center)
                        angle = angles[0]
                        rs.RotateObject(re_scaled, p, angle)
                        a.append(re_scaled)
                        a.append(re_scaled)
                    else:
                        random_height = 0.7 * random.randint(1, 2)
                        random_width = 0.7 * random.randint(1, 2)
                        random_depth = 0.7 * random.randint(1, 2)
                        re_scaled = rs.ScaleObject(ob, suburban_points[i], [random_depth, random_width, random_height], False) 
                        angles = rs.Angle(p, center_center)
                        angle = angles[0]
                        rs.RotateObject(re_scaled, p, angle)
                        a.append(re_scaled)

        i = i + 1


def IsNeighbourWith(point, points):
    for point_b in points:
        dist = rs.Distance(point, point_b)
        if dist <= 7.0:
                return True
    return False

def Roads(start, IsBranch):
    if IsBranch == True:
        length = 6
    else:
        length = 10
    road_length = []
    start_list = []
    start_list.append(start)
    cont = True
    previous_start = start
    Road_points_used.append(start)
    previous_starts = []
    i = 0
    while cont:
        possible_dir = []
        nearest_points = rs.PointCloudClosestPoints(Road_points, start_list, 6)
        nearest_points_list = nearest_points[0]
        start_X = start_list[0].X
        start_Y = start_list[0].Y
        start_Z = start_list[0].Z
        s_point = start_list.pop()
        for p in nearest_points_list:
            X = Road_points[p].X
            Y = Road_points[p].Y
            Z = Road_points[p].Z
            if start_X != X and start_Y != Y and start_Z != Z:
                if start_X >= X or start_Y < Y:
                    if Road_points[p] not in Road_points_used:
                        possible_dir.append(Road_points[p])
        if len(possible_dir)==0:
            cont = False
        else:
            if random.randint(0, 100) < 5:
                if len(possible_dir)-1 <= 0:
                    break
                else:
                    crossroad_i = random.randint(0, len(possible_dir)-1)
                    crossroads_start = possible_dir[crossroad_i]
                    Road_points_used.append(crossroads_start)
                    road_length.append(crossroads_start)
                    print "crossroads!"
                    Road_lines.append(rs.AddLine(previous_start, crossroads_start))
                    if len(road_length)>= length:
                        cont = False
                    else:
                        Roads(crossroads_start, True)

            rand_dir = random.randint(0, len(possible_dir)-1)
            next_start = possible_dir[rand_dir]
            try:
                Road_lines.append(rs.AddLine(previous_start, next_start))
                previous_start = next_start
                start_list.append(next_start)
                Road_points_used.append(next_start)
                road_length.append(next_start)
                if len(road_length)>=length:
                    cont = False
            except:
                print("start and end can't be the same point")

def IfOnRoad(point):
    if Road_points_used.count(point)>0:
        return True
    return False

if __name__=="__main__":
    main()
