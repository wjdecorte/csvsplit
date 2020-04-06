NaviLoader
============

NaviLoader will process all source files in JSON format saved in the
source data directory and save without duplicates in the target data directory.

Look how easy it is to use::

    $ naviload --help
    $ naviload sample --help
    $ naviload loader --help

Features
--------

- Create sample data for testing
- Saves data in date specific files in `Parquet <https://parquet.apache.org/>`_ format
- Removes any duplicate records

Installation
------------

Install naviload CLI by running::

    $ cd /path/to/project/
    $ python3 -m venv naviloader
    $ cd naviloader
    $ source bin/activate
    $ pip install --upgrade pip
    $ pip install git+https://github.com/wjdecorte/naviloader.git@master


Examples
----------

CLI command examples::

    $ naviload --help   # display the command help

    $ naviload <sub-command> --help   # help for a specific sub-command

    # Create 4 sample files that start with the prefix sample_data
    $ naviload sample /path/to/source/data --file-count=4 --file-prefix=sample_data

    # Load the sample files
    $ naviload loader /path/to/source/data /path/to/target/data

Contribute
----------

- Issue Tracker: `<https://github.com/wjdecorte/naviloader/issues>`_
- Source Code: `<https://github.com/wjdecorte/naviloader>`_

Support
-------

If you are having questions, please contact the author at `jdecorte@decorteindustries.com <mailto:jdecorte@decorteindustries.com>`_.

License
-------

The project is licensed under the <TBD> license.

