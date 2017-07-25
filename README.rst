pyfttt
======

Python tools for interacting with IFTTT Webhooks Channel.

Installation
------------

::

    pip install pyfttt

Command Line Tool
-----------------

``pyfttt`` is an included command line tool for sending Webhooks Channel
events. To see a list of available arguments, run ``pyfttt --help``,
which produces:

::

    usage: pyfttt [-h] [--version] [-k K] -e E [value1] [value2] [value3]

    Send Webhooks Channel events to IFTTT

    optional arguments:
      -h, --help       show this help message and exit
      --version        show program's version number and exit

    sending events:
      -k K, --key K    IFTTT secret key
      -e E, --event E  The name of the event to trigger
      value1           Extra data sent with the event (optional)
      value2           Extra data sent with the event (optional)
      value3           Extra data sent with the event (optional)

    Visit https://ifttt.com/channels/maker_webhooks for more information

The ``--key`` argument can be omittrd if the IFTTT secret key is defined
in the environment as ``IFTTT_API_KEY``.

Requirements
------------

-  Python 2.7 or greater
-  `requests <https://pypi.python.org/pypi/requests>`__

License
-------

pyfttt is released under the BSD 2-clause license. See
`LICENSE <https://raw.githubusercontent.com/briandconnelly/pyfttt/master/LICENSE>`__
for details.
