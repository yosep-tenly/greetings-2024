import subprocess

digital_stream=(
    'Tracy', 'Chris K', 'Kate', 'Fredy', 'Matt', 'Greg', 'Paul B', 'Agathon', 'Catherine H', 'Tristan', 'Catherine P', 'Luton', 'Aman', 'Megan', 'Estelle', 'Paul M', 'Chris D', 'Hayden', 'Wilson', 'Yosep'
)

subprocess.run(['say', '-v', 'Good News', 'Happy Holiday, Digital Stream ...', '-o', f'digital_stream.aiff'])

""" 
    For all member in Digital Stream 
    Happy Holiday! :) 
"""
for member in digital_stream:
    greeting=f'Happy Holiday, {member}...!'
    print(greeting)
    subprocess.run(['say', '-v', 'Good News', greeting, '-o', f'{member}.aiff']) 
