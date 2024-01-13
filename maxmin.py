
test_data = [20, 50, 12, 6, 14, 8]

def my_max(num_list):
    max_num = float("-inf")
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

def my_min(num_list):
    min_num = float("inf")
    for num in num_list:
        if num < min_num:
            min_num = num
    return min_num

def get_minmax(num_list):
    return [my_min(num_list), my_max(num_list)]


def main(test_data):
    print("{} returns: {}".format(test_data, get_minmax(test_data)))
    

if __name__ == "__main__":
    main(test_data)