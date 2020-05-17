# CPP Output Comparer

This little script can compile a cpp file, execute it for each input and compare the result with the expected output
![Image](https://i.ibb.co/mRttf4X/cppcomparer.gif)

## Setup

First, you have to set the inputs and outputs. Each input/output must be separated with 'TEST'

Example:

`input.txt`
```
4 5 6
TEST
1 2 3
TEST
7 6 4
```


`output.txt`
```
15
TEST
6
TEST
17
```

Then, set `test.py` as executable
```
$ chmod +x test.py
```

## Running 

Just execute adding the file name argument.

Example:
```
$ ./test.py f.cpp
```

Ouput Example:
```
COMPILING F.CPP...

EXECUTING IT FOR EACH INPUT

CASE 1 :
ACCEPTED

FINAL RESULT: 1/1
```