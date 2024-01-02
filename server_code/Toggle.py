import anvil.server

# Replace 'your_magic_mirror_path' with the actual path where your Magic Mirror is installed
magic_mirror_path = '/home/tommy/MagicMirror'

# Variable to track the Magic Mirror state
magic_mirror_running = False

@anvil.server.callable
def Toggle():
    global magic_mirror_running
    f'cd ~/MagicMirror && npm start'

