import platform

print(sum(filter(lambda x: x%3 == 0 or x%5 == 0, range(1,1000))))