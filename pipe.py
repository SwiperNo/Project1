def rental_car_cost(days):
rental_car_cost = days * 40
	if days >= 7:
		return rental_car_cost + 50
	elif days >=3:
		return rental_car_cost - 20
	else:
		return rental_car_cost
		

rental_car_cost(3)		