#this file is to show how to use the integrated files

from interlink import final_output

inpt=input("Enter your Text here: ")
try:
    result,confidance=final_output(inpt)
    print(result,confidance)
except Exception as ec:
    print("\n Unable to find result, please try again later :) ")