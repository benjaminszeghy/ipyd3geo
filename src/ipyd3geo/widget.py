import pathlib

import anywidget
import traitlets

class Layer:
    def __init__(self, name=""):
        raise NotImplementedError

class point(Layer):
    def __init__(self, location, color="#3388ff", name=""):
        raise NotImplementedError

class Polygon(Layer):
    def __init__(self, locations, color="#3388ff", fill_color="#3388ff", name=""):
        raise NotImplementedError

class Line(Layer):
    def __init__(self, locations, color="#3388ff", name=""):
        raise NotImplementedError

class GeoJSON(Layer):
    def __init__(self, data, name=""):
        raise NotImplementedError

class Projection:
    def __init__(self, name="geoEqualEarth", rotate=(0, 0, 0), center=None, precision=None, parallels=None):
        self.name = name
        self.rotate = tuple(rotate)
        self.center = center
        self.precision = precision
        self.parallels = parallels


class Map(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"

    projection = traitlets.Unicode("geoEqualEarth").tag(sync=True)
    border = traitlets.Bool(True).tag(sync=True)
    graticule = traitlets.Bool(False).tag(sync=True)
    projection_rotate = traitlets.Tuple(traitlets.Float(), traitlets.Float(), traitlets.Float(), default_value=(0, 0, 0)).tag(sync=True)
    projection_center = traitlets.Tuple(traitlets.Float(), traitlets.Float(), allow_none=True, default_value=None).tag(sync=True)
    projection_precision = traitlets.Float(allow_none=True, default_value=None).tag(sync=True)
    projection_parallels = traitlets.Tuple(traitlets.Float(), traitlets.Float(), allow_none=True, default_value=None).tag(sync=True)

    class Export:
        def __init__(self, map):
            self._map = map

        def svg(self, path):
            raise NotImplementedError

    def __init__(self, center=(0.0, 0.0), zoom=1.0, projection=None, graticule=False, border=True, basemap="naturalearth", hamburger=True, draggable=False):
        if center != (0.0, 0.0):
            raise NotImplementedError
        if zoom != 1.0:
            raise NotImplementedError
        if draggable is not False:
            raise NotImplementedError
        if hamburger is not True:
            raise NotImplementedError
        if basemap != "naturalearth":
            raise NotImplementedError
        if projection is None:
            projection = Projection()
        elif isinstance(projection, str):
            projection = Projection(projection)
        super().__init__()
        self.projection = projection.name
        self.projection_rotate = projection.rotate
        self.projection_center = projection.center
        self.projection_precision = projection.precision
        self.projection_parallels = projection.parallels
        self.border = border
        self.graticule = graticule
        self.export = Map.Export(self)

    def add(self, layer):
        raise NotImplementedError

    def remove(self, layer):
        raise NotImplementedError