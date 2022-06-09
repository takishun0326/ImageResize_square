import os 
from PIL import Image

# 画像の中心を切り出し
def CropCenter(img, target_width, target_height):
    return img.crop(((img.width - target_width) // 2,
     (img.height - target_height) // 2,
     (img.width + target_width) // 2,
     (img.height + target_height) // 2))


# 最大サイズの正方形切り出し
def CropMaxSquare(img):
    return CropCenter(img, min(img.size), min(img.size))

# アスペクト比維持リサイズ
def KeepAspectImg(img, target_width, target_height):
    x_ratio = target_width / img.width
    y_ratio = target_height / img.height

    if x_ratio < y_ratio:
        resize_size = (target_width, round(img.height * x_ratio))
    else :
        resize_size = (round(img.width * y_ratio), target_height)
        

    resized_img = img.resize(resize_size)
    
    return resized_img


# 正方形切り出しの画像リサイズmaster
def ImgResizeSquare(i_path, o_path, target_width, target_height):
    
    files = os.listdir(i_path)
    
    for file in files:
        img = Image.open(os.path.join(i_path, file))
        
        # 最大サイズの正方形切り出し → 目的のサイズへリサイズ
        cropped_img = CropMaxSquare(img)
        resized_img = KeepAspectImg(cropped_img, target_width, target_height)

        # 画像保存
        resized_img.save(os.path.join(o_path, file))



if __name__ == "__main__":
    i_path = "C:/Users/81804/Documents/Develop/python/ImgResize_square/imgs"
    o_path = "C:/Users/81804/Documents/Develop/python/ImgResize_square/resized_imgs"
    ImgResizeSquare(i_path, o_path, 256, 256)



