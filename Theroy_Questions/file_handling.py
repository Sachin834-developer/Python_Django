
"""
f=open('demo.txt','r')
print(f.mode)
f.close()


Content Managers: its benefits of the using these is to allow us to work with 
files with the block.  once exit the block they 
automatically close the file.
this will also closes the file when an exceptions thrown

internaly __entry__()   and __ exit__() methods gets called when 
using context manager "with".
"""
with open('demo.txt','w') as f:
    f.write('let write something to the file')
    # f_contents=f.read()
    # print(f_contents)

print(f.closed)

# 4. Working with Files
# Problem: Read a file, process its contents, and write the results to another file.
# Example:
def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    processed_lines = [line.upper() for line in lines]
    
    with open(output_file, 'w') as f:
        f.writelines(processed_lines)

process_file('input.txt', 'output.txt')
# Solution: Use Python's open(), read(), and write() methods for file handling.