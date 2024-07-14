# General Project Strategy: LinkManager

1. [Brief title of the project](#1-project-title)
2. [Write a brief description of the project](#2-description)
3. [Create a roadmap for the project](#3-roadmap)
4. [Explain echt step of the roadmap in detail](#4-design)
5. [Implementation](#4-implementation)

---

#### 1. Project Title

LinkManager in python / flask / SQLite

#### 2. Description

Create a webapp to manage a link database in python, flask and sqlite
with the following requirements:

- Python and flask as framework (frontend/backend)
- HTML Page with a webform to manage the Link Database
    Database backend in sqlite3 and jinja template html 
    template engine
- Styling of the webapp with css

Technology: Python/Flask Environment, Jinja, SQLite, HTML, CSS

#### 3. Roadmap

- Class Links
- Database Schema
- HTML Frontend with webform
- Styling

---

#### 4. Design

4.1 Class Links

Create a Class 'Links' with the following methods:

- add (Adds a link to the database)
- edit (Edits an existing Link and update the database)
- delete (Deletes a Link from the database)
- show (Displays all Links in the Database)
- update (Updates 'new' or 'visted' link status)

4.2 Database Schema

- Create a new database called 'linkmanager.db'
- Create a new table 'Links'
- Add the following collums: ID primary key & autoincrement, URL, TITLE, AUTHOR, TAGS

4.3 HTML Frontend 

- Create a HTML website
- Query the database and display all links by default (showLink)
  with the ability to edit and delete  existing links
- Webform with the ability to add new links to the database
  with route /add

4.4 Styling
- Styling of the HTML body and page elements
- Resource: Semantic UI (https://semantic-ui.com/introduction/getting-started.html)
  CDN:  
  
    ```html
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/semantic-ui@2.5.0/dist/semantic.min.css">
        <script src="https://cdn.jsdelivr.net/npm/semantic-ui@2.5.0/dist/semantic.min.js"></script>
    ```

---

#### 4. Implementation

- [ ] Class 'Links'
- [ ] Database Links
- [ ] HTML Frontend
- [ ] Design

1. Class 'Links'

- Files: 

```python
    # File linkClass.py:
    
```

```python
    # File app.py:
    from linkClass import Links
```

2. Database

Note: The name of the row-counter in sqlite3 = 'ROWID'. The id will be automatically added
      when a table is created.