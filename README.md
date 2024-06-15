# vcf-msp-fb

This repository contains Python/R/C++ code for working with VCF, MSP, and FB files. It is used and maintained by the Reynolds Lab at Baylor University.

## What the project does

There are two scripts available for use:

- ``main.py``: Various functions for working with VCF, MSP, and FB files in Python
  - Run ``main.py`` by using the command line: ``python main.py [path_to_VCF_file] [path_to_MSP_file]``
  - Make sure to edit main.py first to use the function that you want!
  - ``replace_dot_using_ancestry(vcf_path, msp_path, ancestry_in_msp)`` will replace individuals' information in a VCF file with a "." if the ancestry for that individual in the corresponding MSP file does not match ``ancestry_in_msp``

- ``generate.py``: Create a random VCF file and its corresponding random MSP file
  - Run ``generate.py`` by using the command line: ``python generate.py [number_of_individuals] [number_of_variants] [number_of_tracts]``
  - ``generate_vcf(individuals, variants)`` makes a random VCF file; ``generate_msp(individuals, tracts)`` makes a random MSP file.



## Why the project is useful

Although making custom programs to work with VCF files is generally frowned upon because of the volatile development history of the VCF format, not all problems in computational biology can be resolved with the same modules in the same package. Furthermore, with all the different formats that researchers use, there is no reasonable way to expect a single development team at a university to respond to every request from researchers. A repository for active researchers and by active researchers resolves this problem.

## How users can get started with the project

If you'd like to contribute, please create a pull request on the GitHub page for this project! You can also email Kiron at kiron_ang1@baylor.edu.

## Where users can get help with the project

If you need help, please create an issue on the GitHub page for this project! You can also email Kiron at kiron_ang1@baylor.edu

## Who maintains and contributes to the project

- Kiron Ang: https://github.com/Kiron-Ang, kiron_ang1@baylor.edu
- Fernanda Mirón: https://github.com/fernanda-miron, fernanda_miron1@baylor.edu