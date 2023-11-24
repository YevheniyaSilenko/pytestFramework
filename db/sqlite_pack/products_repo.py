from db.sqlite_pack._base_db_connector import BaseDbConnection


class ProductsRepo:
   def __init__(self, db_params):
        self._db = BaseDbConnection(db_params)
        self._table_name = 'PRODUCTS'

   def get_all(self):
        res = self._db.cursor.execute(f"SELECT * FROM {self._table_name}")
        return res.fetchall()

   def get_one_by_id(self, user_id: int):
        res = self._db.cursor.execute(f"SELECT * FROM {self._table_name} WHERE id={user_id}")
        emp = res.fetchone()
        return emp

   def insert_one(self, user_id: int, name: str, category: str, price: int, quantity: int, description: str):
        query_insert = f'''
                INSERT INTO {self._table_name} (id,name,category,price,quantity,description)
                VALUES ({user_id}, '{name}', '{category}', {price}, {quantity}, {description});
                '''
        self._db.cursor.execute(query_insert)
        self._db.conn.commit()

   def __del__(self):
        self._db.cursor.close()
        self._db.conn.close()