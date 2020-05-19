from fuzzywuzzy import fuzz
from ploting_data import plots
def str_cmp(inpts):
    file=open('url_data.csv','r')
    file1=open('fuzywuzy_data.csv','w')
    file1.write('ratio,partial_ratio,token_sort_ratio,token_set_ratio,none \n')
    for i in file:
        file1.write(str(fuzz.ratio(inpts.lower(),i.lower())))
        file1.write(',')
        file1.write(str(fuzz.partial_ratio(inpts.lower(),i.lower())))
        file1.write(',')
        file1.write(str(fuzz.token_sort_ratio(inpts,i)))
        file1.write(',')
        file1.write(str(fuzz.token_set_ratio(inpts,i)))
        file1.write('\n')
    file1.close()
    file.close()

    plots()
    return 0