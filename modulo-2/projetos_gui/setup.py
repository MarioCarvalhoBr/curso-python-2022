import cx_Freeze
import sys
import os
import pandas
import numpy

from PyQt6 import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py", base=base, icon="icone.ico")]
cx_Freeze.setup(
    name="Programa 1",
    options={"build_exe": {"packages": ["PyQt6.QtCore",
                                        "PyQt6.QtGui",
                                        "PyQt6.QtWidgets",
                                        "pandas",
                                        "numpy",
                                        "os",
                                        "sys"],
                           "include_files": ["tela.ui",
                                             "banco.xlsx",
                                             "icone.ico"]}},
    version="0.01",
    author='Mario...',
    description="Descricao aqui",
    executables=executables
)
