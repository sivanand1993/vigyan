
# then call the default open method described above

# python callable function
# import ctypes
# WS_EX_TOPMOST = 0x40000
# windowTitle = "Python Windows Message Box Test"
# message = "Hello, world! This Message box was created by calling the Windows API using the ctypes library."
# ctypes.windll.user32.MessageBoxExW(None, message, windowTitle, WS_EX_TOPMOST)
import webbrowser


def print_hello():
	# ctypes.windll.user32.MessageBoxExW(None, message, windowTitle, WS_EX_TOPMOST)
	return webbrowser.open_new_tab('chrome')

print_hello()
