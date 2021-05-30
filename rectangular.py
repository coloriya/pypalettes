
import json
import math

from pypalettes.color import PyColor

saturations = [35, 55, 75, 95]
lightnesses = [20, 40, 60]
gaps = [30, 40, 50, 60, 70, 80, 100, 110, 120, 130, 140, 150]

palettes = []
index = 1
for h1 in range(0, 170, 10):
	for gap in gaps:
		h2 = h1 + gap
		if h2 >= 180:
			break

		h3 = 180 + h1
		h4 = 180 + h2
		hues = [h1, h2, h3, h4]
		palette = {}
		palette["id"] = index
		palette["type"] = "rectangular"
		palette["hues"] = hues
		palette["saturations"] = saturations
		palette["lightnesses"] = lightnesses
		palette["color_group_length"] = 6
		palette["n"] = 4
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
with open("data/rectangular.json", "w") as f:
	json.dump(jo, f)

print(f"Produced {len(palettes)} rectangular palettes.")
