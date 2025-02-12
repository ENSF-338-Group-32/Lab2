1. Describe the algorithm you will use to find the room. Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan [0.5 pts]

Based on the only knowledge known/given being the sign, I belive Binary search is the optimal search algorithim for this instance.

This is due to several infered facts:
    1.  Rooms are sorted from least to greatest
    2.  Rooms can be traversed linearly
    3.  Room falls within a known range which is given
    4.  Rooms alongside "All Other Rooms" are infered to be greater than 130
    5.  Total # of rooms are intially unknown

2. How many ”steps” it will take to find room EY128? And what is a “step” in this case? [0.25 pts]

Steps in this algorithim surround the action of splitting a decided subarray of rooms in half until the correct room is found.
    In each step, the room directly in front of the user can act as the pivot.

Working through this systematically:
    Step #1: Follow the left arrow, treating each arrow as a subarray with a known range of numbers

    Step #2: Move to the bottom left corner of the room based on this decision.
            Note last room within sight is 110.
            Know that all room to the right of the top left corner are greater than 110.
            Thus a binary search can be infered in the same fashion as the signs.
            Rooms to the left and rooms to the right can be split into two subarrays
                    Rooms less than 110
                    Rooms greater than 110
            Pick Rooms greater than 110
            Repeat.

    Step #3: Move to the top left corner of the room based on this decision.
            Note last room within sight is 124.
            Know that all room to the right of the top left corner are greater than 124.
            Thus a binary search can be infered in the same fashion as the signs.
            Rooms to the left and rooms to the right can be split into two subarrays
                    Rooms less than 124
                    Rooms greater than 124
            Pick Rooms greater than 124
            Repeat.

    Step #4: Move to the top right corner of the room based on this decision.
            Note last room within sight is at least 130.
            Thus a binary search can be infered in the same fashion as the signs.
            Rooms to the left and rooms to the right can be split into two subarrays
                    Rooms less than 130
                    Rooms greater than 130
            Pick Rooms less than 130
            
    Step #5:Find range of rooms within subarray
            Note first room is 124 and last room within sight is 138.  Middle is between 130 and 132, arbitarily pick 132.
            Thus a simple binary search can be infered
            Rooms to the left and rooms to the right can be split into two subarrays
                    Rooms less than 132
                    Rooms greater than 132
            Pick Rooms less than 132
            Repeat.

    Step #6:Find range of rooms within subarray
            Note first room is 124 and last room within range is 130.  Middle is between 126 and 128, Step #7 exists depending on arbitary choice.  If 128, end here.  Else:
            Thus a simple binary search can be infered
            Rooms to the left and rooms to the right can be split into two subarrays
                    Rooms less than 126
                    Rooms greater than 126
            Pick Rooms greater than 126
            Repeat.

    Step #7 (Optional):Find range of rooms within subarray
            Note first room is 128 and last room within range is 130.  Middle is between 128 and 130, Step #8 exists depending on arbitary choice.  If 128, end here.  Else:

    Step #8(Optional):Find range of rooms within subarray
            Note only room is 128, end here.
            
3. Is this a best-case scenario, worst-case scenario, or neither? [0.25 pts]

    This can generally be described as the worst-case scenario
    Room 128 Does not come up as the piot in any step below #5
    Room 128 can only become a pivot arbitarily past step #5

4. With this particular sign and floor layout, explain what a worst-case or best-
case scenario would look like [0.5 pts]

    A worst case scenario can be descirbed like this one:
        1. End range of rooms are unknown
        2. Desired room is not found at the corner
        3. Number of rooms along each wall is even

    Base case scenario can be descirbed like:
        1. End range is known
        2. Desired rooms is found at bottom left or right
        3. Number of rooms along each wall is odd

5. Suppose after a few weeks in the term you memorize the layout of the floor.
How would you improve the algorithm to make it more efficient? [0.5 pts]

    Lowest Room # Should be memorized (Already Known)
    Lowest Room # Should be memorized (Will Need to be memorized)
    Undertsanding that layout is a loop

    Based on these understandings we can optimize the layout to consider making initial step #1 based not on greater or less than,
    but based on closer to or further from.

    Take room 128 for example.  138-128 = 10, where as 128-100 = 28.  Therefore it is in our advantage to move right,
    depite what conentional binary search tells us, as we understand the layout is a loop.