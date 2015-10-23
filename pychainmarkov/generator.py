import sys, types
import random
from collections import defaultdict


class Generator():
    def __init__(self, data):
        self.wordDict = defaultdict(set)
        self.gramList = []
        self.data = data


    def train(self, strength, data):
        for text in data:
            split_text = text.split()
            text_len = len(split_text)
            for i in range(text_len - strength):
                keyTup =()
                step = 0
                j = i
                while (step<strength):
                    keyTup+=(split_text[j],)
                    step += 1
                    j += 1
                self.wordDict[keyTup].add(split_text[j])
            self.gramList = self.wordDict.keys()

    def generate(self, strength, length = 250):
        self.train(strength, self.data)
        rand_options = len(self.gramList)
        rand_i = random.randint(0, rand_options - 1)
        seed_word = self.gramList[rand_i]
        text = u""
        for i in range(length):
            followingList = list(self.wordDict[seed])
            followingLen = len(followingList)
            if followingLen is 0:
                seed = self.gramList[random.randint(0, rand_options - 1)]
                i -= 1
                continue
            nextTup = ()
            nextTup += seed[1:]
            randNext_i = random.randint(0,followingLen - 1)
            nextWord = followingList[randNext_i]
            nextTup += (nextWord,)
            seed = nextTup
        return text

if __name__=="__main__":
    new = Generator(sys.argv[1])
    new.Generate(2,20)