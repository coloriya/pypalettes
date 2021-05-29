
import colorsys

def hsl_to_rgb(h, s, l):
	rgb_decimal = colorsys.hls_to_rgb(h/360, l/100, s/100)
	rgb = [int(x * 255) for x in rgb_decimal]
	return rgb

class PyColor():
	def __init__(self, hue, saturation, lightness):
		self.hue = hue
		self.saturation = saturation
		self.lightness = lightness

	def asObject(self):
		color = {}
		color["hsl"] = [self.hue, self.saturation, self.lightness]
		rgb = hsl_to_rgb(self.hue, self.saturation, self.lightness)
		rgb = hsl_to_rgb(self.hue, self.saturation, self.lightness)
		color["rgb"] = rgb
		color["hex"] = '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])
		return color


