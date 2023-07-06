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

def removewatermark(request):
    if request.method == "POST":

        img = request.FILES["image"]
        # img = str(img)
        # watermark = WaterMarkRemove.objects.create(photo=img)
        # watermark.save()

        today = date.today().strftime("%Y/%m/%d")
        # get_img = WaterMarkRemove.objects.filter(photo=f"photo/{today}/{img}").first().photo
        get_img = WaterMarkRemove.objects.filter(photo=f"photo/2023/07/04/{img}").first().photo
        get_img2 = Image.open(get_img.path)
        # print(get_img2)

        im = Image.open(get_img.path)
        width, height = im.size
        text = Image.new("RGBA", im.size, (255, 255, 255, 0))

        font = ImageFont.truetype("arial.ttf", 60)
        txt = ImageDraw.Draw(text)
        draw = ImageDraw.Draw(im)
        _, _, w, h, = txt.textbbox((0,0), "Akeem Tolani", font=font)
        draw.text(((width-w)/2, (height-h)/2), "Akeem Tolani",(255,255,255), font=font, )
            # Combine the image with text watermark
        # out = Image.alpha_composite(draw, txt)
        im.show()
        
      
        im.save("ak.png")

      
    return render(request, "page/home.html")