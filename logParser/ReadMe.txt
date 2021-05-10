Here is the detail description to use the tool:
1. Created a package called logParser. access.log kept inside the "logs" folder.
2. All .py files are inside "logParser" package.

Module and wrapper used for this assignment:
Module: re and collections
Wrapper: lars.apache

How to run the program:
1. To get Top 10 requested pages and the number of requests made for each:
      --- Created "top10Pages.py" where in "counter.most_common(10)" we need to provide the no of count we want.
	  --- We can run this program using pyCharm to command line using "python top10Pages.py"
	 
2. To get Top 10 unsuccessful page requests:
      --- Created "top10Unsuccessful.py" where in "counter.most_common(10)" we need to provide the no of count we want.
	  --- We can run this program using pyCharm to command line using "python top10Unsuccessful.py"
	  
3. To get The top 10 hosts making the most requests, displaying the IP address and number of requests made
      --- Create "IPAddress_WithNoOfRequests.py". This program will create a CSV file inside "logParser -> logs" with IP address and NoOfRequest. Here I have taken all the IP address, which are listing in access.log file.
	  --- Created CSV file name is "ipAddress.csv"
	  
4. To get Percentage of successful requests.
      --- Created "successful_Req.py". Here we will get the count of Status code-200 and 300. 
	  
5. To get Percentage of unsuccessful requests.
      --- Here I have not created a separate program. For this we can extend "top10Unsuccessful.py" to get the percentage.
	  
	  
Note: I have created a POC for the assignment that I got. I have tried my best to parse the access.log to get the results. As POC is created, it's just how simplest way to combine the code and create a tool. Such as we can create a base class to open the access.log and create a function to perform the actions.
This is a complete new learning for me.

