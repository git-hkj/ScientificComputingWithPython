#Creating a python file with the name entered by the user

from pathlib import Path

print("\n")

name = input("Enter your name: ")

Path(name +".py").write_text(f"Your name = {name!r}\n", encoding="utf-8")
