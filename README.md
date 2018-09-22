# slowloris.py - Simple slowloris in Python

## Slowloris?
Slowloris is basically an HTTP DoS attack that affects threaded servers. How it works:

1. Makes lots of HTTP requests.
2. Send headers periodically to keep the connections open.
3. Never close the connection unless the server does so, if it does, open a new one and keep doing the same thing

Eexhausts the servers thread pool and the server can't reply to other people.

## Installation and running?

You can clone the git repo. Here's how you run it.

### Method 1:

* `git clone https://github.com/thisisyomans/slowlorispy2.git`
* `cd type1_urlarg` <<<<< do this inside of slowlorispy2 directory
* `python3 slowloris.py sitename.com` OR `python slowloris.py sitename.com`
* python3 vs python depends on your Python 3 PATH/environment variable

### Method 2:

* `git clone https://github.com/thisisyomans/slowlorispy2.git`
* `cd type2_script` <<<<< do this inside of slowlorispy2 directory
* `python3 example.py` OR `python example.py`
* python3 vs python depends on your Python 3 PATH/environment variable
* you must edit the site's domain from within the `example.py` file

### SOCKS5 proxy support

However, if you plan on using the `-x` option in order to use a SOCKS5 proxy for connecting instead of a direct connection over your IP address, you will need to install the `PySocks` library (or any other implementation of the `socks` library) as well. [`PySocks`](https://github.com/Anorov/PySocks) is a fork from [`SocksiPy`](http://socksipy.sourceforge.net/) by GitHub user @Anorov and can easily be installed by adding `PySocks` to the `pip` command above or running it again like so:

* `sudo pip3 install PySocks` OR `sudo pip install PySocks`
* pip3 (python3) vs pip (python) depends on your Python 3 PATH/environment variable

You can then use the `-x` option to activate SOCKS5 support and the `--proxy-host` and `--proxy-port` option to specify the SOCKS5 proxy host and its port, if they are different from the standard `127.0.0.1:8080`.

## Configuration options
It is possible to modify the behaviour of slowloris with command-line arguments.

## License
The code is licensed under the MIT License.
