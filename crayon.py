"""
Crayon: patching files
"""
import sys

class Crayon():
    def __init__(self, filename):
        self.filename = filename

    def patch(self, offset, content):
        with open(self.filename, "rb") as file_to_patch:
            file_content = file_to_patch.read()
        new_content = file_content[:offset] + bytes([content]) + file_content[offset + 1:]
        print(len(new_content))
        with open("patched_" + self.filename, "wb") as patched_file:
            patched_file.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: crayon.py <filename> <offset> <patch_content>")
        sys.exit(-1)

    crayon = Crayon(sys.argv[1])
    crayon.patch(int(sys.argv[2], 16), int(sys.argv[3], 16))

