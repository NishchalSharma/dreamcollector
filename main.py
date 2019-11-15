import random
import math
import matplotlib.pyplot as plt

cap_mul=2
vcap_mul=1.5

class player:
    def __init__(self,name):
        self.name=name
        self.score=0
        self.iscap=False
        self.isvcap=False
    def makeCap(self):
        self.iscap=True
    def makeVCap(self):
        self.isvcap=True

    def getscore(self):
        if(self.iscap):
            return(cap_mul*self.score)
        elif(self.isvcap):
            return(vcap_mul*self.score)
        else:
            return(self.score)

    def display(self):
        s="Name:"+str(self.name)
        if(self.iscap):
            s=s+"(C)"
        elif(self.isvcap):
            s=s+"(VC)"
        else:
            pass
        s=s+" "+str(self.getscore())
        print(s)
#--------------------------------------------------------
class team:
    def __init__(self):
        self.name=""
        self.players=[]
        self.count=11
        self.filled=0
        self.GrandScore=0
        self.currentScore=0
    def updateGrandScore(self):
        
        self.currentScore=self.getTotal()
        self.GrandScore+=self.currentScore

    def addplayer(self,player):
        if(self.filled<self.count):
            self.players.append(player)
            self.filled+=1
            
    def totalScore(self):
        s=0
        for p in self.players:
            s=s+p.score()
        return(s)

    def display(self):
        print("***-----***")
        for p in self.players:
            p.display()
        print("***-----***")

    def displayTotal(self):
        t=0
        for p in self.players:
            t+=p.getscore()
        print("T>>>"+str(t))
    def getTotal(self):
        t=0
        for p in self.players:
            t+=p.getscore()
        return(t)

#-----------------------------------------------------------------
class selectionlist:
    def __init__(self,f):
        self.teams=[]
        self.chancelist={}
        self.scorelist={}
        self.sortedScoreList=[]
        self.playername=[]
        self.file=f
        self.totalmatch=0
        self.BingoCount50=0
        self.BingoCount40=0
        self.BingoCount30=0
        self.BingoCount20=0
        self.BingoCount10=0
        self.BingoCount05=0
        self.BingoCount01=0
    

    def createList(self):
        f=open(self.file,"r")
        lines =f.readlines()
        for line in lines:
            player,chance=line.split(",")
            player=player.rstrip("\n")
            chance=chance.rstrip("\n")
            self.playername.append(player)
            self.chancelist[player]=chance
            self.scorelist[player]=0

    def generateTeam(self):
        t=team()
        c=0
        a=0
        l=len(self.playername)
        random.shuffle(self.playername) 
        for p in self.playername:
            r=random.random()*100
            if((11-a)<(l-c)):
                if(r<int(self.chancelist[p])):
                    #print(">>>>"+str(r)+"<<<<"+str(self.chancelist[p]))
                    plr=player(p)
                    t.addplayer(plr)
                    a=a+1
            else:
                plr=player(p)
                t.addplayer(plr)
                a=a+1
            c=c+1
                    

        x=random.randrange(0,11)
        y=random.randrange(0,11)

        t.players[x].makeCap()
        t.players[y].makeVCap()
        return(t)
    def createRandomTeams(self,n,t):
        self.totalmatch=t
        for i in range(n):
            self.teams.append(self.generateTeam())
    
    def assignScore(self):
        for p in self.playername:
            sc=math.floor(random.randrange(-1,20))
            self.scorelist[p]=sc

    def updateAllTeams(self):
        for t in self.teams:
            for p in t.players:               
                p.score=self.scorelist[p.name]
                
        for myp in self.myTeam.players:               
                myp.score=self.scorelist[myp.name]
        
        
    def updateGrandScore(self):
        self.sortedScoreList=[]
        for t in self.teams:
            t.updateGrandScore()
            self.sortedScoreList.append(t.currentScore)
        self.myTeam.updateGrandScore()

        self.sortedScoreList.sort(reverse=True)
        #print(self.sortedScoreList)
        l=len(self.sortedScoreList)
        cutoff50=int(l*0.50)
        cutoff40=int(l*0.40)
        cutoff30=int(l*0.30)
        cutoff20=int(l*0.20)
        cutoff10=int(l*0.10)
        cutoff05=int(l*0.05)
        cutscore50=self.sortedScoreList[cutoff50]
        cutscore40=self.sortedScoreList[cutoff40]
        cutscore30=self.sortedScoreList[cutoff30]
        cutscore20=self.sortedScoreList[cutoff20]
        cutscore10=self.sortedScoreList[cutoff10]
        cutscore05=self.sortedScoreList[cutoff05]

        if self.myTeam.currentScore>=cutscore50:
            self.BingoCount50+=1
        if self.myTeam.currentScore>=cutscore40:
            self.BingoCount40+=1
        if self.myTeam.currentScore>=cutscore30:
            self.BingoCount30+=1
        if self.myTeam.currentScore>=cutscore20:
            self.BingoCount20+=1
        if self.myTeam.currentScore>=cutscore10:
            self.BingoCount10+=1
        if self.myTeam.currentScore>=cutscore05:
            self.BingoCount05+=1
        if self.myTeam.currentScore>=self.sortedScoreList[0]:
            self.BingoCount01+=1

    def ShowBingoCount(self):

        x5=self.BingoCount50-self.BingoCount40
        x4=self.BingoCount40-self.BingoCount30
        x3=self.BingoCount30-self.BingoCount20
        x2=self.BingoCount20-self.BingoCount10
        x1=self.BingoCount10-self.BingoCount05
        x0=self.BingoCount05-self.BingoCount01
        x=self.BingoCount01
        fail=self.totalmatch-self.BingoCount50

        print("Total Bingo50 Hits:"+str(x5))
        print("Total Bingo40 Hits:"+str(x4))
        print("Total Bingo30 Hits:"+str(x3))
        print("Total Bingo20 Hits:"+str(x2))
        print("Total Bingo10 Hits:"+str(x1))
        print("Total Bingo05 Hits:"+str(x0))
        print("Total grand Hits:"+str(x))
        print("Over all Hits:"+str(self.BingoCount50))
        print("Misses="+str(fail))

        plt.bar([1, 2, 3, 4,5,6,7,8],[x,x0, x1, x2, x3,x4,x5,fail])
        plt.show()

    def display(self):
        
        for t in self.teams:
            t.displayTotal()
        self.myTeam.displayTotal()
    def runMatch(self):
        for i in range(self.totalmatch):
            s.assignScore()
            s.updateAllTeams()
            s.updateGrandScore()
        
    def createMyTeam(self,l,c,vc):
        t=team()
        x=0
        for l1 in l:
           # print(">>Adding To my Team",)
            p=self.playername[l1]
            #print(p)
            plr=player(p)
            if(x==c):
                plr.makeCap()
            
            if(x==vc):
                plr.makeVCap()
            
            t.addplayer(plr)
            x=x+1
        self.myTeam=t
        '''
        print(">>Finished adding team")
        for x in t.players:
            x.display() 
        '''
        
    def dump(self):
        s=""
        for t in self.teams:
            s=s+str(t.GrandScore)+","
            s=s+str(t.getTotal())
            for p in t.players:
                s=s+","+self.chancelist[p.name]+","
                if(p.iscap):
                    s=s+"*"+p.name+","+str(p.getscore())
                elif(p.isvcap):
                    s=s+"#"+p.name+","+str(p.getscore())
                else:
                    s=s+p.name+","+str(p.getscore())
            s=s+"\n"
        s=s+"$$$"
        s=s+str(self.myTeam.GrandScore)+","
        s=s+str(self.myTeam.getTotal())
        for p in self.myTeam.players:
                s=s+","+self.chancelist[p.name]+","
                if(p.iscap):
                    s=s+"*"+p.name+","+str(p.getscore())
                elif(p.isvcap):
                    s=s+"#"+p.name+","+str(p.getscore())
                else:
                    s=s+p.name+","+str(p.getscore())
        s=s+"\n"
        sa=open("save.csv","w")
        sa.write(s)

#-----Code--------------------------------------

s=selectionlist("player.txt")
l=[0,1,2,3,4,5,6,7,8,9,10]
#l=[1,2,3,4,8,10,15,13,18,19,21]
s.createList()
s.createMyTeam(l,7,8)
s.createRandomTeams(20,1000)
s.runMatch()
s.ShowBingoCount()
'''
#s.display()
print("--------Score List-----------")
print(s.scorelist)
print("----------Chance List---------")
print(s.chancelist)
'''
#s.dump()



