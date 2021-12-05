import csv
import tweepy as tw

#store API keys
api_key = "ENTER YOUR API KEY"
api_secret_key = "ENTER YOUR SECRET KEY"
access_token = "ENTER YOUR ACCESS TOKEN"
access_token_secret = "ENTER YOUR TOKEN SECRET"

auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
twitter = tw.API(auth, wait_on_rate_limit=True)

screen_name = "niallofficial"
user = twitter.get_user(screen_name=screen_name)

ID = user.id_str

client = tw.Client(bearer_token="ENTERBERRERTOKEN")

filename = "sentiment_analysis_twitter4.csv"

with open(filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    try:
        for tweet in client.get_users_tweets(id=ID, start_time="2021-01-01T00:00:00Z", end_time="2021-02-01T00:00:00Z", max_results=100, tweet_fields=["created_at", "author_id", "public_metrics"], exclude="retweets,replies").data:
            writer.writerow([tweet.author_id, screen_name, tweet.created_at, f'ID: {str(tweet.id)}', tweet.text, tweet.public_metrics["retweet_count"], tweet.public_metrics["reply_count"], tweet.public_metrics["like_count"]])
    except TypeError as e:
        print(e)
        print("No Tweets in January")

with open(filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    try:
        for tweet in client.get_users_tweets(id=ID, start_time="2021-02-01T00:00:00Z", end_time="2021-03-01T00:00:00Z", max_results=100, tweet_fields=["created_at", "author_id", "public_metrics"], exclude="retweets,replies").data:
            writer.writerow([tweet.author_id, screen_name, tweet.created_at, f'ID: {str(tweet.id)}', tweet.text, tweet.public_metrics["retweet_count"], tweet.public_metrics["reply_count"], tweet.public_metrics["like_count"]])
    except TypeError as e:
        print(e)
        print("No Tweets in February")

with open(filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    try:
        for tweet in client.get_users_tweets(id=ID, start_time="2021-03-01T00:00:00Z", end_time="2021-04-01T00:00:00Z", max_results=100, tweet_fields=["created_at", "author_id", "public_metrics"], exclude="retweets,replies").data:
            writer.writerow([tweet.author_id, screen_name, tweet.created_at, f'ID: {str(tweet.id)}', tweet.text, tweet.public_metrics["retweet_count"], tweet.public_metrics["reply_count"], tweet.public_metrics["like_count"]])
    except TypeError as e:
        print(e)
        print("No Tweets in March")

with open(filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    try:
        for tweet in client.get_users_tweets(id=ID, start_time="2021-04-01T00:00:00Z", end_time="2021-05-01T00:00:00Z", max_results=100, tweet_fields=["created_at", "author_id", "public_metrics"], exclude="retweets,replies").data:
            writer.writerow([tweet.author_id, screen_name, tweet.created_at, f'ID: {str(tweet.id)}', tweet.text, tweet.public_metrics["retweet_count"], tweet.public_metrics["reply_count"], tweet.public_metrics["like_count"]])
    except TypeError as e:
        print(e)
        print("No Tweets in April")

with open(filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    try:
        for tweet in client.get_users_tweets(id=ID, start_time="2021-05-01T00:00:00Z", end_time="2021-06-01T00:00:00Z", max_results=100, tweet_fields=["created_at", "author_id", "public_metrics"], exclude="retweets,replies").data:
            writer.writerow([tweet.author_id, screen_name, tweet.created_at, f'ID: {str(tweet.id)}', tweet.text, tweet.public_metrics["retweet_count"], tweet.public_metrics["reply_count"], tweet.public_metrics["like_count"]])
    except TypeError as e:
        print(e)
        print("No Tweets in May")

with open(filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    try:
        for tweet in client.get_users_tweets(id=ID, start_time="2021-06-01T00:00:00Z", end_time="2021-07-01T00:00:00Z", max_results=100, tweet_fields=["created_at", "author_id", "public_metrics"], exclude="retweets,replies").data:
            writer.writerow([tweet.author_id, screen_name, tweet.created_at, f'ID: {str(tweet.id)}', tweet.text, tweet.public_metrics["retweet_count"], tweet.public_metrics["reply_count"], tweet.public_metrics["like_count"]])
    except TypeError as e:
        print(e)
        print("No Tweets in June")