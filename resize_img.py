from PIL import Image, ImageFilter
import os 

file_names = os.listdir('ECG.assets')
new_resized_list = []
new_resized_count = 0

with open('./resized_list.txt') as f:
	resized_img_names = [s.strip() for s in f.readlines()]
	# print(file_names)

	for n in file_names:
		# print(n)
		if n in resized_img_names:
			continue
		if n.endswith(('.png', '.jpeg', '.jpg')):
			print(n)
			image = Image.open("./ECG.assets/{}".format(n))
			resize_img = image.resize((int(image.width/2), int(image.height/2)), Image.LANCZOS)
			resize_img.save("./ECG.assets/{}".format(n))
			new_resized_list.append(n)
			new_resized_count += 1
 
with open('./resized_list.txt', mode="a") as f:
	f.write('\n')
	f.writelines('\n'.join(new_resized_list))
	print('resized {} files'.format(new_resized_count))