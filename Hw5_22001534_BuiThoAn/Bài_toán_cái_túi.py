# Có n loại đồ vật, mỗi loại có số lượng không hạn chế.
# Đồ vật loại i có trọng lượng là wi và có giá trị là vi , i ∈ {1, 2, ..., n}.
# Tìm cách chọn đồ vật để đặt vào cái túi có giới hạn trọng lượng là M sao cho tổng giá trị của các đồ vật được chọn là lớn nhất.

def knapsack(n, m, w, v):
    """
    :param n: số lượng đồ vật
    :param m: khối lượng tối đa của cái túi
    :param w: mảng khối lượng của đồ vật
    :param v: mảng giá trị của đồ vật
    :return:  giá trị lớn nhất có thể đạt được
    """

    for i in range(1, n + 1):
        for j in range((m - )