#coding: UTF-8

print """Hello!, Endou
How are you doing?
See you"""

print "5 + 3 * 4 = ", 5 + 3 * 4
print "(5 + 3) * 4 = ", (5 + 3) * 4
print "2 * ((5 + 3 * 2) * 4 - (4 + 5) / 3) = ",
print 2 * ((5 + 3 * 2) * 4 - (4 + 5) / 3)

identify = u"佐藤"
print u"識別子;" + identify

identify = "Katou"
print u"識別子;" + identify

identify = 204
print u"識別子:" + str(identify)

list = ["A", "B", "C", "D", "E"]
print u"対象リスト", list

print "[1:2]  ", list[1:2]
print "[1:-1] ", list[1:-1]
print "[1:]   ", list[1:]
print "[:2]   ", list[:2]
print "[:]    ", list[:]

tuple = ("A", "B", "C", "D")

print tuple[1:3]
print tuple[1:]
print tuple[:2]

dict = {"itou":64, "yamada":75, "endou":82}
print dict

print 'dict["yamada"] = 78'
dict["yamada"] = 78
print dict
