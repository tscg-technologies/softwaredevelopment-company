"""
Quality Assurance Test Script for SOFTWARE DEVELOPMENT COMPANY Website (Images Updated)
"""
import os
import re

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

def run_qa():
    errors = []
    print("--- 1. VERIFYING ALL 26 HTML PAGES EXIST ---")
    for page in EXPECTED_PAGES:
        if not os.path.exists(page):
            errors.append(f"Missing HTML page: {page}")
        else:
            size = os.path.getsize(page)
            if size < 500:
                errors.append(f"Page {page} is too small ({size} bytes)")
    print(f"Verified {len(EXPECTED_PAGES)} HTML pages exist.")

    print("\n--- 2. VERIFYING SUPPORTING ASSETS ---")
    assets = [
        "assets/css/style.css",
        "assets/js/main.js",
        "assets/images/README.md",
        "sitemap.xml",
        "IMAGE-GENERATION-GUIDE.md",
        "README.md"
    ]
    for asset in assets:
        if not os.path.exists(asset):
            errors.append(f"Missing asset: {asset}")
        else:
            print(f"Verified asset: {asset} ({os.path.getsize(asset)} bytes)")

    print("\n--- 3. CHECKING INTERNAL LINKS & REFERENCES ---")
    all_links = set()
    for page in EXPECTED_PAGES:
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()

        hrefs = re.findall(r'href="([^"#:]+)(?:#[^"]*)?"', content)
        for href in hrefs:
            if href.endswith(".html"):
                all_links.add(href)
                if not os.path.exists(href):
                    errors.append(f"Broken link in {page}: href='{href}' does not exist")

    print(f"Checked internal links across all pages. Found {len(all_links)} unique HTML references.")

    print("\n--- 4. VERIFYING REAL IMAGE REFERENCES ON DISK ---")
    images_found = set()
    for page in EXPECTED_PAGES:
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()

        # Find img src
        matches = re.findall(r'<img [^>]*src="([^"]+)"', content)
        for m in matches:
            images_found.add(m)
            if not os.path.exists(m):
                errors.append(f"Image '{m}' in {page} does not exist on disk!")

    print(f"Found {len(images_found)} unique image references across all 26 HTML pages.")
    for img_path in sorted(images_found):
        size = os.path.getsize(img_path)
        print(f"  [OK] {img_path} ({size} bytes)")

    print("\n--- 5. CHECKING REQUIRED PROMPT CONSTRAINTS ---")
    disallowed = ["react.js", "bootstrap.min.css", "tailwind", "jquery.min.js", "angular.js"]
    for page in EXPECTED_PAGES:
        with open(page, "r", encoding="utf-8") as f:
            content = f.read().lower()
            for d in disallowed:
                if f'src="{d}"' in content or f'href="{d}"' in content:
                    errors.append(f"Disallowed library reference {d} found in {page}")

    with open("assets/js/main.js", "r", encoding="utf-8") as f:
        js_code = f.read()
        target_quote_toast = "Your demo project enquiry has been validated. No information has been transmitted or stored."
        if target_quote_toast not in js_code:
            errors.append("Required Quote Toast message not found verbatim in main.js!")
        else:
            print("Verified exact quote validation message in main.js")

    print("\n--- QA SUMMARY ---")
    if errors:
        print(f"FAILED WITH {len(errors)} ERRORS:")
        for err in errors:
            print(f"  [ERROR] {err}")
    else:
        print("ALL QUALITY ASSURANCE CHECKS PASSED WITH 100% SUCCESS!")

if __name__ == "__main__":
    run_qa()
