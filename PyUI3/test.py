import PyUI3

# Create a window
window = PyUI3.ApplicationWindow()

# Add some widgets
label = PyUI3.Label(Content="Print Hello World!")
button = PyUI3.Button(Content="Do it now!")


window.add()
# Define a callback function for the button
def button_click():
    print("Hello World!")

# Bind the callback to the button
button.on_click = button_click

# Start the main loop
window.run()
