#This code assume the current naming convention of files which is:
	#[1,1a,2,2a,3,3a,........,100,100a].

#Let's start ;)
import os,os.path
import random

from PIL import Image,ImageDraw, ImageFont
#This is a function returns a list of all images names
#Args:DIR (directory which holds the images) rtype:lst, containing strings of files name.
def images_list(DIR):
	return list([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR,name))])

#This function choose a random image from the directory.
#Args:images (lst of file names), rtype:string (str file name)
def random_image(images):
	if(images==[]):
		return ''
	return random.choice(images)
#Test:
#print(random_image(images))
#print(f'{DIR}/{random_image(images)}')

def write_centre(image,text):
	draw=ImageDraw.Draw(image)
	draw.text(xy=(450,325),text=text,fill=(255,69,0),font=font_type2)
def write_line(image,text,x,y):
	draw=ImageDraw.Draw(image)
	draw.text(xy=(x,y),text=text,fill=(255,69,0),font=font_type)
	draw.text(xy=(x,y+35),text=" ",fill=(255,69,0),font=font_type)
	draw.text(xy=(x,y+35),text=" ",fill=(255,69,0),font=font_type)


#Args:text/tweet , rtype:lst[imageObject,filenam(str)]
def write_on_image(text):
	file=random_image(images)
	image = Image.open(f'{DIR}/{file}')
	i=0
	x,y=215,325
	if(len(text)>286):
		return [image,file]
	elif(len(text)<75):
		write_centre(image,text)
	else:
		divisions=len(text)//35
		remainder=len(text)-divisions*35
		for i in range(divisions+1):
			write_line(image,text[:35],x,y)
			text=text.replace(text[:35]," ")
			y+=35
	
	return [image,file]

#Now we have an aray contain an image object returned so we can pass it into a function to tweet or to save locally with
#the returned file name arr[1]

#Driver program to test all above functions:

DIR='img_bg'
images=images_list(DIR)


image = Image.open(f'{DIR}/{random_image(images)}')
font_type=ImageFont.truetype('arial.ttf',40)
font_type2=ImageFont.truetype('arial.ttf',40*2)

#text="Finish what you start my bro its a sample u can use it anytime bro, this is from a git repository  and i dont know i can solve that issue or not because it's difficult and case sensetive brother baby my life is  not that easy i sware the repository id is one ot two i can not rela."
text="Remain valley who mrs uneasy remove wooded him you. Her questions favourite him concealed. We to wife face took he. The taste begin early old why since dried can first. Prepared as or humoured formerly. Evil mrs true get post. Express village evening prudent my as ye hundred forming."
text_short="Hello,its me"


new_image=write_on_image(text)
new_image2=write_on_image(text_short)
new_image2[0].save(f'post_{new_image2[1]}')
new_image[0].save(f'post_short_{new_image[1]}')

new_image[0].show()
new_image2[0].show()
