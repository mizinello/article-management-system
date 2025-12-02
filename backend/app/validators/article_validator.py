def validate_article(data):
    errors = []
    
    # Title validation
    if not data.get('title'):
        errors.append("Title is required")
    elif len(data['title']) < 20:
        errors.append("Title must be at least 20 characters")
    
    # Content validation
    if not data.get('content'):
        errors.append("Content is required")
    elif len(data['content']) < 200:
        errors.append("Content must be at least 200 characters")
    
    # Category validation
    if not data.get('category'):
        errors.append("Category is required")
    elif len(data['category']) < 3:
        errors.append("Category must be at least 3 characters")
    
    # Status validation
    if not data.get('status'):
        errors.append("Status is required")
    elif data['status'] not in ['publish', 'draft', 'thrash']:
        errors.append("Status must be one of: publish, draft, thrash")
    
    return errors