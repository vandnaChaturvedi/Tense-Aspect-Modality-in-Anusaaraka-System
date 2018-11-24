import sys,os,re
f1 = open("standing_1_filt","w")
with open('standing_1', 'r') as inF:
    for line in inF:
        if 'standing' in line:
            words = line.split()
            for j in range(0,len(words)):
                if words[j] == "standing":
                  if j != len(words)-1:
                    if re.match("^[a-zA-Z]*$", words[j+1]): 
                      f1.write(words[j+1])
                      f1.write("\n")
f1.close()

os.system("cd /home/vandna/anusaaraka/apertium")
os.system("lt-proc -a /home/vandna/anusaaraka/apertium/en.morf.bin standing_1_filt > morph_output")

f1 = open("all_pp_standing","w")
f2 = open("morph_output",'r')
lines = f2.readlines()
for i in range(0,len(lines)):
        if "<pp>" in lines[i]:
            f1.write(lines[i])
f1.close()
f2.close()

f1 = open("all_pp_unq_standing","r+")
lines_unq = set()
for line in open("all_pp_standing", "r") :
        if line not in lines_unq: # not a duplicate
            f1.write(line)
            lines_unq.add(line)  
f2= open("standing_words","w")
for line in f1:
    if line.startswith("^") != -1:
        word = line[1:line.index("/")]
        f2.write(word)
        f2.write("\n")
f1.close()
f2.close()

d = {}
lineNumber = {}
print "Processing...."
with open("words_standing", "r+") as f:
    for line in f:
        d[line.split()[0]] = 1

print "[Completed] making DICT."
with open("standing_1", "r+") as f:
    for line in f:
        words = line.split()
        for i in range(len(words)):
            if words[i] == "standing":
                try:
                    d[words[i+1]]
                    lineNumber[words[0].split(":")[0]] = 1
                    break
                except:
                    pass
print "[Completed] finding lineNumber."
flag = False
out_f = open("output_sentences_standing.txt", "w+")
with open("standing_1_1") as f:
    for line in f:
        if flag:
            #print line
            out_f.write(line)
            flag = False
        try:
            words = line.split()
            lineNumber[words[0].split(":")[0]]
            #print line
            out_f.write(line)
            flag = True
        except:
            pass
print "Output is generated, please see output_generated.txt"
out_f.close()