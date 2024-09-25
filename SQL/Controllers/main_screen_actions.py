import Interfaces.user_commands as user_commands
from Models.Users import *
import Controllers.search_tweets_actions as search_tweets_actions
import Controllers.search_users_actions as search_users_actions
import Controllers.compose_tweets as compose_tweets
import Controllers.list_followers_actions as list_followers_actions

def main_screen(conn, cursor, user):

    while True:
        command = input (user_commands.commands)
        if command == '1':
            search_tweets_actions.search_tweets(user, conn, cursor)
        elif command == '2':
            search_users_actions.search_for_users(conn, cursor, user)
        elif command == '3':
            compose_tweets.compose_tweet(conn, cursor, user, None)
        elif command == '4':
            list_followers_actions.list_followers(conn, cursor, user)
        elif command == '5':
            return
        else:
            print("Unrecognizable command! Try again!")

