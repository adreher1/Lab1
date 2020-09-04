'''
Rose Williams
rosew@binghamton.edu
Section #B1
Assignment #1
Ava Dreher
'''

'''
ANALYSIS

RESTATEMENT:
  Ask a user how many people are in a room and output the total number of
  introductions if each person introduces themselves to every other person 
  once

OUTPUT to monitor:
  introductions (int) - when each person introduces themselves to every other
  person once
INPUT from keyboard:
  person_count (int)

GIVEN: 
  HALF (int) - 2

FORMULA:
  (person_count * (person_count - 1)) / HALF
'''

# CONSTANTS

HALF = 2 


# This program outputs the total number of introductions possible if each
# person in a room introduces themselves to every other person in the room 
# once, given the number of people in the room

def main():
  # Explain purpose of program to user
  print("How many introductions will occur if everyone " + "\n" + "introduces themseves to every other person?")
  
  
  # Ask user for number of people in room
  num_people = input('number of people in room:')

      

  # Convert str data to int
  num_people = int(num_people)
  


  # Use the formula to compute the result
  num_intro = (num_people * (num_people - 1)) / HALF
  num_intro = str(num_intro)

  
  
 

  # Display labeled and formatted introduction count
  print('There are '+ num_intro + ' introductions')
  
if __name__ == '__main__':
  main()

