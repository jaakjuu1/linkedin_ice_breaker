from langchain.serpapi import SerpAPIWrapper


def get_profile_url(text: str) -> str:
    """Searches for LinkedIn profile page."""
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res
