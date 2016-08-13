import urllib,re
import lxml.html
contact = urllib.urlopen("https://www.docnme.com/contact-us/")
c = contact.read()
##printing the conatct email id:-
print "Mail ids"
print re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",c)
print "Phone numbers" 
print re.findall(r"\+\(\d{3}\)\s*\d{3}[-\.\s]\d{2}|\d{4}[-\.\s]\d{4}",c)