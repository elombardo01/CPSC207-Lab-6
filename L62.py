#Emme and Viviana
#Part B
"abc"[0]
"abc"[2]
"waffles"[1]
dinner="falafels"
dinner[4]
["a","b","c"][2]
[1,2,3,4][0]
colors= ["red","green","blue"]
colors[1]
countdown=[3,2,1,"action!"]
countdown[3]
"frog"[-1]
"fish"[-2]
"fish"[2]
#Negative index starts from the end.
#Reach the end of a thing faster

def function(x):
    count = 0
    for i in range(len(x)):
        if x[i] == "o":
            count = count +1
    return count

print(function("legos"))
        
    
    
