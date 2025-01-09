
from db import  cur,conn
def add_product(data):
    query = """INSERT INTO products(category,brand,character,stock,price,description)
               VALUES(%s,%s,%s,%s,%s,%s); """
    datas = data
    cur.execute(query,datas)
    conn.commit()
    print('data successfully added')
category = 'phone'
brand = 'Samsung S23'
character = '256 gb'
stock = 15
price = 1200
description = 'Nice'
data = (category,brand,character,stock,price,description)
add_product(data)

category = 'phone'
brand = 'Iphone'
character = '256 gb'
stock = 15
price = 1200
description = 'Nice'
data = (category,brand,character,stock,price,description)
add_product(data)

category = 'Tv'
brand = 'artel'
character = ''
stock = 15
price = 400
description = 'Nice'
data = (category,brand,character,stock,price,description)
add_product(data)

category = 'Tv'
brand = 'Samsung'
character = ''
stock = 15
price = 1200
description = 'Nice'
data = (category,brand,character,stock,price,description)
add_product(data)

category = 'Computer'
brand = 'HP'
character = '256 gb'
stock = 15
price = 1200
description = 'Nice'
data = (category,brand,character,stock,price,description)
add_product(data)

category = 'computer'
brand = 'Ecer'
character = '256 gb'
stock = 15
price = 1200
description = 'Nice'
data = (category,brand,character,stock,price,description)
add_product(data)
