library(syuzhet)
library(dplyr)

#load CSV file "sentiment_analysis_twitter.csv"
filename = "sentiment_analysis_twitter4.csv"
outputcsv = "sentiment_analysis_twitter_scores4.csv"

#get text for each row
tweets <- read.csv(file=filename, header=TRUE)

#get the sentiment for each row's text and add column for sentiment
tweets$sentiment <- get_sentiment(tweets$text)

tweets

#add mean to the Sentiment Score column of loaded csv file
write.table(tweets, file=outputcsv, sep=",")
