CSV Split
============

CSV Split will split a csv file based on the values in a column and store the results in separate files.

Look how easy it is to use::

    $ csvsplit --help
    $ csvsplit sample --help
    $ csvsplit loader --help

Features
--------

- Todo: Coming Soon

Installation
------------

Install csvsplit CLI by running::

    $ cd /path/to/project/
    $ python3 -m venv csvsplit
    $ cd csvsplit
    $ source bin/activate
    $ pip install --upgrade pip  # (optional step)
    $ pip install git+https://github.com/wjdecorte/csvsplit.git@master


Examples
----------

CLI command examples::

    $ csvsplit --help   # display the command help

    $ csvsplit <sub-command> --help   # help for a specific sub-command

    # Create 4 sample files that start with the prefix sample_data
    $ csvsplit sample /path/to/source/data --file-count=4 --file-prefix=sample_data

    # Load the sample files
    $ csvsplit loader /path/to/source/data /path/to/target/data

Contribute
----------

- Issue Tracker: `<https://github.com/wjdecorte/csvsplit/issues>`_
- Source Code: `<https://github.com/wjdecorte/csvsplit>`_

Support
-------

If you are having questions, please contact the author at `jdecorte@decorteindustries.com <mailto:jdecorte@decorteindustries.com>`_.

License
-------

The project is licensed under the <TBD> license.

