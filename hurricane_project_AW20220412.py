# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1 
# Update Recorded Damages

# write your update damages function here:

conversion = {"M": 1000000,
              "B": 1000000000}

### This works, but is not as elegant: 
# def update_damages(dam):
#   updated_damages = []
#   for i in dam:
#     if i[-1] == "M":
#       updated_damages.append(float(i.strip("M"))*float(1000000))
#     elif i[-1] == "B":
#       updated_damages.append(float(i.strip("B"))*float(1000000000))
#     else:
#       updated_damages.append(i)
#   print(updated_damages)

def update_damages(dam):
  updated_damages = []
  for i in dam:
    if i[-1] == "M":
      updated_damages.append(float(i.strip("M"))*conversion["M"])
    elif i[-1] == "B":
      updated_damages.append(float(i.strip("B"))*conversion["B"])
    else:
      updated_damages.append(i)
  return(updated_damages)

new_damages = update_damages(damages)




# 2 
# Create a Table

# write your construct hurricane dictionary function here:

# Create and view the hurricanes dictionary
def full_hurricanes(name, month, year, max_sustained_wind, areas_affected, damage, death):
  hurricanes = {}
  for i in range(0,len(names)):
    hurricanes[name[i]] = {"Names": name[i], "Months": month[i], "Year": year[i], "Max Sustained Wind": max_sustained_wind[i], "Areas Affected": areas_affected[i], "Damage": damage[i], "Deaths": death[i]}
  return(hurricanes)

total_hurricanes = full_hurricanes(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)

# print(total_hurricanes)


# 3
# Organizing by Year

# write your construct hurricane by year dictionary function here:

# create a new dictionary of hurricanes with year and key

def year_hurricanes(hurricane_dict):
  hurricanes_by_year = {}
  for i in hurricanes:
    current_year = hurricanes[i]['Year']
    current_hurricane = hurricanes[i]
    if current_year not in hurricanes_by_year:
      hurricanes_by_year[current_year] = [current_hurricane]
    else:
      hurricanes_by_year[current_year].append(current_hurricane)
  return hurricanes_by_year

by_year = year_hurricanes(hurricanes)




# 4
# Counting Damaged Areas

# write your count affected areas function here:

# create dictionary of areas to store the number of hurricanes involved in
def count_affected_areas(dictionary):
  affected_areas_counts = {}
  for i in hurricanes:
    area = hurricanes[i]['Areas Affected']
    for loc in area:
      if loc not in affected_areas_counts:
        affected_areas_counts[loc] = 1
      else:
        affected_areas_counts[loc] += 1
  return affected_areas_counts

areas_counts = count_affected_areas(hurricanes)
# print(areas_counts["Central America"])



# 5 
# Calculating Maximum Hurricane Count

# write your find most affected area function here:

# find most frequently affected area and the number of hurricanes involved in

#This is probably the most efficient way to do this, but it was not taught in the lessons so far and does not return that key that belongs to the value...
def highest_hit(dictionary):
  max_count = max(areas_counts, key=areas_counts.get)
  return max_count, 
# print(highest_hit(areas_counts))

def most_affected_areas(dictionary):
  max_area = ''
  max_area_count = 0
  for area in dictionary:
    if dictionary[area] > max_area_count:
      max_area = area
      max_area_count = dictionary[area]
  return max_area, max_area_count

print(most_affected_areas(areas_counts))




# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

# write your greatest number of deaths function here:

def most_deaths(dictionary):
  max_death = ''
  max_death_count = 0
  for i in dictionary:
    hurricane = dictionary[i]['Names']
    if dictionary[i]['Deaths'] > max_death_count:
      max_death = dictionary[i]['Names']
      max_death_count = dictionary[i]['Deaths']
  return max_death, max_death_count

print(most_deaths(hurricanes))




# 7
# Rating Hurricanes by Mortality

# write your catgeorize by mortality function here:

# categorize hurricanes in new dictionary with mortality severity as key



def categorize_by_mortality(hurricanes):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  mortality_rates = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for i in hurricanes:
    deaths = hurricanes[i]['Deaths']
    if deaths == mortality_scale[0]:
      mortality_rates[0].append(hurricanes[i])
    elif deaths > mortality_scale[0] and deaths <= mortality_scale[1]:
      mortality_rates[1].append(hurricanes[i])
    elif deaths > mortality_scale[1] and deaths <= mortality_scale[2]:
      mortality_rates[2].append(hurricanes[i])
    elif deaths > mortality_scale[2] and deaths <= mortality_scale[3]:
      mortality_rates[3].append(hurricanes[i])
    elif deaths > mortality_scale[3] and deaths <= mortality_scale[4]:
      mortality_rates[4].append(hurricanes[i])
    elif deaths > mortality_scale[4]:
      mortality_rates[5].append(hurricanes[i])
  return mortality_rates

hurricanes_by_mortality = categorize_by_mortality(hurricanes)
print(hurricanes_by_mortality)






# write your greatest damage function here:
# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost

def most_damage(dictionary):
  max_cost = ''
  max_cost_tracking = 0
  for i in dictionary:
    hurricane = dictionary[i]['Names']
    if dictionary[i]['Damage'] == "Damages not recorded":
      pass # continue also works here
    elif dictionary[i]['Damage'] > max_cost_tracking:
      max_cost = dictionary[i]['Names']
      max_cost_tracking = dictionary[i]['Damage']
  return max_cost, max_cost_tracking

most_damaging = most_damage(hurricanes)
print(most_damaging)# 8 Calculating Hurricane Maximum Damage



# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost



def most_damage(dictionary):
  max_cost = ''
  max_cost_tracking = 0
  for i in dictionary:
    hurricane = dictionary[i]['Names']
    if dictionary[i]['Damage'] == "Damages not recorded":
      pass # continue also works here
    elif dictionary[i]['Damage'] > max_cost_tracking:
      max_cost = dictionary[i]['Names']
      max_cost_tracking = dictionary[i]['Damage']
  return max_cost, max_cost_tracking

most_damaging = most_damage(hurricanes)
print(most_damaging)







# 9
# Rating Hurricanes by Damage
# damage_scale = {0: 0,
#                 1: 100000000,
#                 2: 1000000000,
#                 3: 10000000000,
#                 4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

# write your catgeorize by damage function here:

def cat_by_damage(dictionary):
  damage_scale = {0: 0,
                  1: 100000000,
                  2: 1000000000,
                  3: 10000000000,
                  4: 50000000000}
  damages_ratings = {'NR': [], 0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for i in dictionary:
    if dictionary[i]['Damage'] == "Damages not recorded":
      damages_ratings['NR'].append(dictionary[i]) 
    elif dictionary[i]['Damage'] == damage_scale[0]:
      damages_ratings[0].append(dictionary[i])
    elif dictionary[i]['Damage'] > damage_scale[0] and dictionary[i]['Damage'] <= damage_scale[1]:
      damages_ratings[1].append(dictionary[i])
    elif dictionary[i]['Damage'] > damage_scale[1] and dictionary[i]['Damage'] <= damage_scale[2]:
      damages_ratings[2].append(dictionary[i])
    elif dictionary[i]['Damage'] > damage_scale[2] and dictionary[i]['Damage'] <= damage_scale[3]:
      damages_ratings[3].append(dictionary[i])
    elif dictionary[i]['Damage'] > damage_scale[3] and dictionary[i]['Damage'] <= damage_scale[4]:
      damages_ratings[4].append(dictionary[i])
    elif dictionary[i]['Damage'] > damage_scale[4]:
      damages_ratings[5].append(dictionary[i])
  return damages_ratings

hurricanes_by_damage_rating = cat_by_damage(hurricanes)
print(hurricanes_by_damage_rating[5])
