import csv
import random
import re
from serpapi import GoogleSearch
import json
import requests
from dotenv import load_dotenv


def num_questions(filename):
    """
    This function counts how many jeopardy questions there are in this file.
    """

    with open(filename, encoding="utf-8") as file:
        questions = file.readlines()
        num = len(questions)
        return num
def get_random_question(filename):
    """
    This function breaks up the contents of the CSV file. This file has almost every Jeopardy
    question from December 2004
    """

    category_dict = {} # this dict will store the number of each type of question in it along with the name of the category
    question_answer_dict = {} # this dict will store every question and every answer to that question
    with open(filename,encoding="utf-8") as file:

        csv_file = csv.reader(file)

        next(csv_file)

        for line in csv_file:
            category = line[3]
            question = line[5]
            answer = line[6]
            if question not in question_answer_dict:
                question_answer_dict[question] = [answer,category]

            if category not in category_dict:
                category_dict[category] = category
            else:
                category_dict[category] = category
        
        with open("categories.txt","w",encoding="utf-8") as outfile:
            for key in category_dict:
                outfile.write(category_dict[key] + "\n")

    question1, answer_category = random.choice(list(question_answer_dict.items()))

    return question1,answer_category # this is a question

def search_answer(qwery,api_key):

    params = {
    "api_key": api_key, # this is my api key
    "engine": "google",
    "q": qwery,
    "location": "United States",
    "google_domain": "google.com",
    "gl": "us",
    "hl": "en"
    }

    search = GoogleSearch(params)
    results = search.get_json()
    return results

def write_jsontofile(json_object):
    num = random.randint(0,777777777)
    filename = "search" + str(num) + ".json" 
    with open(filename,"w") as file:
        json.dump(json_object,file)

def parse_json(filename):
    with open(filename) as file:
        data = json.load(file)

        information = data["search_information"]
        items = information["menu_items"]
        for item in items:
            print(item["link"])
       
    

def main():
    # question = get_random_question("JEOPARDY_CSV.csv")
    # print(question)
    # json_object = search_answer(question[0],"36df43dd74116ecb426552de7a41c51f2f46633809e1a3d04b30ce529f732644")
    # write_jsontofile(json_object)

    parse_json("search370879441.json")


    
    # for key in json_object.keys():
    #     if key == "search_information":
    #         for key in search_information
    #     print(key)
    
    ##

if __name__ == "__main__":
    main()