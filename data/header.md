# The largest Awesome List of CLI/TUI programs

This repository contains a list of CLI/TUI apps with links and a short description.

To the best of my knowledge, this is the largest collection of CLI/TUI tools available in the form of awesome list.

If you are looking for additional information, you may like [CLIpedia](https://robot.unipv.it/clipedia/), a growing blog about CLI/TUI programs.

# Data organization and building of the list

The peculiarity of this repository is that the source of information is structured into CSV files with a simple structure.
See the `data/` directory.

This `README` file is generated from the CSV files.
To build `README.md` run:

```
make
```

`python3` is required for building. And `make`, of course. :-)

# How to contribute

If you have any suggestion or want your project included in the list, you can either open a pull request or send me an email with the necessary information.

If you want to contribute through a pull request, make sure to add new entries to the correct CSV file under the `data/` directory.
In the CSV, the `git` field refers to a **clonable git URL**.

Please commit changes **to the CSV file only**, **not the README**.
I will review the request and, upon acceptance, I will take care of generating the README and updating the list.

If you prefer an email, contact me at `toolleeo@gmail.com`.
