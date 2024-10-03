import asyncio
import re

import aiohttp
from bs4 import BeautifulSoup


class WebSearcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    async def bing_search(self, query, count=10):
        url = "https://api.bing.microsoft.com/v7.0/search"
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        params = {
            "q": query,
            "count": count,
            "textDecorations": True,
            "textFormat": "HTML",
        }
        async with self.session.get(url, headers=headers, params=params) as response:
            return await response.json()

    @staticmethod
    def strip_html(html_content):
        soup = BeautifulSoup(html_content, "lxml")
        for script in soup(["script", "style"]):
            script.decompose()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = "\n".join(chunk for chunk in chunks if chunk)
        return re.sub(r"\n{3,}", "\n\n", text)

    async def get_page_content(self, url):
        try:
            async with self.session.get(url, timeout=10) as response:
                html = await response.text()
                return self.strip_html(html)
        except Exception as e:
            print(f"Error fetching {url}: {str(e)}")
            return None

    async def process_search_results(self, search_results):
        tasks = []
        for item in search_results.get("webPages", {}).get("value", []):
            url = item["url"]
            task = asyncio.create_task(self.get_page_content(url))
            tasks.append(task)
        return await asyncio.gather(*tasks)

    async def search_and_process(self, query, count=10):
        search_results = await self.bing_search(query, count)
        content_array = await self.process_search_results(search_results)
        return [content for content in content_array if content]


async def search_web(api_key, query, count=10):
    async with WebSearcher(api_key) as searcher:
        return await searcher.search_and_process(query, count)


# Example usage
if __name__ == "__main__":
    API_KEY = "YOUR_BING_API_KEY"
    QUERY = "your search query"

    async def main():
        results = await search_web(API_KEY, QUERY)
        for i, content in enumerate(results, 1):
            print(f"Content from result {i}:")
            print(content[:500])  # Print first 500 characters as a preview
            print("\n---\n")

    asyncio.run(main())
