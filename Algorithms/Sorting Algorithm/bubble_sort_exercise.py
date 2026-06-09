elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

for i in elements:
    print (i)
    

def sorting (elements,key):
    size = len(elements)
    for i in range (size -1):
        for j in range (size-1-i):
            if elements[j+1][key]>elements[j][key]:
                elements[j],elements[j+1]=elements[j+1],elements[j]

sorting(elements  , 'name')

print ('After sorting : ')
for i in elements:
    print (i)