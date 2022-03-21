# put your python code here
a = int(input())  # Вводим глобальную переменную котороая отвечает за количество циклов и запросов
scop = {"global": {"funcs": [], "vars": []}}  # Вводим словарь для того что бы можно было состовлять запросы

def add(scop, curr_name, what):  # Функция запроса
    if curr_name not in scop:
        scop[curr_name] = {}
        scop[curr_name]["vars"] = []
        scop[curr_name]["vars"].append(what)
    else:
        if "vars" not in scop[curr_name]:
            scop[curr_name]["vars"] = []
            scop[curr_name]["vars"].append(what)
        else:
            scop[curr_name]["vars"].append(what)


def create(scop, curr_name, parent_name):
    if curr_name is not scop:
        scop[curr_name] = {}
        scop[curr_name]["funcs"] = []
        scop[curr_name]["vars"] = []
        scop[curr_name]["funcs"].append(curr_name)
        scop[curr_name]["parent"] = parent_name
    else:
        if "funcs" not in scop[curr_name]:
            scop[curr_name]["funcs"] = []
            scop[curr_name]["parent"] = parent_name
            scop[curr_name]["funcs"].append(curr_name)
        else:
            scop[curr_name]["funcs"].append(curr_name)
            scop[parent_name]["funcs"].append(curr_name)


def search(scop, name_sp, what):
    if what in scop[name_sp]["vars"]:
        return name_sp
    else:
        try:
            upper_name = scop[name_sp]["parent"]
        except KeyError:
            return None
        return search(scop, upper_name, what)


for i in range(a):
    comm = input().split()
    if comm[0] == "add":
        add(scop, comm[1], comm[2])
    elif comm[0] == "create":
        create(scop, comm[1], comm[2])
    elif comm[0] == "get":
        print(search(scop, comm[1], comm[2]))
