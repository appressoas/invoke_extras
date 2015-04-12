# invoke_extras
Adds functionality useful for working with Invoke.

This is very basic at the moment. The meaning of this module is to
provide functionality that we at Appresso AS miss after transitioning
from Fabric to Invoke (http://pyinvoke.org).


## Usage
We do not have a pypi package, so the easiest method of installing the package
is most likely to add the following to your requirements.txt:

```
-e git://github.com/appressoas/invoke_extras.git#egg=invoke_extras
```


## Requirements
Requires python 3. Only tested with python 3.4.


## Development
Checkout the git repo, and run:
```
$ mkvirtualenv invoke_extras
$ pip install -r requirements.txt
```

Run the tests with:
```
$ python setup.py test
```
