#import pickle
dataset = ['hello', 'test']
outputFile = 'test.data'
fw = open(outputFile, 'wb' )
pickle.dump(dataset, fw)
fw.close()

inputFile = 'test.data'
fd = open(inputFile, 'rb' )
dataset = pickle.load(fd)
#print dataset


TRAIN_INPUT = list()
TRAIN_OUTPUT = list()
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    op = a + (2*b) + (3*c)
    TRAIN_INPUT.append([a, b, c])
    TRAIN_OUTPUT.append(op)
    