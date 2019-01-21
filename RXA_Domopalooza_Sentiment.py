###############################
## RXA_Domopalooza_Sentiment ##
## Created:           012019 ##
## Author:         JPrantner ##
###############################

# Import the domomagic, nltk, pandas & numpy packages into the script 
from domomagic import *
from nltk import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

# read data from inputs into a data frame
input1 = read_dataframe('Select Columns')

# check the dataframe
input1.info() 

# transform comments to a list
comment_list = input1['Text'].tolist()

# initializes the sentiment engine
sia = SentimentIntensityAnalyzer()

# create an empty polarity_scores list as results
results = []

#append pol_score to the list results
for line in comment_list:
     pol_score = sia.polarity_scores(line)
     pol_score['Text'] = line
     results.append(pol_score)
     
#create new dataframe df pass in with results
df = pd.DataFrame.from_records(results)

#add features: label 1 positive & -1 negative
df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
df.info()

#merge two dataframe together as input1
input1 = pd.merge(input1,df, on='Text', how='outer')
input1.info()

#writes the data back to domo
write_dataframe(input1)


