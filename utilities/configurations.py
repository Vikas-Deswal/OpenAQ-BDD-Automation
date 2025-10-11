import os

# .env
api_key = os.getenv("OPENAQ_API_KEY")
base_url = os.getenv("OPENAQ_BASE_URL", "https://api.openaq.org/v3")