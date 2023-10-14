class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Use the sorted function with a custom sorting key
  sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
  return sorted_students


# Test the function with different input lists of students
if __name__ == "__main__":
  # Create a list of student objects
  students = [
      Student("Ragu", "S001", 3.7),
      Student("vijay", "S002", 3.5),
      Student("Monaj", "S003", 3.9),
      Student("Rajesh", "S004", 3.2),
  ]

  # Sort the students by CGPA in descending order
  sorted_students = sort_students(students)

  # Print the sorted list of students
  for student in sorted_students:
    print(
        f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}"
    )
