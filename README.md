# chaos
<h2>CLI Tool to plot Lorenz Attractor</h2>

<p>This Tool aims to create an image of the Butterfly shaped lorenz-attractor. In order to portrait the Butterfly Effect on a graphic plot, the Attractor needs Initial Conditions to Sensitively Debend on so that the Chaos would settle into Determination by taking Unpredictable Patterns.</p>

<b>Supported Initial Conditions:</b> 
<ol>
  <li>Lorenz Initial Conditions <details>Rate of convection proportional value <em>x</em> = 0<br> Horizontal Temperature Variation proportional value <em>y</em> = 1<br> Vertical Temprature Variation proportional value <em>z</em> = 1,05</details></li> 
  
  <li>Hardware based Initial Conditions <details>Rate of convection proportional value <em>x</em> = CPU-Temprature<br> Horizontal Temperature Variation proportional value <em>y</em> = Memory-Load<br> Vertical Temprature Variation proportional value <em>z</em> = Recived Network Packets</details></li> 

  <li>Weather based Initial Conditions <details>Rate of convection proportional value <em>x</em> = City-Temprature<br> Horizontal Temperature Variation proportional value <em>y</em> = City-Humidity<br> Vertical Temprature Variation proportional value <em>z</em> = City Wind Speed</details></li> 

</ol>

# Motive behind this repo and general Infos
<details>
  <p>Nothing fancy here, while I'am trying to understand the chaos theory by reading <em>CHAOS by James Gleick</em></p>
  <p>And also while I' am learning <em>golang</em></p>
  <p>I thought to look up a <em>python</em> script that can plot the Lorenz Attractor, by tweaking the Initial Conditions you get to influence the graphic result<p>
  <p>Under the influence of the tragidy of me still not landing a job after my graduation, I picked myself up with the programing language I am comfortable  with, <em>python</em> and its cool dependencies libraries </p>
  <p>i started writing funcs.py to integrate user-input to the orginal lorenz_attractor.py plotter script</p>
  <p>and thought about two ways to get random Initial values for the plot, <b>Hardware readings</b> and <b>Weather readings</b> from a random city based on user input.</p><p>in order to get a similiar attractor to Lorenzs, the fetched initial positive valus has to go through under simple math to keep them near to Lorenzs initial variables values where <em>x</em> < 1 & <em>y</em>, <em>z</em> >= 1 </p> 
</details>

# Whats on this repo
<ul>
  <li><b>chaosenv</b> python enviroment Directory to store dependicies files</li>
  <li><b>graphs</b> Directory to store plotted graphics</li>
  <li><b>filesservergraphs</b> pre-build golang Executable to http serve <em>graphs</em> dir on port <b>9630</b></li>
  <li><b>funcs.py</b> functions to integrate user-input</li>
  <li><b>lorenz_attractor.py</b> plotter</li>
</ul>

# Deployment
<h3>Requierments:</h3>
<ul>
  <li>GNU/LINUX System</li>
  <li>python3</li>
  <li>python3-pip</li>
  <li>python3-venv</li>
</ul>
<h3>get it running:</h3>
<ul>
  <li><b>fork n clone</b> [On-Premises] <details><p>fork this repo and clone it localy</p><p>from your local machine:</p><pre><code>
    $ cd chaos
    $ source chaosenv/bin/activate
    (chaosenv)$ python3 lorenz_attractor.py
  </pre></code>
  <p>in case of Error Module not found:<br>make sure that the venv is activated and install the dependencies<pre><code>
    (chaosenv)$ pip install -r requierments.txt
  </pre></code></p></details></li>
</ul>
