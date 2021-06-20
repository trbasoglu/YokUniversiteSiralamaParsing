import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_aciklama(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO aciklamalar(aciklama_kodu,aciklama)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid





def main():
  
    ozel_aciklama_file = open("ozel_aciklamalar2020.txt", "r",encoding="utf-8")

    content = ozel_aciklama_file.read()

    database = r"YOK2020.db"
    conn = create_connection(database)
    with conn:
        # create a new project
        
            for madde in content.split("Bk. "):
                madde_kodu = str(madde.split(" ")[0])
                if not madde_kodu.isnumeric():
                    madde_kodu = madde.split("\n")[0]
                madde = madde[len(madde_kodu)+1:len(madde)]
                print(f"{madde_kodu}:{madde}")
                try:
                    project_id = create_aciklama(conn, (madde_kodu,madde))
                except:
                    continue
        
    conn.close()
if __name__ == '__main__':
    main()
