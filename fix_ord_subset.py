import os

config_file = 'rust/Cargo.toml'

with open(config_file) as fh:
	lines = fh.readlines()

with open(config_file, 'w') as fw:
	for line in lines:
		if line.strip() == '[dependencies]':
			print(line, file=fw, end='')
			print('ord_subset = "3.1.2"', file=fw)
		else:
			print(line, file=fw, end='')
