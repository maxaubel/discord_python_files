from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='YOUR URL', username="HAL-9000")

with open("python.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='example.jpg')

response = webhook.execute()
print(response)
test