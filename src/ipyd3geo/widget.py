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


class Map(anywidget.AnyWidget):
    _esm = """
    import * as d3 from "https://esm.sh/d3-geo@3";

    function render({ el }) {
      const path = d3.geoPath(d3.geoEqualEarth());

      const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
      const sphere = document.createElementNS("http://www.w3.org/2000/svg", "path");
      sphere.setAttribute("d", path({ type: "Sphere" }));
      svg.appendChild(sphere);
      el.appendChild(svg);
    }

    export default { render };
    """

    class Export:
        def __init__(self, map):
            self._map = map

        def svg(self, path):
            raise NotImplementedError

    def __init__(self, center=(0.0, 0.0), zoom=1.0, projection="geoEqualEarth", graticule=False, border=True):
        super().__init__()
        self.export = Map.Export(self)

    def add(self, layer):
        raise NotImplementedError

    def remove(self, layer):
        raise NotImplementedError