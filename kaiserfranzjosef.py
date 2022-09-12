#import worldpan
import random
import time



def printQuestion(frage, antworten):
    print("MEINE FRAGE LAUTET: \n {}\nThe Answer IS: {} ".format(frage, antworten) )

def chooseName(antworten):
    index = random.randint(0, 3)
    name = antworten[index]
    return name



frage = "Wie heisst du denn mein sohn?"
antworten = ["Kaiser Franz Josef", "FUCK", "Berndt", "PUTIN"]

# Hello Mister CodeBloom
for i in range(0,10):
    time.sleep(3)
    printQuestion(frage, chooseName(antworten))



