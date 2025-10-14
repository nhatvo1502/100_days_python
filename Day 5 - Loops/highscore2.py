student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

def _max(scores):
    max_score = scores[0]
    for score in scores:
        if max_score < score:
            max_score = score
    
    return max_score

def _min(scores):
    min_score = scores[0]
    for score in scores:
        if min_score > score:
            min_score = score
    
    return min_score

print(_max(student_scores))
print(_min(student_scores))