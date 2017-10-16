import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

peeps = open('peeps.csv')
peeps_info = csv.DictReader(peeps)

courses = open('courses.csv')
courses_info = csv.DictReader(courses)

f="peeps_and_courses.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

def make_table(table_name, col_keys, csv_dict):
    key1 = col_keys[0]
    key2 = col_keys[1]
    key3 = col_keys[2]
    
    command = 'CREATE TABLE ' + table_name + '(' + key1 + ' TEXT, ' + key2 + ' TEXT, ' + key3 + ' TEXT);'
    c.execute(command)

    for row in csv_dict:
        val1 = '"' + row[key1] + '"'
        val2 = '"' + row[key2] + '"'
        val3 = '"' + row[key3] + '"'
        
        command = 'INSERT INTO ' + table_name + ' VALUES(' + val1 + ',' + val2 + ',' + val3 + ');'
        c.execute(command)

    command = 'SELECT * FROM ' + table_name + ';'
    c.execute(command)

    
peeps_col_keys = ['name', 'age', 'id']
courses_col_keys = ['code', 'mark', 'id']

make_table('peeps', peeps_col_keys, peeps_info)
make_table('courses', courses_col_keys, courses_info)

#==========================================================
db.commit() #save changes
db.close()  #close database

courses.close()
peeps.close()


