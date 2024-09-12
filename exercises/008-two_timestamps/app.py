def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    # Your code here   
    first_h = hr1 * 3600
    first_min = min1 * 60
    result = first_h + first_min + sec1
    second_h = hr2 * 3600
    second_min = min2 * 60
    result_2 = second_h + second_min + sec2

    return result_2 - result


# Invoke the function and pass two timestamps(6 intergers) as its arguments
print(two_timestamp(1,1,1,2,2,2))
