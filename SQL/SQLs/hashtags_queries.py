hashtags_query = "select *\
                  from hashtags\
                  where term = ?;"

write_hashtag = "insert into hashtags (term) values (?);"