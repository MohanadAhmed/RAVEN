import sys
import random
import json
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

xsd = 1234
if sys.version_info[0] == 2:
    random.seed(xsd)
elif sys.version_info[0] == 3:
    random.seed(xsd, version=1)
else:
    print("What are you doing??!!!")
    exit()

# with open("./src/randStreamMatch/state2.7.json") as f:
#     data = tuple(json.load(f))

# st = (data[0], tuple(data[1]), data[2])
# random.setstate(st)

for i in range(10):
    print(random.random())

z1 = list(range(10))
if sys.version_info[0] == 2:
    random.shuffle(z1)
elif sys.version_info[0] == 3:
    random.shuffle(z1, random.random)
else:
    print("What are you doing??!!!")
    exit()
print(z1)