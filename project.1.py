# fn=input(("enter your first name :"))
# mn=input(("enter your middle name :"))
# ln=input(("enter your last name :"))
age=int(input("enter age :"))
# roll_num=input(("enter roll_number :"))
# mb=input(("enter mobile number :"))
# reg_num=input(("enter registration number :"))
# c=1
# attempt=1
if age>=18:
    print("user valid ")
    password=input("enter paassword ")
    cpass=input("confirm password ")
    if password == cpass:
        print("password match ")
        print("7 terms and conditions")
        print("----------7 terms and conditions------------")
        print("1.quiz contains 7 questions.")
        print("2.each correct answer carries 1 mark.") 
        print("3.no negative marking.")
        print("4.only one option can be selected.")
        print("5.answers cannot be changed later.")
        print("6.read each question carefully.")
        print("7.final score will be shown at the end.")
        choice=input("enter users choice either yes or no ")
        if choice=='yes':
            print(" agree to terms and conditions of quiz !")
        elif choice=='no':
            print("does not agree to terms and conditions of quiz !")
 
 
        print("---------Quiz Start-------")
        score=0
        print("que1:-what is the full form of ram?")
        print("A.read only memory")
        print("B.ramdom access memory")
        print("C.read access memory")
        print("D.ramdom memory only")
            
        chance=3
        while chance>0:
            ans=input("enter answer :")
            if ans=='b': 
                print("correct answer")
                score+=1
                break
            else:
                chance-=1
                if chance>0:
                    print("wrong answer !")
                    print("remaining chances:",chance)
                else:
                    print("no chances left :")
                    print("correct answer is :-> ramdom access memory")
                        
                
                
        print("que2:-how many decision making statements are there?")
        print("A.one")
        print('B.two')
        print("C.three")
        print("D.four")
            
        chance=3
        while chance>0:
            ans=input("enter answer :")
            if ans=='d':
                print("correct answer")
                score+=1  
                break
        
            else:
               chance-=1
            if chance>0:
                print("wrong answer !")
                print("remaining chances:",chance)
            else:
                print("no chances left :")
                print("correct answer is :-> four")
            
        print("que3:-how many looping statements are there?")
        print("A.one")
        print("B.two")
        print("C.three")
        print("D.four")
            
        chance=3
        while chance>0:
            ans=input("enter answer :")
            if ans=='b': 
                print("correct answer")
                score+=1
                break
            else:
                chance-=1
                if chance>0:
                    print("wrong answer !")
                    print("remaining chances:",chance)
                else:
                    print("no chances left :")
                    print("correct answer is :-> two")
            
        print("que4:-which data types stores whole number?")
        print("A.int")
        print("B.float")
        print("C.str")
        print("D.bool")
            
        chance=3
        while chance>0:
            ans=input("enter answer :")
            if ans=='a': 
                print("correct answer")
                score+=1
                break
            else:
                chance-=1
                if chance>0:
                    print("wrong answer !")
                    print("remaining chances:",chance)
                else:
                    print("no chances left :")
                    print("correct answer is :-> int")
                    
        print("que5:-which data type is used for characters?")
        print("A.int")
        print("B.float")
        print("C.str")
        print("D.bool")
            
        chance=3
        while chance>0:
            ans=input("enter answer :")
            if ans=='c': 
                print("correct answer")
                score+=1
                break
            else:
                chance-=1
                if chance>0:
                    print("wrong answer !")
                    print("remaining chances:",chance)
                else:
                    print("no chances left :")
                    print("correct answer is :-> str")
                    
        print("que6:-which data type is used for true/false statement?")
        print("A.int")
        print("B.str")
        print("C.bool")
        print("D.float")
            
        chance=3
        while chance>0:
            ans=input("enter answer :")
            if ans=='c': 
                print("correct answer")
                score+=1
                break
            else:
                chance-=1
                if chance>0:
                    print("wrong answer !")
                    print("remaining chances:",chance)
                else:
                    print("no chances left :")
                    print("correct answer is :-> bool")
                    
        print("que7:-python is which language?")
        print("A.most difficult")
        print("B.easy language")
        print("C.flexible language")
        print("D.both a and b")
            
        chance=3
        while chance>0:
            ans=input("enter answer :")
            if ans=='d': 
                print("correct answer")
                score+=1
                break
            else:
                chance-=1
                if chance>0:
                    print("wrong answer !")
                    print("remaining chances:",chance)
                else:
                    print("no chances left :")
                    print("correct answer is :-> both a and b")
                    
        print("---------------Result---------")
        print("Score:",score,"/7")
            
        if score>=6:
            grade="Outstanding"
        elif score>=5:
             grade="Very Good"
        elif score>=4:
            grade="Good"
        else:
            grade="Participation"
                
        print("Grade",grade)
        print("---------------CERTIFICATE--------")
        print("Total Questions:7")
        print("Correct Answers:",score)
        print("Grade:",grade)                                
                
else: 
    print("password does not match ! 3 chances")    
    attempt=0
    print("enter your password again ! ")
        
    for i in range(1, 3):
        password=input("enter paassword")
        cpass=input("confirm password")
        if password ==cpass:
            print(" match")
            break
        else:
            print(" password does not match! attempt failed")
                       
                       

    
        
            
            
            
                    
                    
                
        
            
        
    
    
    
    
    