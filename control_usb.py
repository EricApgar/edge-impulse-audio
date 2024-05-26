import subprocess


def control_usb_power(bus, state: str):
    '''
    Control the power of a USB port.

    :param bus: The USB bus (e.g., '1-1').
    :param port: The USB port number (e.g., '1').
    :param state: The desired power state ('on' or 'off').

    Note: On the Raspberry Pi 4B, all the USB ports are linked, and so the power status of
    all the ports is turned on or off together. So the "port" argument is not needed (or 
    doesn't affect anything).
    '''

    # command = f"sudo uhubctl -l {bus} -p {port} -a {'on' if state == 'on' else 'off'}"
    command = f"sudo uhubctl -l {bus} -a {'on' if state == 'on' else 'off'}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"USB ports now {'on' if state == 'on' else 'off'}.")
    else:
        print(f"Failed to set USB ports to {'on' if state == 'on' else 'off'}.")
        print(result.stderr)

    return


# # Example usage
# bus = '1-1'  # Internal USB 2.0 hub
# port = '1'   # Replace with the actual port number you want to control

# # Turn on the USB port
# control_usb_power(bus, port, 'on')

# # Wait for 5 seconds
# import time
# time.sleep(5)

# # Turn off the USB port
# control_usb_power(bus, port, 'off')
