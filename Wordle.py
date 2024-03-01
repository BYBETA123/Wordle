import random

def Alpha_Counter(word):
    Alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Counter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    word_list=[]
    result=0
    for char in word:
        word_list.append(char)

    for i in range(len(word_list)):
        for j in range(len(Alphabet)):
            if word_list[i]==Alphabet[j]:
                Counter[j]+=1

    for i in range(26):
        if Counter[i]>1:
            result=1
    return result

def Wordle(number):
    while number >15 or number<0:
        number=int(input("Please input a number between 1 and 15"))
    if number==0:
        f=open("words/allwords.txt", "r")
        line = random.randint(1,65903)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==1:
        f=open("words/onewords.txt", "r")
        line = random.randint(1,26)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==2:
        f=open("words/twowords.txt", "r")
        line=random.randint(1,414)
        word=f.readlines()
        answer=word[line]
        f.close() 
    if number==3:
        f=open("words/threewords.txt", "r")
        line=random.randint(1,1921)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==4:
        f=open("words/fourwords.txt", "r")
        line=random.randint(1,5549)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==5:
        f=open("words/fivewords.txt", "r")
        line=random.randint(1,10173)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==6:
        f=open("words/sixwords.txt", "r")
        line=random.randint(1,13857)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==7:
        f=open("words/sevenwords.txt", "r")
        line=random.randint(1,13661)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==8:
        f=open("words/eightwords.txt", "r")
        line=random.randint(1,10428)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==9:
        f=open("words/ninewords.txt", "r")
        line=random.randint(1,6048)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==10:
        f=open("words/tenwords.txt", "r")
        line=random.randint(1,2626)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==11:
        f=open("words/elevenwords.txt", "r")
        line=random.randint(1,903)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==12:
        f=open("words/twelvewords.txt", "r")
        line=random.randint(1,243)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==13:
        f=open("words/thirteenwords.txt", "r")
        line=random.randint(1,43)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==14:
        f=open("words/fourteenwords.txt", "r")
        line=random.randint(1,10)
        word=f.readlines()
        answer=word[line]
        f.close()
    if number==15:
        answer="dermatoglyphics"
        answer+='\n'
    
    turns_taken=1
    word=answer.rstrip("\n")
    guess=input("Please input your guess ")
    while len(guess) !=number:
        guess=input(f"Please enter a guess that is within {number} letters ")
    correct_word=[]
    for char in word:
        correct_word.append(char)
    while guess != str(word):
        for char in guess:
            print(char, end = "")
            print("", end=" ")
        print("")
        turns_taken+=1
        guess_word=[]
        accuracy=[]
        for i in range(number):
            accuracy.append("O")
        for char in guess:
            guess_word.append(char)

        for i in range(number):
            for j in range(number):
                if str(guess_word[i])==str(correct_word[j]):
                    accuracy[i]="V"
                if str(guess_word[i])==str(correct_word[i]):
                    accuracy[i]="X"
        string=""
        for i in range(len(accuracy)):
            string=string+str(accuracy[i])
        for char in string:
            print(char, end= " ")
        print("")
        guess=input("Please input your next guess ")
        while len(guess) !=number:
            guess=input("Please enter a guess that is within five letters ")
    print(f"Attempts taken: {turns_taken}")

def Wordle_Medium():
    Wordle(5)

def Wordle_Random():
    Wordle(0)

def Wordle_Sort():
    pass
    # count=0
    # f=open("words.txt", "r")
    # file=open("allwords.txt","w")
    # for line in f:
    #         word=line.rstrip("\n")
    #         result=Alpha_Counter(word)
    #         if result==0:
    #             file.write(line)
    #             count+=1
    # print(count)
    # f.close()
    # file.close()

def Wordle_Main():
    print("=========")
    print("1. Easy (4 letters)")
    print("2. Medium (5 letters)")
    print("3. Hard (6 letters)")
    print("4. Random")
    print("5. Sort")
    print("6. Custom")
    print("=========")
    ans=int(input())
    if ans ==1:
        Wordle(4)
    if ans ==2:
        Wordle(5)
    if ans == 3:
        Wordle(6)
    if ans == 4:
        Wordle(0)
    if ans == 5:
        Wordle_Sort()
    if ans == 6:
        number=int(input("Please enter the amount of letters you want to be challenged with"))
        Wordle(number)
    if ans ==9:
        exit()

Wordle_Main()