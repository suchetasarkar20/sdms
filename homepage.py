import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow library for handling images
from gtts import gTTS  # Text-to-Speech
import pygame  # Audio playback
import os


# Function to handle the Registration/Login button click
def on_registration_login_click():
    messagebox.showinfo("Registration/Login", "Navigate to Registration/Login Page")


# Function to handle the Chatroom button click
def on_chatroom_click():
    messagebox.showinfo("Chatroom", "Navigate to Chatroom")


# Function to play the introductory voice message
def play_welcome_voice():
    voice_text = "Welcome to Uni-Hub"  # The text for the voice message
    audio_path = "welcome_message.mp3"  # File to store the generated voice
    
    # Generate the voice message
    if not os.path.exists(audio_path):  # Check if the audio file already exists
        tts = gTTS(text=voice_text, lang='en')
        tts.save(audio_path)
    
    # Play the voice message
    pygame.mixer.init()  # Initialize the mixer
    pygame.mixer.music.load(audio_path)  # Load the audio file
    pygame.mixer.music.play()  # Play the audio


# Create the main application window
root = tk.Tk()
root.title("UNI-HUB")

# Set the window dimensions
root.geometry("400x300")  # Set the window size

# Play the voice message after a short delay
root.after(500, play_welcome_voice)  # Delay to ensure the GUI is initialized

# Load the background image
bg_image_path = "uni-hub.jpg"  # Replace with your image path
bg_image = Image.open(bg_image_path)
bg_image = bg_image.resize((400, 300), Image.Resampling.LANCZOS)  # Resize to fit
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Canvas widget to hold the background image
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill=tk.BOTH, expand=True)  # Expand to fill the window

# Display the background image on the canvas
canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)  # Anchor top-left corner

# Create a welcome label and buttons
welcome_label = tk.Label(
    root,
    text="UNI-HUB",
    font=("Garamond", 16),
    bg='white'  # Background color for visibility
)
registration_login_button = tk.Button(
    root,
    text="Registration/Login",
    command=on_registration_login_click,
    width=20,  # Width of the button
)
chatroom_button = tk.Button(
    root,
    text="Chatroom",
    command=on_chatroom_click,
    width=20,
)

# Place the widgets on the canvas
canvas.create_window(200, 80, window=welcome_label)  # Centered horizontally
canvas.create_window(200, 150, window=registration_login_button)
canvas.create_window(200, 200, window=chatroom_button)

# Start the application event loop
root.mainloop()
