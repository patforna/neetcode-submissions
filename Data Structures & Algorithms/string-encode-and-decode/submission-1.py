DELIMITER = ';'

class Solution:

    def encode(self, strs: List[str]) -> str:
        # this is not a wire-level problem, simply string in string out
        # simply joining by "," or similar doesn't work because input could contain ","
        # two ways around it:
        # 1 escape word delimeters before encoding
        # 2 prefix each word with length (same ideas as content-legnth in HTTP)
        #   2.1 either fixed-length zero padded
        #   2.2 variable length + delimeter
        #
        # we'lmplement 2.2

        parts = []
        for s in strs:
            parts.append(f"{len(s)}{DELIMITER}{s}")

        return "".join(parts)

    def decode_(self, s: str) -> List[str]:
        # read digits until ;
        # parse digits to number
        # keep track of current position
        # return slice between current position and offset
        # + invalid format handling
        
        result = []
        block_start = 0
        i = 0
        while i < len(s):
            if s[i] != DELIMITER: # alternative would be s.find(DELIMETER, block_start)
                i += 1
            else:
                length = int(s[block_start:i]) # may raise                
                string_start = i + 1
                block_end = string_start + length
                result.append(s[string_start:block_end])
                block_start = block_end
                i = block_start

        return result

#         "5;hello3;foo"
#          012345678901
# 
# bstart  i   s[i]   length   sstart    bend  result
# 0       0   5       -        -        -     -   
# 0       1   ;       5        2        7     [hello]
# 7       7   7       
# 7       8   ;       3        9        12    [hello, foo]
# 12      12        

    def decode(self, s: str) -> List[str]:
        # - find delimiter
        # - parse length
        # - slice content
        # - repeat

        result = []
        start = 0
        while start < len(s):
            delim = s.find(DELIMITER, start)
            length = int(s[start:delim])
            content_start = delim + 1
            end = content_start + length
            result.append(s[content_start:end])
            start = end

        return result









































