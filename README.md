# chaos
<h2>CLI Tool to plot Lorenz Attractor</h2>

<p>This Tool aims to create an image of the Butterfly shaped lorenz-attractor. In order to portrait the Butterfly Effect on a graphic plot, the Attractor needs Initial Conditions to Sensitively Debend on so that the Chaos would settle into Determination by taking Unpredictable Patterns.</p>
<details>
<summary><em>where the math is</em></summary> <em>to be found in file <b>lorenz_attractor.py</b> lines 17 to 46 is where the Lorenz ordinary differential equations constansts and variables are declared and described.</em> <em>lines from 67 to 81 is where the 'ode's are defined and solved</em>
</details>

<b>Supported Initial Conditions:</b> 
<ol>
  <li>Lorenz Initial Conditions <details><summary>variables</summary>Rate of convection proportional value <em>x</em> = 0<br> Horizontal Temperature Variation proportional value <em>y</em> = 1<br> Vertical Temprature Variation proportional value <em>z</em> = 1,05</details></li> 
  
  <li>Hardware based Initial Conditions <details><summary>variables</summary>Rate of convection proportional value <em>x</em> = CPU-Temprature<br> Horizontal Temperature Variation proportional value <em>y</em> = Memory-Load<br> Vertical Temprature Variation proportional value <em>z</em> = Recived Network Packets</details></li> 

  <li>Weather based Initial Conditions <details><summary>variables</summary>Rate of convection proportional value <em>x</em> = City-Temprature<br> Horizontal Temperature Variation proportional value <em>y</em> = City-Humidity<br> Vertical Temprature Variation proportional value <em>z</em> = City Wind Speed</details></li> 

</ol>

# Motive behind this repo and general Infos
<details>
<summary><b>more...</b></summary>  
  <p>Nothing fancy here, while I'am trying to understand the chaos theory by reading <em>CHAOS by James Gleick</em></p>
  <p>And also while I' am learning <em>golang</em></p>
  <p>I thought to look up a <em>python</em> script that can plot the Lorenz Attractor, it sounded like fun as by tweaking the Initial Conditions you get to influence the graphic result<p>
  <p>Under the influence of the tragidy of me still not landing a job after my graduation, I picked myself up with the programing language I am comfortable  with, <em>python</em> and its cool dependencies and modules</p>
  <p>i started writing funcs.py to integrate user-input to the orginal lorenz_attractor.py plotter script
  and thought about two ways to get random Initial values for the plot, <b>Hardware readings</b> and <b>Weather readings</b>, the latter based on http request fetched data for a city based on user input.</p><p>in order to get a similiar attractor to Lorenzs, the fetched initial positive valus has to go through under simple math to keep them near to Lorenzs initial variables values where <em>x</em> < 1 & <em>y</em>, <em>z</em> >= 1 </p> 
</details>

# Whats on this repo
<details>
<summary><b>files and dirs</b></summary><br>
  <ul>
  <li><b>__pycache__ </b> directory that is created by the Python interpreter when it imports a module. It contains the compiled bytecode of the module, which can be used to speed up subsequent imports of the same module</li>
  <li><b>.vscode</b> has the settings.json file for your vscode to automate <em>chaosenv</em> activation while running <em>lorenz_attractor.py</em></li>
  <li><b>chaosenv</b> Python enviroment directory to store requierd modules files</li>
  <li><b>graphs</b> directory to store plotted graphics</li>
  <li><b>filesservergraphs</b> pre-build Golang Executable to <b>HTTP</b> serve files in <em>graphs</em> directory on port <u>9630</u></li>
  <li><b>funcs.py</b> functions to integrate user-input</li>
  <li><b>lorenz_attractor.py</b> plotter</li>
 </ul>
</details>

# Deployment
<details>
<summary><b>Requirements</b></summary>
  <ul>
  <li>GNU/LINUX System</li>
  <li>python3</li>
  <li>python3-pip</li>
  <li>python3-venv</li>
</ul>
</details>  
<h3>get it running:</h3>
<details>
  <summary><b>fork n clone</b> [On-Premises]</summary> <p>fork this repo and clone it localy</p><p>from your local machine:</p><pre><code>
    $ cd chaos
    $ source chaosenv/bin/activate
    (chaosenv)$ python3 lorenz_attractor.py
  </pre></code>
  <p>in case of Error Module not found:<br>make sure that the venv is activated and install the dependencies<pre><code>
    (chaosenv)$ pip install -r requierments.txt
  </pre></code></p>
  <p>in case of other errors, make sure you have both <em>python3-pip</em> and <em>python3-venv</em> packages installed on your system</p>
  <pre><code>
    $ sudo apt install python3-pip python3-venv
    $ python3 -m pip install virtualenv
    $ python3 -m venv ~/chaos/chaosenv
    $ source chaosenv/bin/activate
    (chaosenv)$ pip install --upgrade pip
    (chaosenv)$ pip3 install -r requierments.txt
    (chaosenv)$ pip3 install --upgrade matplotlib
    (chaosenv)$ python3 lorenz_attractor.py
  </pre></code>
  <h3>NOTE:</h3><p>Don't forget to kill fileservergraphs process</p>
</details>
