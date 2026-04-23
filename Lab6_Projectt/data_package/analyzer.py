def calculate_mean(num_list):
    if len(num_list) == 0:
        return 0
    return sum(num_list) / len(num_list)

def find_maximum(num_list):
    return max(num_list) if num_list else None

def find_minimum(num_list):
    return min(num_list) if num_list else None