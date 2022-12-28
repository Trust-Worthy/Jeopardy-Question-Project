import csv
import random
import re
from serpapi import GoogleSearch

def num_questions(filename):
    """
    This function counts how many jeopardy questions there are in this file.
    """

    with open(filename, encoding="utf-8") as file:
        questions = file.readlines()
        num = len(questions)
        return num
def get_random_question(filename):

    category_dict = {} # this dict will store the number of each type of question in it along with the name of the category
    question_answer_dict = {}
    with open(filename,encoding="utf-8") as file:

        csv_file = csv.reader(file)

        next(csv_file)

        for line in csv_file:
            category = line[3]
            question = line[5]
            answer = line[6]
            if question not in question_answer_dict:
                question_answer_dict[question] = answer

            if category not in category_dict:
                category_dict[category] = 1
            else:
                category_dict[category] += 1

    question1, value = random.choice(list(question_answer_dict.items()))

    return question1 # this is a question


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

def main():
    question = get_random_question("JEOPardy_CSV.csv")
    print(question)
    # answer = search_answer(question,"41096232330069c7f458ec7fe95a39f301220053fba1af409772c3ceea5d9fa0")
    # print(answer)
    
if __name__ == "__main__":
    main()