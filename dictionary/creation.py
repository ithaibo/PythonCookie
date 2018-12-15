#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# 创建phonebook字典，键和值用“:”分开
phonebook = {'Alice':'94546545', 'Beth':'48454546546', 'Ceil':'15462665465'}
print 'phonebook: ' + str(phonebook)

# 通过键值对序列创建字典
items = [('name', 'Gumby'), ('age', 42)]
person_gumby = dict(items)
print 'person_gumby: ' + str(person_gumby)

person_gumby_fake = dict(name = 'Gumby', age = 42)
print 'person_gumby create again: ' + str(person_gumby_fake)
print 'person_gumby == person_gumby_fake? ' + str(person_gumby_fake == person_gumby)