import os
from pathlib import path
import logging


logging.basicConfig(level=logging.INFO,format= '[%(ascitime)s]: %(message)s:')
project_name = 'textsummarizer'
list_of_files = +[
".github/workflow/.gitkeep",
f"src/{project_name}/_init_.py",
f"src/{project_name}/component/_init_.py",
f"src/{project_name}/utility/_init_.py",
f"src/{project_name}/utility/common.py",
f"src/{project_name}/logging/_init_.py",
f"src/{project_name}/config/_init_.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipelline/_init_.py",
f"src/{project_name}/entity/_init_.py",
f"src/{project_name}/constant/_init_.py",
"config/config.yaml",
"params.yaml",
"app.py",
"main.py",
"Dockerfile",
"requirements.txt",
"setup.py",
"research/trails.ipynb"
]
for filepath in list_of_files:
  filepath = path(filepath)
  filedir, filename = os.path.split(filepath)

if filedir != "":
  os.makedirs(filedir, exit_ok=True)
  logging.info(f"creating directory:{filedir} for the file {filename}")
    
 if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
    with open(filepath, 'w') as f:
    pass 
    logging.info(f"creating empty file: {filepath}")
  

else:
  logging.info(f"{filename} is already there")






