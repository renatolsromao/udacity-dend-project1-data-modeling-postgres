import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    Connect to default database, drop and re-create sparkify database.

    :return: cur, conn - Cursor for executing queries and Connection for commit
    """
    # connect to default database
    conn = psycopg2.connect("host=localhost dbname=default user=renato password=")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host=localhost dbname=sparkifydb user=renato password=")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """
    Drop tables using drop_tables_queries

    :param cur: Database Cursor
    :param conn: Databse Connection
    :return: None
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Create tables using create_table_queries

    :param cur: Database Cursor
    :param conn: Databse Connection
    :return: None
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
