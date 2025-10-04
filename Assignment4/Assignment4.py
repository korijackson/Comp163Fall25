if __name__ == '__main__':
    #part 1
    student_name = "Kori Jackson"
    current_gpa = 3.5
    study_hours = 25
    social_points = 50
    stress_level = 75

    print("Welcome")
    print("Name: " + student_name)
    print("GPA: " + str(current_gpa))
    print("Study Hours: " + str(study_hours))
    print("Social Points: " + str(social_points))
    print("Stress Level: " + str(stress_level))
    print()

    #part2
    course_load_list = ["light", "standard", "heavy"]


    print("Choose your course load:")
    print("Light (12 credits)")
    print("Standard (15 credits)")
    print("Heavy (18 credits)")

    course_load = input("Your course load: ")

    if course_load.lower() == "light":
        study_hours = study_hours - 1
        social_points = social_points + 5
    elif course_load.lower() == "standard":
        study_hours = study_hours - 2
        social_points = social_points + 10
    elif course_load.lower == "heavy":
        study_hours = study_hours - 3
        social_points = social_points + 15
    else:
        print("Invalid input")

    print("Study Hours: " + str(study_hours ))
    print("Social Points: " + str(social_points))

    #part3
    study_option = ["programming", "math", "english", "history"]

    print()
    print("Choose your study option:")
    print("Programming")
    print("Math")
    print("English")
    print("History")
    class_chosen = input("Class to study ")

    if class_chosen.lower() in study_option and class_chosen.lower() == "programming":
        social_points -= 10
        current_gpa -= 0.3
    elif class_chosen.lower() in study_option and class_chosen.lower() == "math":
        social_points -= 5
        current_gpa -= 0.1
    elif class_chosen.lower() in study_option and class_chosen.lower() == "english":
        social_points += 5
        current_gpa += 0.3
    elif class_chosen.lower() in study_option and class_chosen.lower() == "history":
        social_points += 10
        current_gpa += 0.1
    elif class_chosen.lower() in study_option and class_chosen.lower() == "music" or class_chosen.lower() == "video":
        social_points += 15
        current_gpa += 0.4
    elif class_chosen.lower() not in study_option:
        current_gpa = 0.0
        social_points = 0.0
    else:
        print("Invalid input")

    print("Study Hours: " + str(study_hours ))
    print("Current GPA: " + str(current_gpa))
    print()

#part 4
if type(current_gpa) is float:
    if current_gpa >= 3.7:
        print("Congrats: You are on Dean's List")
    elif current_gpa >= 3.5:
        print("Congrats: You are on Chancellor's List")
    elif current_gpa < 2.0:
        print("Talk to you councillor: You are on probation")
    else:
        print("Congrats: Semester over")