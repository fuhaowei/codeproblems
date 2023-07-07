sliding windows are an extension of 2 pointers.

we use 2 pointers to create the window.

main jist is that the problem has a maximum or minimum subrange that will satisify a given conidtion.

we then expand or contract the window to find the optimal range. 

there will be a constant window size, or a variable window size. so we can use memory to save time, get from o(n^2) to o(n).


Expand our window
Meet the condition and process the window
Contract our window

def sliding_window(nums):
    # Iterate over elements in our input
        # Expand the window
        # Meet the condition to stop expansion
            # Process the current window   
            # Contract the window

