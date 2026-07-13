document.querySelectorAll('.case-controls button').forEach((button) => {
  button.addEventListener('click', () => {
    const name = button.dataset.case;
    const view = button.dataset.view;
    const stage = document.querySelector(`[data-case-stage="${name}"]`);
    stage.dataset.state = view;
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
