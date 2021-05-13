def get_result(final_scores):
    if final_scores["home_score"] > final_scores["away_score"]:
        return "Home win"
    elif final_scores["away_score"] > final_scores["home_score"]:
        return "Away win"
    else:
        return "Draw"

def get_results(final_scores):
    scores_list = []
    for score in final_scores:
        scores_list.append(get_result(score))
    return scores_list

    


    
    # (You could try and use a list comprehension for this)



    