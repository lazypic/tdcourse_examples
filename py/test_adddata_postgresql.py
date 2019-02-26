#!/usr/bin/env python
import psycopg2

def insertProject(projectName):
	sql = """INSERT INTO projects(project_name)
			VALUES(%s) RETURNING project_id;"""
	conn = None
	project_id = None
	try:
		conn = psycopg2.connect(host="10.10.10.172", database="projects", user="postgres", password="postgres")
		cur = conn.cursor()
		cur.execute(sql, (projectName,))
		project_id = cur.fetchone()[0]
		conn.commit()
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return project_id

if __name__ == "__main__":
	print insertProject("test2")

