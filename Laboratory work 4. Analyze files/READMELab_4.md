Laboratory work #4: Analysis of files.
The task of this laboratory work: to write a program that provides statistics for a given file:
1. Number of lines;
2. Number of empty lines;
3. The number of lines with the letter "z";
4. The number of letters "z" in the file;
5. The number of lines with the group of symbols “and” (for example, "andromeda" contains "and" so
same as "you and me").
Also mandatory requirements for the program were:
1. Request to obtain the path to the file;
2. Request to continue work on other files;
3. Request to continue operation of the program itself with the possibility of turning it off.
The program also outputs the contents of the file itself for clarity.


The program code looks like this:

>>>

def MAINNN(): #Let's create a control function that will work depending on the entered parameter
     print("Do you want to continue? (Use \"Yes\" to continue and \"No\" to close the application)")
     l = input()
     if l == "Yes": #If the user wants to explore the file
         print("GOOOD! =)")
         ANALYZEYOURFILE() #Call the main function to examine the file
     else: #Actions for a negative response
         print("Bye!")
         exit() #Exit the program

def ANALYZEYOURFILE(): #Exploratory function
     print("Enter the path to the file you want to examine based on the sample (Disk:\\...\\...\\file_name.txt): ")
     Locate = input() #Create a variable that will store the path to the file
     with open(Locate, "r") as file: #This line of code allows you to correctly open the file for reading, as well as
     #properly close even if an error occurs
         number_of_lines = fILE.readlines() #Creating an object that will store the contents of a text file as a list of lines
         all_of_z = 0 #Variable to store the number of letters "z"
         all_of_null_line = 0 #Variable to store the number of empty lines
         all_lines_of_and = 0 #Variable to store the number of lines with the character group "and"
         all_lines_of_z = 0 #Variable to store the number of lines with the letters "z"
         for line in number_of_lines: #Creating a loop that will examine each element (line) of the list of lines of the file
             all_of_z += line.count("z") #Sum of all existing "z" letters in a line
             if line == "\n": #If the line is empty
                 all_of_null_line += 1
             if (line.find('and')) != -1: #If a group of characters "and" was found in the line
                 all_lines_of_and += 1
             if (line.find('z')) != -1: #If the line contains the letter "z"
                 all_lines_of_z += 1
         print("File: ", Locate, "\nTotal lines: ", len(number_of_lines))
         print("Empty lines: ", all_of_null_line, "\nLines with \"z\": ", all_lines_of_z) #Output of results
         print("\"z\" count: ", all_of_z, "\nLines with \"and\": ", all_lines_of_and)
     MAINNN() #Return to control function

print("Hi! Let's analyze your files!")
MAINNN() #Beginning

>>>

Examples of code work: