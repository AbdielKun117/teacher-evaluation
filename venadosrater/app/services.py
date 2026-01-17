from app.db import supabase

def get_all_professors():
    """
    Fetches all professors and calculates their ratings based on reviews.
    """
    # Safe check for missing credentials
    if not supabase:
        return []

    # Fetch professors
    response = supabase.table('professors').select('*').execute()
    professors_data = response.data
    
    # Fetch all reviews to crunch numbers Python-side (Optimization: Create a SQL View later)
    reviews_response = supabase.table('reviews').select('professor_id, quality, difficulty').execute()
    reviews_data = reviews_response.data
    
    # Process reviews
    stats = {}
    for r in reviews_data:
        pid = r['professor_id']
        if pid not in stats:
            stats[pid] = {'quality_sum': 0, 'difficulty_sum': 0, 'count': 0}
        stats[pid]['quality_sum'] += r['quality']
        stats[pid]['difficulty_sum'] += r['difficulty']
        stats[pid]['count'] += 1
        
    # Merge data
    results = []
    for p in professors_data:
        pid = p['id']
        p_stats = stats.get(pid, {'quality_sum': 0, 'difficulty_sum': 0, 'count': 0})
        count = p_stats['count']
        
        rating = round(p_stats['quality_sum'] / count, 1) if count > 0 else 0
        difficulty = round(p_stats['difficulty_sum'] / count, 1) if count > 0 else 0
        
        p['rating'] = rating
        p['difficulty'] = difficulty
        p['reviews'] = count
        results.append(p)
        
    return results

def get_professor_by_id(id):
    """
    Fetches a single professor and their reviews.
    """
    # Safe check for missing credentials
    if not supabase:
        return None

    # Fetch professor details
    p_response = supabase.table('professors').select('*').eq('id', id).execute()
    if not p_response.data:
        return None
    
    professor = p_response.data[0]
    
    # Fetch reviews
    r_response = supabase.table('reviews').select('*').eq('professor_id', id).order('created_at', desc=True).execute()
    reviews = r_response.data
    
    # Calculate stats
    total_quality = sum(r['quality'] for r in reviews)
    total_difficulty = sum(r['difficulty'] for r in reviews)
    count = len(reviews)
    
    professor['rating'] = round(total_quality / count, 1) if count > 0 else 0
    professor['difficulty'] = total_difficulty / count if count > 0 else 0 # keeping it float or int based on template
    professor['difficulty'] = round(professor['difficulty'], 1)
    professor['reviews'] = count
    professor['reviews_list'] = reviews # Match the template expectation
    
    return professor
