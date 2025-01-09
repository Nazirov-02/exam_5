import psycopg2


from utils import Response


db_info = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'KA1275147',
    'database': 'exam_5',
    'port': 5432
}

conn = psycopg2.connect(**db_info)
cur = conn.cursor()


def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        conn.commit()
        return result
    return wrapper


def is_authenticated():
    pass


@commit
def create_table_user():
    query = '''CREATE TABLE IF NOT EXISTS users(
            id serial primary key ,
            phone_number varchar(30),
            password text,
            first_name varchar(200),
            last_name varchar(30),
            login_try_count int default 0,
            role varchar(20),
            created_at timestamp default current_timestamp
    );'''

    cur.execute(query)
    return Response(201, 'Users table created')


@commit
def create_table_products():
    query = '''CREATE TABLE IF NOT EXISTS products(
        id serial primary key,
        category varchar(100),
        brand varchar(30) unique,
        character text,
        stock int,
        price numeric,
        description text,
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP

    );
    '''
    cur.execute(query)
    return Response(201, 'products table  created')
@commit
def created_table_orders():
    query = """CREATE TABLE IF NOT EXISTS orders(
    id serial primary key,
    product_id int references products(id) on delete cascade,
    users_id int references users(id) on delete cascade,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );"""
    cur.execute(query)
    return Response(201,'orders table created')

@commit
def create_cart_table():
    query = """CREATE TABLE IF NOT EXISTS cart(
    id serial primary key,
    category varchar(50),
    brand varchar(50) unique,
    character text,
    user_id int references users(id) on delete cascade,
    product_id int references products(id) on delete cascade,
    price numeric);"""
    cur.execute(query)
    return Response(201,message="cart table created")




# create = create_table_user()
# create_1 = create_table_products()
# create_2 = created_table_orders()
# create_3 = create_cart_table()
# print(create.message)
# print(create_1.message)
# print(create_2.message)
# print(create_3.message)