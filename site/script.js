const hero = document.querySelector('.hero');
const coordinate = document.querySelector('.coordinate');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const finePointer = window.matchMedia('(pointer: fine)');

const updateHeroAxes = (event) => {
  const bounds = hero.getBoundingClientRect();
  const x = Math.max(0, Math.min(100, ((event.clientX - bounds.left) / bounds.width) * 100));
  const y = Math.max(0, Math.min(100, ((event.clientY - bounds.top) / bounds.height) * 100));
  hero.style.setProperty('--pointer-x', `${x}%`);
  hero.style.setProperty('--pointer-y', `${y}%`);
  if (coordinate) coordinate.textContent = `X ${Math.round(x).toString().padStart(2, '0')} / Y ${Math.round(y).toString().padStart(2, '0')}`;
};

const syncHeroTracking = () => {
  hero?.removeEventListener('pointermove', updateHeroAxes);
  if (!hero) return;
  if (!reducedMotion.matches && finePointer.matches) {
    hero.addEventListener('pointermove', updateHeroAxes);
    return;
  }
  hero.style.removeProperty('--pointer-x');
  hero.style.removeProperty('--pointer-y');
  if (coordinate) coordinate.textContent = 'X 00 / Y 00';
};

syncHeroTracking();
reducedMotion.addEventListener?.('change', syncHeroTracking);
finePointer.addEventListener?.('change', syncHeroTracking);

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

document.querySelectorAll('[data-copy], [data-copy-target]').forEach((button) => {
  button.addEventListener('click', async () => {
    const target = button.dataset.copyTarget ? document.getElementById(button.dataset.copyTarget) : null;
    const text = target?.textContent.trim() || button.dataset.copy || '';
    const originalLabel = button.textContent;
    try {
      await navigator.clipboard.writeText(text);
      button.textContent = button.dataset.copiedLabel || 'Copied';
      button.classList.add('copied');
      window.setTimeout(() => {
        button.textContent = originalLabel;
        button.classList.remove('copied');
      }, 1800);
    } catch {
      button.textContent = button.dataset.fallbackLabel || 'Select command';
    }
  });
});

document.querySelectorAll('.mobile-menu a').forEach((link) => {
  link.addEventListener('click', () => link.closest('details')?.removeAttribute('open'));
});
