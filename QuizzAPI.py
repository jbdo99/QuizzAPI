"""Copyright (C) 2016  Jbdo99

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sqlite3

class Quizz():
    def __init__(self):
        self.db = sqlite3.connect('question.db')
        self.cursor = self.db.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS quizz(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,question TEXT,reponse TEXT)""")
        self.db.commit()


    def add_quest(self,quest,rep):
        try:
            self.cursor.execute("""INSERT INTO quizz(question,reponse) VALUES(?,?)""", [quest,rep])
            self.db.commit()
            return True
        except:
            return False


    def all_question(self):
        reponse = []
        self.cursor.execute("""SELECT question FROM quizz""")
        rows = self.cursor.fetchall()
        for row in rows:
            reponse.append('{0}'.format(row[0]))
        return reponse

    def all_reponse(self):
        reponse = []
        self.cursor.execute("""SELECT reponse FROM quizz""")
        rows = self.cursor.fetchall()
        for row in rows:
            reponse.append('{0}'.format(row[0]))
        return reponse

    def question_id(self,question):
        reponse = []
        self.cursor.execute("""SELECT id FROM quizz WHERE question=?""", [question])
        rows = self.cursor.fetchall()
        for row in rows:
            self.reponse.append('{0}'.format(row[0]))
        return reponse

    def question_reponse(self,question):
        reponse = []
        self.cursor.execute("""SELECT reponse FROM quizz WHERE question=?""", [question])
        rows = self.cursor.fetchall()
        for row in rows:
            self.reponse.append('{0}'.format(row[0]))
        return reponse

    def is_correct(self,quest,rep):
        reponse = []
        try:
            int(quest)
            idh = True 
        except:
            idh=False
            pass
        if idh:
            self.cursor.execute("""SELECT reponse FROM quizz WHERE id=?""", [quest])
        else:
            self.cursor.execute("""SELECT reponse FROM quizz WHERE question=?""", [quest])
        rows = self.cursor.fetchone()
        if str(rows[0]) == rep:
            return True
        else:
            return False

