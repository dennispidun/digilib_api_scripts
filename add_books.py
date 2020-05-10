import json
import random
import string

import requests

api_base_url = 'http://localhost:8080/api/'


def login():
    api_url = '{0}login?username=admin&password=password'.format(api_base_url)

    response = requests.post(api_url)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['token']
    else:
        return None


token = login()
headers = {'Content-Type': 'application/json', 'Authorization': token}


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength)).upper()


def register_book(isbn, title, author, invnr):
    api_url = '{0}books'.format(api_base_url)
    json_data = json.dumps({'title': title, 'isbn': isbn, 'invnr': invnr, 'author': author})
    requests.post(api_url, headers=headers, data=json_data)


def register_books():
    books = open('books.csv', 'r')
    Lines = books.readlines()
    count = 0
    for line in Lines:
        book = line.strip().replace('"', '').split(',')
        # print("{0}: {1},{2}".format(randomString(10), book[0], book[1]))
        register_book(book[0], book[1], randomString(5), randomString(10))


register_books()
print("done")
