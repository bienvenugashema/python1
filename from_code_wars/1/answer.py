def open_or_senior(data):
    output = []
    for dt in data:
        if dt[0] >= 55 and dt[1] > 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output
    
print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))