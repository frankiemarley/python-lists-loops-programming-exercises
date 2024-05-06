incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

def data_transformer(ajax_data):
   
    return list(map(lambda x: f"{x['name']} {x['last_name']}", ajax_data))

print(data_transformer(incoming_ajax_data))

