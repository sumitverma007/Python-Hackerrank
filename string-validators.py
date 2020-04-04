if __name__ == '__main__':
    s = input()
    al_st=0
    a_s=0
    d_s=0
    l_s=0
    u_s=0
    for i in range(len(s)):
        if(s[i].isalnum()==True):
            al_st=1
            
        if(s[i].isalpha()==True):
            a_s=1
            
        if(s[i].isdigit()==True):
            d_s=1
            
        if(s[i].islower()==True):
            l_s=1
            
        if(s[i].isupper()==True):
            u_s=1
            

    print(al_st==1)
    print(a_s==1)   
    print(d_s==1)    
    print(l_s==1)    
    print(u_s==1)     