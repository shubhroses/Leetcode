def print_orders(tasks, prerequisites):
    """
    Prerequisites: [0, 1], [1, 2]
    """
def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])
    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
main()