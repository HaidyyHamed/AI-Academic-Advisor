import networkx as nx

def build_curriculum_graph():
    courses = {
        'Intro CS': [],
        'Math I': [],
        'Math II': ['Math I'],
        'Data Structures': ['Intro CS'],
        'Algorithms': ['Data Structures', 'Math II'],
        'AI': ['Algorithms'],
        'Security': ['Algorithms'],
        'Data Science': ['Algorithms'],
        'NLP': ['AI'],
        'ML': ['AI'],
        'Blockchain': ['Security'],
        'Deep Learning': ['ML'],
        'Ethics': []
    }

    G = nx.DiGraph()
    for course, prereqs in courses.items():
        G.add_node(course)
        for prereq in prereqs:
            G.add_edge(prereq, course)
    return G, courses
