data = [
    (1, "Alice", 22,"ICT", 20000),
    (2, "Bob", 24, "ECE",21000),
    (3, "Charlie", 23,"MECH", 20500),
    (4, "David", 21, "CS",19900),
    (5, "Eve", 25, "MECH",22000),
    (6, "Frank", 22, "ECE",20050),
    (7, "Grace", 23, "ICT",20510),
    (8, "Hannah", 21, "CS",19850),
    (9, "Ivy", 24, "ECE",21030),
    (10, "Jack", 20, "MECH",19500)
]
def dept(s,data):
    for i in data:
        if s in i:
            print(f"name:{i[1]} | Dept. : {i[3]}")
def sortingemp(slaray,data):
    l=[]
    for i in data:
        l.append(i[4])
    l.sort(reverse=True)
    for i in l:
        for j in data:
            if j[4]== i:
                print(j)
def updatesal(toup,id,data):
    data1=[]
    for i in data :
        data1.append(list(i))

    for i in data1:
        if i[0]==id:
            i[4]=toup

