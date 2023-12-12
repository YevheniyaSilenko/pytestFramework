from constants import ROOT_PATH
from utilities.sqlite_cm import Sqlite

if __name__ == '__main__':
    with Sqlite(f'{ROOT_PATH}/db/test.db') as c:
        query_create = '''
        CREATE TABLE PRODUCTS  
        (id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        price REAL,
        quantity INTEGER,
        description TEXT);
        '''
        c.execute(query_create)

        query_insert = '''
        INSERT INTO PRODUCTS (id, name, category, price, quantity, description)
        VALUES(1, 'GUCCI', 'GLASSES', 5000, 7, 'WOMAN_GLASSES');
        '''
        c.execute(query_insert)

        res = c.execute("SELECT * FROM PRODUCTS")
        print(res.fetchall())



