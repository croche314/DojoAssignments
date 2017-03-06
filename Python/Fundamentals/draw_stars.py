def draw_stars(arr):
	for x in arr:
		if type(x) == str:
			print x[0].lower() * len(x)
		else:
			print "*" * int(x)

array = [4,"Tom",1,"Michael",.5,7,"Jimmy Smith"]

draw_stars(array)