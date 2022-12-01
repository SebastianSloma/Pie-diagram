import matplotlib.pyplot as p

s = [35, 25, 20, 10, 10]
pie = ["apple pie", "strawberry pie", "banana cake",
       "blueberry pie", "raspberry pie"]
p.pie(s, labels=pie)
p.show()
