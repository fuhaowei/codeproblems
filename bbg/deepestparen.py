"Given a string, find the deepest string nested inside a '()', '[]' or '{}'."


# Given a string with nested brackets e.g. "ab(cd[]m){(ef)g}", return all of its most deeply nested substrings

'''
"abc(def)ghi" => ["def"]
"abc(def[ghi]jkl)mno" => ["ghi"]
"abc(def)ghi[jkl]mno" => ["def", "jkl"]
"abc" => []
"" => []

#iterate through, keep a stack + ans array
#if we get new (, throw everything in stack and what we previously added into ans array away)

#so its just final answer array

