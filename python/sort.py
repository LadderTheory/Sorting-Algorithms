#the format of each algorithm will be a list of integers

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
#end swap

def bubble(arg):
    end = len(arg) - 1
    while end > 0:
        high = arg[0]
        highpos = 0
        for i in range(end):
            if high < arg[i]:
                high = arg[i]
                highpos = i
        
        swap(arg, end, highpos)
        end -= 1
    
    return arg
#end bubble

def merge(L, R):
    s = []

    a, b = 0, 0
    while a < len(L) and b < len(R):
        if L[a] < R[b]:
            s.append(L[a])
            a += 1
        else:
            s.append(R[b])
            b += 1
    
    for i in range(a, len(L)):
        s.append(L[i])

    for i in range(b, len(R)):
        s.append(R[i])

    return s
#end merge

def merge_recurse(arg):
    #print(arg)

    halfs = []
    halfs.append(arg[:len(arg)//2])
    halfs.append(arg[len(arg)//2:])
    
    #print(halfs)

    for i in range(len(halfs)):
        if len(halfs[i]) > 1:
            halfs[i] = merge_recurse(halfs[i])

    srtd = merge(halfs[0], halfs[1])

    #print(srtd)
    arg.clear()
    arg.extend(srtd)
    return arg
#end merge_recurse

def merge_iter(arg):
    cnt = len(arg)

    #print(arg)

    current_size = 1
    while current_size < cnt - 1:
        left = 0
        while left < cnt - 1:
            mid = left + current_size - 1

            a = (2 * current_size) + left - 1
            b = cnt - 1
            right = (a, b)[a > b] #wtf is this syntax, its one unreadable line that replaces an if else

            l = []
            r = []
            #print(left, mid, right, current_size)
            for i in range(left, mid + 1):
                if i < cnt:
                    l.append(arg[i])
            
            for i in range(mid + 1, right + 1):
                r.append(arg[i])
            
            m = merge(l, r)

            for i in range(len(m)):
                arg[left + i] = m[i]

            left = left + (current_size * 2)
        
        current_size = current_size * 2

    #print(arg)

    return arg
#end merge_iter

#for some reason, this is much slower than the recursive method
def quick_iter(arg):
    chunks = [arg.copy()]
    is_sorted = False
    while not is_sorted:
    #for repeat in range(3):
        is_sorted = True
        for c in range(len(chunks)):
            if len(chunks[c]) > 1:
                is_sorted = False

                chunk = chunks[c]

                smol = []
                bigg = []
                pivot = chunk[0]
                for i in range(1, len(chunk)):
                    if chunk[i] < pivot:
                        smol.append(chunk[i])
                    else:
                        bigg.append(chunk[i])

                
                
                pre = chunks[:c]
                post = chunks[c+1:]

                current = []
                if len(smol) > 0:
                    current.append(smol)
                
                current.append([pivot])

                if len(bigg) > 0:
                    current.append(bigg)

                chunks = pre + current + post
                #print(chunks)

                #break
    
    arg.clear()

    for i in range(len(chunks)):
        arg.append(chunks[i][0])

    return arg
#end quick_iter

def quick_recurse(arg):
    pivot = arg[0]
    less = []
    more = []
    for i in range(1, len(arg)):
        if arg[i] < pivot:
            less.append(arg[i])
        else:
            more.append(arg[i])

    if len(less) > 1:
        less = quick_recurse(less)

    if len(more) > 1:
        more = quick_recurse(more)

    less.append(pivot)

    arg.clear()
    arg.extend(less + more)
    return arg
#end quick_recurse

def selection(arg):
    cnt = len(arg)

    start = 0
    while start < cnt:
        low = arg[start]
        lowpos = start
        for i in range(start, cnt):
            if arg[i] < low:
                lowpos = i
                low = arg[lowpos]
        
        swap(arg, start, lowpos)
        start += 1

    print(arg)
    return arg
#end selection

def insertion(arg):
    cnt = len(arg)

    for i in range(1, cnt):
        #print(arg, cnt, i)
        if arg[i] <= arg[i-1]:
            popped = arg.pop(i)

            for j in range(i-1, -1, -1):
                #print(arg, popped, arg[j])
                if popped > arg[j]:
                    arg.insert(j+1, popped)
                    break
                
                if j == 0:
                    arg.insert(j, popped)

    return arg
#end insertion

def shell(arg):
    cnt = len(arg)

    sec = cnt // 2
    while sec >= 1:
        #print("sec: ", sec)
        pos = 0
        while pos < cnt:
            for i in range(pos,pos+sec):
                if i+sec < cnt:
                    #print(arg[i], arg[i+sec])
                    if arg[i] > arg[i+sec]:
                        swap(arg, i, i+sec)
                else:
                    break
            pos += sec
        sec -= 1
        #sec //= 2

    #insertion(arg)
#end shell

def gravity(arg):
    cnt = len(arg)
    
    beads = []
    for i in range(cnt):
        for j in range(arg[i]):
            if len(beads) > j:
                beads[j] += 1
            else:
                beads.append(1)

    #print (beads)

    fallen = []
    empty = False
    while not empty:
        current = 0
        empty = True
        for i in range(len(beads)):
            if beads[i] > 0:
                empty = False
                beads[i] -= 1
                current += 1
            else:
                break
        
        if current > 0:
            fallen.append(current)

    arg.clear()
    arg.extend(list(reversed(fallen)))
    return arg
#end gravity