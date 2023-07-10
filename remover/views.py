from django.shortcuts import render
import cv2
from .models import WaterMarkRemove
from datetime import date
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create your views here.

#  photo = Image.open(self.image.path)
#         draw = ImageDraw.Draw(photo)
#         font = ImageFont.load_default()
#         width, height = photo.size
#         myword = "Hello world !"
#         margin = 10
#         textwidth, textheight = draw.textsize(myword, font)
#         x = width - textwidth - margin
#         y = height - textheight - margin
#         draw.text((x,y), myword, (255, 255, 255), font=font)
#         photo.save(self.image.path)

def home(request):
    print("home la wa")
    return render(request, "page/home.html")

def remove_img_background(request):
    return render(request, "page/removebg.html")

def addwatermark(request):
    if request.method == "POST":

        img = request.FILES["image"]
        word = request.POST["text"]

        print("img", img)

        # img = str(img)
        # watermark = WaterMarkRemove.objects.create(photo=img)
        # watermark.save()

        # today = date.today().strftime("%Y/%m/%d")
        # get_img = WaterMarkRemove.objects.filter(photo=f"photo/{today}/{img}").first().photo


        im = Image.open(img)
        width, height = im.size


        text = Image.new("RGBA", im.size, (255, 255, 255, 0))

        font = ImageFont.truetype("arial.ttf", 50)
        txt = ImageDraw.Draw(text)
        draw = ImageDraw.Draw(im)
        _, _, w, h, = txt.textbbox((0,0), word, font=font)
        
        draw.text(((width-w-10), (height-h-10)), word,(255,255,255), font=font, )
          
#         width 728
# height 410
# width-w 299
# height-h 67
        # # img = str(img)
        # #updating the image to db
        # WaterMarkRemove.objects.filter(photo=img).update(photo=im)
      
        return render(request, "page/watermark.html", context={"wimage":im})
    return render(request, "page/watermark.html")