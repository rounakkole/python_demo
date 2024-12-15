
from random import randint
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

TRAIN_INPUT = list()
tRAIN_output = list()
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    op = a + (2.12*b) + (3.453254*c)
    TRAIN_INPUT.append([a, b, c])
    tRAIN_output.append(op)
print(TRAIN_INPUT)
print(tRAIN_output)