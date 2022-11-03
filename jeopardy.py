import csv
import random


def counter_line(filename):
    counter = 0
    with open(filename,encoding="utf-8") as file:

        csv_file = csv.reader(file)

        next(csv_file)

        for line in csv_file:
            counter += 1
    
    return counter


def get_random_question(filename, category):

    counter = 0 
    quesetion = []
    categories = []
    with open(filename,encoding="utf-8") as file:

        csv_file = csv.reader(file)

        next(csv_file)

        for line in csv_file:
            
            categories.append(line[3])
            # I want to go to every row where the category matches.
            # Then I want to get a random question that matches that category.
            if category == line[3]:
                counter += 1
                quesetion.append(line[5])

    random_question = random.randint(0,counter)
    get_random_question = quesetion[random_question]

            
    
    return category, get_random_question

def main():

    print(get_random_question("JEOPARDY_CSV.csv", "HISTORY"))


if __name__ == "__main__":
    main()