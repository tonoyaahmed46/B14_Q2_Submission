# EDA

## Data Description
The most important thing to note about our data is that the raw data is too large to be uploaded to Github. To be able to run our code, 
you need to follow the link (https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets), download the two csv files, and store them in the data folder. They should be saved as hashtag_donaldtrump.csv and hashtag_joebiden.csv

## Running The Code
### Downloading the data 
The most important thing to note about our data is that the raw data is too large to be uploaded to Github. To be able to run our code, 
you need to follow the link (https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets), download the two csv files, and store them in the data folder. They should be saved as "hashtag_donaldtrump.csv" and "hashtag_joebiden.csv." Please also go into the "data" folder and click into any and all ".zip" files in the folder. This is important for the code to properly run. 
### API Key
Replace all areas with "INSERT_API_KEY" with your own Open AI API key before running the notebook. You can make an API key here: https://platform.openai.com/api-keys

### Opening visualization files
A key part of understanding our project's purpose and analysis includes seeing the plots and graphs in our .ipynb files. Although running
run.py will run all of the .ipynb files, for the graphs to be visible, you must manually open each file. Please take a look at the following 
ipynb files to understand our visualizations: 'exploratory_visualizations.ipynb', 'agent_response_visualizations.ipynb',  'final_bias_visualizations.ipynb'.
### Runtime
Because we are dealing with large amounts of data that are timely to process, it is expected that 'run.py' will take a long time to produce any outputs. Please expect approximately 45 minutes for the code to finish running. Thank you for your patience!

### Running run.py
To run all the code, type in ```python run.py data``` in your command line in your terminal and press enter(Please note it may be "python3" instead depending on what your system has). This will run our entire project on your system, as well as install any packages you need onto your system. 

## File Descriptions
### data_cleaning.py
This file takes in the raw data from Kaggle. We cleaned the dataset, removing all of the unnecessary
punctuation, emojis, hashtags, and stop words. We then filtered tweets, keeping only the ones that have multiple
words, and are tweeted by users who have tweeted at least 20 times. 
### sampling_methods.py
This file contains three methods: sample_user, sample_tweet, sample_tweet_group, and sampling_and_naming. Each of 
these methods sample from the larger dataset to create a small sample size that represents and evenly-distributed portion of 
the larger dataset. This smaller dataset allows us to train our model quicker on data that represents the population 
accurately. 
### exploratory_in_context_learning.py
This file uses in-context learning to prompt the model agent to answer a question when provided with a certain topic. The agent 
will take in the inputted topic, then tell us to what level it agrees with the topic provided, responding with a number ranging from 
1-5, and providing a follow-up explanation of why it chose that number. It uses data it was trained on to provide a rationale for 
its decision. 
### demo.ipynb
This notebook provides a demonstration of how the agents work. It takes in the sampled data, and outputs a few select responses. 
### exploratory_visualizations.ipynb
This notebook has a handful of visualizations that show us the distribution of agreement with certain controversial topics, 
grouped by each political candidate. 
### agent_responses.ipynb
This notebook creates 20 Langchain agents and asks those agents about 10 controversial topics. The agent responds with a number indicating its
level of agreement with the topic and its reasoning. We use these results as the foundation of our analysis.
### agent_response_visualizations.ipynb
This notebook provides visualizations that analyze the results of the previous agent responses. We break the responses down by the distribution
of their level of agreement, by which political candidate they support, how similar their perspectives are to each other, and how frequently they output a certain response. 
### final_bias_visualizations.ipynb
This notebook analyzes some concerning biases that the agents might have. It provides some visualizations that help us break down and understand certain biases, and disprove other biases. Instead of testing all 10 topics for bias as it was too time-consuming, we picked 5 topics to test. We conclude by analyzing why these agents answer questions the way that they do. 
