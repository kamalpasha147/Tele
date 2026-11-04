import os

# GitHub Actions-এ, এই মানগুলো workflow ফাইলের env থেকে আসবে
GEMINI_KEY = os.environ.get("GEMINI_KEY")
TG_TOKEN = os.environ.get("TG_TOKEN")
TG_CHAT = os.environ.get("TG_CHAT")

if not all([GEMINI_KEY, TG_TOKEN, TG_CHAT]):
    print("ত্রুটি: প্রয়োজনীয় গোপনীয় তথ্য অনুপস্থিত")
    exit(1)
