"Given a string, find the deepest string nested inside a '()', '[]' or '{}'."

e.g.
'''
"abc(def)ghi" => ["def"]
"abc(def[ghi]jkl)mno" => ["ghi"]
"abc(def)ghi[jkl]mno" => ["def", "jkl"]
"abc" => []
"" => []

#iterate through, keep a stack + ans array
#if we get new (, throw everything in stack and what we previously added into ans array away)

#so its just final answer array
