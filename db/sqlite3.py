class SQLite3Database:
    def __init__(self, db_file):
        # Connect to the database
        self.connection = sqlite3.connect(db_file)

        # Create tables if they don't exist
        self.create_tables()

    def create_tables(self):
        # Define the tables to be created
        CREATE_TABLES = [
            "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)",
            "CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, total FLOATING POINT)",
            # Add more tables as needed
        ]

        # Execute the create table statements
        for create_table in CREATE_TABLES:
            self.connection.execute(create_table)

    def add_user(self, name):
        # Create a new user entry in the users table
        self.connection.execute("INSERT INTO users (name) VALUES (?)", (name,))

    def get_users(self):
        # Return a list of all user entries in the users table
        return self.connection.query("SELECT * FROM users")

    def add_order(self, user_id, total):
        # Create a new order entry in the orders table
        self.connection.execute("INSERT INTO orders (user_id, total) VALUES (?, ?)", (user_id, total))

    def get_orders(self):
        # Return a list of all order entries in the orders table
        return self.connection.query("SELECT * FROM orders")

    def close(self):
        # Close the database connection
        self.connection.close()
