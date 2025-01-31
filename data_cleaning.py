import regex as re
import pandas as pd 
import langid

def clean_tweets(tweet, link=True, mention=True, hashtag=True):
    
    re_pattern = []
    if link:
        re_pattern.append('http\S+')
    if mention:
        re_pattern.append('@')
    if hashtag:
        re_pattern.append('#')
    re_pattern = "|".join(re_pattern)

    tweet = str(tweet)
    tweet = re.sub(re_pattern, ' ', tweet)
    return tweet.strip()

def filter_tweets(df, min_tweet_count=20, min_word_count=0):
    
    #select variables
    out = df[["tweet","user_id"]]
    out = out.dropna(subset=['user_id'])

    #remove URLS, mentions, hashtags
    out['tweet'] = out['tweet'].astype(str)
    out["cleaned_tweets"] = out["tweet"].apply(clean_tweets)

    #drop duplicate tweets
    out = out.drop_duplicates(subset=['user_id', 'cleaned_tweets'])

    #minimum word count
    out = out[out['cleaned_tweets'].str.split().str.len() >= min_word_count]

    #minimum tweet count
    user_count = out['user_id'].value_counts()
    valid_users = user_count[user_count >= min_tweet_count].index
    out = out[out['user_id'].isin(valid_users)]

    return out[['user_id', 'cleaned_tweets']]

def filter_english_entries(df, text_column):
    # Add a new column to the DataFrame to store language information
    df['language'] = df[text_column].apply(lambda x: langid.classify(x)[0])
    
    # Filter out entries where the detected language is not English
    english_entries = df[df['language'] == 'en'].copy()
    
    # Drop the temporary 'language' column
    english_entries.drop('language', axis=1, inplace=True)
    
    return english_entries


print("data_cleaning.py finished running")
