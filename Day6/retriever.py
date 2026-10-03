import numpy as np


#get Similarity Score
def cosine_similarity(vector1, vector2):
    v1=np.array(vector1)
    v2=np.array(vector2)
    return np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(2))

#get best match
def get_best_matches(user_embedding,kb_embeddings,top_results):

    best_matches={}
    for kb_key in kb_embeddings.keys():
        similarity_score=cosine_similarity(kb_embeddings[kb_key],user_embedding)
        if(len(best_matches)==top_results):
            for best_match_key,value in best_matches.items():
                if value < similarity_score :
                    removed_score = best_matches.pop(best_match_key)
                    best_matches[kb_key]=similarity_score
                    break;
        else:
            best_matches[kb_key]=similarity_score

    return best_matches
