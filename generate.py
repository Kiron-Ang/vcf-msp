# This is a Python program for generating fake VCF and MSP files to test
# how long the functions in main.py take to execute
# The output files will be vcf.txt and msp.txt
# Use small_vcf.txt and small_msp.txt if you want to understand the functions

# Import random for random positions
import random
print("Importing random...")

print("Writing test VCF file in vcf.txt...")
# Open a new file in write mode
vcf = open("vcf.txt", "w")

info_lines = random.randrange(20)
for line in range(info_lines):
    vcf.write(f"##INFORMATION LINE {line}\n")

vcf.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t")

# Each variant will have data for 1000 people
for person in range(0, 1000):
    vcf.write(f"{person}_{person}\t")

# Create a variable to keep track of the positions of the variants
# since variants are listed in order of position in real VCF files
variant_position = 0

# The VCF test file will have 1000 variants
for line in range(0, 1000):
    vcf.write("\n1\t")
    variant_position += random.randrange(100)
    vcf.write(f"{variant_position}\t")
    vcf.write("NONE\tNONE\tNONE\tNONE\tNONE\tNONE\tNONE\t")

    # Each variant will have 1000 people
    for person in range(0, 1000):
        first_number = random.randrange(2)
        second_number = random.randrange(2)
        vcf.write(f"{first_number}|{second_number}\t")

# ALWAYS CLOSE YOUR FILES
vcf.close()



# Now write the MSP file
print("Writing test MSP file in msp.txt...")
msp = open("msp.txt", "w")

msp.write("#SUBPOPULATION INFORMATION LINE 1\n")
msp.write("#chm\tspos\tepos\tsgpos\tegpos\tn snps\t")

# Each tract will have data for 1000 people
for person in range(0, 1000):
    msp.write(f"{person}_{person}.0\t")
    msp.write(f"{person}_{person}.1\t")

# Create a variable to keep track of the tract positions
tract_position = 0

# The MSP test file will have 1000 tracts
for line in range(0, 1000):
    msp.write("\n1\t")

    # Write the spos for the tract
    tract_position += random.randrange(200)
    msp.write(f"{tract_position}\t")

    # Each tract is at least 100 base pairs long
    # write the epos for the tract
    tract_position += random.randrange(100, 200)
    msp.write(f"{tract_position}\t")

    msp.write("NONE\tNONE\tNONE\t")

    for person in range(0, 1000):
        first_number = random.randrange(5)
        second_number = random.randrange(5)
        msp.write(f"{first_number}\t")
        msp.write(f"{second_number}\t")



# ALWAYS CLOSE YOUR FILES
msp.close()