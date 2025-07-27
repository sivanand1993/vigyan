import sqlite3

class DBbase:
    _conn = None
    _cursor = None

    def __init__(self,db_name):
        self._db_name=db_name

    def connect(self):
        self._conn=sqlite3.connect(self._db_name)
        self._cursor=self._conn.cursor()

    def execute_script(self,sql_string):
        self._cursor.executescript(sql_string)

    @property
    def get_cursor(self):
        return self._cursor

    @property
    def get_connection(self):
        return self._conn

    def close_db(self):
        self._conn.close()

class Parts(DBbase):
    def __init__(self):
        super().__init__("inventoryDB.sqlite")
        self.connect()

    def update(self, part_id, name):
        try:
            super().connect()
            super().get_cursor.execute("""update parts set name=? where id=?;""", (name,part_id,))
            super().get_connection.commit()
            super().close_db()
            print("updated part successfully")
        except Exception as e:
            print("An error occurred.", e)



    def add(self, name):
        try:
            super().connect()
            super().get_cursor.execute("""insert or ignore into parts (name) values(?);""",(name,))
            super().get_connection.commit()
            super().close_db()
            print("added part successfully")
        except Exception as e:
            print("An error occurred.",e)

    def delete(self, part_id):
        try:
            super().connect()
            super().get_cursor.execute("""delete from parts where id=?;""",(part_id,))
            super().get_connection.commit()
            super().close_db()
            print("deleted part successfully")
        except Exception as e:
            print("An error occurred.", e)


    def fetch(self, part_id=None):
        try:
            super().connect()
            if part_id is not None:
                return super().get_cursor.execute("""SELECT * FROM parts WHERE id=?; """, (part_id,)).fetchall()
            else:
                return super().get_cursor.execute("""SELECT * FROM parts ;""").fetchall()
            # if Id is null (or None), then get everything, else get by id
        except Exception as e:
            print("An error occurred.", e)
        finally:
            super().close_db()

    def reset_database(self):
       sql= """DROP TABLE IF EXISTS Parts;
               CREATE TABLE Parts(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
               name TEXT UNIQUE
               );"""
       super().execute_script(sql)

class Inventory(DBbase):
    def __init__(self):
        super().__init__("inventoryDB.sqlite")
        self.connect()

    def update(self, id,qty,price):
        try:
            super().connect()
            super().get_cursor.execute("""update Inventory set quantity=?,current_price=? where id=?;""", (qty,price,id,))
            super().get_connection.commit()
            super().close_db()
            print("updated part successfully")
            return True
        except Exception as e:
            print("An error occurred.", e)
            return False



    def add(self,part_id,qty,current_price):
        try:
            super().connect()
            super().get_cursor.execute("""insert or ignore into Inventory (part_id,quantity,current_price) values(?,?,?);""",(part_id,qty,current_price,))
            super().get_connection.commit()
            super().close_db()
            print("added inventory successfully")
        except Exception as e:
            print("An error occurred.",e)

    def delete(self, id):
        try:
            super().connect()
            super().get_cursor.execute("""delete from Inventory where id=?;""",(id,))
            super().get_connection.commit()
            super().close_db()
            print("deleted part successfully")
        except Exception as e:
            print("An error occurred.", e)


    def fetch(self, part_id=None):
        try:
            super().connect()
            if part_id is not None:
                return super().get_cursor.execute("""SELECT * FROM Inventory WHERE id=?; """, (part_id,)).fetchall()
            else:
                return super().get_cursor.execute("""SELECT * FROM Inventory ;""").fetchall()
            # if Id is null (or None), then get everything, else get by id
        except Exception as e:
            print("An error occurred.", e)
        finally:
            super().close_db()

    def reset_database(self):
       sql= """DROP TABLE IF EXISTS Inventory;
               CREATE TABLE Inventory(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
               part_id INTEGER NOT NULL,
               quantity INTEGER NOT NULL,
               current_price varchar(20),
               FOREIGN KEY(part_id) REFERENCES parts(id)
               );"""
       super().execute_script(sql)

parts=Parts()
parts.reset_database()
results=parts.fetch()
print("Datbase creation \n\r",results)
parts.add("Pepsi")
parts.add("Mountain Dew")
parts.add("Rockstar")
parts.add("Spark Plugs")
parts.add("Oil Filters")
parts.add("iPhone")
results=parts.fetch()
print("After insertion \n\r",results)
parts.update(6,"iPad")
results=parts.fetch()
print("After updation \n\r",results)
parts.delete(1)
results=parts.fetch()
print("After deletion \n\r",results)
parts.close_db()

inventory=Inventory()
inventory.reset_database()
results=inventory.fetch()
print("Datbase creation \n\r",results)
inventory.add(1,10,"2.99")
inventory.add(2,12,"2.99")
inventory.add(3,5,"10.00")
results=inventory.fetch()
print("After insertion \n\r",results)
inventory.update(3,8,"1.00")
results=inventory.fetch()
print("After updation \n\r",results)
inventory.delete(3)
results=inventory.fetch()
print("After deletion \n\r",results)
results=inventory.fetch(2)
print("Retrieving 2nd record \n",results)
inventory.close_db()