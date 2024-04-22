# This Python script is for the Reynolds Lab
# Here, you will find various functions to 
# Modify VCF files based on information
# from a corresponding MSP file
# This file was created by Kiron Ang
# It was last updated at 9:06 PM 4/21/2024

# Links to relevant documentation pages:
# https://docs.python.org/3/library/sys.html
# https://docs.python.org/3/tutorial/inputoutput.html
# https://docs.python.org/3/library/timeit.html

def find_start_hashtag(path_to_file):
	opened_file = open(path_to_file, "r+", encoding="utf-8")
	start_number = 0
	for line in opened_file:
		if line[0:2] == "##":
			start_number += 1
			continue
		else:
			opened_file.close()
			return start_number
		


def replace_with_dot_based_on_ancestry(path_to_vcf, path_to_msp):
	# Open the two files in a mode for reading AND writing
	# Please use "r+" because "w" will replace the file
	opened_vcf = open(path_to_vcf, "r+", encoding="utf-8")
	opened_msp = open(path_to_msp, "r+", encoding="utf-8")

	vcf_line_number = 0
	msp_line_number = 0

	# we can use for line in vcf but use a counter for msp!

	# Close the two files
	opened_vcf.close()
	opened_msp.close()


if __name__ == "__main__":
	# Import the sys module for accessing command-line arguments
	import sys

	# Print a message indicating sys module is being imported
	print("Importing sys")

	# Check if the required arguments were specified
	if len(sys.argv) < 3:
		print("Error: Please provide the VCF and MSP paths as arguments.")
		print("Usage: python this_script.py <VCF_path> <MSP_path>")
		sys.exit(1)

	# Confirm the current Python version and the name of this script
	print(f"Executing the script named {sys.argv[0]} with Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} {sys.version_info[3]} {sys.version_info[4]}")

	# Print confirmation messages for VCF and MSP file paths
	vcf_path = sys.argv[1]
	msp_path = sys.argv[2]
	print("The path of the VCF file you specified:", vcf_path)
	print("The path of the MSP file you specified:", msp_path)

	replace_with_dot_based_on_ancestry(vcf_path, msp_path)