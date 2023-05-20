def searchForElement(pageValue, referencedBitMap, fifo_queue):

    pageToInsertAt = 0

    for i in range(len(fifo_queue)):

        element = fifo_queue[i]

        if( referencedBitMap[element] == 0 ):

            pageToInsertAt = fifo_queue.pop(i)

            fifo_queue.append(pageValue)

            break
    
    for i in range(len(fifo_queue)):

        element = fifo_queue[i]

        if( referencedBitMap[element] == 1 ):

            referencedBitMap[element] = 0

            return pageToInsertAt

    return pageToInsertAt


def modifiedFIFO(arr, Frames, PageAccessSequence, startingPoint, referencedBitMap, fifo_queue, outputPageFault):

    for i in range(startingPoint, len(PageAccessSequence)):

        # Check if the page exists in the queue

        pageValue = PageAccessSequence[i]

        if( pageValue in fifo_queue ):

            # If the page value is found, a Hit occurs and we do what we usually do in this case
            # 
            # which is copying the previous column values into the current column values,
            #
            # but in addition to that we should change the value of the referenced bit of the page at which the Hit occurs again to be 1.

            referencedBitMap[pageValue] = 1

            for j in range(Frames):

                arr[j][i] = arr[j][i - 1]

        else:

            # If the page value is not found, a page fault occurs and we should stick to 2 rules
            #
            # rule 1: scan the queue in a FIFO approach that is start iterating from index 0
            #
            # rule 2: according to the second chance approach, the page faults must occur at the "First In" page whose referenced bit value is 0,
            #
            # and the "First In" page whose referenced bit value is 1 will be reset to 0 again.

            outputPageFault += 1

            pageToInsertAt = searchForElement(pageValue, referencedBitMap, fifo_queue)

            for j in range(Frames):

                if( arr[j][i - 1] == pageToInsertAt):

                    arr[j][i] = pageValue

                else:

                    arr[j][i] = arr[j][i - 1]

    return (arr, referencedBitMap, fifo_queue, outputPageFault)


def initialFramesInitializer(arr, Frames, PageAccessSequence, referencedBitMap):

    pageFaults = 1

    existedPages = []

    i = 1

    existedPages.append(PageAccessSequence[0])

    arr[0][0] = PageAccessSequence[0]

    while i < len(PageAccessSequence):

        if( pageFaults == Frames ):
            return (arr, pageFaults, referencedBitMap, existedPages, i)

        pageValue = PageAccessSequence[i]

        if( pageValue not in existedPages ):

            pageFaults += 1

            existedPages.append(pageValue)

            for j in range(Frames):

                if( arr[j][i - 1] == -1 ):

                    arr[j][i] = pageValue

                    break
                
                else:
                    arr[j][i] = arr[j][i - 1]
        else:
            # If page value of the reference string already exist in memory
            # then change its reference bit to 1

            referencedBitMap[pageValue] = 1

            for j in range(Frames):

                arr[j][i] = arr[j][i - 1]

        i += 1

    return (arr, pageFaults, referencedBitMap, existedPages, i)

def secondChance(PageAccessSequence, Frames):
    """
    :param PageAccessSequence: list of numbers indicating the given page input
    :param Frames: integer number of frames
    :return: return two variables (list of list) of the output for each frame & (int) count of page fault
    """

    """
        Second Chance Page replacement algorithm is a modified form of the FIFO page replacement algorithm, and
        
        relatively better than FIFO at little cost for the improvement.

        It works by looking at the front of the queue as FIFO does, but instead of immediately paging out that page, it checks to see if its referenced bit is set.

        If it is not set, the page is swapped out. Otherwise, the referenced bit is cleared.
    """

    # Variables Initialization
    outputFrames = [[-1] * len(PageAccessSequence) for _ in range(Frames)]
    outputPageFault = 0

    # For the second chance algorithm a hash map will be used to store each page value in the reference string
    #
    # with its associated referenced bit value
    #
    # Initially each page's referenced bit value is set to 0

    referencedBitMap = dict()

    fifo_queue = list()

    for i in PageAccessSequence:

        referencedBitMap[i] = 0

    # Initialize initial frames

    outputFrames, outputPageFault, referencedBitMap, fifo_queue, i = initialFramesInitializer(outputFrames, Frames, PageAccessSequence, referencedBitMap)


    outputFrames, referencedBitMap, fifo_queue, outputPageFault = modifiedFIFO(outputFrames, Frames, PageAccessSequence, i, referencedBitMap, fifo_queue, outputPageFault)


    return outputFrames, outputPageFault

inputPageAccessSequence = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 3, 5]

inputFrames = 3

Outputlist, pagefault = secondChance(inputPageAccessSequence, inputFrames)

print(pagefault)

print(inputPageAccessSequence)


for frame in Outputlist:
    print(frame)    