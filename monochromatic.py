
import json
import math

from pypalettes.color import PyColor

saturations = [90, 80, 70, 60, 50, 40]
lightnesses = [60, 50, 40, 30, 20]

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
	palette["n"] = 1
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

print(f"Produced {len(palettes)} monochromatic palettes.")
