from playwright.sync_api import sync_playwright


URL = "https://hanime.tv/downloads/emV0dGFpLWp1bnBha3UtbWFob3Utc2hvdWpv"


def scrape_links():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        print("Opening page...")
        page.goto(URL, wait_until="networkidle")

        print("Clicking Get Download links...")
        page.wait_for_selector("text=Get Download links")

        page.click("text=Get Download links")

        # wait for links to load
        page.wait_for_timeout(5000)

        urls = []

        anchors = page.query_selector_all("a[href]")

        for a in anchors:
            href = a.get_attribute("href")

            if href and href.startswith("http"):
                urls.append(href)

        urls = list(dict.fromkeys(urls))

        print("\n===== DOWNLOAD LINKS =====\n")

        if not urls:
            print("No links found.")
        else:
            for i, url in enumerate(urls, start=1):
                print(f"{i}. {url}")

        browser.close()


if __name__ == "__main__":
    scrape_links()
