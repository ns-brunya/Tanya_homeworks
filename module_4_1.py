from true_math import divide as module_true
from fake_math import divide as module_fake

result1 = module_fake(69, 3)
result2 = module_fake(3, 0)
result3 = module_true(49, 7)
result4 = module_true(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)