def my_steps(n): 
  if  not isinstance(n, int) or n < 1 or n > 25:
    raise ValueError("n must be an integer between 1 and 25")

if n == 1: 
  return 1
if n == 2: 
  return 2

prev2 =1
prev1=2

for i  in range(3, n +1):
  current = prev1 + prev2
  prev2 = prev1
  prev1 = current  

return prev1 
