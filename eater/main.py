#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from bottle import route, run, template, request
import json
import csv
import random




@route('/')
def index():
    categolyNumber = [2, 6, 9, 10, 11, 12, 13, 14, 15, 1607, 1627, 1642]
    recipeUrl = [
            #['月曜日'],
            #['火曜日'],
            #['水曜日'],
            #['木曜日'],
            #['金曜日'],
            #['土曜日'],
            ['日曜日']
    ]
    for i in range(len(recipeUrl)):
        for j in range(3):
            recipeUrl[i].append(str(getRecipeUrl(categolyNumber[random.randrange(0,11)], random.randrange(50), random.randrange(0,9))).replace(r'[','').replace(r']','').replace('\n',''))
        break
    return template('index', recipeList = recipeUrl)

def getRecipeUrl(category, page, order):
    pageUrl = 'http://cookpad.com/category/'+str(category)+'?page='+str(page)
    recipeOrder = '#recipe_' + str(order) + ' h2'
    r = requests.get(pageUrl)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    beautifulRecipe = soup.select(recipeOrder)
    return beautifulRecipe

if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True, reloader=True)