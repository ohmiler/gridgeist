const syncStageState = (stage) => {
  const isBefore = stage.dataset.state === 'before';
  stage.querySelector('.generic-before')?.setAttribute('aria-hidden', String(!isBefore));
  [...stage.children].filter((child) => !child.classList.contains('generic-before')).forEach((child) => {
    child.setAttribute('aria-hidden', String(isBefore));
  });
};

document.querySelectorAll('[data-case-stage]').forEach(syncStageState);

document.querySelectorAll('.case-controls button').forEach((button) => {
  button.addEventListener('click', () => {
    const name = button.dataset.case;
    const view = button.dataset.view;
    const stage = document.querySelector(`[data-case-stage="${name}"]`);
    stage.dataset.state = view;
    syncStageState(stage);
    document.querySelectorAll(`[data-case="${name}"]`).forEach((candidate) => {
      candidate.setAttribute('aria-pressed', String(candidate === button));
    });
  });
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.08 });

document.querySelectorAll('.reveal').forEach((element) => observer.observe(element));
