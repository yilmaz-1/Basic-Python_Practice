import sqlite3
vt=sqlite3.connect("veritabani.sqlite")
im=vt.cursor()

im.execute('''

CREATE TABLE IF NOT EXISTS OGRECI
(ID INT PRIMARY KEY NOT NULL,
ADI TEXT NOT NULL,
SOYADI TEXT NOT NULL,
OKULNO TEXT NOT NULL);

''')


im.execute("INSERT INTO OGRENCI ( ID,ADI,SOYADI,OKULNO) VALUES (2,'MEHMET','ISIK','D-ISL-110')");

vt.commit()
im.close()
