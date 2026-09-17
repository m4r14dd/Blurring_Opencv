"""
This file is for getting the url of the image I want and saving it on the directory

:)
"""
import requests
url = "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQzhYnPG_6Vdsp9cVnSVbzem9UDBaPXu0n4M_LGqf-odMJNGcer"
img = requests.get(url)

with open("imagem.jpg", "wb") as f:
    f.write(img.content)
