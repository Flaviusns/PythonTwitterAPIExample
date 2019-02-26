import base64
import requests
import pprint



print("Welcome to this Python Twitter API script")

client_key = input("Insert your client key: ")
client_secret = input("Insert your secret client key: ")
key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')



base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

if str(auth_resp.status_code) == '200':
    print("Correct credentials")
print(auth_resp.status_code)



access_token = auth_resp.json()['access_token']

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
}

search_key = input("Insert search key: ")
count_elements = input("Select how many response do you want: ")
result_type = input("Select:  mixed | recent | popular ")
lang = input("Select language (ISO 639-1): ")
search_params = {
    'q': search_key,
    'count': count_elements,
    'result_type': result_type,
    'lang': lang
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

tweet_data = search_resp.json()

pprint.pprint(tweet_data)