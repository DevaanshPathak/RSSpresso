# ☕ RSSpresso

A hot, fresh RSS-powered news bot for Discord — brewed just for **Converge**.  
Get your daily dose of tech, dev, and world news delivered directly to your server.

> "Brewed fresh, posted fast — straight from the feed to your channel."

---

## ✨ Features

- 📰 Fetches top articles from multiple RSS feeds
- 🔁 Posts new content to a specific Discord channel every 10 minutes
- 🧠 Filters out duplicate links
- 🌐 Built with `discord.py`, `feedparser`, and `flask`
- 🔓 100% open-source and customizable

---

## 🛠️ Tech Stack

- Python 3.12+
- [discord.py](https://discordpy.readthedocs.io/)
- [feedparser](https://pythonhosted.org/feedparser/)
- [Flask](https://flask.palletsprojects.com/)

---

## 🚀 How It Works

RSSpresso checks selected RSS feeds every 10 minutes, filters out duplicates, and posts new headlines to a configured Discord channel.

By default, it pulls from:

- [Hacker News](https://hnrss.org/frontpage)
- [The Verge](https://www.theverge.com/rss/index.xml)

You can modify or expand the feed list inside the `bot.py` file.

---

## 🔧 Setup (Local)

1. **Clone the repo**:

```bash
git clone https://github.com/<yourusername>/rsspresso.git
cd rsspresso
````

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file**:

```env
TOKEN=your_discord_bot_token
CHANNEL_ID=your_discord_channel_id
PORT=3000
```

4. **Run the bot**:

```bash
python bot.py
```

The bot will begin posting RSS updates to your server!

---

## 📦 Future Improvements

* `!addfeed <url>` command to allow user-submitted feeds
* AI-powered article summaries (via OpenAI or Claude)
* Telegram or Slack support
* RSS category filtering (e.g., dev news, global news)

---

## 🏁 Built for Hack Club Converge

RSSpresso is a project for [Converge](https://converge.hackclub.com), part of [Summer of Making](http://summer.hackclub.com/).
Made with ☕ and 💻 by [@DevaanshPathak](https://github.com/devaanshpathak)
