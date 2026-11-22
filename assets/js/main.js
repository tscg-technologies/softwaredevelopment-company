/**
 * ==========================================================================
 * SOFTWARE DEVELOPMENT COMPANY — CORE INTERACTION ENGINE
 * 100% Vanilla JavaScript (ES6+) | Hostinger Static Hosting Optimized
 * ==========================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileNav();
  initActiveNavLink();
  initBackToTop();
  initFaqAccordions();
  initToastNotification();
  initCrmDashboardDemo();
  initErpDashboardDemo();
  initPosBillingDemo();
  initInventoryDemo();
  initSaasDashboardDemo();
  initWorkflowInteractiveDiagram();
  initPortfolioFilters();
  initTechFilters();
  initForms();
  initButtonActions();
});

/* --------------------------------------------------------------------------
   1. Sticky Header & Scroll Behavior
   -------------------------------------------------------------------------- */
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 30) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/* --------------------------------------------------------------------------
   2. Mobile Navigation & Dropdowns
   -------------------------------------------------------------------------- */
function initMobileNav() {
  const toggleBtn = document.querySelector('.mobile-toggle');
  const mainNav = document.querySelector('.main-nav');
  const navDropdowns = document.querySelectorAll('.nav-item.has-dropdown');

  if (toggleBtn && mainNav) {
    toggleBtn.addEventListener('click', () => {
      const isOpen = mainNav.classList.toggle('open');
      toggleBtn.setAttribute('aria-expanded', isOpen);
      toggleBtn.innerHTML = isOpen 
        ? `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>`
        : `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>`;
    });
  }

  // Mobile dropdown accordion handling
  navDropdowns.forEach(dropdown => {
    const trigger = dropdown.querySelector('.nav-link');
    if (!trigger) return;

    trigger.addEventListener('click', (e) => {
      if (window.innerWidth <= 900) {
        e.preventDefault();
        const wasOpen = dropdown.classList.contains('dropdown-open');
        navDropdowns.forEach(d => d.classList.remove('dropdown-open'));
        if (!wasOpen) {
          dropdown.classList.add('dropdown-open');
        }
      }
    });
  });

  // Close nav on window resize if enlarged
  window.addEventListener('resize', () => {
    if (window.innerWidth > 900 && mainNav && mainNav.classList.contains('open')) {
      mainNav.classList.remove('open');
      if (toggleBtn) {
        toggleBtn.setAttribute('aria-expanded', 'false');
        toggleBtn.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>`;
      }
    }
  });
}

/* --------------------------------------------------------------------------
   3. Active Nav Link Detector
   -------------------------------------------------------------------------- */
function initActiveNavLink() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link, .dropdown-link');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath) {
      link.classList.add('active');
      // If inside dropdown, also highlight parent nav-link
      const parentDropdown = link.closest('.nav-item.has-dropdown');
      if (parentDropdown) {
        const parentLink = parentDropdown.querySelector('.nav-link');
        if (parentLink) parentLink.classList.add('active');
      }
    }
  });
}

/* --------------------------------------------------------------------------
   4. Back to Top Button
   -------------------------------------------------------------------------- */
function initBackToTop() {
  const backToTopBtn = document.querySelector('.back-to-top');
  if (!backToTopBtn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backToTopBtn.classList.add('show');
    } else {
      backToTopBtn.classList.remove('show');
    }
  }, { passive: true });

  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* --------------------------------------------------------------------------
   5. Global Toast Notification System
   -------------------------------------------------------------------------- */
let toastTimeout;
function showToast(title, message, isWarning = false) {
  let toast = document.querySelector('.demo-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'demo-toast';
    document.body.appendChild(toast);
  }

  const iconColor = isWarning ? '#F59E0B' : '#36D6E8';
  toast.innerHTML = `
    <svg class="toast-icon" style="color: ${iconColor};" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <circle cx="12" cy="12" r="10"></circle>
      <line x1="12" y1="8" x2="12" y2="12"></line>
      <line x1="12" y1="16" x2="12.01" y2="16"></line>
    </svg>
    <div class="toast-content">
      <h4>${title}</h4>
      <p>${message}</p>
    </div>
  `;

  toast.classList.add('show');
  clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => {
    toast.classList.remove('show');
  }, 4500);
}

function initToastNotification() {
  // Attached to window for convenience
  window.showToast = showToast;
}

/* --------------------------------------------------------------------------
   6. FAQ Accordions
   -------------------------------------------------------------------------- */
function initFaqAccordions() {
  const faqItems = document.querySelectorAll('.faq-item');
  if (!faqItems.length) return;

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    if (!questionBtn || !answer) return;

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Close all others
      faqItems.forEach(otherItem => {
        otherItem.classList.remove('active');
        const otherAnswer = otherItem.querySelector('.faq-answer');
        if (otherAnswer) otherAnswer.style.maxHeight = null;
        const otherBtn = otherItem.querySelector('.faq-question');
        if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
      });

      if (!isActive) {
        item.classList.add('active');
        questionBtn.setAttribute('aria-expanded', 'true');
        answer.style.maxHeight = answer.scrollHeight + 32 + 'px';
      }
    });
  });
}

/* --------------------------------------------------------------------------
   7. Interactive CRM Dashboard Demo
   -------------------------------------------------------------------------- */
function initCrmDashboardDemo() {
  const crmContainer = document.querySelector('#crm-interactive-demo');
  if (!crmContainer) return;

  const leads = [
    { id: 1, name: "Alexander Wright", company: "Apex Logistics Ltd", email: "alex.w@example-demo.com", phone: "+1 (555) 019-2831", source: "Website Enquiry", status: "New Lead", nextFollow: "Nov 08, 2026", assigned: "David S." },
    { id: 2, name: "Sophia Chen", company: "NextGen Bio Labs", email: "sophia@example-demo.com", phone: "+1 (555) 018-9942", source: "Referral Portal", status: "Interested", nextFollow: "Nov 09, 2026", assigned: "Elena R." },
    { id: 3, name: "Marcus Vance", company: "Nordic Retail Hub", email: "marcus.v@example-demo.com", phone: "+1 (555) 014-4421", source: "Inbound Call", status: "Follow-Up", nextFollow: "Nov 10, 2026", assigned: "David S." },
    { id: 4, name: "Elena Rostova", company: "Crest Financial Group", email: "elena.r@example-demo.com", phone: "+1 (555) 017-8822", source: "Partner Network", status: "Converted", nextFollow: "Completed", assigned: "Sarah M." },
    { id: 5, name: "Julian Rossi", company: "Solaris Clean Energy", email: "julian@example-demo.com", phone: "+1 (555) 012-3391", source: "Webinar Attendee", status: "Interested", nextFollow: "Nov 11, 2026", assigned: "Elena R." },
    { id: 6, name: "Kavita Sharma", company: "OmniSupply Chain", email: "kavita@example-demo.com", phone: "+1 (555) 016-7733", source: "Website Enquiry", status: "Follow-Up", nextFollow: "Nov 12, 2026", assigned: "Sarah M." }
  ];

  let currentFilter = 'All';
  let searchQuery = '';

  const renderLeads = () => {
    const tbody = crmContainer.querySelector('#crm-leads-tbody');
    const totalCountEl = crmContainer.querySelector('#crm-total-count');
    if (!tbody) return;

    const filtered = leads.filter(lead => {
      const matchesFilter = currentFilter === 'All' || lead.status.toLowerCase() === currentFilter.toLowerCase();
      const matchesSearch = lead.name.toLowerCase().includes(searchQuery) ||
                            lead.company.toLowerCase().includes(searchQuery) ||
                            lead.email.toLowerCase().includes(searchQuery);
      return matchesFilter && matchesSearch;
    });

    if (totalCountEl) totalCountEl.textContent = `${filtered.length} Leads`;

    if (filtered.length === 0) {
      tbody.innerHTML = `<tr><td colspan="7" style="text-align:center; padding: 30px; color: var(--text-muted);">No demo leads match current filter.</td></tr>`;
      return;
    }

    tbody.innerHTML = filtered.map(lead => {
      let badgeClass = 'badge-new';
      if (lead.status === 'Interested') badgeClass = 'badge-interested';
      if (lead.status === 'Follow-Up') badgeClass = 'badge-followup';
      if (lead.status === 'Converted') badgeClass = 'badge-converted';

      return `
        <tr>
          <td>
            <strong>${lead.name}</strong><br>
            <span style="font-size:0.75rem; color:var(--text-muted);">${lead.company}</span>
          </td>
          <td>${lead.phone}</td>
          <td>${lead.email}</td>
          <td><span style="font-size:0.8rem; color:var(--text-secondary);">${lead.source}</span></td>
          <td><span class="badge-status ${badgeClass}">${lead.status}</span></td>
          <td>${lead.nextFollow}</td>
          <td>
            <button class="btn btn-sm btn-outline crm-action-btn" data-id="${lead.id}" title="Simulate Status Change">Next Stage</button>
          </td>
        </tr>
      `;
    }).join('');

    // Attach row button actions
    tbody.querySelectorAll('.crm-action-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = parseInt(e.currentTarget.getAttribute('data-id'));
        const lead = leads.find(l => l.id === id);
        if (lead) {
          const stages = ['New Lead', 'Interested', 'Follow-Up', 'Converted'];
          const nextIdx = (stages.indexOf(lead.status) + 1) % stages.length;
          lead.status = stages[nextIdx];
          renderLeads();
          showToast('CRM Stage Updated (Demo)', `Updated status for ${lead.name} to "${lead.status}".`);
        }
      });
    });
  };

  // Filter Buttons
  crmContainer.querySelectorAll('.crm-filter-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      crmContainer.querySelectorAll('.crm-filter-btn').forEach(b => b.classList.remove('active'));
      e.currentTarget.classList.add('active');
      currentFilter = e.currentTarget.getAttribute('data-filter');
      renderLeads();
    });
  });

  // Search Input
  const searchInput = crmContainer.querySelector('#crm-search-input');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.toLowerCase().trim();
      renderLeads();
    });
  }

  renderLeads();
}

/* --------------------------------------------------------------------------
   8. Interactive ERP Dashboard Demo
   -------------------------------------------------------------------------- */
function initErpDashboardDemo() {
  const erpContainer = document.querySelector('#erp-interactive-demo');
  if (!erpContainer) return;

  const tabs = erpContainer.querySelectorAll('.erp-tab-btn');
  const panels = erpContainer.querySelectorAll('.erp-tab-panel');

  tabs.forEach(tab => {
    tab.addEventListener('click', (e) => {
      tabs.forEach(t => t.classList.remove('active'));
      panels.forEach(p => p.style.display = 'none');

      tab.classList.add('active');
      const target = tab.getAttribute('data-target');
      const activePanel = erpContainer.querySelector(`#${target}`);
      if (activePanel) {
        activePanel.style.display = 'block';
      }
      showToast('ERP Module Switched (Demo)', `Viewing illustrative module: ${tab.textContent.trim()}`);
    });
  });
}

/* --------------------------------------------------------------------------
   9. Interactive POS Billing Interface Demo
   -------------------------------------------------------------------------- */
function initPosBillingDemo() {
  const posContainer = document.querySelector('#pos-interactive-demo');
  if (!posContainer) return;

  const catalog = [
    { id: 'pos-1', name: 'Cloud Core License', price: 1499, category: 'Software' },
    { id: 'pos-2', name: 'Thermal Receipt Gateway', price: 349, category: 'Hardware' },
    { id: 'pos-3', name: 'Barcode Scan Bridge', price: 199, category: 'Add-on' },
    { id: 'pos-4', name: 'Annual Maintenance SLA', price: 899, category: 'Services' },
    { id: 'pos-5', name: 'Multi-Branch Sync Node', price: 499, category: 'Software' },
    { id: 'pos-6', name: 'Payment Terminal API Kit', price: 249, category: 'Integration' }
  ];

  let cart = [
    { ...catalog[0], qty: 1 },
    { ...catalog[2], qty: 2 }
  ];

  const renderProducts = () => {
    const grid = posContainer.querySelector('#pos-products-grid');
    if (!grid) return;

    grid.innerHTML = catalog.map(item => `
      <div class="pos-item-card" data-id="${item.id}">
        <span style="font-size: 0.7rem; color: var(--accent-cyan); text-transform: uppercase;">${item.category}</span>
        <div class="pos-item-name">${item.name}</div>
        <div class="pos-item-price">$${item.price}</div>
        <button class="btn btn-sm btn-outline" style="margin-top: 10px; width: 100%;">+ Add to Bill</button>
      </div>
    `).join('');

    grid.querySelectorAll('.pos-item-card').forEach(card => {
      card.addEventListener('click', () => {
        const id = card.getAttribute('data-id');
        const prod = catalog.find(p => p.id === id);
        const existing = cart.find(c => c.id === id);
        if (existing) {
          existing.qty += 1;
        } else {
          cart.push({ ...prod, qty: 1 });
        }
        renderCart();
        showToast('Item Added to POS Cart', `Added 1x ${prod.name}`);
      });
    });
  };

  const renderCart = () => {
    const list = posContainer.querySelector('#pos-cart-list');
    const subtotalEl = posContainer.querySelector('#pos-subtotal');
    const taxEl = posContainer.querySelector('#pos-tax');
    const totalEl = posContainer.querySelector('#pos-total');
    if (!list) return;

    if (cart.length === 0) {
      list.innerHTML = `<div style="text-align:center; padding: 40px 10px; color: var(--text-muted);">Cart is empty. Select products from catalog.</div>`;
      if (subtotalEl) subtotalEl.textContent = '$0.00';
      if (taxEl) taxEl.textContent = '$0.00';
      if (totalEl) totalEl.textContent = '$0.00';
      return;
    }

    let subtotal = 0;
    list.innerHTML = cart.map(item => {
      const lineTotal = item.price * item.qty;
      subtotal += lineTotal;
      return `
        <div class="pos-cart-item">
          <div>
            <div style="font-weight:600;">${item.name}</div>
            <div style="font-size:0.75rem; color:var(--text-muted);">$${item.price} ea</div>
          </div>
          <div class="qty-control">
            <button class="qty-btn pos-dec" data-id="${item.id}">-</button>
            <span style="font-family: var(--font-mono); font-weight: 700; width: 20px; text-align: center;">${item.qty}</span>
            <button class="qty-btn pos-inc" data-id="${item.id}">+</button>
            <span style="font-family: var(--font-mono); font-weight: 700; margin-left: 8px;">$${lineTotal}</span>
          </div>
        </div>
      `;
    }).join('');

    const tax = subtotal * 0.10; // 10% illustrative tax
    const total = subtotal + tax;

    if (subtotalEl) subtotalEl.textContent = `$${subtotal.toFixed(2)}`;
    if (taxEl) taxEl.textContent = `$${tax.toFixed(2)}`;
    if (totalEl) totalEl.textContent = `$${total.toFixed(2)}`;

    // Qty buttons
    list.querySelectorAll('.pos-inc').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.getAttribute('data-id');
        const item = cart.find(c => c.id === id);
        if (item) {
          item.qty += 1;
          renderCart();
        }
      });
    });

    list.querySelectorAll('.pos-dec').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.getAttribute('data-id');
        const itemIdx = cart.findIndex(c => c.id === id);
        if (itemIdx > -1) {
          cart[itemIdx].qty -= 1;
          if (cart[itemIdx].qty <= 0) {
            cart.splice(itemIdx, 1);
          }
          renderCart();
        }
      });
    });
  };

  const checkoutBtn = posContainer.querySelector('#pos-checkout-btn');
  if (checkoutBtn) {
    checkoutBtn.addEventListener('click', () => {
      if (cart.length === 0) {
        showToast('Empty POS Cart', 'Please add products before billing.', true);
        return;
      }
      showToast('Demo Transaction Processed', 'Illustrative billing simulation completed. No live payment is processed.');
    });
  }

  const clearBtn = posContainer.querySelector('#pos-clear-btn');
  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      cart = [];
      renderCart();
      showToast('POS Cart Cleared', 'All demo items removed.');
    });
  }

  renderProducts();
  renderCart();
}

/* --------------------------------------------------------------------------
   10. Interactive Inventory Dashboard Demo
   -------------------------------------------------------------------------- */
function initInventoryDemo() {
  const invContainer = document.querySelector('#inventory-interactive-demo');
  if (!invContainer) return;

  const inventoryItems = [
    { sku: 'INV-SKU-101', name: 'Industrial RFID Scanners', category: 'Hardware', stock: 42, minThreshold: 15 },
    { sku: 'INV-SKU-102', name: 'Thermal Barcode Rolls (100pk)', category: 'Consumables', stock: 8, minThreshold: 20 },
    { sku: 'INV-SKU-103', name: 'Handheld POS Terminals', category: 'Hardware', stock: 19, minThreshold: 10 },
    { sku: 'INV-SKU-104', name: 'Wireless Mesh Gateways', category: 'Networking', stock: 4, minThreshold: 10 },
    { sku: 'INV-SKU-105', name: 'Biometric Access Sensors', category: 'Security', stock: 27, minThreshold: 12 },
    { sku: 'INV-SKU-106', name: 'Smart Rack Sensors (Pair)', category: 'Hardware', stock: 15, minThreshold: 15 }
  ];

  const renderInventory = () => {
    const tbody = invContainer.querySelector('#inventory-tbody');
    if (!tbody) return;

    tbody.innerHTML = inventoryItems.map(item => {
      const isLow = item.stock <= item.minThreshold;
      const statusBadge = isLow 
        ? `<span class="badge-status badge-danger">Low Stock (${item.stock})</span>`
        : `<span class="badge-status badge-converted">In Stock (${item.stock})</span>`;

      return `
        <tr>
          <td><code style="font-size:0.8rem; color:var(--accent-cyan);">${item.sku}</code></td>
          <td><strong>${item.name}</strong></td>
          <td>${item.category}</td>
          <td>${item.stock} units</td>
          <td>${statusBadge}</td>
          <td>
            <button class="btn btn-sm btn-outline inv-adjust-btn" data-sku="${item.sku}" data-delta="5">+5 In</button>
            <button class="btn btn-sm btn-outline inv-adjust-btn" data-sku="${item.sku}" data-delta="-2" style="margin-left: 4px;">-2 Out</button>
          </td>
        </tr>
      `;
    }).join('');

    tbody.querySelectorAll('.inv-adjust-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const sku = e.currentTarget.getAttribute('data-sku');
        const delta = parseInt(e.currentTarget.getAttribute('data-delta'));
        const item = inventoryItems.find(i => i.sku === sku);
        if (item) {
          item.stock = Math.max(0, item.stock + delta);
          renderInventory();
          showToast('Stock Adjusted (Demo)', `${item.name}: now ${item.stock} units in stock.`);
        }
      });
    });
  };

  renderInventory();
}

/* --------------------------------------------------------------------------
   11. Interactive SaaS Dashboard Demo
   -------------------------------------------------------------------------- */
function initSaasDashboardDemo() {
  const saasContainer = document.querySelector('#saas-interactive-demo');
  if (!saasContainer) return;

  const dataSets = {
    '7d': { mrr: '$42,500', growth: '+3.4%', activeUsers: '14,820', churn: '0.8%', apiCalls: '2.4M' },
    '30d': { mrr: '$58,900', growth: '+12.6%', activeUsers: '18,450', churn: '1.2%', apiCalls: '10.8M' },
    '90d': { mrr: '$89,200', growth: '+28.1%', activeUsers: '24,190', churn: '1.4%', apiCalls: '34.2M' },
    '1y': { mrr: '$145,000', growth: '+64.5%', activeUsers: '42,000', churn: '1.9%', apiCalls: '142.0M' }
  };

  const buttons = saasContainer.querySelectorAll('.saas-time-btn');
  buttons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      buttons.forEach(b => b.classList.remove('active'));
      e.currentTarget.classList.add('active');
      const time = e.currentTarget.getAttribute('data-time');
      const data = dataSets[time];

      if (data) {
        const mrrEl = saasContainer.querySelector('#saas-mrr');
        const growthEl = saasContainer.querySelector('#saas-growth');
        const usersEl = saasContainer.querySelector('#saas-users');
        const churnEl = saasContainer.querySelector('#saas-churn');
        const apiEl = saasContainer.querySelector('#saas-api');

        if (mrrEl) mrrEl.textContent = data.mrr;
        if (growthEl) growthEl.textContent = data.growth;
        if (usersEl) usersEl.textContent = data.activeUsers;
        if (churnEl) churnEl.textContent = data.churn;
        if (apiEl) apiEl.textContent = data.apiCalls;

        showToast('SaaS Metrics Updated (Demo)', `Illustrative timeframe switched to ${time.toUpperCase()}.`);
      }
    });
  });
}

/* --------------------------------------------------------------------------
   12. Interactive Workflow Diagram (Business Process Automation)
   -------------------------------------------------------------------------- */
function initWorkflowInteractiveDiagram() {
  const diagram = document.querySelector('#workflow-interactive');
  if (!diagram) return;

  const stageDescriptions = {
    trigger: {
      title: "Stage 1: Event Trigger",
      desc: "An automated workflow is initiated by business events such as an incoming webhook, web form submission, payment confirmation, or scheduled cron timer."
    },
    input: {
      title: "Stage 2: Data Input & Ingestion",
      desc: "Incoming JSON payloads, CSV batches, or API telemetry are captured, parsed, sanitized, and stored into a staging queue for validation."
    },
    processing: {
      title: "Stage 3: Data Transformation & Enrichment",
      desc: "Payload values are normalized, deduplicated, mapped against ERP/CRM schemas, and augmented with internal database lookups."
    },
    rules: {
      title: "Stage 4: Business Rules Engine",
      desc: "Custom business logic applies conditional branching, routing criteria, credit checks, discount validations, and role-based thresholds."
    },
    action: {
      title: "Stage 5: Execution & System Action",
      desc: "The system triggers downstream operations: ERP invoice creation, CRM lead assignment, SMS/email customer alerts, and external API syncs."
    },
    review: {
      title: "Stage 6: Audit Log & Continuous Review",
      desc: "Every step is logged into immutable audit trails with status codes, timestamping, performance telemetry, and failure alert notifications."
    }
  };

  const nodes = diagram.querySelectorAll('.workflow-node');
  const titleEl = diagram.querySelector('#workflow-active-title');
  const descEl = diagram.querySelector('#workflow-active-desc');

  nodes.forEach(node => {
    node.addEventListener('click', (e) => {
      nodes.forEach(n => n.classList.remove('active'));
      node.classList.add('active');
      const stageKey = node.getAttribute('data-stage');
      const info = stageDescriptions[stageKey];
      if (info && titleEl && descEl) {
        titleEl.textContent = info.title;
        descEl.textContent = info.desc;
      }
    });
  });
}

/* --------------------------------------------------------------------------
   13. Portfolio Category Filtering
   -------------------------------------------------------------------------- */
function initPortfolioFilters() {
  const container = document.querySelector('#portfolio-filterable-section');
  if (!container) return;

  const filterBtns = container.querySelectorAll('.portfolio-filter-btn');
  const items = container.querySelectorAll('.portfolio-card-item');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.getAttribute('data-filter');

      items.forEach(item => {
        const itemCat = item.getAttribute('data-category');
        if (cat === 'all' || itemCat === cat) {
          item.style.display = 'flex';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}

/* --------------------------------------------------------------------------
   14. Technology Category Filtering
   -------------------------------------------------------------------------- */
function initTechFilters() {
  const container = document.querySelector('#tech-filterable-section');
  if (!container) return;

  const tabBtns = container.querySelectorAll('.tech-tab-btn');
  const techGroups = container.querySelectorAll('.tech-group-panel');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const targetGroup = btn.getAttribute('data-tech');

      techGroups.forEach(group => {
        if (targetGroup === 'all' || group.getAttribute('data-group') === targetGroup) {
          group.style.display = 'block';
        } else {
          group.style.display = 'none';
        }
      });
    });
  });
}

/* --------------------------------------------------------------------------
   15. Frontend-Only Form Validations & Demonstrations
   -------------------------------------------------------------------------- */
function initForms() {
  // Quote Request Form
  const quoteForm = document.querySelector('#quote-request-form');
  if (quoteForm) {
    const descTextarea = quoteForm.querySelector('#project-description');
    const charCounter = quoteForm.querySelector('#quote-char-count');

    if (descTextarea && charCounter) {
      descTextarea.addEventListener('input', () => {
        const len = descTextarea.value.length;
        charCounter.textContent = `${len} / 1500 characters`;
      });
    }

    quoteForm.addEventListener('submit', (e) => {
      e.preventDefault();

      // Basic field checks
      const name = quoteForm.querySelector('[name="fullName"]')?.value.trim();
      const email = quoteForm.querySelector('[name="businessEmail"]')?.value.trim();
      const phone = quoteForm.querySelector('[name="phoneNumber"]')?.value.trim();

      if (!name || !email || !phone) {
        showToast('Required Fields Missing', 'Please fill in your name, business email, and phone number.', true);
        return;
      }

      // Mandatory Prompt Requirement:
      // "Your demo project enquiry has been validated. No information has been transmitted or stored."
      showToast(
        'Project Enquiry Validated',
        'Your demo project enquiry has been validated. No information has been transmitted or stored.'
      );

      quoteForm.reset();
      if (charCounter) charCounter.textContent = '0 / 1500 characters';
    });
  }

  // General Contact Form
  const contactForm = document.querySelector('#general-contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = contactForm.querySelector('[name="name"]')?.value.trim();
      const email = contactForm.querySelector('[name="email"]')?.value.trim();

      if (!name || !email) {
        showToast('Input Required', 'Please provide your name and email address.', true);
        return;
      }

      showToast(
        'Message Validated (Demo)',
        'Your demo contact message has been validated. No information has been transmitted or stored.'
      );
      contactForm.reset();
    });
  }

  // Careers Demo Form
  const careerForm = document.querySelector('#careers-application-form');
  if (careerForm) {
    const resumeInput = careerForm.querySelector('#career-resume-file');
    const resumeLabel = careerForm.querySelector('#career-resume-filename');

    if (resumeInput && resumeLabel) {
      resumeInput.addEventListener('change', () => {
        if (resumeInput.files && resumeInput.files[0]) {
          resumeLabel.textContent = `Selected: ${resumeInput.files[0].name} (Demo: file is not uploaded)`;
          resumeLabel.style.display = 'block';
        }
      });
    }

    careerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      showToast(
        'Application Validated (Demo)',
        'This is a frontend demonstration. No application data or resume was uploaded or transmitted.'
      );
      careerForm.reset();
      if (resumeLabel) resumeLabel.style.display = 'none';
    });
  }
}

/* --------------------------------------------------------------------------
   16. Ensure All Buttons Have Meaningful Actions
   -------------------------------------------------------------------------- */
function initButtonActions() {
  // Attach safe click feedback to demo buttons without explicit href or handlers
  document.querySelectorAll('button:not([type="submit"]):not(.faq-question):not(.filter-btn):not(.qty-btn):not(.pos-dec):not(.pos-inc):not(.crm-action-btn):not(.saas-time-btn):not(.mobile-toggle):not(.back-to-top)').forEach(btn => {
    btn.addEventListener('click', (e) => {
      // If already handled by another event listener, ignore
      if (e.defaultPrevented) return;
      const label = btn.innerText.trim() || 'Interactive Component';
      showToast('Demo Action Triggered', `Simulating action for: "${label}". Frontend demo environment active.`);
    });
  });
}
