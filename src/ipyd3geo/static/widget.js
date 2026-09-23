import * as d3 from "https://esm.sh/d3-geo@3";

function render({ model, el }) {
  const path = d3.geoPath(d3[model.get("projection")]());

  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("viewBox", "0 0 960 500");
  svg.setAttribute("width", "960");
  svg.setAttribute("height", "500");
  const sphere = document.createElementNS("http://www.w3.org/2000/svg", "path");
  sphere.setAttribute("d", path({ type: "Sphere" }));
  sphere.setAttribute("fill", "none");
  sphere.setAttribute("stroke", model.get("border") ? "black" : "none");
  svg.appendChild(sphere);

  if (model.get("graticule")) {
    const graticule = document.createElementNS("http://www.w3.org/2000/svg", "path");
    graticule.setAttribute("d", path(d3.geoGraticule()()));
    graticule.setAttribute("fill", "none");
    graticule.setAttribute("stroke", "lightgray");
    svg.appendChild(graticule);
  }

  el.appendChild(svg);
}

export default { render };
