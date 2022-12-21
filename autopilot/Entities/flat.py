import pickle
from route import Route
from autopilot.Primitives.graph import Graph
from wall import Wall


class Flat:

    def __init__(self):
        super().__init__()
        self._walls = []
        self._points = []
        self._graph = Graph()

    def load_walls(self, fileName):
        try:
            walls_f = open(fileName, 'rb')
            walls = pickle.load(walls_f)
            walls_f.close()
            for wall in walls:
                self.add_wall(wall)
        except FileExistsError or EOFError:
            print("Can't read " + fileName)

    def add_wall(self, wall):
        if wall not in self._walls:
            for line in self._graph.all_edges():
                if wall.is_intersect(line.point1, line.point2):
                    self._graph.remove_edge((line.point1, line.point2))
                    try:
                        self._graph.dijkstra(line.point1, line.point2)
                    except:
                        # wall is blcking the only way between tow points; cant add it.
                        self._graph.add_edge((line.point1, line.point2))
                        return
            self._walls.append(wall)

    def remove_wall(self, wall):
        self._walls.remove(wall)
        for point1 in self._graph.all_vertices():
            for point2 in self._graph.all_vertices():
                if point1 != point2 and self.is_connected(point1, point2):
                    self._graph.add_edge((point1, point2))

    def get_walls(self):
        return self._walls

    def save_walls(self, fileName):
        walls_f = open(fileName, 'wb')
        pickle.dump(self._walls, walls_f)
        walls_f.close()

    def load_points(self, fileName):
        try:
            points_f = open(fileName, 'rb')
            for p in pickle.load(points_f):
                self.add_point(p)
            points_f.close()
        except FileExistsError or EOFError:
            print("Can't read " + fileName)

    def add_point(self, point):
        if point not in self._points and (self.is_reachable(point) or self.get_points() == []):
            self._graph.add_vertex(point)
            for connected in self.get_reachable_points(point):
                self._graph.add_edge((point, connected))

            self._points.append(point)

    def save_points(self, fileName):
        points_f = open(fileName, 'wb')
        pickle.dump(self._points, points_f)
        points_f.close()

    def remove_point(self, point):
        if all(len(self._graph.edges(connected)) > 1 for connected in self._graph.edges(point)):
            self._points.remove(point)
            self._graph.remove_vertex(point)

    def get_points(self):
        return self._points

    def is_connected(self, point1, point2):
        for wall in self._walls:
            if wall.is_intersect(point1, point2):
                return False
        return True

    def create_route(self, startP, endP):
        self.add_point(startP)
        self.add_point(endP)
        route = Route(self._graph.dijkstra(startP, endP))
        self.remove_point(startP)
        self.remove_point(endP)
        return route

    def get_reachable_points(self, point, points=None):
        if points is None:
            points = self._points
        return [reachable for reachable in points if self.is_connected(point, reachable)]

    def is_reachable(self, point, points=None):
        if points is None:
            points = self._points
        for p in points:
            if self.is_connected(point, p):
                return True
        return False

    def to_blueprint(self, with_graph=False, with_dead_spots=False):
        blueprint = Blueprint().create(1000, 1500)
        blueprint.add_walls(self.get_walls())
        if with_graph:
            blueprint.add_marks(self.get_points(), 10, (0, 255, 0))
            edges = self._graph.all_edges()
            blueprint.add_walls([Wall(edge.point1, edge.point2, 3) for edge in edges], (0, 0, 255))

        if with_dead_spots:
            blueprint.mark_all(lambda point: not self.is_reachable(point), 5)
        return blueprint
