### Python
- [The Python Tutorial](https://docs.python.org/3/tutorial/)
- Virtual environments (Optional but recommended)
  - Ensures that each python project has it's own dependencies
    ##### Basic Usage
    [Guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/) (Skip to virtualenvwrapper section)
    - Follow set up but store your environments somewhere together on your machine, not in the project

    ###### Create a virtual environment:

    ~~~BASH
    # install both:
    $ pip install virtualenv
    $ pip install virtualenvwrapper  # easier to use

    $ mkvirtualenv venv -p python3  # make a virtual environment called e.g. venv_python3_CS4125...
    ~~~

    ###### Work on a virtual environment:

    ~~~BASH
    $ workon venv
    ~~~

    ###### Installing modules:

    ~~~BASH
    $ pip install -r requirements.txt  # install the requirements from the file of dependencies in the project
    $ pip install flask  # install a module called flask
    ~~~

    ###### Deactivate:

    ~~~BASH
    $ deactivate
    ~~~

    ###### Delete:

    ~~~BASH
    $ rmvirtualenv venv
    ~~~

    ###### Other useful commands
    ~~~BASH
    lsvirtualenv      # List all of the environments.
    cdvirtualenv      # Navigate into the directory of the currently activated virtual environment, so you can browse its site-packages, for example.
    cdsitepackages    # Like the above, but directly into site-packages directory.
    lssitepackages    # Shows contents of site-packages directory.
    ~~~

## Flask framework
- [Simple YouTube Tutorial](https://www.youtube.com/playlist?list=PLei96ZX_m9sWQco3fwtSMqyGL-JDQo28l)

## SQLAlchemy
- [](http://flask-sqlalchemy.pocoo.org/2.1/)

## MarkDown
- [MarkDown guide](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Look at this file!

## Git
- [Basics](https://try.github.io/levels/1/challenges/1)
- Submitting a merge/pull request:
  - git checkout -b new_feature_name
  - make changes
  - add changes to stage
  - commit changes with comments
  - git push origin master:new_feature_name
  - [Merge request](https://docs.gitlab.com/ee/gitlab-basics/add-merge-request.html)

### Editors
- Up to you
- Some like PyCharm (IDE)
- I like **atom** (Cool text editor)
  - Extensions:
    - autocomplete-python
    - python-tools
    - multi-cursor
    - linter
    - linter-flake8, linter-pep8, linter-pycodestyle
    - **markdown-preview-plus**
