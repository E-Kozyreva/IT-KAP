worker1, worker2, worker3 = map(int, input().split())
salary = [worker1, worker2, worker3]
print(max(salary) - min(salary))
