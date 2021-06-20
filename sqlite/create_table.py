import sqlite3
from sqlite3 import Error
isLisans = True

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"YOK2020.db"
    sql_create_tasks_table_lisans = """CREATE TABLE lisans(
                                    tercih_kodu integer PRIMARY KEY,
                                    bolum text NOT NULL,
                                    puan_turu text NOT NULL,
                                    universite text NOT NULL,
                                    fakulte text NOT NULL,
                                    ogrenim_suresi integer NOT NULL,
                                    siralama integer NOT NULL,
                                    puan floar NOT NULL,
                                    ogrenim_tipi text,
                                    burs_durumu text,
                                    kontenjan integer NOT NULL,
                                    aciklama text NOT NULL,
                                    FOREIGN KEY (universite) REFERENCES universiteler (isim)
                                );"""
    sql_create_tercihLisesi_table = """CREATE TABLE tercihListesi(
        tercih_kodu integer PRIMARY KEY,
        sira integer NOT NULL
    );"""
    sql_create_aciklamalar = """CREATE TABLE aciklamalar(
        aciklama_kodu integer PRIMARY KEY,
        aciklama text NOT NULL
    );"""
    sql_create_tasks_table_onlisans = """CREATE TABLE onlisans(
                                    tercih_kodu integer PRIMARY KEY,
                                    bolum text NOT NULL,
                                    puan_turu text NOT NULL,
                                    universite text NOT NULL,
                                    fakulte text NOT NULL,
                                    ogrenim_suresi integer NOT NULL,
                                    siralama integer NOT NULL,
                                    puan floar NOT NULL,
                                    ogrenim_tipi text,
                                    burs_durumu text,
                                    kontenjan integer NOT NULL,
                                    aciklama text NOT NULL,
                                    FOREIGN KEY (universite) REFERENCES universiteler (isim)
                                );"""
    if isLisans:
        # database = r"YOK2019_Lisans.db"
        sql_create_tasks_table = """CREATE TABLE bolumler (
                                    tercih_kodu integer PRIMARY KEY,
                                    bolum text NOT NULL,
                                    puan_turu text NOT NULL,
                                    universite text NOT NULL,
                                    fakulte text NOT NULL,
                                    ogrenim_suresi integer NOT NULL,
                                    siralama integer NOT NULL,
                                    puan floar NOT NULL,
                                    ogrenim_tipi text,
                                    burs_durumu text,
                                    kontenjan integer NOT NULL,
                                    aciklama text NOT NULL,
                                    prof_say integer NOT NULL,
                                    doc_say integer NOT NULL,
                                    ogr_gr_say integer NOT NULL,
                                    FOREIGN KEY (universite) REFERENCES universiteler (isim)
                                );"""
    else:
        # database = r"YOK20k19_OnLisans.db"
        sql_create_tasks_table = """CREATE TABLE bolumler (
                                    tercih_kodu integer PRIMARY KEY,
                                    bolum text NOT NULL,
                                    puan_turu text NOT NULL,
                                    universite text NOT NULL,
                                    fakulte text NOT NULL,
                                    ogrenim_suresi integer NOT NULL,
                                    siralama integer NOT NULL,
                                    puan floar NOT NULL,
                                    ogrenim_tipi text,
                                    burs_durumu text,
                                    kontenjan integer NOT NULL,
                                    aciklama text NOT NULL,
                                    FOREIGN KEY (universite) REFERENCES universiteler (isim)
                                );"""
    sql_create_projects_table = """ CREATE TABLE  universiteler (
                                        isim text PRIMARY KEY,
                                        sehir text NOT NULL,
                                        uni_tipi text NOT NULL
                                    ); """


    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # # create tasks table
        create_table(conn, sql_create_tasks_table_lisans)
        create_table(conn, sql_create_tasks_table_onlisans)

        # #createTercihListesiTable
        create_table(conn, sql_create_tercihLisesi_table)
        create_table(conn, sql_create_aciklamalar)
        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()