n=int(input())
list1=[]
count=0
for i in range(n):
    list1.append(input())
for i in range(n):
    if list1[i]=="Tetrahedron":
        count=count+4
    elif list1[i]=="Cube":
        count=count+6
    elif list1[i]=="Octahedron":
        count=count+8
    elif list1[i]=="Dodecahedron":
        count=count+12
    elif list1[i]=="Icosahedron":
        count=count+20
print(count)