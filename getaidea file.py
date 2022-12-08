import requests
import json
import base64

url = 'https://getaidea.com/wp-json/wp/v2'

user = 'myidea'
password = 'lLdX DdYG n5Gd zZdu E0bD MDMW'

creds = user + ':' + password

token = base64.b64encode(creds.encode())

header = {'Authorization': 'Basic ' + token.decode('utf-8')}



def wpp(text):
    myparagraph = '<!-- wp:paragraph --><p>'+text+'</p><!-- /wp:paragraph -->'
    return myparagraph

def wph2(text):
    myheading = '<!-- wp:heading --><h2>'+text+'</h2><!-- /wp:heading -->'
    return myheading

Model_Nam = input ('Type Model_Nam ')
Car_Price = input ('Type car price ')
Model_number = input ('Type Model_number= ')
Available_colours = input ('Type Available_colours ')
Car_Type = input ('Type Car_Type ')
Milage_in_city = input ('Type Milage_in_city')
Milag_on_highway = input ('Type Milag_on_highway')
#Fuel_type = input ('Type Fuel_type ')
Seating_capatity = input ('Type Seating_capatity ')
No_of_doors = input ('Type No_of_doors ')
steering_types = input ('Type steering_types ')
steering_gyres =input ('Type steering_gyres ')
Engine_power = input ('Type Engine_power ')
Torque = input ('Type Torque ')
Fuel_tyoe = input ('Type Fuel_tyoe ')
Transmission_Type = input ('Type Transmission_Type ')
Drive_Type = input ('Type Drive_Type ')
Minimum_Turning_Radius = input ('Type Minimum_Turning_Radius ')
Front_Suspension = input ('TypeFront_Suspension ')
Back_Suspension = input ('Type Back_Suspension ')
#post_name = input ('Type post name')
wp_title = Model_Nam + 'Price in Bangladesh (Brand new)'




first_paragraph = 'Hello world. Welcome to get a idea. Today you wanted to know about'+Model_Nam+ 'Price in bangladesh and also information about this car. Today we will tell you all info about this car.'+Model_Nam+ 'is an excellent vehicle for everyday use. It is extremely reliable, and the design will never go out of style.'

first_heading =wph2("Basic Information Of "+Model_Nam)

first_table = '<figure class="wp-block-table is-style-stripes"><table><tbody><tr><td>Model Name of Car</td><td>'+Model_Nam+' </td></tr><tr><td>Car Price</td><td>'+Car_Price+' Taka </td></tr><tr><td>Model Number</td><td>'+Model_number+' </td></tr><tr><td>Available colours</td><td>'+Available_colours+' </td></tr><tr><td>Car Type</td><td>'+Car_Type+' </td></tr></tbody></table></figure>'

sec_heading =wph2("Fuel and capacities")

second_table = '<figure class="wp-block-table is-style-stripes"><table><tbody><tr><td>Mileage In City</td><td>'+Milage_in_city+' </td></tr><tr><td>Mileage On Highway</td><td>'+Milag_on_highway+' </td></tr><tr><td>Seating capacity</td><td>'+Seating_capatity+' </td></tr><tr><td>No. Of Doors</td><td>'+No_of_doors+' </td></tr></tbody></table></figure>'

thi_heading =wph2("Head Steering")

third_table = '<figure class="wp-block-table is-style-stripes"><table><tbody><tr><td>Steering Type</td><td>'+steering_types+' </td></tr><tr><td>Steering Gear Type</td><td>'+steering_gyres+' </td></tr></tbody></table></figure>'

fou_heading =wph2("Head engine")

fourth_table= '<figure class="wp-block-table is-style-stripes"><table><tbody><tr><td>Engine Power</td><td>'+Engine_power+'</td></tr><tr><td>Torque</td><td>'+Torque+'</td></tr><tr><td>Fuel Type</td><td>'+Fuel_tyoe+' </td></tr></tbody></table></figure>'

fif_heading =wph2("Head Transmission")

fifth_table='<figure class="wp-block-table is-style-stripes"><table><tbody><tr><td>Transmission Type </td><td>'+Transmission_Type+'+  </td></tr><tr><td>Drive Type</td><td>'+Drive_Type+' </td></tr><tr><td>Minimum Turning Radius</td><td>'+Minimum_Turning_Radius+' </td></tr></tbody></table></figure>'

six_heading =wph2("Head suspensions")



sixth_table =  '<figure class="wp-block-table is-style-stripes"><table><tbody><tr><td>Front Suspension</td><td>'+Front_Suspension+' </td></tr><tr><td>Back Suspension</td><td>'+Back_Suspension+' </td></tr></tbody></table></figure>'

sev_heading =wph2("Safety")

seven_table = '<figure class="wp-block-table is-style-stripes"><table><tbody><tr><td>Power Door Locks</td><td>Yes</td></tr><tr><td>Central Locking</td><td>Yes</td></tr><tr><td>Brake Assist</td><td>Yes</td></tr><tr><td>Anti-Lock Braking</td><td>Yes</td></tr><tr><td>Seat Belt Warning</td><td>Yes</td></tr><tr><td>Rear Seat Belts</td><td>Yes</td></tr><tr><td>Child Safety Locks</td><td>Yes</td></tr><tr><td>Door Ajar Warning</td><td>Yes</td></tr><tr><td>Anti-Theft Device</td><td>Yes</td></tr><tr><td>Rear Camera</td><td>Yes</td></tr><tr><td>Centrally Mounted Fuel Tank</td><td>Yes</td></tr><tr><td>Adjustable Seats</td><td>Yes</td></tr><tr><td>Keyless Entry</td><td>Yes</td></tr><tr><td>Vehicle Stability Control System</td><td>Yes</td></tr><tr><td>Crash Sensor</td><td>Yes</td></tr></tbody></table></figure>'

eig_heading =wph2("Entertainment")

eight_table = '<figure class="wp-block-table is-style-stripes"><table><tbody><tr><td>Touch Screen</td><td>Yes</td></tr><tr><td>Central Locking</td><td>Yes</td></tr><tr><td>Speakers Front & Back</td><td>Yes</td></tr><tr><td>Audio System Remote Control</td><td>Yes</td></tr><tr><td>USB & Auxiliary Input</td><td>Yes</td></tr><tr><td>Bluetooth Connectivity</td><td>Yes</td></tr></tbody></table></figure>'

nin_heading =wph2("Features")
ninth_table = '<figure class="wp-block-table is-style-stripes"><table><tbody><tr><td>Air Conditioner</td><td>Yes</td></tr><tr><td>Heater</td><td>Yes</td></tr><tr><td>AntiLock Braking System</td><td>Yes</td></tr><tr><td>Central Locking</td><td>Yes</td></tr><tr><td>Power Steering</td><td>Yes</td></tr><tr><td>Power Windows</td><td>Yes</td></tr><tr><td>Leather Seats</td><td>Yes</td></tr><tr><td>Fog Lights Front & Back</td><td>Yes</td></tr></tbody></table></figure>'

te_heading =wph2("Others")

tenth_table = '<figure class="wp-block-table is-style-stripes"><table><tbody><tr><td>Bottle Holder</td><td>Yes</td></tr><tr><td>Low Fuel Warning Light</td><td>Yes</td></tr><tr><td>Rear Reading Lamp</td><td>Yes</td></tr><tr><td>Anti-Lock Braking</td><td>Yes</td></tr><tr><td>Adjustable Steering Column</td><td>Yes</td></tr><tr><td>Height Adjustable Driving Seat</td><td>Yes</td></tr><tr><td>Digital Clock</td><td>Yes</td></tr><tr><td>Door Ajar Warning</td><td>Yes</td></tr><tr><td>Smoke Headlamps</td><td>Yes</td></tr><tr><td>Automatic Climate Control</td><td>Yes</td></tr></tbody></table></figure>'

sec_para = 'The'+wp_title+'IS'+Car_Price+'So The '+Model_Nam+ 'can be a fantastic vehicle for you.' 'This car is now available in' +Available_colours+ 'Colour. The type of the car is'+Car_Type+' The model number of this car is'+Model_Nam+ '. You car will give you'+Milage_in_city+' milage in city and'+Milag_on_highway+'milage in highway. The engine power of this car is'+Engine_power+' and the sitting capacity of this car is'+Seating_capatity
third_para = 'The fuel type of this car is'+Fuel_tyoe+'. The steering type of this car is'+steering_types+'. The no of doors available in this car is'+No_of_doors+' and lastly the fuel type of this car is'+No_of_doors+'. The Minimum turning radius is'+Minimum_Turning_Radius+'. The front suspension is'+Front_Suspension+' and the back suspension is'+Back_Suspension+'. The drive type of this car is'+Drive_Type+'.'
#content = wpp(sec_para)+first_table+ wpp(sec_para)+wpp(third_para)+wpp(fourth_para)+wpp(fifth_para)+ wpp(sixth_para)+wpp(seven_para)+first_heading+first_link

content = wpp(first_paragraph)+first_heading+ first_table+sec_heading+second_table+thi_heading+third_table+fou_heading+fourth_table+fif_heading+fifth_table+six_heading+sixth_table+sev_heading+seven_table+eig_heading+eight_table+nin_heading+ninth_table+te_heading+tenth_table+wpp(sec_para)+wpp(third_para)

post = {
    'title':wp_title,
    'content': content,
    'status':'publish',
    'categories':'191',
    }

print ( requests.post(url + '/posts', headers=header, json=post))
