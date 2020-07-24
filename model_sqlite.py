#!/usr/bin/env python3

import sqlite3

def save(uid=None, code=None, lang=None):
    if uid is None:
        code = '# Write your code here...'
        connexion = sqlite3.connect('basededonnees.db')
        cur = connexion.cursor()
        cur.execute('INSERT INTO coding(code,lang) VALUES(?,?)',(code, lang))
        connexion.commit()
        connexion.close()
    else:
        connexion = sqlite3.connect('basededonnees.db')
        cur = connexion.cursor()
        cur.execute('UPDATE coding SET code = ?, lang = ? WHERE id = ?',
        (code, lang, uid))
        connexion.commit()
        connexion.close()
    return cur.lastrowid


def read(id):
    connexion = sqlite3.connect('basededonnees.db')
    cur = connexion.cursor()
    cur.execute('SELECT code, lang FROM coding WHERE id = ? LIMIT 1',id)
    record = cur.fetchone()
    return {'code': record[0], 'lang': record[1]}


def getAll():
    d = []
    connexion = sqlite3.connect('basededonnees.db')
    cur = connexion.cursor()
    cur.execute('SELECT id, code FROM coding ORDER BY id DESC LIMIT 10')
    for data in cur.fetchall():
        d.append({'uid': data[0], 'code': data[1]})
    return d

# user --------------------------------------------------

def save_user(ip, navigator, date_time):
    connexion = sqlite3.connect('basededonnees.db')
    cur = connexion.cursor()
    cur.execute('INSERT INTO users(ip, navigator, date_time) VALUES(?,?,?)', (ip, navigator, date_time))
    connexion.commit()
    cur.close()
    connexion.close()
    return True

def getAll_users():
    connexion = sqlite3.connect('basededonnees.db')
    cur = connexion.cursor()
    cur.execute("SELECT * FROM users")
    d = cur.fetchall()
    cur.close()
    connexion.close()
    return d
