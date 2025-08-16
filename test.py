import platform
import os

print("✅ Termux + Python is working!")
print("System:", platform.system())
print("Release:", platform.release())
print("Files in workspace:", os.listdir("."))
