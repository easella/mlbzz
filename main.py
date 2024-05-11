import math
import time
t=[]
x={'game':0}
start_time = time.time()
import pandas as pd
from datetime import date,datetime,timedelta
class Elo:

  def __init__(self,k,g=1,homefield = 24):
    self.ratingDict   = {}  
    self.k        = k
    self.g        = g
    self.homefield    = homefield

  def addPlayer(self,name,rating = 1500):
    self.ratingDict[name] = rating
    
  def gameOver(self, winner, loser, winnerHome,neutral,wins,loses,gpzz,wr,lr):
    global result
   
    tie=False
    if neutral==0:
        
        t.append(1)
        if winnerHome==True:
            result = self.expectResult(self.ratingDict[winner]+24+wr ,lr+self.ratingDict[loser])
            win=eloLeague.ratingDict[winner]+wr+24
            lose=eloLeague.ratingDict[loser]+lr
        if winnerHome==False:
            result = self.expectResult(self.ratingDict[winner]+wr, self.ratingDict[loser] +lr+ 24)
            win=eloLeague.ratingDict[winner]+wr
            lose=eloLeague.ratingDict[loser]+lr+24
    if neutral==1:
        result = self.expectResult(self.ratingDict[winner]+wr, self.ratingDict[loser]+lr)
        win=eloLeague.ratingDict[winner]+wr
        lose=eloLeague.ratingDict[loser]+lr
    
    if(neutral==0 and winnerHome==True):
        win+=24
    if(neutral==0 and winnerHome!=True):
        lose+=24
    x['game']=gpzz
    k=5*(0.9999)**x['game']
    if k<4:
        
        k=4
    z=win-lose
    if wins==loses:
        tie=True
    if tie!=True:
        pd=abs(wins-loses)
        mult=(0.6686*math.log(wins-loses)+0.8048)*(2.05/(z* 0.001 + 2.05))
        
        shift=(k*mult)*(1-result)
        self.ratingDict[winner] +=shift
        self.ratingDict[loser]  -=shift
    if tie:
        pd=wins-loses
        mult=(0.6686*math.log(1)+0.8048)*(2.05/(1* 0.001 + 2.05))
        shift=(k*mult)*(0.5-result)
        self.ratingDict[winner] +=shift
        self.ratingDict[loser]  -=shift
    
  def expectResult(self, p1, p2):
    exp = (p2-p1)/400.0
    return 1/((10.0**(exp))+1)
		
		



adrev=0
today = date.today()
tomorrow = today + timedelta(1)

dfz=pd.read_csv("https://projects.fivethirtyeight.com/mlb-api/mlb_elo.csv").fillna(0)
dfz=dfz.astype({"team1":"string","team2":"string"})
gamesd={}

td=dfz[dfz.index==0]
for row in td.itertuples():
    datez=row.date
gamesd[datez]={}
gamesd['2022-11-05']={}
datez=datetime.strptime(datez, "%Y-%m-%d")
nd=datez
dz=pd.date_range(start="1871-05-01",end=nd)
wins={}
df=pd.read_csv("https://ontheroadtovote.com/mlb/wintotals.txt")
for i in range(1990,2025):
    wins[i]={}
    
for row in df.itertuples():
    wins[float(row.season)][row.Team]={}
    wins[float(row.season)][row.Team]=float(row.WT)
for datee in dz:
    datee=str(datee)
    datee=datee.replace(" 00:00:00","")
    gamesd[str(datee)]={ }

for row in dfz.itertuples():
    gamesd[row.date][row.team1]=1
    gamesd[row.date][row.team2]=1
    
string = date.today()
df=dfz[((dfz.date < str(tomorrow)))] 
df=df.sort_values(by='date')
todayzz=string.strftime("%Y-%m-%d")
from2000  = df

eloLeague   = Elo(k = 4,homefield=24)
from2000=from2000[['date','season','team1','team2','neutral','score1','score2','pitcher1_adj','pitcher2_adj','rating1_pre','rating2_pre','elo1_pre','elo2_pre']]
from tqdm.auto import tqdm
    
toodayzz=datez
   

# Returns the current local date
string = date.today()
todayzz=string.strftime("%Y-%m-%d")
allTeams=(from2000.team1.tolist()+from2000.team2.tolist())
for team in allTeams:
    eloLeague.addPlayer(team,rating=1500)

ss={}
ddf=pd.read_csv("https://ontheroadtovote.com/ncaab/mlb.csv")
import requests
import urllib, json
url = "https://raw.githubusercontent.com/easella/mlbsalaries/main/2021sal.json"
response = requests.get(url)
q=str(response.text)
q=q.replace("'",'"')
data2021 = json.loads(q)
url = "https://raw.githubusercontent.com/easella/mlbsalaries/main/2022sal.json"
response = requests.get(url)
q=str(response.text)
q=q.replace("'",'"')
data2022 = json.loads(q)
for season in dfz.season.unique():
    ss[season]={}
for season in dfz.season.unique():
    j=dfz[dfz.season==season]
    j.sort_values(by='date',inplace=True)
    j=j.head(1)
    for row in j.itertuples():
        ss[season]=row.date
for row in from2000.itertuples():
    fd=str(row.date)
    fd=fd.replace("-","")
    from2000.at[row.Index,'fd']=float(fd)
from2000.sort_values('fd',inplace=True)
currSeason=1871
ddf=ddf.rename(columns={'Tm':"Team"})
from2000=from2000[(from2000.date<str(today))]
w=0
l=0
gpy=0
d=[]
d=[]
msqe={}
import requests
import pandas as pd
dates=[2023]
ts=requests.get("https://ontheroadtovote.com/mlb/teams.json").json()
from2000=from2000[from2000.season<2023]
for row in from2000.itertuples():
    d.append([row.team1,row.team2,row.neutral,row.score1,row.score2,row.date,row.season])
dates=pd.date_range(start='2023-03-30',end='2023-11-01')
for date in dates:
    date=str(date)
    
    e="https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates="+str(date)+"&limit=500"
    e=e.replace(" 00:00:00","")
    e=e.replace("-","")
    html=requests.get(e)
    jsonz=html.json()

    events=jsonz['events']


    for idz in events:
        teams=idz['name']
        teamss=str(teams)
        teams=teamss.split("at")
        ht=teams[1]
        at=teams[0]
        competitions=idz['competitions']
    
        competitors=idz['competitions'][0]['competitors']
    
        c=idz['competitions'][0]
        hn=competitors[0]['team']['shortDisplayName']
        an=competitors[1]['team']['shortDisplayName']
        n=c['neutralSite']
        
        hts=competitors[0]['score']
        ats=competitors[1]['score']
        active=competitors[1]['team']['isActive']
        status=idz['status']
        completed=status['type']['completed']
        datez=idz['date']
        st=status['type']['detail']
        st=str(st)
        st=st.replace("[","")
        stt=st.replace("]","")
        stt=stt
        st=stt.split("at")
        if ("at" in stt):
            st=st[1]
        if ("at" not in stt):
            st=stt
        if("Final") in stt:
            r="Final"
        if("Final") not in stt:
            r="Start Time:"+str(st)
        hn=str(hn)
        an=str(an)
        if "OT" in str(st):
            ot=1
        if "OT" not in str(st):
            ot=0
        else:
            venueinfo='TBD'
            state='TBD'
            
        n=str(n)
        n=n.replace("True","1")
        n=n.replace("False","0")
        if hn in ts:
            hn=ts[hn]
        if an in ts:
            an=ts[an]
        d.append([hn,an,n,hts,ats,date,2023])

msqe={}
import requests
import pandas as pd
dates=[2023]
from datetime import datetime, timedelta
yesterday = datetime.now() - timedelta(1)
yesterday=datetime.strftime(yesterday, '%Y-%m-%d')
dates=pd.date_range(start='2024-03-28',end=yesterday)
for date in dates:
    date=str(date)
    
    e="https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates="+str(date)+"&limit=500"
    e=e.replace(" 00:00:00","")
    e=e.replace("-","")
    html=requests.get(e)
    jsonz=html.json()

    events=jsonz['events']


    for idz in events:
        teams=idz['name']
        teamss=str(teams)
        teams=teamss.split("at")
        ht=teams[1]
        at=teams[0]
        competitions=idz['competitions']
    
        competitors=idz['competitions'][0]['competitors']
    
        c=idz['competitions'][0]
        hn=competitors[0]['team']['shortDisplayName']
        an=competitors[1]['team']['shortDisplayName']
        n=c['neutralSite']
        
        hts=competitors[0]['score']
        ats=competitors[1]['score']
        active=competitors[1]['team']['isActive']
        status=idz['status']
        completed=status['type']['completed']
        datez=idz['date']
        st=status['type']['detail']
        st=str(st)
        st=st.replace("[","")
        stt=st.replace("]","")
        stt=stt
        st=stt.split("at")
        if ("at" in stt):
            st=st[1]
        if ("at" not in stt):
            st=stt
        if("Final") in stt:
            r="Final"
        if("Final") not in stt:
            r="Start Time:"+str(st)
        hn=str(hn)
        an=str(an)
        if "OT" in str(st):
            ot=1
        if "OT" not in str(st):
            ot=0
        else:
            venueinfo='TBD'
            state='TBD'
            
        n=str(n)
        n=n.replace("True","1")
        n=n.replace("False","0")
        if hn in ts:
            hn=ts[hn]
        if an in ts:
            an=ts[an]
        if hts==0 and ats==0:
            m=1
        else:
            d.append([hn,an,n,hts,ats,date,2024])
from2000=pd.DataFrame(d,columns=['team1','team2','neutral','score1','score2','date','season'])
from2000=from2000[from2000.team2!='National']
from2000=from2000[from2000.team1!='National']
from2000=from2000[from2000.team1!='American']
from2000=from2000[from2000.team2!='American']
from2000=from2000.astype({"team1":"string","team2":"string","score1":float,"score2":float,"neutral":float,"season":float})
rest={}
import numpy as np

msqe={}

for i in range(2,120):
    msqe[i]=[]
for game in from2000.itertuples():
    
    
    
                
            
    t1r=0
    t2r=0
    datez=str(game.date)
    datez=datez.replace("-","")
    datez=datez.replace(" 00:00:00","")
    datez=float(datez)
    
    if game.team2 in rest:
        d2=str(rest[game.team2])
        rest[game.team2]=game.date
    else:
        d2=game.date
    if game.team1 in rest:
        
        d1=str(rest[game.team1])
    else:
        rest[game.team1]=game.date
        d1=game.date
    d2=d2.replace("-","")
    d1=d1.replace("-","")
    d1=d1.replace(" 00:00:00","")
    d2=d2.replace(" 00:00:00","")
    dt1r=datez-float(d1)
    dt2r=datez-float(d2)
    if dt2r>dt1r:
        t2r=dt2r-dt1r
    if dt1r>dt2r:
        t1r=dt1r-dt2r
    if t1r>t2r:
        t1r=t1r-t2r
    else:
        t2r=t2r-t1r
    t2r=t2r*2.3
    t1r=t1r*2.3
    if (game.season > currSeason):
        
        
        
        
        print(game.season)
        gpy=0

    
        for key in eloLeague.ratingDict.keys():
            wt=0
            if game.season>1989:
                if key in wins[float(game.season)]:
                    wl=wins[float(game.season)][key]
                    if game.season==2020:
                        wt=(30-round(wl))*-4
                    else:
                        wt=(81-round(wl))*-4
            
            eloLeague.ratingDict[key]+=(wt*(0.67))
            eloLeague.ratingDict[key] = eloLeague.ratingDict[key] - ((eloLeague.ratingDict[key] - 1500) * (0.33))
        
        currSeason =game.season
    if game.score2 > game.score1:
        gpy+=1
        team1=game.team1
        team2=game.team2
    
        if(game.neutral==1):
            eloLeague.gameOver(game.team2, game.team1, True,game.neutral,game.score2,game.score1,gpy,t2r,t1r)
        else:
            
            eloLeague.gameOver(game.team2, game.team1, False,game.neutral,game.score2,game.score1,gpy,t2r,t1r)
    if game.neutral==1:
        hr=eloLeague.ratingDict[game.team1]+t1r
        ar=eloLeague.ratingDict[game.team2]+t2r
    if game.neutral==0:
        hr=eloLeague.ratingDict[game.team1]+t1r+24
        ar=eloLeague.ratingDict[game.team2]+t2r
        
    for i in range(2,120):
        mse = np.mean(((game.score1-game.score2) - round(((hr-ar)/i)))**2)
        msqe[i].append(mse)
    if (game.score1>game.score2)or(game.score1==game.score2):
        already=0
        gpy+=1
        team1=game.team1
        team2=game.team2
        homez=24
        if(game.neutral==1):
        
            homez=0
            eloLeague.gameOver(game.team1, game.team2, True,game.neutral,game.score1,game.score2,gpy,t1r,t2r)
        else:
            eloLeague.gameOver(game.team1, game.team2, True,game.neutral,game.score1,game.score2,gpy,t1r,t2r)
    rest[game.team1]=game.date
    rest[game.team2]=game.date
ms={}
for i in range(2,120):
    ms[float(i)]=0
for k in msqe:
    ms[float(k)]=(np.mean(msqe[k]))
from datetime import date
dates=[date.today()]
h=[]
for date in dates:
    date=str(date)
    
    e="https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates="+str(date)+"&limit=500"
    e=e.replace(" 00:00:00","")
    e=e.replace("-","")
    html=requests.get(e)
    jsonz=html.json()

    events=jsonz['events']


    for idz in events:
        teams=idz['name']
        teamss=str(teams)
        teams=teamss.split("at")
        ht=teams[1]
        at=teams[0]
        competitions=idz['competitions']
    
        competitors=idz['competitions'][0]['competitors']
    
        c=idz['competitions'][0]
        hn=competitors[0]['team']['shortDisplayName']
        an=competitors[1]['team']['shortDisplayName']
        n=c['neutralSite']
        
        hts=competitors[0]['score']
        ats=competitors[1]['score']
        active=competitors[1]['team']['isActive']
        status=idz['status']
        completed=status['type']['completed']
        datez=idz['date']
        st=status['type']['detail']
        st=str(st)
        st=st.replace("[","")
        stt=st.replace("]","")
        stt=stt
        st=stt.split("at")
        if ("at" in stt):
            st=st[1]
        if ("at" not in stt):
            st=stt
        if("Final") in stt:
            r="Final"
        if("Final") not in stt:
            r="Start Time:"+str(st)
        hn=str(hn)
        an=str(an)
        if "OT" in str(st):
            ot=1
        if "OT" not in str(st):
            ot=0
        else:
            venueinfo='TBD'
            state='TBD'
            
        n=str(n)
        n=n.replace("True","1")
        n=n.replace("False","0")
        if hn in ts:
            hn=ts[hn]
        if an in ts:
            an=ts[an]
        h.append([hn,an,n,hts,ats,date,2023])
    
for row in h:
    t1=row[0]
    t2=row[1]
    n=row[2]
    t1r=0
    t2r=0
    datez=str(today)
    datez=datez.replace("-","")
    datez=datez.replace(" 00:00:00","")
    datez=float(datez)
    d2=str(rest[t2])
    rest[t2]=str(today)
    d1=str(rest[t1])
    d2=d2.replace("-","")
    d1=d1.replace("-","")
    d1=d1.replace(" 00:00:00","")
    d2=d2.replace(" 00:00:00","")
    dt1r=datez-float(d1)
    dt2r=datez-float(d2)
    if dt2r>dt1r:
        t2r=dt2r-dt1r
    if dt1r>dt2r:
        t1r=dt1r-dt2r
    if t1r>t2r:
        t1r=t1r-t2r
    else:
        t2r=t2r-t1r
    t2r=t2r*2.3
    t1r=t1r*2.3
    if t1r>0:
        print(row)
    if t2r>0:
        print(row)
    temp = min(ms.values())
    res = [key for key in ms if ms[key] == temp]
    for j in res:
        res=float(j)
 
    if '0' in str(n):
        hr=eloLeague.ratingDict[t1]+24+t1r
        ar=eloLeague.ratingDict[t2]+t2r
    else:
        hr=eloLeague.ratingDict[t1]+t1r
        ar=eloLeague.ratingDict[t2]+t2r
    if hr>ar:
        spread=((hr-ar)/res)
        print(t1+" beats  "+t2+" by "+str(spread))
    else:
        spread=((ar-hr)/res)
        print(t2+" beats  "+t1+" by "+str(spread))
