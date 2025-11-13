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
			#print('ord_subset = "3.1.2"', file=fw)
			print('[target.x86_64-windows-gnu]', file=fw)
			print('linker="gcc"')
			print('rustflags=["-C", "target-feature=+crt-static"]', file=fw)
			print()

		#else:
		print(line, file=fw, end='')
