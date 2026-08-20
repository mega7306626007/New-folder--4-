"""Centralized external API endpoint constants (Section 0).

Previously these URLs were scattered as string literals across
17_api_connectors.py and 11_llm_hybrid.py, which meant changing an
endpoint (or pointing at a self-hosted mirror/proxy) required a
multi-file search-and-replace. None of these are secrets - they're
public API base URLs - so centralizing them here is purely about
having one place to change instead of four.

Loads first (see main.py's _MODULE_FILES) since it has no
dependencies of its own and everything else may reference these
names.
"""

# --- Open-Meteo (weather) ---------------------------------------------
OPEN_METEO_GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
OPEN_METEO_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# --- Frankfurter (currency exchange rates) ------------------------------
FRANKFURTER_RATES_URL = "https://api.frankfurter.dev/v1/latest"
FRANKFURTER_HISTORICAL_URL_TEMPLATE = "https://api.frankfurter.dev/v1/{date}"
FRANKFURTER_CURRENCIES_URL = "https://api.frankfurter.dev/v1/currencies"

# --- Open Trivia Database ------------------------------------------------
OPENTDB_API_URL = "https://opentdb.com/api.php"
OPENTDB_CATEGORIES_URL = "https://opentdb.com/api_category.php"

# --- Translation ---------------------------------------------------------
LIBRETRANSLATE_DEFAULT_ENDPOINT = "https://libretranslate.com/translate"
MYMEMORY_TRANSLATE_URL = "https://api.mymemory.translated.net/get"

# --- Hacker News -----------------------------------------------------------
HN_TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_BEST_STORIES_URL = "https://hacker-news.firebaseio.com/v0/beststories.json"
HN_NEW_STORIES_URL = "https://hacker-news.firebaseio.com/v0/newstories.json"
HN_ASK_STORIES_URL = "https://hacker-news.firebaseio.com/v0/askstories.json"
HN_SHOW_STORIES_URL = "https://hacker-news.firebaseio.com/v0/showstories.json"
HN_ITEM_URL_TEMPLATE = "https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
HN_ITEM_PAGE_URL_TEMPLATE = "https://news.ycombinator.com/item?id={item_id}"

HN_STORY_LIST_URLS = {
    "top": HN_TOP_STORIES_URL,
    "best": HN_BEST_STORIES_URL,
    "new": HN_NEW_STORIES_URL,
    "ask": HN_ASK_STORIES_URL,
    "show": HN_SHOW_STORIES_URL,
}

# --- Openverse (image search) ---------------------------------------------
OPENVERSE_SEARCH_URL = "https://api.openverse.org/v1/images/"

# --- LLM providers -----------------------------------------------------------
ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_CONSOLE_KEYS_URL = "https://console.anthropic.com/settings/keys"
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_PLATFORM_KEYS_URL = "https://platform.openai.com/api-keys"
