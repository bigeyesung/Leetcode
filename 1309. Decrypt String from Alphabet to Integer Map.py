import re
def freqAlphabets(s: str) -> str:
    # create a mapping dic
    # loop to go through digits (while-loop)
    #   if each two digit has hashtag-> map 2
    #   else: map 1 digit
    return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))