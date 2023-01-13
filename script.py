import os,shutil
bms=os.listdir()
bgpath=os.path.abspath( __file__ )[0:-9]+'/bg.jpg'

def disable():
    for bm in bms:
        files=os.listdir(bm)
        imgs=filter(lambda x: x.endswith(('.jpeg','.jpg','.png')),files)
        for img in imgs:
            shutil.copy(os.path.join(bm,img),os.path.join(bm,img+'.bak'))
            shutil.copy(bgpath,os.path.join(bm,img))

def enable():
    for bm in bms:
        files=os.listdir(bm)
        imgs=filter(lambda x: x.endswith(('.jpeg','.jpg','.png')),files)
        for img in imgs:
            shutil.copy(os.path.join(bm,img+'.bak'),os.path.join(bm,img))          


ch=input('Enable(e) or Disable(d)? : ')
if(ch=='e'):
    enable()
elif(ch=='d'):
    disable()