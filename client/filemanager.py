with open("Incoming/MGodfrey.csv") as f:
	# content = f.readline()
	content = f.read()
	print content

f.close()

output =  open("Storage/output.csv", "w+")
# output =  open("Storage/output.csv", "a+") "a+" for appending the file, not overwriting.
output.write(content)

output.close()

