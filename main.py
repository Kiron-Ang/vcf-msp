# This program uses Python programming
# Here, you will find various functions to 
# Modify VCF files based on information
# from a corresponding MSP file


def find_start(path_to_file):
    """Function to find the column titles in an MSP/VCF file"""

    # Open the file for reading only
    opened_file = open(path_to_file, "r", encoding="utf-8")

    # First line is considered line number "0"
    start = 0

    # Iterate over every line in the file
    for line in opened_file:

        # VCF and MSP files start with a chromosome column        
        if "#c" in line.casefold():
            opened_file.close()
            print(path_to_file, "starts at line number", start)
            return start
        else:
            start += 1


def find_first_person(path_to_file, find_start_result):
    """
    Function to find the index of the first person when each row is
    converted to a list. Use in conjunction with find_start()
    """

    # Open the file for reading only
    opened_file = open(path_to_file, "r", encoding="utf-8")

    # First item in the list is considered item number "0"
    start = 0

    lines_list = opened_file.readlines()
    column_titles_list = lines_list[find_start_result].split("\t")

    # Iterate over every column title until you find a number
    for title in column_titles_list:
        # VCF and MSP files designate people with numbers        
        if title[0].isdigit():
            opened_file.close()
            print(path_to_file, "begins describing people information in column", start)
            return start
        else:
            start += 1


def replace_dot_using_ancestry(path_to_vcf, path_to_msp, ancestry_in_msp):
    """
    Function to replace numbers in a VCF file with '.' given an MSP file
    and the number that represents the ancestry of interest in the MSP
    """

    # Open the two files in a mode for reading AND writing
    # Please use "r+" because "w" will replace the file
    opened_vcf = open(path_to_vcf, "r+", encoding="utf-8")
    opened_msp = open(path_to_msp, "r+", encoding="utf-8")

    # Create lists where every item is a line
    vcf_lines_list = opened_vcf.readlines()
    msp_lines_list = opened_msp.readlines()

    # Call find_start() function to determine where to begin
    vcf_start = find_start(path_to_vcf)
    msp_start = find_start(path_to_msp)

    # Figure out the index of the first person for both files
    vcf_people = find_first_person(path_to_vcf, vcf_start)
    msp_people = find_first_person(path_to_msp, msp_start)

    # vcf_start and msp_start will represent the current line that the program
    # is looking at from this point on
    vcf_start += 1
    msp_start += 1

    vcf_lines_list = vcf_lines_list[vcf_start:len(vcf_lines_list)]
    for line in vcf_lines_list:
        print(line)

    # TODO: Process the column names
    # TODO: Match the current row in the VCF file with a range in the MSP file	

    # Close the two files
    opened_vcf.close()
    opened_msp.close()


if __name__ == "__main__":
    # Import the sys module for accessing command-line arguments
    import sys
    print("Importing sys")

    # Check if the required arguments were specified
    if len(sys.argv) < 3:
        print("Error: Please provide the VCF and MSP paths as arguments.")
        print("Usage: python this_script.py <VCF_path> <MSP_path>")
        sys.exit(1)

    # Confirm the current Python version and the name of this script
    print(f"Executing the script named {sys.argv[0]} with Python",
          f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}",
          f"{sys.version_info[3]} {sys.version_info[4]}")

    # Print confirmation messages for VCF and MSP file paths
    vcf_path = sys.argv[1]
    msp_path = sys.argv[2]
    print("The path of the VCF file you specified:", vcf_path)
    print("The path of the MSP file you specified:", msp_path)
    
    # Call the desired vcf-msp function
    replace_dot_using_ancestry(vcf_path, msp_path, 0)
