import time
import json
import os
import feedparser
import logging
from telegram import Bot

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')

RSS_URL = "https://www.marines.mil/DesktopModules/ArticleCS/RSS.ashx?ContentType=6&Site=481&max=10&category=14336"
STATE_FILE = "data/sent.json"

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")  # your user ID


def load_state():
    if not os.path.exists(STATE_FILE):
        return set()
    try:
        with open(STATE_FILE, "r") as f:
            return set(json.load(f))
    except:
        return set()


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(list(state), f)


def fetch_maradmins():
    return feedparser.parse(RSS_URL).entries


def format_message(entry):
    title = entry.title.strip()
    link = entry.link.strip()
    return f"📄 *New MARADMIN Posted*\n\n*{title}*\n{link}"


def main():
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        raise SystemExit("ERROR: TELEGRAM_TOKEN and TELEGRAM_CHAT_ID must be set.")

    bot = Bot(token=TELEGRAM_TOKEN)
    sent_ids = load_state()

    logging.info("MARADMIN bot started. Monitoring feed...")

    while True:
        try:
            entries = fetch_maradmins()

            for entry in entries:
                guid = entry.get("id", entry.link).strip()

                if guid not in sent_ids:
                    msg = format_message(entry)
                    bot.send_message(
                        chat_id=TELEGRAM_CHAT_ID,
                        text=msg,
                        parse_mode="Markdown"
                    )

                    logging.info(f"Sent MARADMIN: {entry.title}")
                    sent_ids.add(guid)
                    save_state(sent_ids)

        except Exception as e:
            logging.error(f"Error: {e}")

        time.sleep(300)  # check every 5 minutes


if __name__ == "__main__":
    main()
