# coding: utf-8
from twitter import Twitter, OAuth

t = Twitter(auth=OAuth(
        '850237748791263232-90do1f0FfaYw1wUPQ5hBH4JUvdHDP5J',
        'DvGsK8pLlwCTSSQdEuaUhDTHLFdxW9oid1cffTV3ZsC5Q',
        'kE2Is95errL2sgBnatcQqZtMM',
        'tEqyLHRjHDWALJYBpjNxf6J1ENIZhENFj50mrB5eVJFHrS1UcV'
    ))
# 获得消息
# pythonTweets = t.search.tweets(q="#python")
# 发送消息
statusUpdate = t.statuses.update(status='Hello, world! from Twitter\'s API')
print(statusUpdate)

