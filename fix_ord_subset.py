import os

config_file = 'rust/Cargo.toml'

with open(config_file) as fh:
	lines = fh.readlines()

with open(config_file, 'w') as fw:
	for line in lines:
		if line.strip() == '[dependencies]':
			#print(line, file=fw, end='')
			#print('openssl = "0.10.75"', file=fw)
			#print('hts-sys = "2.2.0"', file=fw)
			#
			print('[target.x86_64-pc-windows-gnu]', file=fw)
			print('linker = "gcc.exe"', file=fw)
			print('ar = "ar.exe"', file=fw)
			#print('rustflags = ["-C", "target-feature=+crt-static"]', file=fw)
			print(file=fw)
			print(line, file=fw, end='')
			print('ord_subset = "3.1.2"', file=fw)
		else:
			print(line, file=fw, end='')
