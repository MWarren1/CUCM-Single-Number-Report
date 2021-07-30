################################
##   Single Number Reporter   ##
##            v1.0            ##
##        Python 2.7          ##
##     By Redemption.Man      ##
################################

##################################################################################################
## The Script parses a CDR file and an creates a csv file with all calls made and				##
## received by a single number, also includes calls that may have been forwarded				##
## on to that number.																			##
##																								##
## usage: Phone_Number_Reporter.py [-h] --input INPUT --phonenumber PHONENUMBER					##
## optional arguments:																			##
##   -h, --help           		show this help message and exit									##
##   --input INPUT         		CDR file input(must be csv)										##
##   --phonenumber PHONENUMBER	Phone number to report on(remember to add 9 if external number	##
##################################################################################################

import csv
import argparse
import os.path
import time
import sys

## CLI switches
parser = argparse.ArgumentParser(prog='Phone_Number_Reporter.py', description='Reads Cisco CDR files and creates a simplfied call record for a single number')
parser.add_argument('--input', required=True, help='CDR file input(must be csv)')
parser.add_argument('--phonenumber', required=True, help='Phone number to report on(remember to add 9 if external number')

args = parser.parse_args()

## END of CLI switches

## Var's that can be changed
outputfile = "Call_Report_"+args.phonenumber+".csv"

## arg.input is the input file
phonenumber = args.phonenumber

#create parsed output cvs 
parsedoutput = open(outputfile, 'w+')
parsedoutput.write("Incoming/Outgoing,Start of Call,End of Call,Duration,Caller Number,Called Number,Call Answered By\n")

## columns needed:
## starting at zero
## 2 - globalCallID_callId
## 4 - dateTimeOrigination
## 8 - callingPartyNumber
## 47 - dateTimeConnect
## 48 - dateTimeDisconnect
## 55 - Duration
## 30 - finalCalledPartyNumber
## 31 - finalCalledPartyUnicodeLoginUserID
## 101 - huntPilotDN
#### Opens and parses cdr extracting only records with the gateway
duration = 0
calldirection = "Imcoming"
totalcalls = 0

with open(args.input, 'Ur') as f:
	print "Collecting all records for " + phonenumber + "\n\n"
	parserreader = csv.reader(f)
	for row in parserreader:
		callmatch = 0
		# caller number
		if row[8] == phonenumber:
			calldirection = "Outgoing"
			callmatch = 1
		# called number
		if row[30] == phonenumber:
			calldirection = "Incoming"
			callmatch = 1
		# final answered number
		if row[31] == phonenumber:
			calldirection = "Incoming"
			callmatch = 1
		
		if callmatch == 1:
			totalcalls = totalcalls + 1
			callmatch = 0
			convertstarttime = time.localtime(float(row[4]))
			convertendtime = time.localtime(float(row[48]))
			startofcall = str(convertstarttime.tm_year)+"/"+str(convertstarttime.tm_mon)+"/"+str(convertstarttime.tm_mday)+" "+str(convertstarttime.tm_hour) +":"+ str(convertstarttime.tm_min)
			endofcall = str(convertendtime.tm_year)+"/"+str(convertendtime.tm_mon)+"/"+str(convertendtime.tm_mday)+" "+str((convertendtime.tm_hour)) +":"+ str(convertendtime.tm_min)
			
			parsedoutput.write(calldirection+","+startofcall+","+endofcall+","+row[55]+","+row[8]+","+row[29]+","+row[30]+"\n")

parsedoutput.close()
f.close() 
if totalcalls == 0:
	sys.exit("***ERROR*** No calls found for phone number "+huntgroup)
else:
	print "Total calls for "+phonenumber+" : "+str(totalcalls)
