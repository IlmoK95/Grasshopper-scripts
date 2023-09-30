"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "IlmoK"
__version__ = "2022.07.06"

import rhinoscriptsyntax as rs
import ghpythonlib.components as ghc


x_ax = []
point = []
routes = []
neg_Z = ghc.VectorXYZ(0, 0, -1)[0]


def main():
    for p_start in start_points:
        points = []
        points.append(p_start)
        p = ghc.ProjectPoint(p_start, neg_Z, object)[0]
        points.append(p)

        for x in range(0, steps):
            try:
                angle, normal, X_axis = GetAngle(p, object, neg_Z)
                print angle
                if angle <= sliding_angle:
                    points.append(p)
                    break
                elif angle > sliding_angle and angle <= drop_angle:
                    p = ProjectAlongNormal(X_axis, p, normal, object, points)
                    if p.Z == points[-1].Z:
                        p = ProjectVertically(p, neg_Z, object)
                    points.append(p)
                elif angle > drop_angle:
                    p_start = p
                    p = ProjectVertically(p, neg_Z, object)
                    if p==None:
                        p = ProjectVertically(p_start, neg_Z, floor)
                        points.append(p)
                        break
                    points.append(p)
            except Exception as e:
                print e
        routes.append( ghc.PolyLine(points, False))



def ProjectAlongNormal(X_axis, p, normal, object, points):

    p = ghc.Move(p, (X_axis*step_size+normal*(-0.05)))[0]
    p = ghc.MeshClosestPoint(p, object)[0]
    return p


def GetAngle(p, object, neg_Z):
    normal = normals[ghc.MeshClosestPoint(p, object)[1]]
    plane = ghc.PlaneNormal(p, normal)
    plane_aligned = ghc.AlignPlane(plane, neg_Z)[0]
    X_axis = ghc.DeconstructPlane(plane_aligned)[1]
    
    XY_plane = ghc.PlaneNormal(p, ghc.UnitZ(1))
    XY_plane_aligned = ghc.AlignPlane(XY_plane, X_axis)[0]
    XY_X_axis = ghc.DeconstructPlane(XY_plane_aligned)[1]
    angle = ghc.Degrees(ghc.Angle(X_axis, XY_X_axis)[0])
    angle = AngleCorrection( angle, normal)
    print angle
    return angle, normal, X_axis


def ProjectVertically(p, neg_Z, object_dc):
    p = ghc.Move(p, neg_Z*0.08)[0]
    p = ghc.ProjectPoint(p, neg_Z, object_dc)[0]
    return p


def AngleCorrection(angle, normal):
    Z_value = ghc.DeconstructVector(normal)[2]
    if Z_value < 0:
        return 180 - angle
    else:
        return angle


if __name__ == "__main__":
    main()
