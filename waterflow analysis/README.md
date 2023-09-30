
<h2>Waterflow simulator: </h2>

After measuring the stopping/dropping angle on a given texture / surface, the script to simulate the movement of water droplets is relatively simple: 
 - if the angle between the xy-plane and the plane perpendicular to the surface’s normal vector at a given point is between the critical movement 
    angle and the dropping angle, the droplet is moving.
 - Outside of that range, it either stops or drops.
The Python-script created is based on the example structure provided by Park et al. (2018). ( https://www.sciencedirect.com/science/article/abs/pii/S0926580518301602 )
