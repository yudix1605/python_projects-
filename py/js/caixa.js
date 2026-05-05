// Caixa Eletrônico
(function () {
  let saldo = 2000;

  const $saldo = document.getElementById('saldo');
  const $valor = document.getElementById('valor-caixa');
  const $msg   = document.getElementById('msg-caixa');

  function renderSaldo() {
    $saldo.textContent = 'R$ ' + saldo.toFixed(2);
  }

  document.getElementById('btn-depositar').onclick = () => {
    const v = parseFloat($valor.value);
    if (!v || v <= 0) return showMsg($msg, 'error', 'Valor inválido. Tente novamente.');
    saldo += v;
    renderSaldo();
    $valor.value = '';
    showMsg($msg, 'success', `Depósito de R$ ${v.toFixed(2)} realizado!`);
  };

  document.getElementById('btn-sacar').onclick = () => {
    const v = parseFloat($valor.value);
    if (!v || v <= 0) return showMsg($msg, 'error', 'Valor não disponível.');
    if (v > saldo)    return showMsg($msg, 'error', 'Valor maior que o saldo atual.');
    saldo -= v;
    renderSaldo();
    $valor.value = '';
    showMsg($msg, 'success', `Saque de R$ ${v.toFixed(2)} realizado com sucesso!`);
  };

  renderSaldo();
})();
