def longuest_substring(st):
    subs = [] # Where we will store our substrings
    curr_sub = str() #The current substring
    if len(st) > 1:
        for c in range(len(st) - 1):
            tempsub = st[c] + st[c+1]
            #Temporary string
            # sort the temporary sub
            sortedsub = str()
            for x in sorted(tempsub): sortedsub += x
            if tempsub == sortedsub:
                curr_sub += st[c]
                if c == len(st) - 2:
                    curr_sub += st[c+1]
                    if len(curr_sub) > 1:
                        subs.append(curr_sub)
                    curr_sub = ''
            else:
                curr_sub += st[c]
                if len(curr_sub) > 1:
                    subs.append(curr_sub)
                curr_sub = ''
        return max(subs, key = len)
    else:
        return st

st = input()
print(longuest_substring(st))    