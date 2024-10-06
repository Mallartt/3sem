from cm_timer import cm_timer_1
from print_result import print_result
from random import randint
import json
import sys
import os
# Сделаем другие необходимые импорты

path = "C:/Artem/Labs/3semPython/3-4 лаба/pythonProject/data.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path,encoding='utf-8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return sorted(set(item["job-name"].lower() for item in arg))


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith("программист"),arg))


@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))


@print_result
def f4(arg):
    job_names = arg
    salaries = [f"зарплата {randint(100000, 200000)} руб." for _ in job_names]
    return [f"{job}, {salary}" for job, salary in zip(job_names, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))