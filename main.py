import random
import time
#to generate snake positions as dictionary randomly
snake_pos = {}
val1=[]
val2=[]

for i in range(100):
    a=random.randint(1,100)
    b=random.randint(1,100)
    if a>b and a!=100:
        val1.append(a)
        val2.append(b)

for i in range(10):
    snake_pos.update({val1[i]:val2[i]})

print("Snake positions at: ",snake_pos)


#to generate ladder positions randomly as dictionary
# not matching with snake positions
ladder_pos = {}
val3=[]
val4=[]

for i in range(100):
    a=random.randint(1,100)
    b=random.randint(1,100)
    if a<b and b!=100:
        val3.append(a)
        val4.append(b)

j=0
while j!=10 and (val3[j],val4[j] not in snake_pos.items()):
    ladder_pos.update({val3[j]: val4[j]})
    j+=1

print("Ladder positions at: ",ladder_pos)

#class definition with funcs
class Player:

    def __init__(self,aname):
        self.name=aname
        self.pos_initial=1

    def roll_dice(self,name_p):
        print("Rolling Dice for player ",name_p)
        time.sleep(1)
        die=(random.randint(1,6))
        print(die)
        return die

    def snake(self,curr_pos):
        for x, y in snake_pos.items():
            if curr_pos == x:
                curr_pos = y
        return curr_pos

    def ladder(self,curr_pos):
        for x,y in ladder_pos.items():
            if curr_pos==x:
                curr_pos=y
        return curr_pos

    def curr_pos(self,name_play):
        die_result=Player(name_play).roll_dice(name_play)
        self.pos_initial=self.pos_initial+die_result
        a=self.pos_initial
        if a!=Player(name_play).snake(a):
            print("Snake at position", a)
            return Player(name_play).snake(a)
        elif a!=Player(name_play).ladder(a):
            print("Ladder at position ", a)
            return Player(name_play).ladder(a)
        else:
            return a

# end of class

print("Welcome to SNAKES & LADDERS (By Ishan Singh)")
print("Enter the no of players")
p=int(input())


names=[]
for i in range(p):
    print("Enter the name of player ",i+1)
    x=input()
    names.append(x)
#list with names generated

print("Let's Roll")

for i in range(p):
    names[i]=Player(names[i])
#object by names[i] created

final=100
for x in range(1000):
    for i in range(p):
        fin=names[i].curr_pos(names[i].name)
        if fin<=100:
            names[i].pos_initial = fin
            print("The current position of player",i+1,":",names[i].name ,"is", str(names[i].pos_initial),"\n")
            time.sleep(1)
        else:
            continue
        if names[i].pos_initial == 100:
            print("Winner is player ", names[i].name)
            final=101
            break
    if final==101:
        break
























