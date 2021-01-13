from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='', username="LVA")

with open("python.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='example.jpg')

response = webhook.execute()