if __name__ == '__main__':
    score=[]
    name=[]
    for _ in range(int(input())):
        name1 = input()
        score1 = float(input())
        name.append(name1)
        score.append(score1)
    max_element1=min(score)
    max_element2=max(score)
    for i in score:
        if i>max_element1 and i<=max_element2:
            max_element2=i
    idx=[]
    for i in range(0,len(score)):
        if score[i]==max_element2:
            idx.append(i)
    result_name=[]
    for i in idx:
        result_name.append(name[i])
    result_name.sort()
    for i in result_name:
        print(i)   
        
