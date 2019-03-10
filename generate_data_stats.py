import os

path = "C:\\Users\\DlaminiN3\\Downloads\\final_data"
list_char_folders = os.listdir(path)

for training in list_char_folders:
	minimum=200000
	maximum =0
	total_for_char =0
	author_path = path+"\\"+training
	list_in_training = os.listdir(author_path)
	locate_mini = ""
	locate_max = ""
	
	for datapoints in list_in_training:
		list_data_path = os.listdir(author_path+"\\"+datapoints)
		total_for_char+=len(list_data_path)
		if len(list_data_path)>maximum:
			maximum = len(list_data_path)
			locate_max=author_path+"\\"+datapoints
			
		if len(list_data_path)<minimum:
			minimum = len(list_data_path)
			locate_mini =author_path+"\\"+datapoints
	print("Total Chars "+training+" "),print(str(total_for_char))
	print("Maximum Chars "+ str(maximum)), print("Minimum Chars "+str(minimum) +" loc:"+locate_mini)
	print("\n============================\n")

