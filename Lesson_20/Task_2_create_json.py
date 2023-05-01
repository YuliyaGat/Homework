import json

with open('phonebook.json', 'w') as book:
    book_start=[{'first name':'Victor','last name':'Brown','telephone number':'+380503254050','city':'Lviv','state':'Ukraine'},{'first name':'Olena','last name':'Ivasenko','telephone number':'+380673254052','city':'Krakow','state':'Poland'}]
    json.dump(book_start, book, indent=4)
