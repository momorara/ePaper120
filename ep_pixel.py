#!/usr/bin/python

import ep_lib
import random

def main():

    print("画面を初期化して、白くする。")
    draw,image = ep_lib.image_set()
    ep_lib.clear_w(draw)

    draw.text((0, 0),"test random 3000 pixels", font=ep_lib.font_set("gos",24) ,fill=0)
    draw.rectangle((0, 30, 291, 119), outline="black", fill="white")

    for i in range(3000):
        x = random.randint(0, 292)
        y = random.randint(30, 119)
        draw.point((x, y), fill="black")

    # ep_lib.write_buffer()
    ep_lib.ep_draw(0,0,image,0,1)
    
    # SPI を終了（リソースを解放）
    ep_lib.close()

if __name__ == '__main__':
    main()
