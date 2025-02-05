Mention at least two aspects that make interpolation search better than binary search [0.1 pts]

    Interpolation search tries to find a better start point based off the key and the data rather than just starting in the middle like binary search. There’ll be less comparisons as its starts closer to the key.

Interpolation search assumes that data is uniformly distributed. What happens if this data follows a different distribution? Will the performance be affected? Why? [0.2 pts]

    The performance will be significantly affected as interpolation search tries to find the best starting point using the linear interpolation formula but if a different distribution is used the estimated starting point will be inaccurate leading to more recursive jumps and unneeded searches and leading to a worse time complexity.

If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected? [0.1 pts]

    The part of the code that would be affected is the code that figures out the optimal starting position and it would have to be modified based off the distribution.

When is linear search your only option for searching data as binary and interpolation search may fail? [0.2 pts]

    Linear search is your only option when the data is unsorted as binary search and interpolation search only work when the data is sorted.

In which case will linear search outperform both binary and interpolation search, and why? [0.2 pts]

    If the key is at or towards the beginning of the data set as linear search searches sequentially while binary starts in the middle and interpolation tries to find a position. The time complexity if the item is at the beginning for linear search would be Q(1). Linear search is also better when using small datasets as the extra code in binary and interpolation to find a position is unnecessary.

Is there a way to improve binary and interpolation search to solve this issue? [0.2 pts]

    If we know about the data set were working with we can do some preprocessing to make binary and interpolation more efficient.

