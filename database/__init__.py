

def spinup_db_instance(db_conf):
    if db_conf['Type'] == "SQLITE":
        from database.sqlite_database import SQLiteDatabase
        # get db_instance
        db_instance = SQLiteDatabase.get_db_instance(db_conf['Schema'])
        # run create scripts
        with open('sql/sqlite_ddl.sql') as ddl_file:
            ddl_scripts = ddl_file.read()
        with db_instance.conn as conn:
            conn.executescript(ddl_scripts)
        # return db_instance
        return db_instance

    if db_conf['Type'] == 'Oracle':
        from database.oracle_database import OracleDatabase
        assert 'ConnectIdentifier' in db_conf, 'Oracle Database requires an Connect Identifier'
        assert 'OracleHome' in db_conf, 'Oracle Database requires an Oracle Home'
        assert 'OracleSchema' in db_conf, 'Oracle Database requires an Schema'

        return OracleDatabase(oracle_home=db_conf['OracleHome'], connect_identifier=db_conf['ConnectIdentifier'],
                              oracle_schema=db_conf['OracleSchema'], tns_admin=db_conf.get('TNSConfig', None))