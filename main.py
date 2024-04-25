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


def find_column_title(path_to_file, find_start_result, title_name):
    """
    Function to find the index of a column title when each row in
    a VCF or MSP is converted to a list. Use in conjunction with find_start()
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
        if title.casefold() == title_name:
            opened_file.close()
            print(path_to_file, f"has {title_name} in column", start)
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

    # Open a new file that will contain the VCF modifications
    new_vcf = open("new_vcf.txt", "w", encoding="utf-8")

    # Create lists where every item is a line
    vcf_lines_list = opened_vcf.readlines()
    msp_lines_list = opened_msp.readlines()

    # Call find_start() function to determine where to begin
    # This variable will change
    vcf_start = find_start(path_to_vcf)
    msp_start = find_start(path_to_msp)

    # Figure out the index of the first person for both files
    # This variable will not change
    vcf_people = find_first_person(path_to_vcf, vcf_start)
    msp_people = find_first_person(path_to_msp, msp_start)

    # Figure out the index of the variant position in the VCF
    # This variable will not change
    vcf_pos = find_column_title(path_to_vcf, vcf_start, "pos")

    # Figure out the index of the start and end positions for the tracts in
    # the MSP file. This variable will not change
    msp_spos = find_column_title(path_to_msp, msp_start, "spos")
    msp_epos = find_column_title(path_to_msp, msp_start, "epos")

    # vcf_start and msp_start will represent the current line that the program
    # is looking at from this point on

    vcf_start += 1
    msp_start += 1

    vcf_lines_list = vcf_lines_list[vcf_start:len(vcf_lines_list)]
    msp_lines_list = msp_lines_list[msp_start:len(msp_lines_list)]

    vcf_start = 0
    msp_start = 0
    
    msp_spos_value = int(msp_lines_list[msp_start].split("\t")[msp_spos])
    msp_epos_value = int(msp_lines_list[msp_start].split("\t")[msp_epos])

    print("msp_spos_value is", msp_spos_value)
    print("msp_epos_value is", msp_epos_value)

    # Keep going until all lines in VCF have been modified
    for line in vcf_lines_list:
        vcf_values_list = line.split("\t")
        variant_position = int(vcf_values_list[vcf_pos])
        print("looking at the variant at position", variant_position)

        belongs = False
        # Keep checking to see which tract a variant belongs to
        # Note that we don't have to start from the beginning of the MSP
        # file every time because the tracts are sequentially listed
        while belongs is False:
            print(f"Current range is between {msp_spos_value} and {msp_epos_value}") 
            if msp_spos_value < variant_position < msp_epos_value:
                print(f"Variant between {msp_spos_value} & {msp_epos_value}")
                belongs = True
            else:
                # Before moving onto the next tract range, we also have to see
                # whether the variant exists in between ranges (does not 
                # belong in any of the ranges)
                msp_start += 1
                try:
                    msp_spos_value = int(msp_lines_list[msp_start].split("\t")[msp_spos])
                except:
                    print("End of MSP ranges reached! Program exiting now...")
                    exit()
                if msp_epos_value < variant_position < msp_spos_value:
                    print("This variant doesn't belong anywhere!")
                    msp_start -= 1
                    msp_epos_value = int(msp_lines_list[msp_start].split("\t")[msp_epos])
                    break
                
                msp_epos_value = int(msp_lines_list[msp_start].split("\t")[msp_epos])
        if belongs is True:
            new_vcf.write(f"TRUE {variant_position}\n")
        else:
            new_vcf.write(f"FALSE {variant_position}\n")
        

    # Close the three files
    opened_vcf.close()
    opened_msp.close()
    new_vcf.close()


# Run the following code if this file is the file that is directly executed
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
