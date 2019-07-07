import sys
sys.path.append('./TimeProcess')
from TimeLine import TimeLine

if __name__ == '__main__':
    di = {}
    f = open('time', 'r')
    for line in f.readlines():
        line = line.strip()
        line = line.split(' ')
        key = line[0]
        # 将开始和结束时间点加入相应key对应的值中
        if key not in di.keys():
            start = int(line[1])
            end = int(line[2])
            di[key] = [[start, end]]
        else:
            start = int(line[1])
            end = int(line[2])
            di[key].append([start, end])
    print(di)

    for key in di.keys():
        time_list = di[key]
        # 计算并集
        # result = union(time_list)
        # print(result)
        result = TimeLine.intersect(time_list)
        print(key, result)
        # print(line)