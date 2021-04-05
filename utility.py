from collections import namedtuple

def find_actual_bbox_value(x1, y1, x2, y2, img):
      
    x1 = int(x1 * img.shape[0])
    y1 = int(y1 * img.shape[1])
    x2 = x1 + int(x2 * img.shape[0])
    y2 = y1 + int(y2 * img.shape[1])
    
    return x1, y1, x2, y2 

def find_center(x1, x2, y1, y2) :
    Point = namedtuple('Point', 'x y')
    center = Point((x1+x2)/2, (y1+y2)/2)
    return center

def adaptive_gun_detection(list1, list2):

    strong_gun_detection = []
    for i in range(len(list1)):
        center = find_center(list1[i][0], list1[i][1], list1[i][2], list1[i][3])
        for j in range(len(list2)):
            if find_box_in_box(list2[j][0], list2[j][1], list2[j][2], list2[j][3], center.x, center.y): 
                strong_gun_detection.append([list1[i][0], list1[i][1], list1[i][2], list1[i][3]])
                break 
    
    return strong_gun_detection

def find_box_in_box(x1, y1, x2, y2, x, y) :
    if (x > x1 and x < x2 and y > y1 and y < y2) :
        return True
    else :
        return False




# list1 = []
# list2 = []

# strong_gun = []

# list1.append([1,33,54,5])
# list2.append([13,33,54,5])
# list1.append([19,32,54,5])
# list1.append([11,3,54,5])

# list2.append([22,4,3,5])
# list2.append([151, 98, 195, 247])

# list2.append([12,4,3,5])
# list2.append([232,4,3,5])
# list2.append([422,4,3,5])

# list1.append([152, 152, 163, 179])
# list1.append([154, 156, 163, 179])

# list1.append([19,32,54,5])
# list1.append([11,3,54,5])

# print("Strong_gun: " , adaptive_gun_detection(list1, list2))