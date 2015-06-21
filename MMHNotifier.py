import urllib2
import time
import notify
import datetime

while 1:
    f=urllib2.urlopen("http://makemehost.com/games.php").read().lower()
    if ('parasite' in f) | ('p a r a s i t e' in f):
        print 'up!', datetime.datetime.now().strftime("%y-%m-%d %H:%M")
        notify.balloon_tip('Game up!', 'It is time!')
    else:
        print 'down', datetime.datetime.now().strftime("%y-%m-%d %H:%M")
    time.sleep(60)