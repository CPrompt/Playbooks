from i3pystatus import Status
from i3pystatus import get_module
from i3pystatus.updates import dnf
import subprocess


status = Status(standalone=True)

from colors import *

# Displays clock like this:
status.register("clock",
#  Note: this config requires the gsimplecal package to be installed
    hints = {"markup": "pango"},
    format = " %a %d %b <span color=\"#fff\">  </span>  %H:%M:%S %P <span color=\"#fff\"> </span> ",
    color = color_clock,
    on_leftclick = ["gsimplecal"],)

# Display updates

status.register("updates",
                        format = "Updates: {count}",
                        color = updates,
                        format_no_updates = "No updates",
                        color_no_updates = color_no_updates,
						format_working = None,
						color_working = None,
                        backends = [dnf.Dnf()],)

# Shows disk usage of /home/curtis/
status.register("disk",
		path="/home/curtis/",
		hints = {"markup": "pango"},
		format = "<span color=\"#fff\"> :</span> {used}/{total}G [{avail}G]",
		color = color_disk,)



# Shows internet connection status
status.register("online",
    format_online = '',
    color = color_online,
    format_offline = '',
    color_offline = color_offline,)


# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces

status.register("network",
    interface="enp2s0",
    hints = {"markup": "pango"},
    format_up="<span color=\"#fff\"> :</span> {v4} ",
    color_up = color_network_up,
    color_down = color_network_down,)



status.run()
