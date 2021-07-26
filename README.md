
# Installation Instructions
## macOS
Just run `./install_mac.sh`.
You can create an app that wraps the Python script using Automator - (File->New->Application->Run Shell Script->enter bash code that runs the Python script).
Run the app from Spotlight to quickly change displays and toggle KVM.

## Windows
Download ControlMyMonitor from [here](https://www.nirsoft.net/utils/controlmymonitor.zip).
Install. In `to_mac.py`', make sure `CONTROLMYMONITOR_UTIL` path is correctly pointing to `ControlMyMonitor.exe`.
Create a shortcut to `to_mac.py`, name it `to_mac` and put it somewhere in the path. Run from Win-R->to_mac.
