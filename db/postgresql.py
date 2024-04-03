import psycopg2, json

class DataBase(object):
    pass


class PostgreSQLConnector:
    def __init__(self, host, port, dbname, username, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.username = username
        self.password = password
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.dbname,
            user=self.username,
            password=self.password
        )

    def create_table(self, table_name, columns):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE {} ({});".format(table_name, ', '.join(columns)))
        self.conn.commit()

    def insert_record(self, table_name, data):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO {} ({}) VALUES ({});".format(table_name, ", ".join(data),
                                                                 json.dumps(data)))
        self.conn.commit()

    def read_records(self, table_name):
        cursor = self.conn.cursor()
        result = cursor.execute("SELECT * FROM {}".format(table_name))
        return [dict(row) for row in result]

    def update_record(self, table_name, data, where_clause):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE {} SET {} WHERE {};".format(table_name, json.dumps(data),
                                                           where_clause))
        self.conn.commit()


    def delete_record(self, table_name, where_clause):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM {} WHERE {};".format(table_name, where_clause))
        self.conn.commit()


    def close(self):
        self.conn.close()


