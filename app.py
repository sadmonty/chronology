# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import pytz

app = Flask(__name__)

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp DATETIME
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Главная страница
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        if content:
            # Устанавливаем московское время для временной метки
            moscow_tz = pytz.timezone('Europe/Moscow')
            timestamp = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO entries (content, timestamp) VALUES (?, ?)', (content, timestamp))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
