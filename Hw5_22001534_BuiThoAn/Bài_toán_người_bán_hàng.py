# Một người bán hàng muốn giao hàng đến n thành phố T1, T2, T3, ..., Tn.
# Người bán hàng xuất phát từ một thành phố bất kỳ nào đó và muốn đi qua tất cả các thành phố còn lại.
# Mỗi thành phố đi qua đúng 1 lần rồi quay trở lại thành phố xuất phát ban đầu.
# Gọi cij là chi phí đi từ thành phố Ti đến thành phố Tj.
# Hãy tìm một lộ trình thỏa mãn yêu cầu của bài toán sao cho tổng chi phí là nhỏ nhất.

# sử dụng thuật toán nhánh cận (bround and bound)
def tsp(cost_matrix):
    """
    :param cost_matrix: ma trận chi phí
    :param n: số lượng thành phố = số lượng hàng trong ma trận chi phí
    :return : min_cost: chi phí tối thiểu
    :return : best_path: lộ trình tốt nhất
    """
    n = len(cost_matrix)
    min_cost = float('inf')
    best_path = []

    def bound(path, cost):
        """
        :param path: lộ trình hiện tại
        :param cost: chi phí hiện tại
        :return: chi phí tối thiểu có thể đạt được từ lộ trình hiện tại
        """
        if len(path) == n:
            return cost + cost_matrix[path[-1]][path[0]]
        else:
            return cost + (n - len(path)) * min(cost_matrix[path[-1]])

    def branch(path, cost):
        """
        :param path: lộ trình hiện tại
        :param cost: chi phí hiện tại
        """
        nonlocal min_cost, best_path
        if len(path) == n:
            if cost + cost_matrix[path[-1]][path[0]] < min_cost:
                min_cost = cost + cost_matrix[path[-1]][path[0]]
                best_path = path + [path[0]]
            return

        for i in range(n):
            if i not in path:
                new_cost = cost + cost_matrix[path[-1]][i]
                if bound(path + [i], new_cost) < min_cost:
                    branch(path + [i], new_cost)

    for city in range(n):
        branch([city], 0)

    return min_cost, best_path


# Ví dụ sử dụng
import numpy as np
if __name__ == "__main__":
    cost_matrix = [
        [0, 10, 15, 15],
        [5, 15, 35, 25],
        [15, 35,25, 30],
        [20, 15, 35, 5]
    ]
    print(np.array(cost_matrix))
    min_cost, best_path = tsp(cost_matrix)
    print("Chi phí tối thiểu:", min_cost)
    print("Lộ trình tốt nhất:", best_path)

