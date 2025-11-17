import os

config_file = 'rust/Cargo.toml'
lib_file = 'rust/src/lib.rs'

with open(config_file) as fh:
	lines = fh.readlines()

with open(config_file, 'w') as fw:
	for line in lines:
		if line.strip() == '[dependencies]':
			#print(line, file=fw, end='')
			#print('openssl = "0.10.75"', file=fw)
			#print('hts-sys = "2.2.0"', file=fw)
			#
			#print('[target.x86_64-pc-windows-gnu]', file=fw)
			#print('linker = "D:/a/_temp/msys64/mingw64/bin/gcc.exe"', file=fw)
			#print('ar = "D:/a/_temp/msys64/mingw64/bin/ar.exe"', file=fw)
			#print('rustflags = ["-C", "target-feature=+crt-static"]', file=fw)
			#print(file=fw)
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
