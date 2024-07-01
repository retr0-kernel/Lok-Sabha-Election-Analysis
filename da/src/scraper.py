import requests
import time

urls = [
    "https://results.eci.gov.in/PcResultGenJune2024/index.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S27.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S10.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S11.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U09.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U06.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S12.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S06.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S07.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S08.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U08.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S02.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S03.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S04.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U02.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S26.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U03.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S05.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U01.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S01.htm"
]

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

for i, url in enumerate(urls, 1):
    print(f"Scraping URL {i}/{len(urls)}: {url}")
    html_content = fetch_html(url)
    
    if html_content:
        filename = f"scraped_html_{i}.html"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"HTML content saved to {filename}")
    else:
        print(f"Failed to scrape {url}")
        time.sleep(2)

print("Scraping completed.")