# Python: Working with Databases

## Create virtual environment
1. *python3 -m venv sqlalchemy-workspace*
2. *cd sqlalchemy-workspace*
3. *source Scripts/activate*
4. *pip3 install sqlalchemy*
5. *deactivate*

## Create Database
*CREATE DATABASE projects*

## Create Tables
*CREATE TABLE projects(project_id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(30), description VARCHAR(255), PRIMARY KEY(project_id));*

*CREATE TABLE task(task_id INT(11) NOT NULL AUTO_INCREMENT, project_id INT(11) NOT NULL, description VARCHAR(255), PRIMARY KEY(task_id), FOREIGN KEY(project_id) REFERENCES projects(project_id));*

## Insert data into Tables
*INSERT INTO projects(title, description) VALUES ("Organize Photos", "Organize old iPhone photos by year");*

*INSERT INTO tasks(project_id, description) VALUES (1, "Organize 2024 photos");

INSERT INTO tasks(project_id, description) VALUES (1, "Organize 2024 photos");*

## Select database to use
*USE projects*

## Show tables
*SHOW TABLES*
| Tables_in_projects |
| ------------------ |
| projects           |
| tasks              |

## Select data from tables
**projects table**

| project_id | title      | description                        |
| ---------- | ---------- | ---------------------------------- |
|  1 | Organize Photos    | Organize old iPhone photos by year |
|  2 | Read More          | Read a book year                   |

**tasks table**

| task_id | project_id | description          |
| ------- | ---------- | -------------------- |
|       1 |          1 | Organize 2024 photos |
|       2 |          1 | Organize 2023 photos |
|       3 |          2 | Read The Huntress    |

## Create virtual workspace
1. Create virtual environment 1
    * *python3 -m venv mysql-workspace*
2. Move into the workspace directory 2
    * *cd mysql-workspace/*
3. Activate the virtual workspace 3
    * *source Scripts/activate*
4. Install MySQL connector for Python 4
    * *pip3 install mysql-connector-pyton*
5. Create python script 5
    * *touch database.py*
6. Run the script 6
    * *pythone database.py*