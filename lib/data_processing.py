def format_student_data(student):
    """
    Format student data for display.
    """
    return str(student)


def display_students(student_list):
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    for student in student_list:
        print(format_student_data(student))