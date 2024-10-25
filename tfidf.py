import math

class Tfidf:
    """tf, idf, tf-idf"""
    def __init__(self, getlist, tfidf = "tf-idf"):
        self.getlist = getlist
        self.tfidf = tfidf

    def indexing(self, arg):
        """memoization"""
        self.arg = arg
        self.ind = 0
        memo = {}
        for i in self.arg:
            if i not in memo.keys():
                memo[i] = 1
            else:
                memo[i] += 1
        return memo

    def load(self):
        """method return dictionary of words with tf, idf, tf-idf"""
        kdict = {}
        instv = [j for i in self.getlist for j in i]

        ind = self.indexing(instv)

        if self.tfidf == "tf" and len(self.getlist) != 1:
            for i in self.getlist:
                for j in i:
                    c = ind[j]
                    kdict[j] = c / len(instv)
            return kdict

        elif self.tfidf == "idf" and len(self.getlist) != 1:
            for i in self.getlist:
                for j in i:
                    if j not in kdict:
                        kdict[j] = math.log10(len(self.getlist)/sum([1.0 for i in self.getlist if j in i]))
            return kdict

        elif self.tfidf == "tf-idf" and len(self.getlist) != 1:
            for i in self.getlist:
                for j in i:
                    if j not in kdict.keys():
                        c = ind[j]
                        vartf = c / len(instv)
                        varidf = math.log10(len(self.getlist)/sum([1.0 for i in self.getlist if j in i]))
                        kdict[j] = vartf * varidf
            return kdict
