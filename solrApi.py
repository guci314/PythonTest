from SolrClient import SolrClient
import requests
import os
class SolrApi(SolrClient):
    def __init__(self,host):
        #self.suffixs=["md","xml","txt","scala","java","cs","ts","js","ipynb","py","php","rtf","rdf","cpp","c","h","json","csv","ppt","pptx","ots","odt","odp","ods","ott","otp","pdf","html","sbt","docx","doc","xls","xlsx"]
        SolrClient.__init__(self,host)
        self.suffixs=["md","txt","rtf","ppt","pptx","ots","odt","odp","ods","ott","otp","pdf","html","docx","doc","xls","xlsx"]
    def func(self):
        print(self.host)
    def postFile(self,collection,file):
        posturl = self.host+"/"+collection+"/update/extract"
        p={}
        p["commit"]="false"
        p["literal.id"]=file
        p["literal.attr_resourcename"]=file
        suffix=os.path.splitext(file)[1]
        suffix=suffix.strip(".")
        p["literal.suffix"]=suffix
        try:
            payload = open(file, "rb").read()
            r = requests.post(posturl, data=payload, params=p)
            return r
        except Exception as e:
            print(e)
    def getAllId(self,collection):
        ids=[]
        for res in self.cursor_query(collection,{'q':'*:*','fl':'id'}):
            for doc in res.docs:
                ids.append(doc['id'])
        return ids

    def indexFolder(self,collection,folder):
        '''
        索引文件夹
        '''
        
        #suffixs=[".java"]
        counter=0
        for dirpath, dirnames, filenames in os.walk(folder):
            for filepath in filenames:
                name=os.path.join(dirpath, filepath)
                suffix=os.path.splitext(name)[1]
                suffix=suffix.strip(".")
                try:
                    i=self.suffixs.index(suffix)
                    self.postFile(collection,name)
                    counter=counter+1
                    if (counter % 500 == 0):
                        self.commit(collection)
                        print(counter)
                except Exception as e:
                    pass
        self.commit(collection)

solr=SolrApi('http://127.0.0.1:8983/solr')
solr.indexFolder('files','/home/guci/share/baidunetdisk')
print('finished')
