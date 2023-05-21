def lru(page_list, msize):
    mptr, hit, miss = 0, 0, 0
    memory = [-1 for _ in range(msize)]
    memory_states = []

    for i in range(len(page_list)):
        flag = 0
        for j in memory:
            if j == page_list[i]:
                
                flag = 1
                break

        if flag == 0:
            miss += 1
            if mptr >= msize:
                left = page_list[:i]
                dist = [-1 for _ in range(10)]
                present = [-1 for _ in range(10)]

                for j in range(len(left)):
                    k = left[j]
                    dist[k] = i - j
                    for l in range(len(memory)):
                        if memory[l] == left[j]:
                            present[k] = l
                            break

                max_dist, num = 0, 0
                for j in range(len(dist)):
                    if dist[j] > max_dist and present[j] > -1:
                        max_dist = dist[j]
                        num = present[j]
                memory[num] = page_list[i]
            else:
                memory[mptr] = page_list[i]
                mptr += 1

        # Append current state of memory to memory_states list
        memory_states.append(list(memory))

    return memory_states, miss


inputPageAccessSequence = [7, 0, 2, 4, 3, 1, 4, 7, 2, 0, 4, 3, 0, 3, 2, 7]
inputFrames = 3
memory_list, page_faults = lru(inputPageAccessSequence, inputFrames)

print(page_faults)
print( inputPageAccessSequence)

for state in memory_list:
    print(state)
    
#inputPageAccessSequence =  [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
#inputFrames = 4
#list, pagefault = LRU(inputPageAccessSequence, inputFrames)(output 6 page faults)
#print(pagefault)
#print(inputPageAccessSequence)
#for frame in list:
#    print(frame)
    