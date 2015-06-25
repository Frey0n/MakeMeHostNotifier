import urllib2
import time
import notify
import datetime
import sys
import pyperclip

def Clipboard(spoofcheck):    
    backup=pyperclip.paste()
    if backup: print '      Old content:  "'+backup+'"'
    pyperclip.copy(spoofcheck)
    
def HostBot(cent):
    temp=cent
    while 'MakeMe' not in f[temp:temp+7]:
        temp-=1
        if (cent-temp) > 100: return 'Not on MakeMe'
    bot=temp
    while f[temp] != '<':
        temp+=1
    top=temp
    ghost= f[bot:top]
    return ghost
    
def GameName(f,name,stat):
    cent=f.lower().index(name)
    temp=cent
    
    #Getting the host bot  --------------------------
    ghost = HostBot(cent)
    
    # Getting the game name  -------------------------
    while f[temp] != '/':
        temp-=1
    while f[cent] != '>':
        cent-=1
    bot=cent+1
    
    #Getting the number of players --------------------
    while f[cent] != '<':
        cent+=1
    top=cent
    p_bot=x=top+9
    while f[x] != '<':
        x+=1
    p_top=x
    gname=f[bot:top]
    gplay=f[p_bot:p_top]
    
    #Printing out ------------------------
    spoofcheck = '/w '+ghost+' s'
    print '   Game name: '+gname+'\n'+'   Players: '+gplay
    if stat: print'   Spoofcheck: '+spoofcheck
    if stat: Clipboard(spoofcheck)
    return gname,gplay 


def GameSearch(f,tests,stat):
    for name in tests:
        if name in f.lower():
            print 'Up!', datetime.datetime.now().strftime("%H:%M")
            gname,gplay = GameName(f,name,stat)
            notify.balloon_tip('Game up!', 'Game name: '+gname+'\n'+'Players: '+gplay)
            return 0
    print 'Down', datetime.datetime.now().strftime("%H:%M")
    return 1

        
try:
    a=float(sys.argv[1])
except:
    a=60
stat=1

while 1:    
    tests=['parasite','p a r a s i t e']
    f=urllib2.urlopen("http://makemehost.com/games.php").read()
    stat=GameSearch(f,tests,stat)        
    time.sleep(a)