if __name__ == '__main__':
    N = int(input())
    new_list=[]
    for i in range(0,N):
        comand=list(map(str,input().split()))
        if comand[0]=="insert":
            new_list.insert(int(comand[1]),int(comand[2]))
            
        elif comand[0]=="append":
            new_list.append(int(comand[1]))
        elif comand[0]=="remove":
            new_list.remove(int(comand[1]))
        elif comand[0]=="sort":
            new_list.sort()
        elif comand[0]=="reverse":
            new_list.reverse()
        elif comand[0]=="pop":
            new_list.pop()
        elif comand[0]=="print":
            print(new_list)
        