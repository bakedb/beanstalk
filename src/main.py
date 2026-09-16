import tomllib

def setup():
    print("Empty or missing config file detected.")
    branding = 'instance_name = "Beanstalk"\ncurrency_name = "beans"'
    with open("branding.toml", "w") as f:
        f.write(branding)
    print("branding.toml has been initialized. Please customize it, then run the script again.")

try:
    with open("branding.toml", "rb") as f:
        branding = tomllib.load(f)
        if not branding:
            setup()
except FileNotFoundError:
    setup()