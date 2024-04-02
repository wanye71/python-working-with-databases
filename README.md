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

*CREATE TABLE tasks(task_id INT(11) NOT NULL AUTO_INCREMENT, project_id INT(11) NOT NULL, description VARCHAR(255), PRIMARY KEY(task_id), FOREIGN KEY(project_id) REFERENCES projects(project_id));*

## Insert data into Tables
*INSERT INTO projects(title, description) VALUES ("Organize Photos", "Organize old iPhone photos by year");*

*INSERT INTO tasks(project_id, description) VALUES (1, "Organize 2024 photos");*

*INSERT INTO tasks(project_id, description) VALUES (1, "Organize 2023 photos");*

*INSERT INTO tasks(project_id, description) VALUES (2, "Read The Huntress");*

*INSERT INTO projects(title, description) VALUES ("Read More", "Read a book a year");*

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
1. Create virtual environment
    * *python3 -m venv mysql-workspace*
2. Move into the workspace directory
    * *cd mysql-workspace/*
3. Activate the virtual workspace
    * *source Scripts/activate*
4. Install MySQL connector for Python
    * *pip3 install mysql-connector-pyton*
5. Create python script
    * *touch database.py*
6. Run the script 6
    * *pythone database.py*

## Encapsulating database operations
```python
import mysql.connector as mysql

def connect(db_name):
    try:
        return mysql.connect(
        host="localhost",
        user="root",
        password=db_pw,
        database=db_name)
    except Error as e:
        print("Here is your ERROR: ", e)

def add_project(cursor, project_title, project_description, tasks):
    project_data = (project_title, project_description)
    cursor.execute('''INSERT INTO projects(title, description)
                   VALUES (%s, %s)''', project_data)
    tasks_data = []
    for task in tasks:
        task_data = (cursor.lastrowid, task)
        tasks_data.append(task_data)
    cursor.executemany('''INSERT INTO tasks(project_id, description)
                       VALUES (%s, %s)''', tasks_data)

if __name__ == '__main__':
    db = connect("projects")

    cursor = db.cursor()

    project_title = "Clean house"
    project_description = "Clean house by room"
    tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
    add_project(cursor, project_title, project_description, tasks)
    db.commit()

    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)
    db.close()

    cursor.execute("SELECT * FROM tasks")
    tasks_records = cursor.fetchall()
    print(tasks_records)
    db.close()

```
## Setting up MySQL in Python using SQLAlchemy
```python
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root' + db_pw +'@localhost:3306/projects', echo=True)
```

## Building a model with SQLAlchemy ORM
```python
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import registry

engine = create_engine('mysql+mysqlconnector://root:waynehatjr@localhost:3306/projects', echo=True)

mapper_registry = registry()
# mapper_registry.metadata

Base = mapper_registry.generate_base()

class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return "<Project(title='{0}', description='{1}')>".format(self.title, self.description)
```
## Adding up a foreign key with SQLAlchemy ORM
```python
    class Task(Base):
        __tablename__ = 'tasks'
        task_id = Column(Integer, primary_key=True)
        project_id = Column(Integer, ForeignKey('projects.project_id'))
        description = Column(String(length=50))

        project = relationship("Project")

        def __repr_(self):
        return "<Task(description='{0}')>".format(self.description)
        
Base.metadata.create_all(engine)
```
*py database.py*

```
result = py database.py 
2024-04-02 12:31:52,399 INFO sqlalchemy.engine.Engine SELECT DATABASE()
2024-04-02 12:31:52,399 INFO sqlalchemy.engine.Engine [raw sql] {}
2024-04-02 12:31:52,399 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
2024-04-02 12:31:52,399 INFO sqlalchemy.engine.Engine [raw sql] {}
2024-04-02 12:31:52,399 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
2024-04-02 12:31:52,399 INFO sqlalchemy.engine.Engine [raw sql] {}
2024-04-02 12:31:52,399 INFO sqlalchemy.engine.Engine BEGIN (implicit)        
2024-04-02 12:31:52,399 INFO sqlalchemy.engine.Engine DESCRIBE `projects`.`projects`
2024-04-02 12:31:52,399 INFO sqlalchemy.engine.Engine [raw sql] {}
2024-04-02 12:31:52,415 INFO sqlalchemy.engine.Engine DESCRIBE `projects`.`tasks`
2024-04-02 12:31:52,415 INFO sqlalchemy.engine.Engine [raw sql] {}
2024-04-02 12:31:52,420 INFO sqlalchemy.engine.Engine COMMIT
```
## Using SQLAlchemy Sessions to transact on a MySQL database

### Create a Session Object
```python
with Session(engine) as session:
    title = 'Oranize closet'
    description = 'Organize closet by color and style'
    organize_closet_project = Project(title=title, description=description)

    # Insert into database
    session.add(organize_closet_project)

    session.flush()

    # Insert tasks into the database
    description = ["Decide what clothes to donate", "Organize summer clothes", "Organize winter clothes" ]
    tasks = [
        Task(project_id=organize_closet_project.project_id, description=description[0] ),
        Task(project_id=organize_closet_project.project_id, description=description[1]),
        Task(project_id=organize_closet_project.project_id, description=description[2])
    ]

    session.bulk_save_objects(tasks)

    session.commit()

```

> /C/Program Files/Git/etc/profile.d/aliases.sh