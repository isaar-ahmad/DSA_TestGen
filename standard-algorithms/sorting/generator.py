# Generate a folder consisting of reference input-output pairs
import pandas as pd
import sorting_algorithm as sa
import os
import random
TESTCASE_DIR = "./testcases"

RANDOM_SEED = 10

############### Testcase generation parameters ###############
NUM_TESTCASES = 7

MIN_LIST_SIZE = 3
MAX_LIST_SIZE = 10

MIN_INTEGER = 5
MAX_INTEGER = 30

##################################################################
###### DO NOT EDIT BELOW THIS LINE                           #####
##################################################################
# for each reference input-output pair :
    # Read input
    # Run code-under-test on input, generate output in standard format
    # Compare code-under-test output to reference output

def convert_int_list_to_string(integer_list):
    s = ""

    for i in range(len(integer_list)-1) :
        s = s + str(integer_list[i]) + " "

    s = s + str(integer_list[len(integer_list) - 1 ] ) + "\n"

    print ("List_size = " + str(integer_list)) 
    print ("Elements = " + str (s))
    return s

def generate_input():
    random_list = []
    list_size = random.randint(MIN_LIST_SIZE,MAX_LIST_SIZE)

    for i in range(list_size):
        random_list.append(random.randint(MIN_INTEGER,MAX_INTEGER))
    
    return random_list

def generate_output(sample_ip):
    sample_op =  sa.sorting(sample_ip)
    return sample_op

##################################################
random.seed(RANDOM_SEED)

if not os.path.exists(TESTCASE_DIR):
    os.mkdir(TESTCASE_DIR)

for i in range (1,NUM_TESTCASES+1):
    filename = TESTCASE_DIR + "/" + str(i) + ".txt"
    f = open(filename, "w")
    ###############################
    sample_input_list = generate_input()
    sample_output_list = generate_output(sample_input_list)
    print("----------- Testcase " + str (i) + "-------------")
    sample_input_str = convert_int_list_to_string(sample_input_list)
    sample_output_str = convert_int_list_to_string(sample_output_list)

    file_str = ""
    file_str = file_str + "Input:\n"
    file_str = file_str + sample_input_str
    file_str = file_str + "Output:\n"
    file_str = file_str + sample_output_str

    ###############################
    f.write(file_str)
    f.close()

