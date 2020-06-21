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
            if [v, origin] not in E:    # avoids keeping and arch already present in the list
                E.append([origin, v])

    return Graph(V, E)

def file_to_minimum(file_path):
    f = open(file_path, 'r')
    file_lines = f.readlines()
    return file_lines[0]
