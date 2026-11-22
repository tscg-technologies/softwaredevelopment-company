"""
Comprehensive Page Generator for Software Development Company Website
Generates all 26 pages, sitemap.xml, and IMAGE-GENERATION-GUIDE.md
"""
import os
import re

from generator_base import HEADER_TEMPLATE, FOOTER_TEMPLATE, create_img_placeholder

# Registry to catalog every single image placeholder used across the entire site
IMAGE_CATALOG = []

def register_image(filename, page, section, ratio, resolution, orientation, purpose, description, flow_prompt_data):
    entry = {
        "num": len(IMAGE_CATALOG) + 1,
        "filename": filename,
        "page": page,
        "section": section,
        "ratio": ratio,
        "resolution": resolution,
        "orientation": orientation,
        "purpose": purpose,
        "desc": description,
        "prompt": flow_prompt_data
    }
    IMAGE_CATALOG.append(entry)
    return create_img_placeholder(filename, ratio, description)

pages_data = {}

# ==============================================================================
# 1. HOMEPAGE (index.html)
# ==============================================================================
img_home_hero = register_image(
    "home-hero-software-architecture.jpg", "index.html", "Hero Section", "16:9", "1920x1080", "Landscape",
    "Hero software architecture & cloud infrastructure visualization",
    "Abstract 3D software architecture nodes, glowing data pipelines, and floating UI dashboard widgets.",
    {
        "subject": "Modern enterprise software architecture nodes and interconnected cloud microservices data pipelines",
        "environment": "Deep navy digital cyberspace with illuminated geometric node clusters and floating glass dashboard widgets",
        "composition": "Centered perspective showing microservice network converging toward a sleek high-tech SaaS control panel",
        "camera": "Wide-angle isometric view with shallow depth of field",
        "lighting": "Volumetric electric blue (#4F8CFF) edge lights, soft cyan (#36D6E8) glow, subtle violet accent illumination",
        "background": "Deep dark navy #080D18 backdrop with subtle dot-matrix engineering grid",
        "colors": "Primary background #080D18, #101827, Electric Blue #4F8CFF, Cyan #36D6E8, Violet #9878FF",
        "style": "Ultra-clean modern 3D tech art, enterprise digital product render, Octane render quality",
        "mood": "Visionary, highly technical, reliable, enterprise-grade",
        "ratio": "16:9",
        "negative": "cartoon, blurry, low resolution, messy cables, realistic humans, messy text, stock photo cliches"
    }
)

img_home_intro = register_image(
    "home-business-dashboard.jpg", "index.html", "Introduction Section", "16:10", "1600x1000", "Landscape",
    "Overview of unified business operations software dashboard",
    "Multi-module business management software interface showing sales metrics, pipeline flow, and automated tasks.",
    {
        "subject": "Modern enterprise management dashboard UI mockup displaying interactive workflow metrics and data charts",
        "environment": "Sleek dark theme UI interface floating gently over a subtle isometric tech surface",
        "composition": "Slight perspective angle 3/4 view of modern dark dashboard with glowing KPI widgets and clean graphs",
        "camera": "Eye-level 3/4 perspective shot",
        "lighting": "Soft cyan and blue ambient rim lighting reflecting off polished dark glass panels",
        "background": "Dark gradient background #080D18 to #101827 with faint circuit lines",
        "colors": "Dark navy #080D18, Slate #141F32, Electric Blue #4F8CFF, Cyan #36D6E8",
        "style": "High-fidelity digital product design mockup, minimalist UI layout",
        "mood": "Efficient, organized, premium enterprise software",
        "ratio": "16:10",
        "negative": "unrealistic graphics, cluttered icons, bright white background, illegible text, low resolution"
    }
)

img_home_retail = register_image(
    "home-concept-retail.jpg", "index.html", "Featured Concepts", "16:10", "1280x800", "Landscape",
    "Retail Management Software Concept Preview",
    "Illustrative POS and omnichannel retail inventory system dashboard concept.",
    {
        "subject": "Retail management system interface mockup showing inventory status, point-of-sale register metrics, and order streams",
        "environment": "Modern dark UI screen with bar charts and transaction tables",
        "composition": "Frontal UI presentation with modular widgets",
        "camera": "Straight-on digital UI rendering",
        "lighting": "Clean internal UI illumination with blue and cyan accent pills",
        "background": "#141F32 card frame",
        "colors": "Dark theme, #080D18, #4F8CFF, #36D6E8",
        "style": "Clean SaaS software mockup",
        "mood": "Accurate, modern, retail-focused",
        "ratio": "16:10",
        "negative": "physical store photo, people shopping, cashier, low quality"
    }
)

img_home_crm = register_image(
    "home-concept-crm.jpg", "index.html", "Featured Concepts", "16:10", "1280x800", "Landscape",
    "CRM Lead Pipeline Interface Concept",
    "Sales pipeline kanban view with lead stages and communication history.",
    {
        "subject": "CRM sales pipeline software dashboard showcasing deal stages, lead scoring indicators, and follow-up alerts",
        "environment": "Clean dark mode CRM web application interface",
        "composition": "Perspective UI view emphasizing kanban columns and activity metrics",
        "camera": "Subtle isometric tilt",
        "lighting": "Soft directional glow on active pipeline cards",
        "background": "#101827 secondary background",
        "colors": "#141F32 cards, #4F8CFF active state, #36D6E8 badges",
        "style": "Enterprise product design",
        "mood": "Organized, high-velocity sales management",
        "ratio": "16:10",
        "negative": "stock handshakes, office meeting photos, realistic humans"
    }
)

img_home_inventory = register_image(
    "home-concept-inventory.jpg", "index.html", "Featured Concepts", "16:10", "1280x800", "Landscape",
    "Inventory Management System Concept",
    "Warehouse SKU tracking, reorder alert notifications, and logistics sync.",
    {
        "subject": "Warehouse inventory software dashboard showing real-time stock levels, SKU tracking tables, and automated low-stock warnings",
        "environment": "Dark software UI with data tables and gauge charts",
        "composition": "Centered layout with clear metric cards at top and table below",
        "camera": "Direct flat digital display",
        "lighting": "Crisp digital contrast with amber warning highlights and cyan counters",
        "background": "#080D18 deep navy",
        "colors": "Dark blue, cyan, electric blue, warning gold",
        "style": "Industrial software UI mockup",
        "mood": "Systematic, robust, enterprise operations",
        "ratio": "16:10",
        "negative": "forklifts, physical warehouse boxes, muddy textures"
    }
)

img_home_saas = register_image(
    "home-concept-saas.jpg", "index.html", "Featured Concepts", "16:10", "1280x800", "Landscape",
    "SaaS Business Platform Interface Concept",
    "Multi-tenant subscription analytics, MRR charts, and API gateway telemetry.",
    {
        "subject": "B2B SaaS product administration portal showcasing MRR growth curves, tenant health metrics, and API latency graphs",
        "environment": "Futuristic clean analytics dashboard in dark mode",
        "composition": "Dynamic 3D perspective with floating telemetry layer",
        "camera": "Angled perspective with crisp depth",
        "lighting": "Electric blue line charts with bright cyan gradient fills and violet points",
        "background": "Deep space navy #080D18",
        "colors": "#4F8CFF, #36D6E8, #9878FF",
        "style": "State-of-the-art SaaS analytics visual",
        "mood": "High-growth, intelligent, scalable",
        "ratio": "16:10",
        "negative": "generic graphs, 2D clip art, blurry raster"
    }
)

pages_data["index.html"] = {
    "title": "Software Development Company — Custom Software Solutions & Engineering",
    "desc": "We build custom software, scalable web applications, SaaS platforms, CRM, ERP, POS, and process automation solutions tailored for growing businesses and enterprises.",
    "keywords": "Software Development Company, Custom Software Development, Web Applications, SaaS Development, CRM Development, ERP Development, Business Process Automation",
    "content": f"""
  <!-- Section 1: Hero Section -->
  <section class="hero-section">
    <div class="container">
      <div class="hero-grid">
        <div class="hero-content">
          <div class="tagline-badge">
            <span class="badge-dot"></span>
            <span>Custom Engineering Studio</span>
          </div>
          <h1>SOFTWARE THAT SOLVES <span class="text-gradient">REAL BUSINESS PROBLEMS.</span></h1>
          <p class="lead">
            From custom business applications and SaaS platforms to CRM, ERP, and intelligent automation, we transform your requirements into practical digital products.
          </p>
          <div class="btn-group">
            <a href="custom-software.html" class="btn btn-primary">Explore Our Solutions</a>
            <a href="request-quote.html" class="btn btn-secondary">Discuss Your Project</a>
          </div>

          <div class="hero-stats">
            <div class="stat-item">
              <h3>100%</h3>
              <p>Custom Engineered Around Your Workflows</p>
            </div>
            <div class="stat-item">
              <h3>Modular</h3>
              <p>Scalable Cloud & Database Architectures</p>
            </div>
            <div class="stat-item">
              <h3>End-to-End</h3>
              <p>Discovery, UI/UX, Build & Maintenance</p>
            </div>
          </div>
        </div>

        <div class="hero-visual">
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">architecture-preview.sys</span>
              <div style="font-size:0.7rem; color:var(--accent-cyan); font-family:var(--font-mono);">STATUS: ACTIVE</div>
            </div>
            <div class="mockup-body" style="padding:0;">
              {img_home_hero}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 2: Introduction -->
  <section class="section section-alt">
    <div class="container">
      <div class="grid-2" style="align-items: center;">
        <div>
          <div class="tagline-badge">
            <span class="badge-dot"></span>
            <span>Engineering Philosophy</span>
          </div>
          <h2>YOUR IDEAS. <span class="text-gradient">OUR ENGINEERING.</span></h2>
          <p class="lead" style="margin-bottom: 20px;">
            Off-the-shelf software often forces your business into rigid molds. We build custom software systems engineered around your exact operational logic.
          </p>
          <p style="margin-bottom: 16px;">
            Whether you need to streamline internal workflows, unify multi-branch retail operations, manage complex sales pipelines, or launch a proprietary multi-tenant SaaS application, our engineering methodology turns complex requirements into secure, high-performance software.
          </p>
          <ul style="margin-bottom: 24px; display:flex; flex-direction:column; gap:12px;">
            <li style="display:flex; align-items:center; gap:10px;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Automate manual bottlenecks and eliminate repetitive spreadsheet entry.</span>
            </li>
            <li style="display:flex; align-items:center; gap:10px;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Centralize company operations across CRM, ERP, inventory, and accounting.</span>
            </li>
            <li style="display:flex; align-items:center; gap:10px;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Retain full intellectual property and tailor your software as your business grows.</span>
            </li>
          </ul>
          <a href="about.html" class="link-arrow">Discover our business-first engineering approach &rarr;</a>
        </div>
        <div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">enterprise-operations.view</span>
            </div>
            {img_home_intro}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 3: Core Software Development Services -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Core Capabilities</span>
        </div>
        <h2>CUSTOM SOFTWARE <span class="text-gradient">DEVELOPMENT SERVICES</span></h2>
        <p>Comprehensive digital product engineering from conceptual blueprint to enterprise-scale deployment.</p>
      </div>

      <div class="grid-4">
        <!-- Service Card 1 -->
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
          </div>
          <h3>Custom Software</h3>
          <p>Bespoke enterprise management applications built to solve operational inefficiencies and eliminate manual workflows.</p>
          <div class="card-footer">
            <a href="custom-software.html" class="link-arrow">Learn More &rarr;</a>
          </div>
        </div>

        <!-- Service Card 2 -->
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          </div>
          <h3>Web Applications</h3>
          <p>High-speed, responsive customer portals, admin consoles, and secure cloud workflow platforms.</p>
          <div class="card-footer">
            <a href="web-applications.html" class="link-arrow">Learn More &rarr;</a>
          </div>
        </div>

        <!-- Service Card 3 -->
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>
          </div>
          <h3>SaaS Development</h3>
          <p>Multi-tenant architectures, subscription billing integrations, tenant isolation, and self-service analytics.</p>
          <div class="card-footer">
            <a href="saas-development.html" class="link-arrow">Learn More &rarr;</a>
          </div>
        </div>

        <!-- Service Card 4 -->
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <h3>CRM Development</h3>
          <p>Lead pipelines, automated follow-up cadences, communication histories, and sales conversion intelligence.</p>
          <div class="card-footer">
            <a href="crm-development.html" class="link-arrow">Learn More &rarr;</a>
          </div>
        </div>

        <!-- Service Card 5 -->
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
          </div>
          <h3>ERP Development</h3>
          <p>Integrated purchasing, multi-location sales, finance reconciliation, inventory tracking, and executive analytics.</p>
          <div class="card-footer">
            <a href="erp-development.html" class="link-arrow">Learn More &rarr;</a>
          </div>
        </div>

        <!-- Service Card 6 -->
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><line x1="6" y1="8" x2="10" y2="8"/><line x1="14" y1="8" x2="18" y2="8"/><line x1="6" y1="12" x2="18" y2="12"/></svg>
          </div>
          <h3>POS & Billing Software</h3>
          <p>Fast-action retail and dining POS systems, barcode scanning, shift reconciliations, and tax invoicing.</p>
          <div class="card-footer">
            <a href="pos-development.html" class="link-arrow">Learn More &rarr;</a>
          </div>
        </div>

        <!-- Service Card 7 -->
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
          </div>
          <h3>E-commerce Solutions</h3>
          <p>Custom B2B and B2C digital storefronts with catalog rules, tiered customer pricing, and checkout workflows.</p>
          <div class="card-footer">
            <a href="ecommerce-development.html" class="link-arrow">Learn More &rarr;</a>
          </div>
        </div>

        <!-- Service Card 8 -->
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
          </div>
          <h3>Process Automation</h3>
          <p>Automate multi-step approval flows, data synchronization, document generation, and external API hooks.</p>
          <div class="card-footer">
            <a href="business-automation.html" class="link-arrow">Learn More &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 4: What We Build -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Product Showcase</span>
        </div>
        <h2>WHAT WE <span class="text-gradient">ENGINEER & DELIVER</span></h2>
        <p>Purpose-built software platforms designed to optimize every facet of your modern business operations.</p>
      </div>

      <div class="grid-3">
        <div class="card">
          <div class="card-tags">
            <span class="tag-pill">Operations</span>
            <span class="tag-pill">Workflow</span>
          </div>
          <h3>Business Management Software</h3>
          <p>Unified enterprise control centers that connect department workflows, staff authorizations, and real-time operational tracking into one central system.</p>
          <a href="custom-software.html" class="link-arrow">Explore Features &rarr;</a>
        </div>

        <div class="card">
          <div class="card-tags">
            <span class="tag-pill">Sales Ops</span>
            <span class="tag-pill">Pipelines</span>
          </div>
          <h3>Customer Relationship Systems</h3>
          <p>Manage prospective leads, segment customer records, track communication history, and automate quote follow-ups.</p>
          <a href="crm-development.html" class="link-arrow">Explore Features &rarr;</a>
        </div>

        <div class="card">
          <div class="card-tags">
            <span class="tag-pill">Enterprise</span>
            <span class="tag-pill">Resource Planning</span>
          </div>
          <h3>Enterprise Resource Planning (ERP)</h3>
          <p>Connect inventory batches, purchase orders, vendor invoices, multi-branch sales receipts, and general ledger reports.</p>
          <a href="erp-development.html" class="link-arrow">Explore Features &rarr;</a>
        </div>

        <div class="card">
          <div class="card-tags">
            <span class="tag-pill">Retail</span>
            <span class="tag-pill">Billing</span>
          </div>
          <h3>Point of Sale (POS) Systems</h3>
          <p>Touchscreen-optimized checkout screens with barcode reader hooks, split payments, and real-time stock deduction.</p>
          <a href="pos-development.html" class="link-arrow">Explore Features &rarr;</a>
        </div>

        <div class="card">
          <div class="card-tags">
            <span class="tag-pill">Logistics</span>
            <span class="tag-pill">Warehousing</span>
          </div>
          <h3>Inventory Management Systems</h3>
          <p>Keep track of bin locations, SKU reorder points, supplier purchase orders, and stock movements across storage depots.</p>
          <a href="inventory-software.html" class="link-arrow">Explore Features &rarr;</a>
        </div>

        <div class="card">
          <div class="card-tags">
            <span class="tag-pill">Cloud SaaS</span>
            <span class="tag-pill">Multi-Tenant</span>
          </div>
          <h3>Custom SaaS Platforms</h3>
          <p>Scalable cloud products with tenant isolation, tiered billing subscriptions, role permissions, and API key management.</p>
          <a href="saas-development.html" class="link-arrow">Explore Features &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 5: Software Engineering Approach -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Methodology</span>
        </div>
        <h2>ENGINEERED AROUND <span class="text-gradient">YOUR BUSINESS</span></h2>
        <p>We believe technology choices must follow business requirements—not the other way around.</p>
      </div>

      <div class="grid-4">
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">01 / DISCOVERY</div>
          <h4>Requirement Analysis</h4>
          <p>Deep-dive workshops to analyze your team's workflow, bottlenecks, data inputs, and system objectives.</p>
        </div>
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">02 / STRATEGY</div>
          <h4>Product Planning</h4>
          <p>Mapping user journeys, technical constraints, feature milestones, and system scalability goals.</p>
        </div>
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">03 / EXPERIENCE</div>
          <h4>UI/UX Interface Design</h4>
          <p>Designing wireframes, intuitive dashboard layouts, and role-based workflows for daily productivity.</p>
        </div>
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">04 / FOUNDATION</div>
          <h4>Software Architecture</h4>
          <p>Database schema design, security boundaries, API specifications, and modular service structuring.</p>
        </div>
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">05 / CODE</div>
          <h4>Development</h4>
          <p>Writing clean, maintainable code using robust frameworks and engineering best practices.</p>
        </div>
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">06 / ASSURANCE</div>
          <h4>Testing & QA</h4>
          <p>Validating logic, security boundaries, edge cases, responsive views, and performance benchmarks.</p>
        </div>
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">07 / LAUNCH</div>
          <h4>Deployment</h4>
          <p>Seamless production rollout, database migration, environmental tuning, and admin training.</p>
        </div>
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">08 / LONGEVITY</div>
          <h4>Ongoing Support</h4>
          <p>Continuous monitoring, security patches, framework updates, and iterative feature expansion.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 6: Industries We Serve -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Industry Solutions</span>
        </div>
        <h2>INDUSTRIES <span class="text-gradient">WE SERVE</span></h2>
        <p>Illustrative target sectors where custom software drives operational efficiency and competitive advantage.</p>
      </div>

      <div class="grid-3">
        <div class="card">
          <h4>Retail & E-commerce</h4>
          <p>Omnichannel POS, multi-location stock syncing, promotional pricing engines, and customer order trackers.</p>
          <a href="industries.html" class="link-arrow">View Industry Overview &rarr;</a>
        </div>
        <div class="card">
          <h4>Healthcare</h4>
          <p>Patient scheduling, clinic management systems, doctor consultation portals, and medical record workflows.</p>
          <a href="industries.html" class="link-arrow">View Industry Overview &rarr;</a>
        </div>
        <div class="card">
          <h4>Education & E-learning</h4>
          <p>Student information systems, attendance tracking, test grading portals, and course material delivery platforms.</p>
          <a href="industries.html" class="link-arrow">View Industry Overview &rarr;</a>
        </div>
        <div class="card">
          <h4>Real Estate</h4>
          <p>Property portfolio management, tenant lease tracking, maintenance request routing, and payment accounting.</p>
          <a href="industries.html" class="link-arrow">View Industry Overview &rarr;</a>
        </div>
        <div class="card">
          <h4>Logistics & Supply Chain</h4>
          <p>Fleet tracking interfaces, dispatch scheduling, proof-of-delivery capture, and warehouse stock verification.</p>
          <a href="industries.html" class="link-arrow">View Industry Overview &rarr;</a>
        </div>
        <div class="card">
          <h4>Manufacturing</h4>
          <p>Bill of materials (BOM), production batch tracking, machine maintenance logs, and raw material reorder alerts.</p>
          <a href="industries.html" class="link-arrow">View Industry Overview &rarr;</a>
        </div>
        <div class="card">
          <h4>Finance & Accounting</h4>
          <p>Automated invoice generation, tax reconciliation modules, payment tracking, and audit trail ledgers.</p>
          <a href="industries.html" class="link-arrow">View Industry Overview &rarr;</a>
        </div>
        <div class="card">
          <h4>Professional Services</h4>
          <p>Client billing portals, staff timesheet tracking, project milestone billing, and contract document repositories.</p>
          <a href="industries.html" class="link-arrow">View Industry Overview &rarr;</a>
        </div>
        <div class="card">
          <h4>Startups & Technology</h4>
          <p>Minimum viable product (MVP) development, rapid software prototyping, and scalable multi-tenant SaaS foundations.</p>
          <a href="industries.html" class="link-arrow">View Industry Overview &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 7: Featured Software Concepts -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Concept Demonstrations</span>
        </div>
        <h2>FEATURED <span class="text-gradient">SOFTWARE CONCEPTS</span></h2>
        <p>Explore illustrative software interface previews showcasing our product design and architectural approach.</p>
      </div>

      <div class="grid-2">
        <div class="card" style="padding: 20px;">
          <div class="mockup-window" style="margin-bottom: 20px;">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">concept-retail-pos.view</span>
              <span class="badge-status badge-new">Demo Concept</span>
            </div>
            {img_home_retail}
          </div>
          <h3>Retail Management Software</h3>
          <p>An all-in-one retail POS and inventory dashboard concept engineered for multi-counter store checkouts and stock balance monitoring.</p>
          <a href="pos-development.html" class="btn btn-secondary btn-sm">Explore POS Capabilities</a>
        </div>

        <div class="card" style="padding: 20px;">
          <div class="mockup-window" style="margin-bottom: 20px;">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">concept-sales-crm.view</span>
              <span class="badge-status badge-interested">Demo Concept</span>
            </div>
            {img_home_crm}
          </div>
          <h3>CRM Lead Management Dashboard</h3>
          <p>Sales pipeline management concept with real-time prospect tracking, automated follow-up cadences, and conversion metrics.</p>
          <a href="crm-development.html" class="btn btn-secondary btn-sm">Explore CRM Capabilities</a>
        </div>

        <div class="card" style="padding: 20px;">
          <div class="mockup-window" style="margin-bottom: 20px;">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">concept-inventory-node.view</span>
              <span class="badge-status badge-followup">Demo Concept</span>
            </div>
            {img_home_inventory}
          </div>
          <h3>Inventory Management System</h3>
          <p>Warehouse logistics dashboard designed for stock movements, SKU tracking, reorder alert thresholds, and vendor replenishment.</p>
          <a href="inventory-software.html" class="btn btn-secondary btn-sm">Explore Inventory Capabilities</a>
        </div>

        <div class="card" style="padding: 20px;">
          <div class="mockup-window" style="margin-bottom: 20px;">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">concept-saas-core.view</span>
              <span class="badge-status badge-converted">Demo Concept</span>
            </div>
            {img_home_saas}
          </div>
          <h3>SaaS Business Platform</h3>
          <p>Multi-tenant cloud platform concept featuring subscription health metrics, customer tier quotas, and API telemetry graphs.</p>
          <a href="saas-development.html" class="btn btn-secondary btn-sm">Explore SaaS Capabilities</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 8: Visual Six-Step Process -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Delivery Lifecycle</span>
        </div>
        <h2>OUR DEVELOPMENT <span class="text-gradient">PROCESS</span></h2>
        <p>A structured, predictable software delivery framework designed to guarantee transparency and quality.</p>
      </div>

      <div class="process-timeline">
        <div class="process-step">
          <div class="process-number">01</div>
          <div class="process-body">
            <h3>Discover</h3>
            <p>We analyze your business model, understand team workflows, uncover friction points, and document technical specifications.</p>
          </div>
        </div>
        <div class="process-step">
          <div class="process-number">02</div>
          <div class="process-body">
            <h3>Plan</h3>
            <p>We define project scopes, architectural blueprints, database models, technical milestones, and realistic sprint schedules.</p>
          </div>
        </div>
        <div class="process-step">
          <div class="process-number">03</div>
          <div class="process-body">
            <h3>Design</h3>
            <p>We craft intuitive, user-friendly UI/UX mockups, design tokens, and interactive clickable wireframes for stakeholder review.</p>
          </div>
        </div>
        <div class="process-step">
          <div class="process-number">04</div>
          <div class="process-body">
            <h3>Develop</h3>
            <p>Our engineers implement clean, maintainable frontend and backend architectures with rigorous peer reviews and version control.</p>
          </div>
        </div>
        <div class="process-step">
          <div class="process-number">05</div>
          <div class="process-body">
            <h3>Test</h3>
            <p>Every software release undergoes functional testing, regression audits, security validation, and cross-device performance checks.</p>
          </div>
        </div>
        <div class="process-step">
          <div class="process-number">06</div>
          <div class="process-body">
            <h3>Deploy & Support</h3>
            <p>We manage smooth production deployment, perform data migration, train your team, and provide reliable ongoing technical maintenance.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 9: Technology Stack Showcase -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Tech Stack</span>
        </div>
        <h2>TECHNOLOGIES <span class="text-gradient">& TOOLS</span></h2>
        <p>Illustrative software technologies selected based on project performance, security, and long-term maintainability.</p>
      </div>

      <div class="grid-3">
        <div class="card">
          <h4>Frontend Engineering</h4>
          <p>HTML5, Modern CSS3, JavaScript (ES6+), TypeScript, React, Angular, Vue.</p>
          <span class="tag-pill">UI & Dashboard Previews</span>
        </div>
        <div class="card">
          <h4>Backend Architecture</h4>
          <p>Node.js, Python, PHP, Java, .NET Core, Modular Microservices.</p>
          <span class="tag-pill">APIs & Business Logic</span>
        </div>
        <div class="card">
          <h4>Mobile Applications</h4>
          <p>Flutter, React Native, Native Android (Kotlin), Native iOS (Swift).</p>
          <span class="tag-pill">Cross-Platform Clients</span>
        </div>
        <div class="card">
          <h4>Databases & Caching</h4>
          <p>MySQL, PostgreSQL, MongoDB, Redis, SQLite, Structured Data Schemas.</p>
          <span class="tag-pill">ACID Compliance</span>
        </div>
        <div class="card">
          <h4>Cloud & DevOps</h4>
          <p>AWS, Microsoft Azure, Google Cloud, Docker Containers, Git, CI/CD Pipelines.</p>
          <span class="tag-pill">High Availability</span>
        </div>
        <div class="card">
          <h4>APIs & Integrations</h4>
          <p>RESTful APIs, Webhooks, GraphQL, Payment Gateway Bridges, CRM/ERP Connectors.</p>
          <span class="tag-pill">System Interoperability</span>
        </div>
      </div>

      <div style="text-align: center; margin-top: 36px;">
        <a href="technologies.html" class="btn btn-secondary">Explore Detailed Technologies Directory</a>
      </div>
    </div>
  </section>

  <!-- Section 10: Why Choose Us -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Why Work With Us</span>
        </div>
        <h2>ENGINEERING EXCELLENCE <span class="text-gradient">FOR GROWING BUSINESSES</span></h2>
        <p>We combine software engineering depth with business understanding to deliver practical digital solutions.</p>
      </div>

      <div class="grid-3">
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 14 14"/></svg>
          </div>
          <h3>Business-Focused Development</h3>
          <p>We do not build software for the sake of writing code. Every feature, database table, and interface is engineered to solve a tangible business requirement.</p>
        </div>
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          </div>
          <h3>Custom-Built Solutions</h3>
          <p>No generic, cookie-cutter templates that break under scale. You get tailored architecture designed around your company's unique workflows.</p>
        </div>
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
          </div>
          <h3>Scalable Software Architecture</h3>
          <p>Modular codebases, clean database schemas, and structured APIs allow your software to grow seamlessly as transaction volumes multiply.</p>
        </div>
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          </div>
          <h3>User-Friendly Interfaces</h3>
          <p>Complex backend logic wrapped in clean, intuitive UI design that reduces training time and minimizes operational user mistakes.</p>
        </div>
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3>Quality-Focused Engineering</h3>
          <p>Comprehensive code reviews, input validation, defensive error handling, and robust security practices from day one.</p>
        </div>
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
          </div>
          <h3>Ongoing Support Approach</h3>
          <p>We remain your technical partner long after launch, assisting with updates, feature additions, performance tuning, and technical guidance.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 11: Portfolio Preview -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Sample Capabilities</span>
        </div>
        <h2>PORTFOLIO <span class="text-gradient">PREVIEW</span></h2>
        <p>Explore representative demo project concepts that reflect our engineering range across industries.</p>
      </div>

      <div class="grid-3">
        <div class="card">
          <span class="badge-status badge-new" style="align-self:flex-start; margin-bottom:12px;">Demo Project 01</span>
          <h3>Retail Management Software</h3>
          <p>Multi-location retail billing, inventory balancing, real-time counter reconciliations, and supplier purchase orders.</p>
          <div class="card-tags">
            <span class="tag-pill">POS</span>
            <span class="tag-pill">Inventory</span>
            <span class="tag-pill">Billing</span>
          </div>
          <a href="portfolio.html" class="link-arrow">View Project Details &rarr;</a>
        </div>

        <div class="card">
          <span class="badge-status badge-interested" style="align-self:flex-start; margin-bottom:12px;">Demo Project 02</span>
          <h3>CRM Lead Management System</h3>
          <p>Automated prospect intake, lead status pipelines, call scheduling, and team performance tracking dashboards.</p>
          <div class="card-tags">
            <span class="tag-pill">CRM</span>
            <span class="tag-pill">Sales Ops</span>
            <span class="tag-pill">Analytics</span>
          </div>
          <a href="portfolio.html" class="link-arrow">View Project Details &rarr;</a>
        </div>

        <div class="card">
          <span class="badge-status badge-converted" style="align-self:flex-start; margin-bottom:12px;">Demo Project 03</span>
          <h3>SaaS Business Dashboard</h3>
          <p>Multi-tenant subscription management software with tenant usage quotas, automated invoicing, and telemetry graphs.</p>
          <div class="card-tags">
            <span class="tag-pill">SaaS</span>
            <span class="tag-pill">Multi-Tenant</span>
            <span class="tag-pill">Billing</span>
          </div>
          <a href="portfolio.html" class="link-arrow">View Project Details &rarr;</a>
        </div>
      </div>

      <div style="text-align:center; margin-top:36px;">
        <a href="portfolio.html" class="btn btn-secondary">Explore All 8 Demo Projects</a>
      </div>
    </div>
  </section>

  <!-- Section 12: Final CTA -->
  <section class="section section-alt" style="border-top: 1px solid var(--border-color);">
    <div class="container" style="text-align: center; max-width: 800px;">
      <div class="tagline-badge">
        <span class="badge-dot"></span>
        <span>Let's Collaborate</span>
      </div>
      <h2>LET'S BUILD THE SOFTWARE <span class="text-gradient">YOUR BUSINESS NEEDS.</span></h2>
      <p class="lead" style="margin-bottom: 32px;">
        Have a business challenge or a software idea? Let's turn it into a structured development plan.
      </p>
      <div class="btn-group" style="justify-content: center;">
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request a Project Quote</a>
        <a href="contact.html" class="btn btn-outline btn-lg">Contact Our Team</a>
      </div>
    </div>
  </section>
"""
}

# ==============================================================================
# 2. ABOUT PAGE (about.html)
# ==============================================================================
img_about_engineering = register_image(
    "about-engineering-team.jpg", "about.html", "Engineering Philosophy", "16:9", "1920x1080", "Landscape",
    "Modern software engineering workstation and architecture review",
    "Multi-screen developer workspace displaying software architecture diagrams, code editors, and database relational models.",
    {
        "subject": "Modern software engineering workstation showing system architecture diagrams, code schemas, and clean terminal displays",
        "environment": "Sleek technology office studio with dark acoustic paneling and subtle ambient LED lighting",
        "composition": "Over-the-shoulder perspective of dual curved monitors showcasing microservice topologies and clean code",
        "camera": "Eye level cinematic shot with gentle bokeh",
        "lighting": "Deep dark ambiance with electric blue and cyan monitor glow",
        "background": "Minimalist software studio with glass partitions",
        "colors": "#080D18, #101827, #4F8CFF, #36D6E8",
        "style": "High-end corporate software technology photography",
        "mood": "Focused, intelligent, disciplined engineering",
        "ratio": "16:9",
        "negative": "messy desk, coffee spills, cartoonish characters, bright generic office lighting"
    }
)

pages_data["about.html"] = {
    "title": "About Our Software Development Company — Engineering & Mission",
    "desc": "Learn about our business-first software development approach, engineering philosophy, and long-term commitment to quality, scalable architectures.",
    "keywords": "About Software Company, Engineering Philosophy, Custom Software Studio, Business-First Software, Quality Engineering",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>About the Company</span>
        </div>
        <h1>ENGINEERING SOFTWARE WITH <span class="text-gradient">PURPOSE & PRECISION</span></h1>
        <p class="lead">We bridge the gap between complex business requirements and reliable, scalable digital software solutions.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>WHO WE ARE</h2>
          <p style="margin-bottom: 16px;">
            We are a dedicated software development company focused on building custom business applications, scalable web platforms, CRM and ERP systems, and business process automation tools.
          </p>
          <p style="margin-bottom: 16px;">
            Rather than relying on restrictive off-the-shelf software packages that limit business innovation, we work directly with founders, operations leaders, and enterprise teams to engineer bespoke digital products that fit their exact business logic.
          </p>
          <p>
            All company information within this demo website represents editable placeholders configured for easy customization by your team during actual commercial deployment.
          </p>
        </div>
        <div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">about-studio-philosophy.view</span>
            </div>
            {img_about_engineering}
          </div>
        </div>
      </div>

      <!-- Mission & Vision -->
      <div class="grid-2" style="margin-bottom: 60px;">
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>
          </div>
          <h3>Our Mission</h3>
          <p>
            To empower organizations with robust, custom-engineered software systems that automate manual inefficiencies, unify disconnected operations, and provide scalable digital foundations for long-term growth.
          </p>
        </div>
        <div class="card">
          <div class="card-icon-wrap">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          </div>
          <h3>Our Vision</h3>
          <p>
            To be recognized as a premier software development partner known for architectural clarity, unwavering code quality, transparent project delivery, and enduring engineering support.
          </p>
        </div>
      </div>

      <!-- Engineering Philosophy -->
      <div class="section-alt" style="padding: 48px; border-radius: var(--radius-lg); border: 1px solid var(--border-color); margin-bottom: 60px;">
        <div class="section-header text-left" style="margin-bottom: 32px;">
          <h2>OUR ENGINEERING <span class="text-gradient">PHILOSOPHY</span></h2>
          <p>Principles that guide every line of code, database schema, and interface interaction we create.</p>
        </div>

        <div class="grid-3">
          <div>
            <h4 class="text-cyan">1. Business-First Architecture</h4>
            <p>We believe technology is a means to a business outcome. We prioritize workflows, user adoption, and operational clarity over chasing transient tech fads.</p>
          </div>
          <div>
            <h4 class="text-blue">2. Defensible Code Quality</h4>
            <p>Clean, modular, well-documented code that any seasoned engineer can understand, maintain, and expand without painful friction.</p>
          </div>
          <div>
            <h4 class="text-violet">3. Security by Design</h4>
            <p>Every form input is validated, every endpoint authenticated, and every sensitive record guarded through strict role-based access controls.</p>
          </div>
          <div style="margin-top: 16px;">
            <h4 class="text-cyan">4. Predictable Scalability</h4>
            <p>Databases and API microservices structured to handle increased transaction loads without requiring disruptive architecture rewrites.</p>
          </div>
          <div style="margin-top: 16px;">
            <h4 class="text-blue">5. Transparent Delivery</h4>
            <p>Continuous communication, milestone reviews, clear change management, and documented deliverables at every stage of the lifecycle.</p>
          </div>
          <div style="margin-top: 16px;">
            <h4 class="text-violet">6. Long-Term Partnership</h4>
            <p>Our commitment extends past initial launch. We provide ongoing maintenance, platform modernization, and proactive performance tuning.</p>
          </div>
        </div>
      </div>

      <!-- How We Work With Clients -->
      <div class="section-header">
        <h2>HOW WE WORK <span class="text-gradient">WITH CLIENTS</span></h2>
        <p>A collaborative, disciplined engagement model built around accountability.</p>
      </div>

      <div class="grid-4" style="margin-bottom: 60px;">
        <div class="card">
          <h4>1. Requirement Alignment</h4>
          <p>We conduct in-depth scoping sessions to clearly define deliverables, project constraints, and feature priorities before writing any code.</p>
        </div>
        <div class="card">
          <h4>2. Iterative Milestones</h4>
          <p>We work in organized development sprints, providing client demonstrations and working builds for continuous feedback.</p>
        </div>
        <div class="card">
          <h4>3. Rigorous Quality Checks</h4>
          <p>Our software undergoes functional testing, regression audits, performance benchmarking, and edge-case validation.</p>
        </div>
        <div class="card">
          <h4>4. Smooth Handover</h4>
          <p>We deliver comprehensive technical documentation, administrative credentials, source code repositories, and user onboarding guidance.</p>
        </div>
      </div>

      <!-- CTA Block -->
      <div class="card" style="text-align: center; padding: 48px; background: var(--bg-card);">
        <h3>Ready to discuss your software vision?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our software engineering team to turn your operational requirements into a detailed technical project plan.
        </p>
        <div class="btn-group" style="justify-content: center;">
          <a href="request-quote.html" class="btn btn-primary">Request a Project Quote</a>
          <a href="contact.html" class="btn btn-outline">Contact Us</a>
        </div>
      </div>
    </div>
  </section>
"""
}

# Continue defining pages systematically...
print("Generated index.html and about.html definitions.")
