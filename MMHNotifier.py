import urllib2
import time
import notify
import datetime
import sys


def GameName(f,name):
    cent=f.lower().index(name)
    while f[cent] != '>':
        cent-=1
    bot=cent+1
    while f[cent] != '<':
        cent+=1
    top=cent
    p_bot=x=top+9
    while f[x] != '<':
        x+=1
    p_top=x
    gname=f[bot:top]
    gplay=f[p_bot:p_top]
    print 'Game name: '+gname+' '+gplay
    return gname,gplay 


def GameSearch(f,tests):
    for name in tests:
        if name in f.lower():
            print 'up!', datetime.datetime.now().strftime("%H:%M"),
            gname,gplay = GameName(f,name)
            notify.balloon_tip('Game up!', 'Game name: '+gname+' '+gplay)
            return 1
    print 'down', datetime.datetime.now().strftime("%H:%M")
    return 0
    
try:
    a=float(sys.argv[1])
except:
    a=60

while 1:    
    tests=['parasite','p a r a s i t e']
    f=urllib2.urlopen("http://makemehost.com/games.php").read()
    GameSearch(f,tests)        
    time.sleep(a)