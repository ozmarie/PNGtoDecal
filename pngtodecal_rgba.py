from PIL import Image

BGLAYER = True

def pixeltosnow(rgba, x, y):
    hexval = "{:02X}{:02X}{:02X}{:02X}".format(*rgba)
    fromlayer = "Bg" if BGLAYER else "Fg"
    decalform = "{4}{{\n{4}{4}_editorLayer = 0,\n{4}{4}_fromLayer = \"decals{0}\"," \
    "\n{4}{4}color = \"{1}\",\n{4}{4}rotation = 0,\n{4}{4}scaleX = 0.0625,\n{4}{4}scaleY = 0.0625," \
    "\n{4}{4}texture = \"decals/generic/snow_l\",\n{4}{4}x = {2},\n{4}{4}y = {3}\n{4}}},\n"
    return decalform.format(fromlayer,hexval,x,y," "*4)

def process_image():
    img = Image.open("input.png").convert("RGBA")
    width, height = img.size
    pixels = img.load()
    with open("decalout.txt", "w") as f:
        f.write("{\n")
        for y in range(height):
            for x in range(width):
                if pixels[x, y][-1] != 0:
                    f.write(pixeltosnow(pixels[x, y], x, y))
        f.write("}")

if __name__ == "__main__":
    process_image()
