#!/usr/bin/env python3
"""
Test script to verify the site structure and image references using Playwright
"""
from playwright.sync_api import sync_playwright
import time
import sys

def test_site_structure():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Testing site structure...")

        # Test main exercise page
        print("\n1. Testing main exercise page...")
        page.goto("http://localhost:8000/automation-exercises/exercises/01-email-classification/")
        time.sleep(2)

        # Check if overview loads
        title = page.title()
        print(f"   Page title: {title}")

        # Navigate to Part A
        print("\n2. Testing Part A: Environment Setup...")
        page.goto("http://localhost:8000/automation-exercises/exercises/01-email-classification/part-a-setup")
        time.sleep(2)

        # Check for images in Part A
        images = page.query_selector_all("img")
        print(f"   Found {len(images)} images in Part A")

        # Check specific images exist
        broken_images = []
        for img in images:
            src = img.get_attribute("src")
            if src:
                # Check if image loads
                result = page.evaluate("""(img) => {
                    return img.complete && img.naturalHeight !== 0;
                }""", img)
                if not result:
                    broken_images.append(src)
                    print(f"   ❌ Broken image: {src}")

        # Navigate to Part B
        print("\n3. Testing Part B: Build & Test...")
        page.goto("http://localhost:8000/automation-exercises/exercises/01-email-classification/part-b-workflow")
        time.sleep(2)

        # Check for images in Part B
        images = page.query_selector_all("img")
        print(f"   Found {len(images)} images in Part B")

        # Check for broken images
        for img in images:
            src = img.get_attribute("src")
            if src:
                result = page.evaluate("""(img) => {
                    return img.complete && img.naturalHeight !== 0;
                }""", img)
                if not result:
                    broken_images.append(src)
                    print(f"   ❌ Broken image: {src}")

        # Check navigation structure
        print("\n4. Checking navigation...")
        nav_links = page.query_selector_all("nav a")
        print(f"   Found {len(nav_links)} navigation links")

        # Report results
        print("\n" + "="*50)
        if broken_images:
            print(f"❌ Found {len(broken_images)} broken images:")
            for img in broken_images:
                print(f"   - {img}")
            browser.close()
            return False
        else:
            print("✅ All images loaded successfully!")
            browser.close()
            return True

if __name__ == "__main__":
    success = test_site_structure()
    sys.exit(0 if success else 1)
