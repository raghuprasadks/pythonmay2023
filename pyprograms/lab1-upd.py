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
        k.strip()
        if(len(k)>0):
            counter = 1
            if k in freqdict.keys():
                counter=freqdict[k]+1
        freqdict[k]=counter
    print("dictionary ",freqdict)

#frequency('mavaaavmbxb')
frequency('We ARE Penn State!!!')
#frequency('One who IS being Trained')

'''
def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {1: ['one', 'uno'], 2: ['two', 'dos'], 3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'})
        {'Sara': '123-456-78', 'Alex': ['987-12-585', '00000'], 'sara': '258715'}
    """
    # - YOUR CODE STARTS HERE -
    #pass
    swapdictionary={}

    for k,v in d.items():
        #print("key =",k,"value : =",v)

        if v in swapdictionary.keys():
            if (type(swapdictionary[v])!=list):
                lst =[swapdictionary[v]]
                #val = swapdictionary[v]
                lst.append(k)
                swapdictionary[v] = lst
            else:
                swapdictionary[v] =swapdictionary[v].append(k)
        else:
            swapdictionary[v]=k

    print("swapped dictionary ",swapdictionary)

#invert({'one':1, 'two':2,  'three':3, 'four':4})
#invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
#invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'})

def employee_update(d, bonus, year):

    """
        >>> records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
        >>> employee_update(records,7500,2022)
        {2020: {'John': ['Managing Director', 'Full-time', 65000], 'Sally': ['HR Director', 'Full-time', 60000], 'Max': ['Sales Associate', 'Part-time', 20000]}, 2021: {'John': ['Managing Director', 'Full-time', 70000], 'Sally': ['HR Director', 'Full-time', 65000], 'Max': ['Sales Associate', 'Part-time', 25000]}, 2022: {'John': ['Managing Director', 'Full-time', 77500], 'Sally': ['HR Director', 'Full-time', 72500], 'Max': ['Sales Associate', 'Part-time', 32500]}}
    """
    # - YOUR CODE STARTS HERE -
    #pass
    for k,v in d.items():
        if(k==year-1):
            #empdict=v
            d[year] = v
            '''
            for empk,empv in v.items():
                empv[2]=empv[2]+bonus
            '''
            break
    for k,v in d.items():
        updsaldict={}
        if (k==year):
            updsaldict=v
            for empk,empv in updsaldict.items():
                empv[2]=empv[2]+bonus
    print(d)
records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
employee_update(records,7500,2022)
'''