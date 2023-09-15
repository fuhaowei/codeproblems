class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        open_counter = 0
        temp_string = ""
        res_string = ""
        
        for letter in s:
            #if we hv close bracket
            if letter == "]":
                #pop everything until we get [, that goes into the temp string
                #pop one after [, we will get a number, int cast that
                #multiply that number with temp string
                #case on the open_counter
                #either add back to stack or add into resstring
                while stack:
                    curletter = stack.pop()
                    if curletter == "[":
                        open_counter -= 1
                        break
                    else:
                        #everything here would just be letters
                        temp_string = temp_string + curletter

                temp_string = temp_string[::-1]
                str_number = ""
                while stack and stack[-1].isnumeric():
                    tmpnumber = stack.pop()
                    str_number += tmpnumber

                str_number = str_number[::-1]
                number = int(str_number)

                actual_chunk = temp_string * number

                if open_counter > 0:
                    #put it back on stack
                    for letter in actual_chunk:
                        stack.append(letter)
                #append straight to res
                else:
                    res_string = res_string + actual_chunk

                temp_string = ""

            elif letter == "[":
                open_counter += 1
                stack.append(letter)

            elif letter.isalpha():
                if open_counter == 0:
                    res_string += letter
                else:
                    stack.append(letter)

            else:
                stack.append(letter)

        return res_string
         