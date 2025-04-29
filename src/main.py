import re
import os
import shutil
from textnode import *
from htmlnode import HTMLNode, LeafNode, ParentNode
from blocks import *

def main():
    static_to_public('./static')

def static_to_public(static_path, public_path='./public'):
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)

    def copy_dir(src_path, dest_path):
        os.makedirs(dest_path, exist_ok=True)
        for item in os.listdir(src_path):
            src_item = os.path.join(src_path, item)
            dest_item = os.path.join(dest_path, item)

            if os.path.isfile(src_item):
                shutil.copy2(src_item, dest_item)
            elif os.path.isdir(src_item):
                copy_dir(src_item, dest_item)
    
    copy_dir(static_path, public_path)
        

if __name__ == "__main__":
    main()
