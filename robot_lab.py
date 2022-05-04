from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim1   


%%sim_magic_preloaded --background Grey_bands -R
2   # Program to count the bands aloud
3   
4   # Start the robot moving
5   tank_drive.on(SpeedPercent(15), SpeedPercent(15))
6   
7   # Initial count value
8   count = 0
9   
10  # Initial sensor reading
11  previous_value = colorLeft.reflected_light_intensity_pc
12  
13  # Create a loop
14  while True:
15  
16      # Check current sensor reading
17      current_value = colorLeft.reflected_light_intensity_pc
18  
19      # Test when the robot has entered a band
20      if previous_value==100 and current_value < 100:
21          # When on a new band:
22          # - increase the count
23          count = count + 1
24          # - display the count in the output window
25          print(count)
26          # - say the count aloud
27          say(str(count))
28  
29      # Update previous sensor reading
30      previous_value = current_value