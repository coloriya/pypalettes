
import json
import math

from pypalettes.color import PyColor

saturations = [95, 75, 55, 35]
lightnesses = [60, 40, 20]
gaps = [15, 25, 35, 45, 55]

palettes = []
index = 1
for h1 in range(0, 360, 10):
	for gap in gaps:
		h_dash = h1 + 180
		h2 = (h_dash - gap) % 360
		h3 = (h_dash + gap) % 360

		hues = [h1, h2, h3]
		palette = {}
		palette["id"] = index
		palette["type"] = "split-complementary"
		palette["hues"] = hues
		palette["saturations"] = saturations
		palette["lightnesses"] = lightnesses
		palette["color_group_length"] = 6
		palette["n"] = 3
		palette["colors"] = []

		for hue in hues:
			for saturation in saturations:
				for lightness in lightnesses:
					color = PyColor(hue, saturation, lightness)
					palette["colors"].append(color.asObject())

		palettes.append(palette)
		index += 1
		# break

jo = {}
jo["palettes"] = palettes
with open("data/split_complementary.json", "w") as f:
	json.dump(jo, f)

print(f"Produced {len(palettes)} split-complementary palettes.")
