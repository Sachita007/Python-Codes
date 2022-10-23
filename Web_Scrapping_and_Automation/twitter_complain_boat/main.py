from Twitter_Complain_Bot import InternetSpeedTwitterBot
UP = 100
DOWN = 150

PASSWORD = "Sachita1@"
USERNAME = "Sachita620259"

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
upload = float(bot.up)
download = float(bot.down)
if download<DOWN or upload<UP:
    bot.tweet_at_provider(email=USERNAME, password=PASSWORD)