class State:
    def __init__(self,a,b):
        self.time = a
        self.index = b

    def __repr__(self):
        return("State({},{})".format(self.time,self.index))

for fileno in range(1, 11):
    f = open(f"{fileno}.in", "r")
    data = f.read().strip().split('\n')
    n = int(data[0])
    stateList = [0]*2*n

    i=0
    while (i < n):

        l = data[i+1].split(' ')
        start = int(l[0])
        end = int(l[1])

        stateList[2*i] = State(start, i)
        stateList[2*i+1] = State(end, i)
        i += 1

    stateList.sort(key = lambda state:state.time)

    actualCover = 0;
    alone = [0] * n
    last = 0;
    set1 = set()

    for out in stateList:
        if (len(set1) == 1):
            for setItem in set1:
                alone[setItem] += out.time - last

        if (len(set1) > 0):
            actualCover += out.time - last

        if (out.index in set1):
            set1.remove(out.index)
        else:
            set1.add(out.index)

        last = out.time

    ret = 0;
    for outint in alone:
        ret = max(ret, actualCover - outint)
    output = open(f"{fileno}.out", "w")
    output.write(str(ret))
    output.close()

