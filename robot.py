%%sim_magic_preloaded --background Coloured_bands -R
# Program to count the bands aloud

# Start the robot moving
tank_drive.on(SpeedPercent(15), SpeedPercent(15))

# Initial count value
count = 0

# Initial sensor reading
previous_value = colorLeft.reflected_light_intensity_pc

# Create a loop
while True:

    # Check current sensor reading
    current_value = colorLeft.reflected_light_intensity_pc

    # Test when the robot has entered a band
    if previous_value==100 and current_value < 100:
        # When on a new band:
        # - increase the count
        count = count + 1
        # - display the count in the output window
        print(count)
        # - say the count aloud
        say(str(count))
        if count == 4:
            tank_drive.off()
        
        

    # Update previous sensor reading
    previous_value = current_value
