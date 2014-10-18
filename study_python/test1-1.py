#coding: UTF-8

print "Hello!", "Satou",
print "ByeBye"

print 'One', 'Two', "Three"
print "Four"

print 10
print 3.14e8
print 1.27e-3
print 075
print 0x4F
print 3+4j

msg = "Hello"
print msg

sum = 10 + 45
print sum

amari = 10 % 3

if amari != 0:
  print u"割り切れませんでした"
  print u"余りは", str(amari), u"です"

print "True = ", True
print "False = ", False

print "True + 3 = ", True + 3

if True:
  print "Always True"

print (10)
print (10,)
print ("JP")
print ("JP",)

t = "A", "B"
print t

num = 0

print u"繰り返し開始"

while num < 5:
  print "num = " + str(num)
  num += 1

print u"繰り返し終了"
