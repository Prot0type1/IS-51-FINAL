"""
start

this program will output the grades of students on the final by: 
    -number of grades
    -average of grades
    -percentage of grades above the average percentage

the average grade is 83.25.
the total number of grades is 24.
the percentage of grades above average is 54.17
the list will be introduced from the dictionary by using the open method
the grades will then be listed as integers.
after, the calculations can begin.
the end result will display the 3 solutions.

finalize

"""

"""

main()

    initiates the program
    infile = open
    output total number of grades
    print("")
    display average 
    print("")

calculate_percentage_above_average()
    caluate the percentage
    print("")

"""

def main():
    file = "Final.txt"
    calculate_percentage_above_average(file)
"File is being called"

def calculate_percentage_above_average(file):
    infile = open(file, 'r')
    listGrades = [int(line.rstrip()) for line in infile]
    infile.close()
    lenght = len(listGrades)
    sum1 = sum(listGrades)
    avg = sum1 / lenght
    print("number of grades:", lenght)
    print("average grade:", avg)
    counter = 0
    for item in listGrades:
        if item > avg:
            counter += 1
    percentHigher = counter / lenght
    print("Total Percentage of Grades above Average:", end =" ")
    print("{0:.2%}".format(percentHigher))


main()