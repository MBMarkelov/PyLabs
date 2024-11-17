class RealString:
    def __init__(self, string):
        self.string = string

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self.string) == len(other.string)
        elif isinstance(other, str):
            return len(self.string) == len(other)
        return False


    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self.string) < len(other.string)
        elif isinstance(other, str):
            return len(self.string) < len(other)
        return False

def solve():
    str1 = RealString("Apple")
    str2 = RealString("Ябло")

    print(str1 < str2)
    print(str1 == "Orane")
    print(str1 > str2)

if __name__ == "__main__":
    solve()
