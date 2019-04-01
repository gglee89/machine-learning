class Bitstrings:
    n = 2
    B = [None] * n

    def printBitstring(self, B):
        print(B)

    def AllBitstrings(self, i):
        if i == self.n:
            self.printBitstring(self.B)
        else:
            self.B[i] = 0
            self.AllBitstrings(i+1)
            self.B[i] = 1
            self.AllBitstrings(i+1)


bitstr = Bitstrings()
bitstr.AllBitstrings(0)
