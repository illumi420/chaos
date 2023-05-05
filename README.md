# chaos
<h1>CLI Tool to plot Lorenz Attractor</h1>

<p>This Tool aims to create an image of the Butterfly shaped lorenz-attractor in order to portrait the Butterfly Effect on a graphic plot, the Attractor needs Initial Conditions to Sensitively Debend on so that the Chaos would settle into Determination by taking Unpredictable Patterns.</p>

<b>Supported Initial Conditions:</b> 
<ol>
  <li>Lorenz Initial Conditions <details>Rate of convection proportional value <em>x</em> = 0<br> Horizontal Temperature Variation proportional value <em>y</em> = 1<br> Vertical Temprature Variation proportional value <em>z</em> = 1,05</details></li> 
  
  <li>Hardware based Initial Conditions <details>Rate of convection proportional value <em>x</em> = CPU-Temprature<br> Horizontal Temperature Variation proportional value <em>y</em> = Memory-Load<br> Vertical Temprature Variation proportional value <em>z</em> = Recived Network Packets</details></li> 

  <li>Weather based Initial Conditions <details>Rate of convection proportional value <em>x</em> = City-Temprature<br> Horizontal Temperature Variation proportional value <em>y</em> = City-Humidity<br> Vertical Temprature Variation proportional value <em>z</em> = City Wind Speed</details></li> 

</ol>

# Motive behind this repo
<details>
  <p>Nothing fancy here, while I'am trying to understand the chaos theory by reading <em>CHAOS by James Gleick</em></p>
  <p>And also while I' am learning Golang</p>
  <p>I thought to look up a python script that can plot the Lorenz Attractor, by tweaking the Initial Conditions you get to influence the graphic result<p>
  <p>Under the influence of the tragidy of me still not landing a job after my graduation, I picked myself up with the programing language I am comfortable  with, <b>python</b> and its cool dependencies libraries </p>
  <p>i started writing funcs.py to integrate user-input to the orginal lorenz_attractor.py plotter script</p>
  <p>and thought about two ways to get random Initial values for the plot, <b>Hardware readings</b> and <b>Weather readings</b> from a random city based on user input.</p><p>in order to get a similiar attractor to Lorenzs, the random initial positive valus has to go through under simple math to keep them near to Lorenzs initial variables values where <em>x</em> < 1 & <em>y</em>, <em>z</em> >= 1 </p> 
</details>



