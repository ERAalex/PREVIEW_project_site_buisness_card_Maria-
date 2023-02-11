import psycopg2
import psycopg2.extras
from flask import request, flash
import pymysql


# MySQL configurations
# Open database connection
db = pymysql.connect(host='', user='', password='', database='')
# db = pymysql.connect(host='', user='', password='', database='')
# prepare a cursor object using cursor() method
cur = db.cursor()


###### БЛОК ПО ИЗМЕНЕНИЮ В БАЗЕ ДАННЫХ СТАТЕЙ ТЕКСТОВ ######


def art_all_information():
    s = "SELECT * FROM art3"
    cur.execute(s)  # Execute the SQL
    list_users = cur.fetchall()
    return list_users


def art_add_article():
    if request.method == 'POST':
        position = request.form['position']
        name = request.form['name']
        text = request.form['text']
        cur.execute("INSERT INTO art3 (position, name, text) VALUES (%s,%s,%s)", (position, name, text))
        db.commit()
        return flash('Article Added successfully, EspinosaAlex')


def art_get_article(id):
    cur.execute('SELECT * FROM art3 WHERE id = %s', (id,))
    data = cur.fetchall()
    # cur.close()
    total = data[0]
    return total


def art_update_article(id):
    if request.method == 'POST':
        position = request.form['position']
        name = request.form['name']
        text = request.form['text']

        cur.execute("""
            UPDATE art3
            SET position = %s,
                name = %s,
                text = %s
            WHERE id = %s
        """, (position, name, text, id))
        db.commit()
        return flash('Article Updated Successfully, EspinosaAlex')


def art_delete_article(id):
    cur.execute('DELETE FROM art3 WHERE id = {0}'.format(id))
    db.commit()
    return flash('Student Removed Successfully')















