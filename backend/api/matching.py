def score_similarity(nlp, goal_a, goal_b):
    return nlp(goal_a).similarity(nlp(goal_b))
