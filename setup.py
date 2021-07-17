from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "covid",
    version = "1",
    description = "Mapping of result covid test and clustering in yaounde",
    executables = [Executable("manage.py")],
)