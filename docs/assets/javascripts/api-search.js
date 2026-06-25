(function () {
  const slug = (value) => {
    const cleaned = String(value || "").replace(/[^A-Za-z0-9_.-]+/g, "-").replace(/^-+|-+$/g, "");
    return cleaned || "symbol";
  };

  const escapeHtml = (value) => String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");

  const flattenReference = (reference) => {
    const rows = [];
    for (const [packageId, packageData] of Object.entries(reference.packages || {})) {
      for (const symbol of packageData.symbols || []) {
        const symbolPath = `${packageId}/${slug(symbol.name)}/`;
        rows.push({
          name: symbol.name,
          kind: symbol.kind,
          category: symbol.category,
          packageTitle: packageData.title,
          summary: symbol.summary || symbol.remarks || "",
          href: symbolPath,
          haystack: [packageData.title, symbol.name, symbol.kind, symbol.category, symbol.summary, symbol.signature].join(" ").toLowerCase(),
        });
        for (const member of symbol.methods || []) {
          rows.push({
            name: `${symbol.name}.${member.name}`,
            kind: member.kind,
            category: member.category,
            packageTitle: packageData.title,
            summary: member.summary || member.remarks || "",
            href: `${symbolPath}#${member.kind}-${slug(member.name).toLowerCase()}`,
            haystack: [packageData.title, symbol.name, member.name, member.kind, member.category, member.summary, member.signature, member.parameters, member.returns].join(" ").toLowerCase(),
          });
        }
      }
    }
    return rows;
  };

  const renderResults = (target, rows, query) => {
    if (!query) {
      target.innerHTML = "";
      return;
    }
    const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
    const matches = rows
      .map((row) => ({
        row,
        score: terms.reduce((total, term) => total + (row.haystack.includes(term) ? 1 : 0), 0),
      }))
      .filter((item) => item.score === terms.length)
      .slice(0, 20)
      .map(({ row }) => row);
    if (!matches.length) {
      target.innerHTML = '<p class="helios-api-search-empty">No API entries matched.</p>';
      return;
    }
    target.innerHTML = matches.map((row) => `
      <a class="helios-api-search-result" href="${escapeHtml(row.href)}">
        <span>${escapeHtml(row.packageTitle)} / ${escapeHtml(row.category || row.kind)}</span>
        <strong>${escapeHtml(row.name)}</strong>
        <em>${escapeHtml(row.summary || "Source annotation available in the generated reference.")}</em>
      </a>
    `).join("");
  };

  const initApiSearch = async () => {
    const root = document.querySelector("[data-api-search]");
    if (!root || root.dataset.initialized === "true") return;
    root.dataset.initialized = "true";
    const input = root.querySelector("input[type='search']");
    const results = root.querySelector("[data-api-search-results]");
    if (!input || !results) return;
    try {
      const response = await fetch("reference.json", { credentials: "same-origin" });
      if (!response.ok) throw new Error(`reference.json ${response.status}`);
      const rows = flattenReference(await response.json());
      input.addEventListener("input", () => renderResults(results, rows, input.value.trim()));
    } catch (error) {
      results.innerHTML = '<p class="helios-api-search-empty">API search index is unavailable in this build.</p>';
    }
  };

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(initApiSearch);
  } else {
    document.addEventListener("DOMContentLoaded", initApiSearch);
  }
})();
