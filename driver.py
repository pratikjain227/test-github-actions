
import os

print("Running Driver File")

os.remove("config.json")
print("File removed")

with open('config.json', 'w') as f:
    f.write('{}')
print("File created")

