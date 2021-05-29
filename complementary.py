
import json
import math

from pypalettes.color import PyColor

palette_types = [
	None, None, "complementary",
	"triadic", "tetradic",
	"pentagonal", "hexagonal"
]

s_pairs = [
	[70, 30],
	[80, 40],
	[90, 50],
	[85, 55],
	[95, 65]
]

l_pairs = [
	[60, 40, 20],
	[50, 30, 10]
]



index = 1
def get_ngon_palettes(n):
	global index
	palettes = []
	max_base_hue = int(360 / n)
	jump = int(360 / n) # jump between adjacent colors
	step = 10 # a new palette every 10 degrees
	number_of_hues = int(max_base_hue / step)

	for x in range(0, number_of_hues):
		base_hue = x * step
		for s_pair in s_pairs:
			for l_pair in l_pairs:
				palette = {}
				palette["id"] = index
				palette["colors"] = []
				palette["type"] = palette_types[n]
				for color_index in range(0, n):
					h = int(base_hue + (jump * color_index))
					for s in s_pair:
						for l in l_pair:
							color = PyColor(h, s, l)
							palette["colors"].append(color.asObject())
				palettes.append(palette)
				index += 1
	return palettes


palettes = []
for x in range(2, 7):
	palettes += get_ngon_palettes(x)



jo = {}
jo["palettes"] = palettes
with open("data/complementary.json", "w") as f:
	json.dump(jo, f)

print(f"Produced {len(palettes)} palettes.")
