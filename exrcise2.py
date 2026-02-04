import random

def survey():
    print(" Hello whats up? ")

    responce = input("Enter your responce: ")

    question = ['What is your name?',
                'What is your favorite color?',
                'What is your favorite food?',
                'What is your hobby?',
                'What is your dream job?',
                'What is your favorite movie?',
                'What is your favorite book?',
                'what is your favorite country'
                'What is your favorite sport?',
                'What is your favorite travel destination?']
    print(random.choice(question))


    responce_2 = input("Enter your responce: ")

    if responce and responce_2 == '' or None: 
        return "Please answer the question"
    else:
        return f"Your favorite color is {responce_2}"


print(survey())