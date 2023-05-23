def frequency(txt):
    '''
        >>> frequency('mama')
        {'m': 2, 'a': 2}
        >>> answer = frequency('We ARE Penn State!!!')
        >>> answer
        {'w': 1, 'e': 4, 'a': 2, 'r': 1, 'p': 1, 'n': 2, 's': 1, 't': 2}
        >>> frequency('One who IS being Trained')
        {'o': 2, 'n': 3, 'e': 3, 'w': 1, 'h': 1, 'i': 3, 's': 1, 'b': 1, 'g': 1, 't': 1, 'r': 1, 'a': 1, 'd': 1}
    '''
    # - YOUR CODE STARTS HERE -mava
    # freqdict={m:1,a:2,v:1}
    freqdict={}
    for k in txt.lower():
        if(len(k.strip())>0):
            counter = 1
            if k in freqdict.keys():
                counter=freqdict[k]+1
            freqdict[k]=counter
    print("dictionary ",freqdict)

#frequency('mavaaavmbxb')
#frequency('We ARE Penn State!!!')
frequency('One who IS being Trained')
