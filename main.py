from curriculum_graph import build_curriculum_graph
from student_simulation import generate_students
from recommendation import recommend_courses
import json

G, courses = build_curriculum_graph()
students = generate_students(G, courses, 100)
all_courses = list(G.nodes())

# Example output
example = {
    'student': students[0],
    'recommended': recommend_courses(students[0], all_courses, courses)
}
print(json.dumps(example, indent=2))

# Save output
with open("example_output.json", "w") as f:
    json.dump(example, f, indent=2)
