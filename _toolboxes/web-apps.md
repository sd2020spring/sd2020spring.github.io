---
title: Web Apps
category: web-development
compatible: linux, macos
---

{% include toc %}

## Introduction

Flask is a lightweight and powerful web framework for Python. It's easy to
learn and simple to use, allowing you to build your web app in a short amount
of time.

In this toolbox, you'll how to build a simple website, containing two static
pages with a small amount of dynamic content. While Flask can be used for
building complex, database-driven websites, starting with mostly static pages
will be useful to introduce a workflow, which you can then generalize to make
more complex pages in the future. Upon completion, you'll be able to use this
sequence of steps to jump-start your next Flask app.

## Get Set

[GitHub Classroom invite]({{ site.data.github.TB_Flask_invite }})

In this toolbox, you'll be learning Flask. To do this, you'll first need to
install Flask. Run the following command:

```bash
$ pip install Flask
```

This toolbox exercise was developed by Patrick Huston.

## What is Flask, really?

In the introduction, we defined Flask as a "web framework", but what does that
actually mean? Let's dig deeper. Before this, let's develop a better
understanding of how the Internet works.

When you open up a web page in your browser (e.g. Chrome, Firefox, etc.), it
makes an HTTP request to a server somewhere in the world. This could be
something like `GET me the home page`. This server handles this request,
sending back data (this can be in the form of HTML, JSON, XML, etc.), which is
rendered by your browser.

This is where Flask comes in - it allows you to create the logic to make a web
server quickly in Python. You can write logic that will execute when a request
is made for one of your routes (e.g. `www.mycoolwebsite.com/home`)

## Hello World in Flask

Let's write some Flask. In the starter code, there is a file named `hello.py` which is a very simple Hello World application written in Flask:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

Run `hello.py` in the terminal.

```bash
$ python hello.py
 * Running on http://127.0.0.1:5000/
```

<p class="data-proofer-ignore" markdown="1">
Now head over to <http://127.0.0.1:5000/>, and you should see your hello world
greeting.
</p>

In case you're curious `127.0.0.1` points to your local computer, and `5000`
is the port it's listening on.

What did that actually do? Let's walk through the steps.

1. First we imported the Flask class.
2. Next we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use `__name__` because depending on if it’s started as application or imported as module the name will be different ('`__main__'` versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on.
3. We then use the `route()` [decorator](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators) to tell Flask what URL should trigger our function. In this case our route is `/`, commonly referred to as the `index` of a page. This is the homepage of your website.
4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
5. Finally we use the `run()` function to run the local server with our application. The `if __name__== '__main__'` makes sure the server only runs if the script is executed directly from the Python interpreter and not used as an imported module.

To stop the server, hit `ctrl+c`.

## What's this routing business?

In our hello world, example, we had one route denoted by the decorator
`@app.route('/')`. Again, this 'decorator' tells the Flask app that any
incoming requests for `GET /` will run the function we called
`hello_world()`.

Edit your  `hello.py` file so that it looks like the example below. We now have an index page which returns a string and a `'/hello'` route that returns a different string.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
```


In this example, if you now navigate to <http://127.0.0.1:5000> you should see "Index Page" and if you then visit  <http://127.0.0.1:5000/hello>, you should see "Hello World" returned since the `'/hello'` route was defined to do so.

Pretty simple, right? What happens when we want to do something _useful_ \-
*e.g.* display something other than text?

## Let's serve some HTML!

HTML (HyperText Markup Language) is the standard markup language used to
create web pages. In addition to sending back strings, Flask can send back
HTML files to the client, which will be rendered in the browser. Let's get to
work creating a basic HTML document.

> If you are new to HTML or if you need a refresher, [this website](https://www.w3schools.com/html/html_intro.asp) is very helpful and provides many examples.

Let's start by creating a new directory called `templates` and creating a new file within it called `index.html` along with the following code..

```html
<!DOCTYPE html>
<html>
    <head>
        <title>
            A Small Hello
        </title>
    </head>
<body>
    <h1>Hi</h1>
    <p>This is very minimal "hello world" HTML document.</p>
</body>
</html>
```


Now let's serve this HTML page. This can be done with the `render_template()` method that is provided by flask. At the top of `hello.py` make sure you add `render_template` to the import statement so it looks like the updated one below. Let's modify our `'/hello'` route to return our HTML:

```python
from flask import Flask, render_template

@app.route('/hello')
def hello():
    return render_template('index.html')
```

Run `hello.py` once again and go to <http://127.0.0.1:5000/hello> and what appears on the page should resemble the html you just added.



## Rendering Pages with Variables

Rendering pages that have everything hardcoded is not ideal in most situations, because a dynamic web application will want to do some sort of computation with data before returning it to users. Let's figure out how to pass variables to our HTML pages!

All you have
to do is provide the name of the template and the variables you want to pass
to the template engine as keyword arguments. Here’s a simple example of how to
render a template:

```python
from flask import Flask, render_template

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/<name>')
def helloTemplate(name=None):
    return render_template('hello.html', name=name)
```

Then change `hello.html` so that it renders with the name that gets passed through.

```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

And that's it! Again, following the instructions

```bash
$ python hello.py
 * Running on http://127.0.0.1:5000/
```

You can access the templated page by going to http://127.0.0.1:5000/<YOUR_NAME> and you should see your name being inserted into your page! In our route
`/hello/<name>`, we're allowing someone to make a request with an additional
'name' parameter that can be anything. We can then use this `name` and render
it in our HTML template `hello.html`. We use the `{___}` syntax to insert
outside variables into the template. Additionally, we can insert Pythonic flow
logic directly into our HTML page – see `{% raw %}{% if name %}{% endraw %}`. We could go on for
years about all of the power of Jinja templating, but I'll leave that joy to
this [wonderful article](http://jinja.pocoo.org/docs/dev/templates/).



## Build your own app: getting input from the user

What use is a web application if you can't get any data back from the user?
Let's set up a simple app. Here are our end specifications:

**Start creating your app in the flask_app.py file in the starter code**

1. Upon visiting the index page at <http://127.0.0.1:5000/>, the user will be greeted by a page that says hello, and includes an input form that requests their name, age, and favorite SoftDes Ninja.
2. Upon clicking the 'Submit' button, the data from the form will be sent via a POST request to the Flask backend at the route `POST /login`.
3. The Flask backend will handle the request to `POST /login` and perform some simple validation on the user input - simply check to see if they exist.
4. If all the information is present, the app will render a page for the user - presenting their name and age. Regardless of their input for final question, and regardless of whether Patrick is a SofDes Ninja, the app will display `Patrick Huston`
5. If all the information is not present, the app will render a simple error page, which will include some indication that they didn't include all the required information, in addition to a button that will redirect the user back to the home page.

It will be up to you to make this happen. If you feel confident in your
ability to implement this, go for it! If you'd like more scaffolding, continue
reading.


## Suggestions

If you're feeling a little lost, that's perfectly okay! Let's start by making files for all of the pages we need. In the templates folder create the following files:

`questions.html`

`response.html`

`error.html`


### Questions

`questions.html` should be the first page the user see when you run `flask_app.py`. This page should have a text field for the user's name, age, and favorite NINJA. To do this, you will need to create an html form.

>If you are unfamiliar with forms, check out [here](http://www.w3schools.com/html/html_forms>.asp) and [here](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Your_first_HTML_form)


### Response

`response.html` should display the information the user entered. This is where the rendering pages with variables section will come in handy. This means that you have to understand sending data from the html form as well as actions and methods in order to create a functioning submit button.

>For information about sending data, actions, and methods, check out [here](https://www.tutorialspoint.com/flask/flask_http_methods.htm) and [here](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Sending_and_retrieving_form_data).


In order to render the information from the form, you need a way to access the form data. In order to access the inputs, you must use the request object which you can read about [here](http://flask.pocoo.org/docs/1.0/quickstart/#the-request-object).

```python
from flask import Flask, render_template, request
```

You can access the form data by the name you assigned each input in the form html. In this example, we used the name username to identify the data entered in the text field.

###### `response.html`

  ```html
   <input type="text" name='username' />
  ```


###### `flask_app.py`
  ```python
  request.form['username']
  ```



### Error

This page should be a simple error page that gets rendered if the user hasn't entered enough information. Make sure that it informs the user why they are getting this error and provide a button that directions them back to the home page.

>If your button isn't redirecting, try creating a form on the error page with a submit >button that reroutes to the questions page.



## Words of Wisdom
If you are still feeling stuck, the official Flask documentation is also very helpful and provides additional information about the topics introduced in this toolbox. [HERE](http://flask.pocoo.org/docs/1.0/quickstart/).

[This guide](https://www.tutorialspoint.com/flask/flask_quick_guide.htm) is also a good resource. It provides many examples that are easy to understand and can be applied to your app.


There are also many more resources available to you which you are encouraged to take advantage of. We understand that a lot of the topics and concepts in this toolbox will be new to most of you. Web apps are a great tool to have in your toolbox for future projects and it is quite alright to still be confused. Don't hesitate to reach out for help from NINJAs and instructors. Good Luck!



## What to turn in

Push the web app you developed in the previous section to GitHub.

## Going further

1. **Learn more about [Django](https://www.djangoproject.com/)** – an alternative to Flask. They don't have many major differences other than some small quirks in conventions and style. See [here](https://wakatime.com/blog/25-pirates-use-flask-the-navy-uses-django) for more analysis.
2. **Want to keep track of some data in your web app?** Instead of using a .txt file or a pickle file, it's common practice in nearly any web app to use a database. A few especially well-known database choices are MySql, SQLite, or PostgreSQL (which all use [Structured Query Language](https://www.codecademy.com/learn/learn-sql) to manipulate stored data, as do many other common [relational databases](https://en.wikipedia.org/wiki/Relational_database)) You also may have heard some buzz about MongoDB, which uses an unstructured data format in `documents` similar to JSON. Mongo is stupidly easy to set up and use, but I'd stop and think first before jumping right in. It may be the easy choice, but representing your data intelligently in a relational table can be much more effective and less of a headache later on.
3. **But HTML is so ugly!** HTML alone *is* very ugly. That's why we use CSS (Cascading Style Sheets) to add some extra flair and style to our HTML. You can change pretty much anything about HTML - colors, shapes, sizes, placement, etc. with CSS rules. It's also pretty simple to write. Check [this resource](http://www.w3schools.com/css/css_intro.asp) out to learn more about CSS.
4. **What about making my website dynamic?** SoftDes may be a class in Python, but we can venture out a little and use some [jQuery](http://www.w3schools.com/jquery/jquery_intro.asp). jQuery might seem scary, but you use it in a way similar to adding/linking CSS styling to your HTML. You write scripts in JavaScript (which isn't too difficult), which can allow you to add beautiful responsive and dynamic content to your web app. You can also use a Javascript frontend framework like [React](https://reactjs.org/) or [Redux](https://redux.js.org/) to do advanced state based pages. It's pretty cool, but quite advanced!
5. You can also use [D3](https://d3js.org) to display graphical data in a web page.
