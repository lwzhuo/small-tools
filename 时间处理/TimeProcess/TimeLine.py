class TimeLine(object):
    # 将多个时间序列取并集
    @staticmethod
    def union(time_list):
        len_t = len(time_list)
        if len_t == 0:
            return []
        elif len_t == 1:
            return time_list
        else:
            # 给所有时间线按照开始时间从小到大排序
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

                if last_end>=this_start and last_end<=this_end:#上一个时间段的结束时间在这个时间段中(两个时间段部分相交)
                    last = newlist.pop()
                    last[1] = this_end
                    newlist.append(last)
                elif last_end>=this_end:# 上一个时间段的结束时间大于这个时间段的结束时间(上一个时间段完全包住这个时间段)
                    continue
                else:# 其他情况 上一个时间段的结束时间小于这个时间段的开始时间(两个时间段没有交集)
                    newlist.append(this_t)
            return newlist

    #时间线取交集
    @staticmethod
    def intersect(time_list):
        len_t = len(time_list)
        if len_t == 0:
            return []
        elif len_t == 1:# 长度为1无法计算交集
            return []
        else:
            # 给所有时间线按照开始时间从小到大排序
            time_list = sorted(time_list, key=lambda x: x[0])
            print(time_list)
            newlist = []
            last_t = time_list[0]
            newlist.append(last_t)
            for i in range(1, len(time_list)):
                last_t = newlist.pop()#弹出上一个时间段
                this_t = time_list[i]#使用当前时间段
                last_start = last_t[0]
                last_end = last_t[1]
                this_start = this_t[0]
                this_end = this_t[1]

                if this_end<last_start:
                    if i == len(time_list) - 1:  # 是最后一个时间线 终止循环
                        break
                    else:
                        newlist.append(last_t) # 放回原位
                        continue
                if this_start < last_start:#对当前开始时间的附加处理
                    this_start = last_start


                if last_end >= this_start and last_end <= this_end:  # 上一个时间段的结束时间在这个时间段中(两个时间段部分相交)
                    # 进行截断处理 截断成last_t和this_t公共部分和this_t剩余部分
                    public = [this_start,last_end] # 公共部分
                    left = [last_end,this_end] # 剩余部分
                    # 按照先后顺序放入newlist中
                    newlist.append(public)
                    newlist.append(left)
                elif last_end >= this_end:  # 上一个时间段的结束时间大于这个时间段的结束时间(上一个时间段完全包住这个时间段)
                    public = [this_start,this_end]
                    left = [this_end,last_end]
                    # 按照先后顺序放入newlist中
                    newlist.append(public)
                    newlist.append(left)
                else:  # 其他情况 上一个时间段的结束时间小于这个时间段的开始时间(两个时间段没有交集)
                    newlist.append(this_t)

                if i == len(time_list)-1:#是最后一个时间线
                    newlist.pop()#弹出最后一个数据
            return newlist
