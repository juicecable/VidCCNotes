#Copyright Derek Frombach

#This program is designed to take zoom chat logs, and transform them into real-time closed captioning
#The input file must be named input.txt
#There are two options of things: main headings, and bullet points
#A bullet point must be under a main heading, and must start with a dash
#A main heading doesn't start with a dash
#Empty lines do nothing
#Make sure to type in start , when you start the video
#You need to rename the chat file to input.txt
#This will produce an output named output.vtt
#This output file is a transcript file, which may be inserted into Closed Captioning in any video platform that supports closed captioning

#Options
incremental=True #Default is True

#Ignore the rest of this
def lpadd(a):
  if len(a)<2:
    return '0'+a
  return a
def subq(a,b):#a-b
  ac=int(a[:2])*3600
  ad=int(a[3:5])*60
  ae=int(a[6:8])
  bc=int(b[:2])*3600
  bd=int(b[3:5])*60
  be=int(b[6:8])
  af=ac+ad+ae
  bf=bc+bd+be
  o=af-bf
  oa=o//3600
  ob=(o//60)%60
  oc=o-((oa*3600)+(ob*60))
  return lpadd(str(oa))+':'+lpadd(str(ob))+':'+lpadd(str(oc))+'.000'
f=open('input.txt','r')
data=f.read()
f.close()
vlen=input('Please enter the video length in hh:mm:ss : ')+'.000'.lstrip().rstrip()
o='WEBVTT\n\n'
ltime='00:00:00.000'
q=1
stt='00:00:00.000'
u=''
lines=data.splitlines()
for line in lines:
  line=line.rstrip().lstrip()
  if len(line)>0:
    i=line.find('	')
    r=line.rfind(':')
    namen=line[i+1:r]
    timen=line[:i]+'.000'
    linen=line[r+2:]
    if linen[:1]=='-':
      if incremental:
        o+=subq(timen,stt)+'\n'+u+'\n'
        u+=linen+'\n'
        o+=str(q)+'\n'+subq(timen,stt)+' --> '
        q+=1
      else:
        u+=linen+'\n'
    else:
      if linen.lower()=='start':
        stt=timen
        q=0
      elif len(u)==0:
        o+=str(q)+'\n'+ltime+' --> '
        u=linen+'\n'
        ltime=timen
      else:
        o+=subq(timen,stt)+'\n'+u+'\n'
        u=linen+'\n'
        o+=str(q)+'\n'+subq(timen,stt)+' --> '
        ltime=timen
      q+=1
o+=vlen+'\n'+u[:-1]
f=open('output.vtt','w')
f.write(o)
f.close()
print('Done')