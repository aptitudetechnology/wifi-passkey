#!/usr/bin/env python3
import socket
import json
import subprocess

def get_mac_address(interface):
  try:
    output = subprocess.check_output(["ip", "addr", "show", interface]).decode("utf-8")
    mac_address = output.split("link/ether")[1].split()[0]
    return mac_address
  except subprocess.CalledProcessError as e:
    print(f"Error getting MAC address: {e}")
    return None

def register_device(interface):
  mac_address = get_mac_address(interface)
  hostname = socket.gethostname()

  if not mac_address:
    print("Error getting MAC address")
    return

  data = {
    "mac_address": mac_address,
    "hostname": hostname
  }

  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      knock_knock = b"knock knock"  # Define the message to send
      s.connect(("wpk-server.local", 12345))  # Replace 12345 with the actual server port
      s.sendall(knock_knock)
      print("Sending:", knock_knock.decode())  # Print the message before sending
      response = s.recv(1024)
      print(response.decode())
  except Exception as e:
    print(f"Error connecting to server: {e}")

if __name__ == "__main__":
  interface = input("Enter interface name (e.g., eth0): ")
  register_device(interface)
