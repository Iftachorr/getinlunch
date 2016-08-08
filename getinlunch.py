__author__ = 'iftachorr'

import json
from pprint import pprint
import datetime
import requests
import sys, getopt

def send_email(frm, to, subject, text):
    pass

def main(argv):
   inputfile = 'people.json'
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
   except getopt.GetoptError:
      pprint('getinlunch.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'getinlunch.py -i <inputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
   print 'Input file is "', inputfile
   getinlunch(inputfile)

def getinlunch(inputfile):
    try:
        with open(inputfile) as data_file:
            data = json.load(data_file)
        people = data["people"]

        size = 5
        while (len(people) % size) != 0 and size > 3: #Damn you prime numbers, I need to find a solution so no one will go to lunch alone :(
            size = size - 1

        groups = zip(*[iter(people)]*size)

        for group in groups:
            to = []
            text = "Hi Everone,\n\n Your random bunch for today's Getting in Lunch is:\n"
            for person in group:
                text = text+ " ".join([person["firstname"], person["surname"]])+ "\n"
                to.append(" ".join([person["firstname"],person["surname"],"<"+person["email"]+">"]))

            subject = "Get in Lunch "+(datetime.datetime.today().strftime("%a %b %y"))
            frm = "Get in Lunch <invite@getinlunch.com>"
            pprint("*************")
            pprint("*************")
            pprint("*************")
            pprint(to)
            pprint(frm)
            pprint(subject)
            pprint(text)
            send_email(frm, to,subject ,text)
    except Exception as e:
        print "Unexpected error:" + str(sys.exc_info()[0]) + " " + str(e)
        sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])
