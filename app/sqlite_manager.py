import sqlite3


def create_table():
    connection = None
    cursor = None
    try:
        connection = sqlite3.connect("db_hw15.db")
        cursor = connection.cursor()

        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='people'")
        result = cursor.fetchone()

        # Create table if it doesn't exist
        if not result:
            cursor.execute(
                """CREATE TABLE people
                                 (person_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                  contact_name TEXT NOT NULL UNIQUE,
                                  numeral_value INTEGER NOT NULL )"""
            )
            connection.commit()

    except sqlite3.Error as error:
        print(f"Error with DB connection: \n{error}\n")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def check_user_and_add(contact_name, numeral_value):
    connection = None
    cursor = None
    try:
        conn = sqlite3.connect("db_hw15.db")
        cur = conn.cursor()

        print(f"Name: {contact_name}")
        print(f"Numb: {numeral_value}")

        sql_check = """
        SELECT contact_name, numeral_value FROM people;
        """

        # Return all DB lines (List of Tuples):
        res = cur.execute(sql_check)
        db_content = res.fetchall()

        # usr = one Tuple at a Time
        # usr[0] or "elm in usr" = first cell of every Tuple

        for usr in db_content:
            print(f"Show next tuple: {usr}")
            print(f"Show next tuple: {usr[0]}\n")
            if usr[0] == contact_name and usr[1] == numeral_value:
                return True
        return False

    except sqlite3.Error as error:
        print(f"Error checking User: \n{error}\n")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def put_user_info(contact_name, numeral_value):
    connection = None
    cursor = None
    try:
        connection = sqlite3.connect("db_hw15.db")
        cursor = connection.cursor()

        sql_put = """
        INSERT INTO phones (contact_name, numeral_value)
        VALUES(?, ?)
        """

        cursor.execute(sql_put, (contact_name, numeral_value))
        connection.commit()

    except sqlite3.Error as error:
        print(f"Error with DB connection: \n{error}\n")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
