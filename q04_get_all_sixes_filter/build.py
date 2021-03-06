# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype=np.str, skip_header=1, delimiter=',')


#Your Solution
def get_all_sixes_filter():
    return(ipl_matches_array[:,16].astype(np.int) == 6)
get_all_sixes_filter()


