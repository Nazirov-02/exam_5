
from auth import log_or_reg, log_out
from service import search_product, show_cart, show_categories, show_products_by_category, create_order, save_to_card, \
    order
from utils import Response, BadRequest
from validator import check_phone, find_users_id


def log_or_reg_response():
    phone_number = input("Enter your phon number: ")
    if not check_phone(phone_number):
        response = Response(
            message="Invalid phone number please check and try again ! \n phone number must be like +998991234567")
        print(response.message)
        main()
    password = input('Enter your password: ')
    response = log_or_reg(phone_number, password)
    print(response.message)
    main()

def search_product_response():
    data = input("Enter what you search: ")
    if not search_product(data):
        response = Response(message='There is no any product like this !')
        print(response.message)
        main()
    products = search_product(data)
    counter = 1
    for product in products:
        print(f"{counter}) Id: {product[0]} brand: {product[2]} character: {product[3]} price: {product[5]}")
        counter += 1
    main()


def show_cart_response():
    products = show_cart()
    if products:
        counter = 1
        for product in products:
            print(f"{counter}) Id: {product[0]} brand: {product[2]} character: {product[3]} price: {product[6]}")
            counter += 1
        main()
    response = BadRequest(message="There is not any products yet !")
    print(response.message)
    main()








def show_all_categories():
     products = show_categories()
     if products:
         counter = 1
         for product in products:
             print(f"{counter}. {product[0]}")
             counter += 1
         print("0. back")
         choice = input("""
         >>>: """)
         if choice == '0':
           main()
         else:
             category = int(choice) - 1
             print(category)
             data = show_products_by_category(products[category])
             counter = 1
             for row in data:
                 print(f"{counter}. category:{row[1]} brand:{row[2]} character:{row[3]} stock:{row[4]} price:{row[5]} description:{row[6]} created_at:{str(row[7])[:11]}")
                 counter += 1
             order_or_cart(data)
             main()
     response = BadRequest(message="There is not any products yet !")
     print(response.message)
     main()


def order_or_cart(products):
    choice = input("""
    choice one >>>: """)
    request = input(f"""
    1.Create order
    2.Save to cart
    0.back
    >>>:  """)
    num = int(choice) - 1
    if request == '1':
        create_order(products[num])
    elif request == '2':
        save_to_card(products[num])
    elif request == '0':
        show_all_categories()
    else:
        return BadRequest(message='Wrong choice !')




def main():
    choice = input("""
            Online market
      1.Log in
      2.Search product
      3.Check cart
      4.Search by category
      5.Show all orders 
      6.Log out
      >>>: """)
    if choice == '1':
      log_or_reg_response()
    elif choice == '2':
        search_product_response()
    elif choice == '3':
        show_cart_response()
    elif choice == '4':
        show_all_categories()
    elif choice == '5':
        order()
        main()
    elif choice == '6':
        log_out()

if __name__=="__main__":
    main()