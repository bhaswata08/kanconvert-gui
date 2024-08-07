from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "PyPDF2", "docx"],
    "include_files": ["src/"],
    "excludes": ["tkinter.test", "tkinter.tix", "tkinter.ttk"],
    "optimize": 2
}

setup(
    name="Kanconvert",
    version="0.1",
    description="Converts ASCII to Kannada",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="Win32GUI", target_name="Kanconvert.exe")]
)
