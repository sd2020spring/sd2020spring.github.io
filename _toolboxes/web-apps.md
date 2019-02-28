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
$ conda install Flask
```

This toolbox exercise was developed by Patrick Huston.

## What is Flask, really?

In the introduction, we defined Flask as a "web framework", but what does that
actually mean? Let's dig deeper. Before this, let's develop a better
understanding of how the internet works.

When you open up a web page in your browser (e.g. Chrome, Firefox, etc.), it
makes an HTTP request to a server somewhere in the world. This could be
something like `GET me the home page`. This server handles this request,
sending back data (this can be in the form of HTML, JSON, XML, etc.), which is
rendered by your browser.

This is where Flask comes in - it allows you to create the logic to make a web
server quickly in Python. You can write logic that will execute when a request
is made for one of your routes (e.g. `www.mycoolwebsite.com/home`)

## Hello World in Flask

Let's write some Flask. A simple Hello World application written in Flask can
be as simple as this:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

Write this, save it as something like `hello.py`, and run it in terminal. Make
sure to not call your application `flask.py` because this would conflict with
Flask itself.

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

Here are a couple more quick examples -

```python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'
```

In this example, if you now navigate to <http://127.0.0.1:5000/hello>, you should see "Hello World" returned since the `'/hello'` route was defined to do so.

Pretty simple, right? What happens when we want to do something _useful_ \-
*e.g.* display something other than text?

## Let's serve some HTML!

HTML (HyperText Markup Language) is the standard markup language used to
create web pages. In addition to sending back strings, Flask can send back
HTML files to the client, which will be rendered in the browser. Let's get to
work creating a basic HTML document.

Let's start my creating a new directory called `templates`, and saving a new document as
`index.html` there:

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


Now let's serve this HTML page. This can be down with the `render_template()` method that is provided by flask. Let's modify our `'/hello'` route to return our HTML:

```python
from flask import render_template

@app.route('/hello')
def hello():
    return render_template('index.html')
```


## Rendering Pages with Variables

Rendering pages that have everything hardcoded is not ideal in most situations, because a dynamic web application will want to do some sort of computation with data before returning it to users. Let's figure out how to pass variables to our HTML pages!

All you have
to do is provide the name of the template and the variables you want to pass
to the template engine as keyword arguments. Here’s a simple example of how to
render a template:

```python
from flask import render_template

@app.route('/hello/<name>')
def helloTemplate(name=None):
    return render_template('hello.html', name=name)
```

And here is an example template (`hello.html`) that will work with the above snippet:

```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

You may have noticed something really cool that happened here. In our route
`/hello/<name>`, we're allowing someone to make a request with an additional
'name' parameter that can be anything. We can then use this `name` and render
it in our HTML template `hello.html`. We use the `{___}` syntax to insert
outside variables into the template. Additionally, we can insert Pythonic flow
logic directly into our HTML page – see `{% raw %}{% if name %}{% endraw %}`. We could go on for
years about all of the power of Jinja templating, but I'll leave that joy to
this [wonderful article](http://jinja.pocoo.org/docs/dev/templates/).

<!-- Getting back to our simple Hello World app, let's add in a route to display
our `index.html` we created above.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
``` -->

And that's it! Again, following the instructions

```bash
$ python hello.py
 * Running on http://127.0.0.1:5000/
```

to run the application, and head over to <http://127.0.0.1:5000/>, and you
should see your hello world greeting. It might not look very different, but
you're now working with a much more powerful format of representing
information through HTML. 

You can access the templated page by going to <http://127.0.0.1:5000/<YOUR_NAME>> and you should see your name being inserted into your page!

## Build your own app: getting input from the user

What use is a web application if you can't get any data back from the user?
Let's set up a simple app. Here are our end specifications:

1. Upon visiting the index page at <http://127.0.0.1:5000/>, the user will be greeted by a page that says hello, and includes an input form that requests their name, age, and favorite SoftDes Ninja.
2. Upon clicking the 'Submit' button, the data from the form will be sent via a POST request to the Flask backend at the route `POST /login`.
3. The Flask backend will handle the request to `POST /login` and perform some simple validation on the user input - simply check to see if they exist.
4. If all the information is present, the app will render a 'profile' page for the user - presenting their name and age. Regardless of their input for final question, and regardless of whether Patrick is a SofDes Ninja, the app will display `Patrick Huston`
5. If all the information is not present, the app will render a simple error page, which will include some indication that they didn't include all the required information, in addition to a button that will redirect the user back to the home page.

It will be up to you to make this happen. If you feel confident in your
ability to implement this, go for it! If you'd like more scaffolding, continue
reading.

## Tips and tricks

To complete this exercise, the official Flask documentation will get you
pretty far. There is the [full
documentation](http://flask.pocoo.org/docs/0.10/#user-s-guide) and the
[quickstart guide](http://flask.pocoo.org/docs/0.10/quickstart/), both of
should be pretty helpful.

1. _HTML Forms_ To make forms in HTML, check out [this resource](http://www.w3schools.com/html/html_forms.asp). For even more information, check [this](http://tinyurl.com/htmlforms) out.
2. _Sending Data From Your HTML Form_: You'll need to figure out how write HTML form ["actions"](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Sending_and_retrieving_form_data) for Flask, HTML ["methods"](https://www.tutorialspoint.com/flask/flask_http_methods.htm) for Flask, as well as how to write a "submit" button type for HTML forms.
3. _Handling POST Requests_: To learn more about handling post requests in Flask, check this resource from the [Flask documentation](http://flask.pocoo.org/docs/1.0/quickstart/#http-methods) out.
4. \+ 5. _Accessing the Form Data_: To access the form data, check out [this documentation](http://flask.pocoo.org/docs/1.0/quickstart/#the-request-object) on using the Flask `request` utility.

## What to turn in

Push the web app you developed in the previous section to GitHub.

## Going further

1. **Learn more about [Django](https://www.djangoproject.com/)** – an alternative to Flask. They don't have many major differences other than some small quirks in conventions and style. See [here](https://wakatime.com/blog/25-pirates-use-flask-the-navy-uses-django) for more analysis.
2. **Want to keep track of some data in your web app?** Instead of using a .txt file or a pickle file, it's common practice in nearly any web app to use a database. A few especially well-known database choices are MySql, SQLite, or PostgreSQL (which all use [Structured Query Language](https://www.codecademy.com/learn/learn-sql) to manipulate stored data, as do many other common [relational databases](https://en.wikipedia.org/wiki/Relational_database)) You also may have heard some buzz about MongoDB, which uses an unstructured data format in `documents` similar to JSON. Mongo is stupidly easy to set up and use, but I'd stop and think first before jumping right in. It may be the easy choice, but representing your data intelligently in a relational table can be much more effective and less of a headache later on.
3. **But HTML is so ugly!** HTML alone *is* very ugly. That's why we use CSS (Cascading Style Sheets) to add some extra flair and style to our HTML. You can change pretty much anything about HTML - colors, shapes, sizes, placement, etc. with CSS rules. It's also pretty simple to write. Check [this resource](http://www.w3schools.com/css/css_intro.asp) out to learn more about CSS.
4. **What about making my website dynamic?** SoftDes may be a class in Python, but we can venture out a little and use some [jQuery](http://www.w3schools.com/jquery/jquery_intro.asp). jQuery might seem scary, but you use it in a way similar to adding/linking CSS styling to your HTML. You write scripts in JavaScript (which isn't too difficult), which can allow you to add beautiful responsive and dynamic content to your web app. You can also use a Javascript frontend framework like [React](https://reactjs.org/) or [Redux](https://redux.js.org/) to do advanced state based pages. It's pretty cool, but quite advanced!
5. You can also use [D3](https://d3js.org) to display graphical data in a web page.



## (Optional) Going Beyond - Web Deployment

One thing you can do once completing this toolbox is deploy your Flask application to the cloud, so that users can visit it at a public URL. This is especially useful if you end up using Flask in your final project - in past years, teams have used it to make their projects publicly accessible on the Web!

You will learn how to use `git push` to deploy to the Heroku hosting service, how to configure a Flask application to accept external requests, and how and why to configure a Flask application to listen on different TCP/IP ports.


### Get Set

1. Follow the instructions [here](https://signup.heroku.com) to sign up for
   a (free) account Heroku cloud platform. Heroku manages servers that will
   run your app.

2. Follow the instructions [here](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) to download the Heroku command-line interface.

3. Run `heroku login` with the credentials you created in step 1:

    Enter your Heroku credentials.
    Email: youremail@olin.edu
    Password (typing will be hidden):

### Create a Heroku application

Run `heroku apps:create` to create a Heroku **application**:

```bash
$ heroku apps:create web-app
Creating app... done, boiling-brushlands-71788
https://boiling-brushlands-71788.herokuapp.com/ | https://git.heroku.com/boiling-brushlands-71788.git
```

`heroku apps:create` selects a random name (above, `boiling-brushlands-71788`)
for your application. You can also *specify* a name, so long as it is unique among all Heroku applications (for all users).
For example, `heroku app:create softdes-toolbox` makes my application available at `https://softdes-toolbox.herokuapp.com`.

### Publish Your Application to Heroku

```bash
$ cd /path/to/web-app
$ heroku git:remote -a my-heroku-app-name
$ git push heroku master
```

where `my-heroku-app-name` is the name of your Heroku application.

You should see an error message:

    Total 0 (delta 0), reused 0 (delta 0)
    remote: Compressing source files... done.
    remote: Building source:
    remote:
    remote: -----> Failed to detect set buildpack https://codon-buildpacks.s3.amazonaws.com/buildpacks/heroku/python.tgz
    remote: More info: https://devcenter.heroku.com/articles/buildpacks#detection-failure
    remote:
    remote:  !     Push failed
    remote: Verifying deploy....
    remote:
    remote: !  Push rejected to my-heroku-app-name.
    remote:
    To https://git.heroku.com/my-heroku-app-name.git
    ! [remote rejected] 7039fff -> master (pre-receive hook declined)
    error: failed to push some refs to 'https://git.heroku.com/my-heroku-app-name.git'

### Why Doesn't it Work (pt. 1 of 2)? – Setting Your Repo Up for Heroku

If you Google around and spend some time learning what a "buildpack" is
(not required for this toolbox), you will eventually learn that Heroku
can't figure out what programming language your application is written in, and
therefore doesn't know how to run it.

You need to add three files to your repository in order to tell Heroku
how to [provision a server](https://en.wikipedia.org/wiki/Provisioning#Server_provisioning):

`requirements.txt`
: is a list of Python packages. This tells Heroku that your application is a Python
  program, and which packages to install.

`Procfile`
: lists the command and arguments that starts your program.

`runtime.txt`
: specifies the Python version. Without this file, Heroku will use Python 2.7.
The toolboxes use Python 3, so it is necessary to override this.

Here's what to do:

1. Create the following three files, with these contents:

    **`Procfile`**

        web: python3 hello.py

    **`runtime.txt`**

        python-3.7.2

    **`requirements.txt`**

        Flask

2. Use `git add` to add the new files to the repository. `git commit` them.

3. Test the `Procfile` on your laptop:

    ```bash
    $ heroku local web
    ```

    Running `heroku local` has the same effect as running `python3 hello.py`, but it uses the same `Procfile` that Heroku will use.
    Running therefore `heroku local` tests more of what will happen “in production” than running `python3 hello.py` does.
    (See [The Twelve-Factor App: Dev/prod parity](https://12factor.net/dev-prod-parity).

4. Now `git push heroku master` again. This time the deploy should succeed:

    ```bash
    $ git push heroku master
    […]
    remote: -----> Launching...
    remote:        Released v18
    remote:        https://my-heroku-app-name.com/ deployed to Heroku
    remote: Verifying deploy.... done.
    To https://git.heroku.com/my-heroku-app-name.git
    ```

### Open Your App in a Browser

Do you do this in one two ways:

1. Find the line `https://my-heroku-app-name.herokuapp.com/ deployed to Heroku`
   in the `git push` output above. Open `https://my-heroku-app-name.herokuapp.com/`
   in a browser. Or:

2. `heroku apps:open` does this automatically.

You should see an “Application Error” page.

### Why Doesn't it Work (pt. 2 of 2)? Configuring Your Server to Accept Remote Connections

By default, your application only accepts HTTP requests from the same machine.
This is because it uses `127.0.0.1` as the host.

This is appropriate for local development, but does not make for a web server in the cloud. You need to run your application with `0.0.0.0` as the host. This allows it to accept requests from anywhere on the web.

A second issue is that your application currently accepts connections to [TCP/IP port](http://www.bullguard.com/bullguard-security-center/pc-security/computer-security-resources/tcp-ip-ports.aspx) #5000.

From the outside, Heroku accepts HTTPS connections to port #443. This is the default port for an `https:` URL, and is why you (eventually) will get to  use `https://my-heroku-app-name.herokuapp.com/`, instead of `https://my-heroku-app-name.herokuapp.com:5000/`.

Internally, Heroku expects your app to accept an HTTP connection on some port that depends on your application, maybe where it's running, and maybe the time of day – you don't know what the port number is when you write your code. Heroku communicates the port number to your application by setting an [environment variable](https://en.wikipedia.org/wiki/Environment_variable).

Fix these two problems (using `0.0.0.0`, and reading the port number from an environment variable) as follows:

1. Add this line to the top of your file:

    ```python
    import os
    ```

2. Define `HOST` and `PORT` as below. Then add `host` and `port` arguments to the `app.run` function. Commit the change, `git push` to Heroku again, and test again. You should see your web page.

    ```python
    HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host=HOST, port=PORT)
    ```

### Whitelist the Domain

**Problem:** Olin's [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) provider blocks some new sites from the Olin network after a 1-3 day grace period.
Your app may work for a while, and then stop working with the message below:

![]({% link images/toolboxes/heroku/it_security_message.png %})

**Solution:** Send a message to <helpdesk@olin.edu>: “I am using the domain name myapp.herokuapp.com for a class project, and need access to it from within the Olin network. Please configure DNS so that it does not block this site.”

## Even More To Do

Some things you can do to learn more and/or have more fun:

* Add an `app.json` file, and a ![](https://www.herokucdn.com/deploy/button.svg) button. The instructions are [here](https://devcenter.heroku.com/articles/heroku-button).
* Learn about [Gunicorn](https://devcenter.heroku.com/articles/python-gunicorn). Use this to deploy a web application that can serve more than one HTTP request at a time.
