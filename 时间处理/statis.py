def union(time_list):
    len_t = len(time_list)
    if len_t == 0:
        return []
    elif len_t == 1:
        return time_list
    else:
        time_list = sorted(time_list,key= lambda x:x[0])
        print(time_list)
        newlist = []
        last_t = time_list[0]
        newlist.append(last_t)
        for i in range(1,len(time_list)):
            last_t = newlist[-1]
            this_t = time_list[i]
            last_start = last_t[0]
            last_end = last_t[1]
            this_start = this_t[0]
            this_end = this_t[1]

            if last_end>=this_start and last_end<=this_end:
                last = newlist.pop()
                last[1] = this_end
                newlist.append(last)
            elif last_end>=this_end:
                continue
            else:
                newlist.append(this_t)
        return newlist

di = {}
f = open('time','r')
for line in f.readlines():
    line = line.strip()
    line = line.split(' ')
    key = line[0]
    if key not in di.keys():
        start = int(line[1])
        end = int(line[2])
        di[key] = [[start,end]]
    else:
        start = int(line[1])
        end = int(line[2])
        di[key].append([start,end])
print(di)

for key in di.keys():
    time_list = di[key]
    result = union(time_list)
    print(result)
    # print(line)