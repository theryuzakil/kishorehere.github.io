def knapsack_function(val,wt,cap):
    index=list(range(len(val)))
    ratio = [v/w for v,w in zip(val,wt)]
    index.sort(key=lambda i: ratio[i], reverse=True) 
    max_value=0
    fract=[0]*len(val)
    for i in index:
        if wt[i]<=cap:
            fract[i]=1
            max_value +=wt[i]
        else:
            fract[i]=cap/wt[i]
            max_value += val[i]*cap/wt[i]
            break
    return max_value,fract

n=int(input('enter no. of elements'))
val=input('enter the values of the elements in order: '
          .format(n)).split()
val=[int(v) for v in val]
wt=input('enter the weights of elements in order:'
         .format(n)).split()
wt=[int(w) for w in wt]
cap=int(input('enter max weight: ' ))
max_value, fract = knapsack_function(val,wt,cap)
print('max value of elements=', max_value)
print('fractions of elemnts taken=', fract)
    
