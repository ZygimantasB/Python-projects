# Exercise 6: Write all content of a given file into a new file by s
# kipping line number 5
# See:
#
# Python file handling
# Python Read file
# Python write file
# Create a test.txt file and add the below content to it.

with open('test.txt', 'r') as read_lines:
    read_lines1 = read_lines.readlines()

with open('new_file.txt', 'w') as read_lines:
    count = 0
    for reading_lines in read_lines1:
        if count == 4:
            count += 4
            continue
        else:
            read_lines.write(reading_lines)
        count += 1