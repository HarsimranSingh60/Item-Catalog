# Item Catalog Project, Project of Udacity Full Stack Web Developer-II Nanodegree.

## What it is and does

Restaurant Menu App for Item catalog project This is a python module that creates a website and JSON API for a list of restaurants. Each restaurant displays their menus and also provides user authentication using Google. Registered users will have ability to edit and delete their own items. This application uses Flask, SQL Alchemy, JQuery, CSS, Javascript, and OAuth2 to create Item catalog website.

## Installation 
1. VirtualBox
2. Vagrant 
3. python 3.6

## Instructions to Run the project

Setting up OAuth 2.0

1. You will need to signup for a google account and set up a client id and secret.
2. Visit http://console.developers.google.com for google setup.

## Setting up the Environment

1. Clone or download the repo into vagrant environment.
2. Type command vagrant up, vagrant ssh.
3. In VM, cd /vagrant/catalog
4. Run python database_setup.py to create the database.
5. Run Python lotsofmenus.py to add the menu items
6. Run python 'project.py'
7. open your web browser and visit http://localhost:3010/

