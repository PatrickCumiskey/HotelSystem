# 6. Requirements

## Tactics to support specific quality attributes
We decided to use Python for this system as it is portable and has very rich modules. Some team members have gained prior experience with many of these modules, but they are also very accessible to members who are new to the language too.

By implementing the Model View Controller architectural pattern we will develop modular components with well defined interfaces. Our graphical user interface will be completely separate from our business logic. This makes it much easier to provide a REST API with the same business logic as the website or any other clients we implement. This will also help with maintainability.

We decided to use the Flask web development framework for both our GUI and REST API. It is a simple framework which works great for Model View Controller.

For both security and usability a role/permission based system is required for various functions.

We are taking the Agile approach to software development. Iterative releases will help ensure we are writing extensible software. We should be able to add features without having to make large changes very often. We will continuously integrate using git and we will always have a working code base.

In order to support many devices and operating systems we decided to create our GUI using web technologies.
