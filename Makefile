
collect:
	@python collect.py

regenerate:
	@python monochromatic.py
	@python rectangular.py
	@python complementary.py
	@python split_complementary.py
	@python analogous.py
	@python analogous_triad.py
	@python analogous_quad.py

clean:
	@rm -f data/*.json

