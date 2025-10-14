def reverse_sort_dictionary(data):
    
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary")
    
    result = []
    
    
    for name, value in data.items():
       
        if not isinstance(name, str):
            raise TypeError("Dictionary keys must be strings (names)")
        
        
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("Dictionary values must be tuples with 2 elements")
        
        
        phone, age = value
        
        
        result.append((name, phone))
    
    
    result.sort(key=lambda x: x[0], reverse=True)
    
    return result
