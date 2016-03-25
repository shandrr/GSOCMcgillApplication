# Google Summer of Code: McGill Application

This is a Python program written for a Google Summer of Code application with McGill Space Institute.
The requirements can be found at http://msi.mcgill.ca/Lightcurve_modeling_with_Icarus.html.

Those who wish to contribute are asked not to do so, as this is a personal project.

It is also requested that those also applying for the same project as the one this software is directed towards would not use the software on this repository.
(It would make little sense to do so, as the MIT license would require you to provide reference to me if you did use any of this code yourself.)

## License

This software is licensed under the [MIT License (MIT)](LICENSE).

## Requirements

The program requires Python 2.7x and matplotlib to be installed.
Documentation uses Sphinx and reStructuredText.

## Building the Documentation

To build the documentation HTML, go into the docs folder and type in the console

```bash
make html
```

This will build all required files in the subsequent _build directory.

## Installation

To install the program, enter the directory of the README and type

```bash
python setup.py install
```

in the command prompt. After this, ensure that Python27\Scripts is on your PATH.

From this point on, you will be able to invoke the program with

```bash
mcgill_app
```

in the command prompt at any time.

## Execution without installation

If you do not want to install the program, it can be executed in Python directly. First, ensure you have the latest versions of matplotlib and sphinx installed:

```bash
pip install matplotlib
pip install sphinx
```

(You should have pip installed and on your path to do this.)

After this, enter the directory of the README and type

```bash
python ./mcgill_app/main.py
```

in the command prompt. (Ensure that python is on your PATH before doing this.)