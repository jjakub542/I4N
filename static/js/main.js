/* ================================================================
   AtomFact — Main JavaScript
   Non-functional mockup interactions
   ================================================================ */

document.addEventListener('DOMContentLoaded', () => {
  initHeaderScroll();
  initMobileMenu();
  initHeaderSearch();
  initCategoryTabs();
  initFilterDropdowns();
  initLoadMore();
});

/* ── Header Scroll Shadow ── */
function initHeaderScroll() {
  const header = document.getElementById('site-header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 8);
  }, { passive: true });
}

/* ── Mobile Menu ── */
function initMobileMenu() {
  const toggleBtn = document.getElementById('menu-toggle');
  const closeBtn = document.getElementById('menu-close');
  const menu = document.getElementById('mobile-menu');

  if (!toggleBtn || !closeBtn || !menu) return;

  function openMenu() {
    menu.classList.add('is-open');
    menu.setAttribute('aria-hidden', 'false');
    toggleBtn.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    closeBtn.focus();
  }

  function closeMenu() {
    menu.classList.remove('is-open');
    menu.setAttribute('aria-hidden', 'true');
    toggleBtn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    toggleBtn.focus();
  }

  toggleBtn.addEventListener('click', openMenu);
  closeBtn.addEventListener('click', closeMenu);

  // Close on Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && menu.classList.contains('is-open')) {
      closeMenu();
    }
  });

  // Close on backdrop click (clicking the menu background, not inner content)
  menu.addEventListener('click', (e) => {
    if (e.target === menu) {
      closeMenu();
    }
  });
}

/* ── Header Search → Open Menu & Focus Search ── */
function initHeaderSearch() {
  const searchBtn = document.getElementById('header-search-btn');
  const menu = document.getElementById('mobile-menu');
  const toggleBtn = document.getElementById('menu-toggle');
  const searchInput = menu ? menu.querySelector('.mobile-menu__search-input') : null;

  if (!searchBtn || !menu || !toggleBtn || !searchInput) return;

  searchBtn.addEventListener('click', () => {
    // Open the mobile menu
    menu.classList.add('is-open');
    menu.setAttribute('aria-hidden', 'false');
    toggleBtn.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';

    // Focus the search input after transition
    setTimeout(() => {
      searchInput.focus();
    }, 350);
  });
}

/* ── Category Tabs ── */
function initCategoryTabs() {
  const tabs = document.querySelectorAll('.category-tabs__item');
  if (!tabs.length) return;

  tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      // Deactivate all tabs
      tabs.forEach((t) => {
        t.classList.remove('active');
        t.setAttribute('aria-pressed', 'false');
      });

      // Activate clicked tab
      tab.classList.add('active');
      tab.setAttribute('aria-pressed', 'true');
    });
  });
}

/* ── Filter Dropdowns ── */
function initFilterDropdowns() {
  const dropdowns = document.querySelectorAll('.filter-dropdown');
  const clearBtn = document.getElementById('clear-filters');
  const resultsNum = document.getElementById('results-num');

  if (!dropdowns.length) return;

  // Toggle dropdown panels
  dropdowns.forEach((dropdown) => {
    const trigger = dropdown.querySelector('.filter-dropdown__trigger');
    const panel = dropdown.querySelector('.filter-dropdown__panel');

    if (!trigger || !panel) return;

    trigger.addEventListener('click', () => {
      const isOpen = panel.classList.contains('is-open');

      // Close all other dropdowns
      closeAllDropdowns();

      if (!isOpen) {
        panel.classList.add('is-open');
        panel.setAttribute('aria-hidden', 'false');
        trigger.setAttribute('aria-expanded', 'true');
      }
    });

    // Update count badge on checkbox change
    const checkboxes = panel.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach((cb) => {
      cb.addEventListener('change', () => {
        updateFilterCount(dropdown, trigger);
        updateResultsCount(resultsNum);
      });
    });
  });

  // Close dropdowns on outside click
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.filter-dropdown')) {
      closeAllDropdowns();
    }
  });

  // Close on Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAllDropdowns();
    }
  });

  // Clear all filters
  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      dropdowns.forEach((dropdown) => {
        const trigger = dropdown.querySelector('.filter-dropdown__trigger');
        const checkboxes = dropdown.querySelectorAll('input[type="checkbox"]');

        checkboxes.forEach((cb) => { cb.checked = false; });
        updateFilterCount(dropdown, trigger);
      });
      updateResultsCount(resultsNum);
    });
  }
}

function closeAllDropdowns() {
  document.querySelectorAll('.filter-dropdown__panel').forEach((panel) => {
    panel.classList.remove('is-open');
    panel.setAttribute('aria-hidden', 'true');
  });
  document.querySelectorAll('.filter-dropdown__trigger').forEach((trigger) => {
    trigger.setAttribute('aria-expanded', 'false');
  });
}

function updateFilterCount(dropdown, trigger) {
  const checked = dropdown.querySelectorAll('input[type="checkbox"]:checked').length;
  const baseText = trigger.getAttribute('data-base-text') || trigger.textContent.replace(/\s*\(\d+\)\s*$/, '').trim();

  // Store original text for reset
  if (!trigger.getAttribute('data-base-text')) {
    trigger.setAttribute('data-base-text', baseText);
  }

  // Get the icon element
  const icon = trigger.querySelector('.material-symbols-outlined');

  if (checked > 0) {
    trigger.textContent = '';
    trigger.appendChild(document.createTextNode(baseText + ' (' + checked + ') '));
    trigger.appendChild(icon);
  } else {
    trigger.textContent = '';
    trigger.appendChild(document.createTextNode(baseText + ' '));
    trigger.appendChild(icon);
  }
}

function updateResultsCount(el) {
  if (!el) return;

  const totalChecked = document.querySelectorAll('.filter-dropdown input[type="checkbox"]:checked').length;
  const base = 1204;
  const shown = totalChecked > 0 ? Math.max(1, Math.floor(base / (totalChecked + 1))) : base;
  el.textContent = shown.toLocaleString('pl-PL');
}

/* ── Load More ── */
function initLoadMore() {
  const btn = document.getElementById('load-more-btn');
  if (!btn) return;

  btn.addEventListener('click', () => {
    btn.textContent = 'Ładowanie…';
    btn.disabled = true;

    // Simulate loading for mockup
    setTimeout(() => {
      btn.textContent = 'Brak więcej wyników';
    }, 1500);
  });
}