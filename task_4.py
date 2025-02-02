from pydantic import BaseModel, Field
from openai import OpenAI
from typing import List


class SearchItem(BaseModel):
    title: str = Field(..., title="Title of the search result")
    url: str = Field(..., title="URL of the search result")
    short_description: str = Field(
        ..., title="Short snippet/description of the article"
    )


class SearchResult(BaseModel):
    search_results: List[SearchItem] = Field(..., title="List of search results")


info_strings = [
    """
    Here’s your programming language scoop for 2025!

    🚀 Top 5 Programming Languages to Learn in 2025 – Python, Rust, Go… the future is here! Dive in www.techblog.com/top5-2025 .

    🐍 Why Python Will Still Dominate in 2025 – Python isn’t going anywhere! See why www.devnews.com/python-2025 .

    ⚔️ Rust vs. Go: The Ultimate Battle – Who wins in systems programming? Find out. www.codeworld.com/rust-vs-go .
    """,
    """
    Here’s what I found for you:

    🔹 Top 5 Programming Languages to Learn in 2025 – Python, Rust, Go, and more! Check it outwww.techblog.com/top5-2025.

    🔹 Why Python Will Still Dominate in 2025 – AI, web dev, and data science love Python! Read more www.devnews.com/python-2025.

    🔹 Rust vs. Go: The Best Language for Systems Programming – Which one’s better for high-performance apps? Find out here www.codeworld.com/rust-vs-go.
    """,
]

client = OpenAI()

for info_str in info_strings:

    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "You are a friendly assistant. You help extract information from prose",
            },
            {"role": "user", "content": info_str},
        ],
        response_format=SearchResult,
    )

    response = response.choices[0].message.parsed

    print(info_str, response, "", sep="\n")
