import requests
result=requests.get('https://api.github.com/users/{}/events/public'.format(input('Enter Github Username: ')))
json_result=result.json()
final=set()
for x in json_result:
    if x['payload'].get('commits'):
        final.add(x['payload']['commits'][0]['author']['email'])
for mail in final:
    print(mail)

