
# l = ['Nabeed', 'Filza', 'Sualiha', 'Hurain', 'Zainab', 'Kashaf', 'Esa']
# for i in l:
#     print(f"Shoutout to {i}")

# import win32com.shell.shell as shell
# import win32com.shell.shellcon as shellcon

# # Get the current user's documents folder
# documents_folder = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)

# print("Documents Folder:", documents_folder)

# import pyttsx3
# l = ['Nabeed', 'Filza', 'Sualiha']
# for names in l:
#     engine = pyttsx3.init()
#     engine.say(f"Shoutout to {names}")
#     print(f"Shoutout to {names}")
# engine.runAndWait()  # Ensure all the speeches are spoken before the program exits



import pyttsx3 as p

l = ['Nabeed', 'Filza', 'Sualiha', 'Hurain', 'Zainab', 'Kashaf']

for name in l:
    engine = p.init()
    print(f"Shoutout to {name}")
    engine.say(f"Shoutout to {name}")
    engine.runAndWait()   # Ensure the speech for this name is spoken before moving to the next one. This line ensure ke phele ek baar print or speak ensure krao then dusre per move kro.
engine.runAndWait() # Ensure all the speeches are spoken before the program exits. means ye ensure krrha ke sb ke lie print or speak hochuka hai.
