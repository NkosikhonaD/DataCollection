import os
import shutil


digits_list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
path = "C:\\Users\\DlaminiN3\Downloads\\data_points\\training_3"
dest_path ="C:\\Users\\DlaminiN3\Downloads\\final_data\\training_"
writer_list = os.listdir(path)
for writer in writer_list:
	writer_source=path+"\\"+writer
	character_list = os.listdir(writer_source)
	print(writer_source)
	for character_file in character_list:
		lastl = character_file[-1:].lower()
		if character_file[9:] in digits_list:
			lastl = digits_list.index(character_file[9:])
			lastl=str(lastl)
		dest = dest_path+lastl+"\\"+writer
		shutil.move(writer_source+"\\"+character_file,dest)
