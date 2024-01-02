from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        try:
            # Replace 'your_magic_mirror_path' with the actual path where your Magic Mirror is installed.
            magic_mirror_path = '/home/tommy/MagicMirror'

            # Check if Magic Mirror is currently running
            status_command = f'cd {magic_mirror_path} && npm list magicmirror'
            status_result = subprocess.run(status_command, shell=True, capture_output=True, text=True)

            if 'magicmirror not installed' in status_result.stderr:
                # Magic Mirror is not running, start it
                start_command = f'cd {magic_mirror_path} && npm start'
                subprocess.run(start_command, shell=True, check=True)
                print("Magic Mirror has been started.")

            else:
                # Magic Mirror is running, stop it
                stop_command = f'cd {magic_mirror_path} && npm stop'
                subprocess.run(stop_command, shell=True, check=True)
                print("Magic Mirror has been stopped.")

        except subprocess.CalledProcessError:
            print("Error: Unable to execute the subprocess.")

if __name__ == "__main__":
    pass
