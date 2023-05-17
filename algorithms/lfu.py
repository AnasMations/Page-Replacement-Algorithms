def LFU(PageAccessSequence, Frames):
    """
    :param PageAccessSequence: list of numbers indicating the given page input
    :param Frames: integer number of frames
    :return: return two variables (list of list) of the output for each frame & (int) count of page fault
    """
    # Variables Initialization
    outputFrames = []
    outputPageFault = 0

    listToInsert = []
    frequency = {num: 0 for num in PageAccessSequence}

    # Adding an empty list for each Frame
    for i in range(Frames):
        outputFrames.append([])
        listToInsert.append(-1)

    for i in range(len(PageAccessSequence)):
        # Filling up initial Frames
        if i < Frames:
            for j in range(len(listToInsert)):
                if listToInsert[j] == -1:
                    listToInsert[j] = PageAccessSequence[i]
                    outputPageFault += 1
                    break
        else:
            if PageAccessSequence[i] not in listToInsert: # If page not found, do page replacement
                freqOptions = []
                sorted_frequency = dict(sorted(frequency.items(), key=lambda x: x[1]))
                min = sorted_frequency[0]
                # Get least frequencies
                for k, v in sorted_frequency.items():
                    if k in listToInsert and v <= min:
                        freqOptions.append(k)
                    else:
                        break

                print(freqOptions)

                for j in range(Frames):
                    if PageAccessSequence[i - Frames + j] in freqOptions:
                        listToInsert[ listToInsert.index(PageAccessSequence[i - Frames + j]) ] = PageAccessSequence[i]
                        outputPageFault += 1

        frequency[PageAccessSequence[i]] += 1

        for j in range(Frames):
            outputFrames[j].append(listToInsert[j])

    return outputFrames, outputPageFault

inputPageAccessSequence = [7, 0, 2, 4, 3, 1, 4, 7, 2, 0, 4, 3, 0, 3, 2, 7]
inputFrames = 3
list, pagefault = LFU(inputPageAccessSequence, inputFrames)

print(pagefault)
print(inputPageAccessSequence)
for frame in list:
    print(frame)