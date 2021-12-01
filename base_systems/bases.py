'''
10/30/21
850p

likely not finished by test time but will work on it nonetheless
general purpose package that aims to provide various tools to solve base notation problems

numbers will be stored as the following: num = [[2],1,0,1,0,0]

we start with a sublist that contains what base it is in, followed by the number itself
'''

######### Dependencies

'''none'''

######### vars



######## Functions


def nbase_to_dec(num, strt_b = None): # expects num as a list specified in flowerbox. starting base is none to begin with
    strt_b, num = num[0][0], num[1:] # separates them
    
    num = num.reverse()
    final_sln = 0
    for coef in range(len(num)):
        final_sln = final_sln + num[coef]*(strt_b**coef)
    
    return final_sln

def dec_to_nbase(coef_l, end_b = None):
    pass

def nbase_to_nbase(coef_l, strt_b = None, end_b = None):
    pass

####### Main

