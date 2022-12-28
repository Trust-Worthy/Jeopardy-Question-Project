import csv
import random
import re

def num_questions(filename):
    """
    This function counts how many jeopardy questions there are in this file.
    """

    with open(filename, encoding="utf-8") as file:
        questions = file.readlines()
        num = len(questions)
        return num

def get_random_question(filename, category):

    counter = 0 
    quesetion = []
    category_dict = {} # this dict will store the number of each type of question in it along with the name of the category
    with open(filename,encoding="utf-8") as file:

        csv_file = csv.reader(file)

        next(csv_file)

        for line in csv_file:
            line[3] = category
            if category not in category_dict:
                category_dict[category] = 1
            else:
                category_dict[category] += 1
            
            categories.append(line[3])
            # I want to go to every row where the category matches.
            # Then I want to get a random question that matches that category.
            if category == line[3]:
                counter += 1
                quesetion.append(line[5])

    random_question = random.randint(0,counter)
    get_random_question = quesetion[random_question]

    #lets go
    
    return category, get_random_question

def main():
    print(num_questions("JEOPARDY_CSV.csv"))
    print(get_random_question("JEOPARDY_CSV.csv", "HISTORY"))


if __name__ == "__main__":
    main()