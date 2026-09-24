import inspect
import pathlib

import anywidget
import traitlets

class Map(anywidget.AnyWidget):
    """Defines a D3-Geo backed map widget for Jupyter notebooks.

    Args:
        center (tuple): center of the map (longitude, latitude). **Not implemented yet.**
        zoom (float): The zoom level of the map. **Not implemented yet.**
        projection (Projection or str): The projection to use for the map. If a string is provided, it will be used to create a Projection object. Defaults to "geoEqualEarth".
        graticule (bool): Whether to show the graticule.
        border (bool): Whether to draw a border frame around the map.
        basemap (str): The basemap to use. **Not implemented yet. Currently defaults to Natural Earth small scale borders.**
        hamburger (bool): Whether to show the hamburger menu. **Not implemented yet.**
        draggable (bool): Whether the map is dynamically draggable. **Not implemented yet.**
    """

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
        """Add a layer to the map. **Not implemented yet.**"""
        raise NotImplementedError

    def remove(self, layer):
        """Remove a layer from the map. **Not implemented yet.**"""
        raise NotImplementedError

Map.__signature__ = inspect.Signature(list(inspect.signature(Map.__init__).parameters.values())[1:])

class Projection:
    """Defines a D3-Geo projection for the map widget.

    Args:
        name (str): The name of the projection. Defaults to "geoEqualEarth". See `d3-geo geoProjection docs <https://d3js.org/d3-geo/projection#geoProjection>`_ for options.
        rotate (tuple): The rotation of the projection.
        center (tuple): The center of the projection.
        precision (float): The precision of the projection.
        parallels (tuple): The parallels of the projection. Only applicable for conic projections.
    """
    def __init__(self, name="geoEqualEarth", rotate=(0, 0, 0), center=None, precision=None, parallels=None):
        self.name = name
        self.rotate = tuple(rotate)
        self.center = center
        self.precision = precision
        self.parallels = parallels

class Layer:
    """Base class for all layers in the map widget.

    Args:
        name (str): The name of the layer.
    """
    def __init__(self, name=""):
        self.name = name

class Point(Layer):
    """A point layer on the map. **Not implemented yet.**"""
    def __init__(self, location, color="#3388ff", name=""):
        raise NotImplementedError

class Polygon(Layer):
    """A polygon layer on the map. **Not implemented yet.**"""
    def __init__(self, locations, color="#3388ff", fill_color="#3388ff", name=""):
        raise NotImplementedError

class Line(Layer):
    """A line layer on the map. **Not implemented yet.**"""
    def __init__(self, locations, color="#3388ff", name=""):
        raise NotImplementedError

class GeoJSON(Layer):
    """A GeoJSON layer on the map. **Not implemented yet.**"""
    def __init__(self, data, name=""):
        raise NotImplementedError

class GeoData(Layer):
    """A GeoDataFrame (such as from geopandas) layer on the map. **Not implemented yet.**"""
    def __init__(self, data, name=""):
        raise NotImplementedError

class Raster(Layer):
    """A local raster layer on the map. **Not implemented yet.**"""
    def __init__(self, data, name=""):
        raise NotImplementedError

class TileService(Layer):
    """Raster tiles from a service. **Not implemented yet.**"""
    def __init__(self, url, name=""):
        raise NotImplementedError

if __name__ == "__main__":
    pass