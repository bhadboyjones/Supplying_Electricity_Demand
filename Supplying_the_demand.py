# the lecture talks about calculating amount
# of electricity that needs generation to supply the electricity demand taking into account the losses in the network.

# To get number of buses in the system
number_of_buses = int(input('Enter the nuber of buses (integer number): '))

bus_demand = []
# For loop to get bus demand inputs
for i in range(1, number_of_buses + 1):
    user_input = input(f'Bus {i} Demand (MW): ')  # string
    user_input = float(user_input)
    if user_input >= 0:
        pass
    else:
        print('please enter a number >= 0')
        user_input = input(f'Bus {i} Demand (MW) ')  # string
        user_input = float(user_input)
    bus_demand.append(user_input)

print(bus_demand)
'''
# creating variables b1-b5
for i in range(1, number_of_buses+1):
    globals()['b%s' %i] = bus_demand[i-1]
print(b1, b2, b3, b4, b5)
'''
# Taking into account system losses
user_input = input('Transmission & Distribution losses (%): ')  # String

# Converting strings to float
losses = float(user_input)
print(losses)

print('Demand at bus1 = ', bus_demand[0])
print('Demand at bus2 = ', bus_demand[1])
print('Demand at bus3 = ', bus_demand[2])
print('Demand at bus4 = ', bus_demand[3])
print('Demand at bus5 = ', bus_demand[4])
print('  ')
print('Total demand across the system=', sum(bus_demand[0:5]))
bus_output = []

for i in range(number_of_buses):
    temp = bus_demand[i] / (1 - losses / 100)
    bus_output.append(temp)

print(bus_output[0:5])

# Total generation output
total_gen_output = sum(bus_output[0:number_of_buses])  # What all generators produce at this hour
print('total_generation_output = ', total_gen_output)
print('total demand = ', sum(bus_demand[0:number_of_buses]))
print('losses = ', losses / 100 * total_gen_output)
power_supplied = total_gen_output - losses / 100 * total_gen_output
print('power_supplied = ', power_supplied)

import ipywidgets as widgets
from ipywidgets import Layout
from Ipython.display import display


def to_print(a):
    print(a, 'MW')


def get_buttons(i):
    if (i == 1):
        button = widgets.Button(description=f'case{i}: Total Output w/o t&d losses:', layout=Layout(width='50%'))
    else:
        button = widgets.Button(description=f'Case{i}: Total Output with t&d losses', layout=Layout(width='50%)'))
        print(display(button))

    def clicked(b):
        if (i == 1):
            temp = sum(bus_demand[0:number_of_buses])
        else:
            temp = sum(bus_output[0:number_of_buses])
        to_print(temp)

    button.on_click(clicked)


number_of_cases = 2
for i in range(1, number_of_cases + 1):
    get_buttons(i)
