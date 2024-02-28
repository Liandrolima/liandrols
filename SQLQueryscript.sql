DROP DATABASE IF EXISTS Infinity_School;
SHOW DATABASES
CREATE DATABASE IF NOT EXISTS Infinity_School;
SHOW DATABASES
Enter password: ********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 86
Server version: 8.0.36 MySQL Community Server - GPL

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> USE Infinity_School;
Database changed
mysql> mysql -u LIANDRO -p < create_infinity_school.sql
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'mysql -u LIANDRO -p < create_infinity_school.sql' at line 1
mysql> USE Infinity_School;
Database changed
mysql> CREATE TABLE alunos (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nome VARCHAR(50),
    ->     idade INT
    -> );
Query OK, 0 rows affected (2.44 sec)

mysql> INSERT INTO alunos (nome, idade) VALUES ('João', 20), ('Maria', 22), ('Pedro', 25);
Query OK, 3 rows affected (0.13 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM alunos;
+----+-------+-------+
| id | nome  | idade |
+----+-------+-------+
|  1 | João  |    20 |
|  2 | Maria |    22 |
|  3 | Pedro |    25 |
+----+-------+-------+
3 rows in set (0.00 sec)

mysql> UPDATE alunos SET idade = 21 WHERE nome = 'João';
Query OK, 1 row affected (0.17 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> DELETE FROM alunos WHERE nome = 'Pedro';
Query OK, 1 row affected (0.18 sec)

mysql> SELECT * FROM alunos;
+----+-------+-------+
| id | nome  | idade |
+----+-------+-------+
|  1 | João  |    21 |
|  2 | Maria |    22 |
+----+-------+-------+
2 rows in set (0.00 sec)

mysql> CREATE TABLE professores (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nome VARCHAR(50),
    ->     especialidade VARCHAR(50)
    -> );
Query OK, 0 rows affected (0.46 sec)

mysql> SELECT * FROM professores;
Empty set (0.00 sec)

mysql> INSERT INTO professores (nome, especialidade) VALUES
    -> ('Ana', 'Matemática'),
    -> ('Carlos', 'História'),
    -> ('Juliana', 'Inglês');
Query OK, 3 rows affected (0.12 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * alunos, professores;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'alunos, professores' at line 1
mysql> SELECT * FROM alunos, professores;
+----+-------+-------+----+---------+---------------+
| id | nome  | idade | id | nome    | especialidade |
+----+-------+-------+----+---------+---------------+
|  2 | Maria |    22 |  1 | Ana     | Matemática    |
|  1 | João  |    21 |  1 | Ana     | Matemática    |
|  2 | Maria |    22 |  2 | Carlos  | História      |
|  1 | João  |    21 |  2 | Carlos  | História      |
|  2 | Maria |    22 |  3 | Juliana | Inglês        |
|  1 | João  |    21 |  3 | Juliana | Inglês        |
+----+-------+-------+----+---------+---------------+
6 rows in set (0.00 sec)

mysql>
