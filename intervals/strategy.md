## for merge intervals

Iterate over intervals
Check if intervals overlap
Merge Overlapping intervals

while merging:
    Well, if we have two intervals, A and B, the relationship between A and B must fall into 1 of 3 cases.
    Interval A and B do not overlap
    Interval A and B partially overlap
    Interval A and B completely overlap

check overlap like this:
```
def do_overlap(interval_1, interval_2):
    front = max(interval_1[0], interval_2[0])
    back = min(interval_1[1], interval_2[1])
    return back - front >= 0 
```

helps to standardize approach -> to get the duration of overlap too




## sweeping line thing -> used for? meeting rooms 2, how many meeting rooms there are right
