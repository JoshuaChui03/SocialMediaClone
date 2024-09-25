from datetime import datetime
import Interfaces.user_commands as user_commands
import Controllers.search_users_actions as search_users_actions
import SQLs.tweets_queries as tweets_queries
import SQLs.users_queries as users_queries
import SQLs.follows_queries as follows_queries


def list_followers(conn, cursor, user):

    cursor.execute(follows_queries.get_followers, (user.get_usr(), ))
    followers = cursor.fetchall()
    print(followers)

    if not followers:
        print("You have no followers.")
        return
    
    while (True):

        follower_id = input("Select the ID of the follower (id name) or type 'exit' to go back: ")

        if follower_id == 'exit':
            break

        while True:
            try:
                int(follower_id)
                break
            except:
                follower_id = input("Invalid ID input, try again: ")

        cursor.execute(users_queries.single_user_query, (int(follower_id), ))
        follower = cursor.fetchone()

        if follower == None:
            print("No user with the ID given! Try again!")
            break
      
        cursor.execute(tweets_queries.tweet_count, (follower_id, ))
        print(f"Number of tweets by ({follower[2]}): {cursor.fetchall()[0][0]}\n")

        cursor.execute(follows_queries.follower_count, (follower_id, ))
        print(f"Number of followers of ({follower[2]}): {cursor.fetchall()[0][0]}\n")

        cursor.execute(follows_queries.follwee_count, (follower_id, ))
        print(f"Number of users that ({follower[2]}) follow: {cursor.fetchall()[0][0]}\n")

        offset = 0
        cursor.execute(tweets_queries.three_recent_tweets, (follower_id, offset))
        print(f"{follower[2]}'s three most recent tweets: {cursor.fetchall()}\n")


        while True:
            option = input(user_commands.follow_or_tweets)

            if option == '1':
                search_users_actions.follow_user(conn, cursor, user, follower_id)
            elif option == '2':
                offset += 3
                cursor.execute(tweets_queries.three_recent_tweets, (follower_id, offset))
                print(cursor.fetchall())
            elif option == '3':
                break
            else:
                print("Invalid command! Try again!")