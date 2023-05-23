import matplotlib.pyplot as plt
import numpy as np
def FIFO(PageAccessSequence, Frames):
    """
    :param PageAccessSequence: list of numbers indicating the given page input
    :param Frames: integer number of frames
    :return: return two variables (list of list) of the output for each frame & (int) count of page fault
    """
    # Variables Initialization
    outputFrames = []
    outputPageFault = 0

    listToInsert = []
    queue = []

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
            if PageAccessSequence[i] not in listToInsert:
                for j in range(len(listToInsert)):
                    if listToInsert[j] == PageAccessSequence[i - Frames]:
                        listToInsert[j] = PageAccessSequence[i]
                        outputPageFault += 1

        for j in range(Frames):
            outputFrames[j].append(listToInsert[j])

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
    _,page_faults = FIFO(ref_string, num_frames)

    # Append the results to the lists
    page_faults_list.append(page_faults)

# Plot the results
plt.plot(ref_string_sizes, page_faults_list)
plt.xlabel("Reference String Size")
plt.ylabel("Page Faults")
plt.title("FIFO Page Replacement Algorithm - Reference String Size Test")
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
    _,page_faults = FIFO(ref_string, frame_size)

    # Append the results to the lists
    page_faults_list.append(page_faults)

# Plot the results
plt.plot(frame_sizes, page_faults_list)
plt.xlabel("Number of Frames")
plt.ylabel("Page Faults")
plt.title("FIFO Page Replacement Algorithm - Frame Size Test")
plt.show()