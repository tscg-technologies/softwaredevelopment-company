"""
Module 2: Engineering & Directory Pages (mobile-apps, automation, api, database, modernization, maintenance, industries, technologies)
"""
from build_all_pages import register_image, pages_data

# 11. MOBILE APPLICATION DEVELOPMENT (mobile-apps.html)
img_mobile_app_1 = register_image(
    "demo-mobile-screen-operations.jpg", "mobile-apps.html", "Mobile App Screens", "16:9", "1376x768", "Landscape",
    "Business Operations Mobile Client Screen Mockup",
    "Mobile user interface showing field task checklist, dispatch routes, and digital signature sign-off.",
    {
        "subject": "Mobile business application interface mockup displaying task dispatch list and offline sync status",
        "environment": "Sleek dark mode mobile UI within a minimalist smartphone bezel",
        "composition": "Centered smartphone screen showing clean list cards and action buttons",
        "camera": "Frontal screen view",
        "lighting": "Clean internal screen lighting with cyan badges and electric blue buttons",
        "background": "#080D18 background",
        "colors": "#080D18, #141F32, #4F8CFF, #36D6E8",
        "style": "High-fidelity digital mobile product design mockup",
        "mood": "On-the-go productivity, clean mobile UX",
        "ratio": "16:9",
        "negative": "hands holding phone, fake app store badges, 5 star rating graphics, blur"
    }
)

img_mobile_app_2 = register_image(
    "demo-mobile-screen-analytics.jpg", "mobile-apps.html", "Mobile App Screens", "16:9", "1376x768", "Landscape",
    "Executive Metrics Mobile Screen Mockup",
    "Mobile dashboard showing real-time revenue KPIs, customer conversion metrics, and system status alerts.",
    {
        "subject": "Executive analytics mobile application interface showcasing revenue cards, line graph trends, and active customer counters",
        "environment": "Dark mode mobile UI within sleek smartphone frame",
        "composition": "Centered portrait view",
        "camera": "Direct viewport angle",
        "lighting": "Electric blue graph lines and cyan numeric counters against dark navy cards",
        "background": "#080D18 background",
        "colors": "#080D18, #141F32, #4F8CFF, #36D6E8",
        "style": "Digital product UI mockup",
        "mood": "Executive visibility, precision mobile telemetry",
        "ratio": "16:9",
        "negative": "stock photo of person on phone, hand models, low resolution"
    }
)

pages_data["mobile-apps.html"] = {
    "title": "Mobile Application Development Services — iOS & Android Business Apps",
    "desc": "Custom mobile application development for enterprise operations, field workforce tools, customer portals, and e-commerce apps.",
    "keywords": "Mobile Application Development, Android Applications, iOS Applications, Business Mobile Apps, Cross-Platform Mobile Apps, App UI/UX Design",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Mobile Engineering</span>
        </div>
        <h1>MOBILE APPLICATION <span class="text-gradient">DEVELOPMENT SERVICES</span></h1>
        <p class="lead">Native and cross-platform mobile applications engineered to empower your field workforce, engage customers, and provide executive visibility.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>CONNECTING FIELD TEAMS & CUSTOMERS ANYWHERE</h2>
          <p style="margin-bottom: 16px;">
            Whether your operations require field technicians to verify service tickets on-site, delivery drivers to capture digital proof-of-delivery, or customers to browse product catalogs from their smartphones, we engineer responsive, high-performance mobile software.
          </p>
          <p style="margin-bottom: 20px;">
            We build native iOS, native Android, and cross-platform Flutter/React Native solutions that communicate seamlessly with your central cloud backends and ERP databases.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Request Mobile App Quote</a>
            <a href="#mobile-showcase" class="btn btn-outline">View Screen Previews</a>
          </div>
        </div>
        <div>
          <div style="display:flex; flex-direction:column; gap:24px;">
            <div class="mockup-window">
              <div class="mockup-header">
                <div class="mockup-dots">
                  <span class="mockup-dot dot-red"></span>
                  <span class="mockup-dot dot-yellow"></span>
                  <span class="mockup-dot dot-green"></span>
                </div>
                <span class="mockup-title">ops-client.apk &bull; Field Operations</span>
                <span class="badge-status badge-new">Mobile Client</span>
              </div>
              {img_mobile_app_1}
            </div>
            <div class="mockup-window">
              <div class="mockup-header">
                <div class="mockup-dots">
                  <span class="mockup-dot dot-red"></span>
                  <span class="mockup-dot dot-yellow"></span>
                  <span class="mockup-dot dot-green"></span>
                </div>
                <span class="mockup-title">executive-kpi.ipa &bull; Analytics Dashboard</span>
                <span class="badge-status badge-converted">Mobile Client</span>
              </div>
              {img_mobile_app_2}
            </div>
          </div>
        </div>
      </div>

      <!-- Capabilities Grid -->
      <div id="mobile-showcase" class="section-header">
        <h2>MOBILE SOLUTIONS <span class="text-gradient">WE ENGINEER</span></h2>
        <p>Built for reliability, offline data storage, and low-latency API synchronization.</p>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <div class="card">
          <h4>Business & Enterprise Apps</h4>
          <p>Internal apps for inventory scanning, equipment maintenance inspections, staff timecards, and purchase order approvals.</p>
          <span class="tag-pill">Internal Operations</span>
        </div>
        <div class="card">
          <h4>Customer-Facing Applications</h4>
          <p>Dedicated customer loyalty apps, appointment booking, order status notifications, and account self-service.</p>
          <span class="tag-pill">Customer Engagement</span>
        </div>
        <div class="card">
          <h4>Field Service & Dispatch Apps</h4>
          <p>Offline-capable job checklists, GPS route guidance, camera photo capture, and customer signature sign-offs.</p>
          <span class="tag-pill">Field Mobility</span>
        </div>
        <div class="card">
          <h4>Cross-Platform Development</h4>
          <p>Single codebase architectures built with Flutter or React Native, delivering native look and feel on both iOS and Android.</p>
          <span class="tag-pill">Flutter / React Native</span>
        </div>
        <div class="card">
          <h4>Native iOS & Android Engineering</h4>
          <p>High-performance native apps written in Swift and Kotlin for hardware-intensive tasks, BLE sensor connections, and push notifications.</p>
          <span class="tag-pill">Swift & Kotlin</span>
        </div>
        <div class="card">
          <h4>Mobile UI/UX Interface Design</h4>
          <p>Thumb-friendly ergonomics, legible typography, high contrast dark themes, and smooth micro-interactions that make tasks intuitive.</p>
          <span class="tag-pill">Ergonomic UI</span>
        </div>
      </div>

      <div style="text-align:center; margin-bottom:40px;">
        <span class="demo-disclaimer-badge">Demonstration Notice: App mockups are illustrative UI concepts. We do not display fake app-store ratings or fabricated download statistics.</span>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Ready to build a dedicated mobile application?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our mobile engineering team to turn your operational requirements into an intuitive iOS and Android application.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request a Mobile App Quote</a>
      </div>
    </div>
  </section>
"""
}

# 12. BUSINESS PROCESS AUTOMATION (business-automation.html)
pages_data["business-automation.html"] = {
    "title": "Business Process Automation Services — Workflow Automation & System Integrations",
    "desc": "Automate repetitive data entry, lead follow-ups, invoice routing, and multi-system business workflows with custom software.",
    "keywords": "Business Process Automation, Workflow Automation, Invoice Processing, Approval Workflows, CRM ERP Integration, Data Entry Automation",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Workflow Optimization</span>
        </div>
        <h1>BUSINESS PROCESS <span class="text-gradient">AUTOMATION SERVICES</span></h1>
        <p class="lead">Eliminate manual bottlenecks, reduce human error, and connect your business systems with intelligent automated workflows.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>REPLACE MANUAL DATA ENTRY WITH RELIABLE AUTOMATION</h2>
          <p style="margin-bottom: 16px;">
            Manual data transfer between spreadsheets, email inboxes, and disparate software tools drains thousands of productive employee hours each year and causes costly mistakes.
          </p>
          <p style="margin-bottom: 20px;">
            We engineer custom business process automation solutions that connect your web forms, CRM, accounting software, and warehouse databases into cohesive, event-driven pipelines.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Automate Your Workflows</a>
            <a href="#workflow-interactive" class="btn btn-secondary">Explore Interactive Workflow</a>
          </div>
        </div>
        <div>
          <div class="card" style="background:#0d1522; border:1px solid var(--accent-primary);">
            <h4 style="color:var(--accent-cyan); margin-bottom:12px;">What Custom Automation Solves</h4>
            <ul style="display:flex; flex-direction:column; gap:12px; font-size:0.9rem;">
              <li style="display:flex; gap:10px;">
                <span style="color:#10B981; font-weight:700;">&check;</span>
                <span>Automated lead routing to the right sales rep within 5 seconds of form submission.</span>
              </li>
              <li style="display:flex; gap:10px;">
                <span style="color:#10B981; font-weight:700;">&check;</span>
                <span>Automatic PDF invoice generation and reconciliation in accounting software upon order close.</span>
              </li>
              <li style="display:flex; gap:10px;">
                <span style="color:#10B981; font-weight:700;">&check;</span>
                <span>Triggered notifications via SMS/email when inventory reaches critical threshold levels.</span>
              </li>
              <li style="display:flex; gap:10px;">
                <span style="color:#10B981; font-weight:700;">&check;</span>
                <span>Multi-level manager sign-off workflows with automatic escalation if approval stalls.</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Interactive Workflow Diagram -->
      <div id="workflow-interactive" class="dashboard-demo-box">
        <div class="dashboard-toolbar">
          <div>
            <h4 style="margin-bottom: 4px;">Automated Business Process Engine (Interactive Architecture Diagram)</h4>
            <span class="dashboard-notice">Illustrative Workflow — Click any stage node to view execution mechanics</span>
          </div>
        </div>

        <div class="workflow-diagram">
          <div class="workflow-node active" data-stage="trigger">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STAGE 01</div>
            <strong>Trigger</strong>
          </div>
          <div class="workflow-arrow">&rarr;</div>
          <div class="workflow-node" data-stage="input">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STAGE 02</div>
            <strong>Input</strong>
          </div>
          <div class="workflow-arrow">&rarr;</div>
          <div class="workflow-node" data-stage="processing">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STAGE 03</div>
            <strong>Processing</strong>
          </div>
          <div class="workflow-arrow">&rarr;</div>
          <div class="workflow-node" data-stage="rules">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STAGE 04</div>
            <strong>Business Rules</strong>
          </div>
          <div class="workflow-arrow">&rarr;</div>
          <div class="workflow-node" data-stage="action">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STAGE 05</div>
            <strong>Action</strong>
          </div>
          <div class="workflow-arrow">&rarr;</div>
          <div class="workflow-node" data-stage="review">
            <div style="font-size:0.75rem; color:var(--accent-cyan);">STAGE 06</div>
            <strong>Review</strong>
          </div>
        </div>

        <div class="workflow-detail-box" style="margin: 0 24px 24px 24px;">
          <h4 id="workflow-active-title" style="color:var(--accent-cyan); margin-bottom:8px;">Stage 1: Event Trigger</h4>
          <p id="workflow-active-desc" style="font-size:0.95rem; color:var(--text-secondary);">
            An automated workflow is initiated by business events such as an incoming webhook, web form submission, payment confirmation, or scheduled cron timer.
          </p>
        </div>
      </div>

      <!-- Core Automation Solutions -->
      <div class="section-header">
        <h2>AUTOMATION SOLUTIONS <span class="text-gradient">WE ENGINEER</span></h2>
        <p>Purpose-built pipelines configured around your operational bottlenecks.</p>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <div class="card">
          <h4>Lead Follow-Up Workflows</h4>
          <p>Instant SMS acknowledgment, calendar invite generation, and automatic task assignment to active sales representatives.</p>
        </div>
        <div class="card">
          <h4>Invoice & Billing Automation</h4>
          <p>Extract order records, calculate localized taxes, create signed PDFs, and dispatch payment links automatically.</p>
        </div>
        <div class="card">
          <h4>Data Entry & Normalization</h4>
          <p>Ingest raw customer spreadsheets, sanitize phone numbers, eliminate duplicates, and update master databases.</p>
        </div>
        <div class="card">
          <h4>Customer Communication Cadences</h4>
          <p>Automate onboarding email sequences, order shipment tracking links, and renewal reminder notices.</p>
        </div>
        <div class="card">
          <h4>Multi-Tier Approval Workflows</h4>
          <p>Route expense requests or quote discounts based on monetary thresholds with mobile one-click manager approvals.</p>
        </div>
        <div class="card">
          <h4>CRM & ERP Data Synchronization</h4>
          <p>Synchronize won deals in your CRM directly into your ERP for immediate warehouse dispatch and accounting entries.</p>
        </div>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Ready to automate your manual business tasks?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our process engineers to map your repetitive workflows and receive an automation proposal.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request an Automation Quote</a>
      </div>
    </div>
  </section>
"""
}

# 13. API AND SYSTEM INTEGRATION (api-integration.html)
pages_data["api-integration.html"] = {
    "title": "API & System Integration Services — REST, Webhooks & Enterprise Connectors",
    "desc": "Connect disconnected software systems with custom RESTful APIs, webhook bridges, payment gateway integrations, and ERP sync pipelines.",
    "keywords": "API Integration Services, REST API Development, Webhook Workflows, Third-Party API Integration, Payment Gateway Integration, ERP Integration",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>System Interoperability</span>
        </div>
        <h1>API & SYSTEM <span class="text-gradient">INTEGRATION SERVICES</span></h1>
        <p class="lead">Connect isolated software tools, synchronize customer records, and bridge modern web apps with legacy backend infrastructure.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>CONNECT DISCONNECTED SOFTWARE ISLANDS</h2>
          <p style="margin-bottom: 16px;">
            Modern enterprises often use dozens of independent SaaS apps, legacy internal databases, and external partner portals. When these systems cannot talk to each other, data must be manually re-typed, creating delays and inconsistencies.
          </p>
          <p style="margin-bottom: 20px;">
            We engineer secure RESTful APIs, real-time webhook listeners, and resilient middleware services that keep your records automatically synchronized across platforms.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Discuss Integration Project</a>
            <a href="#api-architecture" class="btn btn-outline">View Architecture Model</a>
          </div>
        </div>
        <div>
          <!-- Visual SVG Architecture Diagram -->
          <div class="mockup-window" style="padding: 24px; background:#0d1522;">
            <div style="font-size:0.8rem; font-family:var(--font-mono); color:var(--accent-cyan); margin-bottom:12px; text-transform:uppercase;">
              System Interoperability Architecture (SVG Model)
            </div>
            <svg viewBox="0 0 460 260" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto;">
              <!-- Central API Bridge Node -->
              <rect x="180" y="90" width="100" height="80" rx="8" fill="#141F32" stroke="#4F8CFF" stroke-width="2"/>
              <text x="230" y="125" fill="#F5F7FC" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">API BRIDGE</text>
              <text x="230" y="145" fill="#36D6E8" font-size="9" font-family="monospace" text-anchor="middle">REST & Webhooks</text>

              <!-- Node 1: CRM -->
              <rect x="20" y="20" width="90" height="50" rx="6" fill="#0d1522" stroke="#26344B" stroke-width="1.5"/>
              <text x="65" y="48" fill="#F5F7FC" font-size="10" font-family="sans-serif" text-anchor="middle">CRM System</text>
              <line x1="110" y1="45" x2="180" y2="105" stroke="#36D6E8" stroke-width="1.5" stroke-dasharray="3 3"/>

              <!-- Node 2: ERP -->
              <rect x="20" y="180" width="90" height="50" rx="6" fill="#0d1522" stroke="#26344B" stroke-width="1.5"/>
              <text x="65" y="208" fill="#F5F7FC" font-size="10" font-family="sans-serif" text-anchor="middle">ERP Core</text>
              <line x1="110" y1="205" x2="180" y2="155" stroke="#4F8CFF" stroke-width="1.5"/>

              <!-- Node 3: Payment Gateway -->
              <rect x="350" y="20" width="90" height="50" rx="6" fill="#0d1522" stroke="#26344B" stroke-width="1.5"/>
              <text x="395" y="48" fill="#F5F7FC" font-size="10" font-family="sans-serif" text-anchor="middle">Payment API</text>
              <line x1="350" y1="45" x2="280" y2="105" stroke="#9878FF" stroke-width="1.5"/>

              <!-- Node 4: Warehouse Node -->
              <rect x="350" y="180" width="90" height="50" rx="6" fill="#0d1522" stroke="#26344B" stroke-width="1.5"/>
              <text x="395" y="208" fill="#F5F7FC" font-size="10" font-family="sans-serif" text-anchor="middle">Warehouse Sync</text>
              <line x1="350" y1="205" x2="280" y2="155" stroke="#36D6E8" stroke-width="1.5" stroke-dasharray="3 3"/>
            </svg>
            <div style="font-size:0.75rem; color:var(--text-muted); text-align:center; margin-top:8px;">
              Illustrative System Integration Model — Demonstrates Event Routing
            </div>
          </div>
        </div>
      </div>

      <!-- Core Integration Capabilities -->
      <div id="api-architecture" class="section-header">
        <h2>INTEGRATION CAPABILITIES <span class="text-gradient">WE DELIVER</span></h2>
        <p>Built with enterprise security standards, rate-limiting, and error retry queues.</p>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <div class="card">
          <h4>Custom RESTful API Development</h4>
          <p>Well-documented, structured JSON endpoints with OpenAPI/Swagger specifications, versioning, and token authentication.</p>
        </div>
        <div class="card">
          <h4>Third-Party SaaS Integrations</h4>
          <p>Connect your software with external services such as Salesforce, HubSpot, Stripe, Twilio, Google Workspace, and QuickBooks.</p>
        </div>
        <div class="card">
          <h4>Real-Time Webhook Listeners</h4>
          <p>Instant event-driven listeners that receive and validate external payload changes, executing downstream database updates in milliseconds.</p>
        </div>
        <div class="card">
          <h4>Data Synchronization & Transformation</h4>
          <p>Bi-directional sync engines with conflict resolution algorithms that ensure data consistency across multiple database repositories.</p>
        </div>
        <div class="card">
          <h4>Legacy System API Wrappers</h4>
          <p>Expose legacy on-premise databases through secure modern API microservices, avoiding risky complete system replacements.</p>
        </div>
        <div class="card">
          <h4>Resilient Error Queues & Retries</h4>
          <p>Dead-letter queues (DLQ), automated exponential backoff retries, and failure alerts to ensure zero data packets are lost during downtime.</p>
        </div>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Need to connect your enterprise software applications?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our systems integration specialists to plan API endpoints, authentication keys, and data transformation rules.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request an API Integration Quote</a>
      </div>
    </div>
  </section>
"""
}

# 14. DATABASE DESIGN AND DEVELOPMENT (database-development.html)
pages_data["database-development.html"] = {
    "title": "Database Design & Development Services — Architecture, Optimization & Schemas",
    "desc": "Custom database design, relational schema modeling, SQL query optimization, data migrations, and high-availability database architectures.",
    "keywords": "Database Design, Database Architecture, Relational Database Design, Data Modeling, Database Optimization, SQL Schema",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Data Infrastructure</span>
        </div>
        <h1>DATABASE DESIGN & <span class="text-gradient">DEVELOPMENT SERVICES</span></h1>
        <p class="lead">Robust relational schemas, optimized indexing, secure access controls, and high-concurrency database architectures.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>THE FOUNDATION OF EVERY FAST, RELIABLE SOFTWARE APPLICATION</h2>
          <p style="margin-bottom: 16px;">
            Slow page loads, locking errors, and lost records are almost always caused by poor database modeling. An inefficient database schema will choke even the fastest web frontend as user transactions grow.
          </p>
          <p style="margin-bottom: 20px;">
            We engineer normalized relational schemas (PostgreSQL, MySQL) and scalable document stores (MongoDB) designed for ACID compliance, rapid query execution, and effortless long-term maintenance.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Request Database Consultation</a>
            <a href="#database-services" class="btn btn-outline">Explore Capabilities</a>
          </div>
        </div>
        <div>
          <!-- Visual SVG Database Schema Concept -->
          <div class="mockup-window" style="padding: 24px; background:#0d1522;">
            <div style="font-size:0.8rem; font-family:var(--font-mono); color:var(--accent-cyan); margin-bottom:12px; text-transform:uppercase;">
              Relational Entity Model (Illustrative Schema)
            </div>
            <svg viewBox="0 0 460 220" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto;">
              <!-- Table 1: Customers -->
              <rect x="20" y="20" width="120" height="85" rx="6" fill="#141F32" stroke="#4F8CFF" stroke-width="1.5"/>
              <rect x="20" y="20" width="120" height="24" rx="6" fill="#1A2840"/>
              <text x="30" y="37" fill="#F5F7FC" font-size="11" font-family="sans-serif" font-weight="bold">customers</text>
              <text x="30" y="58" fill="#36D6E8" font-size="9" font-family="monospace">PK id (UUID)</text>
              <text x="30" y="73" fill="#A7B1C2" font-size="9" font-family="monospace">email (VARCHAR)</text>
              <text x="30" y="88" fill="#A7B1C2" font-size="9" font-family="monospace">created_at (TS)</text>

              <!-- Table 2: Orders -->
              <rect x="180" y="20" width="120" height="100" rx="6" fill="#141F32" stroke="#36D6E8" stroke-width="1.5"/>
              <rect x="180" y="20" width="120" height="24" rx="6" fill="#1A2840"/>
              <text x="190" y="37" fill="#F5F7FC" font-size="11" font-family="sans-serif" font-weight="bold">orders</text>
              <text x="190" y="58" fill="#36D6E8" font-size="9" font-family="monospace">PK id (UUID)</text>
              <text x="190" y="73" fill="#9878FF" font-size="9" font-family="monospace">FK customer_id</text>
              <text x="190" y="88" fill="#A7B1C2" font-size="9" font-family="monospace">total_amount</text>
              <text x="190" y="103" fill="#A7B1C2" font-size="9" font-family="monospace">status (ENUM)</text>

              <!-- Table 3: Order Items -->
              <rect x="330" y="20" width="115" height="100" rx="6" fill="#141F32" stroke="#9878FF" stroke-width="1.5"/>
              <rect x="330" y="20" width="115" height="24" rx="6" fill="#1A2840"/>
              <text x="340" y="37" fill="#F5F7FC" font-size="11" font-family="sans-serif" font-weight="bold">order_items</text>
              <text x="340" y="58" fill="#36D6E8" font-size="9" font-family="monospace">PK id (BIGINT)</text>
              <text x="340" y="73" fill="#9878FF" font-size="9" font-family="monospace">FK order_id</text>
              <text x="340" y="88" fill="#9878FF" font-size="9" font-family="monospace">FK product_id</text>
              <text x="340" y="103" fill="#A7B1C2" font-size="9" font-family="monospace">quantity (INT)</text>

              <!-- Connecting Relations -->
              <line x1="140" y1="60" x2="180" y2="70" stroke="#4F8CFF" stroke-width="1.5" stroke-dasharray="2 2"/>
              <line x1="300" y1="70" x2="330" y2="70" stroke="#36D6E8" stroke-width="1.5"/>

              <!-- Bottom Note -->
              <text x="230" y="170" fill="#67758D" font-size="10" font-family="sans-serif" text-anchor="middle">
                Clean Normalization &bull; Foreign Key Constraints &bull; Indexed Lookups
              </text>
            </svg>
          </div>
        </div>
      </div>

      <!-- Capabilities Grid -->
      <div id="database-services" class="section-header">
        <h2>DATABASE ENGINEERING <span class="text-gradient">CAPABILITIES</span></h2>
        <p>From greenfield schema modeling to performance audits of legacy production clusters.</p>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <div class="card">
          <h4>Relational Schema Design</h4>
          <p>Proper normalization (3NF), foreign key constraints, check validations, and primary indexing that ensure data integrity.</p>
        </div>
        <div class="card">
          <h4>SQL Query Optimization</h4>
          <p>Identifying slow running queries, analyzing EXPLAIN plans, creating composite indexes, and rewriting subqueries for maximum speed.</p>
        </div>
        <div class="card">
          <h4>Data Migration & Schema Evolution</h4>
          <p>Safe data transformation from legacy flat files or old databases into structured relational tables with zero data corruption.</p>
        </div>
        <div class="card">
          <h4>Role-Based Access & Security</h4>
          <p>Principle of least privilege database users, encrypted credentials, SSL connections, and protection against SQL injection attacks.</p>
        </div>
        <div class="card">
          <h4>Backup & Disaster Recovery Planning</h4>
          <p>Automated point-in-time snapshot schedules, off-site storage replication, and verified recovery procedures for business continuity.</p>
        </div>
        <div class="card">
          <h4>Caching Layer Integration (Redis)</h4>
          <p>Implementing fast in-memory key-value caches to reduce read loads on primary databases for frequently accessed records.</p>
        </div>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Need expert database architecture for your application?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our database engineers to review your schema design, query benchmarks, and storage scalability.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request a Database Quote</a>
      </div>
    </div>
  </section>
"""
}

# 15. SOFTWARE MODERNIZATION (software-modernization.html)
pages_data["software-modernization.html"] = {
    "title": "Software Modernization Services — Legacy System Migration & Re-platforming",
    "desc": "Modernize legacy desktop applications, outdated codebases, and monolithic systems into secure, scalable, cloud-native web platforms.",
    "keywords": "Software Modernization, Legacy System Migration, Application Redesign, Architecture Modernization, Cloud Migration, Monolith to Microservices",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Legacy Migration</span>
        </div>
        <h1>SOFTWARE MODERNIZATION <span class="text-gradient">SERVICES</span></h1>
        <p class="lead">Transform fragile, outdated legacy software into fast, secure, cloud-ready web applications without disrupting ongoing operations.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>PROTECT YOUR INTELLECTUAL PROPERTY WHILE UPGRADING ARCHITECTURE</h2>
          <p style="margin-bottom: 16px;">
            Legacy software applications often hold decades of unique business logic. However, obsolete desktop frameworks, unsupported runtimes, and outdated databases pose serious security risks and make remote work impossible.
          </p>
          <p style="margin-bottom: 20px;">
            We extract your core business rules and re-architect them into clean, modern web applications. Your team retains the familiarity of their essential workflows while gaining speed, security, and mobile accessibility.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Plan Modernization Project</a>
            <a href="#comparison-section" class="btn btn-outline">Legacy vs Modern Architecture</a>
          </div>
        </div>
        <div>
          <!-- Visual Old vs Modern System Comparison Card -->
          <div id="comparison-section" class="mockup-window" style="background:#0d1522; padding: 24px;">
            <div style="font-size:0.8rem; font-family:var(--font-mono); color:var(--accent-cyan); margin-bottom:16px; text-transform:uppercase;">
              Architecture Comparison (Illustrative Concept)
            </div>
            <div class="grid-2" style="gap:16px;">
              <div style="background:#141f32; border:1px solid rgba(239, 68, 68, 0.3); border-radius:8px; padding:16px;">
                <h4 style="color:#F87171; font-size:0.95rem; margin-bottom:8px;">Legacy Architecture</h4>
                <ul style="font-size:0.8rem; color:var(--text-muted); display:flex; flex-direction:column; gap:6px;">
                  <li>&bull; Desktop client installs</li>
                  <li>&bull; Unsupported runtime versions</li>
                  <li>&bull; Direct unencrypted DB queries</li>
                  <li>&bull; No external API bridges</li>
                  <li>&bull; Frequent UI freezing</li>
                </ul>
              </div>
              <div style="background:#141f32; border:1px solid rgba(54, 214, 232, 0.4); border-radius:8px; padding:16px;">
                <h4 style="color:var(--accent-cyan); font-size:0.95rem; margin-bottom:8px;">Modern Architecture</h4>
                <ul style="font-size:0.8rem; color:var(--text-primary); display:flex; flex-direction:column; gap:6px;">
                  <li>&check; Universal browser access</li>
                  <li>&check; Maintained modern runtimes</li>
                  <li>&check; Microservice API security</li>
                  <li>&check; Webhooks & REST endpoints</li>
                  <li>&check; Sub-second responsive UI</li>
                </ul>
              </div>
            </div>
            <div style="font-size:0.75rem; color:var(--text-muted); text-align:center; margin-top:14px;">
              Visual representation of operational benefits achieved through software modernization.
            </div>
          </div>
        </div>
      </div>

      <!-- Core Modernization Capabilities -->
      <div class="section-header">
        <h2>HOW WE <span class="text-gradient">MODERNIZE SOFTWARE</span></h2>
        <p>A phased, risk-averse methodology that preserves existing business data.</p>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <div class="card">
          <h4>Codebase & Logic Extraction</h4>
          <p>We audit existing code, extract documented and undocumented business rules, and design a modern replacement blueprint.</p>
        </div>
        <div class="card">
          <h4>Modern UI/UX Re-Skinning</h4>
          <p>Replacing clunky, text-dense gray desktop interfaces with intuitive, responsive dark/light web design layouts.</p>
        </div>
        <div class="card">
          <h4>Database Migration & Cleansing</h4>
          <p>Sanitizing legacy records, upgrading obsolete schemas, and migrating data into modern PostgreSQL or MySQL clusters.</p>
        </div>
        <div class="card">
          <h4>Monolith to Modular Decoupling</h4>
          <p>Breaking fragile single-file monoliths into isolated, maintainable services with clean API contracts.</p>
        </div>
        <div class="card">
          <h4>Cloud Hosting & Containerization</h4>
          <p>Packaging applications into Docker containers for fast, automated deployments and effortless server scaling.</p>
        </div>
        <div class="card">
          <h4>Zero-Downtime Transition Planning</h4>
          <p>Running legacy and modern systems in parallel during validation phases to guarantee zero disruption to daily business.</p>
        </div>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Ready to upgrade your mission-critical software?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our engineering team to assess your legacy application and receive a risk-free modernization roadmap.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request a Modernization Assessment</a>
      </div>
    </div>
  </section>
"""
}

# 16. SOFTWARE MAINTENANCE AND SUPPORT (software-maintenance.html)
pages_data["software-maintenance.html"] = {
    "title": "Software Maintenance & Technical Support Services — Longevity & Security",
    "desc": "Proactive software maintenance, bug fixes, security patch updates, performance monitoring, and iterative feature enhancements.",
    "keywords": "Software Maintenance Services, Technical Support, Application Maintenance, Bug Fixes, Security Patching, Performance Monitoring",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Platform Longevity</span>
        </div>
        <h1>SOFTWARE MAINTENANCE <span class="text-gradient">& TECHNICAL SUPPORT</span></h1>
        <p class="lead">Protect your software investment with proactive maintenance, security patches, performance monitoring, and ongoing feature updates.</p>
      </div>

      <div class="grid-2" style="align-items: center; margin-bottom: 60px;">
        <div>
          <h2>SOFTWARE IS AN ASSET THAT REQUIRES DILIGENT CARE</h2>
          <p style="margin-bottom: 16px;">
            Deploying a custom software application is only the first step. Operating systems receive patches, third-party APIs update their endpoints, and security vulnerabilities emerge constantly.
          </p>
          <p style="margin-bottom: 20px;">
            Without structured ongoing maintenance, software degrades over time. Our maintenance services provide regular code audits, dependency upgrades, database index maintenance, and prompt bug fixes so your business runs smoothly.
          </p>
          <div class="btn-group">
            <a href="request-quote.html" class="btn btn-primary">Request Maintenance Plan</a>
            <a href="#maintenance-scope" class="btn btn-outline">View Maintenance Scope</a>
          </div>
        </div>
        <div>
          <div class="card" style="background:#0d1522; border:1px solid var(--border-color); padding: 32px;">
            <h4 style="color:var(--accent-cyan); margin-bottom:12px;">Responsible Maintenance Approach</h4>
            <p style="font-size:0.875rem; margin-bottom:16px;">
              We provide tailored maintenance agreements structured around project requirements.
            </p>
            <ul style="display:flex; flex-direction:column; gap:10px; font-size:0.85rem; color:var(--text-secondary);">
              <li style="display:flex; gap:8px;">
                <span style="color:var(--accent-cyan);">&bull;</span>
                <span>Scheduled dependency and security vulnerability updates.</span>
              </li>
              <li style="display:flex; gap:8px;">
                <span style="color:var(--accent-cyan);">&bull;</span>
                <span>Database defragmentation, index tuning, and log rotations.</span>
              </li>
              <li style="display:flex; gap:8px;">
                <span style="color:var(--accent-cyan);">&bull;</span>
                <span>Iterative user-requested UI improvements and bug fixes.</span>
              </li>
              <li style="display:flex; gap:8px;">
                <span style="color:var(--accent-cyan);">&bull;</span>
                <span>Notice: Actual SLAs and response windows are defined per client contract.</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Scope Grid -->
      <div id="maintenance-scope" class="section-header">
        <h2>WHAT OUR MAINTENANCE <span class="text-gradient">COVERS</span></h2>
        <p>Comprehensive engineering care for your production digital applications.</p>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <div class="card">
          <h4>Bug Fixes & Patch Management</h4>
          <p>Rapid diagnosis and correction of unexpected software edge cases, browser rendering quirks, or reported logic anomalies.</p>
        </div>
        <div class="card">
          <h4>Security Updates & Hardening</h4>
          <p>Proactive upgrading of third-party libraries, SSL certificate renewals, and patching against known CVE security vulnerabilities.</p>
        </div>
        <div class="card">
          <h4>Performance Monitoring Concepts</h4>
          <p>Tracking server CPU loads, memory consumption, query response times, and application error logs to prevent slowdowns.</p>
        </div>
        <div class="card">
          <h4>Feature Enhancements</h4>
          <p>Implementing new reporting widgets, additional form fields, workflow rule adjustments, and user permission tweaks as business needs evolve.</p>
        </div>
        <div class="card">
          <h4>Compatibility Upgrades</h4>
          <p>Ensuring your web and mobile applications remain fully functional as Chrome, Safari, Android, and iOS release new platform versions.</p>
        </div>
        <div class="card">
          <h4>Dedicated Technical Support</h4>
          <p>Direct communication channels with our engineering team for troubleshooting, administrative guidance, and consultation.</p>
        </div>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Need ongoing maintenance for your software?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our software team to establish a tailored maintenance and support agreement for your business.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request a Maintenance Quote</a>
      </div>
    </div>
  </section>
"""
}

# 17. INDUSTRIES WE SERVE (industries.html)
pages_data["industries.html"] = {
    "title": "Industries We Serve — Custom Software for Enterprises & Growing Businesses",
    "desc": "Discover how custom software drives operational efficiency across Retail, Healthcare, Education, Real Estate, Logistics, Finance, and Startups.",
    "keywords": "Software by Industry, Retail Software, Healthcare Software, Education Systems, Logistics Software, Real Estate Management, Finance Software",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Industry Directory</span>
        </div>
        <h1>INDUSTRIES <span class="text-gradient">WE SERVE</span></h1>
        <p class="lead">Explore illustrative target industry sectors where custom software architectures solve operational challenges and scale business operations.</p>
      </div>

      <div style="margin-bottom: 40px; text-align: center;">
        <span class="demo-disclaimer-badge">Illustrative Target Industries Notice: These sectors represent domains where our software engineering models apply. They do not constitute claims of verified past clientele or unverified domain experience.</span>
      </div>

      <div class="grid-3" style="margin-bottom: 60px;">
        <!-- 1. Retail -->
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">RETAIL</div>
          <h4>Retail Businesses</h4>
          <p><strong>Challenges:</strong> Inventory discrepancies between front-end checkout registers and storage depots, slow billing queues, and lack of customer loyalty tracking.</p>
          <p><strong>Software Solution:</strong> Touchscreen POS software with barcode scanning, instant multi-counter inventory deduction, and customer loyalty management.</p>
          <a href="pos-development.html" class="link-arrow">Explore Retail Software &rarr;</a>
        </div>

        <!-- 2. E-commerce -->
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">E-COMMERCE</div>
          <h4>Digital Commerce</h4>
          <p><strong>Challenges:</strong> Platform transaction commissions, rigid off-the-shelf checkout templates, and lack of B2B wholesale tiered pricing rules.</p>
          <p><strong>Software Solution:</strong> Custom digital storefronts, faceted search engines, single-page checkouts, and real-time ERP warehouse synchronization.</p>
          <a href="ecommerce-development.html" class="link-arrow">Explore E-commerce Software &rarr;</a>
        </div>

        <!-- 3. Healthcare -->
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">HEALTHCARE</div>
          <h4>Clinics & Healthcare</h4>
          <p><strong>Challenges:</strong> Patient appointment scheduling conflicts, lost paper consultation notes, and delayed laboratory test record tracking.</p>
          <p><strong>Software Solution:</strong> Doctor consultation portals, appointment booking cadences, role-based medical record repositories, and digital billing.</p>
          <a href="custom-software.html" class="link-arrow">Explore Healthcare Software &rarr;</a>
        </div>

        <!-- 4. Education -->
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">EDUCATION</div>
          <h4>Education & Academies</h4>
          <p><strong>Challenges:</strong> Disjointed student fee records, manual attendance logs, and chaotic distribution of course materials across email threads.</p>
          <p><strong>Software Solution:</strong> Student information systems (SIS), automated fee collection reminders, attendance logging, and digital learning portals.</p>
          <a href="web-applications.html" class="link-arrow">Explore Education Software &rarr;</a>
        </div>

        <!-- 5. Real Estate -->
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">REAL ESTATE</div>
          <h4>Real Estate & Property</h4>
          <p><strong>Challenges:</strong> Tracking lease expiration dates, tenant maintenance requests lost in WhatsApp messages, and multi-property accounting errors.</p>
          <p><strong>Software Solution:</strong> Central property management portals, automated lease renewal notices, maintenance ticketing boards, and tenant billing.</p>
          <a href="custom-software.html" class="link-arrow">Explore Property Software &rarr;</a>
        </div>

        <!-- 6. Logistics -->
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">LOGISTICS</div>
          <h4>Logistics & Supply Chain</h4>
          <p><strong>Challenges:</strong> Disorganized dispatch sheets, inability to verify delivery status in real-time, and lost physical delivery receipts.</p>
          <p><strong>Software Solution:</strong> Dispatch scheduling dashboards, mobile driver apps with digital signature capture, and shipment milestone tracking.</p>
          <a href="mobile-apps.html" class="link-arrow">Explore Logistics Software &rarr;</a>
        </div>

        <!-- 7. Manufacturing -->
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">MANUFACTURING</div>
          <h4>Manufacturing & Assembly</h4>
          <p><strong>Challenges:</strong> Raw material stockouts halting factory lines, lack of multi-stage production batch tracking, and poor machine downtime logging.</p>
          <p><strong>Software Solution:</strong> Bill of materials (BOM) management, production stage tracking, maintenance logs, and automated supplier replenishment.</p>
          <a href="erp-development.html" class="link-arrow">Explore Manufacturing Software &rarr;</a>
        </div>

        <!-- 8. Hospitality -->
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">HOSPITALITY</div>
          <h4>Hospitality & Dining</h4>
          <p><strong>Challenges:</strong> Kitchen order delays, table bill splitting confusion, high delivery aggregator fees, and inventory waste.</p>
          <p><strong>Software Solution:</strong> Table-side mobile ordering POS, kitchen display system (KDS), direct online ordering web portals, and recipe stock depletion.</p>
          <a href="pos-development.html" class="link-arrow">Explore Hospitality Software &rarr;</a>
        </div>

        <!-- 9. Finance -->
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">FINANCE</div>
          <h4>Financial & Accounting</h4>
          <p><strong>Challenges:</strong> Time-consuming manual invoice reconciliation, compliance tracking oversights, and human errors in credit checks.</p>
          <p><strong>Software Solution:</strong> Automated invoice matching engines, multi-tiered credit approval workflows, and immutable audit logging ledgers.</p>
          <a href="business-automation.html" class="link-arrow">Explore Financial Software &rarr;</a>
        </div>

        <!-- 10. Professional Services -->
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">SERVICES</div>
          <h4>Professional Services</h4>
          <p><strong>Challenges:</strong> Unbilled consultant hours, scope creep across deliverables, and fragmented document sharing with clients.</p>
          <p><strong>Software Solution:</strong> Staff timesheet portals, milestone-based client billing, document repositories, and project health dashboards.</p>
          <a href="web-applications.html" class="link-arrow">Explore Services Software &rarr;</a>
        </div>

        <!-- 11. Startups -->
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">STARTUPS</div>
          <h4>Technology Startups</h4>
          <p><strong>Challenges:</strong> Burned capital on unvalidated features, slow development velocity, and inability to build scalable multi-tenant SaaS foundations.</p>
          <p><strong>Software Solution:</strong> Rapid MVP engineering, multi-tenant database structuring, subscription billing integration, and modular API architecture.</p>
          <a href="saas-development.html" class="link-arrow">Explore Startup Software &rarr;</a>
        </div>

        <!-- 12. Wholesale -->
        <div class="card">
          <div class="tag-pill" style="align-self:flex-start; margin-bottom:12px; color:var(--accent-cyan);">WHOLESALE</div>
          <h4>Distribution & Wholesale</h4>
          <p><strong>Challenges:</strong> Complex customer-specific pricing catalogs, high-volume credit line orders, and multi-depot inventory tracking.</p>
          <p><strong>Software Solution:</strong> B2B wholesale ordering portals, negotiated pricing tables, credit limit checks, and multi-depot shipping dispatch.</p>
          <a href="inventory-software.html" class="link-arrow">Explore Wholesale Software &rarr;</a>
        </div>
      </div>

      <div class="card" style="text-align: center; padding: 48px;">
        <h3>Looking for custom software tailored to your specific industry?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our software team to discuss your operational challenges and receive a structured technical solution plan.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request an Industry Software Quote</a>
      </div>
    </div>
  </section>
"""
}

# 18. TECHNOLOGIES AND TOOLS (technologies.html)
pages_data["technologies.html"] = {
    "title": "Technologies and Tools — Software Architecture & Tech Stack Directory",
    "desc": "Directory of frontend, backend, database, cloud, and mobile software technologies utilized across custom enterprise software projects.",
    "keywords": "Software Technologies, Tech Stack Directory, Frontend Frameworks, Backend Languages, Database Technologies, Cloud DevOps",
    "content": f"""
  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="tagline-badge">
          <span class="badge-dot"></span>
          <span>Engineering Stack</span>
        </div>
        <h1>TECHNOLOGIES <span class="text-gradient">& TOOLS DIRECTORY</span></h1>
        <p class="lead">An illustrative overview of the languages, frameworks, databases, and cloud infrastructures utilized in modern software engineering.</p>
      </div>

      <div style="margin-bottom: 30px; text-align: center;">
        <span class="demo-disclaimer-badge">Editable Confirmation Notice: These categories illustrate architectural technologies. Only technologies genuinely verified by the actual engineering team will be retained for production client delivery.</span>
      </div>

      <!-- Filterable Tabs -->
      <div id="tech-filterable-section">
        <div class="filter-group" style="justify-content:center; margin-bottom: 40px;">
          <button class="filter-btn tech-tab-btn active" data-tech="all">All Technologies</button>
          <button class="filter-btn tech-tab-btn" data-tech="frontend">Frontend</button>
          <button class="filter-btn tech-tab-btn" data-tech="backend">Backend</button>
          <button class="filter-btn tech-tab-btn" data-tech="mobile">Mobile</button>
          <button class="filter-btn tech-tab-btn" data-tech="database">Databases</button>
          <button class="filter-btn tech-tab-btn" data-tech="cloud">Cloud & DevOps</button>
          <button class="filter-btn tech-tab-btn" data-tech="apis">APIs & Integrations</button>
        </div>

        <div style="display:flex; flex-direction:column; gap:40px;">
          <!-- 1. Frontend -->
          <div class="tech-group-panel" data-group="frontend">
            <h3 style="border-bottom:1px solid var(--border-color); padding-bottom:10px; margin-bottom:20px;">
              <span class="text-cyan">Frontend</span> Engineering
            </h3>
            <div class="grid-4">
              <div class="card" style="padding:20px;">
                <h4>HTML5 & Semantic Markup</h4>
                <p style="font-size:0.85rem;">Accessible, SEO-friendly, lightweight document architecture.</p>
                <span class="tag-pill">Semantic Standard</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>CSS3 & Modern Layouts</h4>
                <p style="font-size:0.85rem;">Flexbox, CSS Grid, custom properties, and responsive design.</p>
                <span class="tag-pill">Zero Bloat</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>JavaScript (ES6+) & TypeScript</h4>
                <p style="font-size:0.85rem;">High-performance vanilla interactions and type-safe frontend code.</p>
                <span class="tag-pill">Type Safety</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>React, Angular, Vue</h4>
                <p style="font-size:0.85rem;">Single page applications and interactive component libraries.</p>
                <span class="tag-pill">UI Frameworks</span>
              </div>
            </div>
          </div>

          <!-- 2. Backend -->
          <div class="tech-group-panel" data-group="backend">
            <h3 style="border-bottom:1px solid var(--border-color); padding-bottom:10px; margin-bottom:20px;">
              <span class="text-blue">Backend</span> Architecture
            </h3>
            <div class="grid-4">
              <div class="card" style="padding:20px;">
                <h4>Node.js</h4>
                <p style="font-size:0.85rem;">Asynchronous event-driven runtimes for real-time APIs.</p>
                <span class="tag-pill">High Concurrency</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>Python</h4>
                <p style="font-size:0.85rem;">Django and FastAPI for data processing engines and backend APIs.</p>
                <span class="tag-pill">Data Pipelines</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>PHP</h4>
                <p style="font-size:0.85rem;">Modern Laravel architectures for robust business portals.</p>
                <span class="tag-pill">Enterprise MVC</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>Java & .NET Core</h4>
                <p style="font-size:0.85rem;">Enterprise-scale compiled services for high transaction systems.</p>
                <span class="tag-pill">Enterprise Core</span>
              </div>
            </div>
          </div>

          <!-- 3. Mobile -->
          <div class="tech-group-panel" data-group="mobile">
            <h3 style="border-bottom:1px solid var(--border-color); padding-bottom:10px; margin-bottom:20px;">
              <span class="text-violet">Mobile</span> Client Engineering
            </h3>
            <div class="grid-4">
              <div class="card" style="padding:20px;">
                <h4>Flutter</h4>
                <p style="font-size:0.85rem;">High-performance cross-platform apps with unified codebases.</p>
                <span class="tag-pill">Cross-Platform</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>React Native</h4>
                <p style="font-size:0.85rem;">JavaScript-driven native mobile interfaces for iOS and Android.</p>
                <span class="tag-pill">Cross-Platform</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>Native Android (Kotlin)</h4>
                <p style="font-size:0.85rem;">Hardware integrations, barcode scanner drivers, and background tasks.</p>
                <span class="tag-pill">Native Android</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>Native iOS (Swift)</h4>
                <p style="font-size:0.85rem;">Optimized Apple ecosystem apps with smooth ergonomics.</p>
                <span class="tag-pill">Native Apple</span>
              </div>
            </div>
          </div>

          <!-- 4. Databases -->
          <div class="tech-group-panel" data-group="database">
            <h3 style="border-bottom:1px solid var(--border-color); padding-bottom:10px; margin-bottom:20px;">
              <span class="text-cyan">Databases</span> & Caching
            </h3>
            <div class="grid-4">
              <div class="card" style="padding:20px;">
                <h4>PostgreSQL</h4>
                <p style="font-size:0.85rem;">Advanced open-source relational database with JSONB support.</p>
                <span class="tag-pill">Relational Standard</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>MySQL</h4>
                <p style="font-size:0.85rem;">High-performance relational database for web applications.</p>
                <span class="tag-pill">Reliable SQL</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>MongoDB</h4>
                <p style="font-size:0.85rem;">Flexible document database for dynamic schema requirements.</p>
                <span class="tag-pill">Document Store</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>Redis</h4>
                <p style="font-size:0.85rem;">In-memory data store for caching and pub/sub message brokers.</p>
                <span class="tag-pill">Sub-ms Cache</span>
              </div>
            </div>
          </div>

          <!-- 5. Cloud & DevOps -->
          <div class="tech-group-panel" data-group="cloud">
            <h3 style="border-bottom:1px solid var(--border-color); padding-bottom:10px; margin-bottom:20px;">
              <span class="text-blue">Cloud</span> & DevOps Infrastructure
            </h3>
            <div class="grid-4">
              <div class="card" style="padding:20px;">
                <h4>Amazon Web Services (AWS)</h4>
                <p style="font-size:0.85rem;">EC2, S3, RDS, Lambda serverless, and CloudFront distribution.</p>
                <span class="tag-pill">Cloud Infrastructure</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>Microsoft Azure & GCP</h4>
                <p style="font-size:0.85rem;">Enterprise cloud deployments and Google Cloud workloads.</p>
                <span class="tag-pill">Multi-Cloud</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>Docker & Containers</h4>
                <p style="font-size:0.85rem;">Isolated containerized environments ensuring dev/prod parity.</p>
                <span class="tag-pill">Containers</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>Git & CI/CD Pipelines</h4>
                <p style="font-size:0.85rem;">Automated testing and continuous delivery deployments.</p>
                <span class="tag-pill">Automation</span>
              </div>
            </div>
          </div>

          <!-- 6. APIs & Integrations -->
          <div class="tech-group-panel" data-group="apis">
            <h3 style="border-bottom:1px solid var(--border-color); padding-bottom:10px; margin-bottom:20px;">
              <span class="text-violet">APIs</span> & System Integrations
            </h3>
            <div class="grid-4">
              <div class="card" style="padding:20px;">
                <h4>RESTful Web APIs</h4>
                <p style="font-size:0.85rem;">Structured, versioned JSON endpoints with OpenAPI specs.</p>
                <span class="tag-pill">Standards</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>Webhooks & Event Streams</h4>
                <p style="font-size:0.85rem;">Instant real-time event notifications and payload ingestion.</p>
                <span class="tag-pill">Real-Time</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>Payment Integrations</h4>
                <p style="font-size:0.85rem;">Stripe, PayPal, and merchant gateway tokenized APIs.</p>
                <span class="tag-pill">Secure Payments</span>
              </div>
              <div class="card" style="padding:20px;">
                <h4>Enterprise Bridges</h4>
                <p style="font-size:0.85rem;">Bi-directional connectors for CRM, ERP, and logistics hubs.</p>
                <span class="tag-pill">Data Sync</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="card" style="text-align: center; padding: 48px; margin-top: 60px;">
        <h3>Need advice on the right technology stack for your project?</h3>
        <p style="max-width: 600px; margin: 12px auto 24px auto;">
          Contact our software architects to review your technical requirements and select an optimal, cost-efficient tech stack.
        </p>
        <a href="request-quote.html" class="btn btn-primary btn-lg">Request Tech Stack Consultation</a>
      </div>
    </div>
  </section>
"""
}

print("Loaded Module 2 (Engineering & Directories).")
