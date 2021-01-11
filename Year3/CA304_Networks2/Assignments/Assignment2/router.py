import pandas as pd     # used for displaying routing table
# import networkx as nx
# import matplotlib.pyplot as plt
class Router:

    # initialising starting-router name and the graph (graph from Graph class)
    def __init__(self, name, graph):
        self.name = name
        self.graph = graph

    # performs Dijkstras algorithm
    def get_path(self, router_name):
        start = self.name   # router we start at
        goal = router_name   # goal is the router we want to reach
        shortestDistance = {}   # (updated throughout the program) tracks the cost to reach to the router
        routerPredecessors = {}   # tracks path that has led to current router
        # making shallow copy of self.graph dictionary so as to not affect self.graph
        unvisitedRouters = self.graph.copy()   # used to iterate graph to perform relaxation
        infinity = 9999999  # initially sets cost to other routers/nodes as infinity
        routerPath = []   # tracks the optimal path to start node/router

        # setting all cost to be infinity
        for router in unvisitedRouters:
            shortestDistance[router] = infinity
        shortestDistance[start] = 0     # except for start node

        # runs until we visited every router and performed relaxation
        # i.e. until unvisitedRouters is empty
        while unvisitedRouters.items():
            minRouterDistance = None  # initially no minimum cost

            # here we look for shortest distance to a router
            for router in unvisitedRouters:
                if minRouterDistance is None:
                    minRouterDistance = router
                elif shortestDistance[router] < shortestDistance[minRouterDistance]:
                    minRouterDistance = router  # sets minimum distance to router

            # now we look for possible paths we can take from minimum distance nodes/router
            for childRouter, weight in self.graph[minRouterDistance].items():
                # relaxation (updating cost of all nodes/routers if they can be improved)
                if weight + shortestDistance[minRouterDistance] < shortestDistance[childRouter]:
                    shortestDistance[childRouter] = weight + shortestDistance[minRouterDistance]
                    routerPredecessors[childRouter] = minRouterDistance   # update track leading to router
            unvisitedRouters.pop(minRouterDistance)   # pops router from the graph to end loop

        currRouter = goal    # currRouter used to track the path for start->goal
        while currRouter != start:
            try:
                routerPath.insert(0, currRouter)  # adds currRouter appended to start of path
                currRouter = routerPredecessors[currRouter]   # updates currRouter to predecessor router

            # if path not reachable, break from loop
            except KeyError:
                print("Path not found")
                break

        routerPath.insert(0, start)   # finally we insert starting router to path
        # if we reached the path to the goal router, output info
        try:
            if shortestDistance[goal] != infinity:
                return "Start: {}\nEnd: {}\nPath: {}\nCost: {}".format(
                    start, goal, "->".join(routerPath), shortestDistance[goal])
        # else the router was not found
        except KeyError:
            return "Goal router '{}' not found".format(goal)

    def print_routing_table(self):
        # initialising the start router
        start = self.name
        # relevant info about the path to each router from start appended for use of pandas
        fromList = []
        toList = []
        costList = []
        pathList = []
        # iterating the graph to get path from start router
        for router in self.graph.keys():
            # getting info about all other routers except itself (start router)
            if router != start:
                info = self.get_path(router).split()    # splitting the output from get_path
                # appending necessary parts from output to associated list
                fromList.append(info[1])
                toList.append(info[3])
                costList.append(info[7])
                pathList.append(info[5])

        # Anakin provides output to Jedi council, but gets denied rank of Master
        anakin = {"from":fromList, "to":toList, "cost":costList, "path":pathList}
        return pd.DataFrame.from_dict(anakin)

    # removes router/node from graph
    def remove_router(self, router_name):

        # first deleting the "from" router from graph (i.e. the router among the keys of graph)
        # e.g graph = {'a': {'b': 7, 'c': 9, 'f': 14}, 'b': {'a': 7, 'c': 10, 'd': 15}}
        # deleting "a", graph = {'b': {'a': 7, 'c': 10, 'd': 15}}
        self.graph.pop(router_name)
        # notice "a" in values of "b" (i.e "a":7), it's gotta go too..
        # then checking where that router is in the values of the graph
        for connections in self.graph.values():
            if router_name in connections:
                del connections[router_name]    # delete router if present in values
        # so now b would have {'b': {'c': 10, 'd': 15}}

        return self.print_routing_table()   # print updated routing table

class Graph:

    # initialising shared graph to class
    def __init__(self):
        self.graph = {}

    # adding an edge to graph to connect 2 routers
    def add_edge(self, router1, router2, cost):

        # if router not in graph, assigns it an empty mapping
        # then adds it to graph to map connected router
        if router1 not in self.graph:
            self.graph[router1] = {}
        self.graph[router1][router2] = cost

    # these methods allow for graph object to have dictionary methods
    # (since self.graph is recognised as "Graph" object outside class, rather than a dictionary)

    # allows for accessing dictionary entries
    def __getitem__(self, item):
        return self.graph[item] if item in self.graph else None

    # allows for iteration of dictionary
    def __iter__(self):
        return iter(self.graph)

    # returns shallow copy for dictionary
    def copy(self):
        return self.graph.copy()

    def values(self):
        return self.graph.values()

    # returns keys in dictionary
    def keys(self):
        return self.graph.keys()

    # returns items in dictionary
    def items(self):
        return self.graph.items()

    # pops item from dictionary and returns item
    def pop(self, item):
        return self.graph.pop(item)

# method to save graph to filename
def saveGraph(filename, graph):
    # imported it here to see if that prevents second graph from messing up (same problem)
    import networkx as nx
    import matplotlib.pyplot as plt
    g = nx.Graph()  # initialising a graph
    weightedEdges = []  # used for storing weighted edges (each item as a triple (router1, router2, cost))
    # then iterating graph to add router1 (from), router2 (to), and the cost
    for router1, connections in graph.items():
        # iterating through current router's connections
        for router2, cost in connections.items():
            weightedEdges.append((router1, router2, cost))

    # adding the connections to graph, then drawing it with node name displayed
    g.add_weighted_edges_from(weightedEdges)
    nx.draw(g, with_labels=True)

    # as described in README.txt, this doesn't work very well
    # labels = nx.get_edge_attributes(g, "weight")
    # pos = nx.spring_layout(g)
    # nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    
    # saving graph to png file (couldn't use plt.show(), didn't work for me :c )
    plt.savefig("{}.png".format(filename))

    return "Graph saved to {}.png in current directory".format(filename)

def main():

    # initialising graph and adding bidirectional paths to graph with cost
    graph = Graph()
    graph.add_edge("a", "b", 7)
    graph.add_edge("b", "a", 7)

    graph.add_edge("a", "c", 9)
    graph.add_edge("c", "a", 9)

    graph.add_edge("a", "f", 14)
    graph.add_edge("f", "a", 14)

    graph.add_edge("b", "c", 10)
    graph.add_edge("c", "b", 10)

    graph.add_edge("b", "d", 15)
    graph.add_edge("d", "b", 15)
    
    graph.add_edge("c", "d", 11)
    graph.add_edge("d", "c", 11)

    graph.add_edge("c", "f", 2)
    graph.add_edge("f", "c", 2)

    graph.add_edge("d", "e", 6)
    graph.add_edge("e", "d", 6)

    graph.add_edge("e", "f", 9)
    graph.add_edge("f", "e", 9)

    router1 = Router("a", graph)    # starting router1
    router2 = Router("b", graph)    # starting router2

    # showing graph before routers removed
    filename = "beforeDeletion"
    print(saveGraph(filename, graph))
    print()

     # prints router1 path to goal router, same for router2
    print(router1.get_path("f"))
    print()
    print(router2.get_path("d"))
    print()

    # printing routing table for router1 and router2
    print(router1.print_routing_table())
    print()
    print(router2.print_routing_table())
    print()

    # removing router "c" from routing table
    # both routers affected, "c" not in routing table
    print(router1.remove_router("c"))
    print()
    print(router2.print_routing_table())
    print()

    # likewise here for router "f"
    print(router2.remove_router("f"))
    print()
    print(router1.print_routing_table())
    print()

    # updating graph after routers removed (seems to merge with previous graph)
    filename = "afterDeletion"
    print(saveGraph(filename, graph))

if __name__ == '__main__':
    main()
