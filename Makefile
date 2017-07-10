README.md: header.md cli-apps.md resources.yaml
	cat header.md cli-apps.md > README.md

cli-apps.md: cli2md.py cli-apps.yaml resources.yaml
	python3 cli2md.py > cli-apps.md
