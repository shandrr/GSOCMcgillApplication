# Google Summer of Code: Mcgill Application

This is a simple Python program written for a Google Summer of Code application with Mcgill Space Institute.
The requirements can be found at http://msi.mcgill.ca/Lightcurve_modeling_with_Icarus.html.

Those who wish to contribute are asked not to do so, as this is a personal project.

## License

This software is licensed under the [MIT License (MIT)](LICENSE).

## Requirements

The program requires Python 2.7x and matplotlib to be installed.
Docstrings use Epydoc, which is needed to display them properly.

## Execution

To run the program, enter the directory of the README and type

python ./mcgill_app/main.py

in the command prompt. Alternatively, simply run main.py in the mcgill_app directory.

## Questions about Assignment

* I'm not sure what accuracy constants should be to. I've left most of them to 9 significant figures.
* My results for the star's U, B, V and R magnitudes deviate ever so slightly from the values in the provided app. It may be due to erroneous constant values, but is there a better way to calculate the result?