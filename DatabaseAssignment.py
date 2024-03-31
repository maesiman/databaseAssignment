

import sqlite3

# connect to database
conn = sqlite3.connect('test.db')

# create table if it does not exist
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_testFilesAssignment( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()
conn.close()



conn = sqlite3.connect('test.db')


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# loop thru fileLis
for item in fileList:
    # validate if filename ends with txt
    if item.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # insert to table
            cur.execute("INSERT INTO tbl_testFilesAssignment(col_fileName) VALUES(?)", (item,))
            conn.commit()

conn.close()
