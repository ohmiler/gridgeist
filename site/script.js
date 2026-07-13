const hero = document.querySelector('.hero');
const coordinate = document.querySelector('.coordinate');

hero?.addEventListener('pointermove', (event) => {
  const bounds = hero.getBoundingClientRect();
  const x = Math.max(0, Math.min(100, ((event.clientX - bounds.left) / bounds.width) * 100));
  const y = Math.max(0, Math.min(100, ((event.clientY - bounds.top) / bounds.height) * 100));
  hero.style.setProperty('--pointer-x', `${x}%`);
  hero.style.setProperty('--pointer-y', `${y}%`);
  if (coordinate) coordinate.textContent = `X ${Math.round(x).toString().padStart(2, '0')} / Y ${Math.round(y).toString().padStart(2, '0')}`;
});

const demo = document.querySelector('.demo');
const viewButtons = document.querySelectorAll('[data-view]');

viewButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const view = button.dataset.view;
    demo.dataset.state = view;
    viewButtons.forEach((candidate) => candidate.setAttribute('aria-pressed', String(candidate === button)));
    demo.querySelector('.demo-before').setAttribute('aria-hidden', String(view !== 'before'));
    demo.querySelector('.demo-after').setAttribute('aria-hidden', String(view !== 'after'));
    document.querySelector('.demo-status').textContent = view === 'after' ? 'SYSTEMIC' : 'GENERIC';
  });
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach((section) => observer.observe(section));

document.querySelector('.copy-button')?.addEventListener('click', async (event) => {
  const button = event.currentTarget;
  try {
    await navigator.clipboard.writeText(button.dataset.copy);
    button.textContent = 'Copied';
    button.classList.add('copied');
    window.setTimeout(() => {
      button.textContent = 'Copy';
      button.classList.remove('copied');
    }, 1800);
  } catch {
    button.textContent = 'Select command';
  }
});
