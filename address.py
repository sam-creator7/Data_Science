phone_book = {}

phone_book['sam'] ={
    'name': 'sam',
    'address': 'ind',
    'phone': 444
}

phone_book['sampu'] ={
    'name': 'sampu',
    'address': 'nep',
    'phone': 000
}

import json
s=json.dumps(phone_book)
print(phone_book)

with open("/Users/samarthmengji/Desktop/book.txt","w") as f:
    f.write(s)