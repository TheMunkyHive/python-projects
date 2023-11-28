# General Project Strategy: LinkManager

1. [Brief title of the project](#1-linkmanager-in-python)
2. [Write a brief description of the project](#2-description)
    - with requirements and technology used
3. [Create a roadmap for the project](#3-roadmap)
4. [Explain echt step of the roadmap in detail](#4-design)
5. [Implementation](#4-implementation)

---

#### 1. LinkManager in python

#### 2. Description

Create a webapp to manage a link database in python, flask and sqlite
with the following requirements:

- Python and flask as framework (frontend/backend)
- HTML Page with a webform to manage the Link Database
    Database backend in sqlite3 and jinja template html 
    template engine
- Styling of the webapp with css

Technology:

Python/Flask Environment, Jinja, SQLite, HTML, CSS

#### 3. Roadmap

3.1 Class LinkManager 
3.2 Database Schema
3.3 HTML Frontend with webform
3.4 Styling

#### 4. Design

4.1 Class LinkManager

Class 'LinkManager' with the following methods:

- addLink (Adds a link to the database)
- editLink (Edits an existing Link and update the database)
- deleteLink (Deletes a Link from the database)
- showLink (Displays all Links in the Database)

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

#### 4. Implementation

- [ ] Class LinkManager
- [ ] Database Links
- [ ] HTML Frontend
- [ ] Design