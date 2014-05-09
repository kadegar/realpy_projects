#basic twitter app

import tweepy

ADD KEYS here

auth=tweepy.auth.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)

tweets=api.search(q='#draft')

for t in tweets:
	text_for_output=t.text.encode('utf-8','replace')
	print str(t.created_at)+text_for_output+"\n"