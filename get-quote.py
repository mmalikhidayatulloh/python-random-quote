import random
last = 13
rnd = random.randint(0, last)
def main():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #print(quotes[0])
  print(quotes[14])
  print(quotes[0])

if __name__== "__main__":
  main()
