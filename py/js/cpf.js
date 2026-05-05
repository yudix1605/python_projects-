// Validador de CPF
(function () {
  const $cpf  = document.getElementById('cpf-input');
  const $btn  = document.getElementById('btn-cpf');
  const $msg  = document.getElementById('msg-cpf');

  function fmt(v) {
    const d = v.replace(/\D/g, '').slice(0, 11);
    return d
      .replace(/(\d{3})(\d)/, '$1.$2')
      .replace(/(\d{3})(\d)/, '$1.$2')
      .replace(/(\d{3})(\d{1,2})$/, '$1-$2');
  }

  function validarCPF(input) {
    const cpf = input.replace(/\D/g, '');
    if (cpf.length !== 11 || /^(\d)\1+$/.test(cpf)) return false;

    const calc = base => {
      let s = 0;
      for (let i = 0; i < base; i++) s += parseInt(cpf[i]) * (base + 1 - i);
      const d = (s * 10) % 11;
      return d === 10 ? 0 : d;
    };

    return calc(9) === +cpf[9] && calc(10) === +cpf[10];
  }

  $cpf.oninput = () => {
    $cpf.value = fmt($cpf.value);
    $btn.disabled = $cpf.value.replace(/\D/g, '').length !== 11;
    $msg.innerHTML = '';
  };

  $btn.onclick = () => {
    const ok = validarCPF($cpf.value);
    showMsg($msg, ok ? 'success' : 'error', ok ? '✓ CPF válido!' : '✗ CPF inválido. Tente novamente.');
  };
})();
