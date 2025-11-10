import os

config_file = 'rust/Cargo.toml'

with open(config_file) as fh:
	lines = fh.readlines()

with open(config_file, 'w') as fh:
	for line in lines:
		if line.strip() == '[dependencies]':
			print(line, end='')
			print('ord_subset = "3.1.2"')
		else:
			print(line, end='')
