from SolrClient import SolrClient
import requests
import os
class SolrApi(SolrClient):
    def func(self):
        print(self.host)
    def postFile(self,collection,file):
        posturl = self.host+"/"+collection+"/update/extract"
        p={}
        p["commit"]="true"
        p["literal.id"]=file
        p["literal.attr_resourcename"]=file
        suffix=os.path.splitext(file)[1]
        suffix=suffix.strip(".")
        p["literal.suffix"]=suffix
        try:
            payload = open(file, "rb").read()
            r = requests.post(posturl, data=payload, params=p)
            return r
        except e:
            print(e)
    def getAllId(self,collection):
        ids=[]
        for res in self.cursor_query(collection,{'q':'*:*','fl':'id'}):
            for doc in res.docs:
                ids.append(doc['id'])
        return ids
