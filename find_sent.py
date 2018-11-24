#-*- coding: utf-8 -*-
from collections import Counter
import sys,os

reload(sys)
sys.setdefaultencoding('utf-8')

def find_sent(fname,sname):
    with open(fname,'r') as f:
        for line in f:
            i = line[:line.index(':')]
            with open(sname,'r') as s:
                for num, line1 in enumerate(s, 1):
                    if int(i)==num:
                        print line, line1
                        word_list = line1.decode("utf-8","ignore").split()
                        wrd_list.append(word_list)
    check_freq(wrd_list)

def check_freq(w_l):
    wrdl=w_l[0]
    count=0
    ws=[]
    larg_list=[]
    high={}
    for i in range(len(w_l)):
        for j in range(len(w_l)):
            wrdl = list(set(w_l[i]).intersection(set(w_l[j])))
            if len(wrdl)==0:
                wrdl = w_l[i]
            else:
                count+=1
                for k in range(len(wrdl)):
                    ws.append(str(wrdl[k]))
    name_list = ['.',',',' ( ',' ) ',' - ','/',';',':','_','{','}','[',']',' ? ','।','"',' ! ']
    vibhakti_list = ['का','की','से','में','पास','द्वारा','ने','के','लिए','साथ','बाद','को','है','हो','भी','ही','पर','हैं','तथा','और','तब','वें','वह','यह','वही','थी','था','थे','ये']
    count = Counter(ws).items()
    perc = {x: float(float(y) / len(ws) * 100) for x,y in count}
    max_pct = 0
    for name, pct in perc.iteritems():
        if name not in name_list:
            #print '%s - %s%s' %(name, pct, ' %'),					//obvious commented
            if (pct >= max_pct and name not in vibhakti_list):
                max_pct = pct
                n = name
                larg_list.append(pct)
 #   print '\n','max % for all the searching words for given string is : ', max_pct, '% for ', n,'\n'
    larg_list.sort(key=float,reverse=True)
    for i in range(len(larg_list)):
  #      print larg_list[i],'-',
        for name, pct in perc.iteritems():
            if(pct == larg_list[i]):
   #             print name,',',
    #    print '\n'


fname = sys.argv[1]
sname = sys.argv[2]
word_list=[]
wrdl=[]
wrd_list=[]

if fname!=' ':
    find_sent(fname,sname)
else: 
    print 'no such file'

