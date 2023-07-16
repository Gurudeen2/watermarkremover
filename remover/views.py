from django.shortcuts import render
from .models import WaterMarkRemove, RemoveBackground
from PIL import Image, ImageDraw, ImageFont
import os
from django.core.files import File
from rembg import remove

# Create your views here.




def home(request):
    # for file in os.listdir("media/photo"):
    #     file_path = os.path.join("media/photo", file)
    #     if os.path.isfile(file_path):
    #         os.remove(file_path)
    
    # if WaterMarkRemove.objects.exists():
    #     WaterMarkRemove.objects.all().delete()
    # if RemoveBackground.objects.exists():
    #     RemoveBackground.objects.all().delete()
    return render(request, "page/home.html")

def remove_img_background(request):
    if request.method == "POST":
        img = request.FILES['removeimg']

        filename = str(img).split(".")
        img_path = Image.open(img)


        img_path.save("media/photo/"+filename[0]+"."+img_path.format)
        
        
        output = Image.open(f'media/photo/{filename[0]}.{img_path.format}')
        imgregb = remove(output)
        # # removedbg = open(img_path, "rb")
        imgregb = imgregb.convert("RGB")
        imgregb.save(f'media/photo/{filename[0]}.{img_path.format}')
        l_img = open(f'media/photo/{filename[0]}.{img_path.format}', "rb")
        convert_img_to_file = File(l_img)
        
        # save image to database
        remove_db = RemoveBackground.objects.create()
        remove_db.photo.save(filename[0]+"."+img_path.format,convert_img_to_file)


        return render(request, "page/removebg.html", {"removebg":RemoveBackground.objects.all().first().photo})
    return render(request, "page/removebg.html")

def addwatermark(request):
    if request.method == "POST":

        img = request.FILES["image"]
        word = request.POST["text"]


        watermark = WaterMarkRemove.objects.create()
       

# add text to image
        filename = str(img).split(".")
        im = Image.open(img)
        
        width, height = im.size


        text = Image.new("RGBA", im.size, (255, 255, 255, 0))

        font = ImageFont.truetype("arial.ttf", 50)
        txt = ImageDraw.Draw(text)
        draw = ImageDraw.Draw(im)
        _, _, w, h, = txt.textbbox((0,0), word, font=font)
        
        draw.text(((width-w-10), (height-h-10)), word,(255,255,255), font=font)

        im.save("media/photo/"+filename[0]+"."+im.format)
        l_img = open(f'media/photo/{filename[0]}.{im.format}', "rb")
        convert_img_to_file = File(l_img)
        watermark.photo.save(filename[0]+"."+im.format, convert_img_to_file)
      
        return render(request, "page/watermark.html", context={"wimage":WaterMarkRemove.objects.all().first().photo})
    return render(request, "page/watermark.html")