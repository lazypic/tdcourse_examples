#!/usr/bin/env python
import psycopg2

def get_projects():
    conn = None
    try:
        conn = psycopg2.connect(host="10.10.10.172",database="projects", user="postgres", password="postgres")
        cur = conn.cursor()
        cur.execute("""
            SELECT project_id, project_name
            FROM projects
            ORDER BY project_name;
        """)
        print("The number of projects: ", cur.rowcount)
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_projects()