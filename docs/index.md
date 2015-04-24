# Hammer Project

The hammer project is composed of four main components.  Each of these 
subsystems is built on the capabilities of the others.

You can utilize the features in one or more of the systems without needing
to worry about the ones you don't need.


## Docs

This system lets you set up online documents easily.  You can write simple 
documents in Markdown, and then decide how you want to share them.

Hammer Docs supports exporting to HTML (for web sites), creating a PDF with
the output, and even serving the web pages directly from a server.

Hammer Docs utilizes **mkdocs** for creating the presentation of your documents
and building the navigation structure that helps your users find things.

Hammer Docs uses **pandoc** to reformat the output into the format that you
need.


## Commands

Hammer Commands let you create scripts to automate all of the key data types
that you use in your application.

Each type of data object that you define will have a standard set of operators.
You can also add your own specific operations to extend the commands that are 
available.

The standard operations are:
 
* Add
* Edit
* List
* Show
* Delete

These operations act a starting point for you to define the code that handles
your data types.

Several standard command types are implemented for you.  These provide useful 
functionality without modification. You can modify any of this code as you 
need.

The standard commands also act as a guide for how to implment your own 
custom vocalulary.  Consider having your own custom Domain Specific Language
for the types of problems that you frequently solve.

Standard Commands:

* Doc - help to manage documents
* Tst - define and execute system tests
* Cmd - commands to automate all tasks
* App - reusable web application


## Test

The Hammer Test framework is created for easy maintenance of all system tests.
It can be used as a top level test manager for lower level test harnesses.  
It can also manage all of your tests throughout the system. You decide how to
layer the testing within your system to produce the results you want.

In 15 seconds you should be able to:

* create a new system test
* find the code for a failing test
* fix the test failure
* approve the results to accept the actual answer as the new correct answer

The Hammer Test strategy relies on verifying the actual output of each test 
rather than requiring you to know the answer ahead of time.  The system 
verifies each answer and presents the unexpected results.

You can investigate the mystery answers to decide if the answer is really 
correct after all. If the answer you got is acceptable then you can approve
it.  Now this is the new answer that will be required in the future.

Repeated test failures require a modification to the test code to ignore the
frequently changing characteristics. In practices all tests start off very
fragile and are quieted down once they become suitably irritating.


## App


