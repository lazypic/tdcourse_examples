#!/usr/bin/env python
import psycopg2
 
def delete_project(project_id):
    conn = None
    rows_deleted = 0
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host="10.10.10.172",database="projects", user="postgres", password="postgres")
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM projects WHERE project_id = %s", (project_id,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows_deleted

if __name__ == '__main__':
    delete_project("1")