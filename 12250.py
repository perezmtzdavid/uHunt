import sys

lines = sys.stdin.readlines()
count = 1

for word in lines:    
    word = word.replace('\n','')
    if word == "HELLO":
        print("Case %d: ENGLISH"% (count))
    elif word == "HOLA":
        print("Case %d: SPANISH"% (count))
    elif word == "HALLO":
        print("Case %d: GERMAN"% (count))
    elif word == "BONJOUR":
        print("Case %d: FRENCH"% (count))
    elif word == "CIAO":
        print("Case %d: ITALIAN"% (count))
    elif word == "ZDRAVSTVUJTE":
        print("Case %d: RUSSIAN"% (count))
    elif word == '#':
        break
    else:
        print("Case %d: UNKNOWN"% (count))
    count += 1