import csv

summary_template = """
# Summary

To date, **{n_apps}** apps/tools covered, organized in **{n_cats}** categories.

# Index

{cats}

Some links to [related resources](#resources).
"""

resources_template = """
# <a name="resources"></a>Related resources

A list of some online resoures that contribute interesting links to apps and info.

{}
"""


def load_csv(file_name):
    with open(file_name, 'r') as infile:
        csv_reader = csv.DictReader(infile, delimiter=',')
        fields = csv_reader.fieldnames
        data = []
        for item in csv_reader:
           data.append(item)
    return fields, data


def fmt_app(app):
    descr = ''.join(c if c != '\n' else ' ' for c in app['description'])
    if app['homepage'] != '':
        st = '* [{}]({}) - {}'.format(app['name'], app['git'], descr)
    elif app['git'] != '':
        st = '* [{}]({}) - {}'.format(app['name'], app['homepage'], descr)
    else:
        st = '* {} - {}'.format(app['name'], descr)
    return(st)


def print_apps(cats, apps):
    for c in cats:
        cat_item = cats[c]
        print('## <a name="{}"></a>{}\n'.format(c, cat_item['name']))
        if cat_item['description'] != '':
            print(f"{cat_item['description']}.\n")
        apps_in_cat = [a for a in apps if a['category'] == c]
        apps_in_cat = sorted(apps_in_cat, key = lambda i: i['name'].upper())
        for app in apps_in_cat:
            print(fmt_app(app))
        print()

def fmt_categories(cats):
    st = []
    for c in cats:
        st.append("[{}](#{}) ({})".format(cats[c]['name'], c, cats[c]['count']))
    return ' | '.join(st)


def count_apps(apps, categories):
    for c in categories:
        categories[c]['count'] = 0
    for a in apps:
        c = a['category']
        if c in categories:
            categories[c]['count'] += 1
        #else:
        #    print('Category {} does not have any app'.format(c))
    return categories


def categories_list_to_dict(category_list):
    d = {}
    for c in category_list:
        d[c['label']] = {'name': c['name'], 'description': c['description']}
    return d


def main():
    _, apps = load_csv('data/apps.csv')
    _, categories = load_csv('data/categories.csv')
    _, resources = load_csv('data/resources.csv')
    categories = categories_list_to_dict(categories)
    categories = count_apps(apps, categories)

    md_res = ''
    for r in resources:
        md_res += '[{}]({}) - {}\n\n'.format(r['title'], r['url'], r['description'])

    print(summary_template.format(n_apps=len(apps), n_cats=len(categories), cats=fmt_categories(categories)))
    print_apps(categories, apps)
    print(resources_template.format(md_res))


if __name__ == '__main__':
    main()
