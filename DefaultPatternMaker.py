import os
import subprocess
params = ['1 128 5', '3 128 5', '4 128 5','5 128 5','6 128 5','7 128 5','8 128 5','9 128 5']

for param in params:
    process0 = subprocess.Popen("python PatternMaker.py {}".format(param))
