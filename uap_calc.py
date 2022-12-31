from datetime import datetime

# distance to proxima centauri = 4.24 mvlight years
# 4.24 light years =  2.4925e+13 miles = 24925000000000 miles
# uap observed have been estimated to be moving ~43,000 mph
# kuyper belt is 4,400,000,000 to 14,900,000,000 miles from earth
# 8760 hours in a year

# first atomic bomb July 16, 1945
# t0: time between now and the detonation of the atomic bomb
# '1945-07-16'
# July 16, 1945

proxima_centauri = 24925000000000 # miles
kuyper_belt_near = 4400000000 # 4.4 billion miles
kuyper_belt_far = 14900000000 # 14.9 billion miles

origin = {
	'proxima_centauri' :24925000000000, # miles
	'kuyper_belt_near' :4400000000, # 4.4 billion miles
	'kuyper_belt_far' :14900000000 # 14.9 billion miles
}

class UAP:
	def __init__(self, departure=None, arrival=None, origin=None, velocity=None) -> None:
		origins = {
			'proxima_centauri' :24925000000000, # miles
			'kuyper_belt_near' :4400000000, # 4.4 billion miles
			'kuyper_belt_far' :14900000000 # 14.9 billion miles
		}
		self.departure = departure
		self.arrival = arrival
		self.d_miles = origin
		if departure != None:
			self.departure = datetime.strptime(departure, '%m/%d/%Y %H:%M:%S')
		if arrival != None:
			self.arrival = datetime.strptime(arrival, '%m/%d/%Y %H:%M:%S')
		if departure != None and arrival != None:
			travel_timedelta = self.arrival - self.departure
			days = travel_timedelta.days
			self.t_hours = days * 24 # hours
		self.v_mph = velocity
		pass

	def calc_velocity(self):
		v_mph = self.d_miles / self.t_hours
		print(f"{v_mph:,.0f} mph")
		return v_mph
	
	def calc_distance(self, v):
		self.d_miles = v * self.t_hours # d = v * t
		print(f"{self.d_miles:,.0f} miles")
		return self.d_miles

	def calc_time(self, v):
		self.t_hours = self.d_miles / v
		print(f"{self.t_hours:,.0f} hours")
		print(f"{self.t_hours/24/365:,.0f} years")
		return self.t_hours

atomic_bomb_tested = '07/16/1945 00:00:00'
# nimitz_encounter
race_track_uaps_in_wisconsin = '12/01/2022 20:30:00'
origins = {
	'proxima_centauri' : 24925000000000, # miles
	'kuyper_belt_near' : 4400000000, # 4.4 billion miles
	'kuyper_belt_far' : 14900000000, # 14.9 billion miles
	'kuyper_belt_mid' : 9400000000, # 9.4 billion miles
	'mars' : 34800000, # 34.8 million miles
	'jupyter' : 464820000, # 464.82 million mi
	'asteroid_belt' : 111500000, # 111.5 million mi
	'sun' : 91407000, # 91.407 million mi
	'venus' : 38000000 # 38 million miles
}

dates = {
	'atomic_bomb_tested' : '07/16/1945 00:00:00',
	'race_track_uaps_in_wisconsin' : '12/01/2022 20:30:00',
	'battle_of_dulce' : '06/01/1979 00:00:00',
	'nimitz_encounter' : '11/14/2004 00:00:00',
}

origin = origins['proxima_centauri']
departure = dates['atomic_bomb_tested']
arrival = dates['race_track_uaps_in_wisconsin']
proxima_cent = UAP(origin=origin, departure=departure, arrival=arrival)
# proxima_cent.calc_velocity()

origin = origins['kuyper_belt_near']
departure = dates['atomic_bomb_tested']
arrival = dates['race_track_uaps_in_wisconsin']
kuyper_near = UAP(origin=origin, departure=departure, arrival=arrival)
# kuyper_near.calc_velocity()

origin = origins['kuyper_belt_far']
departure = dates['atomic_bomb_tested']
arrival = dates['race_track_uaps_in_wisconsin']
kuyper_far = UAP(origin=origin, departure=departure, arrival=arrival)
# kuyper_far.calc_velocity()

origin = origins['venus']
departure = dates['atomic_bomb_tested']
arrival = dates['race_track_uaps_in_wisconsin']
unknown = UAP(origin=origin, departure=departure, arrival=arrival)
# unknown.d_miles = unknown.calc_distance(43000) # 43,000 mph

origin = origins['kuyper_belt_mid']
departure = dates['battle_of_dulce']
arrival = dates['race_track_uaps_in_wisconsin']
kuyper_mid = UAP(origin=origin, departure=departure, arrival=arrival)
# kuyper_mid.calc_velocity()

origin = origins['kuyper_belt_mid']
departure = dates['battle_of_dulce']
arrival = dates['nimitz_encounter']
kuyper_mid = UAP(origin=origin, departure=departure, arrival=arrival)
kuyper_mid.calc_velocity()
