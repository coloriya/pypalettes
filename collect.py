
import json
import os

def main():
	with open("preferences.json") as f:
		preferences = json.load(f)
	
	palette_json_names = preferences["palette_json_names"]
	palettes = []
	for palette_json_name in palette_json_names:
		palette_json_path = os.path.join("data", palette_json_name)
		if not os.path.isfile(palette_json_path):
			print(f"Not found: {palette_json_path}")
			continue
		pj = json.load(open(palette_json_path))
		palettes += pj["palettes"]

	index = 1
	for palette in palettes:
		palette["id"] = index
		index += 1

	jo = {}
	jo["palettes"] = palettes
	with open("data/palettes.json", "w") as f:
		json.dump(jo, f)
	print(f"Collected {len(palettes)} palettes.")

if __name__ == '__main__':
	main()
