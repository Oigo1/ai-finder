import requests
from bs4 import BeautifulSoup
import json
import os
from categorize import classify_tool

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

SEARCH_TERMS = ["AI tool", "AI generator", "AI assistant", "AI site", "AI productivity"]

def get_ai_sites():
    base_url = "https://www.bing.com/search?q="
    results = []

    for term in SEARCH_TERMS:
        print(f"🔍 Searching for: {term}")
        response = requests.get(base_url + term, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')

        for a in soup.find_all('a', href=True):
            title = a.text.strip()
            url = a['href']

            if "http" in url and "ai" in url.lower() and len(title) > 5:
                category = classify_tool(title, url)
                results.append({
                    "name": title,
                    "function": category,
                    "url": url
                })

    return results

def save_tools(tools):
    file_path = os.path.join(os.path.dirname(__file__), 'models.json')

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing = json.load(file)
    else:
        existing = []

    existing_urls = {tool['url'] for tool in existing}
    new_tools = [t for t in tools if t['url'] not in existing_urls]

    all_tools = existing + new_tools

    with open(file_path, 'w') as file:
        json.dump(all_tools, file, indent=4)

    print(f"✅ Added {len(new_tools)} new tools.")

if __name__ == "__main__":
    tools = get_ai_sites()
    save_tools(tools)
