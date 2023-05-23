import matplotlib.pyplot as plt
import numpy as np

def LRU(page_list, msize):
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

        # Flip Memory List
        new_memory = []
        for i in range(msize):
            new_memory.append([])

        for i in range(len(memory_states)):
            for j in range(msize):
                new_memory[j].append(memory_states[i][j])

    return new_memory, miss


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
    ref_string = list(np.random.randint(1, 10, ref_string_size))

    # Call the FIFO page replacement function
    _,page_faults = LRU(ref_string, num_frames)

    # Append the results to the lists
    page_faults_list.append(page_faults)

# Plot the results
plt.plot(ref_string_sizes, page_faults_list)
plt.xlabel("Reference String Size")
plt.ylabel("Page Faults")
plt.title("LRU Page Replacement Algorithm - Reference String Size Test")
plt.show()

# Test the algorithm against the size of frames

# Define a constant reference string to use for testing
ref_string = list(np.random.randint(1, 10, 1000))

# Define a list of frame sizes to test
frame_sizes = [2, 4, 8, 16, 32]

# Initialize lists to store the results
page_faults_list = []

# Iterate through the frame sizes
for frame_size in frame_sizes:
    # Call the FIFO page replacement function
    _,page_faults = LRU(ref_string, frame_size)

    # Append the results to the lists
    page_faults_list.append(page_faults)

# Plot the results
plt.plot(frame_sizes, page_faults_list)
plt.xlabel("Number of Frames")
plt.ylabel("Page Faults")
plt.title("LRU Page Replacement Algorithm - Frame Size Test")
plt.show()