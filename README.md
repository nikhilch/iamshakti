# Website for I-AM Shakti

This is the official repository for the [I-AM Shakti](https://www.iamshakti.org) website.


# Gearing up for Development

### Setting up your Directories

Make sure you have `python3`, `pip3`, and `virtualenv` installed on your machine before getting started. In Ubuntu 18.04, this can be done as follows (python3 should be installed already):

```
$ sudo apt-get install python-pip3 virtualenv
```

Starting with your favorite bash terminal, run the following commands:

1. Clone the repo: `git clone https://github.com/nikhilch/iamshakti.git`
1. Go in the repo: `cd iamshakti`
1. Create a virtual environment: `virtualenv --python=python3 shakti-venv`
1. Get virtual: `source shakti-venv/bin/activate`
1. Install dependencies: `pip3 install -r requirements.txt`
1. Get the yummy secret file from Nikhil


### The Juicy Stuff

While in the `shakti-venv` virtual environment, run `python3 manage.py runserver` and point your browser to <http://localhost:8000/iamshakti/>. 
