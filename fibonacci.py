#Generate an infinite fibonaaci series by using generator

def fibonacci():
  a,b = 0,1
  while True:
    yield a  ##yield is generator(keyword)
    a,b=b,a+b

f1 = fibonacci()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
