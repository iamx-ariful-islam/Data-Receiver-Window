import time
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


# start button action with thread
def start_action():
    print('Starting data receive processing.....!')
    if network_serial_var.get():
        print(f'Connected: {port_name_combobox.get()}|{baudrate_combobox.get()}')
    else:
        print(f'Connected: {host_entry.get()}|{port_entry.get()}')


# create txt file
def create_file():
    data = byte_text_box.get('0.0', tk.END).strip()
    if data:
        flname = time.strftime('%d%m%Y%I%M%S')+'.txt'
        with open(flname, 'w') as fl:
            fl.write(data)


# set network or serial option
def network_serial_option():
    if network_serial_var.get():
        host_label.config(text='Serial Port Name')
        host_entry.grid_forget()
        port_name_combobox.grid(row=0, column=1, padx=15, pady=4, sticky='ew')
        port_label.config(text='Bytes Size | Baudrate')
        port_entry.grid_forget()
        baudrate_combobox.grid(row=1, column=1, padx=15, pady=4, sticky='ew')
    else:
        host_label.config(text='Network Host Address')
        port_name_combobox.grid_forget()
        host_entry.grid(row=0, column=1, padx=15, pady=5, sticky='ew')
        port_label.config(text='Bytes Size | Port Number')
        baudrate_combobox.grid_forget()
        port_entry.grid(row=1, column=1, padx=15, pady=5, sticky='ew')
    

# create gui window
window = tk.Tk()
window.title('Data Receiver')

# network host address or serial port name
host_label = tk.Label(window, text='Network Host Address')
host_label.grid(row=0, column=0, padx=15, sticky='w')
host_entry = tk.Entry(window)
host_entry.grid(row=0, column=1, padx=15, pady=5, sticky='ew')

# serial port name combobox
ports = []
for x in range(1, 101): ports.append(f'COM{x}')
selected_port = tk.StringVar(window)
selected_port.set(ports[0])  # set the default selected port
port_name_combobox = ttk.Combobox(window, width=10, textvariable=selected_port, values=ports)

# port number label and entry
port_label = tk.Label(window, text='Bytes Size | Port Number')
port_label.grid(row=1, column=0, padx=15, sticky='w')
port_entry = tk.Entry(window)
port_entry.grid(row=1, column=1, padx=15, pady=5, sticky='ew')

# baudrate combobox
baudrate = ['300', '1200', '2400', '4800', '9600', '14400', '19200', '28800', '38400', '57600', '115200', '230400', '460800', '921600']
selected_speed = tk.StringVar(window)
selected_speed.set(baudrate[4])  # set the default selected port
baudrate_combobox = ttk.Combobox(window, width=10, textvariable=selected_speed, values=baudrate)

# byte size
byte_size = tk.Entry(window, width=12)
byte_size.grid(row=1, column=0, sticky='e')
byte_size.insert(0, '1024')

# byte data text box
byte_text_box = scrolledtext.ScrolledText(window, width=70, height=10)
byte_text_box.grid(row=2, column=0, columnspan=2, padx=(15, 0), pady=10)

# patient id label and entry
patient_id_label = tk.Label(window, text='Patient ID')
patient_id_label.grid(row=3, column=0, padx=15, sticky='w')
patient_id_entry = tk.Entry(window)
patient_id_entry.grid(row=3, column=1, padx=15, pady=5, sticky='ew')

# test name label and entry
test_name_label = tk.Label(window, text='Test Name')
test_name_label.grid(row=4, column=0, padx=15, sticky='w')
test_name_entry = tk.Entry(window)
test_name_entry.grid(row=4, column=1, padx=15, pady=5, sticky='ew')

# result value label and rntry
result_value_label = tk.Label(window, text='Result Value')
result_value_label.grid(row=5, column=0, padx=15, sticky='w')
result_value_entry = tk.Entry(window)
result_value_entry.grid(row=5, column=1, padx=15, pady=5, sticky='ew')

# create logs txt output file
txt_button = tk.Button(window, text='Create logs file', width=15, cursor='hand2', command=create_file)
txt_button.grid(row=6, column=0, padx=(15, 0), sticky='w')

server_client_var = tk.IntVar(window)
server_client_var.set(1)
server_client = tk.Checkbutton(window, text='Server Mode', variable=server_client_var, onvalue=1, offvalue=0, cursor='hand2')
server_client.grid(row=6, column=0, padx=(0, 15), sticky='e')

network_serial_var = tk.IntVar(window)
network_serial = tk.Checkbutton(window, text='Serial Mode', variable=network_serial_var, onvalue=1, offvalue=0, cursor='hand2', command=network_serial_option)
network_serial.grid(row=6, column=1, padx=(10, 0), sticky='w')

# start button
start_button = tk.Button(window, text='Start Process', width=14, cursor='hand2', command=start_action)
start_button.grid(row=6, column=1, padx=(0, 15), pady=10, sticky='e')

# listen label
listen_label = tk.Label(window, text='Not Listen')
listen_label.grid(row=7, column=0, padx=(15, 0), sticky='w')

# connect label
connect_label = tk.Label(window, text='Not connected')
connect_label.grid(row=7, column=1, sticky='w')

# connect ip
connect_ip = tk.Label(window, text='Not available')
connect_ip.grid(row=7, column=1, padx=(0, 15), pady=10, sticky='e')


x_axis = (window.winfo_screenwidth() / 2) - (600 / 2)
y_axis = (window.winfo_screenheight() / 2) - (410 / 2)
window.geometry('%dx%d+%d+%d' % (600, 410, x_axis, y_axis-50))
window.resizable(0, 0)
window.mainloop()