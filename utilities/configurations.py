import os

# Configuration Management using Environment Variables
api_key = os.getenv("OPENAQ_API_KEY")
base_url = os.getenv("OPENAQ_BASE_URL", "https://api.openaq.org/v3")

if not api_key:
 raise ValueError(
 "OPENAQ_API_KEY is not set. Please set it using:\n"
 " export OPENAQ_API_KEY=your_key\n"
 " source ~/.bashrc # if added to .bashrc"
 )