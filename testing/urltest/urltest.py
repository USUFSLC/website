import sys
import argparse
import pycurl


try:
	if len(sys.argv) < 3:
		print("Input invalid\nurltext.py <url> <list.txt>")
		sys.exit(0)
	else:
		website = sys.argv[1]
		filename = sys.argv[2]
except:
	sys.exit(0)

# filename = input("String list: ")
# website = input("Website: ")

print("Running check...\nFYI, this ignores all lines that begin with \"#\".\n")

try:
	file = open(filename,"r")
except:
	print("Unable to open file: ", filename)
	sys.exit(0)

c = pycurl.Curl();
c.setopt(pycurl.WRITEFUNCTION, lambda x: None)

try:
	c.setopt(c.URL, website)
except:
	print("Couldn't connect to: ", website)
	sys.exit(0)


for line in file:
	if line[0] == "#":
		url = line[:-2]
		c.setopt(c.URL, website + url)
		
		try:
			c.perform()
		except:
			print("Failed to execute with path: ", website + url)

file.close()

print("Check completed.")
