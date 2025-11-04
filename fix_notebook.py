import nbformat

path = "notes.ipynb"
nb = nbformat.read(path, as_version=4)

if "widgets" in nb.metadata:
    app_state = nb.metadata["widgets"].get("application/vnd.jupyter.widget-state+json", {})
    if "state" not in app_state:
        app_state["state"] = {}
        nb.metadata["widgets"]["application/vnd.jupyter.widget-state+json"] = app_state
        nbformat.write(nb, path)
        print("✅ Fixed: Added empty 'state' key to metadata.widgets.")
    else:
        print("✅ Notebook already valid.")
else:
    print("⚠️ No widget metadata found.")

