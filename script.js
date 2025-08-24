const API = "http://127.0.0.1:8000";

let cyInstance = null;

document.getElementById("btn-graph").addEventListener("click", () => {
  const cy = cytoscape({
    container: document.getElementById("cy"),
    elements: [
      { data: { id: "frontend", label: "Frontend" } },
      { data: { id: "api", label: "API" } },
      { data: { id: "db", label: "DB" } },
      { data: { source: "frontend", target: "api" } },
      { data: { source: "api", target: "db" } },
    ],
    style: [
      { selector: "node", style: { label: "data(label)", "text-valign": "center", "text-halign": "center", "background-color": "#0077cc", color: "#fff" } },
      { selector: "edge", style: { width: 2, "line-style": "solid" } },
    ],
    layout: { name: "grid" },
  });
  cyInstance = cy;
});

document.getElementById("btn-load-vulns").addEventListener("click", async () => {
  const target = document.getElementById("vulns");
  target.innerHTML = "<em>Carregando...</em>";
  try {
    const res = await fetch(`${API}/vulns`);
    const data = await res.json();
    target.innerHTML = "";
    data.forEach(v => {
      const el = document.createElement("div");
      el.className = "vuln";
      el.innerHTML = `<h4>[${v.severidade}] ${v.titulo}</h4><p>${v.descricao}</p><small>Categoria: ${v.categoria}</small>`;
      target.appendChild(el);
    });
  } catch (e) {
    target.innerHTML = `<span style="color:#b00">Erro ao carregar: ${e}</span>`;
  }
});
