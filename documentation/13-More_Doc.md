# 13. More Doc

## Added value

#### Language choice
Our choice of Python for implementation makes this section significant. The syntax and idioms along with the
rich standard library in Python mean that a lot of implementation will differ considerably when compared to
traditional languages such as Java or C++. It is also extremely important to highlight that Python is a
duck-typed language.

Although types are never declared; in Python this is not a problem. Most standard classes have very common
behaviour and almost always rely on the rich standard data types.

This also means that interfaces are practically non existent, at least in a traditional sense. Interfaces are
implicit in that:

> If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.

This allows the language to have a very rich type system without the compexity of inheritance hierarchys.
Python always favours object composition over inheritance.

#### Framework and extensions choice
We used **Flask** extensively for this project. Flask is a micro web framework written in Python. It is extremely
simple to start with and makes great use of common Python idioms.
Both Pinterest and the former US President Obama's 2012 campaign were implemented using Flask.

Our choice of frameworks allowed for rapid development when contrasted with other languages and frameworks such
as Enterprise Java Beans and JavaServer Faces. It is uncommon to use the framework without extensions so they
used extensions are described below.


- ###### Database
  Our project is backed by a MySQL database. The **PyMySQL** client is used for connections.
  Both **SQLAlchemy** and its counterpart **Flask-SQLAlchemy** provide a flexible **Object Relational Mapper
  (ORM)**.

  When contrasted with other ORMs such as the Java Persistance API; SQLAlchemy shines with its simplicity.
  Typically the entity classes used in a Java project are auto generated from a database schema due to the
  complicated syntax required to do it manually. Entity classes in SQLAlchemy can be written in a simple text
  editor. Once the application runs, all the tables are generated in the database if they don't already exist.

- ###### REST API
  By default, the Flask interface mainly supports frontend requests. To implement the REST API we used Both
  **Flask-RESTful** and **Flask-HTTPAuth**. Flask-RESTful provides a similar, but nicer interface for designing
  REST APIs which typically have multiple request methods. Whilst we implemented authorisation ourselves,
  for the REST API we used Flask-HTTPAuth for basic HTTP authentication.

- ###### Forms
  We used **Flask-WTF** to create classes representing forms throughout the application. It provides many
  validators that would be considered trivial to implement as well as the flexibility to add other validators.
  This also helped us to decouple validation from both contollers and the API layer in a consistent fashion.

- ###### Graphical User Interface
  Whilst this was not the focus of our project; it still demonstrates MVC and a flexible framework choice.
  Flask uses a templating engine called **Jinja** which is extremely powerful. It allows template inheritance
  and has and automatic HTML escaping system for **cross site scripting prevention**.
  It uses just in time compilation of the template to Python bytecode ensuring high performance.
  We also used **Flask-Bootstrap** as it both applied a consistent style to the frontend but also allowed us
  to focus on the business layer rather than the CSS. It also integrates with our WTForms and renders them.

- ###### Unit Testing
  Since Python is a duck-typed language we do not have the benefit of a complier like in Java or C++.
  Errors often don't appear until run time. For this reason it is important to have a sufficient level of
  statement coverage in unit tests. We used the **Nose** testing framework as a token acknowledgement of this
  fact.


#### Security
**Function level access control** is implemented on a roles/permissions basis. Implementation details are
described in the decorator and factory design patterns section.
The project is SQL injection safe. The ORM handles this when persisting object data. All other queries use
prepared statements.
It is also safe against Cross-Site Request Forgery (CSRF) attacks in all forms as a token is placed in a hidden
field and validated on submission.

#### Version Control and Project Management
We used Git for version control throughout the project. This ensured that changes could be merged with relative
easy. We also used an online Kanban board to manage assiged tasks and backlogs as well as to provide a point of
discussion if any ambiguities arised with a task. This is an Agile methodology.

#### Dependency Management
Since we made extensive use of many third party frameworks and extensions; we needed to manage our dependencies.
We maintained a dependency file which locked the tested versions of each package. This not only ensured that
everybody would always have the requirements to run the project but also in the context of an enterprise system
the project could be deployed in any environment.

As well as managing dependencies for packages, we must also manage configuration for different environments.
The project allows for a different configuration to be injected through an app **factory**. This allows the
project to execute with development, testing or production configurations. A simple example is the database
configuration. The testing configuration specifies that a temporary in-memory database should be created.
Rollbacks can be performed between tests whilst not impacting our production or development databases.
Our choice of ORM allows for this flexibility.


## Patterns Used
Design patterns in Python are quite interesting. Many of the principles and patterns discussed in by the Gang of
Four disolve until there is little left. This is partly due to the design philosophy of the language and its
syntax.

#### Model View Contoller
Using MVC and a three tiered architecture allowed us to make **highly cohesive modules**.
The Flask framework permitted us to implement MVC eligantly.
The project exposes a frontend as well as a REST API. The controllers are extremely light weight. The user makes
a request through one of the endpoints. If the request is on the frontend; necessary inputs are retreived and
validation is performed if required. The contoller then delegates to the appropriate API level classes which
perform all interactions with the model. Once the result is returned to the controller it is inserted into
a template and finally returned to the user.

A request to the REST API performs similarly, only without the templates. Python provides a dictionary data
type which can be converted into JSON. A REST API allows our service to be used by potentially another web
site such as a central booking site for a **chain of hotels**. We made this design decision as it is common
for a hotel to have their own web site but also because every hotel has no direct relation with another.
This means that each hotel can have its own database (even if they reside on the same server). This is a much
more scalable solution.

#### Null Design Pattern
Whilst this is a rather simple pattern we implemented this so as to avoid unnecessary checks and to improve
consistency. For a typical hotel reservation system users may or may not authenticate. This can be a problem
when trying to query the current user for e.g. their role when managing access contol. The solution was to
create a user representation and set its role to anonymous.

#### Observer Design Pattern
TODO

#### Factory Design Pattern
The factory design pattern is used in 3 places. As discussed previously in dependency management; a factory
is used to create an app with different configurations for particular environments.
Factories are also used for roles and permissions. Roles and permissions both exist as enums in our code.
By using a factory, when we want an object of a particular role or permission; passing an enum value into
the factory method will search the database for it. SQLAlchemy will return the correct object. If such a
role or permission does not exist a new instance will be created. This will only persist in the database
when another entity with a relation to it is persisted. In effect, this allows us to 'lazy load' both roles
and permissions as required. This also means that the project will run without a pre-populated database and
future modifications will not require manual database changes.

#### Decorator Design Pattern
Python has in-built support for decorators. It provides syntactic sugar which makes them very intuitive to use.
This is the most interesting and most extensively used pattern in the project.

It should be mentioned that Python, unlike Java or C++, does not enforce any access control on member variables.
Although, it is convention to prefix "private" members with an underscore, but it is purely convention.
Traditional setters and getters are also completely againsts Python convention. Direct attribute access is
expected. But this is not always ideal. That leads to a use of decorators in Python. We may give an interface
that behaves like direct attribute access but call a method instead. This is known as a **descriptor decorator**
and is used extensively throughout the project.

~~~Python
  class User():

      @property                     # Getter descriptor decorator
      def first_name(self):
          return self._first_name

      @first_name.setter            # Setter descriptor decorator
      def first_name(self, value):
          self._first_name = value

  # Client expects direct attribute access
  user = User()
  user.first_name = 'Tom'
  print(user.first_name)
~~~

Whilst this decorator is provided by Python, we also implemented our own.

Decorators are extremely powerful for writing cohesive code. They modify a call to another method by wrapping
it with another function/method/class wrapper. This can be used for many things; but 2 brilliant examples are
implementing a cache and access control.

Below is a role based access control decorator.

~~~Python
  # This is commonly implemented as a function, but a method similar to java could be used too
  def user_can(*permissions):   # evaluates parameters and creates/returns a decorator
      def decorator(f):         # executes when a decorated function is called, function is passed
          @functools.wraps(f)   # Modify the new function metadata to match the original function
          def decorated(*args, **kwargs):   # The new decorated function
              if not any(AccessManager.user_has_permission(p) for p in permissions):
                  raise UserIsNotPermitted
              return f(*args, **kwargs)
          return decorated
      return decorator

  # Examples:
  @app.route('/booking/booking', methods=['GET', 'POST'])
  @user_can(['MAKE_BOOKING', 'MAKE_BOOKING_OTHER'])  # Either or
  def book_room():
      print('Either permission required')

  @app.route('/booking/company_booking', methods=['GET', 'POST'])
  @user_can('MAKE_COMPANY_BOOKING')
  @user_can(['MAKE_BOOKING', 'MAKE_BOOKING_OTHER'])  # Compound condition
  def book_company():
      print('The user can make comany bookings and either other
            permission required')
~~~

The above example also includes a route decorator provided by Flask for defining a url endpoint for a controller.
The decorator syntax should not be confused with annotations in Java.
