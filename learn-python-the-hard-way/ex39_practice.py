# -*- coding: gb2312 -*-
import hashmap

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, '四川', '川')
hashmap.set(states, '浙江', '浙')
hashmap.set(states, '贵州', '黔')
hashmap.set(states, '重庆', '渝')
hashmap.set(states, '云南', '滇')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, '川', '成都')
hashmap.set(cities, '浙', '杭州')
hashmap.set(cities, '黔', '贵阳')

# add some more cities
hashmap.set(cities, '渝', '江北')
hashmap.set(cities, '滇', '丽江')


# print out some cities
print '-' * 10
print "川 有: %s" % hashmap.get(cities, '川')
print "滇 有: %s" % hashmap.get(cities, '滇')

# print some states
print '-' * 10
print "重庆的简称是: %s" % hashmap.get(states, '重庆')
print "浙江的简称是: %s" % hashmap.get(states, '浙江')

# do it by using the state then cities dict
print '-' * 10
print "重庆有: %s" % hashmap.get(cities, hashmap.get(states, '重庆'))
print "浙江有: %s" % hashmap.get(cities, hashmap.get(states, '浙江'))

# print every state abbreviation
print '-' * 10
hashmap.list(states)

# print every city in state
print '-' * 10
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, '海南')

if not state:
  print "Sorry, no 海南."

# default values using ||= with the nil result
# can you do this on one line?
city = hashmap.get(cities, '海', '不存在')
print "属于'海'的城市: %s" % city