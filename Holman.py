# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 11:28:30 2022

@author: HUAYX179
"""
import json
import requests
import pandas as pd


AUTH_API_ENDPOINT = "https://customer-experience-api.arifleet.com/v1/users/authenticate"
TEST_API_ENDPOINT = "https://customer-experience-api.arifleet.com/v1/fuels?transDateCode=3"

TESTUSER = "E7CCAA5DD8881083D9EA43F04949C72EC1209212"
TESTPW = "Ad32efUH"

def do_auth(username, password, url=AUTH_API_ENDPOINT) -> dict:
    data = {
        'username': username,
        'password': password
    }

    headers = {
        'Content-type': 'application/json',
        'Accept': '*/*'
    }
    
    r = requests.post(url=url, json=data, headers=headers, verify=False)
    response_text = r.text

    d = json.loads(response_text)

    print(d)
    return d

def do_get(url, access_token: str):
    headers = {
        'Content-type': 'application/json',
        'Accept': '*/*',
        'Authorization': access_token
    }
    
    response1 = requests.get(url, headers=headers, verify=False)

    return response1


token_dict = do_auth(TESTUSER, TESTPW)
response = do_get(TEST_API_ENDPOINT, token_dict['token'])
r=response.json()
p=r['totalPages']
'''test=json.loads(r)

print(test)'''
'''print(response.status_code)'''

p=int(p) 

test_1=[]
Pages=range(1,p+1)
for x in Pages:
    url="https://customer-experience-api.arifleet.com/v1/fuels?transDateCode=3&pageNumber="+str(x)
    print(url)
    response3=do_get(url, token_dict['token'])
    data=response3.json()
    test_2=data['can']
    test_1=test_1+test_2
    test_3 = pd.json_normalize(test_1)
    test_3.to_csv('Fuel.csv',index=False)



'''Maintainence table'''
TEST_API_ENDPOINT_MAINTENANCE = "https://customer-experience-api.arifleet.com/v1/maintenance?billPaidDateCode=3"
response_maintenance = do_get(TEST_API_ENDPOINT_MAINTENANCE, token_dict['token'])
r_maintenance=response_maintenance.json()
p_maintenance=int(r_maintenance['totalPages'])


test_1_maintenance=[]
Pages_maintenance=range(1,p_maintenance+1)
for x_maintenance in Pages_maintenance:
    url_maintenance="https://customer-experience-api.arifleet.com/v1/maintenance?billPaidDateCode=3&pageNumber="+str(x_maintenance)
    print(url_maintenance)
    response3_maintenance=do_get(url_maintenance, token_dict['token'])
    data_maintenance=response3_maintenance.json()
    test_2_maintenance=data_maintenance['maintenance']
    test_1_maintenance=test_1_maintenance+test_2_maintenance
    test_3_maintenance = pd.json_normalize(test_1_maintenance)
    test_3_maintenance.to_csv('Maintenance.csv',index=False)

'''Inventory table'''
TEST_API_ENDPOINT_INVENTORY = "https://customer-experience-api.arifleet.com/v1/vehicles"
response_inventory = do_get(TEST_API_ENDPOINT_INVENTORY, token_dict['token'])
r_inventory=response_inventory.json()
p_inventory=int(r_inventory['totalPages'])


test_1_inventory=[]
Pages_inventory=range(1,p_inventory+1)
for x_inventory in Pages_inventory:
    url_inventory="https://customer-experience-api.arifleet.com/v1/vehicles?soldDateCode=1&pageNumber="+str(x_inventory)
    print(url_inventory)
    response3_inventory=do_get(url_inventory, token_dict['token'])
    data_inventory=response3_inventory.json()
    test_2_inventory=data_inventory['inventory']
    test_1_inventory=test_1_inventory+test_2_inventory
    test_3_inventory = pd.json_normalize(test_1_inventory)
    test_3_inventory.to_csv('Inventory.csv',index=False)

'''Accident table'''
TEST_API_ENDPOINT_ACCIDENT = "https://customer-experience-api.arifleet.com/v1/accidents"
response_accident = do_get(TEST_API_ENDPOINT_ACCIDENT, token_dict['token'])
r_accident=response_accident.json()
p_accident=int(r_accident['totalPages'])


test_1_accident=[]
Pages_accident=range(1,p_accident+1)
for x_accident in Pages_accident:
    url_accident="https://customer-experience-api.arifleet.com/v1/accidents?pageNumber="+str(x_accident)
    print(url_accident)
    response3_accident=do_get(url_accident, token_dict['token'])
    data_accident=response3_accident.json()
    test_2_accident=data_accident['accident']
    test_1_accident=test_1_accident+test_2_accident
    test_3_accident = pd.json_normalize(test_1_accident)
    test_3_accident.to_csv('Accident.csv',index=False)


'''Contact table'''
TEST_API_ENDPOINT_CONTACT = "https://customer-experience-api.arifleet.com/v1/persons"
response_contact = do_get(TEST_API_ENDPOINT_CONTACT, token_dict['token'])
r_contact=response_contact.json()
p_contact=int(r_contact['totalPages'])


test_1_contact=[]
Pages_contact=range(1,p_contact+1)
for x_contact in Pages_contact:
    url_contact="https://customer-experience-api.arifleet.com/v1/persons?pageNumber="+str(x_contact)
    print(url_contact)
    response3_contact=do_get(url_contact, token_dict['token'])
    data_contact=response3_contact.json()
    test_2_contact=data_contact['person']
    test_1_contact=test_1_contact+test_2_contact
    test_3_contact = pd.json_normalize(test_1_contact)
    test_3_contact.to_csv('Contact.csv',index=False)
    
'''PM reminder table'''
TEST_API_ENDPOINT_PM_REMINDER = "https://customer-experience-api.arifleet.com/v1/maintenance/preventativeMaintenance?pmDateCode=3"
response_PM_reminder = do_get(TEST_API_ENDPOINT_PM_REMINDER, token_dict['token'])
r_PM_reminder=response_PM_reminder.json()
p_PM_reminder=int(r_PM_reminder['totalPages'])



test_1_PM_reminder=[]
Pages_PM_reminder=range(1,p_PM_reminder+1)
for x_PM_reminder in Pages_PM_reminder:
    url_PM_reminder="https://customer-experience-api.arifleet.com/v1/maintenance/preventativeMaintenance?pmDateCode=3&pageNumber="+str(x_PM_reminder)
    print(url_PM_reminder)
    response3_PM_reminder=do_get(url_PM_reminder, token_dict['token'])
    data_PM_reminder=response3_PM_reminder.json()
    test_2_PM_reminder=data_PM_reminder['pMs']
    test_1_PM_reminder=test_1_PM_reminder+test_2_PM_reminder
    test_3_PM_reminder = pd.json_normalize(test_1_PM_reminder)
    test_3_PM_reminder.to_csv('PM reminder.csv',index=False)
    
    
    
'''Violation table'''
TEST_API_ENDPOINT_VIOLATION = "https://customer-experience-api.arifleet.com/v1/violation?violationDateCode=3"
response_violation = do_get(TEST_API_ENDPOINT_VIOLATION, token_dict['token'])
r_violation=response_violation.json()
p_violation=int(r_violation['totalPages'])



test_1_violation=[]
Pages_violation=range(1,p_violation+1)
for x_violation in Pages_violation:
    url_violation="https://customer-experience-api.arifleet.com/v1/violation?violationDateCode=3&pageNumber="+str(x_violation)
    print(url_violation)
    response3_violation=do_get(url_violation, token_dict['token'])
    data_violation=response3_violation.json()
    test_2_violation=data_violation['violations']
    test_1_violation=test_1_violation+test_2_violation
    test_3_violation = pd.json_normalize(test_1_violation)
    test_3_violation.to_csv('Violation.csv',index=False)
    
'''ODOMETER HISTORY table'''
TEST_API_ODOMETER_HISTORY= "https://customer-experience-api.arifleet.com/v1/Odometer?odometerHistDateCode=1"
response_odometer = do_get(TEST_API_ODOMETER_HISTORY, token_dict['token'])
r_odometer=response_odometer.json()
p_odometer=int(r_odometer['totalPages'])



test_1_odometer=[]
Pages_odometer=range(1,p_odometer+1)
for x_odometer in Pages_odometer:
    url_odometer="https://customer-experience-api.arifleet.com/v1/Odometer?odometerHistDateCode=1&pageNumber="+str(x_odometer)
    print(url_odometer)
    response3_odometer=do_get(url_odometer, token_dict['token'])
    data_odometer=response3_odometer.json()
    test_2_odometer=data_odometer['odometerHistory']
    test_1_odometer=test_1_odometer+test_2_odometer
    test_3_odometer = pd.json_normalize(test_1_odometer)
    test_3_odometer.to_csv('Odometer.csv',index=False)
    
'''ORDER STATUS table'''
TEST_API_ORDER_STATUS= "https://customer-experience-api.arifleet.com/v1/orders"
response_order = do_get(TEST_API_ORDER_STATUS, token_dict['token'])
r_order=response_order.json()
p_order=int(r_order['totalPages'])



test_1_order=[]
Pages_order=range(1,p_order+1)
for x_order in Pages_order:
    url_order="https://customer-experience-api.arifleet.com/v1/orders?pageNumber="+str(x_order)
    print(url_order)
    response3_order=do_get(url_order, token_dict['token'])
    data_order=response3_order.json()
    test_2_order=data_order['orderHistory']
    test_1_order=test_1_order+test_2_order
    test_3_order = pd.json_normalize(test_1_order)
    test_3_order.to_csv('Order Status.csv',index=False)