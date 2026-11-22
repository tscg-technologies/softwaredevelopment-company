"""
Master Compiler for SOFTWARE DEVELOPMENT COMPANY website
Compiles all 26 HTML pages, sitemap.xml, IMAGE-GENERATION-GUIDE.md, and README.md
"""
import os
import sys

# Import base templates and page registries
from generator_base import HEADER_TEMPLATE, FOOTER_TEMPLATE
from build_all_pages import pages_data, IMAGE_CATALOG

# Import modular page definitions
import generate_pages_part1
import generate_pages_part2
import generate_pages_part3

EXPECTED_PAGES = [
    "index.html",
    "about.html",
    "custom-software.html",
    "web-applications.html",
    "saas-development.html",
    "crm-development.html",
    "erp-development.html",
    "pos-development.html",
    "inventory-software.html",
    "ecommerce-development.html",
    "mobile-apps.html",
    "business-automation.html",
    "api-integration.html",
    "database-development.html",
    "software-modernization.html",
    "software-maintenance.html",
    "industries.html",
    "technologies.html",
    "development-process.html",
    "portfolio.html",
    "case-studies.html",
    "careers.html",
    "blog.html",
    "faq.html",
    "contact.html",
    "request-quote.html"
]

def compile_pages():
    print(f"Total registered pages: {len(pages_data)}")
    assert len(pages_data) == 26, f"Expected 26 pages, got {len(pages_data)}"

    for filename in EXPECTED_PAGES:
        if filename not in pages_data:
            print(f"ERROR: Missing page definition for {filename}")
            sys.exit(1)

        p = pages_data[filename]
        header = HEADER_TEMPLATE.format(
            meta_title=p["title"],
            meta_desc=p["desc"],
            meta_keywords=p["keywords"],
            filename=filename
        )
        full_html = header + "\n" + p["content"] + "\n" + FOOTER_TEMPLATE

        with open(filename, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"Compiled: {filename}")

def compile_sitemap():
    urls = []
    for filename in EXPECTED_PAGES:
        priority = "1.0" if filename == "index.html" else ("0.9" if "development" in filename or "software" in filename else "0.8")
        urls.append(f"""  <url>
    <loc>https://demo.example.com/{filename}</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>""")

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>
"""
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("Compiled: sitemap.xml")

def compile_image_guide():
    total_count = len(IMAGE_CATALOG)
    landscape_count = sum(1 for img in IMAGE_CATALOG if img["orientation"] == "Landscape")
    portrait_count = sum(1 for img in IMAGE_CATALOG if img["orientation"] == "Portrait")
    square_count = sum(1 for img in IMAGE_CATALOG if img["orientation"] == "Square")

    guide_lines = [
        "# IMAGE GENERATION GUIDE FOR GOOGLE FLOW",
        "",
        "This master documentation contains the complete inventory of all image placeholders designed for the **Software Development Company** website.",
        "Use this guide to generate each high-fidelity graphic asset separately using **Google Flow**, and then seamlessly integrate them into the website's `assets/images/` directory.",
        "",
        "---",
        "",
        "## 1. EXECUTIVE SUMMARY & INVENTORY METRICS",
        "",
        f"- **Total Images in Catalog:** {total_count}",
        f"- **Landscape Images (16:9, 16:10):** {landscape_count}",
        f"- **Portrait Images (9:16):** {portrait_count}",
        f"- **Square Images (1:1):** {square_count}",
        "- **Target Destination Folder:** `assets/images/`",
        "- **Technology Requirement:** Zero external image URLs or downloads used in production.",
        "",
        "---",
        "",
        "## 2. FILENAME-TO-PAGE MAPPING TABLE",
        "",
        "| Image # | Exact Filename | Page | Section | Ratio | Resolution | Orientation |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |"
    ]

    for img in IMAGE_CATALOG:
        guide_lines.append(
            f"| {img['num']:02d} | `{img['filename']}` | `{img['page']}` | {img['section']} | {img['ratio']} | {img['resolution']} | {img['orientation']} |"
        )

    guide_lines.extend([
        "",
        "---",
        "",
        "## 3. INDIVIDUAL COPY-READY GOOGLE FLOW PROMPTS",
        "",
        "Generate images in the specified order below. Each entry provides full contextual parameters along with an exhaustive, copy-ready prompt string optimized for Google Flow image models.",
        ""
    ])

    for img in IMAGE_CATALOG:
        pr = img["prompt"]
        prompt_block = (
            f"### Image {img['num']:02d}: `{img['filename']}`\n\n"
            f"- **HTML Page:** `{img['page']}`\n"
            f"- **Website Section:** {img['section']}\n"
            f"- **Image Purpose:** {img['purpose']}\n"
            f"- **Recommended Ratio:** {img['ratio']}\n"
            f"- **Target Resolution:** {img['resolution']} px\n"
            f"- **Orientation:** {img['orientation']}\n"
            f"- **Visual Description:** {img['desc']}\n\n"
            f"#### Copy-Ready Google Flow Prompt\n"
            f"```text\n"
            f"High-end corporate software technology photography and 3D digital UI render. "
            f"Main Subject: {pr['subject']}. "
            f"Software Environment: {pr['environment']}. "
            f"Composition: {pr['composition']}. "
            f"Camera & Angle: {pr['camera']}. "
            f"Lighting: {pr['lighting']}. "
            f"Background: {pr['background']}. "
            f"Color Palette: {pr['colors']}. "
            f"Visual Style: {pr['style']}. "
            f"Mood & Atmosphere: {pr['mood']}. "
            f"Aspect Ratio: {pr['ratio']}. "
            f"Negative Instructions: {pr['negative']}.\n"
            f"```\n\n"
            f"---"
        )
        guide_lines.append(prompt_block)

    guide_lines.extend([
        "",
        "## 4. IMAGE GENERATION ORDER & PRIORITY",
        "",
        "To achieve maximum aesthetic cohesion, generate images in this prioritized sequence:",
        "1. **Core Homepage & Brand Assets (Images 01 to 06):** Establishes the foundational lighting, cyan/electric blue palette, and futuristic software styling.",
        "2. **Service & Product Previews (Images 07 to 13):** Renders the custom software, web app, CRM, ERP, POS, and inventory dashboards.",
        "3. **Mobile Screen Mockups (Images 14 & 15):** Renders the vertical 9:16 mobile client screens.",
        "4. **Portfolio & Case Study Assets (Images 16 to 24):** Generates representative project previews and technical architecture diagrams.",
        "5. **Blog & Insight Headers (Image 25):** Produces educational architecture visualizations.",
        "",
        "---",
        "",
        "## 5. PLACEHOLDER REPLACEMENT INSTRUCTIONS",
        "",
        "Once you have generated all image files using Google Flow:",
        "1. Download and rename each image to match the **Exact Filename** listed in Section 2.",
        "2. Place the image files into the website's `assets/images/` directory.",
        "3. In the HTML files, locate the corresponding placeholder element:",
        "   ```html",
        "   <div class=\"img-placeholder\" data-ratio=\"16:9\" ...>",
        "     ...",
        "     <code class=\"placeholder-filename\">filename.jpg</code>",
        "     ...",
        "   </div>",
        "   ```",
        "4. Replace the `<div class=\"img-placeholder\">` container with standard responsive image markup:",
        "   ```html",
        "   <img src=\"assets/images/filename.jpg\" alt=\"[Descriptive Alt Text]\" class=\"img-responsive\" width=\"1280\" height=\"800\" loading=\"lazy\">",
        "   ```",
        "5. Alternatively, add CSS background images pointing to `assets/images/filename.jpg` while preserving all accessibility and layout containment."
    ])

    with open("IMAGE-GENERATION-GUIDE.md", "w", encoding="utf-8") as f:
        f.write("\n".join(guide_lines))
    print("Compiled: IMAGE-GENERATION-GUIDE.md")

def compile_readme():
    readme_md = f"""# Custom Software Development Company — Corporate Website Demo

A complete, premium, responsive multi-page corporate website demo engineered for a **Custom Software Development Company**.

---

## 1. TECHNOLOGY STACK & ARCHITECTURE

- **HTML5:** Semantic, accessible markup with strong hierarchy, ARIA attributes, and Open Graph meta tags.
- **CSS3:** Handcrafted modern CSS without external CSS frameworks (No Bootstrap, Tailwind, or Sass). Features CSS custom variables, fluid `clamp()` typography, flexbox, and responsive CSS grids.
- **Vanilla JavaScript (ES6+):** Zero external JS libraries (No jQuery, React, Vue, Angular, or Node.js runtime).
- **Static Hosting Compatible:** 100% compatible with Hostinger Static Hosting, GitHub Pages, Vercel, Netlify, or standard Apache/Nginx web servers.

---

## 2. WEBSITE STRUCTURE & 26 HTML PAGES

| # | Filename | Page Title / Description |
| :- | :--- | :--- |
| 01 | `index.html` | Homepage: Hero, Capabilities, Product Previews, Process, Tech Stack, Portfolio Preview |
| 02 | `about.html` | About Company: Mission, Vision, Engineering Philosophy, How We Work |
| 03 | `custom-software.html` | Custom Software Development: Bespoke Enterprise Applications & Lifecycle |
| 04 | `web-applications.html` | Web Application Development: Business Portals, Dashboards & Architecture |
| 05 | `saas-development.html` | SaaS Development: Multi-Tenant Architecture & Interactive Telemetry Demo |
| 06 | `crm-development.html` | CRM Software Development: Lead Pipelines & Interactive Lead Table Demo |
| 07 | `erp-development.html` | ERP Software Development: Multi-Module Operations & Interactive Demo |
| 08 | `pos-development.html` | POS & Billing Software: Checkout Registers & Interactive Billing Demo |
| 09 | `inventory-software.html` | Inventory Management Software: Warehouse SKU Tracking & Live Stock Demo |
| 10 | `ecommerce-development.html`| E-commerce Development: Custom Storefronts & Order Routing |
| 11 | `mobile-apps.html` | Mobile Application Development: iOS, Android & Field Mobility |
| 12 | `business-automation.html` | Business Process Automation: Interactive 6-Stage Workflow Engine |
| 13 | `api-integration.html` | API & System Integration: RESTful APIs, Webhooks & SVG Architecture |
| 14 | `database-development.html`| Database Design & Development: Relational Schemas & Optimization |
| 15 | `software-modernization.html`| Software Modernization: Legacy Migration & Architecture Upgrades |
| 16 | `software-maintenance.html`| Software Maintenance & Support: Bug Fixes, Security & Longevity |
| 17 | `industries.html` | Industries We Serve: 12 Business Sectors & Custom Software Opportunities |
| 18 | `technologies.html` | Technologies & Tools Directory: Filterable Tech Stack |
| 19 | `development-process.html` | Our Development Process: Detailed 7-Step Software Lifecycle |
| 20 | `portfolio.html` | Software Portfolio: 8 Filterable Demo Project Concepts |
| 21 | `case-studies.html` | Case Studies: 5 Fictional Problem-and-Solution Scenarios |
| 22 | `careers.html` | Careers: Engineering Culture, 8 Demo Roles & Application Form |
| 23 | `blog.html` | Software Development Insights: 8 In-Depth Technical Articles |
| 24 | `faq.html` | Frequently Asked Questions: 13 Interactive Accordions |
| 25 | `contact.html` | Contact Us: Generic Demo Placeholders & Contact Form |
| 26 | `request-quote.html` | Request a Quote: Custom Software Project Estimation Form |

---

## 3. INTERACTIVE FEATURES (100% VANILLA JS)

- **CRM Dashboard Demo (`crm-development.html`):** Filter by lead status, search leads, simulate stage updates, and see live toast confirmations.
- **ERP Dashboard Demo (`erp-development.html`):** Switch between Sales, Inventory, Purchasing, and Finance modules with real-time record relationship views.
- **POS Billing Interface Demo (`pos-development.html`):** Tap product cards to add items to cart, adjust quantities, calculate subtotal and tax, and test checkout simulation.
- **Inventory Dashboard Demo (`inventory-software.html`):** Test real-time stock movements with `+5 In` and `-2 Out` buttons updating stock badges.
- **SaaS Telemetry Demo (`saas-development.html`):** Switch between 7D, 30D, 90D, and 1Y timeframes to view dynamic changes in MRR and user metrics.
- **Business Process Automation Diagram (`business-automation.html`):** Interactive 6-stage clickable flowchart updating technical descriptions dynamically.
- **Portfolio & Technology Category Filters:** Instant category filtering without page reloads.
- **Accessible FAQ Accordions:** Keyboard-navigable with ARIA expanded states and smooth height transitions.
- **Form Validations:**
  - Quote Request Form: Validates inputs, character counter on description (up to 1500 chars), budget selector, and outputs: `"Your demo project enquiry has been validated. No information has been transmitted or stored."`
  - Contact Form & Careers Application Form: Validates required inputs and provides clear demo toast feedback without transmitting data.

---

## 4. ZERO EXTERNAL ASSETS & GOOGLE FLOW WORKFLOW

- All visual elements use pure CSS3 and inline SVG code.
- Zero external image dependencies ensure zero layout shifts and maximum loading speeds.
- All 25 image placeholders across the site are fully documented with copy-ready prompts in **`IMAGE-GENERATION-GUIDE.md`**.

---

## 5. HOSTINGER STATIC HOSTING DEPLOYMENT GUIDE

1. **Hostinger File Manager / FTP:**
   - Log into your Hostinger control panel (hPanel).
   - Navigate to **Files &rarr; File Manager** or connect via FTP.
   - Open the target domain folder (usually `public_html/`).
2. **Upload Files:**
   - Upload all 26 HTML files, `sitemap.xml`, and the `assets/` folder (`assets/css/style.css`, `assets/js/main.js`, `assets/images/`, `assets/icons/`) directly into `public_html/`.
3. **Verify Deployment:**
   - Visit `https://your-domain.com/` in your browser.
   - Verify that SSL is active (HTTPS).
   - Verify navigation across all 26 pages.

---

## 6. BRAND & EDITABLE PLACEHOLDERS

- **Brand Identity:** `SOFTWARE DEVELOPMENT COMPANY` (Generic business identity).
- **Logo:** Minimalist symbol-only inline SVG (abstract interconnected nodes).
- **Tagline:** "WE TURN COMPLEX BUSINESS IDEAS INTO POWERFUL SOFTWARE."
- **Phone:** `0000000000` / `0000000000`
- **Email:** `demo@example.com`
- **Address:** `Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000.`
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_md)
    print("Compiled: README.md")

if __name__ == "__main__":
    compile_pages()
    compile_sitemap()
    compile_image_guide()
    compile_readme()
    print("Master compilation complete.")
