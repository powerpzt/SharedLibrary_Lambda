#from ctypes.util import find_library
import ctypes
import json
import os
def lambda_handler(event, context):
    print("Hello~")
    #lib=find_library('test')     # work in python3.7, not work in python3.8
    path = f'/opt/lib/libtest.so'
    lib = ctypes.cdll.LoadLibrary(path)
    inference = lib.add
    inference.argtypes=(ctypes.c_int, ctypes.c_int)
    inference.restype = ctypes.c_int
    print(inference(3,10))
    
    inference = lib.addin
    inference.argtypes=(ctypes.c_int, ctypes.c_int)
    inference.restype = ctypes.c_int
    print(inference(3,10))
    # result is 0,   printf is not shown.
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

