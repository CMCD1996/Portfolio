# Mathematics.py is a script to generate arithmetic problems related problems 
# to practise mental math for consulting interviews.

# Imports useful python packages.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sc
import sklearn as skl
import csv as csv
import openpyxl as pyxl
import pathlib
import os
import pydrive
import random as rd

# Defines the mathematics class
#################################
# Do not touch
#################################
class mathematics:
    # Defines long_multiplication
    def arithmetic_practise(self, questions, answers, max_figures,
                            max_decimals, arithmetic_type):
        """Generates problems to practise arithmetric

        Args:
            questions (dict): Dictionary of mental math questions
            answers (dict): Dictionary of mental math answers
            max_figures (int): Maximum randomly generated number, expressed in multiples of 10 (10,100,1000 etc.)
            max_decimals (int): Maximum number of decimal places (1,2,3 etc.)
            arithmetic_type (str): Type of operation to be applied (addition, subtraction, multiplication or division)

        Returns:
            questions (dict): Updated dictionary of mental math questions
            answers (dict): Updated dictionary of mental math answers 
        """
        # loops through the questions dictionary
        for key in questions:
            # Generates random values to practise
            num_1 = round(rd.random() * max_figures,
                          round(rd.random() * max_decimals))
            print(num_1)
            num_2 = round(rd.random() * max_figures,
                          round(rd.random() * max_decimals))
            # Set questions and answers if multiplication
            if arithmetic_type == 'multiplication':
                #Calculates the answers from the numbers generated
                answers[key] = num_1 * num_2
                # Stores the question in the question string
                questions[key] = str(num_1) + ' x ' + str(num_2)
            # Set questions and answers if division
            elif arithmetic_type == 'division':
                #Calculates the answers from the numbers generated
                answers[key] = num_1 / num_2
                # Stores the question in the question string
                questions[key] = str(num_1) + ' / ' + str(num_2)
            # Set questions and answers if addition
            elif arithmetic_type == 'addition':
                #Calculates the answers from the numbers generated
                answers[key] = num_1 + num_2
                # Stores the question in the question string
                questions[key] = str(num_1) + ' + ' + str(num_2)
            # Set questions and answers if subtraction
            elif arithmetic_type == 'subtraction':
                #Calculates the answers from the numbers generated
                answers[key] = num_1 - num_2
                # Stores the question in the question string
                questions[key] = str(num_1) + ' - ' + str(num_2)
            else:
                # Sets a no operation appplied
                questions[key] = 'No operation applied!'
        # Returns the answers
        return questions, answers

    def quiz(self, questions, answers):
        """Generates a quiz to ask mental math questions

        Args:
            questions (dict): Dictionary of mental math questions
            answers (dict): Dictionary of mental math answers
        """
        # Print welcome message
        print('Answer the following questions in turn')
        # Loop through the question dictionaries.
        for key in questions:
            # Prints the question
            print(questions[key])
            # Sets a tolerance
            tol = 1e-3
            # Ask the intial question
            ans = float(input("Please enter your answer: "))
            while abs(ans - answers[key]) > tol:
                # Ask if would like to try again
                retry = input("Incorrect! Would you like to try again (Type 'Y' or 'N'): ")
                if retry == 'N':
                    print('The answer is ',answers[key])
                    break
                print('Please try again')
                ans = float(input("Please enter your answer: "))
        # Print finishing message
        print('Congratulaions, you finished the quiz')

###########################
# End of Class Definition
###########################

# Initialises an object to use the mathematics class
mental_math = mathematics()

# Initialises the input dictionaries and other variables (User changes these inputs)
questions = {
    1: 'NA',
    2: 'NA',
    3: 'NA',
    4: 'NA',
    5: 'NA',
    6: 'NA',
    7: 'NA',
    8: 'NA',
    9: 'NA',
    10: 'NA',
    11: 'NA',
    12: 'NA',
    13: 'NA',
    14: 'NA',
    15: 'NA',
    16: 'NA',
    17: 'NA',
    18: 'NA',
    19: 'NA',
    20: 'NA',
}
answers = {
    1: 'NA',
    2: 'NA',
    3: 'NA',
    4: 'NA',
    5: 'NA',
    6: 'NA',
    7: 'NA',
    8: 'NA',
    9: 'NA',
    10: 'NA',
    11: 'NA',
    12: 'NA',
    13: 'NA',
    14: 'NA',
    15: 'NA',
    16: 'NA',
    17: 'NA',
    18: 'NA',
    19: 'NA',
    20: 'NA',
}
question_reset = questions
answer_reset = answers
max_fig = 100
max_dec = 3
modes = ['addition','subtraction','multiplication','division']

# Sets active mode
active_mode = modes[1]

#Creates a series of mental math problems to solve
questions, answers = mental_math.arithmetic_practise(
    questions, answers, max_fig, max_dec, active_mode)

# Run the quiz
mental_math.quiz(questions, answers)