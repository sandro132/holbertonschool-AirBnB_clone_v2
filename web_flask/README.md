# Web Framework and Flask Tutorial

This repository provides a beginner-friendly guide to understanding what a web framework is and how to build a basic web application using Flask, a micro web framework for Python.

## What is a Web Framework?

A web framework is a software framework designed to aid in the development of web applications including web services, web resources, and web APIs. It provides a structured way to handle various aspects of web development, such as routing, templating, and interacting with databases.

## Building a Web Framework with Flask

This tutorial will walk you through the process of building a basic web framework using Flask. Flask is a micro web framework that allows you to quickly build web applications with Python.

### Defining Routes in Flask

In Flask, a route is a URL pattern that corresponds to a specific function in your code. Routes are used to determine what code should be executed when a user visits a particular URL. Here's an example of defining a route in Flask:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

In this example, when a user visits the root URL (`/`), the `home` function is executed, and the response 'Hello, World!' is sent back to the user's browser.

### Handling Variables in Routes

Flask allows you to define routes with variables in the URL. These variables can be captured and used within your route functions. Here's an example:

```python
@app.route('/user/<username>')
def show_user(username):
    return f'Hello, {username}!'
```

In this case, when a user visits a URL like `/user/john`, the `show_user` function is executed with the captured variable `username` set to "john".

### Using Templates

Templates in Flask are used to generate dynamic HTML content. They allow you to separate the presentation layer from the application logic. Flask uses the Jinja2 template engine for rendering templates.

To render a template, you first need to create a `templates` folder in your project directory. Here's an example of rendering a template:

```python
from flask import render_template

@app.route('/greet/<name>')
def greet(name):
    return render_template('greeting.html', name=name)
```

In this example, the `greet` function renders the `greeting.html` template, passing the `name` variable to the template.

### Creating Dynamic Templates

Dynamic templates in Flask allow you to use loops, conditions, and variables to create flexible HTML content. For example, you can iterate over a list of items and display them using a loop in your template:

```html
<ul>
  {% for item in items %}
    <li>{{ item }}</li>
  {% endfor %}
</ul>
```

### Displaying Data from a MySQL Database

To display data from a MySQL database in a Flask application, you would need to install a MySQL connector library, establish a connection to the database, retrieve the data using SQL queries, and pass the data to your template for rendering.

Here's a high-level overview of the process:

1. Install a MySQL connector library, such as `mysql-connector-python`.
2. Establish a connection to your MySQL database.
3. Retrieve data using SQL queries.
4. Pass the retrieved data to your template for rendering.



### **Authors**
--- 

* ![GitHub Contributors Image](https://contrib.rocks/image?repo=MichiCaballero07/holbertonschool-higher_level_programming) Michel Caballero Granado - <a href="https://github.com/MichiCaballero07" target="_blank"> @MichiCaballero07</a> :genie_woman:![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=MichiCaballero07&show_icons=true)