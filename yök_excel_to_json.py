import csv
import json

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

known_keywords = ['%25 İndirimli', '%50 İndirimli', '%75 İndirimli', 'Almanca', 'Ankara', 'Arapça', 'Açıköğretim', 'Bulgarca', 'Burslu', 'Erkek', 'Ermenice', 'Farsça', 'Fransızca', 'KKTC Uyruklu', 'Korece', 'Kız', 'Lehçe', 'M.T.O.K.', 'Milli Savunma Bakanlığı Adına', 'Rus Dili ve Edebiyatı', 'Rusça', 'SUNY Albany', 'T.C. Vatandaşları', 'Türkçe-Rusça', 'Türkçe/İngilizce/Fransızca', 'UNCW', 'UOLP- FH KIEL Uygulamalı Bilimler Üniversitesi', 'UOLP- North Carolina Wilmington Üniversitesi', 'UOLP-ABD North Carolina Üniversitesi', 'UOLP-ABD State University of New York University at Albany', 'UOLP-Azerbaycan Mimarlık ve İnşaat Üniversitesi', 'UOLP-ECAM-Lyon', 'UOLP-Hamburg Üniversitesi', 'UOLP-Köln Üniversitesi', 'UOLP-Marmara Üniversitesi', 'UOLP-New Jersey Institute of Technology', 'UOLP-New York Eyalet Üniversitesi', 'UOLP-SUNY Binghamton', 'UOLP-SUNY Buffalo', 'UOLP-SUNY Cortland', 'UOLP-SUNY Empire State College', 'UOLP-SUNY Maritime', 'UOLP-SUNY New Paltz', 'UOLP-Sam Houston State', 'UOLP-Sağlık Bilimleri Üniversitesi', 'UOLP-Uluslararası Balkan Üniversitesi', 'UOLP-Uluslararası Kırgızistan Üniversitesi', 'UOLP-Uluslararası Saraybosna Üniversitesi', 'Uzaktan Öğretim', 'Çin Dili ve Edebiyatı', 'Çince', 'Öğretmenlik', 'Ücretli', 'İng-Fra-Türkçe', 'İngiliz Dili ve Edebiyatı', 'İngilizce', 'İngilizce, Fransızca, Türkçe', 'İngilizce-Fransızca', 'İspanyolca', 'İstanbul', 'İtalyanca', 'İÖ', 'İçişleri Bakanlığı Adına']
burs_durumları = ['Ücretli','%25 İndirimli', '%50 İndirimli', '%75 İndirimli','Burslu']
ogrenim_durumu = ['Uzaktan Öğretim','İÖ','Örgün','Açık Öğretim','KKTC', 'Yabancı']
universite_turleri = ['Devlet Üniversitesi','Vakıf Üniversitesi',]
iller = ['ADANA', 'ADIYAMAN', 'AFYONKARAHİSAR', 'AĞRI', 'AMASYA', 'ANKARA', 'ANTALYA', 'ARTVİN', 'AYDIN', 'BALIKESİR', 'BİLECİK', 'BİNGÖL', 'BİTLİS', 'BOLU', 'BURDUR', 'BURSA', 'ÇANAKKALE', 'ÇANKIRI', 'ÇORUM', 'DENİZLİ', 'DİYARBAKIR', 'EDİRNE', 'ELAZIĞ', 'ERZİNCAN', 'ERZURUM', 'ESKİŞEHİR', 'GAZİANTEP', 'GİRESUN', 'GÜMÜŞHANE', 'HAKKARİ', 'HATAY', 'ISPARTA', 'MERSİN', 'İSTANBUL', 'İZMİR', 'KARS', 'KASTAMONU', 'KAYSERİ', 'KIRKLARELİ', 'KIRŞEHİR', 'KOCAELİ', 'KONYA', 'KÜTAHYA', 'MALATYA', 'MANİSA', 'KAHRAMANMARAŞ', 'MARDİN', 'MUĞLA', 'MUŞ', 'NEVŞEHİR', 'NİĞDE', 'ORDU', 'RİZE', 'SAKARYA', 'SAMSUN', 'SİİRT', 'SİNOP', 'SİVAS', 'TEKİRDAĞ', 'TOKAT', 'TRABZON', 'TUNCELİ', 'ŞANLIURFA', 'UŞAK', 'VAN', 'YOZGAT', 'ZONGULDAK', 'AKSARAY', 'BAYBURT', 'KARAMAN', 'KIRIKKALE', 'BATMAN', 'ŞIRNAK', 'BARTIN', 'ARDAHAN', 'IĞDIR', 'YALOVA', 'KARABÜK', 'KİLİS', 'OSMANİYE', 'DÜZCE']
puanturuBolumDict = {}
uniList = []
def delete_spaces(_str):
    while _str.startswith(' '):
        prev_len = len(_str)
        _str = _str[1:]
    while _str.endswith(' '):
        _str = _str[:-1]
    return _str
i = 0
with open('tablo4_21_07_20.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    universiteler = {}
    universite = None
    fakulteler = []
    fakulte = None
    bolumDict = {}
    keywords = []
    print(f'{type(csv_reader)}')
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
            meb = row[6]
            aciklamalar = row[7]
            siralama = row[8]
            tbn_puanlar = row[9]
            p_dr_say = row[10]
            d_dr_say = row[11]
            dr_ogr_say = row[12]


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
                # print(universite)
                fakulte = None
            elif fakulte is None or "Fakülte" in program_adi or "Yüksekokulu" in program_adi:
                fakulte = program_adi
                if not fakulte in fakulteler:
                    fakulteler.append(fakulte)
                # print(f"\t{fakulte}")
            if len(program_kodu)>0:
                program_parts = program_adi.split('(')
                program_parts_number = len(program_parts)
                if program_parts_number >1:
                    for keyword in program_parts[1:]:
                        keyword = keyword.replace(')','')
                        keyword = delete_spaces(keyword)
                        if not keyword in keywords:
                            keywords.append(keyword)
                program_adi, ogrenim_tipi,burs_durumu = get_program_infos(program_adi)
                bolum_ismi = program_adi
                # bolum_ismi = delete_spaces(bolum_ismi)
                bolumInstance = {
                        'isim':bolum_ismi,"üniversite":uni_name,"fakülte":fakulte,"puan_türü": puan_türü,"kontenjan":kontenjan,"okul_birinci_kont":okul_birinci_kont, "aciklamalar":aciklamalar,"sıralama":siralama,"tbn_puanlar":tbn_puanlar,"prof say":p_dr_say,"doçent_sayısı":d_dr_say,"dr_ogr_say":dr_ogr_say}    
                i+=1
                if bolum_ismi in bolumDict:
                    bolumDict[bolum_ismi].append(bolumInstance)
                else:
                    bolumDict[bolum_ismi] = []
                    bolumDict[bolum_ismi].append(bolumInstance)
                    if puan_türü not in puanturuBolumDict:
                       puanturuBolumDict[puan_türü]= []
                    else:
                        puanturuBolumDict[puan_türü].append(bolum_ismi)
            line_count += 1
# bolumler = list(bolumDict.keys())
# bolumler.sort()
# # for bolum in bolumler[:]:
# #     print(bolum)
# for uni, value in universiteler.items():
#     print(f"{uni}:{value}")
# print(len(universiteler))
bolumler = []
bolum_isimleri = []
for bolumIsmi, instances in bolumDict.items():
    bolumler.append({"isim":bolumIsmi,"instances":instances, "puan_türü":instances[0]["puan_türü"]})
    for instance in instances:
        if(instance["puan_türü"] != instances[0]["puan_türü"]):
            print(instance)
    bolum_isimleri.append(bolumIsmi)
bolum_isimleri.sort()
bolumlerStr = ''
for bolum in bolum_isimleri:
    bolumlerStr += f"'{bolum}',\n"

with open('bölümler_20.txt', 'w', encoding='utf8') as txt_file:
  txt_file.write(bolumlerStr)
txt_file.close()

puanturuBolumDict['EA'].sort()
puanturuBolumDict['SAY'].sort()
puanturuBolumDict['DİL'].sort()
puanturuBolumDict['SÖZ'].sort()
with open('bölümAlan_20.json', 'w', encoding='utf8') as json_file:
  json.dump(puanturuBolumDict, json_file, ensure_ascii=False, indent=4)
json_file.close()

with open('bölümler_20.json', 'w', encoding='utf8') as json_file:
  json.dump(bolumler, json_file, ensure_ascii=False, indent=4)
json_file.close()

with open('üniversiteler_20.json', 'w',encoding='utf8') as json_file:
  json.dump(uniList, json_file, ensure_ascii=False, indent=4)
json_file.close()

print(i)