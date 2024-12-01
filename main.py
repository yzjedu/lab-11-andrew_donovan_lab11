# Programmers:  Donovan, Andrew
# Course:  CS151,
# Due Date: november tbd
# Lab Assignment:  lab011
# Problem Statement:  Ciphers have been very popular for millenia as a way to hide information.
                      #Can you create a program to convert them back to plain English??
# Data In: file name
# Data Out:  table #, seat # and name from list
# Credits:
# Input Files: [description of the format of the input files you need for this program to work]


import os

def read_filename():
    # Prompt user for the filename to read
    name = input("What file do you want to read? ")

    # Check if the file exists, and if not, ask again until a valid file is entered
    while not os.path.isfile(name):
        print("That file does not exist. Please try again.")
        name = input("What file do you want to read? ")

    # Return the valid filename
    return name



def read_into_dict(dict_file):
    with open(dict_file, 'r') as file:
        # read the lines in the file
        lines = file.readlines()


    data_dict = {}

    # put every line into a list and take the elements to put into the dictionary
    for line in lines:
        #turn the line into a list
        line = line.strip('\n').split('  ')
        #put the values into the dictionary
        value = line[0]
        key = line[1]
        data_dict[key] = value

    file.close()

    return data_dict


def write_to_file(data_dict, filename, new_filename):
    # Open the file for reading and writing ('r+' mode)
    new_file = open(new_filename, 'w')
    with open(filename, 'r') as file_data:
        # Read the file into a list
        data = file_data.readlines()

        # Initialize the translation variable to store the translated text
        translation = ''

        # Process each line in the file
        for line in data:
            # for every code in the list line
            for code in line.split():
                # Translate the word using the dictionary, or keep it unchanged if not found
                print(code)
                letter = data_dict[code]
                translation += letter  # Add the translated letter

            # Add a space character after each translated line to make words
            translation += ' '



        new_file.write(translation)

    file_data.close()
    new_file.close()

def main():
    filename = read_filename()
    dict_file = 'morsecode.txt'
    data_dict = read_into_dict(dict_file)
    new_filename = input('what do you want to be the new file name')
    write_to_file(data_dict, filename, new_filename)


main()