import os


def main():
    i = 0
    path = input("Enter the path of directory: ")
    name = input("Enter the base name of file: ")
    ext = input("Enter the extension of file: ")
    for filename in os.listdir(path):
        my_dest = name + str(i) + ext
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1


if __name__ == "__main__":
    main()
