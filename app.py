from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


domain_search = []
output = []
inputt = []

api_key = 'key to be added here.'
api_secret = 'secret to be added here'
headers = {"Authorization" : "sso-key {}:{}".format(api_key, api_secret)}



@app.route("/")
def home():
    return render_template("index.html")

def const():
    domain_search.clear()
    output.clear()
    inputt.clear()
    
@app.route("/", methods = ['POST'])
def show_text():
    const()
    text = request.form['u']
    domain_search.append(text)

    text = request.form['v']
    domain_search.append(text)

    text = request.form['w']
    domain_search.append(text)
    #print (type(text))
    #return text
    #return (text)
    inputt.append(domain_search[0])
    inputt.append(domain_search[1])
    inputt.append(domain_search[2])

    url = "https://api.godaddy.com/v1/domains/suggest"
    print ('\n')
    for i in domain_search:
        flag=0
        my_domain = requests.get(url, params={'query':i}, headers=headers).text #query to find the domains
        to_strin = json.loads(my_domain)  #converting JSON to Strings.
        print ("These domains are available!")
        for i in to_strin:
            print (i["domain"])
            output.append(i['domain'])
            flag+=1
            if (flag == 5):
                break

        print ('\n\n')
    return render_template("output.html", data=output)
    #print ("I am herjfdjkldfsjlkfds")
    

#app.run(debug=True, host="127.0.0.1", port =3000)
if __name__== '__main__':
    app.run()
