# MARADMIN Telegram Notifier Bot

A lightweight Dockerized Python bot that monitors the official USMC
MARADMIN RSS feed and immediately sends newly posted MARADMINs to your
Telegram account.

This bot:

-   Polls the official MARADMIN RSS feed
-   Detects and remembers new MARADMINs
-   Sends each new message to you via Telegram with title + link
-   Runs automatically inside a Docker container
-   Keeps state so you never receive duplicates

------------------------------------------------------------------------

## 1. Installation

### Clone the repository

``` bash
git clone https://github.com/rmilanese/maradmin-telegram-bot.git
cd maradmin-telegram-bot
```

------------------------------------------------------------------------

## 2. Create Your Telegram Bot

1.  Open Telegram\
2.  Search for **@BotFather**\
3.  Run `/start`\
4.  Run `/newbot` and follow prompts\
5.  BotFather gives you a **Bot Token**, save it.

------------------------------------------------------------------------

## 3. Get Your Telegram Chat ID

1.  Open Telegram\
2.  Search for **@userinfobot**\
3.  Type `/start`\
4.  It replies with your **chat ID**

Save this as well.

------------------------------------------------------------------------

## 4. Initiate Bot Conversation

1. Open Telegram\
2. Search for your new bot by its username\
3. Click **Start** to initiate conversation

------------------------------------------------------------------------


## 5. Configuration

Open `docker-compose.yml` and set:

``` yaml
environment:
  TELEGRAM_TOKEN: "YOUR_TELEGRAM_BOT_TOKEN"
  TELEGRAM_CHAT_ID: "YOUR_CHAT_ID"
```

------------------------------------------------------------------------

## 6. Run With Docker

Build and start the bot:

``` bash
docker compose up -d
```

View logs:

``` bash
docker compose logs -f
```

Stop the bot:

``` bash
docker compose down
```

------------------------------------------------------------------------

## How It Works

The bot checks the MARADMIN RSS feed every 5 minutes.

For each `<item>`, it extracts:

-   `<title>`
-   `<link>`
-   `<guid>`

If the GUID has not been seen before, it sends:

    New MARADMIN Posted

    <TITLE>
    <URL>

It then records the GUID in `data/sent.json` so you don't receive
duplicates.

------------------------------------------------------------------------

## 📂 File Structure

    maradmin-telegram-bot/
    ├── bot.py                # main bot logic
    ├── requirements.txt      # python deps
    ├── Dockerfile            # container build
    ├── docker-compose.yml    # easier deployment
    ├── README.md             # documentation
    └── data/                 # persistent storage

------------------------------------------------------------------------

## Future Work

-   Filters (e.g., only send PMOS-related MARADMINs)
-   Push to a Telegram channel/group
-   Log to a local file or Grafana Loki
-   HTML formatting with inline buttons
-   Notifications for all USMC message traffic (ALMAR, NAVADMIN, etc.)

------------------------------------------------------------------------

## License

MIT License -- free to use, modify, fork, deploy.

------------------------------------------------------------------------

## 🤝 Contributions

Pull requests welcome.
