from discord_webhook import DiscordWebhook, DiscordEmbed

<<<<<<< HEAD
webhook = DiscordWebhook(url='YOUR URL', username="HAL-9000")
=======
webhook = DiscordWebhook(url='', username="HAL-9000")
>>>>>>> 69a66cb75434176c977a424a6ce7e97cbfaaba62

with open("python.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='example.jpg')

response = webhook.execute()
