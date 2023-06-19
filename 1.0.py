""" def strcounter(s): # O(M*N)
    for sym in set(s):
        counter = 0
        for sud_sym in s:
            if sym == sud_sym:
                counter += 1
        print(sym, counter)        

strcounter('pcprt')
print(' ')
strcounter('abcaa')
# r 1
# c 1
# t 1
# p 2
   
# a 3
# c 1
# b 1

def strcounter(s): # O(N**2)
    for sym in set(s):
        counter = 0
        for sud_sym in s:
            if sym == sud_sym:
                counter += 1
        print(sym, counter)     """
       
def strcounter(s): # O(N)
    syms_counter = {}
    for sym in set(s):
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)   
        
strcounter("aaabbbbccd")
strcounter("bpvtytybz")     