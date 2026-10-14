import os


class FileInfo:
    def __init__(self, name):
        self.name = name

    def show(self):
        if os.path.exists(self.name):
            if os.path.isfile(self.name):
                size = os.path.getsize(self.name)
                print(self.name, "- file -", size, "bytes")
            elif os.path.isdir(self.name):
                print(self.name, "- directory")


current_folder = os.getcwd()
print("Current working directory:")
print(current_folder)

names = os.listdir()
files_and_folders = []
i = 0

while i < len(names):
    item = FileInfo(names[i])
    files_and_folders.append(item)
    i = i + 1

print("\nFiles and directories:")

i = 0

with open("output.txt", "w") as report:
    report.write("Current working directory:\n")
    report.write(current_folder + "\n\n")
    report.write("Files and directories:\n")

    while i < len(files_and_folders):
        item = files_and_folders[i]
        item.show()

        if os.path.isfile(item.name):
            size = os.path.getsize(item.name)
            report.write(
                item.name + " - file - " + str(size) + " bytes\n"
            )
        elif os.path.isdir(item.name):
            report.write(item.name + " - directory\n")

        i = i + 1

print("\nReport saved to output.txt")