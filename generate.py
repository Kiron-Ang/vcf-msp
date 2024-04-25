# This is a Python program for generating fake VCF and MSP files to test
# how long the functions in main.py take to execute
# The output files will be vcf.txt and msp.txt
# Use small_vcf.txt and small_msp.txt if you want to understand the functions

# Import random for random positions
import random
print("Importing random...")


def generate_vcf(individuals, variants):
    """
    Function to generate a random VCF file for testing
    """
    print("Writing test VCF file in vcf.txt...")
    # Open a new file in write mode
    vcf = open("vcf.txt", "w")

    info_lines = random.randrange(20)

    for line in range(info_lines):
        vcf.write(f"##INFORMATION LINE {line}\n")

    vcf.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t")

    # Each variant will have data for "individuals" people
    # This will add columns
    for person in range(0, individuals):
        vcf.write(f"{person}_{person}\t")

    # Create a variable to keep track of the positions of the variants
    # since variants are listed in order of position in real VCF files
    variant_position = 0

    # The VCF test file will have "variants" variants
    for line in range(0, variants):
        print("Writing variant number", line)
        vcf.write("\n1\t")
        variant_position += random.randrange(100)
        vcf.write(f"{variant_position}\t")
        vcf.write("NONE\tNONE\tNONE\tNONE\tNONE\tNONE\tNONE\t")

        # Each variant will have "individuals" people
        for person in range(0, individuals):
            first_number = random.randrange(2)
            second_number = random.randrange(2)
            vcf.write(f"{first_number}|{second_number}\t")

    # ALWAYS CLOSE YOUR FILES
    vcf.close()


def generate_msp(individuals, tracts):
    """
    Function to generate a random MSP file for testing
    """

    print("Writing test MSP file in msp.txt...")
    msp = open("msp.txt", "w")

    msp.write("#SUBPOPULATION INFORMATION LINE 1\n")
    msp.write("#chm\tspos\tepos\tsgpos\tegpos\tn snps\t")

    # Each tract will have data for "individuals" people
    # This will add columns
    for person in range(0, individuals):
        msp.write(f"{person}_{person}.0\t")
        msp.write(f"{person}_{person}.1\t")

    # Create a variable to keep track of the tract positions
    tract_position = 0

    # The MSP test file will have "tracts" tracts
    for line in range(0, tracts):
        print("Writing tract number", line)
        msp.write("\n1\t")

        # Write the spos for the tract
        tract_position += random.randrange(200)
        msp.write(f"{tract_position}\t")
    
        # Each tract is at least 100 base pairs long
        # Write the epos for the tract
        tract_position += random.randrange(100, 200)
        msp.write(f"{tract_position}\t")

        msp.write("NONE\tNONE\tNONE\t")

        for person in range(0, individuals):
            first_number = random.randrange(5)
            second_number = random.randrange(5)
            msp.write(f"{first_number}\t")
            msp.write(f"{second_number}\t")

    # ALWAYS CLOSE YOUR FILES
    msp.close()


# Run the following code if this file is the file that is directly executed
if __name__ == "__main__":
    # Import the sys module for accessing command-line arguments
    import sys
    print("Importing sys")

    # Import the time module for timing execution
    import time
    print("Importing time")

    # Check if the required arguments were specified
    if len(sys.argv) < 4:
        print("Error: Please provide the number of individuals, variants, and tracts as arguments.")
        print("Usage: python generate.py <individuals> <variants> <tracts>")
        sys.exit(1)

    # Confirm the current Python version and the name of this script
    print(f"Executing the script named {sys.argv[0]} with Python",
          f"{sys.version_info[0]}.{sys.version_info[1]}.",
          f"{sys.version_info[2]} {sys.version_info[3]} "
          f"{sys.version_info[4]}")

    # Print confirmation messages for VCF and MSP file paths
    individuals = int(sys.argv[1])
    variants = int(sys.argv[2])
    tracts = int(sys.argv[3])
    print("Individuals:", individuals)
    print("Variants:", variants)
    print("Tracts:", tracts)
    
    start_time = time.time()
    print("The start time is:", start_time)

    generate_vcf(individuals, variants)
    generate_msp(individuals, tracts)

    end_time = time.time()
    print("The end time is:", end_time)
    print("Total time elapsed in seconds:", end_time - start_time)

