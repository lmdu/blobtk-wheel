import os

__version__ = "0.4.7-post1"

config_file = 'rust/Cargo.toml'
lib_file = 'rust/src/lib.rs'
py_file = 'rust/src/python.rs'

with open(config_file) as fh:
	lines = fh.readlines()

with open(config_file, 'w') as fw:
	for line in lines:
		if line.startswith('version ='):
			print('version = "{}"'.format(__version__), file=fw)

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
]
with open(lib_file, 'w') as fw:
	for line in lines:
		if line.strip() in mods:
			continue

		print(line, file=fw, end='')

with open(py_file) as fh:
	lines = fh.readlines()

dels = [
	'mod depth;',
	'mod filter;',
	'let filter = PyModule::new(py, "filter")?;',
	'filter.add_function(wrap_pyfunction!(filter::fastx, m)?)?;',
	'm.add_submodule(filter)?;',
	'let depth = PyModule::new(py, "depth")?;',
	'depth.add_function(wrap_pyfunction!(depth::bam_to_bed, m)?)?;',
	'depth.add_function(wrap_pyfunction!(depth::bam_to_depth, m)?)?;',
	'm.add_submodule(depth)?;',
	'filter.add_function(wrap_pyfunction!(filter::fastx, &filter)?)?;',
	'm.add_submodule(&filter)?;',
    'depth.add_function(wrap_pyfunction!(depth::bam_to_bed, &depth)?)?;',
    'depth.add_function(wrap_pyfunction!(depth::bam_to_depth, &depth)?)?;',
    'm.add_submodule(&depth)?;',
]
with open(py_file, 'w') as fw:
	for line in lines:
		if line.strip() in dels:
			continue

		print(line)

		print(line, file=fw, end='')

