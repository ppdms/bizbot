from pollevbot import PollBot
from pollevbot.creds import user, password

def main():
    host = "panagiotasap513" #'tyrellwellick638'

    with PollBot(user, password, host, login_type='pollev') as bot:
        bot.run()

if __name__ == '__main__':
    main()
