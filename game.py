# user1=input("Enter the name of 1st contestant: ")
# user2=input("Enter the name of 2nd contestant: ")
# print("1. Rock\n2. Paper\n3. Scissor\n")
# print(user1,", enter your choice as 1,2,3:")
# choice1=int(input())
# if(choice1==1):
#   print(user2,", enter your choice as 2,3:")
# elif(choice1==2):
#   print(user2,", enter your choice as 1,3:")
# else:
#   print(user2,", enter your choice as 1,2:")

















# choice2=int(input())
# if((choice1==1 and choice2==1) or (choice1==2 and choice2==2) or (choice1==3 and choice2==3)):
#     print("Game Tie, Try again!!")
# elif((choice1==1 and choice2==3) or (choice1==2 and choice2==1) or (choice1==3 and choice2==2)):
#     print("Congratulations, ",user1," Won!!\nYou are at the HOTSEAT now!! ")
# else:
#     print("Congratulations, ",user2," Won!!\nYou are at the HOTSEAT now!!")
# print("Now let the game begin!!!")
# money=1000
# print("Moving to the first question..\nYour first question is:\nWhat is the capital of France?\nA. Berlin               B. Madrid\nC. Paris               D. Rome")
# answer1=input("Choose your answer: ")
# if(answer1=="C"):
#     print("Correct!!, You reached the 2nd level")
#     money=money*5
#     print("Moving to the second question..\nYour second question is:\nWhich planet is known as Red Planet?\nA. Venus               B. Mars\nC. Jupiter               D. Saturn")
#     answer2=input("Choose your answer: ")
#     if(answer2=="B"):
#          print("Correct!!, You reached the 3rd level")
#          money=money*5
#          print("Moving to the third question..\nYour third question is:\nWho wrote the play Romeo And Juliet?\nA. Charles Dickens               B. William Shakespeare\nC. Mark Twain               D. leo Tolstoy")
#          answer3=input("Choose your answer: ")
#          if(answer3=="B"):
#               print("Correct!!, You reached the 4th level")
#               money=money*5
#               print("Moving to the fourth question..\nYour fourth question is:\nWhich gas do plants absorb from atmosphere during photo synthesis?\nA. Oxygen               B. Helium\nC. Carbon Dioxide               D. Nitrogen")
#               answer4=input("Choose your answer: ")
#               if(answer4=="C"):
#                     print("Correct!!, You reached the 5th level")
#                     money=money*5
#                     print("Moving to the fifth question..\nYour fifth question is:\nWhat is the largest mammal on the earth?\nA. African Element               B. Great White Shark\nC. Giraffe               D. Blue Whale")
#                     answer5=input("Choose your answer: ")
#                     if(answer5=="D"):
#                             print("Correct!!, You reached the 6th level")
#                             money=money*5
#                             print("Moving to the sixth question..\nYour sixth question is:\nIn which year did the Titanic sink?\nA. 1905               B. 1912\nC. 1920               D. 1935")
#                             answer6=input("Choose your answer: ")
#                             if(answer6=="B"):
#                                 print("Correct!!, You reached the 7th level")
#                                 money=money*5
#                                 print("Moving to the seventh question..\nYour seventh question is:\nWhich element has the chemical symbol O?\nA. Oxygen               B. Hydrogen\nC. Gold               D. Iron")
#                                 answer7=input("Choose your answer: ")
#                                 if(answer7=="A"):
#                                         print("Correct!!, You reached the 8th level")
#                                         money=money*5
#                                         print("Moving to the eighth question..\nYour eighth question is:\nWhich is the smallest prime number?\nA. 0               B. 1\nC. 2              D. 3")
#                                         answer8=input("Choose your answer: ")
#                                         if(answer8=="C"):
#                                             print("Correct!!, You reached the 9th level")
#                                             money=money*5
#                                             print("Moving to the ninth question..\nYour ninth question is:\nWhich ocean is largest by surface area?\nA. Atlantic Ocean               B. Indian Ocean\nC. Pacific Ocean               D. Arctic Ocean")
#                                             answer9=input("Choose your answer: ")
#                                             if(answer9=="C"):
#                                                 print("Correct!!, You reached the 10th level")
#                                                 money=money*5
#                                                 print("Moving to the tenth question..\nYour tenth question is:\nWhat is the currency of Japan?\nA. Dollar               B. Yuro\nC. Yen              D. Peso")
#                                                 answer10=input("Choose your answer: ")
#                                                 if(answer10=="C"):
#                                                     money=money*5
#                                                     print("Correct!!, You won ",money, "rupees")

                                              
#     else:          
#         print("Incorrect!!, Sorry you won ",money, "rupees")     
        
# else:
#     print("Incorrect!!, Sorry you won nothing")
user1=input("Enter the name of 1st contestant: ")
user2=input("Enter the name of 2nd contestant: ")
print("1. Rock\n2. Paper\n3. Scissor\n")
print(user1,", enter your choice as 1,2,3:")
choice1=int(input())
if(choice1==1):
  print(user2,", enter your choice as 2,3:")
elif(choice1==2):
  print(user2,", enter your choice as 1,3:")
else:
  print(user2,", enter your choice as 1,2:")
choice2=int(input())
if((choice1==1 and choice2==1) or (choice1==2 and choice2==2) or (choice1==3 and choice2==3)):
    print("Game Tie, Try again!!")
elif((choice1==1 and choice2==3) or (choice1==2 and choice2==1) or (choice1==3 and choice2==2)):
    print("Congratulations, ",user1," Won!!\nYou are at the HOTSEAT now!! ")
else:
    print("Congratulations, ",user2," Won!!\nYou are at the HOTSEAT now!!")
print("Now let the game begin!!!")
money=0
print("Moving to the first question..\nYour first question is:\nWhat is the capital of France?\nA. Berlin               B. Madrid\nC. Paris               D. Rome")
answer1=input("Choose your answer: ")
if(answer1=="C"):
    print("Correct!!, You reached the 2nd level")
    money=1000
    print("Moving to the second question..\nYour second question is:\nWhich planet is known as Red Planet?\nA. Venus               B. Mars\nC. Jupiter               D. Saturn")
    answer2=input("Choose your answer: ")
    if(answer2=="B"):
         print("Correct!!, You reached the 3rd level")
         money=money*5
         print("Moving to the third question..\nYour third question is:\nWho wrote the play Romeo And Juliet?\nA. Charles Dickens               B. William Shakespeare\nC. Mark Twain               D. leo Tolstoy")
         answer3=input("Choose your answer: ")
         if(answer3=="B"):
              print("Correct!!, You reached the 4th level")
              money=money*5
              print("Moving to the fourth question..\nYour fourth question is:\nWhich gas do plants absorb from atmosphere during photo synthesis?\nA. Oxygen               B. Helium\nC. Carbon Dioxide               D. Nitrogen")
              answer4=input("Choose your answer: ")
              if(answer4=="C"):
                    print("Correct!!, You reached the 5th level")
                    money=money*5
                    print("Moving to the fifth question..\nYour fifth question is:\nWhat is the largest mammal on the earth?\nA. African Element               B. Great White Shark\nC. Giraffe               D. Blue Whale")
                    answer5=input("Choose your answer: ")
                    if(answer5=="D"):
                            print("Correct!!, You reached the 6th level")
                            money=money*5
                            print("Moving to the sixth question..\nYour sixth question is:\nIn which year did the Titanic sink?\nA. 1905               B. 1912\nC. 1920               D. 1935")
                            answer6=input("Choose your answer: ")
                            if(answer6=="B"):
                                print("Correct!!, You reached the 7th level")
                                money=money*5
                                print("Moving to the seventh question..\nYour seventh question is:\nWhich element has the chemical symbol O?\nA. Oxygen               B. Hydrogen\nC. Gold               D. Iron")
                                answer7=input("Choose your answer: ")
                                if(answer7=="A"):
                                        print("Correct!!, You reached the 8th level")
                                        money=money*5
                                        print("Moving to the eighth question..\nYour eighth question is:\nWhich is the smallest prime number?\nA. 0               B. 1\nC. 2              D. 3")
                                        answer8=input("Choose your answer: ")
                                        if(answer8=="C"):
                                            print("Correct!!, You reached the 9th level")
                                            money=money*5
                                            print("Moving to the ninth question..\nYour ninth question is:\nWhich ocean is largest by surface area?\nA. Atlantic Ocean               B. Indian Ocean\nC. Pacific Ocean               D. Arctic Ocean")
                                            answer9=input("Choose your answer: ")
                                            if(answer9=="C"):
                                                print("Correct!!, You reached the 10th level")
                                                money=money*5
                                                print("Moving to the tenth question..\nYour tenth question is:\nWhat is the currency of Japan?\nA. Dollar               B. Yuro\nC. Yen              D. Peso")
                                                answer10=input("Choose your answer: ")
                                                if(answer10=="C"):
                                                    money=money*5
                                                    print("Correct!!, You won ",money, "rupees")
                                                else:          
                                                    print("Incorrect!!, Sorry you won ",money, "rupees")
                                            else:          
                                                    print("Incorrect!!, Sorry you won ",money, "rupees")
                                        else:
                                                print("Incorrect!!, Sorry you won",money,"rupees.")
                                else:
                                              print("Incorrect!!, Sorry you won",money,"rupees.")
                            else:
                                    print("Incorrect!!, Sorry you won",money,"rupees.")
                    else:
                                print("Incorrect!!, Sorry you won",money,"rupees.")
              else:
                        print("Incorrect!!, Sorry you won",money,"rupees.")
         else:
                    print("Incorrect!!, Sorry you won",money,"rupees.")
                    
        
    else:
     print("Incorrect!!, Sorry you won",money,"rupees.")
else:
    print("Incorrect!!, Sorry you won",money,"rupees.")