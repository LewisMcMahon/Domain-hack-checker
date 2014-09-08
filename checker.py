import pprint

pp = pprint.PrettyPrinter(indent=4)

def getFileAsList(file):
    
    list = []
    
    for line in open(file, 'rb').readlines():
        
        line = line.rstrip('\n')
        line = line.rstrip('\r')
        
        if line <> "":            
            list.append(line)
    
    return list

tlds = getFileAsList("tld.txt")

words = getFileAsList("names.txt")

matches = []

for word in words:
    wordrev = word[::-1].lower()
    for tld in tlds:
        tldrev = tld[::-1].lower()
        tldlen = len(tld)
        
        #print tldrev
        
        if wordrev[:tldlen] == tldrev:
            matchInfo = [word.lower(),tld.lower()]
            print matchInfo
            matches.append(matchInfo)

            
#pp.pprint( matches)