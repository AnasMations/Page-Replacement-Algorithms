import matplotlib.pyplot as plt
import numpy as np

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
    _,page_faults = LFU(ref_string, num_frames)

    # Append the results to the lists
    page_faults_list.append(page_faults)

# Plot the results
plt.plot(ref_string_sizes, page_faults_list)
plt.xlabel("Reference String Size")
plt.ylabel("Page Faults")
plt.title("LFU Page Replacement Algorithm - Reference String Size Test")
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
    _,page_faults = LFU(ref_string, frame_size)

    # Append the results to the lists
    page_faults_list.append(page_faults)

# Plot the results
plt.plot(frame_sizes, page_faults_list)
plt.xlabel("Number of Frames")
plt.ylabel("Page Faults")
plt.title("LFU Page Replacement Algorithm - Frame Size Test")
plt.show()