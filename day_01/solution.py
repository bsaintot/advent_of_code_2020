import os
from typing import List


def parse_expenses(filename: str) -> List[int]:
    expenses = []
    with open(filename) as f:
        for line in f:
            expenses.append(int(line))
    return expenses


def first_star(expenses: List[int]) -> int:
    for i in range(len(expenses)):
        for j in range(i + 1, len(expenses)):
            if expenses[i] + expenses[j] == 2020:
                return expenses[i] * expenses[j]


def second_star(expenses: List[int]) -> int:
    for i in range(len(expenses)):
        for j in range(i + 1, len(expenses)):
            for k in range(j + 1, len(expenses)):
                if expenses[i] + expenses[j] + expenses[k] == 2020:
                    return expenses[i] * expenses[j] * expenses[k]


if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    expenses_list = parse_expenses(input_file_path)
    print(first_star(expenses_list))  # 988771
    print(second_star(expenses_list))  # 171933104
