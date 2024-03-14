# B14-2 Quarter 2 Code
## Project Description
The main goal of politicians is to cater to their constituents and understand the changes they want to see. To do so, they need to be able to accurately identify their target voters, contact and survey them, understand their values and ideals, and predict which policies would best represent such populations. However, this process can often be time-consuming and expensive. Our project aims to help this problem.

Twitter data contains a wealth of information that contains public opinions on policies and politicians. By analyzing tweets from different political groups, we aim to create personas that mimic key voter groups using LangChain Agents and OpenAI’s GPT-3.5 Turbo API. Our goal is to develop a model that can generate new data to predict real voting patterns based on previously posted tweets. We will then be able to ask these personas different political questions and explore their response and reasoning.

## Data Description
Link to the data: https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets

Our data consists of two separate CSV files. The first dataset contains all of the tweets
from the 2020 election that included the hashtag #biden in it. The second dataset contained all
the tweets that included the hashtag #trump. Neither dataset was exclusively partisan to either
candidate. Rather, they consisted of opinions and sentiments from voters who held various
perspectives on the two candidates, irrespective of their stance. It included any tweet that had the
corresponding hashtag, regardless of whether that hashtag was used to express support or
opposition for the tagged candidate. We cleaned the dataset, removing all of the unnecessary
punctuation, emojis, hashtags, stop words, and also non-english tweets. 

We then wanted to divide the users into 5 clusters total. The first group will consists of users who strongly support Biden. The second group will be for those who weakly support Biden. The third group will be for those who are neutral. The fourth group will be for those who weakly support Trump, and the fifth group will be for those who strongly support Trump. As you will see, a certain threshold was used to determine the division of these clusters. These clusters will be 5 new datasets, all labeled accordingly, in order to better represent the different groups of voters. This datasets are stored in the split_data folder.

## Running The Code
### Downloading the data 
The most important thing to note about our data is that the raw data is too large to be uploaded to Github. To be able to run our code, 
you need to follow the link (https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets), download the two csv files, and store them in the data folder. They should be saved as "hashtag_donaldtrump.csv" and "hashtag_joebiden.csv." Please also go into the "data" folder and click into any and all ".zip" files in the folder. This is important for the code to properly run. 
### API Key
Replace all areas with "INSERT_API_KEY" with your own Open AI API key before running the notebook. You can make an API key here: https://platform.openai.com/api-keys
### Running run.py
To run all the code, type in python run.py data in your command line in your terminal and press enter (Please note it may be "python3" instead depending on what your system has). This will run our entire project on your system, as well as install any packages you need onto your system.

## File Descriptions
### data_cleaning.py
This file takes in the raw data from Kaggle. We cleaned the dataset, removing all of the unnecessary punctuation, emojis, hashtags, and stop words. We then filtered tweets, keeping only the ones that are written in English, have multiple words, and are tweeted by users who have tweeted at least 20 times.

### sentiment_analysis.ipynb
In this file, we calculated the average sentiment of each user’s tweets and classified each user into Biden-supporting voter, Trump-supporting voter, or neutral voter. We then split the Biden-supporting users into Biden Strong and Biden Weak based on a sentiment threshold, and repeated this process for Trump-supporting users as well. This file gives us 5 separate clusters (Biden Strong, Biden Weak, Neutral, Trump Strong, Trump Weak) that we will train our model on.

### final_model.ipynb
Using the clusters created in `sentiment_analysis.ipynb`, we created 5 separate models to replicate the political affiliation, policy related opinions, opinion polarity, and emotional tone relating to common political discourses for each of these clusters. We performed both semantic and contextual training on these tweets and asked each of the models a set of 9 political questions to gain a general understanding of their political opinions.

### sentiment_analysis_viz_creation.ipynb
This file creates visualizations based on the sentiments of the models's responses towards each of the political topics asked.
