import zipfile

zip_file = 'alien-sample-42.zip'
possible_passwords = [
	'pant', 'papa', 'paps', 'para', 'path', 'pats', 'paty',
	'pard', 'pare', 'park', 'parr', 'pars', 'part', 'pase',
	'pash', 'past', 'pate', 'peal', 'pean', 'pear', 'peas',
	'pave', 'pawl', 'pawn', 'paws', 'pays', 'peag', 'peak',
	'peck', 'pele', 'peat', 'pech', 'peke', 'perm', 'perp',
	'pecs', 'peds', 'peed', 'peek', 'peel', 'peen', 'peep',
	'pelf', 'pelt', 'pend', 'pens', 'pent', 'pass', 'pepo',
	'pert', 'phon', 'phot', 'phut', 'peer', 'pegs', 'pehs',
	'pere', 'peri', 'perk', 'phat', 'phew', 'phis', 'phiz',
	'perv', 'peso', 'pest', 'pets', 'pews', 'pfft', 'pfui',
	'pial', 'pian', 'pias', 'pica', 'pice', 'pick', 'pics',
	'pied', 'pier', 'pies', 'pigs', 'plan', 'plat', 'ploy',
	'pika', 'pike', 'piki', 'pint', 'piny', 'pion', 'pith',
	'pile', 'pili', 'pill', 'pily', 'pima', 'pimp', 'pina',
	'pine', 'ping', 'pink', 'pins', 'plug', 'plum', 'pein',
	'poll', 'peps', 'pits', 'pity', 'pixy', 'plop', 'plot',
	'pipe', 'pips', 'pipy', 'pirn', 'pish', 'piso', 'pita',
	'pole', 'plow', 'plod', 'pois', 'poke', 'poky',
	'play', 'plea', 'pleb', 'pled', 'plew', 'plex', 'plie',
	'plus', 'pock', 'poco', 'pods', 'poem', 'poet', 'pogy'
]

for password in possible_passwords:
	with zipfile.ZipFile(zip_file) as zf:
    	try:
        	zf.extractall(path='/tmp', pwd=password.encode())
        	print(f"File extracted successfully using password: {password}")
        	break
    	except:
        	pass
