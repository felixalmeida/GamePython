import cx_Freeze
executables = [cx_Freeze.Executable(
    script="jogo.py", icon="assets/bolaIcon.ico")]

cx_Freeze.setup(
    name="Fut Imed",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]
                           }},
    executables=executables
)
