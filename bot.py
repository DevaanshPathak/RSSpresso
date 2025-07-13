import os
import discord
import feedparser
import asyncio
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

# Load environment variables from .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
PORT = int(os.getenv("PORT", 3000))

# RSS Feeds to fetch from
FEEDS = [
    ("Hacker News", "https://hnrss.org/frontpage"),
    ("The Verge", "https://www.theverge.com/rss/index.xml")
]

# Track previously posted links
posted_links = set()

# Discord client
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Background task to fetch and post news
async def fetch_and_post():
    await client.wait_until_ready()
    print("✅ RSS loop started.")
    
    while not client.is_closed():
        print("⏰ Checking feeds...")
        channel = client.get_channel(CHANNEL_ID)
        
        if not channel:
            print(f"❌ Channel ID {CHANNEL_ID} not found. Make sure the bot is invited and ID is correct.")
        else:
            print(f"📢 Found channel: {channel.name}")
            for name, url in FEEDS:
                feed = feedparser.parse(url)
                for entry in feed.entries[:3]:
                    if entry.link not in posted_links:
                        posted_links.add(entry.link)
                        message = f"📰 **{entry.title}**\n{name} | {entry.link}"
                        await channel.send(message)
                        print(f"✅ Posted: {entry.title}")
        
        await asyncio.sleep(600)  # Wait 10 minutes before checking again

@client.event
async def on_ready():
    print(f"🤖 Logged in as {client.user}")
    client.loop.create_task(fetch_and_post())

# Keep-alive Flask web server (for Nest or uptime pings)
app = Flask('')

@app.route('/')
def home():
    return "RSSpresso is running!"

def run_flask():
    app.run(host='0.0.0.0', port=PORT)

def keep_alive():
    thread = Thread(target=run_flask)
    thread.start()

# Start everything
print("🚀 Launching RSSpresso...")
keep_alive()
client.run(TOKEN)
