## Environment Setup (Windows)
### Installing Python
Download Python:
* Go to the official Python website.
* Click on the "Downloads" tab and choose the version suitable for your operating system (Windows, macOS, or Linux).

Install Python:
* Follow the installation instructions provided on the website.

### Setting up a Development Environment
Text Editor/IDE:
* Choose a text editor or an Integrated Development Environment (IDE) for writing Python code. Some popular choices include Visual Studio Code, PyCharm, and Jupyter Notebooks.  

_I ended up using Visual Studio Community Edition_

### Run Python scripts on Windows, follow these steps:

    Create the Python Script:
        Open Notepad++ and write your "Hello, World!" script.
        Save the file with a .py extension, for example, hello_world.py. Make sure to choose "All types" in the "Save as type" dropdown.

    Open Command Prompt:
        Press Win + R to open the Run dialog.
        Type cmd and press Enter to open the Command Prompt.

    Navigate to the Script's Directory:
        Use the cd command to navigate to the directory where you saved your Python script. For example:

        bash

    cd path\to\your\script\directory

Run the Script:

    Once you're in the script's directory, type the following command to run the script:

    bash

python hello_world.py

If your Python installation is in the system PATH, this command should work. If not, you might need to provide the full path to the Python executable, like:

bash

        C:\Path\to\python.exe hello_world.py

        If you've set up Python correctly, you should see "Hello, World!" printed in the Command Prompt.

That's it! This is a simple way to run Python scripts from the command line. As you progress, you might explore integrated development environments (IDEs) like Visual Studio Code, PyCharm, or Jupyter Notebooks, which provide a more user-friendly interface for coding and running Python scripts.
Thanks, worked perfectly, I have my solution ready, how do I denote code blocks in this chat?
ChatGPT

You're welcome! To denote code blocks in this chat, you can use triple backticks (```) before and after your code. For example:

```python
print("Hello, World!")
```

Replace the backslashes with the actual backticks. This will format your text as a code block, making it easier to read and understand. Feel free to share your solution using this format, and I'll provide feedback!