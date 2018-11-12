def students_ranker(s):
    return sorted(s, key=lambda e: (e['subject']['math'], e['subject']['physic'], e['subject']['history']), reverse=False)
