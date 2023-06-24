input_file = open("Input_file.txt", "r")
heuristic = {}
city = {}

for line in input_file:
    line = line.split()
    heuristic[line[0]] = int(line[1])
    destinations = []
    for i in range(2, len(line), 2):
        destinations.append((line[i], int(line[i + 1])))
    city[line[0]] = destinations


def A_star_search(start_node, stop_node):
    open_list = {start_node}
    closed_list = set([])
    g = {start_node: 0}
    parents = {start_node: start_node}

    while len(open_list) > 0:
        n = None
        for v in open_list:
            if n is None or g[v] + heuristic[v] < g[n] + heuristic[n]:
                n = v
        if n is None:
            print("NO PATH FOUND")
            return None
        if n == stop_node:
            result_path = []
            while parents[n] != n:
                result_path.append(n)
                n = parents[n]
            result_path.append(start_node)
            result_path.reverse()
            print("Path: {}".format(" -> ".join(result_path)))
            print("Total distance: {} km".format(g[stop_node]))
            return result_path
        for (m, weight) in city[n]:
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)
        open_list.remove(n)
        closed_list.add(n)

    print("NO PATH FOUND")
    return None


start = input("Start node: ")
destination = input("Destination: ")
A_star_search(start, destination)