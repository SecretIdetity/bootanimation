from PIL import Image, ImageDraw
import os

#zip: store, no compression
#desc.txt: newline at end, see https://android.googlesource.com/platform/frameworks/base/+/master/cmds/bootanimation/FORMAT.md
#zip in /system/media: chmod 644

scaling = 0.6 #scale for performace
saveasgif = 0 #for debugging
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
c = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0]
d = [
    3, 3, 3, 3, 3,
    3, 2, 2, 2, 3,
    2, 2, 1, 2, 2,
    2, 1, 0, 1, 2,
    2, 1, 0, 1, 2,
    2, 2, 1, 2, 2,
    3, 2, 2, 2, 3,
    3, 3, 3, 3, 3,
]
e = [
    [0.00, 0.00, 0.00, 0.00, 'part0'],
    [0.02, 0.00, 0.00, 0.00, 'part0'],
    [0.05, 0.00, 0.00, 0.00, 'part0'],
    [0.07, 0.00, 0.00, 0.00, 'part0'],
    [0.10, 0.00, 0.00, 0.00, 'part0'],
    [0.12, 0.00, 0.00, 0.00, 'part0'],
    [0.15, 0.00, 0.00, 0.00, 'part0'],
    [0.17, 0.00, 0.00, 0.00, 'part0'],
    [0.20, 0.00, 0.00, 0.00, 'part0'],
    [0.22, 0.02, 0.00, 0.00, 'part0'],
    [0.25, 0.05, 0.00, 0.00, 'part0'],
    [0.27, 0.07, 0.00, 0.00, 'part0'],
    [0.30, 0.10, 0.00, 0.00, 'part0'],
    [0.32, 0.12, 0.00, 0.00, 'part0'],
    [0.35, 0.15, 0.00, 0.00, 'part0'],
    [0.37, 0.17, 0.00, 0.00, 'part0'],
    [0.40, 0.20, 0.00, 0.00, 'part0'],
    [0.40, 0.22, 0.02, 0.00, 'part0'],
    [0.40, 0.25, 0.05, 0.00, 'part0'],
    [0.40, 0.27, 0.07, 0.00, 'part0'],
    [0.40, 0.30, 0.10, 0.00, 'part0'],
    [0.40, 0.32, 0.12, 0.00, 'part0'],
    [0.40, 0.35, 0.15, 0.00, 'part0'],
    [0.40, 0.37, 0.17, 0.00, 'part0'],
    [0.40, 0.40, 0.20, 0.00, 'part0'],
    [0.40, 0.40, 0.22, 0.02, 'part0'],
    [0.40, 0.40, 0.25, 0.05, 'part0'],
    [0.40, 0.40, 0.27, 0.07, 'part0'],
    [0.40, 0.40, 0.30, 0.10, 'part0'],
    [0.40, 0.40, 0.32, 0.12, 'part0'],
    [0.40, 0.40, 0.35, 0.15, 'part0'],
    [0.40, 0.40, 0.37, 0.17, 'part0'],
    [0.40, 0.40, 0.40, 0.20, 'part0'],
    [0.40, 0.40, 0.40, 0.22, 'part0'],
    [0.40, 0.40, 0.40, 0.25, 'part0'],
    [0.40, 0.40, 0.40, 0.27, 'part0'],
    [0.40, 0.40, 0.40, 0.30, 'part0'],
    [0.40, 0.40, 0.40, 0.32, 'part0'],
    [0.40, 0.40, 0.40, 0.35, 'part0'],
    [0.40, 0.40, 0.40, 0.37, 'part0'], #end of part0 frame 39
    [0.40, 0.40, 0.40, 0.40, 'part1'],
    [0.45, 0.40, 0.40, 0.40, 'part1'],
    [0.50, 0.40, 0.40, 0.40, 'part1'],
    [0.55, 0.40, 0.40, 0.40, 'part1'],
    [0.60, 0.40, 0.40, 0.40, 'part1'],
    [0.65, 0.45, 0.40, 0.40, 'part1'],
    [0.70, 0.50, 0.40, 0.40, 'part1'],
    [0.75, 0.55, 0.40, 0.40, 'part1'],
    [0.80, 0.60, 0.40, 0.40, 'part1'],
    [0.80, 0.65, 0.45, 0.40, 'part1'],
    [0.80, 0.70, 0.50, 0.40, 'part1'],
    [0.80, 0.75, 0.55, 0.40, 'part1'],
    [0.75, 0.80, 0.60, 0.40, 'part1'],
    [0.70, 0.80, 0.65, 0.45, 'part1'],
    [0.65, 0.80, 0.70, 0.50, 'part1'],
    [0.60, 0.80, 0.75, 0.55, 'part1'],
    [0.55, 0.75, 0.80, 0.60, 'part1'],
    [0.50, 0.70, 0.80, 0.65, 'part1'],
    [0.45, 0.65, 0.80, 0.70, 'part1'],
    [0.40, 0.60, 0.80, 0.75, 'part1'],
    [0.40, 0.55, 0.75, 0.80, 'part1'],
    [0.40, 0.50, 0.70, 0.80, 'part1'],
    [0.40, 0.45, 0.65, 0.80, 'part1'],
    [0.40, 0.40, 0.60, 0.80, 'part1'],
    [0.40, 0.40, 0.55, 0.75, 'part1'],
    [0.40, 0.40, 0.50, 0.70, 'part1'],
    [0.40, 0.40, 0.45, 0.65, 'part1'],
    [0.40, 0.40, 0.40, 0.60, 'part1'],
    [0.40, 0.40, 0.40, 0.55, 'part1'],
    [0.40, 0.40, 0.40, 0.50, 'part1'],
    [0.40, 0.40, 0.40, 0.45, 'part1'], #end of part1 frame 70
    [0.40, 0.40, 0.40, 0.40, 'part2'],
    [0.45, 0.40, 0.40, 0.40, 'part2'],
    [0.50, 0.40, 0.40, 0.40, 'part2'],
    [0.55, 0.40, 0.40, 0.40, 'part2'],
    [0.60, 0.40, 0.40, 0.40, 'part2'],
    [0.65, 0.45, 0.40, 0.40, 'part2'],
    [0.70, 0.50, 0.40, 0.40, 'part2'],
    [0.75, 0.55, 0.40, 0.40, 'part2'],
    [0.80, 0.60, 0.40, 0.40, 'part2'],
    [0.85, 0.65, 0.45, 0.40, 'part2'],
    [0.90, 0.70, 0.50, 0.40, 'part2'],
    [0.95, 0.75, 0.55, 0.40, 'part2'],
    [1.00, 0.80, 0.60, 0.40, 'part2'],
    [1.00, 0.85, 0.65, 0.45, 'part2'],
    [1.00, 0.90, 0.70, 0.50, 'part2'],
    [1.00, 0.95, 0.75, 0.55, 'part2'],
    [1.00, 1.00, 0.80, 0.60, 'part2'],
    [0.90, 1.00, 0.85, 0.65, 'part2'],
    [0.90, 1.00, 0.90, 0.70, 'part2'],
    [1.00, 0.90, 0.95, 0.75, 'part2'],
    [1.00, 0.90, 1.00, 0.80, 'part2'],
    [1.00, 1.00, 0.90, 0.85, 'part2'],
    [1.00, 1.00, 0.90, 0.90, 'part2'],
    [1.00, 1.00, 1.00, 0.95, 'part2'],
    [1.00, 1.00, 1.00, 1.00, 'part2'],
    [0.95, 1.00, 1.00, 1.00, 'part2'],
    [0.90, 1.00, 1.00, 1.00, 'part2'],
    [0.85, 0.95, 1.00, 1.00, 'part2'],
    [0.90, 0.90, 1.00, 1.00, 'part2'],
    [0.95, 0.85, 0.95, 1.00, 'part2'],
    [1.00, 0.90, 0.90, 1.00, 'part2'],
    [1.00, 0.95, 0.85, 0.95, 'part2'],
    [1.00, 1.00, 0.90, 0.90, 'part2'],
    [1.00, 1.00, 0.95, 0.85, 'part2'],
    [1.00, 1.00, 1.00, 0.90, 'part2'],
    [1.00, 1.00, 1.00, 0.95, 'part2'],
    [1.00, 1.00, 1.00, 1.00, 'part2'],
    [1.00, 1.00, 1.00, 1.00, 'part2'],
    [0.90, 0.90, 0.90, 0.90, 'part2'],
    [0.80, 0.80, 0.80, 0.80, 'part2'],
    [0.70, 0.70, 0.70, 0.70, 'part2'],
    [0.60, 0.60, 0.60, 0.60, 'part2'],
    [0.50, 0.50, 0.50, 0.50, 'part2'],
    [0.40, 0.40, 0.40, 0.40, 'part2'],
    [0.30, 0.30, 0.30, 0.30, 'part2'],
    [0.20, 0.20, 0.20, 0.20, 'part2'],
    [0.10, 0.10, 0.10, 0.10, 'part2'],
    [0.00, 0.00, 0.00, 0.00, 'part2'], #end of part2 frame 118
    ]
f = []
i = 0
o = int(20 * scaling)
u = int(240 * scaling)
s = (int(1200 * scaling), int(1920 * scaling))
t = Image.open("img.png").resize((u - o * 2, u - o * 2)).convert('RGBA')
p = Image.new('RGBA', (u - o * 2, u - o * 2), (0, 0, 0))

for k in e:
    if os.path.exists(f'./{k[4]}'):
        os.rmdir(f'./{k[4]}')
    os.mkdir(f'./{k[4]}') #not efficient but who cares

while i < len(e):
    img = Image.new('RGBA', s, (0, 0, 0))
    x = 0
    y = 0
    for j, k in enumerate(c):
        k = e[i][d[j]]
        t = t.rotate(180)
        img.paste(Image.blend(p, t, k), (x + o, y + o, x + u - o, y + u - o))
        x += u
        if x == s[0]:
            x = 0
            y += u
    img.resize(s)
    if saveasgif:
        f.append(img)
    else:
        img.save(f'./{e[i][4]}/{str(i).zfill(5)}.png')
    i += 1

if saveasgif:
    img = Image.new('RGBA', s, (0, 0, 0))
    img.save("img.gif", save_all=True, append_images=f, duration=33, loop=0)
