from collections import Counter


def _user_count_key(user_count):
    """
    Generate sorting key for user event counts.
    
    Sorting order:
    1. Count: descending (more events first)
    2. User name: ascending (alphabetically)
    
    Args:
        user_count: Tuple (username, count)
        
    Returns:
        Tuple of sort keys: (-count, username)
    """
    username, count = user_count
    return (-count, username)


def _get_top_action(action_counter):
    """
    Extract the most common action from counter.
    
    Args:
        action_counter: Counter object of actions
        
    Returns:
        Tuple (action_name, count) or (None, 0) if empty
    """
    if not action_counter:
        return (None, 0)
    
    # Find action with highest count
    max_action = max(action_counter.items(), key=lambda x: x[1])
    return max_action


def summarize_logs(logs):
    """
    Summarize event logs to count user activities and identify top action.
    
    Args:
        logs: List of tuples [(user, action), ...] representing events
        
    Returns:
        Tuple (user_counts, top_action) where:
        - user_counts: List of (user, count) tuples sorted by:
          1. count (descending)
          2. user name (ascending)
        - top_action: Tuple (action, count) with highest occurrence count
          or (None, 0) for empty logs
          
    Example:
        >>> logs = [('alice', 'login'), ('bob', 'login'), ('alice', 'view')]
        >>> user_counts, top_action = summarize_logs(logs)
        >>> user_counts
        [('alice', 2), ('bob', 1)]
        >>> top_action
        ('login', 2)
    """
    # Handle empty input
    if not logs:
        return ([], (None, 0))
    
    # Count occurrences of each user and action
    user_counter = Counter()
    action_counter = Counter()
    
    for user, action in logs:
        user_counter[user] += 1
        action_counter[action] += 1
    
    # Sort user counts by count (desc) then name (asc)
    user_counts = sorted(user_counter.items(), key=_user_count_key)
    
    # Find top action
    top_action = _get_top_action(action_counter)
    
    return (user_counts, top_action)
