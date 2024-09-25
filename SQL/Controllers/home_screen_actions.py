import SQLs.tweets_queries as tweets_queries
import Interfaces.user_commands as user_commands
from Controllers.main_screen_actions import *
import Controllers.search_tweets_actions as search_tweets_actions

def print_tweets_home(conn, cursor, user, offset):
    cursor.execute(tweets_queries.followee_tweets, (user.get_usr(), offset))
    all_tweets = cursor.fetchall()

    for single_tweet in all_tweets:
        print("ID: " + str(single_tweet[0]) + " - Writer: " + str(single_tweet[1]) + " - Date: " + single_tweet[2] + " - Text: " + single_tweet[3])


def print_retweets_home(conn, cursor, user, offset):
    cursor.execute(tweets_queries.followee_retweets, (user.get_usr(), offset))
    all_retweets = cursor.fetchall()

    for retweet in all_retweets:
        print("User {} retweeted tweet {} on {}".format(retweet[0], retweet[1], retweet[2]))


def home_screen(conn, cursor, user):
    
    while True:
        offset_tweets = 0
        offset_retweets = 0

        # print("\nTweets:")
        # print_tweets_home(conn, cursor, user, offset_tweets)

        # print('\nRetweets')
        # print_retweets_home(conn, cursor, user, offset_retweets)

        while True:
            print("\nTweets:")
            print_tweets_home(conn, cursor, user, offset_tweets)

            print('\nRetweets')
            print_retweets_home(conn, cursor, user, offset_retweets)

            user_input = input(user_commands.home_screen_commands)

            if user_input == '1':
                offset_tweets += 5
                # print("\nTweets:")
                # print_tweets_home(conn, cursor, user, offset_tweets)
            elif user_input == '2':
                offset_retweets += 5
                # print('\nRetweets')
                # print_retweets_home(conn, cursor, user, offset_retweets)
            elif user_input == '3':
                search_tweets_actions.tweet_info_interaction(conn, cursor, user)
            elif user_input == '4':
                main_screen(conn, cursor, user)
                offset_tweets = 0
                offset_retweets = 0
            elif user_input == '5':
                return
            else:
                user_input = input("\nInvalid command input! Try again!")
        
