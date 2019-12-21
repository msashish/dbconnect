import sqlite3
import logging

sqlite3.paramstyle = "named"


class Database:
    """Base DB class"""

    def __init__(self, conn):
        self.conn = conn
        self.logger = logging.getLogger(self.__class__.__name__)

    # Metadata interface
    def get_table_names(self, **kwargs):
        return self.select('APP_DB.SQLITE_MASTER', kwargs)

    # Customer table related interfacing methods
    def select_many_customers(self, **kwargs):
        pass

    def select_one_customer(self, **kwargs):
        pass

    def insert_customer(self, **kwargs):
        pass

    def update_customer(self, cust_id, **kwargs):
        pass

    def delete_customer(self, cust_id, **kwargs):
        pass

    # Location table related interfacing methods
    def select_many_locations(self, **kwargs):
        pass

    def select_one_location(self, **kwargs):
        pass

    def insert_location(self, **kwargs):
        pass

    def update_location(self, location_id, **kwargs):
        pass

    def delete_location(self, location_id, **kwargs):
        pass

# Customer-Location table related interfacing methods
    def select_many_customer_locations(self, **kwargs):
        pass

    def select_one_customer_location(self, **kwargs):
        pass

    def insert_customer_location(self, **kwargs):
        pass

    def update_customer_location(self, customer_location_id, **kwargs):
        pass

    def delete_customer_location(self, customer_location_id, **kwargs):
        pass

    # Atomic low level methods
    def select(self, table, where_hash=None, limit=1000):

        if where_hash is None:
            where_hash = {}

        where_placeholders = '\nAND '.join(
            [f"{k} = :{k}" for k, v in where_hash.items()])
        if len(where_placeholders) > 0:
            where_placeholders = "WHERE\n" + where_placeholders
        sql = f"SELECT * FROM {table} {where_placeholders}"  # nosec

        crsr = self.conn.cursor()

        try:
            crsr.execute(sql, where_hash)
            rows = crsr.fetchmany(limit)

            name_column_idx = 0
            col_names = [column_meta[name_column_idx].upper() for column_meta in crsr.description]
        finally:
            crsr.close()
        return [dict(zip(col_names, row)) for row in rows]

    def select_one(self, table, where_hash=None):

        if where_hash is None:
            where_hash = {}

        where_placeholders = '\nAND '.join(
            [f"{k} = :{k}" for k, v in where_hash.items()])
        if len(where_placeholders) > 0:
            where_placeholders = "WHERE\n" + where_placeholders
        sql = f"SELECT * FROM {table} {where_placeholders}"

        crsr = self.conn.cursor()
        crsr.execute(sql, where_hash)

        rows = crsr.fetchmany(2)
        if len(rows) == 0:
            raise Exception(
                "No rows returned for sql:\n{}\nvalues:\n{}".format(sql, str(where_hash)))
        if len(rows) > 1:
            raise Exception(
                "More than 1 rows returned for sql:\n{}\nvalues:\n{}".format(sql, str(where_hash)))

        name_column_idx = 0
        col_names = [column_meta[name_column_idx].upper() for column_meta in crsr.description]
        crsr.close()
        first_row = rows[0]
        return dict(zip(col_names, first_row))