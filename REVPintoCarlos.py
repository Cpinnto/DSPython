''' Vower Counter Program'''

# Name: Carlos M. Pinto
# Date: 09/19/2025
# Module: 03Rev - Review Python Fundamentals
# Description: This program accepts a text string from the user and counts the number of vowels it contains. 
# It uses loops, conditionals, and dictionaries to store the count for each vowel (A, E, I, O, U). 
# The program is modular, with separate functions for counting the vowels and generating the final report. 
# All input is converted to uppercase to avoid mismatches between lowercase and uppercase characters. 
# The output is displayed in a simple report format that shows the count for each vowel and the total count. 
# This project demonstrates the use of functions, constants, data structures, and clean program design.

TITLE = "Welcome to the Vowel Counter Program 2025, by Carlos Pinto!"
SUBTITLE = 'A program that would let you know how many vowels are in your text.. just for fun!'
PROMPT = "Please, enter any text that you may like"
REPORT_INF = ['VOWEL COUNT REPORT:', 'Vowel', 'Count', 'Total']
LINE = '-'

def main():   # Main function: defines the workflow of the program. Is the best way I can explain what is the purpose of a main function. Guide the path.
    print(TITLE, '\n', SUBTITLE)  # Main function: defines the workflow of the program
    text = input(PROMPT).upper()  #  Ask user for input and convert to uppercase
    vDict, total = findVowelCount(text)  # Ask user for input and convert to uppercase
    generateReport(vDict, total) # Ask user for input and convert to uppercase


def findVowelCount(text): #  Ask user for input and convert to uppercase
    vDict = {'A':0, 'E':0, 'I':0 , 'O':0, 'U':0}
    total = 0
    for chr in text: #  Ask user for input and convert to uppercase
        if chr in vDict: # If character is a vowel, increments its count (value of the key) and total count
            vDict[chr] += 1
            total += 1
    return vDict, total # return dictionary and total
            
def generateReport(vDict, total): # Function that prints the final report in table format
    print(REPORT_INF[0])
    print(LINE * (len(REPORT_INF[0]) + 1 ))
    print(REPORT_INF[1], " " * ((len(REPORT_INF[0]) - (len(REPORT_INF[1] + REPORT_INF[2]))) - 2), REPORT_INF[2])
    print(LINE * (len(REPORT_INF[0]) + 1 ))
    for vowel in vDict:
        print(vowel, " " * (len(REPORT_INF[0]) - 4),  vDict[vowel])
    print(LINE * (len(REPORT_INF[0]) + 1 ))
    print(REPORT_INF[3], " " * (len(REPORT_INF[0]) - 8), total)
    print(LINE * (len(REPORT_INF[0]) + 1 ))
    # It's probably not very Pythonic, but I avoid using features I'm not comfortable with.

main() # Finally, we called the main function and the IPO starts!!