# Created by: Roman Beya & Malcolm McCarthy
# Created on 21-12-17
# Created for ICS3U
# This program uses enumerated types for the provinces and street type parameters

from enum import Enum

# Create an enumeration of street types
Street_Type = Enum('Street', 'Lane', 'Avenue', 'Drive', 'Road')

# Create an array of street types that will hold the value that the user enters
street_array = []

# Create an enumeration of provinces/territories
Provinces = Enum('BC', 'AB', 'ON', 'NB', 'NS', 'QC', 'MB', 'NL', 'SK', 'PE', 'NU', 'NT', 'YT')

# Create an array of provinces/territories that will hold the value that the user enters
provinces_array = []

class Postal_Service():
	def __init__(self, full_name, city, province, unit, street, postal_code):
		self.full_name = full_name
		self.city = city
		self.province = province
		self.unit = unit
		self.street = street
		self.postal_code = postal_code
		
		
FULL_NAME = raw_input("Enter your full name: ")
CITY = raw_input("Enter the city in which you reside: ")
PROVINCE = raw_input("Enter the province or territory that you live in: ")

# Append their responce to an array
provinces_array.append(PROVINCE)

# Loop through the array to compare their responce to a valid responce in the enumerated types
for valid_province_or_territory in provinces_array:
	# If their responce matches one of the enumerated values, proceed with the rest of the program
	if valid_province_or_territory in Provinces:
		UNIT = raw_input("Enter your house/apt that you live at: ")
		STREET = raw_input("Enter your street type: ")
		street_array.append(STREET)
		# Repeated logic as stated, above
		for valid_street_type in street_array:
			if valid_street_type in Street_Type:	
				POSTAL_CODE = raw_input("Enter your postal code: ")
			else:
				print 'Sorry, that is not a valid street type.'
				break
	else:
		print 'Sorry, that is not a valid Canadian province or territory.'
		break

canada_post = Postal_Service(FULL_NAME, CITY, PROVINCE, UNIT, STREET, POSTAL_CODE)

print(canada_post.full_name, canada_post.city, canada_post.province, canada_post.unit, canada_post.street, canada_post.postal_code)
