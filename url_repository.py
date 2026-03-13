import psycopg2
import os
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')



class UrlRepository:
#метод для создания соединения, init не нужен,  потому что в
#каждом методе соединение открывается заново
    def get_connection(self):
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    
#вывод всех данных из таблицы urls    
    def get_content(self):
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                sql = """
                SELECT u.*, MAX(u_c.created_at) AS last_check
                FROM urls as u
                LEFT JOIN url_checks as u_c ON u.id = u_c.url_id
                GROUP BY u.id, u.name, u.created_at
                ORDER BY u.created_at DESC
                """
                cur.execute(sql)
                return cur.fetchall()
            
#получение данных об url по id    
    def find(self, id):
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                sql = "SELECT * FROM urls WHERE id = %s;"
                cur.execute(sql, (id,))
                return cur.fetchone()

#сохранение url в БД и вывод его id
    def save(self, url):
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                sql = """
                INSERT INTO urls (name)
                VALUES (%s) RETURNING id;
                """
                cur.execute(sql, (url,))
                result = cur.fetchone()
                conn.commit()
                return result['id']

#поиск id по имени(url)    
    def find_by_name(self, name):
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                sql = """
                SELECT id FROM urls WHERE  name= %s;
                """
                cur.execute(sql, (name,))
                return cur.fetchone()
    

    def save_check(self, url_id):
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                sql = """
                INSERT INTO url_checks (url_id)
                VALUES (%s) RETURNING id;
                """
                cur.execute(sql, (url_id,))
                check_id = cur.fetchone()
                conn.commit()
                return check_id
    
    def get_url_checks(self, url_id):
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                sql = """
                SELECT * FROM url_checks WHERE url_id = %s
                ORDER BY created_at DESC;
                """
                cur.execute(sql, (url_id,))
                return cur.fetchall()
    