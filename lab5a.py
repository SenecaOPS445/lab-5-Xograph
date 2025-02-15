#!/usr/bin/env python3
# Author ID: kho55

def read_file_string(file_name):
    file = open(file_name, 'r')
    return file.read()
    # Takes file_name as string for a file name, returns its entire contents as a string

def read_file_list(file_name):
    file = open(file_name, 'r')
    content = []
    for line in file:
        content.append(line.strip())
    return content
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))