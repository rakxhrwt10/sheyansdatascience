def set_operations(n1, set1, n2, set2):
    
    s1 = set(set1)
    s2 = set(set2)
    
    union = sorted(s1 | s2)
    intersection = sorted(s1 & s2)
    difference1 = sorted(s1 - s2)
    difference2 = sorted(s2 - s1)
    print(f"Union: {union}\nIntersection: {intersection}\nDifference: {difference1}")
    