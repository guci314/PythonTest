
#%%
# import moudules
from urllib.request import urlopen
import urllib.parse
import json
import urllib
from IPython.core.debugger import set_trace
import requests
import os

q=urllib.parse.quote("\"漂亮前女友\"")
conn = urlopen('http://127.0.0.1:8983/solr/files/select?q='+q+'&&wt=python')
response = eval(conn.read())
print(response['response']['numFound'], "documents found.")
# Print the name of each document.
x=response['response']['docs']
for document in response['response']['docs']:
  print ("  ResourceName =", document.get("attr_resourcename"))


#%%
#import tika
#tika.TikaClientOnly = True
#tika.initVM()
#from tika import parser
#from tika.tika import detectType1

def postFile(file):
    url = "http://localhost:8983/solr/files/update/extract"
    #t=detectType1(urlOrPath=file,option='type')[1]
    #print(t)
    
    #headers = {}
    #headers["content-type"]="text/plain" #parsed["metadata"]["Content-Type"]
    #suffix=os.path.splitext(file)[1]
    #suffix=suffix.strip(".")
    p={}
    p["commit"]="true"
    p["literal.id"]=file
    #p["literal.qqqq"]="dfdfd"
    p["literal.attr_resourcename"]=file
    #p["literal.ext"]=suffix
    #params={"commit":"true","literal.id":"/home/guci/temp/Serial.txt","literal.resourcename":"/home/guci/temp/Serial.txt"}
    #set_trace()
    try:
        payload = open(file, "rb").read()
        r = requests.post(url, data=payload, params=p)
    except e:
        print(e)
    #print("got back: %s" % r.text)

def indexFolder(folder):
    '''
    xml,json,jsonl,csv,pdf,doc,docx,ppt,pptx,xls,xlsx,odt,odp,ods,ott,otp,ots,rtf,htm,html,txt,java,scala,sbt,cs,js,ts,c,cpp,h,cs,py,ipynb,php,rdf 
    '''
    suffixs=["md","xml","txt","scala","java","cs","ts","js","ipynb","py","php","rtf","rdf","cpp","c","h","json","csv","ppt","pptx","ots","odt","odp","ods","ott","otp","pdf","html","sbt","docx","doc","xls","xlsx"]
    #suffixs=[".java"]
    for dirpath, dirnames, filenames in os.walk(folder):
        for filepath in filenames:
            name=os.path.join(dirpath, filepath)
            suffix=os.path.splitext(name)[1]
            suffix=suffix.strip(".")
            try:
                i=suffixs.index(suffix)
                postFile(name)
                print(name)
            except :
                pass
            
#postFile("/home/guci/temp/Serial.txt")
#indexFolder("/home/guci/share/baidunetdisk")
#indexFolder("/home/guci/projects")
#indexFolder("/home/guci/我的坚果云")
#indexFolder("/home/guci/gdrive/all/")
print("finished")


#%%
'''
curl -X POST -H 'Content-type:application/json' --data-binary '{
  "add-field":{
	 "name":"suffix",
	 "type":"string",
	 "docValues":true,
	 "stored":true }
}' http://localhost:8983/solr/test/schema
'''
def addSuffix(filename):
    suffix=os.path.splitext(filename)[1]
    suffix=suffix.strip(".")
    url = "http://localhost:8983/solr/files/update?commit=true"
    doc = [{'id': filename, 'suffix':{'set':suffix}}]
    try:
        r = requests.post(url, json=doc)
    except e:
        print(e)
        
def addSuffixInFolders(folder):
    '''
    xml,json,jsonl,csv,pdf,doc,docx,ppt,pptx,xls,xlsx,odt,odp,ods,ott,otp,ots,rtf,htm,html,txt,java,scala,sbt,cs,js,ts,c,cpp,h,cs,py,ipynb,php,rdf 
    '''
    suffixs=["md","xml","txt","scala","java","cs","ts","js","ipynb","py","php","rtf","rdf","cpp","c","h","json","csv","ppt","pptx","ots","odt","odp","ods","ott","otp","pdf","html","sbt","docx","doc","xls","xlsx"]
    #suffixs=[".java"]
    for dirpath, dirnames, filenames in os.walk(folder):
        for filepath in filenames:
            name=os.path.join(dirpath, filepath)
            suffix=os.path.splitext(name)[1]
            suffix=suffix.strip(".")
            try:
                i=suffixs.index(suffix)
                addSuffix(name)
                print(name)
            except :
                pass

#addSuffixInFolders("/home/guci/我的坚果云")
addSuffixInFolders("/home/guci/share/baidunetdisk")
addSuffixInFolders("/home/guci/projects")
addSuffixInFolders("/home/guci/gdrive/all/")
print('finished')


#%%
from baidupcsapi import PCS
pcs = PCS('guci314@gmail.com','guci700127')
print (pcs.quota().content)
#print (pcs.list_files('/').content)


#%%
def indexFile(file):
    print(file)
def listFolder(folder):
    print(folder)
    try:
        elements= json.loads(pcs.list_files(folder).content.decode())["list"] 
        #pcs.list_files('/',"name","asc").json().get("list")
        for element in elements:
            if element["isdir"]==1:
                listFolder(element["path"])
            else:
                indexFile(element["path"])
    except:
        pass


listFolder("/快盘/pda/backup/Books")


#%%
elements= json.loads(pcs.list_files("/快盘/pda/backup/Books").content.decode())["list"] 
for element in elements:
            if element["isdir"]==1:
                print("is dir")
                print(element["path"])
                #listFolder(element["path"])
            else:
                print("is file")
                print(element["path"])
                #indexFile(element["path"])


#%%

#/快盘/My Dropbox/document/humor/变态楼主和暴强回复.txt
#headers = {}
f="/快盘/pda/backup/Books/漂亮前女友.txt"
#f="/快盘/pda/backup/Books/Mind.Tools.Essential.Skills.pdf"
x=pcs.download(f).content #.decode(encoding='gbk').encode(encoding='utf8')
#x.content
url = "http://localhost:8983/solr/gettingstarted/update/extract"
p={}
p["commit"]="true"
p["literal.id"]=f
p["literal.resourcename"]=f
r = requests.post(url, data=x,params=p)
print("got back: %s" % r.text)
#filelist = pcs.list_files('/',"name","asc").json().get("list")
#filelist


#%%
import tika
tika.TikaClientOnly = True
tika.initVM()
from tika import parser
from tika.tika import detectType1

f="/快盘/pda/backup/Books/漂亮前女友.txt"
s=pcs.download(f).content.decode(encoding='gbk')
#bytes=pcs.download(f).content
f = open('/home/guci/temp/output.txt', 'wb')
f.write(s.encode('gbk'))
f.close()
#t=tika.tika.detectType1(urlOrPath='/home/guci/temp/output.txt',option="type")
#print(t)
postFile('/home/guci/temp/output.txt')
print("finished")


#%%
s='http://127.0.0.1:8983/solr/test/select?q=\"漂亮\"&fl=*'
r=requests.get(s)
j=json.loads(r.text)
d=j["response"]["docs"]
d[0]
#d[1]["attr_wwwwwww"]


#%%
'''
curl -X POST -H 'Content-type:application/json' --data-binary '{
  "add-field":{
	 "name":"tag",
	 "type":"string",
	 "stored":true }
}' http://localhost:8983/solr/test/schema
'''
url = "http://localhost:8983/solr/test/update?commit=true"
doc = [{'id': '/home/guci/我的坚果云/books/变态楼主.txt', 'attr_tag':{'add':'1111111111'}}]
r = requests.post(url, json=doc)
print("got back: %s" % r.text)


#%%
postFile("/home/guci/projects/PythonTest/Optimization using SciPy.ipynb")


