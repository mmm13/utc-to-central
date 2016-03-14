import sys
import getopt
import datetime
from dateutil import tz

def main(argv):
#hardcode timezones
	from_zone = tz.gettz('UTC')
	to_zone = tz.gettz('America/Chicago')

   #setting up variables
	in_date = ''
	in_time = ''

   #walk thru the arguments
	opts, args = getopt.getopt(sys.argv[1:],"hd:t:",["date=","time="])
	for opt, arg in opts:
		if opt == '-h':
			print "The time needs to be entered in the following format:"
			print " HH:MM:SS"
			print str(sys.argv[0]) + " -t HH:MM:SS \n"
			print "A date can be inculded using the -d or --date option"
			print str(sys.argv[0]) + " -t HH:MM:SS -d YYYY-MM-DD\n"
			sys.exit()
		elif opt in ("-d","--date"):
			in_date = arg
		elif opt in ("-t","--time"):
			in_time = arg


	#time is required
	if in_time == '':
		print "the time needs to be entered in the following formt:"
		print " HH:MM:SS"
		print str(sys.argv[0]) + " -t HH:MM:SS\n"
		sys.exit()

	#parse time
	hour, minute, second = in_time.split(":",4)

	#parse date
	now = datetime.datetime.now()
	if in_date == '':
		year = now.year
		month = now.month
		day = now.day
	else:
		year, month, day = in_date.split("-",4)

	NOW = str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
	print "UTC " + NOW

	utc = datetime.datetime.strptime(NOW, "%Y-%m-%d %H:%M:%S")

	#Tell the datetime object that it's in UTC time zone since
	# datetime objects are 'naive' by default
	utc = utc.replace(tzinfo=from_zone)

	#convert timezone
	local = utc.astimezone(to_zone)

	print "LOCAL " , local

if __name__ == '__main__':
   main(sys.argv)
