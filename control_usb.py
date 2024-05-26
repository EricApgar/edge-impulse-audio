import subprocess


def control_usb_power(bus, port, state):
    """
    Control the power of a USB port.

    :param bus: The USB bus (e.g., '1-1').
    :param port: The USB port number (e.g., '1').
    :param state: The desired power state ('on' or 'off').
    """
    command = f"sudo uhubctl -l {bus} -p {port} -a {'on' if state == 'on' else 'off'}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"USB port {port} on bus {bus} is now {'on' if state == 'on' else 'off'}.")
    else:
        print(f"Failed to set USB port {port} on bus {bus} to {'on' if state == 'on' else 'off'}.")
        print(result.stderr)


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
