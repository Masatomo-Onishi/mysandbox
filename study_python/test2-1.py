#coding: utf-8

#import sys
#print sys.stdin.encoding
#print sys.stdout.encoding
#print sys.stderr.encoding

print "Hello!\nByeBye"
print "Tomato is \"very\" delicious"
print "The browser displays an \
error message"

print "10 + 8    = ", 10 + 8
print "10 + 8.0  = ", 10 + 8.0
print "10 / 3    = ", 10 / 3
print "10 / 3.0  = ", 10 / 3.0
print "10.0 / 3  = ", 10.0 / 3
print "17 / 5    = ", 17 / 5
print "-17 / 5   = ", -17 / 5
print "10.0 // 3 = ", 10.0 // 3
print "10 // 3   = ", 10 // 3
print "10 % 3    = ", 10 % 3
print "5 ** 3    = ", 5 ** 3

name = u"佐藤"
old = 31
code_no = 115
cityName = u"札幌市"

print u"名前;" + name
print u"年齢:" + str(old)
print u"識別番号:" + str(code_no)
print u"出身地:" + cityName

print "Start"
x = 0
y = 1

if x == 0:
  print "x is 0"

  if y == 0:
    print "y is 0"

  if y != 0:
    print "y is not 0"
print "End"

plist = [u"山田", u"太郎", 12, 31, u"男性"]

print u"氏名: " + plist[0] + plist[1]
print u"生年月日: " + str(plist[2]) + "/" + str(plist[3])
print u"性別: " + plist[4]

tuple = ("A", "B", "C", "D")

print tuple[0]
print tuple[1]
print tuple[2]
print tuple[3]

dict = {"itou":64, "yamada":75, "endou":82}
print dict["itou"]
print dict["yamada"]
print dict["endou"]

num = 0

print u"繰り返し開始"

while num < 2:
  print "num = " + str(num)
  num += 1
else:
  print u"繰り返しが終了した時の最後の値", 
  print "num = " + str(num)

print u"繰り返し終了"
