import * as d3 from "https://esm.sh/d3-geo@3";

async function render({ model, el }) {
  const countries = await fetch(
    "https://cdn.jsdelivr.net/gh/nvkelso/natural-earth-vector/geojson/ne_110m_admin_0_countries.geojson"
  ).then((res) => res.json());
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

  const naturalEarth = document.createElementNS("http://www.w3.org/2000/svg", "path");
  naturalEarth.setAttribute("d", path(countries));
  naturalEarth.setAttribute("fill", "none");
  naturalEarth.setAttribute("stroke", "black");
  svg.appendChild(naturalEarth);

  if (model.get("graticule")) {
    const graticule = document.createElementNS("http://www.w3.org/2000/svg", "path");
    graticule.setAttribute("d", path(d3.geoGraticule()()));
    graticule.setAttribute("fill", "none");
    graticule.setAttribute("stroke", "lightgray");
    graticule.setAttribute("opacity", "0.5");
    svg.appendChild(graticule);
  }

  el.appendChild(svg);
}

export default { render };
