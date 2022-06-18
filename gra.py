import random,os
H="♥X"
while True:
    print("press ctrl+c to close")
    
    #seeds
    makeseed=input("seed(left Empty if random):")
    if len(makeseed)==0:
        random.seed()
    else:
        print("seed loaded:",sum([ord(i) for i in makeseed]))
        random.seed(sum([ord(i) for i in makeseed]))
    print('użuj syntaxu pythona żeby robić bramki logiczne!')

    def test(f,table):
        """function that test function as answer to level"""
        for i in table:
            if f(*i)!=table[i]:
                return False,f"not correct(test faild) at {i} {f(*i)}+"
        return True,'NaN'
    
    def printTable(table):
        """prints table in fun way!"""
        print('your table')
        for i in table:
            print(i,table[i],sep=":")

    print("(E)asy  -> for noobs!")
    print("(N)rmal -> for people")
    print("(H)ard  -> haker mode")
    
    odp=input("choose>").lower()
    
    if odp=="n":
        levelO=2
        levelI=2
        yO=10
        yI=3
        maxLevel=42
    elif odp=='e':
        levelO=1
        levelI=1
        yO=12
        yI=3
        maxLevel=15
    elif odp=='h':
        levelO=2
        levelI=3
        yO=4
        yI=2
        maxLevel=69
    else:
        levelO=2
        levelI=2
        yO=10
        yI=3
        maxLevel=42
    
    HC=False
    print("do you wanna survival hardcore (Y/N)")
    if input("choose:").lower()=='y':
        HC=True

    hp=10
    level=0
    while True:
        table={}
        for i in range(0,2**levelI):
            arINP=[int(j) for j in bin(i).split('b')[1]]
            if len(arINP)<levelI:
                arINP=([0]*(levelI-len(arINP)))+arINP
            table[tuple(arINP)]=[random.choice([1,0]) for i in range(levelO)]
    
        print(f"LEVEL:{level} I:{levelI} O:{levelO}")
        ins=[chr(97+i) for i in range(levelI)]
        printTable(table)
        print(ins)
    
        while True:
            cmd=input(">")
            if cmd=="$player":
                print("hp:",f"{int(hp)*H[0]}{(10-int(hp))*H[1]} {hp}/10")
            elif cmd=="$level-info":
                print(f"LEVEL:{level} I:{levelI} O:{levelO}")
                printTable(table)
            elif cmd=="$cls":
                os.system('cls||clear')
            elif (cmd=="$help") | (cmd=="$h") | (cmd=="?"):
                print("$h|?|$help (this msg)")
                print("$cls (clear output" )
                print("$level-info (level_info)")
                print("$player  show player hp")
            else:
                try:
                    f=eval(f"lambda {','.join(ins)}:["+cmd+"]")
                    enso=test(f,table)
                except Exception as E:
                    if HC:
                        hp-=0.5
                    enso=[0,E]
                if enso[0]==True:
                    print('win')
                    break
                else:
                    print(enso[1])
                    if HC:
                        hp-=1
                if hp==0:break
        
        level+=1
        if level%yO==0:
            levelO+=1
            hp+=0.5
        if levelO>yI:
            levelO=1
            levelI+=1
            hp+=1
        if (level>maxLevel)&(not EA):
            print('good job')
            odp=input("wanna play endless? (that will activate hardcore) Y/N")
            if odp.lower()=='y':
                yI-=yI//2
                yO-=yO//2
                HC=True
                EA=True
            else:
                print('you win at:',level)
                break
        if hp==0:
            print("you lost on:",level)
            break