#!/usr/bin/env python3

import os

# Define the menu items as a dictionary
menu_items = {
    "WindowManager Settings": "bsp",
    "Keyboard Shortcuts": "sxh",
    "Look and Feel": "lxappearance",
}

# Format the menu items as one option per line with a pipe symbol separator
menu = "\n".join([f"{key}" for key, value in menu_items.items()])

# Write the menu to a temporary file
with open("/tmp/my_menu", "w") as f:
    f.write(menu)

# Launch Rofi and pass the temporary file as input
dir = "$HOME/.config/rofi/launchers/type-7"
theme = "style-1"


rofi_command = (
    f"rofi -dmenu -i -p 'Settings Manager' -theme {dir}/{theme}.rasi < /tmp/my_menu"
)

selected_option = os.popen(rofi_command).read()
selected_option = selected_option.strip()

if selected_option in menu_items:
    command = menu_items[selected_option]
    os.system(command)
