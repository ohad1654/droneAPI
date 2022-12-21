from Primitives.line import Line


class Route:
    def __init__(self, points):
        self._points = points

    def optimized(self, flat, depth):
        optimizedRoute = [self._points[0]]
        i = 1
        while i < len(self._points) - 1:
            optimizedVia = self._optimize_via(optimizedRoute[-1], self._points[i], self._points[i + 1], flat, depth)
            optimizedRoute += optimizedVia
            i += 1
        return Route(optimizedRoute + [self._points[-1]])

    def _optimize_via(self, startP, viaP, endP, flat, depth):
        if flat.is_connected(startP, endP):
            return []
        if depth <= 0:
            return [viaP]

        options = []
        middle1 = Line(startP, viaP).get_presentation()(0.5)
        middle2 = Line(viaP, endP).get_presentation()(0.5)
        flag = True
        if flat.is_connected(middle1, endP):
            options += [self._optimize_via(startP, middle1, endP, flat, depth - 1)]
            flag = False

        if flat.is_connected(startP, middle2):
            options += [self._optimize_via(startP, middle2, endP, flat, depth - 1)]
            flag = False

        if flag:
            if flat.is_connected(middle1, middle2):
                res = self._optimize_via(startP, middle1, middle2, flat, depth - 1)
                if flat.is_connected(res[-1], endP):
                    options += [res]
                else:
                    options += [res + [middle2]]

            else:

                res = self._optimize_via(middle1, viaP, endP, flat, depth - 1)
                if flat.is_connected(startP, res[0]):
                    options += [res]
                else:
                    options += [[middle1] + res]
        return min(options, key=lambda opt: Route([startP] + opt + [endP]).length())

    def length(self):
        length = 0
        for i in range(0, len(self._points) - 1):
            length += self._points[i].distance(self._points[i + 1])
        return length

    def get_points(self):
        return self._points
