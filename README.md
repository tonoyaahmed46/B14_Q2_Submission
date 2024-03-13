# B14 Quarter 2 Code
## Project Description
The main goal of politicians is to cater to their constituents and understand the changes they want to see. To do so, they need to be able to accurately identify their target voters, contact and survey them, understand their values and ideals, and predict which policies would best represent such populations. However, this process can often be time-consuming and expensive. Our project aims to help this problem. \\

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

TALK ABOUT THE SPLIT DATA

## Running The Code
### Downloading the data 
The most important thing to note about our data is that the raw data is too large to be uploaded to Github. To be able to run our code, 
you need to follow the link (https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets), download the two csv files, and store them in the data folder. They should be saved as "hashtag_donaldtrump.csv" and "hashtag_joebiden.csv." Please also go into the "data" folder and click into any and all ".zip" files in the folder. This is important for the code to properly run. 
### API Key
Replace all areas with "INSERT_API_KEY" with your own Open AI API key before running the notebook. You can make an API key here: https://platform.openai.com/api-keys
