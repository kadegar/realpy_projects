#basic twitter app

import tweepy

consumer_key="8a2rIIiaLPAGnLRf4xtaH5aU6"
consumer_secret="R3mtkW1ZvMegzAEe2G2vmw1x6VhsgmahCiEIbqyoIHVW1oUC9S"
access_token="379119787-BJXtkn7NmWjTZQRVVwooilOsNW7d1zEjPiMnPATK"
access_secret="zHyN1ptiXmgtjf9btFk2tPCKDwoqie6svXyAsiaKGG98J"

auth=tweepy.auth.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)

tweets=api.search(q='#draft')

for t in tweets:
	text_for_output=t.text.encode('utf-8','replace')
	print str(t.created_at)+text_for_output+"\n"