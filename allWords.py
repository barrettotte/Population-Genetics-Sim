class AllWords:
    allNouns = []
    allAdjectives = []
    nounsLen = []
    adjectivesLen = []

    def __init__(self):
        self.allNouns = self.getWords('nouns.txt')
        self.allAdjectives = self.getWords('adjectives.txt')
        self.nounsLen = len(self.allNouns)
        self.adjectivesLen = len(self.allAdjectives)
        
    def getWords(self, fileName):
        with open(fileName, 'r') as f:
            content = f.read()
        return content.split('\n')