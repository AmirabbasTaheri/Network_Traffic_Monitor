# Network Traffic Monitor

A simple Python GUI application to monitor network usage over time using `tkinter` and `psutil`.

## 🖥️ Overview

This application displays the total network traffic (sent + received) on your system every **10 seconds** in a scrollable text window.

The interface is built with `tkinter`, and traffic data is fetched using the `psutil` library. Monitoring runs on a separate thread to keep the UI responsive.

## 📸 Screenshot

<img width="335" height="367" alt="image" src="https://github.com/user-attachments/assets/f59c0748-6690-456c-9521-dbe550d41692" />

## 🚀 Features

- Displays network traffic usage in MB
- Updates every 10 seconds
- Scrollable log of usage history
- Multithreaded traffic monitoring for a smooth UI

## 🧰 Requirements

Make sure you have Python 3.x installed.

Install required Python library:

```bash
pip install psutil
tkinter is included with most standard Python distributions.

▶️ How to Run
Save the Python code in a file (e.g. network_monitor.py) and run it:

python network_monitor.py
A window will open showing the network traffic log updating every 10 seconds.

📁 File Structure

network_monitor.py   # Main application script
README.md            # This file
🧠 How It Works
At launch, the app records the total bytes sent/received.

Every 10 seconds, it calculates how many new bytes have been transferred.

Converts bytes to MB and appends the info to a text widget.

Uses threading to avoid freezing the UI.

📄 License
This project is licensed under the MIT License.
