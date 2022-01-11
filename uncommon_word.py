from collections import Counter
class Sol:
    def uncommon_word(self,s1,s2):
        all=list(s1.split(" "))+list(s2.split(" "))
        return [word for word,count in Counter(all).items() if count==1]
if __name__ == '__main__':
    p = Sol()
    print(p.uncommon_word(s1 = "app app", s2 = "ban"))
