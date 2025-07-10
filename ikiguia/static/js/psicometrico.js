document.addEventListener('DOMContentLoaded', () => {
  const steps     = Array.from(document.querySelectorAll('.steps .step'));
  const prevBtn   = document.getElementById('prevBtn');
  const nextBtn   = document.getElementById('nextBtn');
  const submitBtn = document.getElementById('submitBtn');
  const progress  = document.getElementById('progressBar');
  let current     = 0;

  function updateUI() {
    steps.forEach((el, i) => el.classList.toggle('active', i === current));
    prevBtn.style.visibility   = current === 0                 ? 'hidden' : 'visible';
    nextBtn.style.display      = current === steps.length - 1  ? 'none'   : 'inline-block';
    submitBtn.style.display    = current === steps.length - 1  ? 'inline-block' : 'none';
    progress.style.width       = `${((current + 1) / steps.length) * 100}%`;
  }

  prevBtn.addEventListener('click', e => {
    e.preventDefault();
    if (current > 0) current--, updateUI();
  });

  nextBtn.addEventListener('click', e => {
    e.preventDefault();
    if (current < steps.length - 1) current++, updateUI();
  });

  // Inicializa
  updateUI();
});
