import requests
import json

domain_search = []
#taking inputs
for i in range (5):
    ii = str(input("Enter the domain values: "))
    domain_search.append(ii)
#api key and secret  generated from GoDaddy
api_key = 'dLDHUMRNZ45L_QPyhk5hY3MhNN14ZrUkAD1'
api_secret = 'QNhN1XaVVqG6nZ4AGkdKoa'
headers = {"Authorization" : "sso-key {}:{}".format(api_key, api_secret)}

def findmydomain():
    url = "https://api.godaddy.com/v1/domains/suggest"
    print ('\n')
    for i in domain_search:
        flag=0
        my_domain = requests.get(url, params={'query':i}, headers=headers).text #query to find the domains
        to_strin = json.loads(my_domain)  #converting JSON to Strings.
        print ("These domains are available!")
        for i in to_strin:
            print (i["domain"])
            flag+=1
            if (flag == 5):
                break

        print ('\n\n')


findmydomain()