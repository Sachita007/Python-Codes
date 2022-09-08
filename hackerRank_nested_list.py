if __name__ == '__main__':
    record=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
    
   
    def min(record):
        min=record[0][1]
        for i in record:
            if min>i[1]:
                min=i[1]
        return min
    min1=min(record)
    
    new_list = [x for x in record if x[1]!=min1]
    min2=min(new_list)
    
    n_record = [x for x in new_list if x[1]==min2 ]
    n_record = [x[0] for x in n_record]
   
    for i in sorted( n_record):
        print(i)