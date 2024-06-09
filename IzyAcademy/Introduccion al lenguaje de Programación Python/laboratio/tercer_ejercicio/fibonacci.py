
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

def fibonnaci(num):    
    fibo = [0,1]

    for x in range(num):
        fibo.append(fibo[-2] + fibo[-1])
    
    return fibo;
        

print(fibonnaci(10))