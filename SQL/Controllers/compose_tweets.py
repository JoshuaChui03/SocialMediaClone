from datetime import datetime
import Interfaces.tweets as tweet_commands
import SQLs.tweets_queries as tweets_queries
import SQLs.hashtags_queries as hashtag_queries
import SQLs.mentions_queries as mentions_queries


def id_generate(cursor) -> int:
    tweet_id = 1

    while True:
        cursor.execute(tweets_queries.get_single_tweet, (tweet_id, ))
        result = cursor.fetchone()
        
        if result is None:
            return tweet_id
        else:
            tweet_id += 1
    

def hashtags_creation(conn, cursor, text):
    
    hashtags_in_text = []

    if '#' in text:
        text_split = text.split()
        for word in text_split:
            if word[0] == '#':
                hashtags_in_text.append(word[1:])

    # existing_hastags = {row[0].lower() for row in cursor.fetchall()}

    for hashtag in hashtags_in_text:
        cursor.execute(hashtag_queries.hashtags_query, (hashtag.lower(), ))
        current_row = cursor.fetchone()

        if current_row is not None:
            continue
        else:
            cursor.execute(hashtag_queries.write_hashtag, (hashtag.lower(),))
            conn.commit()
            
    return hashtags_in_text


def create_mentions(conn, cursor, tid, text, hashtags_in_text):
    for hashtag in hashtags_in_text:
        cursor.execute(mentions_queries.insert_into_mentions, (tid, hashtag.lower()))
        conn.commit()


def compose_tweet(conn, cursor, user, reply_id = None):
    text = input(tweet_commands.write_tweet)

    if text == '':
        print("\nTweet text cannot be empty!")
        return

    hashtags_in_text = hashtags_creation(conn, cursor, text)

    tid = int(id_generate(cursor))
    
    cursor.execute(tweets_queries.new_tweet, (tid, user.get_usr(), datetime.now().date().strftime("%Y-%m-%d"), text, reply_id))
    conn.commit()

    create_mentions(conn, cursor, tid, text, hashtags_in_text)

    print("Your new tweet ID is " + str(tid))