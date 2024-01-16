import tkinter as tk
from plyer import notification  # Make sure to install plyer using: pip install plyer

def show_notification():
    title = entry_title.get()
    message = entry_message.get()
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will stay for 10 seconds
    )

# Create the main window
root = tk.Tk()
root.title("Desktop Notifier")
root.geometry("300x200")
root.configure(bg='white')

# Create widgets
label_title = tk.Label(root, text="Notification Title:", bg='white')
entry_title = tk.Entry(root)
label_message = tk.Label(root, text="Notification Message:", bg='white')
entry_message = tk.Entry(root)
button_notify = tk.Button(root, text="Notify", command=show_notification, bg='blue', fg='white')

# Place widgets on the window
label_title.pack(pady=5)
entry_title.pack(pady=5)
label_message.pack(pady=5)
entry_message.pack(pady=5)
button_notify.pack(pady=10)

# Start the main loop
root.mainloop()