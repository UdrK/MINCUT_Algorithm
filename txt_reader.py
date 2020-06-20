from graph import Graph

def file_to_graph(file_path):
    f = open(file_path, 'r')
    file_lines = f.readlines()
    E = []
    V = []
    for fl in file_lines:
        values = fl.split()
        origin = values.pop(0)
        V.append(origin)
        for v in values:
            if [v, origin] not in E: # evito di inserire un arco già inserito
                E.append([origin, v])

    return Graph(V, E)
