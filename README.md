# LogN - Log Ninja

A tool to log/document my life.

## Currently supports

* Movies

## Future plans

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

    git clone https://github.com/MiteshNinja/logninja 
    cd logninja
    virtualenv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

Done.

## How to use?

Initialise the databse first.

    logn initdb

Feel free to add movies now:

    logn add <string:MOVIE NAME>  <number:your_personal_rating>
