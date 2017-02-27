from yaml import load


def print_app(app):
    print("* [{}]({}) - {}".format(app["name"], app["url"], app["description"]))


with open('cli-apps.yaml', 'r') as yf:
    data = load(yf)
    # print(data)
    apps = data["apps"]
    for cat in apps:
        print(cat)
        for app in apps[cat]:
            print_app(app)
