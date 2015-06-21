import urllib2
import time
import notify
import datetime

while 1:
    f=urllib2.urlopen("http://makemehost.com/games.php").read()
    if ('PARASITE' in f) | ('P A R A S I T E' in f):
        print 'up!',
        notify.balloon_tip('Game up!', 'It is time!')
    else:
        print 'down',
    print datetime.datetime.now().strftime("%y-%m-%d %H:%M")
    time.sleep(60)