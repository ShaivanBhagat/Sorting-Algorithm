# running the Bubble sort and Quick sort algorithm here whilst also running the plotting file to plot the runtime performance

import plotting
import sys


# Python has a default maximum recursion limit of 1,000. The sorting algorithm functions exceed this limit
# The recurison limit can be extended using the sys.setrecursionlimit() function
# The limit was set to 2,000. However, I felt that a limit of 4,000 supports the runtime better and thus I set it to 4000

sys.setrecursionlimit(4000)  # this is to avoid hitting the recursion limit
plotting.generate_data()
