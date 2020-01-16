# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    def x(n):
       x = [i for i in n]
       x.reverse()
       return "".join(x)
        
    return " ".join([i if len(i) < 5 else x(i) for i in sentence.split()])
    
print(spin_words("Welcome"))