"""
Module 1: Service Pages Generator (custom-software, web-applications, saas, crm, erp, pos, inventory, ecommerce)
"""
from build_all_pages import register_image, pages_data

# 3. CUSTOM SOFTWARE DEVELOPMENT (custom-software.html)
img_custom_software = register_image(
    "service-custom-software.jpg", "custom-software.html", "Custom Software Overview", "16:10", "1600x1000", "Landscape",
    "Bespoke Enterprise Software Architecture & Management Suite",
    "High-tech enterprise software architecture layout showing custom data models, workflow engines, and modular service hubs.",
    {
        "subject": "Modular enterprise software dashboard showing customized business operations, internal tooling, and microservice status",
        "environment": "Dark aesthetic software engineering console with glowing data pipelines and sleek typography",
        "composition": "Elevated perspective of high-density business software control panel",
        "camera": "Isometric 3D render",
        "lighting": "Electric blue and cyan pipeline illumination with dark navy ambient shadow",
        "background": "#080D18 cyber grid background",
        "colors": "#080D18, #141F32, #4F8CFF, #36D6E8",
        "style": "Modern enterprise software product mockup",
        "mood": "Reliable, technical, robust",
        "ratio": "16:10",
        "negative": "clipart, low resolution, messy graphics, stock photo people"
    }
)

pages_data["custom-software.html"] = {
    "title": "Custom Software Development Services — Enterprise Applications & Systems",
    "desc": "Custom software development engineered to solve operational inefficiencies, eliminate spreadsheets, and automate internal business processes.",
    "keywords": "Custom Software Development, Business Software Development, Enterprise Applications, Custom Management Systems, Workflow Applications, Legacy Software Modernization",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Bespoke Engineering</span>
        </div>
        <h1>CUSTOM SOFTWARE <span class="text-gradient">DEVELOPMENT SERVICES</span></h1>
        <p class="lead">Purpose-built software systems engineered around your exact company operations, business logic, and security requirements.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>ENGINEERED AROUND YOUR EXACT WORKFLOWS</h2>
          <p style="margin-bottom: 16px;">
            Every growing business encounters the limits of commercial off-the-shelf software. Generic platforms force you to compromise your processes, incur recurring seat-license inflation, and maintain fragile workarounds.
          </p>
          <p style="margin-bottom: 20px;">
            We architect and build tailored software solutions that align 100% with your operational reality. From multi-department workflow management to complex data processing engines, our custom software scales with your organization.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Request a Custom Software Quote</a>
            <a href="#services-breakdown" class="btn btn-outline">Explore Capabilities</a>
          </div>
        </div>
        <div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">custom-system-architecture.view</span>
            </div>
            {img_custom_software}
          </div>
        </div>
      </div>

      <!-- Core Capabilities Grid -->
      <div id="services-breakdown" class="section-header">
        <h2>SOLUTIONS WE <span class="text-gradient">DESIGN & ENGINEER</span></h2>
        <p>Comprehensive custom application development across all enterprise tiers.</p>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <div class="card">
          <h4>Business Software Development</h4>
          <p><strong>What it is:</strong> Tailored operational systems that automate daily administration, track work orders, and coordinate departmental tasks.</p>
          <p><strong>Problems solved:</strong> Disconnected spreadsheets, human data-entry errors, and lack of real-time management visibility.</p>
          <div class="card-footer">
            <span class="tag-pill">Workflow Engine</span>
            <span class="tag-pill">Centralized Database</span>
          </div>
        </div>

        <div class="card">
          <h4>Enterprise Applications</h4>
          <p><strong>What it is:</strong> High-concurrency enterprise portals featuring granular role-based permissions, comprehensive audit trails, and multi-tenant scaling.</p>
          <p><strong>Problems solved:</strong> Fragmented compliance monitoring, unauthorized data access, and bottlenecked operational reviews.</p>
          <div class="card-footer">
            <span class="tag-pill">Role-Based Access</span>
            <span class="tag-pill">Audit Trails</span>
          </div>
        </div>

        <div class="card">
          <h4>Custom Management Systems</h4>
          <p><strong>What it is:</strong> Unified portals that bridge field operations, warehouse dispatch, supplier communications, and invoicing in real-time.</p>
          <p><strong>Problems solved:</strong> Information silos between warehouse staff, procurement managers, and accounting departments.</p>
          <div class="card-footer">
            <span class="tag-pill">Operations Sync</span>
            <span class="tag-pill">Department Hub</span>
          </div>
        </div>

        <div class="card">
          <h4>Workflow Applications</h4>
          <p><strong>What it is:</strong> Multi-step state machine applications that route tasks, manage manager sign-offs, and trigger automated alerts.</p>
          <p><strong>Problems solved:</strong> Stalled client approvals, lost email authorization chains, and unmonitored SLA breaches.</p>
          <div class="card-footer">
            <span class="tag-pill">State Machines</span>
            <span class="tag-pill">SLA Routing</span>
          </div>
        </div>

        <div class="card">
          <h4>Internal Business Tools</h4>
          <p><strong>What it is:</strong> High-efficiency staff consoles, support ticketing dashboards, reconciliation tools, and data migration utilities.</p>
          <p><strong>Problems solved:</strong> Slow customer issue resolution times and clunky administrative back-office panels.</p>
          <div class="card-footer">
            <span class="tag-pill">Admin Tooling</span>
            <span class="tag-pill">Productivity</span>
          </div>
        </div>

        <div class="card">
          <h4>Legacy Application Modernization</h4>
          <p><strong>What it is:</strong> Re-architecting outdated desktop or monolithic applications into clean, secure, cloud-ready web systems.</p>
          <p><strong>Problems solved:</strong> Vulnerable unsupported databases, slow user experiences, and inability to integrate with modern web APIs.</p>
          <div class="card-footer">
            <span class="tag-pill">Cloud Migration</span>
            <span class="tag-pill">API Ready</span>
          </div>
        </div>
      </div>

      <!-- Lifecycle of a Custom Software Project -->
      <div class="section-alt" style="padding: 48px; border-radius: var(--radius-lg); border: 1px solid var(--border-color); margin-bottom: 60px;">
        <div class="section-header text-left" style="margin-bottom: 32px;">
          <h2>LIFECYCLE OF A <span class="text-gradient">CUSTOM SOFTWARE PROJECT</span></h2>
          <p>How an enterprise software system moves from initial discovery to reliable ongoing operation.</p>
        </div>

        <div class="grid-4">
          <div class="card" style="background: #0d1522;">
            <div class="tag-pill" style="color:var(--accent-cyan); align-self:flex-start; margin-bottom:10px;">STAGE 1</div>
            <h4>Business Analysis & Architecture</h4>
            <p>We interview domain experts, map existing relational entities, document user permissions, and establish technical specifications.</p>
          </div>
          <div class="card" style="background: #0d1522;">
            <div class="tag-pill" style="color:var(--accent-primary); align-self:flex-start; margin-bottom:10px;">STAGE 2</div>
            <h4>Interactive Prototype</h4>
            <p>Our UX designers create full wireframes and clickable interface flows so your team can test usability before backend coding starts.</p>
          </div>
          <div class="card" style="background: #0d1522;">
            <div class="tag-pill" style="color:var(--accent-violet); align-self:flex-start; margin-bottom:10px;">STAGE 3</div>
            <h4>Agile Sprint Engineering</h4>
            <p>Engineers build backend services, database migrations, and clean UI components in 2-week deliverable sprint cycles with live demos.</p>
          </div>
          <div class="card" style="background: #0d1522;">
            <div class="tag-pill" style="color:var(--accent-cyan); align-self:flex-start; margin-bottom:10px;">STAGE 4</div>
            <h4>Deployment & Handover</h4>
            <p>Production server hardening, data migration, staff training manuals, API documentation, and scheduled maintenance support.</p>
          </div>
        </div>
      </div>

      <!-- CTA -->
      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Need custom software engineered for your business?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our software architects to review your requirements, explore technology options, and receive a structured implementation plan.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request a Custom Software Quote</a>
      </div>
    </div>
  </section>
"""
}

# 4. WEB APPLICATION DEVELOPMENT (web-applications.html)
img_web_apps = register_image(
    "service-web-applications.jpg", "web-applications.html", "Web Applications Overview", "16:10", "1600x1000", "Landscape",
    "Modern Web Application Dashboard & Portal Interface",
    "Clean enterprise web application dashboard showing responsive navigation, real-time data tables, and charting components.",
    {
        "subject": "Modern responsive enterprise web application interface preview on laptop and desktop monitors",
        "environment": "Modern dark mode software interface with glassmorphism header and cyan data visualization cards",
        "composition": "Frontal 3/4 perspective shot of web application dashboard with floating notification cards",
        "camera": "Direct camera angle with subtle depth",
        "lighting": "Soft cyan and blue ambient rim light across the dark card borders",
        "background": "#080D18 backdrop with soft blurred glow",
        "colors": "#080D18, #141F32, #36D6E8, #4F8CFF",
        "style": "High-fidelity digital SaaS product mockup",
        "mood": "Sleek, responsive, high-velocity",
        "ratio": "16:10",
        "negative": "stock handshakes, physical people, messy screen, low resolution"
    }
)

pages_data["web-applications.html"] = {
    "title": "Web Application Development Services — Portals, Dashboards & Platforms",
    "desc": "Custom web applications, client portals, admin dashboards, and employee workflow platforms built for high performance and security.",
    "keywords": "Web Application Development, Business Web Portals, Admin Dashboards, Customer Portals, Workflow Platforms, Reporting Applications",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Web Engineering</span>
        </div>
        <h1>WEB APPLICATION <span class="text-gradient">DEVELOPMENT SERVICES</span></h1>
        <p class="lead">Fast, responsive, secure web platforms engineered for business portals, executive dashboards, and high-volume customer interactions.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>SECURE, RESPONSIVE & CLOUD-READY WEB PLATFORMS</h2>
          <p style="margin-bottom: 16px;">
            Modern businesses require web applications that load instantly across all devices, maintain bulletproof security, and provide smooth desktop-class user experiences.
          </p>
          <p style="margin-bottom: 20px;">
            We engineer custom business portals, internal management tools, and customer-facing web platforms using clean architectures. Our focus on semantic markup, accessible navigation, and optimized frontend assets ensures fast load speeds and reliable uptime.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Discuss Your Web App</a>
            <a href="#web-app-types" class="btn btn-outline">Explore Web App Types</a>
          </div>
        </div>
        <div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">enterprise-web-portal.app</span>
            </div>
            {img_web_apps}
          </div>
        </div>
      </div>

      <!-- Web Application Categories -->
      <div id="web-app-types" class="section-header">
        <h2>WEB APPLICATIONS <span class="text-gradient">WE ENGINEER</span></h2>
        <p>From client-facing self-service portals to mission-critical internal admin panels.</p>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <div class="card">
          <h4>Custom Web Portals</h4>
          <p>Secure client and vendor portals that allow external stakeholders to submit inquiries, review project progress, and download approved invoices.</p>
          <span class="tag-pill">Client Self-Service</span>
        </div>
        <div class="card">
          <h4>Executive Admin Dashboards</h4>
          <p>High-density analytics panels that aggregate live sales data, operational KPIs, server status metrics, and department throughput in real time.</p>
          <span class="tag-pill">Executive Visibility</span>
        </div>
        <div class="card">
          <h4>Employee Management Applications</h4>
          <p>Centralized employee self-service hubs for leave requests, document verification, performance check-ins, and team announcements.</p>
          <span class="tag-pill">HR & Operations</span>
        </div>
        <div class="card">
          <h4>Workflow Management Platforms</h4>
          <p>Digital dispatch boards, job ticketing systems, and multi-user editorial queues that keep cross-functional teams synchronized.</p>
          <span class="tag-pill">Task Pipelines</span>
        </div>
        <div class="card">
          <h4>Reporting & Data Query Apps</h4>
          <p>Interactive web interfaces that allow non-technical business managers to query historical records, export spreadsheets, and generate PDF summaries.</p>
          <span class="tag-pill">Reporting Engine</span>
        </div>
        <div class="card">
          <h4>Web-Based Management Systems</h4>
          <p>Browser-accessible platforms that replace obsolete desktop installations, enabling seamless remote work without complex VPN overhead.</p>
          <span class="tag-pill">Remote Access</span>
        </div>
      </div>

      <!-- Architectural Capabilities Breakdown -->
      <div class="section-alt" style="padding: 48px; border-radius: var(--radius-lg); border: 1px solid var(--border-color); margin-bottom: 60px;">
        <div class="section-header text-left" style="margin-bottom: 32px;">
          <h2>WEB ARCHITECTURE <span class="text-gradient">AS A SERVICE CAPABILITY</span></h2>
          <p>The engineering layers behind every reliable web application we deploy.</p>
        </div>

        <div class="grid-3">
          <div>
            <h4 class="text-cyan">Frontend Engineering</h4>
            <p>Responsive, lightweight HTML5, CSS3, and modern vanilla or component-driven JavaScript designed for sub-second interactions and high accessibility.</p>
          </div>
          <div>
            <h4 class="text-blue">Backend Architecture</h4>
            <p>Modular microservices or structured monolithic backends written in Node.js, Python, or PHP, engineered for high concurrency and clear API boundaries.</p>
          </div>
          <div>
            <h4 class="text-violet">Database Integration</h4>
            <p>Optimized relational (PostgreSQL, MySQL) and document (MongoDB) database integrations with query caching and parameterized safeguards.</p>
          </div>
          <div style="margin-top: 20px;">
            <h4 class="text-cyan">Authentication & RBAC</h4>
            <p>Session management, JWT tokens, OAuth providers, and granular permission matrices that restrict administrative actions to verified roles.</p>
          </div>
          <div style="margin-top: 20px;">
            <h4 class="text-blue">API Integrations</h4>
            <p>Seamless communication with external payment gateways, CRM databases, email deliverability servers, and SMS verification networks.</p>
          </div>
          <div style="margin-top: 20px;">
            <h4 class="text-violet">Testing & CI/CD Deployment</h4>
            <p>Automated test suites, browser compatibility tests, Docker containerization, and static/cloud hosting deployments with zero downtime.</p>
          </div>
        </div>
      </div>

      <!-- Notice -->
      <div style="text-align:center; margin-bottom: 40px;">
        <span class="demo-disclaimer-badge">Demonstration Notice: This website itself is a static frontend showcase illustrating service capabilities.</span>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Ready to build your company's web application?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our development team to discuss your user flows, data model, and deployment requirements.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request a Web Application Quote</a>
      </div>
    </div>
  </section>
"""
}

# 5. SAAS DEVELOPMENT (saas-development.html)
img_saas_dashboard = register_image(
    "demo-saas-dashboard.jpg", "saas-development.html", "SaaS Admin Mockup", "16:10", "1600x1000", "Landscape",
    "Multi-Tenant SaaS Administration & MRR Telemetry Dashboard",
    "Clean SaaS admin dashboard preview with active subscriber graphs, monthly recurring revenue charts, and tenant usage metrics.",
    {
        "subject": "Modern SaaS administrative platform dashboard showing MRR curve, active tenant breakdown, and usage quotas",
        "environment": "Sleek dark mode analytics console with glowing electric blue and violet metric cards",
        "composition": "Centered isometric presentation of SaaS product metrics",
        "camera": "Slightly angled 3D camera view with crisp details",
        "lighting": "Deep contrast with electric blue accents and soft cyan ambient illumination",
        "background": "#080D18 tech background",
        "colors": "#080D18, #141F32, #4F8CFF, #9878FF, #36D6E8",
        "style": "High-fidelity digital SaaS product mockup",
        "mood": "High-growth, enterprise, visionary",
        "ratio": "16:10",
        "negative": "stock photos of people, paper documents, blur, low resolution"
    }
)

pages_data["saas-development.html"] = {
    "title": "SaaS Product Development Services — Multi-Tenant Cloud Architecture",
    "desc": "End-to-end SaaS application engineering: multi-tenant architecture, subscription billing, tenant isolation, and self-service analytics.",
    "keywords": "SaaS Product Development, Multi-Tenant Architecture, SaaS Subscription Management, Role-Based Access, SaaS Admin Dashboard",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Cloud Products</span>
        </div>
        <h1>SAAS PRODUCT <span class="text-gradient">DEVELOPMENT SERVICES</span></h1>
        <p class="lead">From initial prototype to multi-tenant cloud platforms, we engineer scalable SaaS products designed for high recurring revenue.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>ENGINEERING DIGITAL PRODUCTS THAT SCALE</h2>
          <p style="margin-bottom: 16px;">
            Launching a modern Software-as-a-Service (SaaS) platform requires far more than basic feature coding. It demands rock-solid multi-tenant data isolation, automated subscription life-cycle management, fine-grained access tiers, and resilient cloud architectures.
          </p>
          <p style="margin-bottom: 20px;">
            Whether you are a startup building a disruptive B2B product or an established enterprise commercializing internal software into a SaaS revenue engine, we provide end-to-end software architecture and development.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Build Your SaaS Platform</a>
            <a href="#saas-interactive-demo" class="btn btn-secondary">Interact With Demo Dashboard</a>
          </div>
        </div>
        <div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">saas-cloud-console.sys</span>
              <span class="badge-status badge-new">Demo Mockup</span>
            </div>
            {img_saas_dashboard}
          </div>
        </div>
      </div>

      <!-- Interactive SaaS Dashboard Simulation -->
      <div id="saas-interactive-demo" class="dashboard-demo-box">
        <div class="dashboard-toolbar">
          <div>
            <h4 style="margin-bottom: 4px;">SaaS Telemetry & Revenue Dashboard (Interactive Demo)</h4>
            <span class="dashboard-notice">Illustrative Demo Data — Simulated Metrics for Visual Demonstration</span>
          </div>
          <div class="filter-group">
            <span style="font-size:0.8rem; color:var(--text-muted); margin-right:4px;">Timeframe:</span>
            <button class="filter-btn saas-time-btn" data-time="7d">7D</button>
            <button class="filter-btn saas-time-btn active" data-time="30d">30D</button>
            <button class="filter-btn saas-time-btn" data-time="90d">90D</button>
            <button class="filter-btn saas-time-btn" data-time="1y">1Y</button>
          </div>
        </div>

        <div style="padding: 24px;">
          <div class="grid-4" style="margin-bottom: 24px;">
            <div class="card" style="padding: 20px; background: #0d1522;">
              <span style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Monthly Recurring Revenue</span>
              <h3 id="saas-mrr" style="color:var(--accent-cyan); font-family:var(--font-mono); margin: 8px 0 4px 0;">$58,900</h3>
              <span id="saas-growth" style="font-size:0.8rem; color:#10B981; font-weight:600;">+12.6% vs last period</span>
            </div>
            <div class="card" style="padding: 20px; background: #0d1522;">
              <span style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Active Tenants / Users</span>
              <h3 id="saas-users" style="color:var(--accent-primary); font-family:var(--font-mono); margin: 8px 0 4px 0;">18,450</h3>
              <span style="font-size:0.8rem; color:var(--text-muted);">across 420 organization accounts</span>
            </div>
            <div class="card" style="padding: 20px; background: #0d1522;">
              <span style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Churn Rate</span>
              <h3 id="saas-churn" style="color:#34D399; font-family:var(--font-mono); margin: 8px 0 4px 0;">1.2%</h3>
              <span style="font-size:0.8rem; color:var(--text-muted);">Industry benchmark: 3.5%</span>
            </div>
            <div class="card" style="padding: 20px; background: #0d1522;">
              <span style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">API Requests</span>
              <h3 id="saas-api" style="color:var(--accent-violet); font-family:var(--font-mono); margin: 8px 0 4px 0;">10.8M</h3>
              <span style="font-size:0.8rem; color:var(--text-muted);">99.98% successful responses</span>
            </div>
          </div>

          <div class="grid-2">
            <div class="card" style="background:#090f19; padding: 20px;">
              <h4 style="margin-bottom: 12px;">Active Subscription Tiers (Demo Distribution)</h4>
              <ul style="display:flex; flex-direction:column; gap:12px; font-size:0.875rem;">
                <li style="display:flex; justify-content:space-between; border-bottom:1px solid rgba(255,255,255,0.05); padding-bottom:6px;">
                  <span>Starter Tier ($49/mo)</span>
                  <span style="font-family:var(--font-mono); color:var(--accent-cyan);">245 accounts (58%)</span>
                </li>
                <li style="display:flex; justify-content:space-between; border-bottom:1px solid rgba(255,255,255,0.05); padding-bottom:6px;">
                  <span>Growth Tier ($149/mo)</span>
                  <span style="font-family:var(--font-mono); color:var(--accent-primary);">135 accounts (32%)</span>
                </li>
                <li style="display:flex; justify-content:space-between; border-bottom:1px solid rgba(255,255,255,0.05); padding-bottom:6px;">
                  <span>Enterprise Dedicated ($499/mo)</span>
                  <span style="font-family:var(--font-mono); color:var(--accent-violet);">40 accounts (10%)</span>
                </li>
              </ul>
            </div>
            <div class="card" style="background:#090f19; padding: 20px;">
              <h4 style="margin-bottom: 12px;">Infrastructure Health (Simulated)</h4>
              <div style="display:flex; flex-direction:column; gap:10px; font-size:0.85rem;">
                <div>
                  <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                    <span>Database CPU Load</span>
                    <span style="color:var(--accent-cyan); font-family:var(--font-mono);">24%</span>
                  </div>
                  <div style="height:6px; background:#141f32; border-radius:3px; overflow:hidden;">
                    <div style="width:24%; height:100%; background:var(--accent-cyan);"></div>
                  </div>
                </div>
                <div>
                  <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                    <span>API Gateway Latency</span>
                    <span style="color:#10B981; font-family:var(--font-mono);">38ms</span>
                  </div>
                  <div style="height:6px; background:#141f32; border-radius:3px; overflow:hidden;">
                    <div style="width:18%; height:100%; background:#10B981;"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- SaaS Journey Timeline -->
      <div class="section-alt" style="padding: 48px; border-radius: var(--radius-lg); border: 1px solid var(--border-color); margin-bottom: 60px;">
        <div class="section-header text-left" style="margin-bottom: 32px;">
          <h2>THE SAAS DEVELOPMENT <span class="text-gradient">JOURNEY</span></h2>
          <p>Our systematic path from concept validation to sustainable recurring software revenue.</p>
        </div>

        <div class="workflow-diagram">
          <div class="workflow-node active" style="min-width:110px;">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STEP 01</div>
            <strong>Idea & Scope</strong>
          </div>
          <div class="workflow-arrow">&rarr;</div>
          <div class="workflow-node" style="min-width:110px;">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STEP 02</div>
            <strong>Discovery</strong>
          </div>
          <div class="workflow-arrow">&rarr;</div>
          <div class="workflow-node" style="min-width:110px;">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STEP 03</div>
            <strong>UI/UX Design</strong>
          </div>
          <div class="workflow-arrow">&rarr;</div>
          <div class="workflow-node" style="min-width:110px;">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STEP 04</div>
            <strong>Architecture</strong>
          </div>
          <div class="workflow-arrow">&rarr;</div>
          <div class="workflow-node" style="min-width:110px;">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STEP 05</div>
            <strong>Development</strong>
          </div>
          <div class="workflow-arrow">&rarr;</div>
          <div class="workflow-node" style="min-width:110px;">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STEP 06</div>
            <strong>Testing & Launch</strong>
          </div>
          <div class="workflow-arrow">&rarr;</div>
          <div class="workflow-node" style="min-width:110px;">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STEP 07</div>
            <strong>Iteration</strong>
          </div>
        </div>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Ready to build your next-generation SaaS product?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Schedule an architectural planning session to define your SaaS data model, pricing strategy, and launch timeline.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request a SaaS Product Quote</a>
      </div>
    </div>
  </section>
"""
}

# 6. CRM SOFTWARE DEVELOPMENT (crm-development.html)
img_crm_dashboard = register_image(
    "demo-crm-dashboard.jpg", "crm-development.html", "CRM Dashboard Interface", "16:10", "1600x1000", "Landscape",
    "Interactive CRM Lead Management & Sales Pipeline Dashboard",
    "Sales management dashboard featuring lead status tags, pipeline stages, contact history, and next follow-up cadences.",
    {
        "subject": "Modern CRM web application interface preview showing lead pipelines, conversation timelines, and sales reps",
        "environment": "Sleek dark theme CRM dashboard with illuminated stage badges and contact metrics",
        "composition": "Straight-on UI screen display with sharp typographic hierarchy",
        "camera": "Direct viewport angle",
        "lighting": "Clean internal UI illumination with vibrant status badges (New, Interested, Converted)",
        "background": "#080D18 background",
        "colors": "#080D18, #141F32, #4F8CFF, #36D6E8, #10B981",
        "style": "High-fidelity digital product UI mockup",
        "mood": "High conversion, structured, disciplined sales workflow",
        "ratio": "16:10",
        "negative": "stock photo of sales team shaking hands, generic clipart, low resolution"
    }
)

pages_data["crm-development.html"] = {
    "title": "CRM Software Development Services — Custom Sales Pipelines & Lead Systems",
    "desc": "Custom CRM software development: lead capture, sales pipelines, automated follow-up cadences, contact histories, and executive sales analytics.",
    "keywords": "CRM Software Development, Custom CRM Solutions, Lead Management Software, Sales Pipeline System, Contact Management, CRM Dashboard",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Sales Operations</span>
        </div>
        <h1>CRM SOFTWARE <span class="text-gradient">DEVELOPMENT SERVICES</span></h1>
        <p class="lead">Custom CRM platforms engineered to capture every lead, streamline sales follow-ups, and organize customer relationships.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>STOP LOSING VALUABLE LEADS IN SPREADSHEETS</h2>
          <p style="margin-bottom: 16px;">
            Standard commercial CRMs charge hefty per-user subscription fees while cluttering your sales reps with dozens of irrelevant buttons and confusing menus they never touch.
          </p>
          <p style="margin-bottom: 20px;">
            We build custom CRM software centered squarely on your sales qualification process, team ownership structures, and customer communication channels.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Request CRM Development Quote</a>
            <a href="#crm-interactive-demo" class="btn btn-secondary">Test CRM Demo Below</a>
          </div>
        </div>
        <div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">crm-pipeline-view.app</span>
              <span class="badge-status badge-new">Demo Mockup</span>
            </div>
            {img_crm_dashboard}
          </div>
        </div>
      </div>

      <!-- Interactive CRM Dashboard Demonstration -->
      <div id="crm-interactive-demo" class="dashboard-demo-box">
        <div class="dashboard-toolbar">
          <div>
            <h4 style="margin-bottom: 4px;">CRM Lead Pipeline Management (Interactive Frontend Demo)</h4>
            <span class="dashboard-notice">Illustrative Demo Data — Filter, search, and click "Next Stage" to test UI interactions</span>
          </div>
          <div style="display:flex; align-items:center; gap:12px; flex-wrap:wrap;">
            <input type="text" id="crm-search-input" class="form-control" style="width:200px; padding:6px 12px; font-size:0.8125rem;" placeholder="Search demo leads...">
            <div class="filter-group">
              <button class="filter-btn crm-filter-btn active" data-filter="All">All</button>
              <button class="filter-btn crm-filter-btn" data-filter="New Lead">New</button>
              <button class="filter-btn crm-filter-btn" data-filter="Interested">Interested</button>
              <button class="filter-btn crm-filter-btn" data-filter="Follow-Up">Follow-Up</button>
              <button class="filter-btn crm-filter-btn" data-filter="Converted">Converted</button>
            </div>
            <span id="crm-total-count" style="font-size:0.8125rem; font-family:var(--font-mono); color:var(--accent-cyan);">6 Leads</span>
          </div>
        </div>

        <div class="table-responsive">
          <table class="demo-table">
            <thead>
              <tr>
                <th>Lead / Company</th>
                <th>Phone</th>
                <th>Email</th>
                <th>Source</th>
                <th>Stage Status</th>
                <th>Next Follow-Up</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody id="crm-leads-tbody">
              <!-- Rendered via main.js -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Core CRM Modules Breakdown -->
      <div class="section-header">
        <h2>KEY MODULES IN A <span class="text-gradient">CUSTOM CRM</span></h2>
        <p>Architected around your sales team's exact daily tasks.</p>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <div class="card">
          <h4>Lead Capture & Intake</h4>
          <p>Instant ingestion from website forms, external ads, email inquiries, and phone switchboards with automatic rep assignment.</p>
        </div>
        <div class="card">
          <h4>Sales Pipeline & Stages</h4>
          <p>Custom stages reflecting your real closing steps: Discovery &rarr; Proposal &rarr; Review &rarr; Negotiation &rarr; Converted.</p>
        </div>
        <div class="card">
          <h4>Follow-Up Automation</h4>
          <p>Automated reminders, scheduled callback notifications, and email alerts ensure no prospect is ever forgotten.</p>
        </div>
        <div class="card">
          <h4>Activity & Call History</h4>
          <p>Centralized activity timelines documenting every call note, meeting outcome, quotation version, and message sent.</p>
        </div>
        <div class="card">
          <h4>User Roles & Permissions</h4>
          <p>Granular access control allowing sales reps to see only assigned prospects while managers monitor full team pipeline volume.</p>
        </div>
        <div class="card">
          <h4>Executive Conversion Analytics</h4>
          <p>Visual reports on lead velocity, source effectiveness, rep closing ratios, and projected pipeline revenue.</p>
        </div>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Ready to streamline your sales operations with custom CRM?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Let us engineer a dedicated CRM platform designed specifically around your customer lifecycle.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request a CRM Development Quote</a>
      </div>
    </div>
  </section>
"""
}

# 7. ERP SOFTWARE DEVELOPMENT (erp-development.html)
img_erp_dashboard = register_image(
    "demo-erp-dashboard.jpg", "erp-development.html", "ERP Dashboard Interface", "16:10", "1600x1000", "Landscape",
    "Unified Enterprise Resource Planning (ERP) Multi-Module Control Suite",
    "Comprehensive ERP dashboard interface preview showing interconnected modules for Sales, Inventory, Purchasing, and Finance.",
    {
        "subject": "Enterprise resource planning software dashboard showing unified business metrics across inventory, purchase orders, and accounts",
        "environment": "Dark executive software interface with multi-tab module navigation and real-time ledger entries",
        "composition": "Slight perspective view of multi-column enterprise ERP dashboard",
        "camera": "Wide angle viewport capture",
        "lighting": "Deep navy background with cyan border highlights and electric blue active module indicators",
        "background": "#080D18 background",
        "colors": "#080D18, #141F32, #4F8CFF, #36D6E8",
        "style": "Enterprise product design mockup",
        "mood": "Systematic, robust, executive-grade",
        "ratio": "16:10",
        "negative": "stock handshake photos, realistic people, messy clip art, low resolution"
    }
)

pages_data["erp-development.html"] = {
    "title": "ERP Software Development Services — Custom Enterprise Resource Planning",
    "desc": "Custom ERP software development: connect purchasing, sales, finance, inventory, multi-branch operations, and vendor management.",
    "keywords": "ERP Software Development, Custom ERP Systems, Enterprise Resource Planning, Inventory Management, Multi-Branch ERP, Finance Software",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Enterprise Operations</span>
        </div>
        <h1>ERP SOFTWARE <span class="text-gradient">DEVELOPMENT SERVICES</span></h1>
        <p class="lead">Centralize your purchasing, inventory, sales, multi-branch logistics, and accounting into one unified software platform.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>UNIFY YOUR ENTIRE BUSINESS UNDER ONE SYSTEM</h2>
          <p style="margin-bottom: 16px;">
            When your business grows, disjointed software tools create dangerous blind spots. Purchasing orders fail to sync with inventory counts, sales staff sell out-of-stock items, and financial reconciliation becomes an endless nightmare.
          </p>
          <p style="margin-bottom: 20px;">
            Our custom ERP development bridges these departments into a single source of truth. Every transaction automatically updates downstream inventory, vendor payables, and general ledger accounts.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Request ERP Quote</a>
            <a href="#erp-interactive-demo" class="btn btn-secondary">Explore Interactive ERP Demo</a>
          </div>
        </div>
        <div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">enterprise-erp-core.view</span>
              <span class="badge-status badge-new">Demo Mockup</span>
            </div>
            {img_erp_dashboard}
          </div>
        </div>
      </div>

      <!-- Interactive ERP Dashboard Demo -->
      <div id="erp-interactive-demo" class="dashboard-demo-box">
        <div class="dashboard-toolbar">
          <div>
            <h4 style="margin-bottom: 4px;">ERP Operations Suite (Interactive Frontend Demo)</h4>
            <span class="dashboard-notice">Illustrative Demo Data — Click module tabs to preview data relationships</span>
          </div>
          <div class="filter-group">
            <button class="filter-btn erp-tab-btn active" data-target="erp-overview">Overview</button>
            <button class="filter-btn erp-tab-btn" data-target="erp-sales">Sales Orders</button>
            <button class="filter-btn erp-tab-btn" data-target="erp-inventory">Live Inventory</button>
            <button class="filter-btn erp-tab-btn" data-target="erp-purchasing">Purchasing</button>
            <button class="filter-btn erp-tab-btn" data-target="erp-finance">Finance</button>
          </div>
        </div>

        <!-- Relationship Breadcrumb -->
        <div style="background:#090f19; padding: 14px 24px; border-bottom: 1px solid var(--border-color); display:flex; align-items:center; gap:8px; font-size:0.8125rem; overflow-x:auto;">
          <span style="color:var(--text-muted);">Data Flow Pipeline:</span>
          <span class="tag-pill" style="color:var(--accent-cyan);">Sales Order</span>
          <span style="color:var(--accent-primary);">&rarr;</span>
          <span class="tag-pill" style="color:var(--accent-cyan);">Inventory Allocation</span>
          <span style="color:var(--accent-primary);">&rarr;</span>
          <span class="tag-pill" style="color:var(--accent-cyan);">PO Generation</span>
          <span style="color:var(--accent-primary);">&rarr;</span>
          <span class="tag-pill" style="color:var(--accent-cyan);">General Ledger Entry</span>
          <span style="color:var(--accent-primary);">&rarr;</span>
          <span class="tag-pill" style="color:var(--accent-cyan);">Audit Reporting</span>
        </div>

        <div style="padding: 24px;">
          <!-- Panel 1: Overview -->
          <div id="erp-overview" class="erp-tab-panel">
            <div class="grid-4" style="margin-bottom: 24px;">
              <div class="card" style="padding: 16px; background:#0d1522;">
                <span style="font-size:0.75rem; color:var(--text-muted);">TOTAL REVENUE (MTD)</span>
                <h3 style="color:var(--accent-cyan); font-family:var(--font-mono); margin: 6px 0;">$348,200</h3>
                <span style="font-size:0.75rem; color:#10B981;">&uarr; 8.4% vs last month</span>
              </div>
              <div class="card" style="padding: 16px; background:#0d1522;">
                <span style="font-size:0.75rem; color:var(--text-muted);">PENDING SHIPMENTS</span>
                <h3 style="color:var(--accent-primary); font-family:var(--font-mono); margin: 6px 0;">42 Orders</h3>
                <span style="font-size:0.75rem; color:var(--text-muted);">14 dispatched today</span>
              </div>
              <div class="card" style="padding: 16px; background:#0d1522;">
                <span style="font-size:0.75rem; color:var(--text-muted);">OPEN PURCHASE ORDERS</span>
                <h3 style="color:var(--accent-violet); font-family:var(--font-mono); margin: 6px 0;">$89,450</h3>
                <span style="font-size:0.75rem; color:var(--text-muted);">6 vendor approvals pending</span>
              </div>
              <div class="card" style="padding: 16px; background:#0d1522;">
                <span style="font-size:0.75rem; color:var(--text-muted);">ACTIVE WAREHOUSES</span>
                <h3 style="color:#FBBF24; font-family:var(--font-mono); margin: 6px 0;">4 Branches</h3>
                <span style="font-size:0.75rem; color:var(--text-muted);">All nodes synchronized</span>
              </div>
            </div>
            <p style="font-size:0.875rem; color:var(--text-muted);">This overview aggregates cross-department metrics from illustrative ERP modules.</p>
          </div>

          <!-- Panel 2: Sales -->
          <div id="erp-sales" class="erp-tab-panel" style="display:none;">
            <table class="demo-table">
              <thead>
                <tr>
                  <th>Order #</th>
                  <th>Customer Account</th>
                  <th>Branch Origin</th>
                  <th>Total Amount</th>
                  <th>Inventory Status</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>SO-8921</code></td>
                  <td>Metro Electronics Ltd</td>
                  <td>Central Depot</td>
                  <td>$14,250.00</td>
                  <td><span class="badge-status badge-converted">Stock Allocated</span></td>
                </tr>
                <tr>
                  <td><code>SO-8922</code></td>
                  <td>Apex Retail Stores</td>
                  <td>North Branch</td>
                  <td>$8,400.00</td>
                  <td><span class="badge-status badge-followup">Awaiting Dispatch</span></td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Panel 3: Inventory -->
          <div id="erp-inventory" class="erp-tab-panel" style="display:none;">
            <table class="demo-table">
              <thead>
                <tr>
                  <th>SKU Code</th>
                  <th>Product Description</th>
                  <th>Primary Bin Location</th>
                  <th>Available Units</th>
                  <th>Threshold Status</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>SKU-5541</code></td>
                  <td>Industrial Power Controllers</td>
                  <td>Depot 1 - Row C4</td>
                  <td>240 Units</td>
                  <td><span class="badge-status badge-converted">Healthy Stock</span></td>
                </tr>
                <tr>
                  <td><code>SKU-3129</code></td>
                  <td>Micro-Sensor Modules</td>
                  <td>Depot 2 - Row B1</td>
                  <td>12 Units</td>
                  <td><span class="badge-status badge-danger">Reorder Required</span></td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Panel 4: Purchasing -->
          <div id="erp-purchasing" class="erp-tab-panel" style="display:none;">
            <table class="demo-table">
              <thead>
                <tr>
                  <th>PO Reference</th>
                  <th>Vendor Partner</th>
                  <th>Expected Receipt</th>
                  <th>Invoice Status</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>PO-4410</code></td>
                  <td>Global Micro-Components Inc</td>
                  <td>Nov 14, 2026</td>
                  <td><span class="badge-status badge-new">Pending Goods In</span></td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Panel 5: Finance -->
          <div id="erp-finance" class="erp-tab-panel" style="display:none;">
            <table class="demo-table">
              <thead>
                <tr>
                  <th>Ledger Ref</th>
                  <th>Account Category</th>
                  <th>Debit / Credit</th>
                  <th>Reconciliation</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>GL-9021</code></td>
                  <td>Accounts Receivable</td>
                  <td>+$22,650.00</td>
                  <td><span class="badge-status badge-converted">Reconciled</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Ready to unify your enterprise with custom ERP?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our software architects to review your departmental workflows and receive a structured ERP implementation plan.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request an ERP Development Quote</a>
      </div>
    </div>
  </section>
"""
}

# 8. POS AND BILLING SOFTWARE (pos-development.html)
img_pos_interface = register_image(
    "demo-pos-interface.jpg", "pos-development.html", "POS Interface Preview", "16:10", "1600x1000", "Landscape",
    "Modern Retail POS and Touchscreen Billing Interface",
    "Point-of-sale checkout screen with interactive product grid, live order cart, subtotal/tax calculations, and payment tenders.",
    {
        "subject": "Modern retail POS touch checkout screen with dark mode UI, quick-tap item buttons, and receipt summary panel",
        "environment": "High-tech retail terminal display with sharp pricing figures and barcode scan indicators",
        "composition": "Frontal angle of modern touchscreen POS terminal",
        "camera": "Direct flat display rendering",
        "lighting": "Clean UI backlight with electric blue highlights on active transaction buttons",
        "background": "#080D18 background",
        "colors": "#080D18, #141F32, #36D6E8, #4F8CFF",
        "style": "High-fidelity digital POS software mockup",
        "mood": "Fast, accurate, intuitive counter checkout",
        "ratio": "16:10",
        "negative": "stock photo of cashiers, physical currency bills, customers in line, low resolution"
    }
)

pages_data["pos-development.html"] = {
    "title": "POS and Billing Software Development — Retail & Restaurant Systems",
    "desc": "Custom Point of Sale (POS) and billing software: fast counter checkouts, barcode scanning, inventory deduction, and multi-register sync.",
    "keywords": "POS Software Development, Billing and Invoicing Software, Retail POS, Restaurant POS, Barcode Billing, Multi-Counter POS",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Point of Sale Systems</span>
        </div>
        <h1>POS & BILLING <span class="text-gradient">SOFTWARE DEVELOPMENT</span></h1>
        <p class="lead">High-speed, reliable point-of-sale systems built for retail outlets, multi-counter stores, and hospitality environments.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>RAPID COUNTER BILLING WITH INSTANT STOCK DEDUCTION</h2>
          <p style="margin-bottom: 16px;">
            Long queues at checkout cost retail businesses customers and revenue. Standard desktop billing software is often slow, crashes during network drops, and requires excessive keyboard navigation.
          </p>
          <p style="margin-bottom: 20px;">
            We engineer custom POS systems that optimize speed and accuracy. Featuring touch-first product grids, rapid barcode lookup, split payments, and instant inventory reconciliation, our POS software keeps your checkout lines moving.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Request a POS Quote</a>
            <a href="#pos-interactive-demo" class="btn btn-secondary">Test Interactive POS Demo</a>
          </div>
        </div>
        <div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">pos-terminal-billing.ui</span>
              <span class="badge-status badge-new">Demo Mockup</span>
            </div>
            {img_pos_interface}
          </div>
        </div>
      </div>

      <!-- Interactive POS Billing Demonstration -->
      <div id="pos-interactive-demo" class="dashboard-demo-box">
        <div class="dashboard-toolbar">
          <div>
            <h4 style="margin-bottom: 4px;">Retail POS Checkout Interface (Interactive Frontend Demo)</h4>
            <span class="dashboard-notice">Illustrative Demo Data — Click products to add to bill, adjust quantities, and test checkout</span>
          </div>
          <div style="display:flex; gap:8px;">
            <button id="pos-clear-btn" class="btn btn-sm btn-outline">Clear Cart</button>
          </div>
        </div>

        <div class="pos-grid">
          <!-- Left: Product Catalog -->
          <div>
            <div style="margin-bottom: 12px; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:0.85rem; font-weight:600; text-transform:uppercase; color:var(--text-muted);">Quick-Select Catalog (Demo Items)</span>
              <span style="font-size:0.75rem; color:var(--accent-cyan);">Tap item to add to bill</span>
            </div>
            <div id="pos-products-grid" class="pos-products">
              <!-- Rendered via main.js -->
            </div>
          </div>

          <!-- Right: Cart & Billing Panel -->
          <div class="pos-cart-panel">
            <div style="font-weight:700; font-size:1rem; border-bottom:1px solid var(--border-color); padding-bottom:10px; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span>Active Bill #POS-8841</span>
              <span style="font-size:0.75rem; color:var(--text-muted);">Terminal: 01</span>
            </div>

            <div id="pos-cart-list" class="pos-cart-items">
              <!-- Rendered via main.js -->
            </div>

            <div class="pos-summary-line">
              <span>Subtotal:</span>
              <span id="pos-subtotal" style="font-family:var(--font-mono);">$0.00</span>
            </div>
            <div class="pos-summary-line">
              <span>Tax (10% Demo):</span>
              <span id="pos-tax" style="font-family:var(--font-mono);">$0.00</span>
            </div>
            <div class="pos-total-line">
              <span>Total Due:</span>
              <span id="pos-total" style="color:var(--accent-cyan);">$0.00</span>
            </div>

            <button id="pos-checkout-btn" class="btn btn-primary" style="margin-top:16px; width:100%;">
              Process Demo Checkout &rarr;
            </button>
            <span style="font-size:0.7rem; color:var(--text-muted); text-align:center; margin-top:6px; display:block;">
              Simulation Only — No live payments or banking gateway interactions.
            </span>
          </div>
        </div>
      </div>

      <!-- POS Capabilities Breakdown -->
      <div class="section-header">
        <h2>CORE CAPABILITIES OF OUR <span class="text-gradient">POS SOFTWARE</span></h2>
        <p>Built for resilience, transaction volume, and operational simplicity.</p>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <div class="card">
          <h4>Barcode & Scanner Integration</h4>
          <p>Instant item scanning with support for 1D/2D barcodes, SKU lookups, and weighted scale data inputs.</p>
        </div>
        <div class="card">
          <h4>Multi-Counter & Register Sync</h4>
          <p>Manage multiple checkout lanes simultaneously with shared product catalogs and unified shift totals.</p>
        </div>
        <div class="card">
          <h4>Shift Reconciliation & Day-End Close</h4>
          <p>Automate cash drawer counts, card batch settlements, and manager variance reporting at shift changeovers.</p>
        </div>
        <div class="card">
          <h4>Tax Invoicing & Compliant Receipts</h4>
          <p>Print or email compliant invoices with customized tax breakdowns, business registration labels, and return terms.</p>
        </div>
        <div class="card">
          <h4>Real-Time Inventory Depletion</h4>
          <p>Every checkout immediately deducts stock units from the central inventory database, preventing overselling.</p>
        </div>
        <div class="card">
          <h4>Customer Loyalty & Purchase History</h4>
          <p>Quick lookup by phone number to apply customer loyalty discounts, review previous bills, and issue credits.</p>
        </div>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Need custom POS & billing software for your store?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Talk to our software engineers to design a checkout interface tailored to your specific store or restaurant operations.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request a POS Development Quote</a>
      </div>
    </div>
  </section>
"""
}

# 9. INVENTORY MANAGEMENT SOFTWARE (inventory-software.html)
img_inventory_dashboard = register_image(
    "demo-inventory-dashboard.jpg", "inventory-software.html", "Inventory Dashboard Preview", "16:10", "1600x1000", "Landscape",
    "Interactive Inventory & Warehouse Stock Tracking Dashboard",
    "Warehouse management dashboard showing SKU balance tables, reorder threshold alerts, supplier details, and stock-in/stock-out logs.",
    {
        "subject": "Warehouse inventory management software interface displaying SKU stock levels, bin locations, and automated reorder triggers",
        "environment": "Dark theme industrial software dashboard with clear status indicators and SKU tables",
        "composition": "Straight-on viewport angle showing tabular inventory metrics",
        "camera": "Direct digital rendering",
        "lighting": "Clean UI illumination with amber warning tags for low stock items and green tags for healthy stock",
        "background": "#080D18 background",
        "colors": "#080D18, #141F32, #36D6E8, #F59E0B, #10B981",
        "style": "High-fidelity digital product mockup",
        "mood": "Systematic, controlled, efficient warehouse management",
        "ratio": "16:10",
        "negative": "physical warehouse photos, forklift drivers, stock photo actors, blur"
    }
)

pages_data["inventory-software.html"] = {
    "title": "Inventory Management Software Development — Warehouse & Stock Tracking",
    "desc": "Custom inventory software development: product catalog, stock tracking, stock in/out, purchase orders, supplier management, and low stock alerts.",
    "keywords": "Inventory Management Software, Warehouse Management Software, Stock Tracking System, Barcode Inventory, Purchase Order Management, Low Stock Alerts",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Stock Control</span>
        </div>
        <h1>INVENTORY MANAGEMENT <span class="text-gradient">SOFTWARE DEVELOPMENT</span></h1>
        <p class="lead">Gain complete visibility over stock movements, bin locations, purchase orders, and supplier fulfillment.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>PREVENT STOCKOUTS & ELIMINATE INVENTORY DISCREPANCIES</h2>
          <p style="margin-bottom: 16px;">
            Inaccurate stock records lead to missed sales, unhappy customers, and capital tied up in slow-moving merchandise. Relying on spreadsheets or disconnected tools leads to human counting mistakes and delayed reorders.
          </p>
          <p style="margin-bottom: 20px;">
            We engineer custom inventory software that centralizes product catalogs, tracks stock movements across multiple storage warehouses, and automates supplier purchase orders before critical items run out.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Request an Inventory Quote</a>
            <a href="#inventory-interactive-demo" class="btn btn-secondary">Test Live Stock Demo</a>
          </div>
        </div>
        <div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">inventory-depot-tracker.ui</span>
              <span class="badge-status badge-new">Demo Mockup</span>
            </div>
            {img_inventory_dashboard}
          </div>
        </div>
      </div>

      <!-- Interactive Inventory Dashboard Demo -->
      <div id="inventory-interactive-demo" class="dashboard-demo-box">
        <div class="dashboard-toolbar">
          <div>
            <h4 style="margin-bottom: 4px;">Warehouse SKU Tracking & Adjustment (Interactive Demo)</h4>
            <span class="dashboard-notice">Illustrative Demo Data — Click "+5 In" or "-2 Out" to test real-time stock calculation</span>
          </div>
          <span style="font-size:0.8125rem; font-family:var(--font-mono); color:var(--accent-cyan);">Warehouse Node: Depot Alpha</span>
        </div>

        <div class="table-responsive">
          <table class="demo-table">
            <thead>
              <tr>
                <th>SKU Code</th>
                <th>Product Name</th>
                <th>Category</th>
                <th>Current Units</th>
                <th>Stock Status</th>
                <th>Simulate Stock Movement</th>
              </tr>
            </thead>
            <tbody id="inventory-tbody">
              <!-- Rendered via main.js -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Core Features Grid -->
      <div class="section-header">
        <h2>FEATURES OF OUR <span class="text-gradient">INVENTORY SYSTEMS</span></h2>
        <p>Engineered for high-volume distributors, retailers, and manufacturing depots.</p>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <div class="card">
          <h4>Multi-Warehouse Bin Tracking</h4>
          <p>Organize items by warehouse depot, zone aisle, shelf rack, and specific bin coordinate for rapid picking.</p>
        </div>
        <div class="card">
          <h4>Automated Low-Stock Warnings</h4>
          <p>Set minimum threshold triggers per SKU and receive automated notifications to replenish stock before depletion.</p>
        </div>
        <div class="card">
          <h4>Supplier & Purchase Order Workflows</h4>
          <p>Generate structured purchase orders, track vendor lead times, and reconcile received goods against manifests.</p>
        </div>
        <div class="card">
          <h4>Batch & Serial Number Tracking</h4>
          <p>Trace individual batch manufacturing dates, expiry periods, and serial numbers for warranty verification.</p>
        </div>
        <div class="card">
          <h4>Stock-In & Stock-Out Auditing</h4>
          <p>Immutable event logging of every inventory addition, transfer, damage write-off, and customer dispatch.</p>
        </div>
        <div class="card">
          <h4>Barcode & Mobile Scanner Sync</h4>
          <p>Equip warehouse pickers with mobile interfaces to scan items directly at the pallet level, eliminating paper clipboards.</p>
        </div>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Looking for custom inventory management software?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our software architects to review your SKU hierarchy, supplier integrations, and warehouse structure.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request an Inventory Software Quote</a>
      </div>
    </div>
  </section>
"""
}

# 10. ECOMMERCE SOFTWARE DEVELOPMENT (ecommerce-development.html)
img_ecommerce_preview = register_image(
    "service-ecommerce-development.jpg", "ecommerce-development.html", "E-commerce Interface Preview", "16:10", "1600x1000", "Landscape",
    "Custom E-commerce Storefront & Order Management Panel",
    "Digital storefront interface preview showcasing product catalog rules, faceted filtering, shopping cart, and order processing workflows.",
    {
        "subject": "Modern custom e-commerce product catalog and checkout web application interface preview",
        "environment": "Dark high-tech digital storefront showcasing product grid, filter sidebar, and shopping basket modal",
        "composition": "Frontal angle of modern e-commerce platform interface",
        "camera": "Direct viewport rendering",
        "lighting": "Electric blue accents on pricing labels with cyan checkout CTA button",
        "background": "#080D18 background",
        "colors": "#080D18, #141F32, #4F8CFF, #36D6E8",
        "style": "High-fidelity digital e-commerce mockup",
        "mood": "Frictionless, conversion-optimized, enterprise shopping experience",
        "ratio": "16:10",
        "negative": "stock photos of shoppers, physical credit cards, low resolution"
    }
)

pages_data["ecommerce-development.html"] = {
    "title": "E-commerce Software Development Services — Custom Digital Commerce Platforms",
    "desc": "Custom e-commerce platforms engineered for complex product catalogs, B2B wholesale pricing, custom checkout workflows, and high transaction volume.",
    "keywords": "E-commerce Software Development, Custom E-commerce Platforms, B2B E-commerce, Shopping Cart Development, Order Management System, Custom Checkout",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Digital Commerce</span>
        </div>
        <h1>E-COMMERCE SOFTWARE <span class="text-gradient">DEVELOPMENT SERVICES</span></h1>
        <p class="lead">Bespoke online commerce platforms engineered for high transaction speed, complex product rules, and seamless order fulfillment.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>BEYOND THE LIMITS OF STANDARD STORE BUILDERS</h2>
          <p style="margin-bottom: 16px;">
            Generic store builders charge hefty transaction surcharges, struggle with complex B2B tiered pricing, and impose strict limitations on checkout customizations and database queries.
          </p>
          <p style="margin-bottom: 20px;">
            We engineer custom digital commerce platforms tailored around your exact catalog architecture, fulfillment logistics, payment processing gateways, and ERP backend synchronization.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Request an E-commerce Quote</a>
            <a href="#ecommerce-features" class="btn btn-outline">Explore Commerce Features</a>
          </div>
        </div>
        <div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="mockup-dots">
                <span class="mockup-dot dot-red"></span>
                <span class="mockup-dot dot-yellow"></span>
                <span class="mockup-dot dot-green"></span>
              </div>
              <span class="mockup-title">custom-commerce-storefront.app</span>
              <span class="badge-status badge-new">Demo Mockup</span>
            </div>
            {img_ecommerce_preview}
          </div>
        </div>
      </div>

      <!-- Features Grid -->
      <div id="ecommerce-features" class="section-header">
        <h2>CUSTOM COMMERCE <span class="text-gradient">CAPABILITIES</span></h2>
        <p>Engineered for high-volume B2C and complex B2B wholesale environments.</p>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <div class="card">
          <h4>Custom Product Catalog Engines</h4>
          <p>Support for multi-attribute variants, dynamic volume discount tiers, customizable bundles, and faceted category search filters.</p>
        </div>
        <div class="card">
          <h4>Optimized Checkout Interfaces</h4>
          <p>Frictionless single-page or multi-step checkout flows designed to minimize abandoned carts and validate customer shipping details.</p>
        </div>
        <div class="card">
          <h4>B2B Wholesale Portals</h4>
          <p>Customer account approval workflows, corporate credit limits, negotiated tier pricing, and purchase order checkout options.</p>
        </div>
        <div class="card">
          <h4>Order Management & Fulfillment</h4>
          <p>Centralized order routing dashboard, printable packing slips, tracking number generation, and partial fulfillment queues.</p>
        </div>
        <div class="card">
          <h4>Payment Gateway Integration Concepts</h4>
          <p>Architectural support for Stripe, PayPal, Razorpay, Authorize.Net, and localized merchant processors with strict tokenization.</p>
        </div>
        <div class="card">
          <h4>Inventory & ERP Synchronization</h4>
          <p>Automated real-time stock sync between your web storefront and physical warehouse ERP systems to avoid overselling.</p>
        </div>
      </div>

      <div style="text-align:center; margin-bottom:40px;">
        <span class="demo-disclaimer-badge">Notice: Payment gateway, shipping carrier, and tax APIs are shown as architectural capabilities. This demo does not execute actual financial transactions.</span>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Ready to build a proprietary e-commerce platform?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our software team to discuss your product catalog size, customer workflows, and fulfillment integrations.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request an E-commerce Platform Quote</a>
      </div>
    </div>
  </section>
"""
}

print("Loaded Module 1 (Services).")
