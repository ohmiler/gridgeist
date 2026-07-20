const themeKey = 'ledger-account-theme';
const root = document.documentElement;
const themeButton = document.querySelector('[data-theme-toggle]');

function applyTheme(theme) {
  root.dataset.theme = theme;
  if (!themeButton) return;
  const dark = theme === 'dark';
  themeButton.setAttribute('aria-pressed', String(dark));
  themeButton.textContent = dark ? 'Light theme' : 'Dark theme';
}

applyTheme(window.localStorage.getItem(themeKey) || 'light');

themeButton?.addEventListener('click', () => {
  const nextTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
  window.localStorage.setItem(themeKey, nextTheme);
  applyTheme(nextTheme);
});

const profileForm = document.querySelector('[data-profile-form]');
const profileStatus = document.querySelector('[data-profile-status]');

profileForm?.addEventListener('submit', (event) => {
  event.preventDefault();
  const saveButton = profileForm.querySelector('button');
  saveButton.disabled = true;
  saveButton.textContent = 'Saving…';
  profileStatus.textContent = 'Saving profile.';

  window.setTimeout(() => {
    saveButton.disabled = false;
    saveButton.textContent = 'Save profile';
    profileStatus.textContent = 'Profile saved locally.';
  }, 350);
});

const invoiceFilter = document.querySelector('[data-invoice-filter]');
const invoiceRows = [...document.querySelectorAll('[data-invoice-row]')];
const invoiceCount = document.querySelector('[data-invoice-count]');

function updateInvoices() {
  let visible = 0;
  for (const row of invoiceRows) {
    const matches = invoiceFilter.value === 'all' || row.dataset.status === invoiceFilter.value;
    row.hidden = !matches;
    visible += Number(matches);
  }
  invoiceCount.textContent = visible + (visible === 1 ? ' invoice' : ' invoices');
}

invoiceFilter?.addEventListener('change', updateInvoices);

const billingStatus = document.querySelector('[data-billing-status]');

for (const button of document.querySelectorAll('[data-invoice]')) {
  button.addEventListener('click', () => {
    billingStatus.textContent = 'Sample ' + button.dataset.invoice + ' prepared locally.';
  });
}

document.querySelector('[data-manage-plan]')?.addEventListener('click', () => {
  billingStatus.textContent = 'Plan management is unavailable in this fictional fixture.';
});
