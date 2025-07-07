import random
import numpy as np

def generate_students(curriculum, courses, n=100):
    interests_pool = ['AI', 'Security', 'Data Science']
    all_courses = list(curriculum.nodes())
    students = []

    for i in range(n):
        completed = set()
        for course in all_courses:
            if all(p in completed for p in courses[course]):
                if random.random() < 0.3:
                    completed.add(course)
        gpa = round(random.uniform(2.0, 4.0), 2)
        interest = random.choice(interests_pool)
        grades = {c: round(random.uniform(1.0, 4.0), 2) for c in completed}
        students.append({
            'id': i,
            'completed_courses': list(completed),
            'grades': grades,
            'gpa': gpa,
            'interest': interest
        })
    return students
