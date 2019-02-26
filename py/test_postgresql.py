#!/usr/bin/env python
import psycopg2

def createTables():
	commands = (
		"""	CREATE TABLE projects (
			project_id SERIAL PRIMARY KEY,
			project_name VARCHAR(255) NOT NULL
			)
		""",
		""" CREATE TABLE users (
			user_id SERIAL PRIMARY KEY,
			user_name VARCHAR(255) NOT NULL
			)
		""",
		""" CREATE TABLE project_extension (
			project_id INTEGER NOT NULL,
			project_deadline VARCHAR(25),
			FOREIGN KEY (project_id)
				REFERENCES projects (project_id)
				ON UPDATE CASCADE ON DELETE CASCADE
			)
		""",
		""" CREATE TABLE project_user (
			project_id INTEGER NOT NULL,
			user_id INTEGER NOT NULL,
			role VARCHAR(25),
			PRIMARY KEY (project_id, user_id),
			FOREIGN KEY (project_id)
				REFERENCES projects (project_id)
				ON UPDATE CASCADE ON DELETE CASCADE,
			FOREIGN KEY (user_id)
				REFERENCES users (user_id)
				ON UPDATE CASCADE ON DELETE CASCADE
			)
		"""
	)
	conn = None
	try:
		conn = psycopg2.connect(host="10.10.10.172", database="projects", user="postgres", password="postgres")
		cur = conn.cursor()
		for c in commands:
			cur.execute(c)
		cur.close()
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

if __name__ == "__main__":
	createTables()
