
import colorsys
import json

s_pairs = [
	[0.4, 0.6],
	[0.6, 0.8],
	[0.8, 0.4]
]

l_pairs = [
	[0.2, 0.4],
	[0.4, 0.6],
	[0.6, 0.2]
]

def get_ngon_palettes(n):
	palettes = []
	max_base_hue = 360 / n
	jump = 360 / n # jump between adjacent colors
	step = 10 # a new palette every 10 degrees

	for x in range(0, int(max_base_hue / step)):
		base_hue = x * step
		for s_pair in s_pairs:
			for l_pair in l_pairs:
				palette = []
				for color_index in range(0, n):
					hue = base_hue + (jump * color_index)
					h = round(hue/360, 4)
					for s in s_pair:
						for l in l_pair:
							c = [h, s, l]
							palette.append(c)
				#print(palette)
				palettes.append(palette)
	return palettes


palettes = []
for x in range(2, 7):
	palettes += get_ngon_palettes(x)

pals = []
index = 1
for palette in palettes:
	pal = {}
	pal["id"] = index
	pal["colors"] = []
	for hsl_color in palette:
		color = {}
		h = int(hsl_color[0] * 360)
		s = int(hsl_color[1] * 100)
		l = int(hsl_color[2] * 100)
		color["hsl"] = [h, s, l]
		rgb = colorsys.hls_to_rgb(*hsl_color)
		rgb = [int(e * 256) for e in rgb]
		color["rgb"] = rgb
		color["hex"] = '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])
		pal["colors"].append(color)
	pals.append(pal)
	index += 1

jo = {}
jo["palettes"] = pals
with open("data/complementary.json", "w") as f:
	json.dump(jo, f)

print(f"Produced {len(palettes)} palettes.")
