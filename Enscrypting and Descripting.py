import random 


def random_string():
  a = ("a", "b", "c", "d", "e", "f", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@" "#", "$", "%", "^", "&", "*", ")", "(", "-", "_", "+", "=", ",", "<", ">", "/", "?", ".", ";", ":", "'", "[", "]", "{", "}", "~", "`")

  # Select 6 random elements
  random_elements = random.sample(a, 15)

  # Join the elements into a single string
  reasult = "".join(random_elements)
  return reasult
st = input("Enter message : ")

r1 = random_string()
r2 = random_string()

words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding : ")
coding = True if (coding=="1") else False
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      stnew = r1+ word[1:] + word[0] + r2
      nwords.append(stnew)
    else:
      # if less then 3 letters, it simply reverse's it
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[15:-15]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
