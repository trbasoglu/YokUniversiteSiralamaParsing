import sqlite3
from sqlite3 import Error
import csv


isLisans = False
universite_turleri = ['Devlet Üniversitesi','Vakıf Üniversitesi',]
iller = ['ADANA', 'ADIYAMAN', 'AFYONKARAHİSAR', 'AĞRI', 'AMASYA', 'ANKARA', 'ANTALYA', 'ARTVİN', 'AYDIN', 'BALIKESİR', 'BİLECİK', 'BİNGÖL', 'BİTLİS', 'BOLU', 'BURDUR', 'BURSA', 'ÇANAKKALE', 'ÇANKIRI', 'ÇORUM', 'DENİZLİ', 'DİYARBAKIR', 'EDİRNE', 'ELAZIĞ', 'ERZİNCAN', 'ERZURUM', 'ESKİŞEHİR', 'GAZİANTEP', 'GİRESUN', 'GÜMÜŞHANE', 'HAKKARİ', 'HATAY', 'ISPARTA', 'MERSİN', 'İSTANBUL', 'İZMİR', 'KARS', 'KASTAMONU', 'KAYSERİ', 'KIRKLARELİ', 'KIRŞEHİR', 'KOCAELİ', 'KONYA', 'KÜTAHYA', 'MALATYA', 'MANİSA', 'KAHRAMANMARAŞ', 'MARDİN', 'MUĞLA', 'MUŞ', 'NEVŞEHİR', 'NİĞDE', 'ORDU', 'RİZE', 'SAKARYA', 'SAMSUN', 'SİİRT', 'SİNOP', 'SİVAS', 'TEKİRDAĞ', 'TOKAT', 'TRABZON', 'TUNCELİ', 'ŞANLIURFA', 'UŞAK', 'VAN', 'YOZGAT', 'ZONGULDAK', 'AKSARAY', 'BAYBURT', 'KARAMAN', 'KIRIKKALE', 'BATMAN', 'ŞIRNAK', 'BARTIN', 'ARDAHAN', 'IĞDIR', 'YALOVA', 'KARABÜK', 'KİLİS', 'OSMANİYE', 'DÜZCE']
uniList = []
bolumler = []
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


def create_universite(conn, project):
    print(project)
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO universiteler(isim,sehir,uni_tipi)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_bolum(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    if isLisans:
        # sql = ''' INSERT INTO lisans(tercih_kodu,bolum,puan_turu,universite,fakulte,ogrenim_suresi,siralama, puan,ogrenim_tipi,burs_durumu, kontenjan, aciklama,prof_say,doc_say,ogr_gr_say)
        #         VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
        sql = ''' INSERT INTO lisans(tercih_kodu,bolum,puan_turu,universite,fakulte,ogrenim_suresi,siralama, puan,ogrenim_tipi,burs_durumu, kontenjan, aciklama)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''
    else:
        sql = ''' INSERT INTO onlisans(tercih_kodu,bolum,puan_turu,universite,fakulte,ogrenim_suresi,siralama, puan,ogrenim_tipi,burs_durumu, kontenjan, aciklama)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''  
    # print(project)
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

def delete_spaces(_str):
    while _str.startswith(' '):
        prev_len = len(_str)
        _str = _str[1:]
    while _str.endswith(' '):
        _str = _str[:-1]
    _str.replace("  ", " ")
    return _str

def  get_program_infos(program_adi):
    burs_durumları = ['Ücretli','%25 İndirimli', '%50 İndirimli', '%75 İndirimli','Burslu']
    ogrenim_tipleri = ['Uzaktan Öğretim','İÖ','Örgün','Açık Öğretim']

    ogrenim_tipi = "Örgün"
    burs_durumu = "Ücretsiz"

    for burs in burs_durumları:
        if burs in program_adi:
            program_adi = program_adi.replace(f"({burs})","")
            burs_durumu = burs
    
    for ogrenim in ogrenim_tipleri:
        if ogrenim in program_adi:
            ogrenim_tipi = ogrenim
    program_adi = delete_spaces(program_adi)
    return program_adi, ogrenim_tipi, burs_durumu
def read_csv():
    i = 0
    if isLisans:
        csv_file_name ='tablo4_21_07_20.csv'
    else:
        csv_file_name ='tablo3_21_07_2020.csv'
    with open(csv_file_name, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        universiteler = {}
        universite = None
        fakulteler = []
        fakulte = None
        bolumDict = {}
        keywords = []
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # CSV COLUMNS
                program_kodu = row[0]
                program_adi = row[1]
                ogrenım_suresı= row[2]
                puan_türü = row[3]
                kontenjan = row[4]
                okul_birinci_kont = row[5]
                if isLisans:
                    meb = row[6]
                    aciklamalar = row[7]
                    siralama = row[8] 
                    tbn_puanlar = row[9]
                    p_dr_say = row[10]
                    d_dr_say = row[11]
                    dr_ogr_say = row[12]
                else:
                    aciklamalar = row[6]
                    siralama = row[7]
                    tbn_puanlar = row[8]
                if(siralama=="..."):
                        siralama=-1
                if siralama=="****":
                    siralama=-2
                if siralama=="":
                    siralama=7000000   

                if len(program_kodu)==0 and "ÜNİVERSİTE" in program_adi:
                    universite = program_adi
                    uni_parts = universite.split('(')
                    uni_parts_number = len(uni_parts)
                    tur = None
                    konum = None
                    if uni_parts_number > 1:
                        uni_name = uni_parts[0]
                        for uni_part in uni_parts[1:]:
                            uni_part = uni_part.replace(')', '')
                            uni_part = delete_spaces(uni_part)
                            # if not uni_part in universite_turleri: 
                            #     universite_turleri.append(uni_part)
                            # if not uni_part in iller:
                            if uni_part in universite_turleri:
                                tur = uni_part
                            else:
                                konum = uni_part
                            if 'KKTC' in uni_part:
                                tur = 'KKTC'
                                konum = uni_part
                        if konum is None:
                            for il in iller:
                                il = il+' '
                                if il in uni_name:
                                    konum = il[:-1]
                        if tur is None:
                            tur = 'Yabancı'
                    if not uni_name in universiteler.keys():
                        universiteler[uni_name] = {"tür":tur,"konum":konum,}
                        uniList.append({'isim':uni_name, 'tür':tur, 'sehir':konum})
                    universite = uni_name
                    # print(universite)
                    fakulte = None
                elif fakulte is None or "Fakülte" in program_adi or "Yüksekokulu" in program_adi:
                    fakulte = program_adi
                    if not fakulte in fakulteler:
                        fakulteler.append(fakulte)
                    # print(f"\t{fakulte}")
                if len(program_kodu)>0:
                    program_adi, ogrenim_tipi,burs_durumu = get_program_infos(program_adi)
                    bolum_ismi = program_adi
                    if isLisans:
                        bolumler.append((program_kodu,
                        bolum_ismi,
                        puan_türü,
                        universite,
                        fakulte,
                        ogrenım_suresı,
                        siralama,
                        tbn_puanlar,
                        ogrenim_tipi,
                        burs_durumu,
                        kontenjan,
                        aciklamalar,
                        # p_dr_say,
                        # d_dr_say,
                        # dr_ogr_say
                        ))
                        bolumInstance = {
                            'tercih_kodu':program_kodu,'isim':bolum_ismi,"üniversite":universite,"fakülte":fakulte,"puan_türü": puan_türü,"kontenjan":kontenjan,"okul_birinci_kont":okul_birinci_kont, "aciklamalar":aciklamalar,"sıralama":siralama,"tbn_puanlar":tbn_puanlar,"prof say":p_dr_say,"doçent_sayısı":d_dr_say,"dr_ogr_say":dr_ogr_say}    
                   
                    else:
                        bolumler.append((program_kodu,
                        bolum_ismi,
                        puan_türü,
                        universite,
                        fakulte,
                        ogrenım_suresı,
                        siralama,
                        tbn_puanlar,
                        ogrenim_tipi,
                        burs_durumu,
                        kontenjan,
                        aciklamalar))
                    i+=1
                line_count += 1

def main():
    if isLisans:
        database = r"YOK2019_Lisans.db"
    else:
        database = r"YOK2019_OnLisans.db"

    database = r"YOK2020.db"
    read_csv()
    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        
            for uni in uniList:
                try:
                    universite = (uni["isim"], uni['sehir'],uni['tür'])
                    project_id = create_universite(conn, universite)
                except:
                    continue
                
            for bolum in bolumler:
                project_id = create_bolum(conn, bolum)
        
    conn.close()
if __name__ == '__main__':
    main()
