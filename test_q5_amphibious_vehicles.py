import cmath
import sys

def is_P_InSegment_P0P1(P, P0,P1):
    p0 = P0[0]- P[0], P0[1]- P[1]
    p1 = P1[0]- P[0], P1[1]- P[1]
    det = (p0[0]*p1[1] - p1[0]*p0[1])
    prod = (p0[0]*p1[0] + p0[1]*p1[1])
    return (det == 0 and prod < 0) or (p0[0] == 0 and p0[1] == 0) or (p1[0] == 0 and p1[1] == 0)

def isInsidePolygon(P: tuple, Vertices: list, validBorder=False) -> bool:
    sum_ = complex(0,0)
    for i in range(1, len(Vertices) + 1):
        v0, v1 = Vertices[i-1] , Vertices[i%len(Vertices)]
        if is_P_InSegment_P0P1(P,v0,v1):
            return validBorder, True
        sum_ += cmath.log( (complex(*v1) - complex(*P)) / (complex(*v0) - complex(*P)) )
    return abs(sum_) > 1, False

def lines_intersect(line1, polygon):
    intersect=False
    x1, y1, x2, y2 = line1
    no_of_sides = len(polygon)
    for index, side in enumerate(polygon):
        x3, y3 = side
        x4, y4 = polygon[(index+1)%no_of_sides]


        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            intersect = False  # lines are parallel
            continue
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if 0 <= t <= 1 and 0 <= u <= 1:
            return True
    return False

logs = sys.stdin.readlines()

no_of_veh = int(logs[0])
vehs = logs[1:1+no_of_veh]
vehs = [tuple([int(a) for a in coords.split()]) for coords in vehs]
no_of_polygons = int(logs[1+no_of_veh])

polygons = logs[2+no_of_veh:]
polygon_count = no_of_polygons

polygons_reorg = []
index = 0
while polygon_count != 0:
    no_of_sides = int(polygons[index])
    new_polygon = [list([int(a) for a in coords.split()]) for coords in polygons[1+index:1+index+no_of_sides]]
    polygons_reorg.append(new_polygon)
    index+=(no_of_sides+1)
    polygon_count-=1
    
for veh in vehs:
    x1, y1, x2, y2 = veh
    output = "Sea"
    for polygon in polygons_reorg:
        if lines_intersect(veh, polygon):
            output='Land/Sea'
            break

        front_on_land, front_on_border = isInsidePolygon((veh[0], veh[1]), polygon)
        rear_on_land, rear_on_border = isInsidePolygon((veh[2], veh[3]), polygon)
        if front_on_border or rear_on_border:
            output='Land/Sea'
            break
        if front_on_land and rear_on_land:
            output = 'Land'
            break
    print(output)