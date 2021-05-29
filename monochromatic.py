
import json
import math

from pypalettes.color import PyColor

saturations = [40, 50, 60, 70, 80, 90, 100]
lightnesses = [20, 30, 40, 50, 60]

palettes = []
index = 1
for hue in range(0, 360, 5):
	palette = {}
	palette["id"] = index
	palette["type"] = "monochromatic"
	palette["hues"] = [hue]
	palette["saturations"] = saturations
	palette["lightnesses"] = lightnesses
	palette["color_group_length"] = len(lightnesses)
	palette["colors"] = []

	for saturation in saturations:
		for lightness in lightnesses:
			color = PyColor(hue, saturation, lightness)
			palette["colors"].append(color.asObject())

	palettes.append(palette)
	index += 1
	# break

jo = {}
jo["palettes"] = palettes
with open("data/monochromatic.json", "w") as f:
	json.dump(jo, f)

print(f"Produced {len(palettes)} palettes.")
