from bot.client import BotClient
import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("credentials.conf")

    if "API" in config and "KEY" in config["API"] and "SECRET" in config["API"]:
        BotClient(config["API"]["KEY"], config["API"]["SECRET"]).run()
    else:
        print("credentials.conf file is missing or misconfigured")
