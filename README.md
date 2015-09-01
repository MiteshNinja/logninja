# LogN - Log Ninja

A tool to log/document my life.

### Currently supports

* Movies

### Future plans

* Flexible
* Logs everything
* Makes graphs/charts
* Encrypted databse
* Online Sync
* Easy to use

## Initial Idea

Build a complete open-source logging utility in Python; which is flexible, 
extensible, and customizable.

Key features:

* add data
* remove data
* shift data
* ~~plain text format~~
    * using sqlite3 now

## Why do I need this?

Simply because DATA IS BEAUTIFUL.
Also, I like documenting/tracking/logging things.

## Install

LogNinja needs Python 3.x

Clone this repository
    
    git clone https://github.com/MiteshNinja/logninja 

Change current working directory to 'logninja'

    cd logninja

Optional but highly recommended: Setup a virtualenv(ironment) and activate it.

    virtualenv venv
    source venv/bin/activate

Install the requirements

    pip3 install -r requirements.txt

Done.

## How to use?

Initialise the databse first.

    logn initdb

Feel free to add movies now:

    logn add <string:MOVIE NAME>  <number:your_personal_rating>
