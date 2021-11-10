value = float(input())
iterations = 0
if value >= 10:
	while 1 <= value and value >= 10:
		value = value/10
		iterations+=1
	if iterations < 10:
		print(f"+{(value):.4f}E+0{iterations}")
	else:
		print(f"+{(value):.4f}E+{iterations}")
elif 0 < value < 10:
    if value >= 1:
        while value <= 10:
            if value * 10 >= 10:
                break
            else:
                value = value * 10
                iterations += 1
        if iterations < 10:
            print(f"+{(value):.4f}E+0{iterations}")
        else:
            print(f"+{(value):.4f}E+{iterations}")
    else:
        while value <= 10:
            if value * 10 >= 10:
                break
            else:
                value = value * 10
                iterations += 1
        if iterations < 10:
            print(f"+{(value):.4f}E-0{iterations}")
        else:
            print(f"+{(value):.4f}E-{iterations}")
        
elif value < 0:
	if abs(value) < 10:
		while value * (-1) < 10:
			value = value * 10
			iterations += 1
		if iterations < 10:
			print(f"{(value/10):.4f}E-0{iterations - 1}")
		else:
			print(f"{(value/10):.4f}E{iterations - 1}")
	elif abs(value) > 10:
		while abs(value) > 10:
			value = value/10
			iterations+=1
		if iterations < 10:
			print(f"{(value):.4f}E+0{iterations}")
		else:
			print(f"{(value):.4f}E+{iterations}")
elif str(value)[0] == '-':
	print(f'-0.0000E+00')
elif str(value)[0] == '0':
	print(f'+0.0000E+00')