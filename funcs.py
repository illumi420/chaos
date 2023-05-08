import re, subprocess, matplotlib.pyplot as plt
import requests, json
from bs4 import BeautifulSoup
import os, random, string  

global GRAPHS_PATH
GRAPHS_PATH = os.getcwd()+"/graphs/"


def ascii_art():
    ascii_art = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@&&&&&&&&&&&##&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&@@@@@@@@@@\n@@@@@@@@@&&&&&&##&&&&&&&&&####&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#BBBB##&&&&@@@@@@@@\n@@@@@@@@&&&&&#&&&&&&&&&&&&&&&&####&&&&&@@@@@@@@@@@@@@@@@@@@&&#BGPPGGB###&&&&#&@@@@@@@\n@@@@@@@&&@&&#&&&&&&@@@&&&&&&&&&&&###&&&&&@@@@@@@@@@@@@@&&#GP5PPGB##&&&&&#&&##@@@@@@@@\n@@@@@@@&&&&#&&&&&&@@&&&&&&&&&&&&&&&###&&&&@@@@@@@@@&&#GPP5PGB&&@@@@@&&##B&##@@@@@@@@@\n@@@@@@&&@&&#&&@&&@&&&@@@@@@&&&&&&&&&&##&&&&&@@&&&#BGPPPGB&@@@@@@@@@&##BB#B#@@@@@@@@@@\n@@@@@@@&@&&#&&&&&@&&@@@@@@@@@&&&&&&&&&&#&&&&##BGGGGGB#&@@@@@@@@@@&#BBB###&@@@@@@@@@@@\n@@@@@@@&&&&#&&@&&@&&&@@@@@@@@@@&&&&&&&&#B##BBGBBBB#&&@@@@@@@@@&&#BBBBB#&@@@@@@@@@@@@@\n@@@@@@@&&&&##&&&&&&&&&@@@@@@@@&&&&&&&&#&BGBB#BB##&&&@@@@@@@&&#BBBBBB#&&@@@@@@@@@@@@@@\n@@@@@@@@&&&&##&&&&&&&&&&&&@@&&&&@@&&&@&#BG###B&#&&&&&&&&&&#BBBBB###&@@@@@@@@@@@@@@@@@\n@@@@@@@@@&&&&##&&&&&&&&&&&&&&@@@&&&&&&B#&B#&##&&#&&&&###########&&@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@&&&&&###&&&&&&&&&&&&&&&&&&&##&&#&&&#&&&&&&&&&######&&@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@&&&&&&###&&&&&&&&&&&&&&##&&&&&&&@&&&&&&&&###&&&@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@&&&&&&&&###########&&&&&&&&@&&@@@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"

    return ascii_art


def menu():
    print()
    print(ascii_art())
    selection = None
    gretting = " Welcome to lorenz-attractor CLI tool\n\n This Tool aims to create an image of the Butterfly shaped lorenz-attractor\n in order to portrait the Butterfly Effect on a graphic plot, the Attractor needs\n Initial Conditions to Sensitively Debend on so that the Chaos would settle into\n Determination by taking Unpredictable Patterns\n\n Please Select from the following Initial Conditions:\n\n"
    
    options = "1.Edward Lorenz\n 2.Your Hardware\n 3.City's Weather\n 4.Manualy/Random \n 0.quit\n"
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
    random_mood = random.randint(0, 11)
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
        [plt.cm.Wistia, "Wistia"]
        ]
    cm_list_indecies =  [i for i in range(len(colormap_list_of_lists))]
    
    msg = "\n btw how are you doing today ?\n can you please answer from the following options\n which can describe your mood the best:\n\n"
    options = ""
    moods = {}
    
    for n,c in zip(cm_list_indecies, colormap_list_of_lists[:]):
        moods[n] = str(c[1]).capitalize()
        
    for key, value in  moods.items():
        options += f"{key}.{value} "
            
    try:
        print(msg,options+"\n press Enter if You're feeling Random")
        color = int(input(" please enter option number> "))
        print()
        if color in cm_list_indecies:
            return colormap_list_of_lists[color]
    except:
        print()
        return colormap_list_of_lists[random_mood]


def graphics_extension(fname):
    extensions = [
        ".eps", ".jpeg", ".jpg", ".pdf", ".pgf", ".png", ".ps", ".raw", ".rgba", ".svg", ".svgz", ".tif", ".tiff", ".webp" 
        ]
    extensions_list_indecies =  [i for i in range(len(extensions))]
    options = " "
    formats = {}
    
    for i, e in zip(extensions_list_indecies,extensions):
        formats[i] = e
    for key, value in formats.items():
        options += f"{key}{value}  "    
    print(options)
    
    try:
        msg = int(input(" please select file extension option number> "))
        print()
        if msg in extensions_list_indecies:
            return f"{fname}{extensions[msg]}"
    except:
        return f"{fname}{extensions[5]}"


def fileserver():
    NETIF = str(subprocess.check_output("ip -4 -o a | cut -d ' ' -f 2,7 | cut -d '/' -f1 | awk 'NR==2{print $1}'",shell=True, text=True, executable="/bin/sh")).replace("\n","") 
    
    IP = str(subprocess.check_output(f"ip -f inet addr show {NETIF} | sed -En -e 's/.*inet ([0-9.]+).*/\\1/p'", shell=True, text=True, executable="/bin/sh")).replace("\n","")
    
    check_port = subprocess.check_output("netstat -tl | grep ':963' | awk 'NR==1{print $6}'",shell=True, text=True, executable="/bin/sh").replace("\n","")
    
   
    
    msg = f" You can check stored graphics in {GRAPHS_PATH}\n by visiting http://{IP}:9630 from your Web-Browser\n you can stop the file server by kill "
    
    if check_port == "LISTEN":
        process_id = str(subprocess.check_output("ps -aux | grep ./fileservergraphs | awk 'NR==1{print $2}'",shell=True, text=True, executable="/bin/sh")).replace("\n","")
        
        check_service = subprocess.check_output("ps -p "+process_id+"| awk 'NR==2{print $4}'",shell=True, text=True, executable="/bin/sh").replace("\n","")
        
        if check_service == "fileservergraph":
            return msg+process_id
        else:
            return " please make sure that port 9630 not in use!"
    
    
    else:
        run_server = "./fileservergraphs&"
        subprocess.check_call(run_server, shell=True, text=True, executable="/bin/sh")
        
        process_id =  str(subprocess.check_output("ps -aux | grep ./fileservergraphs | awk 'NR==1{print $2}'",shell=True, text=True, executable="/bin/sh")).replace("\n","")
    
        return msg+process_id
     

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
    
    
def controling_input(input_string):
    new_float = "0."
    temp = ""
    special_chars = "/,-#_!?@\"|';:+$%=*([])}{><"
                         
    # for mixed values if input is not empty
    if ( len(input_string) != 0 ) and ( (any(s_chars in string.ascii_letters for s_chars in input_string)) or (any(s_chars in special_chars for s_chars in input_string)) ) and ( (input_string[0] != ".") or (input_string[-1] != ".") ):
        
        # for negative values
        if  input_string[0] == "-":
            input_string = input_string.replace("-","")
            
        # taking care of the floating point
        if ( input_string[0] == "." ) or ( input_string[-1] == "." ):
            input_string = input_string.replace(".","")    
        
        # for any numerical values provided, to keep it rather returning the ASCII-Code of it
        for char in input_string:
            if (re.compile('[0-9]+').search(char)):
                temp += char
                
            # use char ASCII-Code    
            else:    
                temp += str(ord(char))
                
        input_string = temp    
         
    # for empty input
    global random_flag
    random_flag = False 
    if len(input_string) == 0:
        random_string = str(round(random.uniform(0.0, 9.99),random.randint(1,9)))
        input_string = random_string
        random_flag = True
    
    # checking if input_string can be parsed as a float, and spliting input_string to create a new_float out of it  
    if isinstance(float(input_string),float):
               
        # for int input    
        if (str(float(input_string))[-2] == ".") and (str(float(input_string))[-1] == "0"):
            before_comma  = input_string.split(".")[0]
            after_comma = "0"
        
        # input is valid float    
        else:
            before_comma, after_comma = input_string.split(".")
            
        if int(before_comma) >= 1:
            new_float  += before_comma + after_comma
            return float(new_float)

        elif int(before_comma) == 0:
            new_float  += after_comma
            return float(new_float)        
    

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


def weatherInitConditions():
    headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
    cities = []
    file =  open("cities.txt")
    for city in file:
        cities.append(city)
    file.close()    
    
    global city_name 
    city_name = input(" Enter city you want to fetch weather data from> ").title()
    print(" press Enter for Random City")

    if len(city_name) != 0:
        try:
            res = requests.get(
            f'https://www.google.com/search?q={city_name}+weather&oq={city_name}+weather&aqs=chrome..69i57j0i10i512l9.3827j1j7&client=ubuntu-chr&sourceid=chrome&ie=UTF-8', headers=headers)

            soup = BeautifulSoup(res.text, 'html.parser')
            
            temperature = divider(float(soup.select('#wob_tm')[0].getText().strip()))
            humidity = divider(clean_data(soup.select('#wob_hm')[0].getText().strip())) * 10
            wind = divider(clean_data(soup.select('#wob_ws')[0].getText().strip())) * 10
            
            return temperature, humidity, wind, city_name
        except:
            return " Please enter a valid city name"
    
    # for random city
    else:
        random_city = random.randint( 0, (len(cities)-1))
        city_name = str(cities[random_city]).replace("\n","")
        
        try:
            res = requests.get(
                f'https://www.google.com/search?q={city_name}+weather&oq={city_name}+weather&aqs=chrome..69i57j0i10i512l9.3827j1j7&client=ubuntu-chr&sourceid=chrome&ie=UTF-8', headers=headers)

            soup = BeautifulSoup(res.text, 'html.parser')
            
            temperature = divider(float(soup.select('#wob_tm')[0].getText().strip()))
            humidity = divider(clean_data(soup.select('#wob_hm')[0].getText().strip())) * 10
            wind = divider(clean_data(soup.select('#wob_ws')[0].getText().strip())) * 10
        
            return temperature, humidity, wind, city_name
        
        except IndexError:
            return " Please try again", weatherInitConditions()
        



def manual_randomInitConditions():
    print()
    print(" press Enter for Random value")
    x, y, z = controling_input(input(" enter proportional value for Rate of convection x ")), controling_input(input(" enter proportional value Horizontal Temperature Variation y ")), controling_input(input(" enter proportional value Vertical Temperature Variation z "))
        
    return x, y * 10, z * 10

           
#user = input("bla ")
#print(ord(user))
#print(controling_input(user))

# print(hardwareInitConditions())
# weatherInitConditions()
# print(clean_data("17%"))
#print(fileserver())
#weatherInitConditions1()
#mood()
#print(manualInitConditions())
# fn = "graphs/lorenz"
# print(graphics_extension(fn))