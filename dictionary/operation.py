#!/usr/local/bin/python
# -*- coding: utf-8 -*-

people = {
    'Alice':{
        'phone':'32414214',
        'address':'fewfewf2341'
    },
    'Beth':{
        'phone':'423432423',
        'address':'fewfwe324'
    },
    'Ceil':{
        'phone':'4643423141',
        'address':'fafsferfr32'
    }
}

labels = {
    'phone' : 'phone number',
    'address' : 'home address'
}

name = raw_input('Name : ')
request = raw_input('Phone number(p) or address(a)?')
if request == 'p' : key = 'phone'
if request == 'a' : key = 'address'

if name in people:
    print "%s's %s is %s" % (name, labels[key], people[name][key])