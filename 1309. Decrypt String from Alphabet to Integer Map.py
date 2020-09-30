def freqAlphabets(s):
    char_map = "abcdefghijklmnopqrstuvwxyz"
    stack = []
    for index, val in enumerate(s):
        if stack and val == '#':
            a, b = stack.pop(), stack.pop()
            stack.append(b+a)
        else:
            stack.append(val)
    res = ""
    for i in stack:
        res += char_map[int(i)-1]
    return res
if __name__ == "__main__":
    s = "10#11#12"
    ret = freqAlphabets(s)