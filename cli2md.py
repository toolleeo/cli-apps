from yaml import load

summary = """
# Summary

To date, **{}** apps/tools covered, divided in **{}** categories; **8** related sites reviewed and listed.

# Index

{}
Some links to [related resources](#resources).

I'm always interested to new tools, so if you have any suggestion please drop me an email at `toolleeo@gmail.com`.
"""

def fmt_app(app):
    descr = ''.join(c if c != '\n' else ' ' for c in app["description"])
    return("#### [{}]({})\n\n{}\n".format(app["name"], app["url"], descr))


def print_apps(cats, apps):
    for cat_item in cats:
        category = cat_item["label"]
        print('## <a name="{}"></a>{}\n'.format(category, cat_item["name"]))
        for app in apps[category]:
            print(fmt_app(app))


def fmt_cats(cats):
    newlist = sorted(cats, key=lambda k: k['name'])
    st = []
    for cat_item in newlist:
        category = cat_item["label"]
        st.append("[{}](#{})".format(cat_item["name"], cat_item["label"]))
    return ' | '.join(st)


def count_apps(apps):
    tot = 0
    for cat in apps:
        tot += len(apps[cat])
    return tot


with open('cli-apps.yaml', 'r') as yf:
    data = load(yf)
    # print(data)
    apps = data["apps"]
    cats = data["categories"]
    print(summary.format(count_apps(apps), len(cats), fmt_cats(cats)))
    print_apps(cats, apps)
