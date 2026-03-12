def get_ranking(students, k):
    # 分數降序, 年齡升序, 名字升序
    sorted_list = sorted(students, key=lambda x: (-x[1], x[2], x[0]))
    return sorted_list[:k]