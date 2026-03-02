from PIL import Image, ImageFilter


before = Image.open("before.jpg")
after = before.filter(ImageFilter.BoxBlur(15))
after.save("after.jpg")