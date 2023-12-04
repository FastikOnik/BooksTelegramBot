# database.py
import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                description TEXT,
                genre TEXT
            )
        ''')
        self.conn.commit()

    def add_book(self, title, author, description, genre):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO books (title, author, description, genre) VALUES (?, ?, ?, ?)',
                       (title, author, description, genre))
        self.conn.commit()

    def get_all_books(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, title, author FROM books')
        return cursor.fetchall()

    def get_book_details(self, book_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
        return cursor.fetchone()

    def get_books_by_genre(self, genre):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, title, author FROM books WHERE genre = ?', (genre,))
        return cursor.fetchall()

    def search_books(self, keyword):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, title, author FROM books WHERE title LIKE ? OR author LIKE ? OR genre LIKE ?',
                       ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        return cursor.fetchall()

    def delete_book(self, book_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        self.conn.commit()

    def get_all_genres(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT DISTINCT genre FROM books')
        return [item[0] for item in cursor.fetchall()]
