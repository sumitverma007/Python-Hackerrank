if __name__ == '__main__':
    N = int(input())
    initial_list=[]
    for _ in range(N):
        temp_list=input().split(" ")
        if temp_list[0]=="insert":
            initial_list.insert(int(temp_list[1]),int(temp_list[2]))
        elif temp_list[0]=="print":
            print(initial_list)
        elif temp_list[0]=="remove":
            initial_list.remove(int(temp_list[1]))
        elif temp_list[0]=="append":
            initial_list.append(int(temp_list[1]))
        elif temp_list[0]=="sort":
            initial_list.sort()
        elif temp_list[0]=="pop":
            initial_list.pop()
        else:
            initial_list.reverse()        

