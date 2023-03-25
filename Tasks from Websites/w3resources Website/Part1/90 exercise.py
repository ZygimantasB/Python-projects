# 90. Write a Python program to create a copy of its own source code.

def file_copy(src, dest):
    with open(src) as f, open(dest, 'w') as d:
        d.write(f.read())
        file_copy("untitled0.py", "z.py")
        with open('z.py', 'r') as filehandle:
            for line in filehandle:
                print(line, end = '')
