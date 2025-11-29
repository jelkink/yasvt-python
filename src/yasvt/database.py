import sqlite3
from yasvt.word import Word

class Database:

    def __init__(self, db_path, language1, language2):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.language1 = language1
        self.language2 = language2
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS words (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                word1 VARCHAR(100),
                word2 VARCHAR(100),
                language1 VARCHAR(20),
                language2 VARCHAR(20),
                note TEXT,
                score INTEGER,
                UNIQUE(word1, word2, language1, language2)          
            )
        ''')
        self.conn.commit()

    def flip_languages(self):
        self.language1, self.language2 = self.language2, self.language1

    def merge_word_list(self, word_list):
        for word in word_list.words:
            self.cursor.execute("SELECT score FROM words WHERE word1 = ? AND word2 = ? AND language1 = ? AND language2 = ?",
                                (word.source_word, word.target_word, word.source_language, word.target_language))
            row = self.cursor.fetchone()
            if row:
                existing_score = row[0]
                word.set_score_byte(existing_score)
            else:
                self.cursor.execute('''
                    INSERT OR IGNORE INTO words (word1, word2, language1, language2, note, score)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (word.source_word, word.target_word, word.source_language, word.target_language, word.note, word.get_score_byte()))
        self.conn.commit()

    def read_word_list(self, word_list, start=0, number=-1):
        query = 'SELECT word1, word2, language1, language2, note, score FROM words WHERE language1 = ? AND language2 = ?'
        if number > 0:
            query += ' LIMIT ? OFFSET ?'
        self.cursor.execute(query,
                            (self.language1, self.language2, number, start) if number > 0
                            else (self.language1, self.language2))
        rows = self.cursor.fetchall()
        for row in rows:
            source_word, target_word, source_language, target_language, note, score = row
            word = Word(source_language, target_language, source_word, target_word, note)
            word.set_score_byte(score)
            word_list.append(word)

        print(f"Imported {len(rows)} words from database.")

    def update_word_score(self, word):
        self.cursor.execute('''
            UPDATE words
            SET score = ?
            WHERE word1 = ? AND word2 = ? AND language1 = ? AND language2 = ?
        ''', (word.get_score_byte(), word.source_word, word.target_word, word.source_language, word.target_language))
        self.conn.commit()
        
    def read_word_score(self, word):
        self.cursor.execute("SELECT score FROM words WHERE word1 = ? AND word2 = ? AND language1 = ? AND language2 = ?",
                            (word.source_word, word.target_word, word.source_language, word.target_language))
        row = self.cursor.fetchone()
        if row:
            existing_score = row[0]
            word.set_score_byte(existing_score)
    
    def close(self):
        self.conn.close()