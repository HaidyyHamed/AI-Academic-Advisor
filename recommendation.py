def recommend_courses(student, all_courses, courses, max_courses=5):
    completed = set(student['completed_courses'])
    interest = student['interest']
    eligible = []

    for course in all_courses:
        if course in completed:
            continue
        if all(prereq in completed for prereq in courses[course]):
            if interest in course or "AI" in course or "Data" in course or "Security" in course:
                eligible.append(course)

    # Prioritize by interest
    interest_courses = [c for c in eligible if interest.lower() in c.lower()]
    others = [c for c in eligible if c not in interest_courses]
    recommended = interest_courses + others
    return recommended[:max_courses]
