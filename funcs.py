import re, subprocess, matplotlib.pyplot as plt
import requests, json
from bs4 import BeautifulSoup


def menu():
    selection = None
    gretting = " Welcome to lorenz-attractor CLI tool\n This Tool aims to create an image of the Butterfly shaped lorenz-attractor\n in order to portrait the Butterfly Effect on a graphic plot, the Attractor needs\n Initial Conditions to Sensitively Debend on\n so that the Chaos would settle into Determination by taking Unpredictable Patterns\n\n Please Select from the following Initial Conditions:\n\n"
    
    options = "1.Edward Lorenz\n 2.Your Hardware\n 3.City's Weather\n 4.Manualy \n 0.quit\n\n"
    while selection != 0:
        print(gretting,options)
        selection =  int(input(" please enter option number> "))
        if selection == 0:
            quit()
        else:
            return selection
        
        
def selection_msg(option,x,y,z):
    if option == 1:    
        print(f" \n based on Edward N. Lorenz:\n Rate of convection proportional value = {x} \n Horizontal Temperature Variation proportional value = {y} \n Vertical Temprature Variation proportional value = {z}")
        
    elif option == 2:
        print(f" \n based on your Hardware state:\n Rate of convection proportional value = {x} = CPU-Temp \n Horizontal Temperature Variation proportional value = {y} = Mem-Load \n Vertical Temprature Variation proportional value = {z} = Net-Interface Recived Packets")        
    
    elif option == 3:    
        print(f" \n based on the Weather in {city_name}:\n Rate of convection proportional value = {x} = Temperature \n Horizontal Temperature Variation proportional value = {y} = Humidity \n Vertical Temprature Variation proportional value = {z} = Wind")    

    elif option == 4:    
        print(f" \n based on stdin:\n Rate of convection proportional value = {x}\n Horizontal Temperature Variation proportional value = {y}\n Vertical Temprature Variation proportional value = {z}")
            
            
def mood():
    color = None
    colormap_list_of_lists = [
        [plt.cm.autumn, "autumn"],
        [plt.cm.summer, "summer"],
        [plt.cm.spring, "spring"],
        [plt.cm.winter, "winter"],
        [plt.cm.cool, "cool"],
        [plt.cm.pink, "pink"],
        [plt.cm.hot, "hot"],
        [plt.cm.copper, "copper"],
        [plt.cm.bone, "bone"],
        [plt.cm.afmhot, "afmhot"],
        [plt.cm.gist_heat, "gist_heat"],
        ]
    cm_list_indecies =  [i for i in range(len(colormap_list_of_lists))]
    
    msg = "\n btw how are you doing today ?\n can you please answer from the following options\n which can describe your mood the best:\n\n"
    options = ""
    moods = {}
    
    for n,c in zip(cm_list_indecies, colormap_list_of_lists[:]):
        moods[n] = str(c[1]).capitalize()
        
    for key, value in  moods.items():
        options += f"{key}.{value} "    
    
    print(msg,options)
    color = int(input(" please enter option number> "))
    print()
    if color in cm_list_indecies:
        return colormap_list_of_lists[color]
    else:
        return plt.cm.cool, "cool"
    
    
def fileserver():
    run_server = "./fileservergraphs&"
    subprocess.check_call(run_server, shell=True, text=True, executable="/bin/sh")
    
    process_id =  str(subprocess.check_output("ps -aux | grep ./fileservergraphs | awk 'NR==1{print $2}'",shell=True, text=True, executable="/bin/sh")).replace("\n","")
    
    command  = "ip -4 -o a | cut -d ' ' -f 2,7 | cut -d '/' -f1 | awk 'NR==2{print $1}'"
    net_interface = str(subprocess.check_output(command,shell=True, text=True, executable="/bin/sh")).replace("\n","")
    
    command =  f"ip -f inet addr show {net_interface} | sed -En -e 's/.*inet ([0-9.]+).*/\\1/p'"
    ip_address = str(subprocess.check_output(command, shell=True, text=True, executable="/bin/sh")).replace("\n","")
    
    msg = f" You can check created graphics by visiting http://{ip_address}:9630 from your Web-Browser\n you can stop the file server by kill {process_id}"
    
    return msg


def divider(num):
    num = int(num)
    num  =  str(num)
    zeros =  10 ** len(num)
    return (float(num)) / zeros


def clean_data(a_string):
    value = ""
    for n in a_string:
        if n.isdigit():
            value += n
    return float(value)        
    
    
def hardwareInitConditions():
    cpu_temp  = None
    ram_load = None
    recived_net_packets = None
    
    msg = subprocess.getstatusoutput("cat /sys/class/thermal/thermal_zone*/temp")  # returns a list[status,output]
    m = re.search(r'-?\d\.?\d*', msg[1])   # a solution with a regex 
    cpu_temp = float(m.group())           # returns the substring that was matched by the RE
    
    command = "free -m | awk 'NR==2{print $3}'" # using NR==2 in the awk command, we tell it to only operate on the second line of free's output.
    #command = "awk '/^Mem/ {print $3}' <(free -m)"  # for  /bin/bash 
    output = subprocess.check_output(command, shell=True, text=True, executable="/bin/sh")
    ram_load = float(output.strip())
    
    command = "netstat -i | awk 'NR==3{print $3}'"
    output = subprocess.check_output(command, shell=True, text=True, executable="/bin/sh")
    recived_net_packets = float(output.strip())
    
    
    x = divider(cpu_temp)
    y = divider(ram_load)*10
    z = divider(recived_net_packets)*10
    return x, y, z



headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def weatherInitConditions():
    global city_name 
    city_name = input(" Enter city you want to fetch weather data from> ").capitalize()

    try:
        res = requests.get(
        f'https://www.google.com/search?q={city_name}+weather&oq={city_name}+weather&aqs=chrome..69i57j0i10i512l9.3827j1j7&client=ubuntu-chr&sourceid=chrome&ie=UTF-8', headers=headers)

        soup = BeautifulSoup(res.text, 'html.parser')
        temperature = soup.select('#wob_tm')[0].getText().strip()
        humidity = soup.select('#wob_hm')[0].getText().strip()
        wind = soup.select('#wob_ws')[0].getText().strip()

        temperature =  divider(float(temperature))
        humidity = divider(clean_data(humidity)) * 10
        wind = divider(clean_data(wind)) * 10
        
        return temperature, humidity, wind, city_name
    except:
        return " Please enter a valid city name"


def manualInitConditions():
    x, y, z = divider(float(input(" enter proportional value for Rate of convection x "))), divider(float(input(" enter proportional value Horizontal Temperature Variation y "))), divider(float(input(" enter proportional value Vertical Temperature Variation z ")))
    return x, y * 10, z * 10


# print(hardwareInitConditions())
# weatherInitConditions()
# print(clean_data("17%"))
#print(fileserver())
#weatherInitConditions1()
#mood()
#print(manualInitConditions())