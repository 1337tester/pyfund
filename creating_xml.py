__author__ = 'e1063127'
import xml.etree.ElementTree as etree
import datetime, time

tree = etree.parse('c:\Testing/test_files/aaa.xml')
root = tree.getroot()
print (root)
print (tree.findall('{http://www.w3.org/2005/Atom}end'))
cifra = tree.find('.//{http://www.w3.org/2005/Atom}cifra')


cifra.text = t = time.time()


tree.write('c:\Testing/test_files/bbb.xml')


"""fi = open('c:\Testing/test_files/aaa.xml', 'r')
fo = open('c:\Testing/test_files/bbb.xml', "w")
lines = fi.readlines()
fo.writelines(lines)

fi.close()
fo.close()"""

