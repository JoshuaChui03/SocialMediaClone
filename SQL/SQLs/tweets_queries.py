
search_tweets = 'select distinct t1.tid, t1.writer, t1.tdate, t1.text, t1.replyto\
                from tweets as t1\
                left outer join mentions as m1 on t1.tid = m1.tid\
                where 1=0\
                {}\
                order by t1.tdate desc\
                limit 5 offset ?'

aggre_count_retweets = '(select count(rt1.usr)\
                        from retweets as rt1\
                        where rt1.tid = t1.tid)'

aggre_count_replies = '(select count(t2.tid)\
                        from tweets as t2\
                        where t2.replyto = t1.tid)'

retweets_query = "Insert into retweets values (?, ?, ?)"

get_tweet_info = 'select t1.tid, t1.writer, t1.tdate, t1.text, t1.replyto, {} as retweets_count, {} as replies_count\
                from tweets as t1\
                where t1.tid = ?'.format(aggre_count_retweets, aggre_count_replies)

get_retweet = 'select *\
            from retweets\
            where usr = ? and tid = ?'

new_tweet = "insert into tweets values (?, ?, ?, ?, ?);"

tweet_count = "select count(*)\
                from tweets\
                where  writer = (?) "
            
three_recent_tweets = "select text\
                    from tweets\
                    where writer = (?)\
                    order by tdate desc\
                    limit 3 offset ?;"

followee_tweets = "select distinct t1.tid, t1.writer, t1.tdate, t1.text, t1.replyto\
                    from tweets as t1, follows as f1\
                    where t1.writer = f1.flwee and f1.flwer = ?\
                    order by t1.tdate desc\
                    limit 5 offset ?"
                        
followee_retweets = "select distinct r1.usr, r1.tid, r1.rdate\
                        from retweets as r1, follows as f1\
                        where f1.flwer = ? and f1.flwee = r1.usr\
                        order by r1.rdate desc\
                        limit 5 offset ?"

get_single_tweet = "select * from tweets where tid = ?"