# @ Rupam Das, 30.07.2017
import time
import threading

class Tester:
    def __init__(self, paragraph):
        self.correctWords = []
        self.incorrectWords = {}
        self.typedWords = []
        self.totalWords = []
        self.input = None
        self.paragraph = paragraph
        self.accuracy = 0
        self.time = 0
        self.wordPermin = 0
        self.run()

    def clock(self):
        while len(self.typedWords) == 0:
            self.time += 1
            time.sleep(1)

    def run(self):
        threading.Thread(target=self.clock).start()
        threading.Thread(target=self.testSpeed).start()

    def testSpeed(self):
        print('\n\n'+self.paragraph+'\n\n')
        self.input = str(input('\t\n'+'Type The Word Which You Want To Know the Speed As well as Incorrect \n\n'))
        self.totalWords = self.paragraph.split(' ')
        self.typedWords = self.input.split(' ') 

        try:
            for i in range(len(self.typedWords)):
                if(self.typedWords[i] == self.totalWords[i]):
                    self.correctWords.append(self.typedWords[i])
                else:
                    self.incorrectWords.update({self.totalWords[i] : self.typedWords[i]})

        except Exception as e:
            print(e)


        self.accuracy = len(self.correctWords)/len(self.typedWords) * 100
        self.wordPerMin = len(self.typedWords) / (self.time/60)

        print('\n\n Result :--')
        print(f'Accuracy: -- {self.accuracy}')
        print(f'Word Per Minute :-- {self.wordPerMin}')
        print(f'Incorrect Words :-- {self.incorrectWords}')

Mytester =Tester("Most of the people would find the picture of our universe as an infinite tower of tortoise rather ridiculous, but why we think we know better")