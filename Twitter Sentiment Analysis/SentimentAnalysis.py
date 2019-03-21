from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100 * float(part)/float(whole)

consumer_key = "eO1LqLd6uCsHKlH41Nvrm8R6N"
consumer_key_secret = "NINjQzHghlLiS3VmAewMLXvBDXTYTTCwok1qA0u5D9FGj1vrhZ"
access_token = "1108727623171997696-xzMRuxWfHTBbGrnj2q5XqlXIm0Vc64"
access_token_secret = "7HefbIqIJ8tP4NOUjYyM52rRZAWk3OuF4UPjXN4gOfAxQ"

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search_term = input('Enter keyword/hashtag to search about: ')
number_of_search_terms = int(input('Enter how many tweets to analyze: '))

tweets = tweepy.Cursor(api.search, q=search_term, lang='en').items(number_of_search_terms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
    	neutral += 1
    elif(analysis.sentiment.polarity < 0.00):
    	negative += 1
    elif(analysis.sentiment.polarity > 0.00):
    	positive += 1


positive = percentage(positive, number_of_search_terms)
negative = percentage(negative, number_of_search_terms)
neutral = percentage(neutral, number_of_search_terms)
polarity = percentage(polarity, number_of_search_terms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print('How people are reacting on '+ search_term + ' by analyzing '+ str(number_of_search_terms)+ ' tweets.')

if(polarity == 0):
	print('Neutral')
elif(polarity < 0):
	print('Negative')
elif(polarity > 0):
	print('Positive')


labels = ['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]', 'Negative ['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches,texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc='best')
plt.title('How people are reacting on '+ search_term + ' by analyzing '+ str(number_of_search_terms)+ ' tweets.')
plt.axis('equal')
plt.tight_layout
plt.show()