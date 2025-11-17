import os

config_file = 'rust/Cargo.toml'
lib_file = 'rust/src/lib.rs'

with open(config_file) as fh:
	lines = fh.readlines()

with open(config_file, 'w') as fw:
	for line in lines:
		if line.startswith('version ='):
			print('version = "0.4.7-post1"', file=fw)

		elif line.strip() == '[dependencies]':
			print(line, file=fw, end='')
			print('ord_subset = "3.1.2"', file=fw)

		elif line.startswith('rust-htslib'):
			continue

		else:
			print(line, file=fw, end='')

with open(lib_file) as fh:
	lines = fh.readlines()

mods = [
	'pub mod bam;',
	'pub mod depth;',
	'pub mod filter;',
	'pub mod python;'
]
with open(lib_file, 'w') as fw:
	for line in lines:
		if line.strip() in mods:
			continue

		print(line, file=fw, end='')
