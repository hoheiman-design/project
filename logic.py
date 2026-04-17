
def rank_students(student_list):
    
    #heap_sort
    
    return sorted(student_list, key=lambda s: s.get_average(), reverse=True)