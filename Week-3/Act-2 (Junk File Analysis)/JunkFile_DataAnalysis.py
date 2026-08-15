from pathlib import Path

file_path = Path(__file__).resolve().parent / "junk.txt"

with open(file_path,"r") as junk:
    total_lines = junk.readlines()
    print(f"No of Lines: {len(total_lines)}")

with open(file_path,"a") as junk:
    new_line = "text file nanalyssis"
    junk.write(new_line)
    print("--> New Line Added...")

with open(file_path,"r") as junk:
    lowercase_junk = junk.read().lower()

with open(file_path,"w") as junk:
    junk.write(lowercase_junk)
    print("--> Changed to Lowercase...")