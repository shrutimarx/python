def count_it(num):
    count = 0
    new_num = str(num)
    for ch in new_num:
        if int(ch) % 2 == 0:
            count += 1
    return count
    
