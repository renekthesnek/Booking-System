import os

ui_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".ui"):
            ui_files.append(os.path.join(root, file))

for ui_file in ui_files:
    py_file = os.path.splitext(ui_file)[0] + ".py"
    os.system("python -m PyQt5.uic.pyuic {} -o {}".format(ui_file, py_file))
    print("Translated {} to {}".format(ui_file, py_file))

