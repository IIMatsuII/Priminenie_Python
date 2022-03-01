objects = [1,1,2,2,3,3,4,5]
def fun_1():
    conter = 0
    if len(objects) != 0:
        cont = []
        for obj in objects:
            if obj not in cont:
                cont.append(obj)
                conter += 1
    print(cont)
    print(conter)
    print(id(cont))

fun_1()