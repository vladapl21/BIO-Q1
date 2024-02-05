# question 1a
def integers(n, i):
  string = ""
  for x in range(int(n), int(n+i)):
    string += str(x)
  print(n, i)
  print(int(string[i-1]))
  #print(len(string))


#integers(999, 11)
n = int(input())
i = int(input())
integers(n, i)