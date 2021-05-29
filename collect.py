
import json
import os

def main():
	with open("preferences.json") as f:
		preferences = json.load(f)
	
	palette_json_names = preferences["palette_json_names"]
	palettes = []
	for palette_json_name in palette_json_names:
		palette_json_path = os.path.join("data", palette_json_name)
		pj = json.load(open(palette_json_path))
		palettes += pj["palettes"]

	jo = {}
	jo["palettes"] = palettes
	with open("data/palettes.json", "w") as f:
		json.dump(jo, f)
	print(f"{len(palettes)} palettes found.")

if __name__ == '__main__':
	main()
