import numpy as np

def optimize_study_schedule(topics: list, total_hours: float = 20.0) -> list:
    """
    Calculates dynamic time allocation per topic using constrained optimization.
    
    Formula: Need Index (N_i) = Weight_i * (1 - Confidence_i)
    Allocated Hours = (N_i / sum(N)) * Total Available Hours
    
    topics: List of dicts, e.g., [{"topic": "Optimization", "weight": 0.35, "confidence": 0.40}, ...]
    """
    if not topics:
        return []

    weights = np.array([t.get('weight', 0.25) for t in topics], dtype=float)
    confidences = np.array([t.get('confidence', 0.50) for t in topics], dtype=float)
    
    # Calculate Need Index
    need_scores = weights * (1.0 - confidences)
    
    if np.sum(need_scores) == 0:
        allocated_hours = np.full(len(topics), total_hours / len(topics))
    else:
        # Normalize to allocate total_hours
        allocated_hours = (need_scores / np.sum(need_scores)) * total_hours

    # Round nicely for presentation
    allocated_hours = np.round(allocated_hours, 1)

    result = []
    for idx, t in enumerate(topics):
        result.append({
            "topic": t["topic"],
            "weightage": f"{int(weights[idx] * 100)}%",
            "confidence": f"{int(confidences[idx] * 100)}%",
            "allocated_hours": float(allocated_hours[idx])
        })

    return result