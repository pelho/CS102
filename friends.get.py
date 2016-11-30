import requests
import datetime

domain = "https://api.vk.com/method"
access_token = "5ff56e0da021af79831376bbec7a3b2f4668629ec66c2968b268230ab9a5e9a853f3085b481384a3243e2"
user_id = "87103988"
query_params = {
    'domain' : domain,
    'access_token': access_token,
    'user_id': user_id,
    'fields': 'bdate'


}

query = "{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.53".format(**query_params)
response = requests.get(query)

def avg(list):
    return sum(list)/len(list)


def age_predict(user_id):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    response = requests.get(query)
    age = []
    for item in response.json()['response']['items']:
        if 'bdate' in item:
            age.append(item['bdate'])
        continue
    ages_with_years = []
    int_ages = []
    for value in age:
        if value.count('.') == 2:
            ages_with_years.append(value[-4:])
    return ages_with_years
    # for x in ages_with_years:
    #     int_ages.append(2016 - int(x))
    # return avg(int_ages)



