def LFU(PageAccessSequence, Frames):
    """
    :param PageAccessSequence: list of numbers indicating the given page input
    :param Frames: integer number of frames
    :return: return two variables (list of list) of the output for each frame & (int) count of page fault
    """
    # Variables Initialization
    outputFrames = []
    outputPageFault = 0

    listToInsert = [] # Column list to insert each iteration to the Frames
    frequency = {num: 0 for num in PageAccessSequence} # Frequencies for each process
    fifoQueue = [] # Sorted FIFO Queue, first element to be replaced

    # Adding an empty list for each Frame
    for i in range(Frames):
        outputFrames.append([])
        listToInsert.append(-1) # Indicate NONE values by -1

    for i in range(len(PageAccessSequence)):
        # Filling up initial Frames
        if i < Frames:
            for j in range(len(listToInsert)):
                if listToInsert[j] == -1:
                    listToInsert[j] = PageAccessSequence[i]
                    fifoQueue.append(PageAccessSequence[i])
                    outputPageFault += 1
                    break
        else:
            if PageAccessSequence[i] not in listToInsert: # If page not found, do page replacement
                freqOptions = []
                sorted_frequency = dict(sorted(frequency.items(), key=lambda x: x[1]))
                min = 99999999
                # Get min value from listToInsert
                for num in listToInsert:
                    if min >= frequency[num]:
                        min = frequency[num]

                # Get least frequencies and add them to freqOptions
                for k, v in sorted_frequency.items():
                    if k in listToInsert and min == v:
                        min = v
                        freqOptions.append(k)

                #print(PageAccessSequence[i], min, sorted_frequency, listToInsert, fifoQueue, freqOptions)

                # Choosing page to replace based on the furthest page in the FIFO Queue and is in the freqOptions
                for j in fifoQueue:
                    if j in freqOptions:
                        listToInsert[ listToInsert.index(j) ] = PageAccessSequence[i]
                        frequency[j] = 0 # Setting replaced page freq with zero
                        outputPageFault += 1
                        break

                # Update FIFO Queue
                fifoQueue.append(PageAccessSequence[i]) # Add new process to end
                fifoQueue = fifoQueue[1:] # Remove top process


        frequency[PageAccessSequence[i]] += 1

        # Update the Frames with the updated listToInsert
        for j in range(Frames):
            outputFrames[j].append(listToInsert[j])

    return outputFrames, outputPageFault

inputPageAccessSequence = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2]
inputPageAccessSequence2 = [7, 0, 2, 4, 3, 1, 4, 7, 2, 0, 4, 3, 0, 3, 2, 7]
inputFrames = 3
list, pagefault = LFU(inputPageAccessSequence, inputFrames)

print(pagefault)
print(inputPageAccessSequence)
for frame in list:
    print(frame)