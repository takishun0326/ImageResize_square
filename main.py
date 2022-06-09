import os 
from PIL import Image

# 画像の中心を切り出し
def CropCenter(img, target_width, target_height, amt_shift):
    return img.crop(((img.width - target_width) // 2,
     (img.height - target_height) // 2 + amt_shift,
     (img.width + target_width) // 2,
     (img.height + target_height) // 2 + amt_shift))


# 最大サイズの正方形切り出し
def CropMaxSquare(img, amt_shift):
    return CropCenter(img, min(img.size), min(img.size), amt_shift)

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
def ImgResizeSquare(i_path, o_path, target_width, target_height, amt_shift):
    
    files = os.listdir(i_path)
    
    for file in files:
        img = Image.open(os.path.join(i_path, file))
        
        # 最大サイズの正方形切り出し → 目的のサイズへリサイズ
        cropped_img = CropMaxSquare(img, amt_shift)
        resized_img = KeepAspectImg(cropped_img, target_width, target_height)

        # 画像保存
        resized_img.save(os.path.join(o_path, file))

# 入力パス, 出力パスをコンソールの入力として取得
def GetInputOutputPath():
    
    print("入力画像フォルダのパス")
    i_path = input(">> ")

    print("出力先フォルダのパス")
    o_path = input(">> ")

    return i_path, o_path


if __name__ == "__main__":

    RESIZE_WIDTH_DEFAULT = 256
    RESIZE_HEIGHT_DEFAULT = 256

    # 正方形切り出しの位置を上げる量 負: 上へシフト, 正: 下へシフト
    AMOUNT_SHIFT = -240

    # 入力, 出力のパス取得
    i_path, o_path = GetInputOutputPath()

    ImgResizeSquare(i_path, o_path, RESIZE_WIDTH_DEFAULT, RESIZE_HEIGHT_DEFAULT, AMOUNT_SHIFT)



