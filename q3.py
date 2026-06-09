#identifying the number of times a word has occured in a file and also printing its respective lines

def lines():
    data = True
    count = 0
    line = 1
    word = input("What's your target word: ")
    with open("f1.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                count+=1
                print(f"The word {word} exists in line {line}")
            line+=1
    if(count != 0):
        print(f"The word {word} occured {count} times in the file")
    else:
        print(f"The word {word} does not exist in the file")


lines()
        
            
            




