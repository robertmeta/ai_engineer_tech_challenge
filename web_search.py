import asyncio
from typing import List, Tuple

import aiohttp
import html2text
from duckduckgo_search import DDGS


class DuckDuckGoSearcher:
    def __init__(self):
        self.ddgs = DDGS()
        self.html_converter = html2text.HTML2Text()
        self.html_converter.ignore_links = True
        self.html_converter.ignore_images = True
        self.html_converter.ignore_emphasis = True

    async def fetch_url(
        self, session: aiohttp.ClientSession, url: str
    ) -> Tuple[str, str]:
        try:
            async with session.get(url, timeout=10) as response:
                html = await response.text()
                return url, self.html_converter.handle(html)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return url, ""

    async def fetch_duckduckgo_page(
        self, session: aiohttp.ClientSession, query: str
    ) -> str:
        url = f"https://duckduckgo.com/html/?q={query}"
        try:
            async with session.get(url, timeout=10) as response:
                html = await response.text()
                return self.html_converter.handle(html)
        except Exception as e:
            print(f"Error fetching DuckDuckGo page: {e}")
            return ""

    async def search_and_fetch(
        self, query: str, num_results: int = 15
    ) -> List[Tuple[str, str, str]]:
        search_results = list(self.ddgs.text(query, max_results=num_results))

        async with aiohttp.ClientSession() as session:
            duckduckgo_page_task = self.fetch_duckduckgo_page(session, query)
            result_tasks = [
                self.fetch_url(session, result["href"]) for result in search_results
            ]

            duckduckgo_page = await duckduckgo_page_task
            contents = await asyncio.gather(*result_tasks)

        results = [
            (query, url, content.strip()) for url, content in contents if content
        ]

        # Add DuckDuckGo search result page as the first item
        results.insert(
            0, (query, f"https://duckduckgo.com/html/?q={query}", duckduckgo_page)
        )

        return results

    def search(self, query: str, num_results: int = 15) -> List[Tuple[str, str, str]]:
        return asyncio.run(self.search_and_fetch(query, num_results))


# Usage example:
if __name__ == "__main__":
    searcher = DuckDuckGoSearcher()
    results = searcher.search("Python programming")
    for i, (query, url, content) in enumerate(results):
        print(f"Result {i} for query '{query}':")
        print(f"URL: {url}")
        print(f"Content: {content[:200]}...\n")
