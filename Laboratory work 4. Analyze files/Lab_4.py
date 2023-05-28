def MAINNN():
    print("Hi! Let's analuze your files!")
    print("Do you want to continue? (Use \"Yes\" to continue and \"No\" to close the application)")
    l = input()
    if l == "Yes":
        print("GOOOD! =)")
        ANALYZEYOURFILE()
    else:
        print("Bye!")
        exit()

def ANALYZEYOURFILE(): #C:\\Users\\user\\Desktop\\Lab_4_Python.txt
    print("Specify the location of your file:")
    Locate = input()
    with open(Locate, "r") as fILE:
        number_of_lines = fILE.readlines() 
        all_of_z = 0 
        all_of_null_line = 0 
        all_lines_of_and = 0 
        all_lines_of_z = 0
        for line in number_of_lines:
            all_of_z += line.count("z") 
            if line == "\n": 
                all_of_null_line += 1 
            if (line.find('and')) != -1: 
                all_lines_of_and += 1 
            if (line.find('z')) != -1:
                all_lines_of_z += 1
        print("File: ", Locate, "\nTotal lines: ", len(number_of_lines))
        print("Empty lines: ", all_of_null_line, "\nLines with \"z\": ", all_lines_of_z)
        print("\"z\" count: ", all_of_z, "\nLines with \"and\": ", all_lines_of_and)
    MAINNN()

MAINNN()