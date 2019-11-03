# Programming Exercise 10-8
# Added another comment

import question

def main():
    # Local variables
    first_points = 0
    second_points = 0
    player = ''
    
    # Create question list.
    questions = get_questions()

    for i in range(10):

        if i % 2 == 0:
            player = 'first'
        else:
            player = 'second'
        print('Question for the', player, 'player:')

        current = questions[i]
        print(current)
        user_answer = int(input('Enter your solution (a number' + \
                                            ' between 1 and 4): '))
        if current.isCorrect(user_answer):
            if player == 'first':
                first_points += 1
            else:
                second_points += 1
            print('That is the correct answer.')
            print()
        else:
            print('That is incorrect. The correct answer is',\
                  current.get_solution())
            print()

    print('The first player earned', first_points, 'points.')
    print('The second player earned', second_points, 'points.')
    if first_points == second_points:
        print('It is a tie.')
    elif first_points > second_points:
        print('The first player wins the game.')
    else:
        print('The second player wins the game.')
    
def get_questions():

    questions = []

    # Create questions and add to list.
    question1 = question.Question('How many days are in a ' + \
                                  'lunar year?', '354', '365', \
                                  '243', '379', 1)
    questions.append(question1)
    question2 = question.Question('What is the largest planet?', \
                                  'Mars', 'Jupiter', 'Earth', \
                                  'Pluto', 2)
    questions.append(question2)
    question3 = question.Question('What is the largest kind of ' + \
                                  'whale?', 'Orca whale', \
                                  'Humpback whale', \
                                  'Beluga whale', 'Blue whale', 4)
    questions.append(question3)
    question4 = question.Question('Which dinosaur could fly?', \
                                  'Triceratops', 'Tyranosaurus Rex', \
                                  'Pteranodon', 'Diplodocus', 3)
    questions.append(question4)
    question5 = question.Question('Which of these Winnie the Pooh ' + \
                                  'characters is a donkey?', \
                                  'Pooh', 'Eeyore', 'Piglet', \
                                  'Kanga', 2)
    questions.append(question5)
    question6 = question.Question('What is the hottest planet?', \
                                  'Mars', 'Pluto', 'Earth', \
                                  'Venus', 4)
    questions.append(question6)
    question7 = question.Question('Which dinosaur had the ' + \
                                  'largest brain compared to body' + \
                                  ' size?', 'Troodon', 'Stegosaurus', \
                                  'Ichthyosaurus', 'Gigantoraptor', 1)
    questions.append(question7)
    question8 = question.Question('What is the largest type ' + \
                                  'of penguins?', \
                                  'Chinstrap penguins', \
                                  'Macaroni penguins', \
                                  'Emperor penguins', \
                                  'White-flippered penguins', 3)
    questions.append(question8)
    question9 = question.Question("Which children's story " + \
                                  'character is a monkey?', \
                                  'Winnie the Pooh', \
                                  'Curious George', 'Horton', \
                                  'Goofy', 2)
    questions.append(question9)
    question10 = question.Question('How long is a year on Mars?', \
                                   '550 Earth days', \
                                   '498 Earth days', \
                                   '126 Earth days', \
                                   '687 Earth days', 4)
    questions.append(question10)

    return questions

# Call the main function.
main()

