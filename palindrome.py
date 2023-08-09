# s ="hiHellolleHih"
# if s == s[::-1]:  #s[start:stop:step]
#     print("Yes Palindrome")
# else:
#     print("No")

#Alternative way
s = "hiHellolleHih"
n = len(s)
x = 0
for i in range(n):
    if s[i] != s[n-i-1]:
      x = 1
      break

if x == 0:
   print("Yes Palindrome")
else:
   print("No")