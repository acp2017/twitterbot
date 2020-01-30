#!/usr/bin/python

from twitterbot.py import getApi
api = getApi()

def postStatus(update):
	status = api.PostUpdate(update)
	print(status)

	postStatus("hi, i'm a twitter bot")
	end
