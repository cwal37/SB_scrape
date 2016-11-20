# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:37:54 2016

@author: Connor
"""

from selenium import webdriver
import pdb
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

#game = []
#answers = []
#clues = []
#categories = []
#game_id = []
#rounds_longform = ['jeopardy_round', 'double_jeopardy_round']#, 'final_jeopardy_round']


driver = webdriver.Chrome()
base_url =' http://shovelbums.org/index.php/2015-02-23-16-25-08/2016-archaeology-cultural-resource-management-and-anthropology-jobs?limit=15&start='

for i in range (15, 75, 15):
    exact_url = base_url + str(i)
    driver.get(exact_url)
    content = driver.find_element_by_class_name('eb-post-body type-email')
    print content
    
    
driver.close()
driver.quit()

    #/html[@class='com_easyblog view-categories layout-listings itemid-568 j36 mm-hover  no-touch']/body/div[@class='t3-wrapper corporate']/div[@id='t3-mainbody']/div[@class='row']/div[@id='t3-content']/div[@id='fd']/div[@class='eb-posts eb-responsive DS030727216335634333 wide w960 w768']/div[@class='eb-post'][1]/div[@class='eb-post-content']/div[@class='eb-post-body type-email']
#total_time = 0
#for g_id in range(1,5163):
#    start = time.clock()
#    game_url = base_url + str(g_id)
#    driver.get(game_url)
#    cat_names = []
#    rounds = ['J', 'DJ']
#    
#    
#    for round_type in rounds:
#        for i in range(1,7):
#            for j in range(1,6):
#                clue_id = 'clue_'+round_type+'_'+str(i)+'_'+str(j)
#                #print clue_id
#                try:
#                    clue = driver.find_element_by_id(clue_id)
#                    clue_value = clue.text
#                    clues.append(clue_value)
#                except NoSuchElementException:
#                    clues.append('MISSING CLUE')
#    #clue_length = 60
#    
#    
#    for jround in rounds_longform:
#        for i in range(1,7):
#            try:
#                cat_name = driver.find_element_by_xpath('//*[@id="'+jround+'"]/table[1]/tbody/tr[1]/td['+str(i)+']/table/tbody/tr[1]/td').text
#                cat_names.append(cat_name)
#            except NoSuchElementException:
#                cat_names.append('NO GAME')
#    
#    for cat in cat_names:
#        for i in range(0,5):
#            categories.append(cat)
#    
#    for i in range(0,60):
#        game_id.append(g_id)
#    
#    # use sdata = str(data) to get a string
#    # then use ans_start = sdata.find('correct_response') to get the start of that string
#    # and ans_end = sdata.find('</em>') to find the end of the answer string
#    # from there you can do ans_str = sdata[ans_start+23:ans_end]
#    # could also iterate through for questions in this manner
#    # just need to finalize the tr/td i/j looping structure and we should be in business
#    
#    
#    for jround in rounds_longform:
#        for i in range(1,7):
#            for j in range(2,7):
#                #current_xpath = '//*[@id="'+jround+'"]/table[1]/tbody/tr['+str(j)+']/td['+str(i)+']/table/tbody/tr[1]/td/div'
#                #print current_xpath
#                try:
#                    data =  driver.find_element_by_xpath('//*[@id="'+jround+'"]/table[1]/tbody/tr['+str(j)+']/td['+str(i)+']/table/tbody/tr[1]/td/div').get_attribute('outerHTML')
#                    #print data
#                    #sdata = str(data)
#                    ans_start = data.find('correct_response')+23
#                    #print sdata
#                    ans_end = data.find('</em>')
#                    ans_uni = data[ans_start:ans_end]
#                    #print ans_uni
#                    #ans_str = str(ans_uni)
#                    answers.append(ans_uni)
#                except NoSuchElementException:
#                    answers.append('MISSING CLUE')
#    end = time.clock()
#    total_time = total_time+(end-start)
#    print(total_time)
#    

#
#clues_series = pd.Series(clues)
#answers_series = pd.Series(answers)
#
#games = pd.DataFrame(clues_series, columns=['Clues'])
#
#games['Answers'] = answers_series
#
#games['G_ID'] = game_id
#games['Category'] = categories
#
#games.to_excel('proof_of_concept2.xlsx')