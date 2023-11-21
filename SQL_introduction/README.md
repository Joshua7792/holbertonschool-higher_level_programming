# SQL Introduction Project

This project aims to provide a hands-on introduction to SQL and MySQL. By completing the tasks in this project, you will gain a solid understanding of fundamental database concepts, SQL syntax, and MySQL server operations.

## Learning Objectives

Upon completion of this project, you should be able to explain the following concepts without relying on external resources:

### General
- **Database Basics:**
  - What's a database?
  - What's a relational database?
  - What does SQL stand for?
  - What's MySQL?

- **MySQL Operations:**
  - How to create a database in MySQL?
  - What does DDL (Data Definition Language) and DML (Data Manipulation Language) stand for?
  - How to CREATE or ALTER a table?
  - How to SELECT data from a table?
  - How to INSERT, UPDATE, or DELETE data?

- **Advanced Concepts:**
  - What are subqueries?
  - How to use MySQL functions?

### Requirements
- Use allowed editors: vi, vim, emacs.
- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25).
- Files should end with a new line.
- SQL queries should have a comment just before (i.e., syntax above).
- Files should start with a comment describing the task.
- All SQL keywords should be in uppercase (SELECT, WHERE, etc.).

## Getting Started

### Install MySQL 8.0 on Ubuntu 20.04 LTS
```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
Connect to MySQL Server
bash

$ sudo mysql
Use the sandbox to run MySQL
In the container, credentials are root/root.
Project Structure
0-list_databases.sql
Write a script that lists all databases of your MySQL server.

bash

$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
1-create_database_if_missing.sql
Write a script that creates the database hbtn_0c_0 in your MySQL server.

bash

$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
2-remove_database.sql
Write a script that deletes the database hbtn_0c_0 in your MySQL server.

bash

$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
3-list_tables.sql
Write a script that lists all the tables of a database in your MySQL server.

bash

$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
4-first_table.sql
Write a script that creates a table called first_table in the current database in your MySQL server.

bash

$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
5-full_table.sql
Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

bash

$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
6-list_values.sql
Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

bash

$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
7-insert_value.sql
Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

bash

$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
8-count_89.sql
Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

bash

$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
9-full_creation.sql
Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and adds multiple rows.

bash

$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
10-top_score.sql
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server, ordered by score (top first).

bash

$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
11-best_score.sql
Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

bash

$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
12-no_cheating.sql
Write a script that updates the score of Bob to 10 in the table second_table without using Bob’s id value, only the name field.

bash
$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
13-change_class.sql
Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

bash

$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
14-average.sql
Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

bash

$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
15-groups.sql
Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

bash

$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
16-no_link.sql
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server, excluding rows without a name value, and listing records by descending score.

bash

$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0