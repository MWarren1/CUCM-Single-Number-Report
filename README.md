# CUCM-Single-Number-Report
###### Dependencies : Python 2.7
###### By Redemption.Man
a quick a dirty python script that take a cisco CDR file as input and creates a file of all the calls of a single phone number, including incoming or outgoing, duration start and end times

```
usage: Phone_Number_Reporter.py [-h] --input INPUT --phonenumber PHONENUMBER
optional arguments:
 -h, --help           		  show this help message and exit
 --input INPUT         		  CDR file input(must be csv)
 --phonenumber PHONENUMBER	  Phone number to report on(remember to add 9 if external number
```
