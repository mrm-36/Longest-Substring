def longuest_substring(st):
    subs = [] # Where we will store our substrings
    curr_sub = str() #The current substring
    if (len(st) <= 1) return st;
    for c in range(len(st) - 1):
        tempsub = st[c] + st[c + 1] #Temporary String
        sortedsub = str() # Sorted Version of the Temporary String
        for x in sorted(tempsub): sortedsub += x # Building the Sorted version
        if tempsub == sortedsub: # If the string is in alphabetical order
            curr_sub += st[c] # Add the current character to the current substring
            if c == len(st) - 2: # If we are at the before last character, we add it to the substring
                curr_sub += st[c + 1]
                if len(curr_sub) > 1: # Add the current substring to the possiblities 
                    subs.append(curr_sub)
                curr_sub = '' # Clear the current substring
        else: #If the Temporary String is not in alphabetical order
            curr_sub += st[c] # Add the current character to the current substring
            # Notice that here we don't add the next character
            if len(curr_sub) > 1: # Add the current substring to the possiblities 
                subs.append(curr_sub)
            curr_sub = '' # Clear the current substring
    return max(subs, key = len) # Return the string with maximum length out of all the possibilities

st = input()
print(longuest_substring(st))    
