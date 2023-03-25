 # Exercise 10: Read line number 4 from the following file

file_path = r"G:\My Drive\Python programing learn\pynative\Pynative\Input and Output Exercise\test.txt"

with open(file_path, 'r') as real_line:
    read_all_lines = real_line.readlines()
    print(read_all_lines[3])
