// Roteador simples: alterna seções <section id="page-*">
(function () {
  const pages = ['home', 'caixa', 'media', 'cpf'];

  function go(route) {
    pages.forEach(p => {
      const el = document.getElementById('page-' + p);
      if (el) el.classList.toggle('hidden', p !== route);
    });
    document.querySelectorAll('nav a').forEach(a => {
      a.classList.toggle('active', a.dataset.route === route);
    });
    window.scrollTo(0, 0);
  }

  document.querySelectorAll('[data-route]').forEach(el => {
    el.addEventListener('click', e => {
      e.preventDefault();
      go(el.dataset.route);
    });
  });

  // Helper global para mostrar mensagens
  window.showMsg = function (el, type, text) {
    el.innerHTML = `<div class="msg ${type}">${text}</div>`;
  };

  go('home');
})();
