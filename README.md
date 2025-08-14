# How to setup the Project Analyser (via Command Prompt Commands)
By using pre-packaged wheels, this will not require an internet connection.

---
### 0. Copy the the J drive folder into the location you want to install, and including all its contents
`J:\RND\Vadan Khan\liv-analyser-vk-deployment`

---
### 1. Go to your project root folder (replace this path with whatever your path is)
`cd /d C:\liv-analyser-vk`

---
### 2. Create a virtual environment (requires python installed + added to PATH)
If installed via software centre this "adding to path" will be setup.

`python -m venv .venv`

---
### 3. Activate the virtual environment
`Call .venv\Scripts\activate.bat`

---
### 4. Install packages using only the local wheels folder
`pip install --no-index --find-links=wheels -r requirements.txt`


<br>
<br>
<br>

# How to Run Deployment Build  

### 1. Configure the Paths in `config.py`
Here you can configure where
- the code expects files to appear ("MONITORED_PATH")
- the code slowly writes the GTX files ("GTX_RESULTS_PATH")
- the code slowly writes the Levee files ("LEVEE_RESULTS_PATH")
- the code will output the completed levee_files if a "final-recipe" recipe is found ("LEVEE_FOLDER")
- the location of the levee.exe ("LEVEE_EXE_PATH")
- the log name and path ("LOG_NAME", "LOG_PATH")
- the version string of the code (appears in exports as a string), ("VERSION")

---
### 2. Activate the code by clicking `photonic_analysis.bat`
this will open a cmd window that by default minimises (this may look like it closed but it is just minimised if in your taskbar).

---
### 3. Add an appropriate raw file into the MONTIORED_FOLDER path, and watch the analysis occur
- cmd output is mirrored live into the log file
- the writing of the exports is chunked as the code runs.
- the final levee shunting only occurs when the full file is written
