from google.colab import drive
drive.mount('/content/drive')

cd '/content/drive/My Drive/Colab Notebooks'

def wordCount(contents):
  d = {}
  for line in contents.split(', \'.|_|-|!'):
    line = line.lower() 
    words = line.split(" ")
    for word in words:
      if word.isnumeric():
        continue
      if word[-1] == '.' or word[-1] == ',' or word[-1] == '\'' or word[-1] == ')':
        word = word[:-1]
      if word[0] == '\'' or word[0] == '(':
        word = word[1:]
      if word in d: 
        d[word] = d[word] + 1
      else: 
        d[word] = 1
  return d

def topTenWords(d):
  s = sorted(d.items(), key=lambda x: x[1], reverse=True)
  count = 0
  for i in s:
    if count<10:
      print(i[0],"\t\t:\t", i[1])
      count += 1
    else:
      break
      
def readFile(path):
    with open(path, 'r') as f:
        return f.read()
      
path = "sample.txt"
contents = readFile(path)
d = wordCount(contents)
topTenWords(d) 
