const params = new URLSearchParams(window.location.search);
const view = params.get('view') === 'after' ? 'after' : 'before';

document.documentElement.dataset.view = view;
document.querySelector('.version-before')?.setAttribute('aria-hidden', String(view !== 'before'));
document.querySelector('.version-after')?.setAttribute('aria-hidden', String(view !== 'after'));
