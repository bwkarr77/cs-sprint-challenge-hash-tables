def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for each in a:
        # checks each value in cache...
        if (each * -1) in cache:
            # ..if the opposite sign of each value exists in cache
            # --> if each = 2, and each = -2, then the if statement is TRUE
            result.append(abs(each))
        else:
            # ..if the opposite sign doesn't exist, then create it in cache
            cache[each] = each
    return result


if __name__ == "__main__":
    print(has_negatives([-5, -1, -2, -5, 5, 1, 2, 3, 4, -4]))
