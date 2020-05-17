#!/usr/bin/env python3
import sys
import difflib
import os
from os import path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) < 2:
    print("Please select the file...")
elif path.isfile("input.txt") == False or path.isfile("output.txt") == False:
    print("Missing input.txt and output.txt")
elif len(open("input.txt","r").read().split("TEST\n")) != len(open("output.txt","r").read().split("TEST\n")):
    print("The number of inputs and outputs doesn't match")
else:
    file = str(sys.argv[1])
    cases = open("input.txt","r").read().split("TEST\n")
    expected = open("output.txt","r").read().split("TEST\n")

    print("COMPILING "+file.upper()+"...\n")
    os.system("g++ "+file+" -std=c++17 -static -O2 -lm")

    print("EXECUTING IT FOR EACH INPUT\n")

    correct_answers = 0

    for i in range(len(cases)):
        case_file = open("tmp/test.txt","w")
        case_file.write(cases[i])
        case_file.close()

        os.system("./a.out < tmp/test.txt  > tmp/result.txt")

        result_file = open("tmp/result.txt","r")
        result = result_file.read()
        result_file.close()

        if result == expected[i]:
            print("CASE",i+1,":",bcolors.OKGREEN+"ACCEPTED"+bcolors.ENDC)
            correct_answers += 1
        else:
            print("CASE",i+1,":",bcolors.FAIL+"WRONG ANSWER"+bcolors.ENDC)
            print(" expecting:")
            print("  "+bcolors.WARNING+expected[i].replace("\n"," ")+bcolors.ENDC)
            print(" result:")
            print("  "+bcolors.FAIL+result.replace("\n"," ")+bcolors.ENDC)
            
        
    
    if correct_answers == 0:
        print(bcolors.FAIL+"\nFINAL RESULT: "+str(correct_answers)+"/"+str(len(cases))+bcolors.ENDC)
    elif correct_answers == len(cases):
        print(bcolors.OKGREEN+"\nFINAL RESULT: "+str(correct_answers)+"/"+str(len(cases))+bcolors.ENDC)
    else:
        print(bcolors.WARNING+"\nFINAL RESULT: "+str(correct_answers)+"/"+str(len(cases))+bcolors.ENDC)

    