import pyperclip

def Clipboard(spoofcheck,stat):    
    backup=pyperclip.paste()
    print '      Old content:  "'+backup+'"'
    pyperclip.copy(spoofcheck)