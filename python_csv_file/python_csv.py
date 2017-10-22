
#CSV stands for comma separated value, 
#Values can be comma separated, dash separated or other delimiter
#For working with csv file python has built in module called csv 
#We can work with file module but csv is more efficient
#We will oepn and close the csv file with with open() context manager
#It takes two args one--> file name, Two-->file open mode

import csv

with open('test_file.csv','r') as csv_context:
	#csv.reader() method is use to read from csv
	#reader() method returns csv_content as a iteratable object
	#expected at least 1 arguments	others are optional
	#2nd arg is delimiter coma,dash or other as you want (see the writing part of the csv)
	csv_reader=csv.reader(csv_context) 
	# csv_reader=csv.reader(csv_context,delimiter='\t') 
	# csv_reader is iteratable
	print csv_reader 
	#If we get iterate we will get the each content line as list formate
	#So we can print the content of each list using index
	# for content in csv_reader:
	# 	print content
	# 	print content[0]

	#for writing into csv file we should open it as a write mode
	#Use writer() method to get obejct (This object is not iteratable)
	#Than use writerow() method to write into the new csv file as each line
	with open('test_file_2.csv','w') as csv_context_w:

		#writer() metho open up csv writer using given delimiter
		#Common delimiter are , ,-, tab,
		#By default its coma if no delimiter is passed
		#In python \t is used as tab
		# csv_writer=csv.writer(csv_context_w,delimiter='-')
		#If we want to read from other delimiter csv file rather than coma we must pass the delimiter
		#If we don't there will be no error but we won't get the actuall content 
		csv_writer=csv.writer(csv_context_w,delimiter='\t')
		for content in csv_reader:
			csv_writer.writerow(content)

#---------------Csv reading and writing using dictionary reader and writer--------------

#for dictionary reader we use DictReader() and DictWriter()	
#DictReader() return each line as single dictionary
#First values are covered as key 
#There might be little difference
#We can now acces values as key of dict 
#For dict writing we can specify field names as a frist line as header
#DictWriter() takes exactly three param
#And we use writeheader() method
#We can also del a field name from writing 
#Remove the field name from field list and use del inside the loop

with open('test_file.csv','r') as csv_context:

	csv_dict_reader=csv.DictReader(csv_context)	

	with open ('test_file_dict','w') as csv_context_w:
		fieldnames=['Appliances','Binders and Binder Accessories','Telephones and Communication','Appliances', 'Office Furnishings','Binders and Binder Accessories','Storage & Organization','Storage & Organization','Paper']
		csv_dict_writer=csv.DictWriter(csv_context_w,fieldnames=fieldnames,delimiter=',')
		csv_dict_writer.writeheader()

		for line in csv_dict_reader:
			# del line['Storage & Organization']
			csv_dict_writer.writerow(line)	


