from yaml import load


def print_app(app):
    print("* [{}]({}) - {}".format(app["name"], app["url"], app["description"]))


def count_apps(apps):
    tot = 0
    for cat in apps:
        tot += len(apps[cat])
    return tot

with open('cli-apps.yaml', 'r') as yf:
    data = load(yf)
    # print(data)
    apps = data["apps"]
    for cat in apps:
        print("\n{}\n".format(cat))
        for app in apps[cat]:
            print_app(app)
    print("\nTotal: {} apps.".format(count_apps(apps)))
