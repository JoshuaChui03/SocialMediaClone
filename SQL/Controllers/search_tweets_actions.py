import Interfaces.tweets as tweets_interfaces
import SQLs.tweets_queries as tweet_queries
from Models.Users import *
from datetime import datetime
from Controllers.compose_tweets import *

def print_tweets(conn, cursor, offset, conditions):
    conditions = ' or 1=1' if (conditions == '') else conditions

    cursor.execute(tweet_queries.search_tweets.format(conditions), (offset, ))
    current_tweets_list = cursor.fetchall()
    for tweet in current_tweets_list:
        print('ID: ' + str(tweet[0]) + ' - ' + tweet[3])

def retweet_tweet(conn, cursor, usr, tid):
    cursor.execute(tweet_queries.get_retweet, (usr, tid))
    existing_retweet = cursor.fetchone()
    
    if existing_retweet != None:
        print("\nYou already retweeted this tweet!\n")
        return

    cursor.execute(tweet_queries.retweets_query, (usr, tid, datetime.now().strftime('%Y-%m-%d')))
    conn.commit()
    print("\nYou retweeted tweet " + str(tid) + ".")

def tweet_info_interaction(conn, cursor, user):
    tweet_id = input("\nEnter the tweet ID: ")

    while True:
        try:
            int(tweet_id)
            break
        except:
            tweet_id = input("\nInvalid ID format! Try again!\n")

    cursor.execute(tweet_queries.get_tweet_info, (tweet_id, ))
    current_tweet_info = cursor.fetchone()
    
    if current_tweet_info == None:
        print("\nNo tweets with ID given!\n")
        return
    else: 
        print('ID: {}, Writer: {}, Date: {}, Text: {}, Reply To: {}, Retweets count: {}, Replies count: {}'.format(\
            current_tweet_info[0],
            current_tweet_info[1],
            current_tweet_info[2],
            current_tweet_info[3],
            current_tweet_info[4],
            current_tweet_info[5],
            current_tweet_info[6],
            ))
    
    while True:
        tweet_interact_command = input(tweets_interfaces.tweets_interaction)

        if tweet_interact_command == '1':
            retweet_tweet(conn, cursor, user.get_usr(), current_tweet_info[0])
        elif tweet_interact_command == '2':
            compose_tweet(conn, cursor, user, int(current_tweet_info[0]))
        elif tweet_interact_command ==  '3':
            break
        else:
            print("\nUnrecognizable command! Try again!\n")
                    

def search_tweets(user, conn, cursor):
    exit_search = False

    while True:

        if exit_search:
            break

        offset = 0
        keywords_input = input(tweets_interfaces.search_tweets_input)
        keywords = list(keywords_input.split(' '))
        conditions = ''

        for keyword in keywords:
            if keyword == '':
                continue
            elif keyword[0] == '#':
                conditions += ' or m1.term = \'{}\' collate nocase'.format(keyword[1::])
            else:
                conditions += ' or t1.text like \'%{}%\' collate nocase'.format(keyword)
        
        print_tweets(conn, cursor, offset, conditions)

        while True:
            command_next = input(tweets_interfaces.search_tweets_next)

            if command_next == '1':
                offset += 5
                print_tweets(conn, cursor, offset, conditions)
            elif command_next == '2':
                tweet_info_interaction(conn, cursor, user)
            elif command_next == '3':
                break
            elif command_next == '4':
                exit_search = True
                break
            else:
                print("\nUnrecognizable command! Try again!\n")

        

