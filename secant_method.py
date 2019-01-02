import math
def f(x):
   return (1/2) + math.sin(x) - math.cos(x)

error = math.pow(10, -6)
x0 = 0
x1 = 1
converged = False

count = 1
while count <= 10:
    x2 = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))

    print(f'Iteration: {count}')
    print(f'x0 = {x0}')
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
    print(f'f(x0) = {f(x0)}')
    print(f'f(x1) = {f(x1)}')
    print(f'f(x2) = {f(x2)}')

    if(abs(f(x2)) < error):
        converged = True
        print("converged!")
        break
    
    x0 = x1
    x1 = x2
    count += 1

if converged is False:
    print("did not converge!")