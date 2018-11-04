import os


def walk_dir(sPath):
    for root, dirs, files in os.walk(sPath):
        # for dir in dirs:
        #     print(os.path.join(root, dir))
        for file in files:
            print(os.path.join(root, file))


def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


p = "C:\\Program Files\\AMD"
walk_dir(p)
print("-"*10)
print_directory_contents(p)
