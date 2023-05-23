import matplotlib.pyplot as plt
import numpy as np

def initialFramesInitializer(arr, Frames, PageAccessSequence):
    pageFaults = 1

    existedPages = []

    i = 1

    existedPages.append(PageAccessSequence[0])

    arr[0][0] = PageAccessSequence[0]

    while i < len(PageAccessSequence):

        if (pageFaults == Frames):
            return (arr, pageFaults, i)

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

            for j in range(Frames):
                arr[j][i] = arr[j][i - 1]

        i += 1

    return (arr, pageFaults, i)


def optimalCaseOneInitializer(Frames, page, pageValue, arr):
    for frame in range(Frames):

        if (arr[frame][page - 1] == pageValue):

            arr[frame][page] = pageValue

        else:

            arr[frame][page] = arr[frame][page - 1]

    return arr


def optimalCaseTwoInitializer(PageAccessSequence, Frames, page, pageValue, arr):
    """
        optimalCaseTwoInitializer() function Compares between each page in the current column for the "longest one in the future".

        "longest one in the future" technically means that you from the pages you have in the current column you should find the one with longest distance,

        but note that for each page you shuold consider only the first occurence of that page while you're searching for the longest distance.
    """

    longestPageIndex = 0

    for frame in range(Frames):
        index = (PageAccessSequence[page + 1:].index(arr[frame][page - 1])) + (page + 1)

        longestPageIndex = max(index, longestPageIndex)

    for frame in range(Frames):

        if (arr[frame][page - 1] == PageAccessSequence[longestPageIndex]):

            arr[frame][page] = pageValue

        else:
            arr[frame][page] = arr[frame][page - 1]

    return arr


def optimalCaseThreeInitializer(Frames, page, pageValue, arr, nonFoundPages):
    """
       optimalCaseThreeInitializer() function will handle a page fault which occurs only at one position.

       Parameter nonFoundPages will be a list of only one element.

    """

    for frame in range(Frames):

        if (arr[frame][page - 1] == nonFoundPages[0]):

            arr[frame][page] = pageValue

        else:

            arr[frame][page] = arr[frame][page - 1]

    return arr


def optimalCaseFourInitializer(PageAccessSequence, Frames, page, pageValue, arr, nonFoundPages):
    """
       For the pages that do not exist optimalCaseFourInitializer() function

       will search for the "least recently used (LRU)" page and a page fault will occur at its position.

    """
    leastRecentlyUsedPageIndex = len(PageAccessSequence)

    for val in nonFoundPages:

        for pages in range(page - 1, 0, -1):

            if (val == PageAccessSequence[pages]):
                leastRecentlyUsedPageIndex = min(pages, leastRecentlyUsedPageIndex)
                break

    for frame in range(Frames):

        if (arr[frame][page - 1] == PageAccessSequence[leastRecentlyUsedPageIndex]):

            arr[frame][page] = pageValue

        else:

            arr[frame][page] = arr[frame][page - 1]

    return arr


def caseChecker(PageAccessSequence, arr, Frames, page):
    # Case 1
    for frames in range(Frames):

        if (PageAccessSequence[page] == arr[frames][page - 1]):
            return (1, [])

    # Check for Cases 2, 3, and 4

    counter = 0

    nonFoundPages = []

    for frames in range(Frames):

        if ((page < len(PageAccessSequence) - 1) and (arr[frames][page - 1] in PageAccessSequence[page + 1:])):
            counter += 1

        else:
            nonFoundPages.append(arr[frames][page - 1])

    # Case 2
    if (counter == Frames):
        return (2, [])

    # Case 3
    elif (counter == Frames - 1):
        return (3, nonFoundPages)

    # Case 4
    else:
        return (4, nonFoundPages)


def OPTIMAL(PageAccessSequence, Frames):
    """
    :param PageAccessSequence: list of numbers indicating the given page input
    :param Frames: integer number of frames
    :return: return two variables (list of list) of the output for each frame & (int) count of page fault
    """
    # Variables Initialization
    outputFrames = [[-1] * len(PageAccessSequence) for _ in range(Frames)]
    outputPageFault = 0

    # initialize the memory with initial frames

    outputFrames, outputPageFault, i = initialFramesInitializer(outputFrames, Frames, PageAccessSequence)

    for page in range(i, len(PageAccessSequence)):

        caseNumber, nonFoundPages = caseChecker(PageAccessSequence, outputFrames, Frames, page)

        #  Case 1 : Page already exists & a Hit occurs
        if (caseNumber == 1):
            outputFrames = optimalCaseOneInitializer(Frames, page, PageAccessSequence[page], outputFrames)

        # Case 2: All pages in the current column exist in the page reference string after the page to be placed & a page fault occurs
        elif (caseNumber == 2):
            outputFrames = optimalCaseTwoInitializer(PageAccessSequence, Frames, page, PageAccessSequence[page],
                                                     outputFrames)
            outputPageFault += 1

        # Case 3: Only one page in the current column does not exist in the page reference string after the page to be placed & a page fault occurs
        elif (caseNumber == 3):
            outputFrames = optimalCaseThreeInitializer(Frames, page, PageAccessSequence[page], outputFrames,
                                                       nonFoundPages)
            outputPageFault += 1

        # Case 4: Two or more pages in the current column do not exist in the page reference string after the page to be placed & a page fault occurs
        else:
            outputFrames = optimalCaseFourInitializer(PageAccessSequence, Frames, page, PageAccessSequence[page],
                                                      outputFrames, nonFoundPages)
            outputPageFault += 1

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
    _,page_faults = OPTIMAL(ref_string, num_frames)

    # Append the results to the lists
    page_faults_list.append(page_faults)

# Plot the results
plt.plot(ref_string_sizes, page_faults_list)
plt.xlabel("Reference String Size")
plt.ylabel("Page Faults")
plt.title("Optimal Page Replacement Algorithm - Reference String Size Test")
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
    _,page_faults = OPTIMAL(ref_string, frame_size)

    # Append the results to the lists
    page_faults_list.append(page_faults)

# Plot the results
plt.plot(frame_sizes, page_faults_list)
plt.xlabel("Number of Frames")
plt.ylabel("Page Faults")
plt.title("Optimal Page Replacement Algorithm - Frame Size Test")
plt.show()