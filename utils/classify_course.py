def classify_course(courses):
    course_category = []

    for course in courses:
        if course["department"] == "general":
            course_category.append("GENERAL")
        elif len(course["department"]) > 1:
            course_category.append("SHARED")
        else:
            course_category.append("ISOLATED")

    return course_category