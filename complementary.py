
import colorsys
import json

def get_ngon_palettes(n):
	palettes = []
	max_base_hue = 360 / n
	jump = 360 / n # jump between adjacent colors
	step = 2 # a new palette every 4 degrees

	for x in range(0, int(max_base_hue / step)):
		palette = []
		base_hue = x * step
		for color_index in range(0, n):
			hue = base_hue + (jump * color_index)
			c1 = [round(hue/360, 4), 0.4, 0.4]
			c2 = [round(hue/360, 4), 0.4, 0.6]
			c3 = [round(hue/360, 4), 0.6, 0.4]
			c4 = [round(hue/360, 4), 0.6, 0.6]
			palette.append(c1)
			palette.append(c2)
			palette.append(c3)
			palette.append(c4)
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


