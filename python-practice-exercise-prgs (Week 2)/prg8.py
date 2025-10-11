def init_component(name, **settings):
    print(f"Component Name: {name}")

    for setting, value in settings.items():
        print(f"{setting}: {value}")

init_component("Database", host="localhost", port=5432, user="admin")
