#Importing pathlib for easier location of file
from pathlib import Path

file_path = Path(__file__).resolve().parent / "junk.txt"


with open(file_path,"r") as junk:
    #Reading total lines and Counting the no of lines
    total_lines = junk.readlines()
    print(f"No of Lines: {len(total_lines)}")

with open(file_path,"a") as junk:
    #Appending a new line through Append mode
    new_line = "text file nanalyssis"
    junk.write(new_line)
    print("--> New Line Added...")

with open(file_path,"r") as junk:
    #Copying file content instead of overwriting
    lowercase_junk = junk.read().lower()

with open(file_path,"w") as junk:
    #Changing the file content into Lowercase
    junk.write(lowercase_junk)
    print("--> Changed to Lowercase...")
