# ==============================
# SIMPLE STUDENT GRADE CHECKER
# ==============================

# Gumagawa tayo ng class na Student
class Student:
    # Ito ang constructor
    # Automatic itong tumatakbo kapag gumawa tayo ng object
    def __init__(self, name, grade):
        # Ang "self" ay tumutukoy sa kasalukuyang object
        # Dito natin sine-save ang name at grade sa object
        self.name = name
        self.grade = grade

    # Method para ipakita ang impormasyon ng student
    def display_info(self):

        # Nagpi-print ng separator
        print("\n--- STUDENT INFORMATION ---")

        # Ipinapakita ang name na naka-save sa object
        print("Name:", self.name)

        # Ipinapakita ang grade na naka-save sa object
        print("Grade:", self.grade)

        # Condition para malaman kung pasado o hindi
        # Kung ang grade ay 75 pataas, pasado
        if self.grade >= 75:
            print("Status: PASSED")
        else:
            print("Status: FAILED")


# ==============================
# MAIN PROGRAM (Dito nagsisimula)
# ==============================

# Humihingi tayo ng pangalan mula sa user
# input() ay laging string ang binabalik
name = input("Enter student name: ")

# Humihingi tayo ng grade mula sa user
# Kailangan natin gawing integer gamit ang int()
# dahil string ang default ng input()
grade = int(input("Enter student grade: "))

# Gumagawa tayo ng object na student1
# Dito tatawagin ang constructor (__init__)
student1 = Student(name, grade)

# Tinatawag natin ang method na display_info()
# para ipakita ang lahat ng impormasyon
student1.display_info()