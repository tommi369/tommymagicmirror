import anvil.server

# Replace 'your_magic_mirror_path' with the actual path where your Magic Mirror is installed
magic_mirror_path = '/home/tommy/MagicMirror'

# Variable to track the Magic Mirror state
magic_mirror_running = False

@anvil.server.callable
def Toggle():
    global magic_mirror_running

    try:
        if not magic_mirror_running:
            # Magic Mirror is not running, start it
            # Uncomment the line below and replace 'your_start_command' with the actual command to start your Magic Mirror
            # os.system('your_start_command')
            f'cd ~/MagicMirror && npm start'
            magic_mirror_running = True
            return {"status": "Magic Mirror started"}
        else:
            # Magic Mirror is running, stop it
            # Uncomment the line below and replace 'your_stop_command' with the actual command to stop your Magic Mirror
            # os.system('your_stop_command')
            magic_mirror_running = False
            return {"status": "Magic Mirror stopped"}

    except Exception as e:
        return {"error": str(e)}

