

from db import cur, conn
from utils import BadRequest, Response
from validator import find_users_id,return_users_phone


def search_product(ipt):
    query = """select * from products where category ilike %s  or brand ilike  %s  or character ilike %s; """
    data = ('%' + ipt + '%',) * 3
    cur.execute(query,data)
    products = cur.fetchall()
    if not products:
        return False
    return products


def show_cart():
    query = """SELECT * FROM cart where user_id = %s ;"""
    data = find_users_id()
    cur.execute(query,data)
    products = cur.fetchall()
    if products:
        return products
    return False


def show_categories():
    query = """SELECT distinct category from products;"""
    cur.execute(query)
    products = cur.fetchall()
    if products:
        return products
    else:
        return False

def show_products_by_category(category):
    query = """Select distinct  * from products where category = %s;"""
    data = (category,)
    cur.execute(query,data)
    products = cur.fetchall()
    if products:
        return products
    else:
        return False



def create_order(product):

    query = """INSERT INTO orders(product_id,users_id)
               VALUES(%s,%s);"""
    user_id = find_users_id()
    product_id = product[0]
    data = (product_id,user_id[0])
    cur.execute(query,data)
    conn.commit()
    response = Response(message='Order successfully created ')
    print(response.message)

def save_to_card(product):
 try:
    query = """INSERT INTO cart(category,brand,character,user_id,product_id,price)
               VALUES(%s,%s,%s,%s,%s,%s);"""
    user_id = find_users_id()
    data = (product[1],product[2],product[3],user_id[0],product[0],product[5])
    cur.execute(query,data)
    conn.commit()
    response = Response(message='Product successfully save to cart ')
    print(response.message)
 except Exception as e:
     print('This product already in your cart')



def order():
    query = """select o.id,u.phone_number,u.first_name,p.category,p.brand,o.created_at
               from orders o join users u on o.users_id = u.id join products p on o.product_id = p.id;"""
    cur.execute(query)
    products = cur.fetchall()
    for product in products:
        print(f"""id:{product[0]} phone:{product[1]} name: {product[2]} category:{product[3]} brand:{product[4]} created_at{product[5]}""")




# def add_product(data):
#     query = """INSERT INTO products(category,brand,character,stock,price,description)
#                VALUES(%s,%s,%s,%s,%s,%s); """
#     datas = data
#     cur.execute(query,datas)
#     conn.commit()
#     print('data successfully added')
# category = 'phone'
# brand = 'Samsung S24'
# character = '256 gb'
# stock = 15
# price = 1200
# description = 'Nice'
# data = (category,brand,character,stock,price,description)
# add_product(data)
