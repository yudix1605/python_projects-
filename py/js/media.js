// Calculadora de Média
(function () {
  let notas = ['', ''];

  const $list  = document.getElementById('notas-list');
  const $media = document.getElementById('media-valor');
  const $badge = document.getElementById('media-badge');

  function renderNotas() {
    $list.innerHTML = notas.map((n, i) => `
      <div class="nota-row">
        <span>Nota ${i + 1}</span>
        <input type="number" data-i="${i}" value="${n}" placeholder="0,0" step="0.1"/>
        ${notas.length > 1 ? `<button class="x" data-rm="${i}" aria-label="Remover">✕</button>` : ''}
      </div>`).join('');

    $list.querySelectorAll('input').forEach(inp => {
      inp.oninput = e => {
        notas[+inp.dataset.i] = e.target.value;
        calcMedia();
      };
    });

    $list.querySelectorAll('[data-rm]').forEach(b => {
      b.onclick = () => {
        notas.splice(+b.dataset.rm, 1);
        renderNotas();
        calcMedia();
      };
    });
  }

  function calcMedia() {
    const nums = notas.map(parseFloat).filter(n => !isNaN(n));
    const m = nums.length ? nums.reduce((a, b) => a + b, 0) / nums.length : 0;
    $media.textContent = m.toFixed(2);

    if (!nums.length) { $badge.innerHTML = ''; return; }
    const ok = m >= 7;
    $badge.innerHTML = `<span class="badge ${ok ? 'success' : 'error'}">${ok ? 'Aprovado 🎉' : 'Abaixo da média'}</span>`;
  }

  document.getElementById('add-nota').onclick = () => {
    notas.push('');
    renderNotas();
  };

  renderNotas();
  calcMedia();
})();
