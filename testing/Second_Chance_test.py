import matplotlib.pyplot as plt
import numpy as np
def searchForElement(pageValue, referencedBitMap, fifo_queue):
    pageToInsertAt = 0

    for i in range(len(fifo_queue)):

        element = fifo_queue[i]

        if (referencedBitMap[element] == 0):
            pageToInsertAt = fifo_queue.pop(i)

            fifo_queue.append(pageValue)

            break

    for i in range(len(fifo_queue)):

        element = fifo_queue[i]

        if (referencedBitMap[element] == 1):
            referencedBitMap[element] = 0

            return pageToInsertAt

    return pageToInsertAt


def modifiedFIFO(arr, Frames, PageAccessSequence, startingPoint, referencedBitMap, fifo_queue, outputPageFault):
    for i in range(startingPoint, len(PageAccessSequence)):

        # Check if the page exists in the queue

        pageValue = PageAccessSequence[i]

        if (pageValue in fifo_queue):

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

                if (arr[j][i - 1] == pageToInsertAt):

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

        if (pageFaults == Frames):
            return (arr, pageFaults, referencedBitMap, existedPages, i)

        pageValue = PageAccessSequence[i]

        if (pageValue not in existedPages):

            pageFaults += 1

            existedPages.append(pageValue)

            for j in range(Frames):

                if (arr[j][i - 1] == -1):

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

    outputFrames, outputPageFault, referencedBitMap, fifo_queue, i = initialFramesInitializer(outputFrames, Frames,
                                                                                              PageAccessSequence,
                                                                                              referencedBitMap)

    outputFrames, referencedBitMap, fifo_queue, outputPageFault = modifiedFIFO(outputFrames, Frames, PageAccessSequence,
                                                                               i, referencedBitMap, fifo_queue,
                                                                               outputPageFault)

    return outputFrames, outputPageFault


# Test the algorithm against the size of the reference string

# Define the number of frames in memory
num_frames = 3

# Define a list of reference string sizes to test
ref_string_sizes = [10, 50, 100, 500, 1000]

# Initialize lists to store the results
page_faults_list = []

# Iterate through the reference string sizes
for ref_string_size in ref_string_sizes:
    # Generate a random reference string of the specified size
    ref_string = list(np.random.randint(1, 101, ref_string_size))

    # Call the FIFO page replacement function
    _,page_faults = secondChance(ref_string, num_frames)

    # Append the results to the lists
    page_faults_list.append(page_faults)

# Plot the results
plt.plot(ref_string_sizes, page_faults_list)
plt.xlabel("Reference String Size")
plt.ylabel("Page Faults")
plt.title("Second chance Page Replacement Algorithm - Reference String Size Test")
plt.show()

# Test the algorithm against the size of frames

# Define a constant reference string to use for testing
ref_string = list(np.random.randint(1, 101, 1000))

# Define a list of frame sizes to test
frame_sizes = [2, 4, 8, 16, 32]

# Initialize lists to store the results
page_faults_list = []

# Iterate through the frame sizes
for frame_size in frame_sizes:
    # Call the FIFO page replacement function
    _,page_faults = secondChance(ref_string, frame_size)

    # Append the results to the lists
    page_faults_list.append(page_faults)

# Plot the results
plt.plot(frame_sizes, page_faults_list)
plt.xlabel("Number of Frames")
plt.ylabel("Page Faults")
plt.title("Second chance Page Replacement Algorithm - Frame Size Test")
plt.show()