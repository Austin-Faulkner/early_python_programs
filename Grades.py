#  File: Grades.py
#  Description: This program creates a grade roster complete with
#               homework averages, weighted at 55%, and exam averages,
#               weighted at 45%. For each person in the class,
#               a final, overall grade is computed and displayed on the same
#               line with the other two scores and the last and first name
#               of the student.
#  Student's Name: Austin Keith Faulkner
#  Student's UT EID: akf354
#  Course Name: CS 303E 
#  Unique Number: 50075
#
#  Date Created: November 15, 2019
#  Date Last Modified: November 22, 2019 (5:23pm)


def main():

    NUMBER_OF_HOMEWORKS = 15
    NUMBER_OF_EXAMS = 3

    infile = open("gradeInput.txt", "r")
    
    outfile = open("gradeOutput.txt", "w+")
    outfile.write(format("HW", ">35s") + format("Exam", ">9s") + format("Final", ">8s") + "\n") 
    outfile.write(format("Last Name", "15s") + format("First Name", ">6s") + format("Avg", ">11s") \
                                             + format("Avg", ">7s") + format("Grade", ">9s") + "\n")
    outfile.write("----------------------------------------------------\n")

    studentData = infile.readline()

    while studentData != "":
        student_list = studentData.split(" ")
        names = student_list[0].split(",")
        outfile.write(format(str(names[0]), "15s") + format(str(names[1]), "<15s"))
        studentData = infile.readline()

        homeworkSum = 0
        for i in range(1, len(student_list) - 3):
            homeworkSum += int(student_list[i])    
        homeworkAverage = homeworkSum /  NUMBER_OF_HOMEWORKS
        outfile.write(format(str(round(homeworkAverage, 1)), ">7s"))

        examSum = 0
        for j in range(16, 19):
            examSum += int(student_list[j])
        examAverage = examSum / NUMBER_OF_EXAMS
        finalGrade = 0.55 * homeworkAverage + 0.45 * examAverage
        outfile.write(format(str(round(examAverage, 1)), ">7s") + format(str(round(finalGrade, 1)), ">7s") + "\n")

    outfile.write("\n")
        
    infile.close()
    outfile.close()        
    
main()

