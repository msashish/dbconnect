from pathlib import Path


def spinup_db_instance(db_conf):
    if db_conf['Type'] == "SQLITE":
        from application.database.sqlite_database import SQLiteDatabase
        import sqlite3
        sqlite3.paramstyle = "named"
        # get SQLite db_instance and run scripts to create structures
        db_instance = SQLiteDatabase(db_conf['Schema'])
        if Path('sql/sqlite_ddl.sql').is_file():
            db_instance.run_scripts('sql/sqlite_ddl.sql')
        else:
            print("No DDL file for creating structures for you in SQLite. Check and rerun..")

    if db_conf['Type'] == 'Oracle':
        from application.database import OracleDatabase
        assert 'ConnectIdentifier' in db_conf, 'Oracle Database requires an Connect Identifier'
        assert 'OracleHome' in db_conf, 'Oracle Database requires an Oracle Home'
        assert 'OracleSchema' in db_conf, 'Oracle Database requires an Schema'
        db_instance = OracleDatabase(oracle_home=db_conf['OracleHome'], connect_identifier=db_conf['ConnectIdentifier'],
                                     oracle_schema=db_conf['OracleSchema'], tns_admin=db_conf.get('TNSConfig', None))

    # return db_instance
    return db_instance