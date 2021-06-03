name_1=["Ann", "Britt", "Chris","Dave"]
name_2=["Ed", "Frank", "Grant"]
name_3=[]
def likes(names):
    return({0: 'no one likes this',
           1: '{} likes this',
           2: '{} and {} like this',
           3: '{}, {} and {} like this',
           4: '{}, {}, and {others} others like this'}[min(4,len(names))].format(*names[:3], others=len(names)-2))
    
    pass
likes(name_3)
likes(name_2)
likes(name_1)