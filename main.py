import requests
import json
a=[]
s=0
response = requests.get('https://randomuser.me/api/')

if response.status_code == 200:
    content = response.content
    data = json.loads(content.decode())
# user={"fulname":data["results"][0]['first']+' '+data["results"][0]['first']}
randomuser=data["results"][0]
for i in randomuser:
    a.append({"fulname":i["name"]["first"]+i["name"]["last"],
               "email":i["email"],
               "phone":i["phone"]})
    s+=1
b=open("users.json","w")
b.write(json.dumps(a,indent=4))