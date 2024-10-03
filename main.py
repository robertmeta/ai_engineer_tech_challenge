import os

import bottle
from bottle import Bottle, jinja2_view, request, run

from oq import ollama_query
from web_search import DuckDuckGoSearcher

app = Bottle()

template_path = os.path.join(os.path.dirname(__file__), "views")
bottle.TEMPLATE_PATH.insert(0, template_path)


@app.route("/")
@jinja2_view("index.j2")
def index():
    return {}


@app.route("/search", method="POST")
@jinja2_view("result.j2")
def search():
    query = request.forms.get("query")

    # Use DuckDuckGoSearcher for web search
    searcher = DuckDuckGoSearcher()
    results = searcher.search(query, num_results=20)
    prompt = ""

    # Prepare prompt for Ollama
    for result in results:
        # Assuming the result is a tuple, let's print it to see its structure
        # print(f"Result: {result}")
        # For now, we'll just add the whole result to the prompt
        prompt += f"""

        {result}

        """

    prompt += f"""
    with the above information only, please respond to '{query}' in simple html markup with no additional feedback at all, just answer the question in html and if you can't then output that you don't know."""
    print(prompt)

    # Use ollama_query function to get the response
    answer = ollama_query(prompt)

    # Extract a relevant link from search results
    # We'll need to adjust this based on the actual structure of the results
    link = (
        results[0][2] if results else ""
    )  # Assuming the URL is the third item in the tuple

    return {"answer": answer, "link": link}


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8080, debug=True)
