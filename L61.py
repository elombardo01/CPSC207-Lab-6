#Emme and Viviana
#Part A
def too_long(x):
    if x > 140:
        print("Too long")
    else:
        print("Good")
too_long(150)
too_long(130)

import unicodedata
print(unicodedata.lookup("sun"))
print(unicodedata.lookup("cat"))
print(unicodedata.lookup("two hearts"))

print("I love cats!", unicodedata.lookup("cat"))
print("Snakes are silly", unicodedata.lookup("snake"))
print("Dogs are the best!", unicodedata.lookup("dog"))
print("Roses are the prettiest flower", unicodedata.lookup("rose"))

print(unicodedata.name("&"))
print(unicodedata.name("["))
print(unicodedata.name("/"))
