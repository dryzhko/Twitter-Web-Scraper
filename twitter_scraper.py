import tweepy
from tweepy import OAuthHandler
import sys
import json


 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

user = sys.argv[1]
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)




numtweets = 0 #keeping track of tweets collected



tweets = api.user_timeline(user_id = user, count =200)  #initial api call

for x in range (0,199):  
	tweet_dict = tweets[x]._json  #json attribute of data, as python dict
	tweet_json = json.dumps(tweet_dict, indent = 4)  #convert python dict to json
	numtweets+=1  
	print(tweet_json)
	print(numtweets) #used for debugging, to see how many tweets i'm getting with each call
	with open('%s.json' % user, 'a') as f:  #write to json file, 'a' becuase mutliple api calls returning things, maybe better way?
		json.dump(tweet_json, f, indent = 4)			

try:										#Sometimes returns 199 per page instead of 200, so do 199 and then check for 200
	tweet_dict = tweets[199]._json
	tweet_json = json.dumps(tweet_dict, indent = 4)
	numtweets+=1
	print(tweet_json)
	print(numtweets)
	with open('%s.json' % user, 'a') as f:
		json.dump(tweet_json, f, indent = 4)

except:
	pass
	



max_id = tweets[-1].id - 1   #id of last tweet -1, use with the rest of the api calls

#while len(tweets) > 0:
while numtweets < 3001:  #last call happens at 3000, so we get 3200 
		
	
	#all subsiquent requests use the max_id param to prevent duplicates
	tweets = api.user_timeline(user_id = user,count=200,max_id=max_id)  #remaining calls with max_id

	for x in range (0,199):
		tweet_dict = tweets[x]._json
		tweet_json = json.dumps(tweet_dict, indent = 4)
		numtweets+=1
		print(tweet_json)
		print(numtweets)
		with open('%s.json' % user, 'a') as f:
			json.dump(tweet_json, f, indent = 4)

	try:
		tweet_dict = tweets[199]._json
		tweet_json = json.dumps(tweet_dict, indent = 4)
		numtweets+=1
		print(tweet_json)
		print(numtweets)
		with open('%s.json' % user, 'a') as f:
			json.dump(tweet_json, f, indent = 4)

	except:
		pass
		
		
		
		
	#update the id of the oldest tweet less one
	max_id = tweets[-1].id - 1


		
		
	



