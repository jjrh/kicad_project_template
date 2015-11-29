#!/usr/bin/python
import pystache
from os import listdir

renderer = pystache.Renderer()

images = listdir("images")


template ="#+CAPTION:{{caption}}\n#+NAME:{{name}}\n#+attr_html: :width 800px\n[[{{img_location}}]]"

for img in images:
    print renderer.render(template,{'name':img,'img_location':"./images/"+img})
    print ""
