# Google Summer of Code: Mcgill Application

This is a piece of Python code written for an application with Mcgill.
The requirements can be found at http://msi.mcgill.ca/Lightcurve_modeling_with_Icarus.html.

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
* I was unsure of how to calculate the star's magnitude without its temperature or using another reference star.
    * My implementation ended up assuming the star's temperature from an HR diagram and using Vega as a reference, assuming it has a magnitude of 0 and is a black body.
    * How would this be done in general? I read lecture slides from various astrophysics courses, and cobbled what I found together, but I remain unsure.