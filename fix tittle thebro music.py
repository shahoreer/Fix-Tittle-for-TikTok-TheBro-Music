import os
import random

#path
source_path_="/Users/shahoreertalha/Desktop/Work/TheBro Music/to be fix/"
done_path_="/Users/shahoreertalha/Desktop/Work/TheBro Music/fixed vids/"

#customizable variable
tittle_limit=150

#def
def loadfolder(path):
     arr=os.listdir(path)
     if arr.__contains__('.DS_Store'):
         arr.remove('.DS_Store')
     return arr

#program variable
all_vids=loadfolder(source_path_)
print(all_vids)

#def 2...
def cut_bywords_cahr_limit(string,limit):
    if len(string)>limit:
        string=string.split(" ")
        ret_str=""
        for i in string:
            if len(ret_str+i)>limit:
                return ret_str[1:]
            else:
                ret_str=ret_str+" "+i
    return string

def loadfolder(path):
     arr=os.listdir(path)
     if arr.__contains__('.DS_Store'):
         arr.remove('.DS_Store')
     return arr

def findfilenameandext(path):
     file_name = os.path.basename(path)
     return os.path.splitext(file_name)

def writetittle(path):
    name=findfilenameandext(path)

    add=" lyrics #TheBroMusic English Song #TheBro English Music "
    the_hastags="#newsong #pop #favoritesong #newmusic #happymusic #music #goodmusic #song"
    the_hastags=the_hastags.split(" ")
    random.shuffle(the_hastags)
    new_name=cut_bywords_cahr_limit(name[0]+add+" ".join(the_hastags),150)+name[1]
    print(len(new_name))
    return new_name

def change_tittle(old_name,new_name):
    os.rename(source_path_+old_name,done_path_+new_name)

#program starter
for i in all_vids:
    change_tittle(i,writetittle(i))