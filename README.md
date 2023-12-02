# The largest Awesome List of CLI/TUI programs

This repository - to the best of my knowledge - contains the largest collection of CLI/TUI tools available in the form of awesome list.

To contribute, see the [contribution section](#contribute).

Some links are available to [related resources](#resources).

# Summary

* Apps/tools covered: **1267**
* Number of categories: **75**.

# Index

* [AI / ChatGPT](#ai) (13), [Anki, decks and flashcards](#flashcard) (6)
* [Backup](#backup) (16)
* [Calculators](#calc) (10), [Chat and instant messaging](#chat) (27), [Clean up of files and directories](#file-dir-cleanup) (12), [Co-pilot](#copilot) (9), [Command launchers](#launcher) (20), [Commands cheatsheet and snippets](#cheatsheet) (18), [Conversion](#conversion) (11)
* [Data management](#data-management) (17), [Data management - JSON/YAML/etc.](#data-management-json) (43), [Data management - Tabular data](#data-management-tabular) (19), [Data transfer](#transfer) (40), [DevOps](#devops) (10), [Diff](#diff) (10), [Directory changers (alternatives to cd)](#cd) (18), [Disk usage analyzers](#disk-analyzer) (12)
* [Editors](#editors) (25), [Email](#email) (14)
* [File and file system handling](#file-handling) (20), [File deletion and trash bin (alternatives to rm)](#rm) (5), [File explorer and tree visualization](#file-explorer) (10), [File finding (alternatives to find)](#find) (7), [File listing (alternatives to ls)](#ls) (9), [File manager](#file-manager) (19), [File renamers](#file-renamer) (12), [File systems](#file-system) (4), [File watching for changes](#file-watch) (8), [Financial tools](#financial) (12), [Font management](#font) (2), [Funny tools](#funny) (30), [Fuzzy finders](#fuzzy-finder) (11)
* [Games](#games) (48), [Git and accessories](#git) (42), [Graphics](#graphics) (34)
* [History management](#history) (4)
* [Markdown](#markdown) (11)
* [Networking](#networking) (47), [Note taking](#note-taking) (21)
* [Office tools](#office) (11), [Online search and resources](#online) (15), [Organizers and calendars](#organizers) (21)
* [Package managers](#package-manager) (11), [Password managers](#password-manager) (18), [Process viewers and monitoring (alternatives to top)](#monitor-top) (19), [Productivity](#productivity) (9), [Program templates and boilerplate](#programming-boilerplate) (11), [Programming](#programming) (34), [Prompts](#prompt) (4)
* [RSS](#rss) (9), [Religion](#religion) (4)
* [Science](#science) (17), [Screen recorder](#screen-recorder) (10), [Screen savers](#screensaver) (4), [Security and encryption](#security) (26), [Shells](#shells) (14), [Sound and music](#music) (42), [System monitoring](#monitor) (23), [System tools](#system) (22)
* [Terminals](#terminal) (13), [Text processing](#text-processing) (31), [Text search (alternatives to grep)](#text-search) (10), [Text search and replace (alternatives to sed)](#text-search-replace) (4), [Time trackers](#time-tracker) (15), [Todo managers](#todo-manager) (30), [Torrent](#torrent) (7), [Typing test and practice](#typing) (8)
* [Utilities](#utility) (31)
* [Versioning](#versioning) (6), [Video](#video) (11), [Viewers](#viewers) (20)
* [Web browser](#browser) (17), [Web development](#webdev) (25), [Writing](#writing) (9)

## <a name="ai"></a>AI / ChatGPT

Interfaces and front-ends to GPT engines and other tools powered by artificial intelligence and Natural Language Processing.

* [AI](https://github.com/nitefood/ai-bash-gpt) - A commandline ChatGPT client in BASH with conversation/completion support.
* [AIChat](https://github.com/sigoden/aichat) - Using ChatGPT/GPT-3.5/GPT-4 in the terminal.
* [ata](https://github.com/rikhuijzer/ata) - Ask the Terminal Anything: OpenAI GPT in the terminal.
* [Chatblade](https://github.com/npiv/chatblade) - Chatblade is a versatile command-line interface (CLI) tool designed to interact with OpenAI's ChatGPT.
* [chatgpt](https://github.com/mglantz/chatgpt) - Simple command line integration to Chat GPT.
* [clevercli](https://github.com/clevercli/clevercli) - ChatGPT powered CLI utilities. Easily add new prompt types.
* [cligpt](https://github.com/paij0se/cligpt) - ChatGPT but in the terminal.
* [gpterm](https://github.com/MakisChristou/gpterm) - Yet another command-line chat GPT frontend written in Rust.
* [HAL 2023](https://github.com/Brutuski/hal2023-cli) - Inspired by the infamous HAL9000, it is a simple script to chat with OpenAI's ChatGPT.
* [Instrukt](https://github.com/blob42/Instrukt) - A integrated AI environment in the terminal. Build, test and instruct agents.
* [llm-term](https://github.com/juftin/llm-term) - Chat with OpenAI's GPT models directly from the command line.
* [Mods!](https://github.com/charmbracelet/mods) - AI for the command line, built for pipelines.
* [safespace](https://github.com/danlou/safespace) - Your local AI counselor. LLM app that runs offline from a single binary.

## <a name="flashcard"></a>Anki, decks and flashcards

Manage decks of flashcards and Anki decks.

* [flash-tui](https://github.com/TBS1996/speki) - Flashcard app for the terminal.
* [hardv](https://github.com/dongyx/hardv) - A CLI flashcard app for UNIX-compatible systems, conforming to the UNIX philosophy.
* [py_flashcards](https://github.com/M4THYOU/py_flashcards) - Text-only CLI flashcards parsed from Markdown file.
* [speki](https://github.com/tbs1996/speki) - Manage flashcards in the terminal similar to anki.
* [ToRRential Card processor](https://github.com/Constantin1489/trrc) - A command-line program to add a card to Anki using AnkiConnect API.
* [tui-deck](https://github.com/mebitek/tui-deck) - A TUI frontend for Nextcloud Deck app.

## <a name="backup"></a>Backup

Tools to manage the backup of files and directories.

* [autorestic](https://autorestic.vercel.app/) - A wrapper around the [restic](https://restic.net/) backup tool, with the goal of simplifying the setup and usage through the use of config files.
* [borg](https://www.borgbackup.org/) - Encrypted backups with a clean and simple interface, easy to use and set up, possibility to mount the backup archive with FUSE and inspect it as a regular file system.
* [bup](https://bup.github.io/) - Very efficient backup system based on the git packfile format, providing fast incremental saves and global deduplication.
* [bupstash](https://github.com/andrewchambers/bupstash) - Easy and efficient encrypted backups.
* [Crestic](https://nils-werner.github.io/crestic/) - Configurable Restic Wrapper.
* [duplicity](http://duplicity.nongnu.org/) - Creates GPG encrypted, compressed backups; client-side encryption allows to upload the backup onto untrusted servers.
* [Duply](http://duply.net/) - Simplifies the use of [duplicity](http://duplicity.nongnu.org/) by keeping clean configuration files to automate the backup.  
* [gwbackupy](https://github.com/smartondev/gwbackupy) - Open source Google Workspace™ backup solution.
* [Kopia](https://kopia.io/) - Cross-platform backup tool for Windows, macOS & Linux with fast, incremental backups, client-side end-to-end encryption, compression and data deduplication. CLI and GUI included.
* [paperbackup](https://github.com/intra2net/paperbackup) - Create a pdf with barcodes to backup text files on paper.
* [rdiff-backup](https://rdiff-backup.net/) - Reverse differential backup tool, over a network or locally, using the same protocol as rsync to transfer and store data.
* [Restic](https://restic.net/) - A backup program that is fast, efficient and secure.
* [shallow-backup](https://github.com/alichtman/shallow-backup) - Git integrated backup tool.
* [thread-safe](https://github.com/dkaslovsky/thread-safe) - Keep your favorite Twitter threads safe with a local copy.
* [Zaloha.sh](https://github.com/Fitus/Zaloha.sh) - Shellscript for synchronization of files and directories.
* [zbackup](http://zbackup.org/) - A globally-deduplicating backup tool, based on the ideas found in rsync.

## <a name="calc"></a>Calculators

Calculators for mathematical operations among numbers, dates, base conversions, etc..

* [bcal](https://github.com/jarun/bcal) - Byte CALculator - A REPL CLI utility for storage expression evaluation, SI/IEC conversion, byte address calculation, base conversion and LBA/CHS calculation.
* [Bitwise](https://github.com/mellowcandle/bitwise) - Base conversion and bit manipulator in ncurses.
* [kalc](https://github.com/bgkillas/kalc) - A complex numbers, 2d/3d graphing, arbitrary precision, vector, cli calculator with real-time output.
* [kalk](https://github.com/PaddiM8/kalker) - Command line calculator that supports math-like syntax with user-defined variables, functions, derivation, integration, and complex numbers.
* [mdlt](https://github.com/metadelta/mdlt) - A lightweight command line tool that lets you perform arithmetic and symbolic math operations right from the terminal.
* [Nota](https://kary.us/nota/) - Terminal calculator with rich notation.
* [Numbat](https://github.com/sharkdp/numbat) - Numbat is a calculator for scientific computations with first class support for physical dimensions and units.
* [pdd](https://github.com/jarun/pdd) - Tiny date, time diff calculator.
* [Programmer calculator](https://github.com/alt-romes/programmer-calculator) - Terminal calculator made for programmers working with multiple number representations, sizes, and overall close to the bits.
* [Qalculate](https://qalculate.github.io/) - Multi-purpose calculator with customizable functions, units, arbitrary precision, plotting (it includes a GUI).

## <a name="chat"></a>Chat and instant messaging

Clients for chat and other instant messaging protocols, e.g., IRC, Discord, Mattermost, Matrix, Slack, Telegram, Reddit.

* [Discordo](https://github.com/ayn2op/discordo) - A lightweight, secure, and feature-rich Discord terminal client.
* [finch](http://www.pidgin.im/) - IM program supporting many protocols, including Yahoo!, AIM, IRC, or WLM; comes with the `Pidgin` project.
* [GNU Freetalk](https://www.gnu.org/software/freetalk/) - A console based chat client for Jabber and other XMPP servers. It has context sensitive auto-completion for buddy names, commands, and even ordinary English words.
* [gomuks](https://github.com/tulir/gomuks) - A terminal based Matrix client written in Go.
* [irssi](http://www.irssi.org) - The most popular IRC client for the command-line; a flexible program, with many options and supporting many protocols.
* [kirc](http://kirc.io/) - A tiny IRC client written in POSIX C99.
* [matrix-commander](https://github.com/8go/matrix-commander) - Simple but convenient CLI-based Matrix client app for sending and receiving.
* [matrixcli](https://github.com/saadjsct/matrixcli) - A minimal command line matrix client.
* [matterhorn](https://github.com/matterhorn-chat/matterhorn) - A terminal client for the Mattermost chat system.
* [MCABBER](https://mcabber.com/) - A small XMPP (Jabber) console client including features such as SASL/SSL/TLS support, MUC (Multi-User Chat) support, history logging, command completion, OpenPGP encryption and more.
* [PingMe](https://github.com/kha7iq/pingme) - Sends messages or alerts to multiple messaging platforms & email, including Slack, Telegram, Mattermost, WeChat and others.
* [Poezio](https://poez.io/en/) - Poezio is a free console XMPP client. It lets you connect very easily (no account creation needed) to the network and join various chatrooms. Many commands are identical to common IRC clients. Configuration can be made in a configuration file or directly from the client.
* [Profanity](https://profanity-im.github.io/) - Profanity is a console based XMPP client written in C using ncurses and libstrophe, inspired by Irssi.
* [RainbowStream](http://www.rainbowstream.org/) - Twitter client for the terminal allows almost all the operations that can be done from GUI and Web clients.
* [Servitor](https://github.com/bentonedmondson/servitor) - A command-line Fediverse client that doesn’t require a server.
* [sic](https://tools.suckless.org/sic/) - sic is an extremely simple IRC client. It consists of less than 250 lines of code.
* [signal-cli](https://github.com/AsamK/signal-cli) - signal-cli provides an unofficial commandline, dbus and JSON-RPC interface for the Signal messenger.
* [ssh-chat](https://github.com/shazow/ssh-chat) - Custom SSH server written in Go. Instead of a shell, you get a chat prompt.
* [Telegram messenger CLI](https://github.com/vysheng/tg) - Command-line interface for Telegram using the readline interface.
* [tgbounce](https://github.com/azhuchkov/tgbounce) - Simple Telegram Assistant that allows replying to messages, clicking buttons from bots, marking messages as read, logging notable messages, and providing desktop notifications, among other features.
* [tiny](https://github.com/osa1/tiny) - tiny is an IRC client written in Rust.
* [toxic](https://github.com/Jfreegman/toxic) - A Tox-based instant messaging and video chat client.
* [ttchat](https://github.com/atye/ttchat) - Twitch chats in the terminal.
* [tuir](https://gitlab.com/ajak/tuir) - Reddit TUI.
* [tweets](https://github.com/diracdeltas/tweets) - Decentralized alternative to twitter that uses git as support tool to manage the tweets.
* [WeeChat](http://weechat.org/) - WeeChat is a fast, light and extensible chat client, with a text-based user interface, designed to be light and extensible: a lightweight core with optional plugins.
* [Weechat-Matrix](https://github.com/poljar/weechat-matrix) - A Python script for Weechat that lets Weechat communicate over the Matrix protocol.

## <a name="file-dir-cleanup"></a>Clean up of files and directories

Find/remove duplicate files, automatically organize files, etc..

* [backdown](https://github.com/Canop/backdown) - Safely and ergonomically remove duplicate files
* [classifier](https://github.com/bhrigu123/classifier) - Organize files in your current directory, by classifying them into folders of music, pdfs, images, etc.
* [czkawka](https://qarmin.github.io/czkawka/) - Remove unnecessary files from your computer
* [detox](http://detox.sourceforge.net/) - A utility designed to easily clean up filenames, it replaces characters like spaces with standard equivalents, it also replace UTF-8 or Latin-1 (or CP 1252) characters with more handy ones.
* [Dext](https://github.com/AfzGit/dext) - (Directories by Extensions) is a script that moves (or copies) files of the same extension into a folder.
* [FClones](https://github.com/pkolaczk/fclones) - Efficient Duplicate File Finder.
* [ff](https://github.com/akymos/ff) - ff is a command-line tool to manage favorite folders, creating an alias, to be used via shell directly with the cd command.
* [Framed](https://github.com/mactat/framed) - A CLI tool that simplifies the organization and management of files and directories in a reusable and architectural manner.
* [inventory](https://github.com/mothdotmonster/inventory) - Move files like an old text adventure.
* [mat2](https://0xacab.org/jvoisin/mat2.git) - Metadata removal tool, supporting a wide range of commonly used file formats.
* [organize-cli](https://github.com/ManrajGrover/organize-cli) - Organize your files automatically.
* [rmlint](https://github.com/sahib/rmlint/) - A tool to recursively scan a directory tree looking for duplicate and broken files, it outputs statistics and save the list of files in JSON format, it produce a shell script that can be inspected before running it to delete the desire files.

## <a name="copilot"></a>Co-pilot

Programs that use GPT and GPT-like engines to generate commands at the command line or code in general from natural language.

* [aido-cli](https://github.com/kris7ian/aido-cli) - Looks another interface to online GPT models to execute command through natural language. Very poor documentation and readme, though.
* [aish](https://github.com/chr15m/aish) - A program that retrieve shell script one-liners, ready to be executed in the terminal.
* [CLI Co-Pilot](https://github.com/AntonOsika/CLI-Co-Pilot) - CLI tool that uses GPT4 to turn natural language commands into their Bash/ZShell/PowerShell equivalents.
* [codemancer](https://0xmmo.github.io/codemancer/) - Code with GPT-4 from your command line.
* [Commandpilot](https://github.com/barthr/commandpilot) - An assistant which uses ChatGPT to aid in constructing commands for bash.
* [gpt-do](https://github.com/yasyf/gpt-do) - This is a handy-dandy CLI for when you don't know wtf to do; instead of furiously grepping through man pages, simply use do (or ddo if on bash/zsh), and have GPT-3 do all the magic for you.
* [Llama Terminal Completion](https://github.com/adammpkins/llama-terminal-completion) - Application that interacts with the llama.cpp library to provide virtual assistant capabilities through the command line. It allows you to ask questions and receive intelligent responses, as well as generate Linux commands based on your prompts.
* [Open Interpreter](https://github.com/KillianLucas/open-interpreter) - OpenAI's Code Interpreter in your terminal, running locally.
* [Yai](https://github.com/ekkinox/yai) - Yai (your AI) is an assistant for your terminal, using OpenAI ChatGPT to build and run commands for you.

## <a name="launcher"></a>Command launchers

Applications to launch/execute programs, either interactively, automatically, in parallel, etc..

* [climenu](https://github.com/10xJSChad/climenu) - Compact application for creating shell menus with executable entries. Use it to build straightforward static shortcut menus or dynamically generate advanced menus for more complex programs.
* [entr](https://github.com/eradman/entr) - Event Notify Test Runner - Run an arbitrary command when files change.
* [foy](https://github.com/zaaack/foy) - A simple, light-weight, type-friendly and modern task runner for general purpose.
* [Gaze](https://github.com/wtetsu/gaze) - Runs a command, right after you save a file.
* [hypershell](https://github.com/holepunchto/hypershell) - Spawn shells anywhere. Fully peer-to-peer, authenticated, and end to end encrypted.
* [lmt](https://github.com/Rohansjamadagni/lmt) - A program that can be used to run applications with resource limits enforced using cgroupsv2 on Linux; it allows to set limits on CPU usage, memory usage, and the number of cores for a process.
* [Marker](https://github.com/pindexis/marker) - The terminal command palette.
* [mprocs](https://github.com/pvolok/mprocs) - mprocs runs multiple commands in parallel and shows output of each command separately.
* [Mxflow-cli](https://github.com/metaory/mxflow-cli) - A modern, general purpose CLI task runner with human readable yaml config file.
* [parallel](https://www.gnu.org/software/parallel/) - A shell tool from GNU for executing jobs in parallel using one or more computers, it can split the input and pipe it into commands in parallel.
* [procmux](https://github.com/napisani/procmux) - A TUI utility for running multiple commands in parallel in easily switchable terminals.
* [pueue](https://github.com/Nukesor/pueue) - Pueue is a command-line task management tool for sequential and parallel execution of long-running tasks.
* [rofi](https://github.com/davatorium/rofi) - A window switcher, application launcher and dmenu replacement.
* [sake](https://github.com/alajmo/sake) - A command runner for local and remote hosts. You define servers and tasks in sake.yaml file and then run the tasks on the servers.
* [shell2http](https://github.com/msoap/shell2http) - Executing shell commands via HTTP server.
* [sofi](https://github.com/don-aman/sofi) - Terminal-based application launcher written in POSIX-compliant shell.
* [Task](https://taskfile.dev/) - A task runner / simpler Make alternative written in Go.
* [task-spooler](http://vicerveza.homeunix.net/~viric/soft/ts/) - A Unix batch system that can be used to add the Linux commands to the queue and execute them one after the other in numerical order (ascending order, to be precise). This can be very useful when you have to run a lots of commands, but you don't want to waste time waiting for one command to finish and run the next command. You can queue it all up and Task Spooler will execute them one by one. In the mean time, you can do other activities.
* [taverner](https://github.com/vagos/taverner) - CLI launcher menu for games (or anything), the UNIX way.
* [Violet](https://github.com/braheezy/violet) - Colorful TUI frontend to run Vagrant commands.

## <a name="cheatsheet"></a>Commands cheatsheet and snippets

Tools to manage often used commands, code snippets, and alternative manual pages.

* [carapace](https://github.com/rsteube/carapace-bin) - Carapace provides argument completion for multiple CLI commands and works across multiple POSIX and non-POSIX shells.
* [docfd](https://github.com/darrenldl/docfd) - TUI fuzzy document finder that looks for documentation files in markdown and txt format in the directory tree.
* [eg](https://github.com/srsudar/eg) - Useful examples at the command line.
* [ehh](https://github.com/lennardv2/ehh) - Command-line tool for remembering linux/terminal commands.
* [fzf-help](https://github.com/BartSte/fzf-help) - An fzf extension that allows you to select command line options of a given command; the options are retrieved from the command its `--help` documentation.
* [halp](https://github.com/orhun/halp) - halp aims to help find the correct arguments for command-line tools by checking the predefined list of commonly used options/flags.
* [IntelliShell](https://github.com/lasantosr/intelli-shell) - Like IntelliSense, but for shells, acting like a bookmark store for commands.
* [kmdr-cli](https://github.com/ediardo/kmdr-cli) - The CLI tool for explaining commands from your terminal.
* [ManPDF & ManWEB](https://github.com/sebastiancarlos/manpdf) - Read your Man pages in PDF format. Even online!
* [MUC](https://github.com/nate-sys/muc) - Visualize your most used commands.
* [Nap](https://github.com/maaslalani/nap) - Code snippet manager that allows to create and access new snippets quickly with the command-line interface or browse, manage, and organize them with the text-user interface.
* [navi](https://github.com/denisidoro/navi) - An interactive cheatsheet tool for the command-line.
* [pet](https://github.com/knqyf263/pet) - Pet is a simple command-line snippet manager, written in Go.
* [tealdeer](https://github.com/dbrgn/tealdeer) - Very fast implementation of tldr in Rust.
* [The Fuck](https://github.com/nvbn/thefuck) - Magnificent app which corrects your previous console command (although I would be extra-cautious at making a program to automatically infer what I was intending).
* [tldr](https://tldr.sh/) - Client for tldr pages, a community effort to simplify the beloved man pages with practical examples.
* [topalias](https://github.com/meteoritt/topalias) - Linux alias generator from bash/zsh command history with statistics, written on Python.
* [Wat](https://github.com/dthree/wat) - Instant, central, community-built docs.

## <a name="conversion"></a>Conversion

File format converters.

* [antiword](https://web.archive.org/web/20071002133135/http://www.winfield.demon.nl/) - Reader and converted for the proprietary MS .doc file format.
* [BaFi](https://mmalcek.github.io/bafi/) - Universal JSON, BSON, YAML, CSV, XML translator to ANY format using templates.
* [catdoc](http://www.wagner.pp.ru/~vitus/software/catdoc/) - Command line converter from Microsoft Word to plain text, output is sent to the standard output.
* [hget](https://github.com/bevacqua/hget) - A CLI to convert HTML into plain text. Can be used to fetch a site's HTML version and convert it into plain text, or to deliver plain text versions of your site dynamically.
* [jsonify-resume](https://github.com/ashishbinu/jsonify-resume) - A cli that converts resumes into JSON Resume schema.
* [NestedTextTo](https://github.com/AndydeCleyre/nestedtextto) - CLI to convert between NestedText and JSON, YAML, or TOML.
* [Pandoc](http://pandoc.org/) - Universal document file converter; handles input output from/to a number of formats: HTML, PDF, LaTeX, docx, odt, AsciiDoc, Markdown, Textile, just to mention a few; the quality of conversion strongly depends on the combination of input/output formats.
* [simtex](https://github.com/simtex-dev/engine) - simtex (simplified LaTeX) allows you to convert your markdown or text lectures into LaTeX file with one command, configured with simple .json file.
* [unoserver](https://github.com/unoconv/unoserver/) - Using LibreOffice as a server for converting documents, it allows to convert multiple documents without loading libreoffice into memory every time.
* [Vertopal-CLI](https://github.com/vertopal/vertopal-cli) - Vertopal-CLI is a small, yet powerful utility for converting digital files to a variety of file formats using Vertopal public API.
* [wv](https://wvware.sourceforge.net/) - Utility for performing operations on .doc files. The tools is now deprecated in favor of AbiWord, which uses the same library that is used in the CLI program.

## <a name="data-management"></a>Data management

Tools to manage data files.

* [crudini](https://github.com/pixelb/crudini) - A utility for manipulating ini files.
* [datadash](https://github.com/keithknott26/datadash) - Visualize and graph data in the terminal.
* [datasetGPT](https://github.com/radi-cho/datasetGPT) - A command-line interface and a Python library for inferencing Large Language Models to generate textual datasets.
* [dateutils](http://www.fresse.org/dateutils/) - Dateutils are a bunch of tools that revolve around fiddling with dates and times in the command line with a strong focus on use cases that arise when dealing with large amounts of financial data.
* [GNU Recutils](https://www.gnu.org/software/recutils/manual/) - Set of tools and libraries to access human-editable, text-based databases called recfiles.
* [gnuplot](https://www.explainshell.com/explain/1/gnuplot) - Generate two and three dimensional plots of data.
* [IRedis](https://github.com/laixintao/iredis) - Interactive Redis: A Cli for Redis with AutoCompletion and Syntax Highlighting.
* [lowcharts](https://github.com/juan-leon/lowcharts) - lowcharts is meant to be used in those scenarios where we have numerical data in text files that we want to display in the terminal to do a basic analysis.
* [osmf](https://github.com/codesoap/osmar) - OpenStreetMap find - A simple command line tool to explore OSM data.
* [play](https://github.com/paololazzari/play) - TUI playground for your favorite programs, such as grep, sed and awk.
* [ramda-cli](https://github.com/raine/ramda-cli) - A tool for processing data with functional pipelines.
* [Redis Viewer](https://github.com/SaltFishPr/redis-viewer) - A tool to view redis data in terminal.
* [redis_tui](https://github.com/mat2cc/redis_tui) - Redis terminal browser application.
* [ROAPI](https://github.com/roapi/roapi) - ROAPI automatically spins up read-only APIs for static datasets without requiring you to write a single line of code.
* [sampler](https://github.com/sqshq/sampler) - Sampler is a tool for shell commands execution, visualization and alerting. Configured with a simple YAML file.
* [WOPR](https://github.com/yaronn/wopr) - A simple markup language for creating rich terminal reports, presentations and infographic.
* [zq](https://zed.brimdata.io/docs/commands/zq/) - A command-line tool that uses the Zed language for pipeline-style search and analytics. It can query a variety of data formats (CSV, JSON, etc.) in files, over HTTP, or in S3 storage.

## <a name="data-management-json"></a>Data management - JSON/YAML/etc.

Tools to manage data files, dedicated to JSON, YAML and other similar formats.

* [dasel](https://github.com/TomWright/dasel) - Allows you to query and modify data structures using selector strings.
* [faq](https://github.com/jzelinskie/faq) - Format Agnostic jQ - process various formats with libjq.
* [fx](https://github.com/antonmedv/fx) - Command-line JSON viewer.
* [gojq](https://github.com/itchyny/gojq) - Pure Go implementation of jq.
* [Graphtage](https://github.com/trailofbits/graphtage) - Graphtage is a commandline utility and underlying library for semantically comparing and merging tree-like structures, such as JSON, XML, HTML, YAML, plist, and CSS files.
* [gron](https://github.com/tomnomnom/gron) - gron transforms JSON into discrete assignments to make it easier to grep for what you want and see the absolute 'path' to it.
* [GROQ](https://github.com/sanity-io/groq-cli) - The CLI tool consumes both JSON and NDJSON documents. You can pass in data from a local file, or from piping to standard input.
* [jaq](https://github.com/01mf02/jaq) - jaq is a clone of the JSON data processing tool jq, that aims to support a large subset of jq's syntax and operations.
* [jayin](https://github.com/we-cli/jayin) - Piping with js at terminal.
* [jc](https://github.com/kellyjonbrazil/jc) - Serializes the output of command line tools to JSON.
* [jello](https://github.com/kellyjonbrazil/jello) - CLI tool to filter JSON and JSON Lines data with Python syntax, similar to - suprise :-), jq!
* [jid](https://github.com/simeji/jid) - You can drill down JSON interactively by using filtering queries like jq.
* [jiq](https://github.com/fiatjaf/jiq) - jid on jq - interactive JSON query tool using jq expressions.
* [jj](https://github.com/tidwall/jj) - A command line utility that provides a fast and simple way to retrieve or update values from JSON documents.
* [jl](https://github.com/chrisdone/jl) - jl ("JSON lambda") is a tiny functional language for querying and manipulating JSON.
* [jless](https://pauljuliusmartinez.github.io/) - Command-line JSON viewer designed for reading, exploring, and searching through JSON data.
* [jo](https://github.com/jpmens/jo) - A small utility to create JSON objects from the command line.
* [jp](https://github.com/therealklanni/jp) - A tiny commandline tool for parsing JSON from any source.
* [jp](https://github.com/jmespath/jp) - A command line interface to JMESPath, an expression language for manipulating JSON.
* [jq](https://stedolan.github.io/jq/) - (JSON Query?) is sed-like processor for JSON data; can be used to process JSON files and data streams and perform operations such as those allowed by `cat`, `sed`, `grep` and `awk` on regular text files.
* [jqp](https://github.com/noahgorstein/jqp) - A TUI playground for exploring jq.
* [jqview](https://github.com/fiatjaf/jqview) - Simplest possible native GUI for inspecting JSON.
* [Jsawk](https://github.com/micha/jsawk) - Like awk, but for JSON. You work with an array of JSON objects read from stdin, filter them using JavaScript to produce a results array that is printed to stdout.
* [jsed](https://github.com/jtopjian/jsed) - jsed is a small command-line utility to add, remove, and search for data in a JSON structure.
* [jshon](https://github.com/keenerd/jshon) - Jshon is a JSON parser designed for maximum convenience within the shell.
* [json](https://github.com/trentm/json) - A "json" command for massaging JSON on your Unix command line.
* [JSON Command](https://github.com/zpoley/json-command) - JSON command line processing toolkit: no more writing code to inspect or transform JSON objects.
* [JSON-Grep](https://github.com/ploubser/JSON-Grep) - JGrep is a command line tool and API for parsing JSON documents based on logical expressions.
* [JSON.awk](https://github.com/step-/JSON.awk) - A practical JSON parser written in awk.
* [JSON.sh](https://github.com/dominictarr/JSON.sh) - A JSON parser written in shell, compatible with ash, bash, dash and zsh.
* [jsongrep](https://github.com/dsc/jsongrep) - A shell tool to search and select bits out of JSON documents.
* [jsongrep](https://github.com/terrycojones/jsongrep) - Python for extracting pieces of JSON objects
* [jsonpp](https://github.com/jmhodges/jsonpp) - A fast command line JSON pretty printer.
* [jsonv.sh](https://github.com/archan937/jsonv.sh) - A Bash command line tool for converting JSON to CSV.
* [jtbl](https://github.com/kellyjonbrazil/jtbl) - A simple CLI tool to print JSON and JSON Lines data as a table in the terminal.
* [jtc](https://github.com/ldn-softdev/jtc) - JSON manipulation and transformation.
* [RecordStream](https://github.com/benbernard/RecordStream) - Commandline tools for slicing and dicing JSON records.
* [rq](https://github.com/dflemstr/rq) - Record Query - A tool for doing record analysis and transformation.
* [TickTick](https://github.com/kristopolous/TickTick) - TickTick enables you to put JSON in bash scripts. Yes, just encapsulate them with two back-ticks.
* [underscore-cli](https://github.com/ddopson/underscore-cli) - Command-line utility-belt for hacking JSON and Javascript.
* [vj](https://github.com/busyloop/vj) - JSON Humanizer makes JSON human readable by applying visual formatting.
* [YAML Paths](https://github.com/wwkimball/yamlpath) - YAML/JSON/EYAML/Compatible get/set/merge/validate/scan/convert/diff processors using powerful, intuitive, command-line friendly syntax.
* [yq](https://github.com/mikefarah/yq) - Portable command-line YAML processor.

## <a name="data-management-tabular"></a>Data management - Tabular data

Tools to manage tabular data files, such as CSV, spreadsheets, and database tables.

* [csvkit](https://github.com/wireservice/csvkit) - A suite of command-line tools for converting to and working with CSV, the king of tabular file formats.
* [csvq](https://github.com/mithrandie/csvq) - SQL-like query language for csv.
* [csvtk](https://bioinf.shenwei.me/csvtk/) - A cross-platform, efficient and practical CSV/TSV toolkit written in Go.
* [Dolt](https://github.com/dolthub/dolt) - Dolt is Git for Data! Dolt is a SQL database that you can fork, clone, branch, merge, push and pull just like a git repository.
* [litecli](https://github.com/dbcli/litecli) - CLI for SQLite Databases with auto-completion and syntax highlighting.
* [Miller](https://github.com/johnkerl/miller) - Miller is like awk, sed, cut, join, and sort for data formats such as CSV, TSV, JSON, JSON Lines, and positionally-indexed.
* [mycli](https://github.com/dbcli/mycli) - A command line client for MySQL that can do auto-completion and syntax highlighting.
* [pgcli](https://github.com/dbcli/pgcli) - Postgres CLI with autocompletion and syntax highlighting.
* [pykli](https://github.com/eshepelyuk/pykli) - Interactive ksqlDB command line client with autocompletion and syntax highlighting written in Python.
* [q](http://harelba.github.io/q/) - Executes SQL-like queries on CSVs/TSVs tabular data files; each tabular file is treated as a database table; support to all SQL constructs (`WHERE`, `GROUP BY`, `JOIN`).
* [Soul](https://github.com/thevahidal/soul) - A SQLite REST and realtime server.
* [sq](https://github.com/neilotoole/sq) - Command line tool that provides jq-style access to structured data sources such as SQL databases, or document formats like CSV or Excel.
* [tabview](https://github.com/TabViewer/tabview) - Python curses command line CSV and tabular data viewer.
* [termdbms](https://github.com/mathaou/termdbms) - A TUI for viewing and editing databases, written in pure Go.
* [TSV Utilities](https://github.com/eBay/tsv-utils) - Command line tools for large, tabular data files.
* [TV](https://github.com/alexhallam/tv) - Cross-platform CSV pretty printer made to maximize viewer enjoyment.
* [usql](https://github.com/xo/usql) - Universal command-line interface for PostgreSQL, MySQL, Oracle Database, SQLite3, Microsoft SQL Server, and others, including NoSQL and non-relational databases.
* [VisiData](https://www.visidata.org/) - Interactive multitool for tabular data. It combines the clarity of a spreadsheet, the efficiency of the terminal, and the power of Python, into a lightweight utility which can handle millions of rows with ease.
* [xsv](https://www.johndcook.com/blog/2019/12/31/sql-join-csv-files/) - Doing a SQL join with CSV files.

## <a name="transfer"></a>Data transfer

Programs for transferring files and data between different machines.

* [aria2](https://github.com/aria2/aria2) - Lightweight and easy-to-use download utility; it supports HTTP/HTTPS, FTP, SFTP, BitTorrent, Metalink and multiple sources; cross-platform.
* [Clipsync](https://github.com/marcopaganini/clipsync) - Share your clipboard across multiple machines using an MQTT service.
* [croc](https://github.com/schollz/croc) - Easily and securely send things from one computer to another.
* [curl](https://curl.haxx.se/) - A tool and library for transferring data with URL syntax, supports a lot of protocols.
* [curlie](https://github.com/rs/curlie) - The power of curl, the ease of use of httpie.
* [downloader-cli](https://github.com/deepjyoti30/downloader-cli) - A simple downloader written in Python with an awesome customizable progressbar.
* [feuille](https://basedwa.re/tmtt/feuille.git) - A fast, dead-simple socket-based pastebin.
* [ffsend](https://github.com/timvisee/ffsend) - Easily and securely share files from the command line. A fully featured Firefox Send client.
* [gallery-dl](https://github.com/mikf/gallery-dl) - Gallery-dl is a command-line program to download image galleries and collections from several image hosting sites.
* [Jitter](https://github.com/kevspau/jitter) - A repository-oriented binary manager for Linux, Jitter searches through online repository (currently only on GitHub) for releases with .tar.gz, .tgz, .zip or .AppImage assets.
* [lftp](https://lftp.yar.ru/) - "Sophisticated ftp/http client, and a file transfer program supporting a number of network protocols"; support for bookmarks and mirroring features.
* [lux](https://github.com/iawia002/lux) - Lux is a fast and simple video downloader built with Go.
* [Magic Wormhole](https://github.com/magic-wormhole/magic-wormhole) - The program allows transfer arbitrary-sized files and directories (or short pieces of text) from one computer to another The two endpoints are identified by using identical human-readable codes.  
* [newsboat_video_downloader](https://github.com/Jocomol/newsboat_video_downloader) - Downloads content from youtube and have them sorted into different folders depending on the channel.
* [Nextcloud share URL downloader](https://github.com/aertslab/nextcloud_share_url_downloader) - Download files from and list content of NextCloud (password protected) share directly from the command line without needing a webbrowser.
* [OnionShare](https://onionshare.org/) - "An open source tool that lets you securely and anonymously share a file of any size." 
* [pbgopy](https://github.com/nakabonne/pbgopy) - Copy and paste between devices.
* [pbproxy](https://github.com/nikvdp/pbproxy) - Send your clipboard anywhere you can ssh to.
* [portal](https://github.com/SpatiumPortae/portal) - A quick and easy command-line file transfer utility from any computer to another.
* [qr-filetransfer](https://github.com/sdushantha/qr-filetransfer) - Transfer files over WiFi between your computer and your smartphone from the terminal.
* [qrcp](https://www.linuxuprising.com/2020/07/qrcp-transfer-files-between-desktop-and.html) - Transfer Files Between Desktop And Mobile Devices Over Wi-Fi By Scanning A QR Code.
* [rclone](https://rclone.org/) - Rclone manages file synchronization on cloud storage.
* [rclone-tui](https://github.com/darkhz/rclone-tui) - Cross-platform manager for rclone, which aims to be on-par with the web GUI.
* [rsync](https://download.samba.org/pub/rsync/rsync.html) - Mirror directories across networked machines, handles diffs/changed files, works across SSH, plenty of parameters.
* [sharing](https://github.com/parvardegr/sharing) - Sharing is a command-line tool to share directories and files from the CLI to iOS and Android devices without the need of an extra client app.
* [shbin](https://github.com/Shiphero/shbin/) - Upload code snippets, notebooks, images or any other content to a Github repository that acts as your internal pastebin, and returns the URL to share it with your team.
* [shcopy](https://github.com/aymanbagabas/shcopy) - Copy text to your system clipboard locally and remotely using ANSI OSC52 sequence.
* [sitecopy](http://www.manyfish.co.uk/sitecopy/) - Synchronizes a local copy of a website with a remote copy on a server, does not use SSH/`scp` but FTP for file copy, useful when the remote server does not support secure copy.
* [stftp](http://stftp.sourceforge.net/) - (simple terminal FTP) aims to be a "easy-to-use and unbloated client for the UNIX (and UNIX-like) console".
* [tdl](https://github.com/iyear/tdl) - Beautiful and feature-rich Telegram downloader, written in Go.
* [tran](https://github.com/abdfnx/tran) - Securely transfer and send anything between computers with TUI.
* [tshare](https://github.com/trikko/tshare) - The fastest way to share your files on the web, for free.
* [Unison](https://www.cis.upenn.edu/~bcpierce/unison/) - File synchronizer. It allows two replicas of a collection of files and directories to be stored on different hosts (or different disks on the same host), modified separately, and then brought up to date by propagating the changes in each replica to the other.
* [Woof](http://www.home.unix-ag.org/simon/woof.html) - (Web Offer One File) sets up an HTTP webserver to serve files from a given local directory all the users connected to the network can see and download the files.
* [xh](https://github.com/ducaale/xh) - xh is a friendly and fast tool for sending HTTP requests. It reimplements as much as possible of HTTPie's excellent design.
* [Yark](https://github.com/Owez/yark) - YouTube archiving made simple.
* [youtube-dl](https://github.com/ytdl-org/youtube-dl/) - Downloads videos from [YouTube](https://www.youtube.com/) and some other sites useful for automated bulk downloads.
* [yt-dlp](https://github.com/yt-dlp/yt-dlp) - A youtube-dl fork with additional features and fixes.
* [ytfzf](https://github.com/pystardust/ytfzf) - A POSIX script that helps you find Youtube videos (without API) and opens/downloads them using mpv/youtube-dl.
* [ytmdl](https://github.com/deepjyoti30/ytmdl) - Get songs from Youtube in mp3 format.

## <a name="devops"></a>DevOps

Applications for supporting DevOps tasks, such as containers or cloud systems management.

* [ContainerSSH](https://github.com/ContainerSSH/ContainerSSH) - An SSH Server that Launches Containers in Kubernetes and Docker on demand.
* [decompose](https://github.com/s0rg/decompose) - Reverse-engineering tool for docker environments.
* [Devbox](https://github.com/jetpack-io/devbox) - Devbox is a command-line tool that lets you easily create isolated shells and containers by defining the list of packages required by the environment.
* [docker](https://docs.docker.com/) - Self-sufficient runtime for containers.
* [docker-shell](https://github.com/Trendyol/docker-shell) - A simple interactive prompt for Docker.
* [Dockly](https://github.com/lirantal/dockly) - Immersive terminal interface for managing docker containers, services and images.
* [k9s](https://github.com/derailed/k9s) - Kubernetes CLI To Manage Your Clusters In Style!
* [lazydocker](https://github.com/jesseduffield/lazydocker) - The lazier way to manage everything docker. A simple terminal UI for both docker and docker-compose, written in Go with the gocui library.
* [OPS](https://github.com/nanovms/ops) - Ops is a tool for creating and running a [Nanos](https://github.com/nanovms/nanos) unikernel. It is used to package, create, and run your application as a [Nanos](https://github.com/nanovms/nanos) unikernel instance.
* [SAWS](https://github.com/donnemartin/saws) - A supercharged AWS command line interface (CLI).

## <a name="diff"></a>Diff

Calculation of diffs between files and data, even with context or semantic awareness (i.e., considering the meaning of the data).

* [csv-diff](https://github.com/simonw/csv-diff) - Python CLI tool and library for diffing CSV and JSON files
* [delta](https://github.com/dandavison/delta) - A syntax-highlighter for git and diff output.
* [diff-so-fancy](https://github.com/so-fancy/diff-so-fancy) - Make your diffs human readable instead of machine readable.
* [diff2html-cli](https://github.com/rtfpessoa/diff2html-cli) - Parse git diffs as JSON and generate pretty HTML.
* [Difftastic](https://github.com/Wilfred/difftastic) - Syntax-aware structured diff tool.
* [Dirdiff](https://github.com/OCamlPro/dirdiff) - Efficiently compute the differences between two directories.
* [dyff](https://github.com/homeport/dyff) - A diff tool for YAML files, and sometimes JSON.
* [leven-cli](https://github.com/sindresorhus/leven-cli) - Measure the difference between two strings using the Levenshtein distance algorithm.
* [pdf-diff](https://github.com/serhack/pdf-diff) - A tool for visualizing differences between two pdf files. Mainly dedicated to editors that usually spends a lot of hours on several pdf.
* [ydiff](https://github.com/ymattw/ydiff) - View colored, incremental diff.

## <a name="cd"></a>Directory changers (alternatives to cd)

Programs for improving the efficiency of directory traversal by remembering common paths and other approaches; alternatives to the `cd` command.

* [Apparition](https://github.com/david-haerer/apparition) - Apparition allows to give names to paths, so that moving to the specific path can be done by using the name; it also allows to manage the list of assigned names.
* [autojump](https://github.com/wting/autojump) - A cd command that maintains a database of most visited paths and allows the access to a directory with shortened versions of the path.
* [broot](https://dystroy.org/broot/) - broot displays an optimized (omitting unnecessary content) tree view of the filesystem, allowing to fuzzy search files and folder, and move to specified directories.
* [cdwe](https://github.com/synoet/cdwe) - (cd with env vars) Wrapper of the cd command that sets and unsets env vars when you change dir based on a config file.
* [fasd](https://github.com/clvv/fasd) - It offers quick access to files and directories for POSIX shells by keeping track of files and directories you have accessed, so that you can quickly reference them in the command line.
* [fastdiract](https://github.com/dp12/fastdiract) - Lightning-fast cd and command execution.
* [fz](https://github.com/changyuheng/fz.sh) - Fuzzy tab completion for z.
* [Jmp](https://github.com/gholmes829/Jmp) - Change directory with smart searching of the path specified through regex.
* [menucd](https://github.com/andy5995/menucd) - Directory browser and changer for the command line.
* [nav](https://github.com/dkaslovsky/nav) - Terminal navigator for interactive ls workflows.
* [pazi](https://github.com/euank/pazi) - Fast autojump helper.
* [pm](https://github.com/Angelmmiguel/pm) - The easy way to switch between your projects on ZSH. In short, another directory changer.
* [qcd](https://github.com/ClaasBontus/qcd_rs) - A tool to change to another directory by just by entering commands like `qcd 3` and step back to where you came from with `qcd -o`. Frequently visited directories are stored in a sqlite3 database.
* [slingshot](https://github.com/caio-ishikawa/slingshot) - Lightweight command line tool to quickly navigate across folders.
* [SmartCd](https://github.com/CodesOfRishi/smartcd) - A cd command with improved usability features, which can remember your recently visited directory paths and, search and directly traverse to sub-directories and as well as parent directories, all with Fuzzy searching.
* [z](https://github.com/rupa/z) - Directory changer based on aging and frecency.
* [z.lua](https://github.com/skywind3000/z.lua) - Directory changer that learns your habits.
* [zoxide](https://github.com/ajeetdsouza/zoxide) - It remembers which directories you use most frequently, so you can "jump" to them in just a few keystrokes.

## <a name="disk-analyzer"></a>Disk usage analyzers

Programs to analyze and summarize the usage of disks, visualize and report the size of directories and sub-directories, etc..

* [cdu](http://arsunik.free.fr/prog/cdu.html) - cdu (colored `du`) is a perl script that calls `du` and displays a pretty histogram with optional colors allowing to immediately see the directories which take most disk space.
* [dfc](https://github.com/rolinh/dfc) - Report file system space usage information with style.
* [diskonaut](https://github.com/imsnif/diskonaut) - Terminal disk space navigator that traverse the file-system with a TUI interface.
* [diskus](https://github.com/sharkdp/diskus) - Minimal, fast alternative to du -sh.
* [dua](https://github.com/Byron/dua-cli) - Disk Usage Analyzer. Learn about the usage of disk space of a given directory with parallel access to max out SSD exploration.
* [duf](https://github.com/muesli/duf) - Disk Usage/Free Utility.
* [Dust](https://github.com/bootandy/dust) - du + rust = dust. Like du but more intuitive.
* [dutree](https://github.com/nachoparker/dutree) - A tool to analyze file system usage written in Rust.
* [erdtree](https://github.com/solidiquis/erdtree) - A multi-threaded file-tree visualizer and disk usage analyzer.
* [gdu](https://github.com/dundee/gdu) - Pretty fast disk usage analyzer written in Go. Gdu is intended primarily for SSD disks where it can fully utilize parallel processing. However HDDs work as well, but the performance gain is not so huge.
* [ncdu](https://dev.yorhel.nl/ncdu) - "A disk usage analyzer with an ncurses interface.  It is designed to find space hogs on a remote server where you don't have an entire graphical setup available."
* [vizex](https://github.com/bexxmodd/vizex) - Visualize the disk space usage for every partition and media on the user's machine.

## <a name="editors"></a>Editors

Text editors.

* [ash](https://github.com/akashnag/ash) - A simple and clean terminal-based text editor, that aims to be easy to use with modern key-bindings.
* [Bob](https://github.com/MordechaiHadad/bob) - Bob is a cross-platform and easy-to-use Neovim version manager, allowing for easy switching between versions.
* [Diakonos](https://github.com/Pistos/diakonos) - A powerful editor with “standard" keybindings and several advanced features; written in Ruby.
* [ed](https://www.gnu.org/software/ed/) - GNU ed is a line-oriented text editor. It is used to create, display, modify and otherwise manipulate text files, both interactively and via shell scripts.
* [Emacs](https://www.gnu.org/software/emacs/) - One of the godfathers of text editors, free long-standing software project, with a huge amount of funcionalities and extensions; implemented and extendable with E-Lisp.
* [eon](https://github.com/tomas/eon) - A light, modern editor for your terminal that doesn't want to be vim.
* [Feather](https://www.feathereditor.com/) - The only terminal based text editor designed to work with BIG files.
* [Helix](https://github.com/helix-editor/helix) - A kakoune / neovim inspired editor, written in Rust. The editing model is very heavily based on kakoune.
* [jed](http://www.jedsoft.org/jed/index.html) - A text editor with a drop-down menu facility that make it especially user-friendly.  
* [joe](http://joe-editor.sourceforge.net/) - (Joe's Own Editor) is a compact text editor written in C, a detailed list of features and missing ones is explicitly reported in the website, this editor is mentioned in several web sources for its capability in handling large files.
* [Kakoune](http://kakoune.org/) - Modal editor, faster as in less keystrokes, multiple selections, orthogonal design.
* [micro](https://github.com/zyedidia/micro) - A terminal-based text editor written in Go that aims to be easy to use and intuitive, while also taking advantage of the full capabilities of modern terminals.
* [nano](https://www.nano-editor.org/) - Easy to use, lightweigth text editor; no complex keybindings to remember.
* [neovim](https://neovim.io/) - A work in progress attempt to improve [vim](http://www.vim.org/), dropping older/unused OS compatibility, improving the codebase readability, modularity and maintainability; it has chances to become the next choice of vim users.
* [o](https://github.com/xyproto/orbiton) - Configuration-free text editor and IDE limited to VT100. Suitable for writing git commit messages, editing Markdown, config files, source code, viewing man pages and for quick edit-compile cycles when programming.
* [pickaxe](https://github.com/mdom/pickaxe) - The redmine wiki editor.
* [slap](https://github.com/slap-editor/slap) - Text editor inspired by [Sublime Text](https://www.sublimetext.com/) written in NodeJS, extedable in Javascript.
* [Tilde](https://os.ghalkes.nl/tilde/) - Tilde is a text editor that provides an intuitive interface for people accustomed to GUI environments, usual shortcuts for common operation, a traditional menu bar, etc.
* [vai](https://github.com/stefanoborini/vai) - A text editor similar to `vim` written in Python; many feature are nicely replicated, some are still missing; however, the advantage of this implementation is its simplicity, maintainability and extensibility, thanks to the Python implementation.
* [VE](http://www.inverary.net/ve/ve.html) - Lean, fast and feature rich text editor.
* [vim](http://www.vim.org/) - Historically one of the preferred text editors, behavior based on editing modes, plenty of plugins and tips to address every possible editing problem.
* [vis](https://github.com/martanne/vis) - "a modern, legacy free, simple yet efficient vim-like editor", and more: "The intention is not to be bug for bug compatible with vim, instead a similar editing experience should be provided. The goal could thus be summarized as 80% of vim's features implemented in roughly 1% of the code"; the editor is scriptable in LUA and supports editing large files.
* [vy](https://github.com/vyapp/vy) - A vim-like in python made from scratch.
* [WordGrinder](https://cowlark.com/wordgrinder/) - From the website: "WordGrinder is a word processor for processing words. It is not WYSIWYG. It is not point and click. It is not a desktop publisher. It is not a text editor. It does not do fonts and it barely does styles. What it does do is words. It's designed for writing text. It gets out of your way and lets you type." 
* [zee](https://github.com/zee-editor/zee) - Zee is a modern editor for the terminal, in the spirit of Emacs. It is written in Rust and it is somewhat experimental.

## <a name="email"></a>Email

Email clients (MUA - Mail User Agents), mail synchronization, generation indexing and search.

* [aerc](https://aerc-mail.org/) - A pretty good email client
* [alot](https://github.com/pazz/alot) - MUA written in Python using the [NotMuch](https://notmuchmail.org/) backend, MailDir format support.
* [alpine](http://www.washington.edu/alpine/) - Mail client which aims at being "fast, easy to use email client that is suitable for both the inexperienced email user as well as for the most demanding of power users".
* [Himalaya](https://github.com/soywod/himalaya) - Command-line interface for email management.
* [mbsync](http://isync.sourceforge.net/mbsync.html) - Mailboxes synchronization tool, allows to download email locally, MailDir format supported.
* [meli](https://git.meli.delivery/meli/meli.git) - BSD/Linux terminal email client with support for multiple accounts and Maildir / mbox / notmuch / IMAP / JMAP.
* [Mutt](http://www.mutt.org/) - Mail client with tons of features, customization chances, support for IMAP, POP3, multiple storage formats.
* [NeoMutt](https://neomutt.org/) - Patched and up-to-dated mutt fork.
* [nmail](https://github.com/d99kris/nmail) - nmail is a console-based email client for Linux and macOS with a user interface similar to alpine / pine.
* [Notmuch](https://git.notmuchmail.org/git/notmuch) - Notmuch is a command-line based program for indexing, searching, reading, and tagging large collections of email messages.
* [pop](https://github.com/charmbracelet/pop) - Send emails from your terminal; it uses the API at [https://resend.com/](resend.com).
* [pymailgen](https://github.com/toolleeo/pymailgen) - Starting from the content of a CSV file and a template text file, pymailgen generates a list of emails to be sent out using a command-line SMTP client.
* [sup](http://sup-heliotrope.github.io/) - MUA written in Ruby; specifically developed for accounts with "a lot of emails"; nice thread-based presentation.
* [tmpmail](https://github.com/sdushantha/tmpmail) - A command line utility written in POSIX sh that allows you to create a temporary email address and receive emails to the temporary email address.

## <a name="file-handling"></a>File and file system handling

Tools for managing files and directories (copy, move, extraction from compressed archives, change permissions, etc.).

* [compsize](https://github.com/kilobyte/compsize) - Find compression type/ratio on a file or set of files on a btrfs file system.
* [conan](https://github.com/mirage/conan) - Find clue about the type of the file.
* [doppelganger](https://github.com/witchard/doppelganger) - Save and load your shell environment to create doppelganger shells!
* [dtrx](https://brettcsmith.org/2007/dtrx/) - (Do The Right eXtraction) aims at taking "all the hassle out of extracting archives"; allows to use one command to extract archives in different formats, recursive extraction (files into file) and extracts files into dedicated directories.
* [Fast Files](https://github.com/mintycube/fast-files) - ff is a bash script which is a combination of `mkdir` and `touch`. It can create directory structures and files simultaneously and lists the created objects using `eza`, `lsd`, or `ls`.
* [file-type-cli](https://github.com/sindresorhus/file-type-cli) - Detect the file type of a file or stdin.
* [ForkFS](https://github.com/SUPERCILEX/forkfs) - ForkFS allows you to sandbox a process's changes to your file system.
* [gcp](https://github.com/aelafifi/gcp/) - `gcp` (Goffi's cp) is an advanced file copier tool, heavily inspired from the traditional `cp` command utility, but with some additional features: Displays the copy progress indicator, with estimated time, current file speed; logs of all actions; resume of interrupted copy processes.
* [GoCatGo](https://github.com/vaaleyard/gocatgo) - GoCatGo is another pastebin tool with a super focus on transparency.
* [PathPicker](https://facebook.github.io/PathPicker/) - A tool from Facebook that parses the output from a command and presents a UI to select files and directories, can be used to apply a command of a interactively selected files or to move across directories.
* [pcopy](https://github.com/binwiederhier/pcopy) - A temporary file host, nopaste and clipboard across machines. It can be used from the Web UI, via a CLI or without a client by using curl.
* [progress](https://github.com/Xfennec/progress) - A tool to monitor the progress of common Coreutils command-line tools (`cp`, `mv`, `dd`, `tar`, `rsync`, etc.); it uses an ncurses interface to display the percentage of data copied; it works by reading from system files and retrieving the necessary information for the estimation.
* [pycp](https://github.com/dmerejkowsky/pycp) - cp and mv with a progressbar.
* [rm-trash](https://github.com/nateshmbhat/rm-trash) - A "rm-trash" is meant to be used in place of rm system command in linux . This script will safely delete your files and put them in the trash for later retrieval.
* [Snoop](https://github.com/Mandrew0822/Snoop) - A command-line utility for Linux that provides information about files in a directory.
* [symlinks](https://github.com/brandt/symlinks) - Symlinks is a simple tool that helps find and remedy problematic symbolic links on a system.
* [TUI Archiver](https://www.nexus0.net/pub/sw/tuiarchiver/) - A TUI/CLI application to list / manage archives. Can be used stand-alone and has some features for integrating with TUI file managers
* [unix-permissions](https://github.com/ehmicky/unix-permissions) - Swiss Army knife for Unix permissions.
* [vidir](https://github.com/trapd00r/vidir) - vidir allows editing of the contents of a directory in a text editor.
* [xcp](https://github.com/tarka/xcp) - Extended cp.

## <a name="rm"></a>File deletion and trash bin (alternatives to rm)

Tools to manage the deletion of files/directories, often with the support of a trash can, i.e., the ability to restore deleted items.

* [Brash](https://github.com/zakariagatter/brash) - CLI Trash Manager in Pure Bash.
* [RecoverPy](https://github.com/PabloLec/RecoverPy) - RecoverPy is a powerful tool that leverages your system capabilities to recover lost files. Unlike others, you can not only recover deleted files but also overwritten data.
* [rip](https://github.com/nivekuil/rip) - Safe and ergonomic alternative to rm.
* [rmw](https://remove-to-waste.info/) - (ReMove to Waste) is a trashcan/recycle bin utility for the command line. It can move and restore files to and from directories specified in a configuration file.
* [trash-cli](https://github.com/sindresorhus/trash-cli) - Move files and folders to the trash.

## <a name="file-explorer"></a>File explorer and tree visualization

Show directory trees and navigate through the file system (but not full featured file managers).

* [alder](https://github.com/aweary/alder) - Directory tree visualizer.
* [browsr](https://github.com/juftin/browsr) - A pleasant file explorer that can browse the contents of local and remote filesystems with your keyboard or mouse; remotes include GitHub, over SSH, in AWS S3, Google Cloud Storage, or Azure Blob Storage.
* [Hop!](https://github.com/benrutter/hop) - File explorer designed to be fast, simple and user friendly, running on any operating system.
* [ictree](https://github.com/NikitaIvanovV/ictree) - Like tree but interactive.
* [Rust-Traverse](https://github.com/dmcg310/Rust-Traverse) - Rust traverse is a terminal based file explorer. It is inspired by the NNN file manager. It uses Ratatui for the terminal UI, with Crossterm for the terminal backend.
* [tere](https://github.com/mgunyho/tere) - Terminal file explorer that is a faster alternative to using cd and ls to browse folders in your terminal.
* [tre](https://github.com/dduan/tre) - `tree` command improved with git awareness, editor aliasing, and colors.
* [tree](http://mama.indstate.edu/users/ice/tree/) - "Recursive directory listing command that produces a depth indented listing of files".
* [twf](https://github.com/wvanlint/twf) - Standalone tree view file explorer.
* [xplr](https://github.com/sayanarijit/xplr) - A hackable, minimal, fast TUI file explorer, stealing ideas from nnn and fzf.

## <a name="find"></a>File finding (alternatives to find)

Search the filesystem looking for files with specific characteristics, e.g., names; alternatives to `find`.

* [bfs](https://github.com/tavianator/bfs) - A breadth-first version of the UNIX find command.
* [fd](https://github.com/sharkdp/fd) - A simple, fast and user-friendly alternative to find. Written in Rust.
* [Findpick](https://github.com/thingsiplay/findpick) - General purpose file picker combining "find" command with a fuzzy finder.
* [friendly-find](https://github.com/sjl/friendly-find) - Usable replacement for find.
* [gret](https://github.com/4imothy/gret) - A command-line utility designed to search through directories and files for a regex expression that matches.
* [happyfinder](https://github.com/hugows/hf) - (another) Fuzzy file finder for the command line.
* [plocate](https://plocate.sesse.net/) - A much faster locate; plocate is a locate based on posting lists, completely replacing mlocate with a much faster (and smaller) index.

## <a name="ls"></a>File listing (alternatives to ls)

List directory content and files, with colors or icons; alternatives to `ls`.

* [colorls](https://github.com/athityakumar/colorls) - A Ruby script that colorizes the `ls` output with color and icons.
* [exa](https://the.exa.website/) - Replacement for 'ls' written in Rust, with colors and several additional "views". As of today, the README says it is currently unmaintained and the only maintainer is unreachable. See `eza` for a maintained fork. 
* [eza](https://github.com/eza-community/eza) - eza is a modern, _maintained_ replacement for `ls`, built on `exa`.
* [ll](https://github.com/antonmedv/ll) - ls with git status.
* [lsd](https://github.com/lsd-rs/lsd) - This project is a rewrite of GNU ls with lot of added features like colors, icons, tree-view, more formatting options etc. The project is heavily inspired by the super colorls project.
* [nat](https://github.com/willdoescode/nat) - Complete replacement for the `ls` command.
* [pretty-ls](https://github.com/ix/pretty-ls) - Rust ls clone with pretty colors.
* [stree](https://github.com/orangekame3/stree) - A CLI tool designed to visualize the directory tree structure of an S3 bucket.
* [vivid](https://github.com/sharkdp/vivid) - A themeable LS_COLORS generator with a rich filetype datebase.

## <a name="file-manager"></a>File manager

Applications for interactively managing files and directories.

* [cfiles](https://github.com/mananapr/cfiles) - ncurses file manager written in C with vim like keybindings
* [clifm](https://github.com/leo-arch/clifm) - A CLI-based, shell-like, and non-curses terminal file manager written in C: simple, fast, extensible, and lightweight as hell.
* [felix](https://github.com/kyoheiu/felix) - TUI file manager with vim-like key mapping
* [fff](https://github.com/dylanaraps/fff) - Fast, simple file manager written in bash.
* [fman](https://github.com/nore-dev/fman) - TUI File Manager
* [goful](https://github.com/anmitsu/goful) - Goful is a CUI file manager written in Go.
* [hunter](https://github.com/rabite0/hunter) - Ranger-like file browser written in rust.
* [joshuto](https://github.com/kamiyaa/joshuto) - ranger-like terminal file manager
* [lf](https://github.com/gokcehan/lf) - lf (as in "list files") is a terminal file manager written in Go with a heavy inspiration from ranger file manager.
* [lfm](https://inigo.katxi.org/devel/lfm/) - (Last File Manager) is a file manager written in Python; it comes with lots of features, including 1-pane or 2-pane view, files filters and bookmarks, tree view, virtual file-systems to open compressed archives, search in files, customizable keybindings and themes.
* [Midnight Commander](http://www.midnight-commander.org/) - A visual file manager, full-screen text mode application that allows you to copy, move and delete files and whole directory trees and search for files; includes an internal viewer and editor.
* [ncursesFM](https://github.com/FedeDP/ncursesFM) - File manager written in C, rather complete in terms of features, especially lightweight and responsive.
* [nnn](https://github.com/jarun/nnn) - "The unorthodox terminal file manager" is a tiny, nearly 0-config and fast file manager supporting all the operations on files and directories.
* [projectable](https://github.com/dzfrias/projectable) - A TUI file manager built for projects.
* [ranger](https://ranger.github.io/) - Console file manager with vi key bindings, curses interface with a view on the directory hierarchy, comes with a file launcher that automatically determines which program to use for opening a given file type.
* [rnr](https://github.com/bugnano/rnr) - The RNR File Manager (RNR's Not Ranger) is a text based file manager that combines the best features of Midnight Commander and Ranger.
* [TUIFI Manager](https://github.com/GiorgosXou/TUIFIManager) - A cross-platform terminal-based termux-oriented file manager (and component), meant to be used with a Uni-Curses project or as is.
* [vifm](https://vifm.info/) - "ncurses based file manager with vi like keybindings/modes/options/commands/configuration, which also borrows some useful ideas from mutt" (cit.).
* [Yazi](https://github.com/sxyazi/yazi) - Blazing fast terminal file manager written in Rust, based on async I/O.

## <a name="file-renamer"></a>File renamers

Utilities to rename files and directories: address multiple items with one command, interactively edit the name within an editor, etc..

* [Bren](https://www.byteptr.com/bren/) - Bren is a command line tool for GNU/Linux (and many others). It has support for GNU Guile scripting. Bren is simple, fast and it's written in C.
* [F2](https://github.com/ayoisaiah/f2) - Cross-platform command-line tool for batch renaming files and directories quickly and safely.
* [massren](https://github.com/laurent22/massren) - Easily rename multiple files using your text editor.
* [mmv](https://github.com/itchyny/mmv) - Rename multiple files using your $EDITOR. The command name is named after multi-mv.
* [mmv-c](https://github.com/mcauley-penney/mmv-c) - Interactively rename files with your favorite editor.
* [moove](https://github.com/urin/moove) - Manipulate file names and locations using a text editor.
* [Musort](https://github.com/tdeerenberg/Musort) - Rename multiple audio/music files based on the ID3 tag at once.
* [nomino](https://github.com/yaa110/nomino) - Batch rename utility for developers.
* [rename](https://www.kernel.org/pub/linux/utils/util-linux/) - Included in `util-linux`, allows bulk rename of files with regex support.
* [rename-cli](https://github.com/jhotmann/node-rename-cli) - File renamer with TUI interface and preview.
* [renameutils](http://www.nongnu.org/renameutils/) - A set of programs to change file and directory names by editing them inplace, I find `imv` especially useful to edit a filename at the program prompt.
* [Tempren](https://github.com/idle-code/tempren) - A powerful file renaming utility that uses flexible template expressions to create new file paths and names.

## <a name="file-system"></a>File systems

File systems with specific features; e.g., the possibility to add tags and labels to files.

* [ipfs-deploy](https://github.com/ipfs-shipyard/ipfs-deploy) - Zero-Config CLI to Deploy Static Websites to IPFS [IPFS](https://en.wikipedia.org/wiki/InterPlanetary_File_System).
* [sshfs](https://github.com/libfuse/sshfs) - Locally mount a remote file-system through SSH and access files and directory as they would be on the local machine.  
* [TMSU](http://tmsu.org/) - A tool for tagging files, it provides a simple command line tool for applying tags and a virtual filesystem so that you can get a tag-based view of your files from within any other program.
* [wutag](https://github.com/vv9k/wutag) - CLI Tool for tagging and organizing files by tags.

## <a name="file-watch"></a>File watching for changes

Services that watch files for changes and perform actions when something happens.

* [Chokidar CLI](https://github.com/open-cli-tools/chokidar-cli) - Fast cross-platform command line utility to watch file system changes.
* [reflex](https://github.com/cespare/reflex) - Reflex is a small tool to watch a directory and rerun a command when certain files change.
* [rwatch](https://github.com/davidhfrankelcodes/rwatch) - A Rust re-implementation of the classic Unix watch command that allows you to run a command repeatedly and watch its output.
* [Viddy](https://github.com/sachaos/viddy) - Modern watch command. Time machine and pager etc.
* [watch](http://www.linfo.org/watch.html) - Periodically runs a command in the console while temporarily clearing the screen content; it makes it easy to check differences between the output of two subsequent commands; it provides "diff" functionality to highlight the changing characters between outputs.
* [watcher](https://github.com/sethigeet/watcher) - Watches all the files present in a directory and whenever a file is changed or a file is created/deleted from the directory, it runs a specified command.
* [watchexec](https://github.com/watchexec/watchexec) - Executes commands in response to file modifications.
* [wfh](https://github.com/kzys/wfh) - Continuously watches your local directories and rsync them against a remote host.

## <a name="financial"></a>Financial tools

Personal ledger trackers, currency converters, and tools to manage and track cryptocurrencies.

* [bits](https://github.com/jtraub91/bits) - CLI tool and pure Python library for Bitcoin.
* [cash-cli](https://github.com/xxczaki/cash-cli) - Convert Currency Rates.
* [Cloudcash](https://github.com/mrusme/cloudcash) - Check your cloud spending from the CLI, from Waybar, and from the macOS menu bar!
* [cointop](https://github.com/cointop-sh/cointop) - A fast and lightweight interactive terminal based UI application for tracking cryptocurrencies.
* [hledger](https://hledger.org/) - A is fast, reliable, free, multicurrency double-entry accounting software to track money, investments, cryptocurrencies, time, or any other quantifiable commodity; uses a future-proof plain text file format.
* [Invoice](https://github.com/maaslalani/invoice) - Generate invoices from the command line.
* [Lakshmi](https://github.com/sarvjeets/lakshmi) - Investing library and command-line interface inspired by the Bogleheads philosophy.
* [ledger](http://ledger-cli.org/) - A powerful, double-entry accounting system from the command-line; it uses a simple yet powerful text syntax to specify the items to account.
* [moeda](https://github.com/thompsonemerson/moeda) - A foreign exchange rates and currency conversion using the command line.
* [paycon](https://github.com/arcorion/paycon) - Converts pay amounts between different time units.
* [Quoter](https://github.com/frossm/quoter) - The console based stock quote tool.
* [Ticker](https://github.com/achannarasappa/ticker) - Terminal stock watcher and stock position tracker.

## <a name="font"></a>Font management

Utilities to manage system fonts and to generate text using ASCII-art-like characters.

* [FIGlet](http://www.figlet.org/) - Not exactly a font manager, but a nice program for making large letters out of ordinary text; an astonishing number of different fonts is available.
* [toilet](http://caca.zoy.org/wiki/toilet) - A program that tries to improve `FIGlet`; can load FIGlet fonts; supports Unicode input and output, colour fonts and output, and various output formats, including HTML, IRC and ANSI; uses `libcaca` to produce nice textual effects.

## <a name="funny"></a>Funny tools

Miscellaneous of tools that provide some funny/aesthetical functionality (animations, funny quotes, original message visualization, etc.).

* [ascii-movie](https://github.com/gabe565/ascii-movie) - Allows to play the ASCII art Star War movie locally or it can open a connection to play it over SSH or telnet.
* [asciicquarium](http://www.robobunny.com/projects/asciiquarium/html/) - Enjoy the mysteries of the sea from the safety of your own terminal!
* [Binary Clock](https://github.com/tom-on-the-internet/binary-clock) - Displays a clock where numbers are represented with blue and gray dots with binary encoding.
* [boxes](https://github.com/ascii-boxes/boxes) - Boxes is a command line filter program which draws ASCII art boxes around your input text.
* [cbonsai](https://gitlab.com/jallbrit/cbonsai) - A bonsai tree generator, written in C using ncurses. It intelligently creates, colors, and positions a bonsai tree.
* [cli-fireplace](https://github.com/dolsup/cli-fireplace) - Shows digital fireplace.
* [cmatrix](http://www.asty.org/cmatrix/) - ncurses program that display the scrolling lines found in the movie `The matrix`.
* [cowsay](https://en.wikipedia.org/wiki/Cowsay) - A program that generates a ASCII art of a cow with a bubble containing the specified message (I provide the Wikipedia link since at the moment the link to the author's homepage results to be unreachable).  
* [cowthink](https://en.wikipedia.org/wiki/Cowsay) - Same as `cowsay`, but uses a "think" bubble instead of a speech bubble.
* [ctree](https://github.com/gleich/ctree) - A Christmas tree right from your terminal.
* [daktilo](https://github.com/orhun/daktilo) - Turn your keyboard into a typewriter adding sounds at each keystroke.
* [Draw](https://github.com/maaslalani/draw) - draw is an simple drawing tool in the terminal. Hold your mouse down and move it across the screen to draw anything you want!
* [fortune](http://software.clapper.org/fortune/) - Generates random messages feched from a quotation database.  
* [kyun](https://github.com/file-acomplaint/kyun) - Kyun is a low productivity, low fidelity, low customizablity text editor that has its focus firm on user discomfort.
* [Limoji](https://github.com/GEROGIANNIS/Limoji) - Limoji is an open source tool that makes it easy to choose between hundreds of cool ASCII emoticons and share them with your friends.
* [LundukeHoliday](https://github.com/BryanLunduke/LundukeHoliday) - A simple Bash script that shows some animated, ASCII holiday decorations in your shell.
* [matrix-webcam](https://github.com/joschuck/matrix-webcam) - Take your video conference from within the matrix.
* [Maze Solver](https://github.com/Vlamonster/maze_solver_rust) - Generate, display and solve mazes in an animated way in the terminal.
* [neo](https://github.com/st3w/neo) - Recreates the digital rain effect from "The Matrix". Streams of random characters will endlessly scroll down your terminal screen.
* [No More Secrets](https://github.com/bartobri/no-more-secrets) - A command line tool that recreates the famous data decryption effect seen in the 1992 movie Sneakers.
* [paclear](https://github.com/orangekame3/paclear) - paclear is a clear command with pacman animation.
* [pokeget](https://github.com/talwat/pokeget) - A bash script you can use to display cool sprites of pokemon in your terminal.
* [ponysay](https://github.com/erkin/ponysay) - Pony rewrite of cowsay.
* [pyjokes](https://github.com/pyjokes/pyjokes) - One line jokes for programmers (jokes as a service).
* [Russhian Roulette](https://github.com/cyradotpink/russhian-roulette) - 1/6 chance of posting your SSH private key on pastebin (do you really want to try?).
* [sha256-animation](https://github.com/in3rsha/sha256-animation) - Animation of the SHA-256 hash function in your terminal.
* StarWars vision - See Star Wars in ASCII with ``telnet towel.blinkenlights.nl`` (server seems down recently - I leave the link in the hope that it will be resumed in the future).
* [Steam Locomotive](http://www.cyberciti.biz/tips/displays-animations-when-accidentally-you-type-sl-instead-of-ls.html) - A steam locomotive traverses the screen from right to left if `sl` is typed instead of `ls`.  
* [ternimal](https://github.com/p-e-w/ternimal) - Simulate a lifeform in the terminal.
* [yosay](https://github.com/yeoman/yosay) - Like cowsay, but for yeoman.

## <a name="fuzzy-finder"></a>Fuzzy finders

Fuzzy finders and generic option pickers in lists of strings.

* [choose](https://github.com/jagprog5/choose) - NCurses based token selector with a nice terminal user interface for selecting tokens. Selecting a line from the bash history is only one of its use cases.
* [fzf](https://github.com/junegunn/fzf) - (FuZzy Finder) is a general-purpose command-line finder with fuzzy search/filter capabilities, good integration with `vim`.
* [fzy](https://github.com/jhawthorn/fzy) - Better fuzzy finder.
* [lSel](https://github.com/unsigned-enby/lSel) - Simple no-fuss TUI selection menu for use in scripts.
* [luneta](https://github.com/fbeline/luneta) - Interactive filter that can be easily composed within any script.
* [percol](https://github.com/mooz/percol) - A Python script that "1) receives input lines from `stdin` or a file, 2) lists the input lines and waits for input that filter/select the line(s), 3) outputs the selected line(s) to `stdout`"; can be used to add interactivity to many regular shell commands.
* [pick](https://github.com/mptre/pick) - Utility that allows users to choose one option from a set of choices using an interface with fuzzy search functionality.  
* [pmenu](https://github.com/sgtpep/pmenu) - A dynamic terminal-based menu inspired by dmenu.
* [shmenu](https://github.com/duclos-cavalcanti/shmenu) - Menu TUI tool written solely in bash.
* [skim](https://github.com/lotabout/skim) - Fuzzy Finder in rust.
* [smenu](https://github.com/p-gen/smenu) - Started as a lightweight and flexible terminal menu generator, it evolved into a powerful and versatile CLI selection tool for interactive or scripting use.

## <a name="games"></a>Games

Board games, puzzles, roguelikes, role-play, adventures, card games, etc..

* [Angband](https://rephial.org/) - Angband is a free, single-player dungeon exploration game.
* [anonymine](https://oskog97.com/projects/anonymine/) - Curses mode minesweeper without guessing and other original features.
* [bastet](http://fph.altervista.org/prog/bastet.html) - (Bastard Tetris) implements the classical Tetris but with a logic to generate the next block which maximizes the difficulty for the player.  
* [blackjack](https://github.com/acidvegas/blackjack) - IRC bot to play blackjack.
* [Cataclysm: Dark Days Ahead](https://cataclysmdda.org/) - Open source turn-based survival RPG development project.
* [Cemetery Escape](https://github.com/tom-on-the-internet/cemetery-escape) - A game in which you must escape the cemetery. Search tombstones to find the key. Then head for the door, but watch out for ghosts.
* [chs](https://github.com/nickzuber/chs) - Play chess against the Stockfish engine in your terminal.
* [cli-chess](https://github.com/trevorbayless/cli-chess) - A highly customizable way to play chess in your terminal. Play online (via Lichess.org) and offline against the Fairy-Stockfish engine. All Lichess variants are supported.
* [clidle](https://github.com/ajeetdsouza/clidle) - Wordle, now over SSH.
* [crappybird-py](https://github.com/JonPizza/crappybird-py) - Flappy bird.
* [Dino](https://github.com/wldfngrs/chrome-dinosaur-terminal) - A C++ and ncurses rendering of the popular chrome dinosaur game on the terminal.
* [Durak](https://github.com/levkush/durak) - Durak card game for two in a terminal.
* [Dwarf fortress](http://www.bay12games.com/dwarves/) - A fantasy game using ASCII art graphical representation of the game environment, it features a rich environment with many options and possibilities.
* [escaping-figures-game-cli](https://github.com/akgondber/escaping-figures-game-cli) - Count figure's occurences in the escaping figures matrix.
* [Flapioca](https://github.com/kbrgl/flapioca) - A Flappy Bird-inspired terminal game written in Go.
* [freesweep](http://www.upl.cs.wisc.edu/~hartmann/sweep/) - A Minesweeper clone for the terminal which allows you to configure settings such as table rows and columns up to 1024x1024!), percentage of bombs, colors and also has a highscores table.
* [Frotz](https://davidgriffith.gitlab.io/frotz/) - Frotz is an interpreter for Infocom games and other Z-machine games.
* [gambit](https://github.com/maaslalani/gambit) - Chess board in your terminal.
* [GameShell](https://github.com/phyver/GameShell) - GameShell was devised as a tool to help university students to engage with a real shell, in a way that encourages learning while also having fun.
* [go-sweep](https://github.com/maxpaulus43/go-sweep) - Minesweeper game in the command line programmed in Go.
* [gof-rs](https://github.com/omagdy7/gof-rs) - Game of life rendered in your terminal with over 500+ unique patterns to choose from.
* [greed](http://www.catb.org/~esr/greed/) - A game of consumption. Eat as much as you can before munching yourself into a corner.
* [guess-word-cli](https://github.com/akgondber/guess-word-cli) - Find out a source word which characters was shuffled and moreover an extra character was added to bring some complexity.
* [hangman](https://github.com/braheezy/hangman) - A Go TUI Hangman game built with the lovely BubbleTea framework.
* [Language-games](https://github.com/Hellisotherpeople/Language-games) - Dead simple games made with word vectors.
* [mazter](https://github.com/Canop/mazter) - A maze in your terminal.
* [minesweeper](https://github.com/gazpachoking/minesweeper) - Cross-platform terminal based minesweeper.
* [Minesweeper Game](https://github.com/omerkarabacak/minesweeper) - A small command line Minesweeper Game.
* [nc2048](https://github.com/t0xk/nc2048) - A ncurses 2048 game that can be played in the terminal.
* [Nethack](http://nethack.org/) - Single player rogue-like dungeon exploration game.
* [Oldrunner](http://culot.org/public/Code/oldrunner.html) - Character-based remake of Lode Runner, includes all the original 150 levels.
* [othello-cli](https://github.com/LelsersLasers/othello-cli) - othello-cli is a cli version of Othello (Reversi) written in Rust. You can play against another player, the AI, or watch two AIs play each other.
* [Pokete](https://github.com/lxgr-linux/pokete) - A terminal based Pokemon like game.
* [rooshk](https://github.com/cmspeedrunner/rooshk) - A command line game in which you act as god over a sandbox world.
* [rpg-cli](https://github.com/facundoolano/rpg-cli) - Your filesystem as a dungeon!
* [sku](https://github.com/fedeztk/sku) - Simple TUI written in go to play sudoku in the terminal.
* [Slash'EM](http://slashem.sourceforge.net/) - Rogue-like game derived from `nethack` offering extra features, monsters, and items; includes a GUI version.
* [Solitaire TUI](https://github.com/brianstrauch/solitaire-tui) - Klondike solitaire for the terminal.
* [sssnake](https://github.com/AngelJumbo/sssnake) - (Smart and sexy snake) The classic snake game for the terminal that can plays itself and be use like a screensaver.
* [terdle](https://github.com/neelkarma/terdle) - Wordle implemented in Rust.
* [Terminal Phase](https://dustycloud.org/blog/terminal-phase-1.0/) - A space shooter game you can play in your terminal.
* [Terminal Roulette](https://github.com/levkush/TerminalRoulette) - Your own roulette table in the terminal.
* [terminal_board_games](https://github.com/salt-die/terminally_bored_terminal_board_games) - Board games for the terminal.
* [terminordle](https://github.com/HP4k1h5/terminordle) - Inspired by the popular online game wordle made, you can play a pretty close replica of the original locally or multiplayer over the network.
* [usolitaire](https://github.com/eliasdorneles/usolitaire) - Solitaire in your terminal.
* [Wordle Solver](https://gitlab.com/christosangel/wordle-solver) - A bash script that can solve wordle riddles.
* [wordle-curses](https://github.com/knosmos/wordle-curses) - A simple TUI wordle game with curses.
* [Words](https://github.com/ludovicianul/words) - A set of word-based puzzle games for the CLI while you wait for the build to run.

## <a name="git"></a>Git and accessories

Tools to support and extend the functionalities of the `git` version tracker.

* [BFG Repo-Cleaner](https://github.com/rtyley/bfg-repo-cleaner) - Removes large or troublesome blobs like git-filter-branch does, but faster.
* [czg](https://github.com/Zhengqbbb/cz-git) - Interactively generate standardized commit messages.
* [Export Pull Requests](https://github.com/sshaw/export-pull-requests/) - Export pull requests and/or issues to a CSV file. Supports GitHub, GitLab, and Bitbucket.
* [forgit](https://github.com/wfxr/forgit) - A utility tool powered by fzf for using git interactively.
* [fzf-git.sh](https://github.com/junegunn/fzf-git.sh) - bash and zsh key bindings for Git objects, powered by fzf.
* [gh-f](https://github.com/gennaro-tedesco/gh-f) - The ultimate, compact and snappy fzf extension for gh cli.
* [gh-s](https://github.com/gennaro-tedesco/gh-s) - Search github repositories interactively.
* [gh-stars](https://github.com/aymanbagabas/gh-stars) - A GitHub CLI extension to show repository stargazers.
* [git](https://git-scm.com/) - The winner across all the existing file versioning tools, distributed versioning, fully controllable from the command-line, plenty of configuration and usage options, behind a number of related project that leverage git as backend.
* [git absorb](https://github.com/tummychow/git-absorb/) - git commit --fixup, but automatic.
* [Git Auto Sync](https://github.com/GitJournal/git-auto-sync) - Automatically commits changes to a git repository, and always keep that repo up to date.
* [git commander](https://github.com/golbin/git-commander) - A git tool with an easy interactive terminal interface.
* [Git Commit Vanity Hash Solver](https://github.com/trichner/gitc0ffee) - Neat tool to find a 'vanity' hash for a given git commit. Make all your commits hashes start with the prefix c0ffee, cafe, badc0de5 or whatever makes you happy!
* [git-all-branches](https://github.com/zacanger/git-all-branches) - Improved visualization of git branches (`git branch -a`).
* [git-annex](https://git-annex.branchable.com/) - Manages files with `git`, without checking the file contents into git; very useful to manage large/binary files.
* [git-booster-cli](https://github.com/akgondber/git-booster-cli/) - Improve your git workflow with customizable and runnable blocks.
* [git-cliff](https://github.com/orhun/git-cliff) - A highly customizable Changelog Generator that follows Conventional Commit specifications.
* [git-cz](https://github.com/streamich/git-cz) - Semantic Git commits.
* [git-extras](https://github.com/tj/git-extras) - Little git extras like git-ignore, git-setup, git-changelog, git-release, git-effort and more.
* [git-fuzzy](https://github.com/bigH/git-fuzzy) - Interactive `git` with the help of `fzf`.
* [git-identity](https://github.com/cookiengineer/git-identity) - Automated git alias management.
* [git-peek](https://github.com/Jarred-Sumner/git-peek) - git peek is the fastest way to open a remote git repository in your local text editor.
* [git-remote-aws](https://github.com/nathants/git-remote-aws) - Management of encrypted git hosting.
* [git-secret](https://github.com/sobolevn/git-secret) - A bash tool which stores private data inside a git repo; it uses users' public keys, allowing trusted users to access encrypted data using pgp and their secret keys.
* [git-stats](https://github.com/IonicaBizau/git-stats) - Local git statistics including GitHub-like contributions calendars.
* [gita](https://github.com/nosarthur/gita) - A command-line tool to manage multiple git repos.
* [Gitea](https://gitea.com/) - Single binary self-hosted Git service.
* [gitlab-cli](https://github.com/vishwanatharondekar/gitlab-cli) - Create GitLab merge requests.
* [gitnr](https://github.com/reemus-dev/gitnr) - Create `.gitignore` files using one or more templates from TopTal, GitHub or your own collection.
* [gitsummary](https://github.com/glenreesor/gitsummary) - A better git status taht lists stashes, file statuses, branch list, all nicely formatted with color.
* [GitUI](https://github.com/extrawurst/gitui) - The comfort of a git GUI but right in your terminal, with keyboard only control, scalable UI, and features all the necessary operations of git.
* [grv](https://github.com/rgburke/grv) - Git Repository Viewer - A terminal based interface for viewing Git repositories. It allows refs, commits and diffs to be viewed, searched and filtered.
* [Kusa](https://github.com/Ryu0118/Kusa) - Displays GitHub contribution graphs.
* [Lazygit](https://github.com/jesseduffield/lazygit) - A simple terminal UI for git commands that simplify the execution of many operations making them interactive.
* [onefetch](https://github.com/o2sh/onefetch) - Git repository summary on your terminal.
* [rcz](https://github.com/Cassin01/rcz) - A tool to write a commit message based on “Conventional Commits”.
* [sad](https://github.com/ms-jpq/sad) - CLI search and replace. Show you a nice diff of proposed changes before you commit them.
* [semantic-git-commit-cli](https://github.com/JPeer264/node-semantic-git-commit-cli) - Ensure semantic commits messages. With emoji support.
* [Soft Serve](https://github.com/charmbracelet/soft-serve) - Self-hostable Git server for the command line. One distinguished feature is the possibility to create new repositories with a push.
* [stargazer](https://github.com/gennaro-tedesco/stargazer) - Github stats from the command line.
* [tig](https://github.com/jonas/tig) - An ncurses-based text-mode interface for `git` that can act as a repository browser, but can also assist in staging changes for commit at chunk level.
* [travelgrunt](https://github.com/ivanilves/travelgrunt) - cd inside [mono]repos without fatigue.

## <a name="graphics"></a>Graphics

Applications to process images, colors and ASCII art.

* [Aewan](http://aewan.sourceforge.net/) - Aewan is a multi-layered ASCII graphics/animation editor. It produces stand-alone cat-able ASCII art files and an easy-to-parse format for integration into terminal applications.
* [Artem](https://github.com/FineFindus/artem) - Convert images from multiple formats (jpg, png, webp, etc.) to ASCII art, written in Rust.
* [ArTTY](https://github.com/mjwhitta/artty) - Pixel art with optional system info, similar to neofetch.
* [BlockPaint](https://github.com/wooster0/blockpaint) - BlockPaint is a painting program that allows you to draw pixel graphics in the terminal using the mouse.
* [catnip](https://github.com/sweetbbak/catnip) - An Image picker using pure bash (C and Go version in the works) and kittys icat and Chafa's Sixel protocol.
* [chafa](https://github.com/hpjansson/chafa) - Terminal graphics for the 21st century.
* [cli-mandelbrot](https://github.com/danyshaanan/cli-mandelbrot) - A cli for traversing the Mandelbrot fractal.
* [D2](https://github.com/terrastruct/d2) - D2 is a modern diagram scripting language that turns text to diagrams.
* [deviceframe](https://github.com/c0bra/deviceframe) - Put device frames around mobile/web/progressive app screenshots.
* [gifgen](https://github.com/lukechilds/gifgen) - Simple high quality GIF encoding.
* [gifsicle](https://github.com/kohler/gifsicle) - Create, manipulate, and optimize GIF images and animations.
* [givegif](https://github.com/passy/givegif) - GIFs on the command line.
* [GraphicsMagick](http://www.graphicsmagick.org/) - Swiss army knife of image processing.
* [Graphviz](https://graphviz.org/) - Graphviz is open source graph visualization software. It contains several command line tools to generate and manipulate graphs.
* [haylxon](https://github.com/pwnwriter/haylxon) - Blazing-fast tool to grab screenshots of your domain list right from terminal.
* [ImageMagick](http://www.imagemagick.org/script/index.php) - Software suite to create, edit, compose, or convert bitmap images; it handles many file formats (including PDF and SVG) and provides processing tools to "resize, flip, mirror, rotate, distort, shear and transform images, adjust image colors, apply various special effects, or draw text, lines, polygons, ellipses and Bezier curves".
* [img2ascii](https://github.com/JosefVesely/Image-to-ASCII) - Convert images to ASCII art.
* [imgcat](https://github.com/trashhalo/imgcat) - Tool to output images in the terminal. Built with bubbletea.
* [imgp](https://github.com/jarun/imgp) - A command line image resizer and rotator for JPEG and PNG images. It can resize (or thumbnail) and rotate thousands of images in a go, at lightning speed, while saving significantly on storage.
* [inklayers](https://github.com/toolleeo/inklayers) - A command line program that exports layers from an SVG file. It can be used to create slide shows by editing a single SVG file.
* [jp2a](https://csl.name/jp2a/) - Command-line tool that converts images to ASCII art in the Linux terminal.
* [kakikun](https://github.com/file-acomplaint/kakikun) - Kakikun is a tool to paint, draw and create ASCII art in your terminal using unicode characters.
* [Korkut](https://github.com/oguzhaninan/korkut) - Quick and simple image processing with the following functions: optimize, convert, crop, resize, rotate, watermark, flip.
* [LinuxLogo](https://sourceforge.net/projects/linuxlogo/) - Display the Linux distribution logo in ASCII format.
* [mandelbrot-cli](https://github.com/MicheleFiladelfia/mandelbrot-cli) - Multiplatform terminal mandelbrot set explorer.
* [MapSCII](https://github.com/rastapasta/mapscii) - A Braille & ASCII world map renderer for your console
* [Mercator](https://github.com/mrusme/mercator) - OpenStreetMap but as terminal user interface (TUI) program.
* [pastel](https://github.com/sharkdp/pastel) - A command-line tool to generate, analyze, convert and manipulate colors.
* [rclip](https://github.com/yurijmikhalevich/rclip) - AI-Powered Command-Line Photo Search Tool.
* [scrot](https://github.com/dreamer/scrot) - A simple CLI tool to capture screenshots.  
* [svgcleaner](https://github.com/RazrFalcon/svgcleaner) - Clean up your SVG files from the unnecessary data.
* [SVGO](https://github.com/svg/svgo) - SVG Optimizer is a Node.js-based tool for optimizing SVG vector graphics files.
* [TermImg](https://github.com/srlehn/termimg) - termimg tries to draw images into terminals. The rectangular drawing area is given in cell coordinates (not pixels). Origin is the upper left corner.
* [terminal-art](https://github.com/Eric-Lennartson/terminal-art) - Art made in the terminal: rotating cube.

## <a name="history"></a>History management

Programs to replace or improve the management of command line history.

* [atuin](https://github.com/ellie/atuin) - Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands. Additionally, it provides optional and fully encrypted synchronisation of your history between machines, via an Atuin server.
* [Bevel](https://github.com/NorfairKing/bevel) - Command line history in an SQLite database for effective re-use.
* [hiSHtory](https://github.com/ddworken/hishtory) - A better shell history that stores context (directory, succeeded or failed, how long it took, etc). The history is stored locally and end-to-end encrypted for syncing to other computers.
* [hstr](https://github.com/dvorka/hstr) - A tool for managing the history, powerful visual search and execution of previous commands, history editing capabilities.

## <a name="markdown"></a>Markdown

Utilities to display, convert and reformat Markdown files.

* [DocToc](https://github.com/thlorenz/doctoc) - Generates table of contents for markdown files inside local git repository. Links are compatible with anchors generated by github or other sites.
* [Frogmouth](https://github.com/Textualize/frogmouth) - A Markdown viewer / browser for the terminal.
* [glow](https://github.com/charmbracelet/glow) - Render markdown on the CLI, with pizzazz!
* [Grip](https://github.com/joeyespo/grip) - GitHub Readme Instant Preview - Preview markdown files as GitHub would render them.
* [lowdown](https://kristaps.bsd.lv/lowdown/) - Markdown translator (HTML5, roff, LaTeX, gemini, OpenDocument, and terminal output)
* [mdBook](https://github.com/rust-lang/mdBook) - Create book from markdown files.
* [mdcat](https://github.com/swsnr/mdcat) - cat for Markdown
* [mdformat](https://github.com/executablebooks/mdformat) - Mdformat is an opinionated Markdown formatter that can be used to enforce a consistent style in Markdown files.
* [mdt](https://github.com/robolab-pavia/mdt) - MarkDown in the Terminal. A markdown viewer with themes defined by JSON files and interactive mode to open links and word-wrapping adaptable to the terminal width.
* [Terminal Markdown Viewer](https://github.com/axiros/terminal_markdown_viewer) - Python based Markdown viewer for the terminal.
* [Textual Markdown Browser](https://github.com/willmcgugan/textual-markdown) - Experimental "Markdown browser" for the terminal, built with Textual.

## <a name="networking"></a>Networking

Networks and communication tools: bandwidth monitoring, packet inspection, remote connection, VPNs, terminal sharing, etc..

* [bandwhich](https://github.com/imsnif/bandwhich) - Terminal bandwidth utilization tool.
* [bluetuith](https://github.com/darkhz/bluetuith) - A TUI-based Bluetooth connection manager, which can interact with Bluetooth adapters and devices. It aims to be a replacement to most Bluetooth managers, like blueman.
* [bore](https://github.com/ekzhang/bore) - A simple CLI tool for making tunnels to localhost.
* [darkhttpd](https://unix4lyfe.org/darkhttpd/) - Darkhttpd is a simple, fast HTTP 1.1 web server for static content. It does not support PHP or CGI etc but is designed to serve static content, which it does very well.
* [dog](https://github.com/ogham/dog) - dog is a command-line DNS client. It has colourful output, understands normal command-line argument syntax, supports the DNS-over-TLS and DNS-over-HTTPS protocols, and can emit JSON.
* [echo](https://github.com/devem-tech/echo) - Speedy API emulation facilitated by a reverse proxy and mock json server.
* [ejabberd](https://www.ejabberd.im/) - ejabberd is an XMPP application server and an MQTT broker, written mainly in the Erlang programming language.
* [geoiplookup](https://github.com/maxmind/geoip-api-c) - A little application to find geographical and network information of an IP address based no the geoip C API.
* [gping](https://github.com/orf/gping) - Ping, but with a graph.
* [hflow](https://github.com/comradequinn/hflow) - A command-line, debugging http/s proxy server.
* [ipcalc](http://jodies.de/ipcalc) - Takes an IP address and netmask and calculates the resulting broadcast, network, Cisco wildcard mask, and host range.
* [mitmproxy](https://mitmproxy.org/) - An interactive HTTPS proxy.
* [mosh](https://mosh.org/) - Remote SSH client that achieve good responsiveness in presence of intermittent connectivity and roaming.
* [mtr](https://github.com/traviscross/mtr) - mtr combines the functionality of the 'traceroute' and 'ping' programs in a single network diagnostic tool.
* [neoss](https://github.com/PabloLec/neoss) - User-friendly and detailed socket statistics with a Terminal UI.
* [oha](https://github.com/hatoo/oha) - oha is a tiny program that sends some load to a web application and show realtime tui.
* [Optic](https://www.useoptic.com/) - Optic's Open Source tools make OpenAPI and API-first practices easy for any team to adopt.
* [Prosody](https://prosody.im/) - Prosody is a modern XMPP communication server. It aims to be easy to set up and configure, and efficient with system resources.
* [PSSH](https://code.google.com/archive/p/parallel-ssh/) - PSSH provides parallel versions of OpenSSH and related tools. Included are pssh, pscp, prsync, pnuke, and pslurp. The project includes psshlib which can be used within custom applications.
* [quark](https://tools.suckless.org/quark/) - quark is an extremely small and simple HTTP GET/HEAD-only web server for static content.
* [quickserve](https://github.com/haileys/quickserve) - Quickserve is a very simple HTTP server written in Python that is intended for quickly sharing files on an ad-hoc basis. Aside from opening a port in your firewall if you have one, quickserve requires no set-up and should work with no hassle.
* [redive](https://github.com/neelkarma/redive) - Trace URL redirections in the terminal.
* [rtop](http://www.rtop-monitor.org/) - rtop is a simple, agent-less, remote server monitoring tool that works over plain SSH. Written in golang, it does not need any software to be installed on the server that you want to monitor. It works by establishing an SSH session, and running commands on the remote server to collect system metrics.
* [Rustcat](https://github.com/robiot/rustcat) - Netcat Alternative in Rust.
* [serve](https://github.com/vercel/serve) - Serves a static site, single page application, or just a static file, and provides a neat interface for listing the directory's contents.
* [SMBScan](https://github.com/jeffhacks/smbscan) - SMBScan is a tool to enumerate file shares on an internal network.
* [sngrep](https://github.com/irontec/sngrep) - Ncurses SIP Messages flow viewer.
* [speedtest-net](https://github.com/ddsol/speedtest.net) - Test internet connection speed and ping using speedtest.net.
* [ssh-menu](https://github.com/antonjah/ssh-menu) - A very simple terminal tool that renders an interactive menu with your ssh profiles listed.
* [sshed](https://github.com/trntv/sshed) - sshed is a ssh config editor and bookmarks manager.
* [sshs](https://github.com/quantumsheep/sshs) - Terminal user interface for SSH.
* [sshto](https://github.com/vaniacer/sshto) - Small bash script to manage your ssh connections. It builds menu (via dialog) from your ~/.ssh/config. It can not only connect but also to run commands, copy files, tunnel ports.
* [sshuttle](https://github.com/sshuttle/sshuttle) - Transparent proxy server that works as a poor man's VPN. Forwards over ssh. Doesn't require admin. Works with Linux and MacOS. Supports DNS tunneling.
* [sslh](https://github.com/yrutschle/sslh) - A ssl/ssh multiplexer (Applicative Protocol Multiplexer) that allows, for example, to share SSH and HTTPS on the same port.
* [SSM](https://github.com/elliot40404/ssm) - A simple SSH manager.
* [termishare](https://github.com/qnkhuat/termishare) - Peer to peer terminal sharing.
* [Termshark](https://termshark.io/) - A terminal UI for tshark, inspired by Wireshark.
* [TGORQ](https://github.com/vitor-augusto1/tgorq) - Terminal GO ReQuest (TGORQ) is a Vim-like lightweight CLI tool for performing HTTP requests.
* [TStream](https://github.com/qnkhuat/tstream) - Live streaming from the terminal. Requires the connection to a central server, from which the streaming is dispatched.
* [ttfb](https://github.com/phip1611/ttfb) - ttfb is a CLI-Tool to measure the TTFB (time to first byte) of HTTP requests.
* [ttyd](https://github.com/tsl0922/ttyd) - Share your terminal over the web.
* [tunblkctl](https://github.com/azhuchkov/tunblkctl) - Command-line frontend for Tunnelblick.
* [Tunnelmole](https://github.com/robbie-cahill/tunnelmole-client) - Connect to local servers from anywhere.
* [websocat](https://github.com/vi/websocat) - Netcat, curl and socat for WebSockets.
* [Wishlist](https://github.com/charmbracelet/wishlist) - With Wishlist you can have a single entrypoint for multiple SSH endpoints.
* [xiringuito](https://github.com/ivanilves/xiringuito) - VPN made easy! No configuration. No VPN servers. No hassle. Using SSH capabilities.
* [xxh](https://github.com/xxh/xxh) - Bring your favorite shell wherever you go through the ssh.

## <a name="note-taking"></a>Note taking

Tools to take, organize and manage notes.

* [cadmus](https://github.com/RyanGreenup/cadmus) - Shell Scripts to Facilitate Effective Note Taking.
* [Clipboard](https://getclipboard.app/) - An easy-to-use information management tool that acts like an external brain.
* [dn](https://github.com/tomlockwood/dn) - Daily notes command line tool.
* [dnote](https://github.com/dnote/dnote) - A simple command line notebook for the terminal. It also offers a seamless multi-device sync and a web interface.
* [eureka](https://github.com/simeg/eureka) - Store your ideas without leaving the terminal.
* [Geeknote](https://github.com/jeffkowalski/geeknote) - A command line client for Evernote that can be use on Linux, FreeBSD and OS X.
* [idea](https://github.com/IonicaBizau/idea) - A lightweight tool for keeping ideas in a safe place quick and easy.
* [jot](https://github.com/araekiel/jot) - Jot is a feature-stripped version of Obsidian focused on rapid note management through the terminal. It uses the same format of storage as Obsidian.
* [journalC](https://github.com/Dr-42/journalC) - A simple encrypted terminal jounaling book.
* [jrnl](https://github.com/jrnl-org/jrnl) - jrnl is a simple journal application for the command line to easily create, search, and view journal entries; journals are stored as human-readable plain text, and can also be encrypted using AES encryption.
* [kb](https://github.com/gnebbia/kb) - A minimalist knowledge base manager.
* [meudeus](https://github.com/dj8yfo/meudeus) - A skim-based `*.md` explore and surf tool.
* [nb](https://github.com/xwmx/nb) - A command line and local web note-taking, bookmarking, archiving, and knowledge base application.
* [Noted](https://github.com/torbratsberg/noted) - Notes library, with viewer and shortcuts to add, delete and edit notes.
* [NoteSH](https://github.com/Cvaniak/NoteSH) - Sticky notes App in the Terminal, built with Textual, an amazing TUI framework!
* [posce](https://github.com/vdt/posce) - A note-taking toolkit for your command line.
* [sncli](https://github.com/insanum/sncli) - A Python application that gives you access to your Simplenote account via the command line.
* [Standard Unix Notes](https://github.com/Standard-Unix-Notes/unix-notes) - GPG Encrypted Notes/Notebook manager for BSD/Linux.
* [Terminal velocity](https://vhp.github.io/terminal_velocity/) - A fast, cross-platform note-taking application for the UNIX terminal.
* [TUI-Journal](https://github.com/AmmarAbouZor/tui-journal) - Terminal-based application written in Rust that allows you to write and manage your journal/notes with a nice user interface.
* [zk](https://github.com/mickael-menu/zk) - zk is a command-line tool helping you to maintain a plain text Zettelkasten or personal wiki.

## <a name="office"></a>Office tools

Programs to manage spreadsheets and to make presentations.

* [DeckTape](https://github.com/astefanutti/decktape) - DeckTape is a high-quality PDF exporter for HTML presentation frameworks.
* [Lotus 1-2-3 for Linux](https://github.com/taviso/123elf) - A native port of Lotus 1-2-3 Release 3 to Linux.
* [mdp](https://github.com/visit1985/mdp) - A command-line based markdown presentation tool.
* [PDFtk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) - PDFtk is a simple tool for doing everyday things with PDF documents.
* [presenterm](https://github.com/mfontanini/presenterm) - A terminal slideshow tool.
* [sc-im](https://github.com/andmarti1424/sc-im) - Spreadsheet Calculator Improvised -- An ncurses spreadsheet program for terminal. It is rich in functionalities, but the syntax of functions and other details are different from the common spreadsheets such as Excel and Calc, making difficult to "re-cycle" existing knowledge on these programs to work proficiently with sc-im. Neverthless, a nice piece of software."
* [sent](https://tools.suckless.org/sent/) - Simple plaintext presentation tool.
* [Slideck](https://github.com/piotrmurach/slideck) - Present Markdown-powered slide decks in the terminal.
* [Slides](https://github.com/maaslalani/slides) - Terminal based presentation tool.
* [Teapot](https://www.syntax-k.de/projekte/teapot/) - Compact ncurses-based spreadsheet with original syntax, 3D-style and built-in functions.
* [tpp](http://www.ngolde.de/tpp.html) - (text presentation program) a ncurses Ruby program that allows to produce nice text-based presentation with simple markup language.

## <a name="online"></a>Online search and resources

Tools that interact with online resources to provide their services, e.g., searches, wiki, etc..

* [arch-wiki](https://github.com/deadhead420/arch-wiki) - Search the Arch Wiki anywhere from the command line.  
* [Awesome CLI](https://github.com/umutphp/awesome-cli) - Awesome CLI is a simple command line tool to give you a fancy command line interface to dive into Awesome lists.
* [Awesome Finder](https://github.com/mingrammer/awesome-finder) - Search the awesome lists from the command line.
* [ddgr](https://github.com/jarun/ddgr) - A command line utility to search DuckDuckGo (html version) from the terminal.
* [Fjira](https://github.com/mk-5/fjira) - The fuzziest Jira command line tool in the world.
* [ghfetch](https://github.com/orangekame3/ghfetch) - ghfetch is a CLI tool to fetch GitHub user information and show like neofetch.
* [googler](https://github.com/jarun/googler) - Google Search, Google Site Search, Google News from the terminal.
* [magic-tape](https://gitlab.com/christosangel/magic-tape) - Magic-tape is an image supporting fuzzy finder command line interface YouTube client.
* [pockyt](https://github.com/achembarpu/pockyt) - Read, manage, and automate the collection of articles in [Pocket](https://getpocket.com), an application for managing a reading list of articles from the Internet.
* [Seashells](https://seashells.io/) - Pipe output to the web.
* [Shreddit](https://github.com/x89/Shreddit) - Remove your comment history on Reddit as deleting an account does not do so.
* [so](https://github.com/samtay/so) - Terminal interface for Stack Overflow.
* [socialscan](https://github.com/iojw/socialscan) - Python library and CLI for accurately querying username and email usage on online platforms.
* [socli](https://github.com/gautamkrishnar/socli) - Stack overflow command line client written in Python.  Search and browse stack overflow without leaving the terminal 
* [wikit](https://github.com/KorySchneider/wikit) - A command line program for getting Wikipedia summaries easily.

## <a name="organizers"></a>Organizers and calendars

Calendar and appointment managers.

* [addrb](https://github.com/mrusme/addrb) - A lightweight CLI / TUI address book that supports CardDAV.
* [avail](https://github.com/mufeez-amjad/avail) - Find available times between all your calendars.
* [buku](https://github.com/jarun/buku) - A powerful bookmark manager written in Python3 and SQLite3.
* [Calcure](https://github.com/anufrievroman/calcure) - Modern TUI calendar and task manager with customizable interface.
* [calcurse](https://calcurse.org/) - A calendar and scheduling application for the command line. It helps keep track of events, appointments and everyday tasks.
* [caldr](https://github.com/mrusme/caldr) - A lightweight CLI / TUI calendar that supports CalDAV.
* [gcalcli](https://github.com/insanum/gcalcli) - CLI to access Google Calendars; allows to do the main tasks: create, delete, and list events.
* [Girok](https://github.com/noisrucer/girok) - A powerful and beautiful CLI scheduler.
* [goobook](https://gitlab.com/goobook/goobook) - The purpose of GooBook is to make it possible to use your Google Contacts from the command-line and from MUAs such as Mutt.  It can be used from Mutt the same way as abook.
* [icsp](https://github.com/loteoo/icsp) - Command-line iCalendar (.ics) to CSV utility.
* [khal](https://github.com/pimutils/khal) - CLI and terminal calendar program, able to synchronize with CalDAV servers through [vdirsyncer](https://github.com/pimutils/vdirsyncer).
* [khard](https://github.com/lucc/khard) - Console carddav client written in Pyhton.  
* [pal](http://palcal.sourceforge.net/) - Calendar program for Unix/Linux systems that can keep track of events; custom, plain text storage format; interesting and fully functional.
* [peroutine](https://github.com/UlyssesZh/peroutine) - Remind you of periodical events. The period can be any positive integer of days, so work around the fact that the number of days in a week is prime.
* [plann](https://github.com/tobixen/plann) - Command-line interface to online calendars.
* [ppl addressbook](http://ppladdressbook.org/) - `ppl` is free software made out of other free software.  It's built on top of Ruby and Git, and the completely free vcard address book format.
* [Remind](https://dianne.skoll.ca/projects/remind/) - Calendar program with possibility to set complex rules to define events; custom, powerful text-based storage format.
* [remint](https://sr.ht/~mlaparie/remint/) - A simple terminal UI wrapper for D. Skoll's Remind calendar program
* [tz](https://github.com/oz/tz) - tz helps you schedule things across time zones. It's an interactive TUI program that displays time across the time zones of your choosing.
* [vdirsyncer](https://github.com/pimutils/vdirsyncer) - CalDAV synchronization program.
* [Wyrd](http://freecode.com/projects/wyrd/) - Curses front-end for [Remind](https://www.roaringpenguin.com/products/remind) written in OCaml with vertically scrollable time table.  

## <a name="package-manager"></a>Package managers

Package managers to manage/install/uninstall software packages, as source code or binaries.

* [aptitude](https://salsa.debian.org/apt-team/aptitude) - A TUI front-end to APT, the Debian package manager.
* [asdf](https://asdf-vm.com/) - Manage multiple runtime versions with a single CLI tool.
* [bin](https://github.com/marcosnils/bin) - Manages binary files downloaded from different sources.
* [cli-tools-info](https://github.com/Lilja/cli-info) - An overview of your CLI tools, if they are installed and what version they are on.
* [getghrel](https://github.com/kavishgr/getghrel) - A user-friendly command-line tool that fetches and installs the latest release assets from Github for MacOS and Linux; it automatically detects your operating system and architecture, downloads the relevant binary, and unpacks it, ensuring a hassle-free experience.
* [hysp](https://github.com/pwnwriter/hysp) - An independent package manager that every hacker deserves.
* [JAPM](https://github.com/TheAlexDev23/japm) - A package manager that uses curses to provide a friendly UI
* [nala](https://gitlab.com/volian/nala) - apt package manager front-end with cleaner interface.
* [pypi-command-line](https://github.com/wasi-master/pypi-command-line) - A powerful, colorful, beautiful command-line-interface for pypi.org.
* [Shell Bling Ubuntu](https://github.com/hiAndrewQuinn/shell-bling-ubuntu) - A few scripts to be run on a fresh-off-the-presses Ubuntu VM, in order to get its shell nice 'n purdy.
* [stew](https://github.com/marwanhawari/stew) - An independent package manager for compiled binaries.

## <a name="password-manager"></a>Password managers

Programs to store and manage collections of password and other login/authentication information.

* [Bitwarden CLI](https://bitwarden.com/help/cli/) - Command-line interface for Bitwarden, a multi-platform password manager targeted to companies and enterprises.
* [cpass](https://github.com/xlucn/cpass) - Another console UI for pass.
* dpg - The Deterministic Password Generator - Generates passwords based on a master password and the indication of the website/service/username, without the need of storing anything.
* [gopass](https://www.gopass.pw/) - gopass is a rewrite of the pass password manager in Go with the aim of making it cross-platform and adding additional features. The target audience are professional developers and sysadmins (and especially teams of those) who are well versed with a command line interface.
* [hide](https://github.com/whatl3y/hide) - AES-256 bit encrypted password manager with all encrypted passwords stored locally on your machine
* [keydex](https://github.com/shikaan/keydex) - Manage KeePass databases from your terminal.
* [kpcli](http://kpcli.sourceforge.net/) - A command line interface for KeePass.
* [pa](https://github.com/biox/pa) - A simple password manager; encryption via age, written in portable posix shell.
* [pash](https://github.com/dylanaraps/pash) - A simple password manager using GPG written in POSIX sh.
* [pass](https://www.passwordstore.org/) - With pass, each password lives inside of a gpg encrypted file whose filename is the title of the website or resource that requires the password. These encrypted files may be organized into meaningful folder hierarchies, copied from computer to computer, and, in general, manipulated using standard command line file management utilities.
* [pass](https://github.com/acidvegas/pass) - POSIX password manager that keeps passwords inside gpg encrypted files inside a simple directory tree.
* [passage](https://github.com/FiloSottile/passage) - A fork of [password-store](https://www.passwordstore.org) that uses [age](https://age-encryption.org) as a backend instead of GnuPG.
* [passfzf](https://git.sr.ht/~mlaparie/passfzf) - A simple fzf wrapper for pass (the UNIX password-store). It allows fuzzy finding your pass passwords to copy, show, edit, delete, rename and duplicate them.
* [Pswd](https://github.com/Mandrew0822/pswd) - A secure password generator written in C.
* [rbw](https://github.com/doy/rbw) - Unofficial command line client for Bitwarden that is “stateful”, i.e., it does not require required the manual lock and unlock of the client.
* [safe.sh](https://github.com/windowsrefund/safe) - Pure Bash script to manage secure archives; simple and clean; uses [gnugpg](https://gnupg.org/) for encryption/decryption, thus can leverage tools like [GPG Agent](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html).
* [SpicyPass](https://github.com/JFreegman/SpicyPass) - A light-weight password manager with a focus on simplicity and security.
* [titan](https://www.byteptr.com/titan/) - Password management belongs to the command line, deep into the Unix heartland, the shell. Titan is written in C and is available under the MIT license.

## <a name="monitor-top"></a>Process viewers and monitoring (alternatives to top)

Programs to list and monitor currently running processes; alternatives to the `top` command.

* [atop](https://www.atoptool.nl/index.php) - Atop is TUI performance monitor for Linux; it reports the activity of all processes (even if processes have finished during the interval), daily logging of system and process activity for long-term analysis, overloaded system resources, etc.
* [bashtop](https://github.com/aristocratos/bashtop) - Resource monitor that shows usage and stats for processor, memory, disks, network and processes.
* [below](https://github.com/facebookincubator/below) - A time traveling resource monitor for modern Linux systems
* [bpytop](https://github.com/aristocratos/bpytop) - Linux/OSX/FreeBSD resource monitor with a nice interface.
* [Btop++](https://github.com/aristocratos/btop) - Resource monitor that shows usage and stats for processor, memory, disks, network and processes. C++ version and continuation of [bashtop](https://github.com/aristocratos/bashtop) and [bpytop](https://github.com/aristocratos/bpytop).
* [gtop](https://github.com/aksakalli/gtop) - System monitoring dashboard for terminal written in Node.js.
* [htop](http://hisham.hm/htop/) - An interactive process viewer for Unix; improves the UI of `top`, by adding real-time meters and colors.
* [iotop](http://guichaz.free.fr/iotop/) - "A Python program with a top like UI used to show of behalf of which process is the I/O going on".
* [nmon](https://nmon.sourceforge.io/pmwiki.php) - Nigel's performance Monitor for Linux.
* [nvitop](https://github.com/XuehaiPan/nvitop) - An interactive NVIDIA-GPU process viewer and beyond, the one-stop solution for GPU process management.
* [PCtrl](https://github.com/MohamedSherifNoureldin/PCtrl) - Robust, featureful, easy-to-use and powerful process manager.
* [procs](https://github.com/dalance/procs) - A modern replacement for ps written in Rust.
* [s-tui](https://github.com/amanusk/s-tui) - Stress-Terminal UI, s-tui, monitors CPU temperature, frequency, power and utilization in a graphical way from the terminal.
* [tiptop](https://github.com/nschloe/tiptop) - A command-line system monitoring tool in the spirit of top, written in Python. It displays various interesting system stats and graphs them. Works on all operating systems.
* [top](https://gitlab.com/procps-ng/procps) - The classical Unix utility that provides a rolling display of top cpu using processes.  
* [ttop](https://github.com/inv2004/ttop) - top-like system monitoring tool with TUI, historical data service and triggers.
* [TTV](https://github.com/caio-ishikawa/term-task-viewer) - terminal-task-viewer: a lightweight terminal tool to manage processes in Unix machines.
* [vtop](https://github.com/MrRio/vtop) - Alternative to top with several additional stats.
* [ytop](https://github.com/cjbassi/ytop) - TUI system monitor written in Rust.

## <a name="productivity"></a>Productivity

Applications for improving own productivity that do not deserve (at the moment) a specific category; e.g., resume generators and mind maps.

* [ancv](https://github.com/alexpovel/ancv) - Renders your (JSON) resume/CV for online & pretty terminal display.
* [classis](https://github.com/ginschel/classis) - An easy CLI for the terminal fans out there who want to access Open Assistant's API through the terminal or want to use the API in their own aplications.
* [gdir](https://github.com/pafoster/gdir) - A command line tool which queries Google Directions. The tool displays results as human-readable text.
* [h-m-m](https://github.com/nadrad/h-m-m) - h-m-m (pronounced like the interjection "hmm") is a simple, fast, keyboard-centric terminal-based tool for working with mind maps.
* [speedread](https://github.com/pasky/speedread) - A simple terminal-based open source Spritz-alike filter that shows input text as a per-word RSVP (rapid serial visual presentation) aligned on optimal reading points.
* [TUI apps](https://github.com/learnbyexample/TUI-apps) - A repository containing a couple of one-script programs, mainly dedicated to training/learning CLI tools such as grep, awk, etc.
* [tuxi](https://github.com/Bugswriter/tuxi) - A CLI tool that scrapes Google search results and SERPs that provides instant and concise answers.
* [wtf](https://github.com/wtfutil/wtf) - The personal information dashboard for your terminal, including todos, calendar, JIRA, etc.
* [zeitkatze](https://github.com/leonmavr/zeitkatze) - Simplest stopwatch in a linux console.

## <a name="programming-boilerplate"></a>Program templates and boilerplate

Utilities that generate licenses, documentation structure (README files), project directories and other boilerplate for software projects.

* [add-gitignore](https://github.com/TejasQ/add-gitignore) - Interactively generate a .gitignore for software projects.
* [boilr](https://github.com/tmrts/boilr) - Boilerplate template manager that generates files or directories from template repositories.
* [clog](https://github.com/clog-tool/clog-cli) - Creates a changelog automatically from local git metadata.
* [Cookiecutter](https://github.com/cookiecutter/cookiecutter) - A cross-platform command-line utility that creates projects from cookiecutters (project templates), e.g. Python package projects, C projects.
* [kickstart](https://github.com/Keats/kickstart) - Scaffolding tool to get new projects up and running quickly.
* [legit](https://github.com/captainsafia/legit) - Automagically generates a LICENSE file for the current working directory that you are in or a license header for a file where applicable.
* [license-up](https://github.com/nikitavoloboev/license-up) - Create a license quickly for a given name.
* [mklicense](https://github.com/cezaraugusto/mklicense) - CLI tool for easily generating the text of the most common licenses.
* [Proji](https://github.com/nikoksr/proji) - Powerful cross-platform CLI project templating tool.
* [readme-md-generator](https://github.com/kefranabg/readme-md-generator) - CLI that generates beautiful README.md files.
* [upnup](https://github.com/tomit4/upnup) - A command line utility that generates a LICENSE file in the current working directory.

## <a name="programming"></a>Programming

Tools for developers, including debuggers, testing, line counters, boilerplate and license generators, etc..

* [argbash](https://github.com/matejak/argbash) - Bash argument parsing code generator.
* [cgasm](https://github.com/bnagy/cgasm) - Pronounced “SeekAzzem”, it is a standalone, offline terminal-based tool with no dependencies that gives me x86 assembly documentation.
* [chars](https://github.com/antifuchs/chars) - Display names and codes for various ASCII (and unicode) characters / code points.
* [cloc](https://github.com/AlDanial/cloc) - Tool for counting blank lines, comment lines, and physical lines of source code in many programming languages.
* [CodeMark CLI](https://github.com/rootCircle/codemark-cli) - Helps you manage coding assignments and tests; easily initialize the configuration, list assignments, fetch and check your code, submit your code for grading, and get AI-powered error recommendations.
* [Cppcheck](http://cppcheck.net/) - Static analysis tool for C/C++ code providing unique code analysis to detect bugs and focuses on detecting undefined behaviour and dangerous coding constructs.
* [DEM](https://www.axemsolutions.io/dem_doc/index.html) - Containerized Development Environment Manager for embedded development.
* [dtool](https://github.com/guoxbin/dtool) - Collection of development tools.
* [fastmod](https://github.com/facebookincubator/fastmod) - A tool to assist you with large-scale codebase refactors, and it supports most of codemod's options. It is focused on improving the use case "I want to use interactive mode to make sure my regex is correct, and then I want to apply the regex everywhere".
* [fmake](https://github.com/bharatvaj/fmake) - Brings `make`s interface to almost any build system.
* [Frama-C](https://frama-c.com/) - Open-source extensible and collaborative platform dedicated to source-code analysis of C software. Frama-C can assist from the navigation through unfamiliar projects up to the certification of critical software.
* [gdb-dashboard](https://github.com/cyrus-and/gdb-dashboard) - Modular visual interface for GDB in Python.
* [grex](https://github.com/pemistahl/grex) - A command-line tool for generating regular expressions from user-provided test cases.
* [gup](https://github.com/nao1215/gup) - Update binaries installed by "go install" with goroutines.
* [hors](https://github.com/WindSoilder/hors) - Instant coding answers via the command line.
* [howdoi](https://github.com/gleitz/howdoi) - Instant coding answers via the command line.
* [Kool](https://github.com/kool-dev/kool) - CLI tool that brings the complexities of modern software development making these environments lightweight, fast and reproducible.
* [Leetcode-go](https://github.com/Manan-Prakash-Singh/leetcode-go) - A simple CLI tool for searching, downloading and submitting problems to leetcode.
* [mk](https://github.com/pycontribs/mk) - mk is a CLI tool that aims to ease contribution to any open-source project by hiding repository implementation details from the casual contributor.
* [nbterm](https://github.com/davidbrochart/nbterm) - Jupyter Notebooks in the terminal.
* [np](https://github.com/sindresorhus/np) - A better `npm publish`.
* [pire](https://github.com/johannestaas/pire) - Python Interactive Regular Expressions.
* [pvcheck](https://github.com/claudio-unipv/pvcheck) - A tool to apply automated testing to programs that produce textual output. The format of the output is very specific, making pvcheck suitable to test programming quizzes.
* [rebound](https://github.com/shobrook/rebound) - Fetch Stack Overflow results in your terminal when you get an error. Supported languages: Python, Node.js, Ruby, Golang, and Java.
* [release-it](https://github.com/release-it/release-it) - Automate releases for Git repositories and/or Node.js packages.
* [rr](https://rr-project.org/) - Debug the recording, deterministically, as many times as you want.
* [scc](https://github.com/boyter/scc) - Sloc Cloc and Code (scc) is a codebase statistics counter. Goal is to be the fastest code counter possible, but also perform COCOMO calculation like sloccount and to estimate code complexity similar to cyclomatic complexity calculators. In short one tool to rule them all.
* [scons](https://github.com/SCons/scons) - Software construction tool.
* [semantic-release](https://github.com/semantic-release/semantic-release) - Automates the whole node.js package release workflow including: determining the next version number, generating the release notes, and publishing the package.
* [stepci](https://github.com/stepci/stepci) - Automated API Testing and Quality Assurance.
* [temci](https://github.com/parttimenerd/temci) - Advanced benchmarking tool written in Python 3 that supports setting up an environment for benchmarking and the generation of visually appealing reports.
* [todocheck](https://github.com/preslavmihaylov/todocheck) - Static code analyzer for annotated TODO comments.
* [Tokei](https://github.com/XAMPPRocky/tokei) - Tokei is a program that displays statistics about your code. Tokei will show the number of files, total lines within those files and code, comments, and blanks grouped by language.
* [umake](https://github.com/mcandre/unmake) - Makefile linter emphasizing portability, targeting the POSIX make standard.

## <a name="prompt"></a>Prompts

Prompts and welcome messages at the command line.

* [Basta!](https://www.kylheku.com/cgit/basta/about/) - A small amount of GNU Bash code that maintains a scroll-protected status line at the bottom of the terminal.
* [powerline](https://github.com/powerline/powerline) - Powerline is a statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile.
* [Starship](https://starship.rs/) - The cross-shell prompt for astronauts.
* [welcome.sh](https://github.com/G2-Games/welcome.sh) - A nice little script that greets you on every launch, with some helpful (and customizable!) information.

## <a name="rss"></a>RSS

RSS feed visualizers, converters and managers.

* [Canto Curses](https://github.com/themoken/canto-curses) - Curses frontend for [Canto daemon](https://github.com/themoken/canto-next) for RSS feeds.
* [Newsbeuter](http://newsbeuter.org/) - "The Mutt of RSS Feed Readers": Newsbeuter is an open-source RSS/Atom feed reader for text terminals. Has great configurability and vast number of features, making it a slick and fast feed reader that can be completely controlled via keyboard.
* [Newsboat](https://newsboat.org/) - An RSS/Atom feed reader for the text console. It's an actively maintained fork of Newsbeuter.
* [Newsraft](https://codeberg.org/newsraft/newsraft) - Newsraft is a feed reader with ncurses user interface. It is greatly inspired by Newsboat and tries to be its lightweight counterpart.
* [nom](https://github.com/guyfedwards/nom) - RSS reader for the terminal.
* [openring](https://git.sr.ht/~sircmpwn/openring) - A tool for generating a webring from RSS feeds, so you can link to other blogs you like on your own blog.
* [rReader](https://github.com/rainygirl/rreader) - RSS reader client with TUI interface.
* [rss-cli](https://github.com/Clortox/rss-cli) - A unix-inspired cli application for interacting with RSS feeds.
* [Sfeed](https://codemadness.org/sfeed.html) - Sfeed is a RSS and Atom parser (and some format programs). It converts RSS or Atom feeds from XML to a TAB-separated file.

## <a name="religion"></a>Religion

Tools to handle religious material, e.g. reading the Holy Bible.

* [bbl](https://github.com/nehemiaharchives/bbl) - Read, search Holy Bible in command line.
* [bible](https://github.com/BibleJS/BibleApp) - Read the Holy Bible via the command line.
* [ltorah](https://github.com/Mandrew0822/ltorah) - ltorah provides a way to read the ancient hebrew Torah from the command line.
* [The Rock](https://gitlab.com/NoahJelen/the-rock) - Command line King James bible viewer for Linux systems modeled after Debian's bible-kjv, but with extra features.

## <a name="science"></a>Science

Packages for scientific research and science applications, e.g., bibliography and publication management.

* [bib.awk](https://github.com/huijunchen9260/bib.awk) - Bibliography manager written in awk.
* [BibMan](https://ductri.github.io/note/2023/09/27/bibman.html) - A TUI bibliography manager. It aims to support only the most basis features as a general bibliography manager.
* [bibtools](https://github.com/pkgw/bibtools) - Command-line bibliography manager.
* [cobib](https://gitlab.com/mrossinek/cobib) - Simple, command-line based bibliography management tool.
* [conrad](https://github.com/vinayak-mehta/conrad) - Track conferences and meetups.
* [element](https://github.com/gennaro-tedesco/element) - Periodic table on the command line.
* [FAWOC](https://github.com/robolab-pavia/fawoc) - FAWOC is a TUI program for manually labelling a list of words. It has been developed to support the efficient clustering of documents based on topic modeling algorithms such as Dirichlet Latent Allocation.
* [GCTU](https://github.com/Mandrew0822/GCTU---Genetic-code-translation-utility) - A simple command line tool which allows one to convert DNA code sequences to the different RNA sequences.
* [Go-L](https://github.com/Jeadie/Go-L) - Game of Life with different update rules and on a bunch of different topologies (sphere, torus, klein bottle, etc.).
* [papis](https://github.com/alejandrogallo/papis) - Extensible document and bibliography manager.
* [periodic-table-cli](https://github.com/spirometaxas/periodic-table-cli) - An interactive Periodic Table of Elements app for the console!
* [pt.sh](https://github.com/alexeytal/pt.sh) - CLI periodic table with search and many properties.
* [ptable](https://github.com/velorek1/ptable) - A beautiful TUI periodic table for GNU/linux terminals.
* [Pubs](https://github.com/pubs/pubs) - Pubs organizes your scientific papers together with their bibliographic data and provides command line access to basic and advanced manipulation of your library.
* [scholarref](https://adamsgaard.dk/scholarref.html) - Tools to never deal with journal webpages again.
* [slr-kit](https://github.com/robolab-pavia/slr-kit) - Set of CLI tools to assist the writing of Systematic Literature Reviews powered by Natural Language Processing.
* [starfetch](https://github.com/Haruno19/starfetch) - Command line tool that displays constellations.

## <a name="screen-recorder"></a>Screen recorder

Tools to record the content of the terminal and manage the recording (e.g., converting into animated GIFs).

* [agg](https://github.com/asciinema/agg) - agg is a command-line tool for generating animated GIF files from asciicast v2 files produced by `asciinema` terminal recorder.
* [asciinema](https://github.com/asciinema/asciinema) - Terminal session recorder.
* [goscript](https://github.com/elisescu/goscript) - Goscript is a tool that records the terminal session (well, any command you run it with) and saves the output in a self contained html file that can be run in the browser, to playback the session.
* [t-rec](https://github.com/sassman/t-rec-rs) - Blazingly fast terminal recorder that generates animated gif images for the web written in rust.
* [terminal-recorder](https://github.com/cortezcristian/terminal-recorder) - Terminal recorder allows you to record your bash session, and export it to html so then you can share it with your friends.
* [terminalizer](https://github.com/faressoft/terminalizer) - Record your terminal and generate animated gif images or share a web player link [www.terminalizer.com](www.terminalizer.com).
* [termtosvg](https://github.com/nbedos/termtosvg) - A Unix terminal recorder written in Python that renders your command line sessions as standalone SVG animations.
* [ttygif](https://github.com/icholy/ttygif) - ttygif converts a ttyrec file into gif files. It's a stripped down version of ttyplay that screenshots every frame.
* [ttystudio](https://github.com/chjj/ttystudio) - Record your terminal and compile it to a GIF or APNG without any external dependencies, bash scripts, gif concatenation, etc.
* [vhs](https://github.com/charmbracelet/vhs) - Write terminal GIFs as code for integration testing and demoing your CLI tools.

## <a name="screensaver"></a>Screen savers

Screen savers with animations for the idle times of the computer.

* [ASCII Saver](https://gitlab.com/mezantrop/ascsaver) - Screensaver for terminals.
* [pipes.sh](https://github.com/pipeseroni/pipes.sh) - Animated pipes terminal screensaver.
* [sclocka](https://github.com/mezantrop/sclocka) - The real screensaver/lock for terminals.
* [termsaver](http://termsaver.brunobraga.net/) - termsaver to enjoy fancy ASCII screensavers like matrix, clock, starwars, and a couple of not-safe-for-work screens.

## <a name="security"></a>Security and encryption

Cryptography, ciphered archive managers, encrypted file-systems.

* [acmetool](https://github.com/hlandau/acmetool) - Easy-to-use command line tool for automatically acquiring certificates from ACME servers (such as Let's Encrypt).
* [cipher](https://github.com/ash-shell/cipher) - An Ash module that makes it easy to perform aes-256-cbc encryption for files and directories.  
* [cotp](https://github.com/replydev/cotp) - Trustworthy, encrypted, command-line TOTP/HOTP authenticator app with import functionality.
* [cream](https://z3bra.org/cream/) - Encrypt and decrypt streams of data with only a master password. The key is derivated from the password + salt combo, and used to encrypt data byte per byte.
* [enc](https://github.com/life4/enc) - A modern and friendly CLI alternative to GnuPG: generate and download keys, encrypt, decrypt, and sign text and files, and more.
* [encfs](http://www.arg0.net/#!encfs/c1awt) - Encrypted filesystem in user-space based on [FUSE](https://it.wikipedia.org/wiki/FUSE), mounts an encrypted directory into a clear one.
* [feroxbuster](https://github.com/epi052/feroxbuster) - A fast, simple, recursive content discovery tool written in Rust.
* [Firejail](https://firejail.wordpress.com/) - A SUID program that reduces the risk of security breaches by restricting the running environment of untrusted applications using Linux namespaces and seccomp-bpf.
* [GnuPG](https://gnupg.org/) - GnuPG is a complete and free implementation of the OpenPGP standard as defined by RFC4880 (also known as PGP).
* [gocryptfs](https://nuetzlich.net/gocryptfs) - An encrypted overlay filesystem written in Go.
* [hashcat](https://hashcat.net/hashcat/) - A robust and efficient password cracking tool that can help you recover lost passwords, audit password security, benchmark, or just figure out what data is stored in a hash.
* [Image Steganography Tool](https://github.com/7thSamurai/steganography) - Simple C++ Encryption and Steganography tool that uses Password-Protected-Encryption to secure a file's contents.
* [jdvrif](https://github.com/CleasbyCode/jdvrif) - CLI tool to embed or extract files via a JPG image. Post & share your embedded JPG image on compatible sites.
* [LUKS](https://guardianproject.info/code/luks/) - Hard disk encryption tool; it stores all setup information in the partition header, enabling easy data transport or migration.
* [Minisign](https://github.com/jedisct1/minisign) - A dead simple tool to sign files and verify digital signatures.
* [OAuth2c](https://github.com/cloudentity/oauth2c) - A command-line tool for interacting with OAuth 2.0 authorization servers.
* [ots](https://github.com/sniptt-official/ots) - Share end-to-end encrypted secrets with others via a one-time URL.
* [PaperAge](https://github.com/matiaskorhonen/paper-age) - Easy and secure paper backups of secrets, which takes a text and generates an encrypted QRcode to print on paper.
* [pgen](https://github.com/ctsrc/Pgen) - Generate passphrases using the wordlists for random passphrases made by the EFF.
* [safe](https://z3bra.org/safe/) - Password protected secret keeper. Secrets are encrypted and stored on disk using a key derivated from your master password - no keys to manage.
* [securo](https://github.com/iunary/securo) - Encrypt and descrypt files and folders using a symmetric encryption.
* [SOPS](https://github.com/getsops/sops) - SOPS (Secrets OPerationS) is a simple and flexible tool for managing secrets, sops is an editor of encrypted files that supports YAML, JSON, ENV, INI and BINARY formats, encrypting the values but not the keys.
* [StegCloak](https://github.com/kurolabs/stegcloak) - Hide secrets with invisible characters in plain text securely using passwords
* [uacme](https://github.com/ndilieto/uacme) - ACMEv2 client written in plain C with minimal dependencies.
* [van-gonography](https://github.com/JoshuaKasa/van-gonography) - Hide your files of any type inside a image of your choice using steganography.
* [wifi-password](https://github.com/rauchg/wifi-password) - Get wifi pass.

## <a name="shells"></a>Shells

Shell programs that enable the interaction through the terminal.

* [Bash](https://www.gnu.org/software/bash/) - (Bourne Again SHell) The most widespread system shell to date.  
* [Cat9](https://github.com/letoram/cat9) - Cat9 is a user shell script for LASH - a command-line shell that discriminates against terminal emulators, written in Lua.
* [cosh](https://github.com/tomhrr/cosh) - Concatenative command-line shell.
* [DASH](http://gondor.apana.org.au/~herbert/dash/) - DASH is a POSIX-compliant implementation of /bin/sh that aims to be as small as possible. It does this without sacrificing speed where possible.
* [Elvish](https://github.com/elves/elvish) - Elvish is a versatile interactive shell and expressive programming language, combined into one seamless package.
* [Fish](https://fishshell.com/) - "A command line shell for the 90s"; focused on user-friendliness, with powerful autosuggestions, colors, "sane scripting" (w.r.t. to Bash).
* [Ion](https://github.com/redox-os/ion) - Ion is a modern system shell that features a simple, yet powerful, syntax.
* [N-Commodore](https://github.com/psprint/n-commodore) - A novel file manager/shell/command-line, where everything is panelized, greppable and remembered.
* [Nushell](https://github.com/nushell/nushell) - A modern shell written in Rust, where all data is structured.
* [Reptyl](https://github.com/0ut0flin3/Reptyl) - A cross-platform command line shell that supports execution of commands in natural language.
* [Spaceship](https://spaceship-prompt.sh/) - Minimalistic, powerful and extremely customizable Zsh prompt.
* [Twin](https://github.com/cosmos72/twin) - Text mode window environment. A "retro" program for embedded or remote systems, that doubles as X11 terminal and text-mode equivalent of VNC server.
* [xonsh](https://xon.sh/) - The xonsh shell lets you easily mix Python and shell commands in a powerful and simplified approach to the command line.
* [Zsh](http://www.zsh.org/) - Alternative shell designed for interactive use.  

## <a name="music"></a>Sound and music

Music players, podcast, synthesizers, downloaders, online radios.

* [Alsamixer](http://www.alsa-project.org/main/index.php/Main_Page) - ALSA mixer with curses interfaces.  
* [BadaBoomBooks](https://github.com/WirlyWirly/BadaBoomBooks) - Quickly organize audiobooks using a terminal and web-browser.
* [beets](https://github.com/beetbox/beets) - Beets is the media library management system for obsessive music geeks: catalogs your collection, automatically improving its metadata as it goes.
* [castero](https://github.com/xgi/castero) - A TUI podcast client for the terminal.
* [cmus](https://cmus.github.io/) - A fast and lightweight audio player with configurable keybindings and playlist support.  
* [cTune](https://github.com/An7ar35/ctune) - A ncurses based internet radio player written in C for Linux.
* [cue](https://github.com/ravachol/cue) - A command-line music player.
* [dzr](https://github.com/yne/dzr) - Command Line deezer.com Player for Linux, BSD, Android, Windows.
* [espeak](http://espeak.sourceforge.net/) - A compact open source software speech synthesizer for English and other languages.
* [fme](https://github.com/andreykaere/fme) - Flexible metadata editor that allows to edit the metadata of music files.
* [Gomu](https://github.com/issadarkthing/gomu) - Gomu is intuitive, powerful CLI music player. It has embedded scripting language and event hook to enable user to customize their config extensively.
* [Instant Music Downloader](https://github.com/yask123/Instant-Music-Downloader) - Instantly download any song!
* [kord](https://github.com/synestematic/kord) - A python framework that provides programmers with a simple api for the creation of music-based applications.
* [line](https://github.com/pd3v/line) - Tiny command-line midi sequencer and language for live coding.
* [maestro-cli](https://github.com/PrajwalVandana/maestro-cli) - A command-line tool to play songs (or any audio, really) in the terminal.
* [mfp](https://github.com/guptarohit/mfp) - A command-line utility for playing music mixes for programming & focus (from  [musicforprogramming.net](musicforprogramming.net)), unlocking the flow state.
* [MOC](https://moc.daper.net/) - (music on console) is a powerful and easy to use console audio player, user interface a la Midnight Commander, plenty of features, fully controllable from the keyboard.
* [Mp3blaster](http://www.mp3blaster.org/?m=1) - Audio player for the text console.
* [mpg123](http://mpg123.org/) - Quick `mp3` sound file player; no visual interface, just a command-line audio file player for `mp3` files.
* [mps-youtube](https://github.com/mps-youtube/yewtube) - A curses player for music tracks from Youtube; it allows to search for songs and playlists; it downloads the video, extracts the audio track and plays it; handles local playlists and many configuration parameters.
* [mpvc](https://github.com/gmt4/mpvc/) - A minimal mpc-like CLI and TUI for controlling mpv from the shell.
* [muCLIar](https://github.com/aayush1205/muCLIar) - YouTube automator bringing you your music right on your CLI.
* [MusicPlayerPlus](https://github.com/doctorfree/MusicPlayerPlus) - Featureful ncurses based MPD client inspired by ncmpc with integration for Beets, spectrum visualization,Bandcamp/Soundcloud, asciimatics, cantata, and more.
* [musicScraper](https://github.com/mBaratta96/musicScraper) - CLI tool for scraping information from musical websites (Rateyourmusic, Metal Archives), with nice album ASCII art.
* [musikcube](https://github.com/clangen/musikcube) - A cross-platform, terminal-based audio engine, library, player and server written in C++.
* [mzk](https://github.com/acidvegas/mzk) - Music theory helper.
* [ncmpcpp](https://rybczak.net/ncmpcpp/) - NCurses Music Player Client (Plus Plus) - featureful ncurses based MPD client inspired by ncmpc. Relevant features: tag editor, playlist editor, easy to use search engine, media library, music visualizer, ability to fetch artist info from [last.fm](https://www.last.fm/), new display mode, alternative user interface, ability to browse and add files from outside of MPD music directory.
* [ncspot](https://github.com/hrkfdn/ncspot) - Cross-platform ncurses Spotify client written in Rust, inspired by ncmpc and the likes.
* [ogg123](https://www.xiph.org/downloads/) - Quick `ogg` sound file player; no visual interface, just a command-line audio file player for the free and open `ogg` file format.
* [pulsemixer](https://github.com/GeorgeFilipkin/pulsemixer) - CLI and curses mixer for PulseAudio.
* [PyRadio](https://github.com/coderholic/pyradio) - Curses based internet radio player.
* [pytunes](https://github.com/bernhardfritz/pytunes) - Self-hosted music streaming service.
* [radio-active](https://github.com/deep5050/radio-active) - Internet radio player with 40k+ stations.
* [radio-beats](https://github.com/quangnguyen30192/radio-beats) - Rofi-like menu for playing radio stations.
* [Siren](https://www.kariliq.nl/siren/) - Siren is a text-based audio player for UNIX-like operating systems.
* [Spotify TUI](https://github.com/Rigellute/spotify-tui) - A Spotify client for the terminal written in Rust.
* [spotify-player](https://github.com/aome510/spotify-player) - spotify-player is a fast, easy to use, and configurable terminal music player having feature parity with the official Spotify application.
* [Tera](https://github.com/shinokada/tera) - Terminal Radio: an easy-to-use CLI music player to play favorite music, radio stations and explore various radio stations from the terminal only.
* [termusic](https://github.com/tramhao/termusic) - Terminal Music Player written in Rust.
* [Tizonia](https://github.com/tizonia/tizonia-openmax-il) - Command-line cloud music player for Linux with support for Spotify, Google Play Music, YouTube, SoundCloud, TuneIn, iHeartRadio, Plex servers and Chromecast devices.
* [yt-audio](https://github.com/RijulGulati/yt-audio) - A simple, configurable youtube-dl wrapper to download and manage youtube audio.
* [ytui-music](https://github.com/sudipghimire533/ytui-music) - Youtube client in terminal for music (lightweight Youtube client).

## <a name="monitor"></a>System monitoring

Applications to display the usage of system resources: network, memory, power, etc..

* [Batfetch](https://github.com/ashish-kus/batfetch) - A command-line tool that displays detailed information about the battery of your device in a clean and organized way.
* [dmidecode](https://www.nongnu.org/dmidecode/) - System information utility.
* [dysk](https://dystroy.org/dysk) - A thing to get information on your mounted disks
* [Fastfetch](https://github.com/LinusDierheimer/fastfetch) - Like neofetch, but much faster because written in C.
* [glances](https://nicolargo.github.io/glances/) - A comprehensive and detailed system monitoring tool; monitored parameters include: CPU, memory, load, process list, network interfaces, disk I/O, sensors, filesystems, docker, system info, uptime.
* [HyFetch](https://github.com/hykilpikonna/hyfetch) - A fork of the abandoned [Neofetch](https://github.com/dylanaraps/neofetch), HyFetch displays information about your system next to an image, your OS logo, or any ASCII file of your choice.
* [hyperfine](https://github.com/sharkdp/hyperfine) - A command-line benchmarking tool.
* [inxi](http://smxi.org/docs/inxi.htm) - A comprehensive system information script; provides information about CPU, graphics, audio and network devices, drives and partitions, sensors; implemented as a Bash script.
* [LNAV](https://github.com/tstack/lnav) - Log file navigator.
* [multitail](https://www.vanheusden.com/multitail/) - A command to open multiple log files in a single terminal window and monitor them in real-time.  
* [neofetch](https://github.com/dylanaraps/neofetch) - Neofetch is a CLI system information tool written in BASH. Neofetch displays information about your system next to an image, your OS logo, or any ASCII file of your choice. Currently abandoned.
* [ngrep](http://ngrep.sourceforge.net/) - (Network grep) applies the `grep` logic to the network layer, allowing to match regular expressions against data payloads of packets; it recognizes IPv4/6, TCP, UDP, ICMPv4/6, IGMP and Raw across Ethernet, PPP, SLIP, FDDI, Token Ring and null interfaces.
* [noti](https://github.com/variadico/noti) - Monitor a process and trigger a notification.
* [powertop](https://01.org/powertop) - A `top`-like utility to monitor the sources of power consumption, allows to turn on/off many components, quite useful to track possible power-related issues.
* [pv](http://www.ivarch.com/programs/pv.shtml) - The pv command is used to monitor the progress of data through pipe.
* [ramfetch](https://github.com/WhoseTheNerd/ramfetch) - A fetch which displays memory info using /proc/meminfo.
* [screenFetch](https://github.com/KittyKatt/screenFetch) - It can be used to generate one of those nifty terminal theme information + ASCII distribution logos. It auto-detects the distribution and display an ASCII version of that distribution's logo and some valuable information to the right.
* [smem](https://www.selenic.com/smem/) - Python program that reports memory usage; it can report the "proportional set size" (PSS), a meaningful representation of the amount of memory used by libraries and applications in a virtual memory system; it has built-in chart generation.
* [sysdig](https://www.sysdig.org/) - Sysdig captures system calls and events from the Linux kernel.  You can save, filter, and analyze the data with our CLI or our desktop app.  Think of sysdig as strace + tcpdump + htop + iftop + lsof + wireshark for your entire system.
* [The Logfile Navigator](https://lnav.org/) - An advanced and colorful log file viewer with TUI interface.
* [ttyload](http://www.daveltd.com/src/util/ttyload/) - ttyload is a lightweight utility which is intended to offer a color-coded graph of load averages over time on Linux and other Unix-like systems. It enables a graphical tracking of system load average in a terminal ("tty").
* [whowatch](https://www.tecmint.com/whowatch-monitor-linux-users-and-processes-in-real-time/) - Monitor Linux Users and Processes in Real Time.
* [zfxtop](https://github.com/ssleert/zfxtop) - Self described as “fetch top written by bubbletea enjoyer”.

## <a name="system"></a>System tools

System management tools, such as for brightness control, dotfile and environment variable management, notifications, etc..

* [active-win-cli](https://github.com/sindresorhus/active-win-cli) - Get the title/id/etc of the active window.
* [argc-completions](https://github.com/sigoden/argc-completions) - Autocompletion for any shell and any command.
* [brightnessctl](https://github.com/Hummer12007/brightnessctl) - Read and control device brightness. Devices, by default, include backlight and LEDs - searched for in corresponding classes.
* [checksum.sh](https://checksum.sh/) - Checksum.sh is a simple way to download, review, and verify install scripts. If the checksum is OK the script will be printed to stdout, which can be piped to sh or elsewhere.
* [conspy](http://conspy.sourceforge.net/) - "Conspy allows a (possibly remote) user to see what is displayed on a Linux virtual console, and send keystrokes to it." 
* [fkill-cli](https://github.com/sindresorhus/fkill-cli) - Simple cross-platform process killer.
* [has](https://github.com/kdabir/has) - Checks presence of various command line tools on the PATH and reports their installed version.
* [inshellisense](https://github.com/microsoft/inshellisense) - IDE style command line auto complete with support for 600+ command line tools.
* [just](https://github.com/casey/just) - Handy way to save and run project-specific commands.
* [Kill](https://github.com/unsigned-enby/Kill) - Small bash-only script for killing processes/sending signals.
* [killport](https://github.com/jkfran/killport) - A command-line tool to easily kill processes running on a specified port.
* [lshw](http://www.ezix.org/project/wiki/HardwareLiSter) - A small tool to provide detailed information on the hardware configuration of the machine. It can report exact memory configuration, firmware version, mainboard configuration, CPU version and speed, cache configuration, bus speed, etc.
* [mackup](https://github.com/lra/mackup) - Keep your application settings in sync (OS X/Linux).
* [Ntfy](https://github.com/dschep/ntfy) - Cross-platform Python utility that enables you to automatically get desktop notifications on demand or when long running commands complete. It can as well send push notifications to your phone once a particular command completes.
* [rfsh](https://github.com/docsion/rfsh) - Run shell scripts in batch, concurrently, fully customized with variable.
* [rs-env](https://github.com/sysid/rs-env) - Hierarchical environment variable management, compiling the resulting set of from a hierarchical list of `<name>.env` files.
* [Rumos](https://github.com/octagony/rumos) - CLI utility for controlling screen brightness.
* [sysm](https://github.com/jafarlihi/sysm) - Makes your system play custom sounds when any configured system or external event happens.
* [systeroid](https://github.com/orhun/systeroid) - A more powerful alternative to sysctl(8) with a terminal user interface.
* [viewport-list-cli](https://github.com/kevva/viewport-list-cli) - Return a list of devices and their viewports.
* [YAS-BDSM](https://github.com/sebastiancarlos/yas-bdsm) - YAS-BDSM (Yet Another Stow-Based Dotfiles System Manager):  a minimal, UNIX-based, cross-platform, hierarchical dotfiles manager.
* [ydf](https://github.com/yunielrc/ydf) - A disruptive dotfiles manager+. Be ready to work in just a few minutes on your Fresh OS.

## <a name="terminal"></a>Terminals

Terminal and terminal multiplexers.

* [byobu](http://byobu.co/) - A text-based window manager and terminal multiplexer; it features enhanced profiles, convenient keybindings, configuration utilities, and toggle-able system status notifications; compatible with `screen` and `tmux`.
* [dtach](https://github.com/crigler/dtach) - A program written in C that emulates the detach feature of screen.
* [mtm](https://github.com/deadpixi/mtm) - Micro Terminal Multiplexer - Simple but usable, stable and minimalistic terminal multiplexer.
* [mx](https://gitlab.com/lpireyn/mx) - A tmux session manager written as a single Bash script.
* [peaches](https://github.com/KCaverly/peaches) - A smart switcher for the terminal. Based on tmux.
* [screen](https://www.gnu.org/software/screen/) - Terminal multiplexer that split a physical terminal between several processes, typically interactive shells.
* [Tmate](https://tmate.io/) - A fork of tmux that allows to share the terminal with other users. AFAIK, it connects to a centralized server to establish the connection. Someone may see this inconvenient for privacy issues.
* [tmux](https://tmux.github.io/) - Terminal multiplexer; born to improve `screen`; client-server architecture, `vi` and `emacs` key-bindings, search in window feature and many more.
* [tmux-session](https://github.com/BartSte/tmux-session) - Manage tmux sessions using fzf.
* [vtm](https://github.com/netxs-group/vtm) - Virtual terminal multiplexer with window manager and session sharing.
* [warp](https://github.com/spolu/warp) - Secure and simple terminal sharing.  
* [wezterm](https://github.com/wez/wezterm) - A GPU-accelerated cross-platform terminal emulator and multiplexer implemented in Rust with tons of features.
* [Zellij](https://github.com/zellij-org/zellij) - A workspace aimed at developers, ops-oriented people and anyone who loves the terminal. At its core, it is a terminal multiplexer.

## <a name="text-processing"></a>Text processing

Text processing utilities to cut or sort lines, find dead links, colorize command output, etc..

* [anew](https://github.com/tomnomnom/anew) - Tool for adding new lines to files, skipping duplicates.
* [as-tree](https://github.com/jez/as-tree) - Print a list of paths as a tree of paths.
* [awk](https://github.com/onetrueawk/awk) - A historical, general-purpose text file processor, implements a domain-specific language designed for text processing and typically used as a data extraction and reporting tool.
* [brok](https://github.com/smallhadroncollider/brok) - Find broken links in text documents.
* [deadlink](https://github.com/nschloe/deadlink) - Parses text files for HTTP URLs and checks if they are still valid. Good to use on markdown documentation files.
* [detect-indent-cli](https://github.com/sindresorhus/detect-indent-cli) - Detect the indentation of code.
* [espanso](https://github.com/espanso/espanso) - Cross-platform Text Expander written in Rust. Not limited to the command line.
* [fullname-cli](https://github.com/sindresorhus/fullname-cli) - Get the fullname of the current user.
* [grc](https://github.com/pengwynn/grc) - (Generic Colouriser) can be configured to parse a given text stream and to colorize it according to regexp written in configuration files, different patterns can be associated to file types.
* [gtree](https://github.com/ddddddO/gtree) - Using either Markdown or programmatically to generate directory trees and directories, and to verify directories.
* [gzip-size-cli](https://github.com/sindresorhus/gzip-size-cli) - Get the gzipped size of a file.
* [HASHA CLI](https://github.com/sindresorhus/hasha-cli) - Hashing made simple. Get the hash of text or stdin.
* [hck](https://github.com/sstadick/hck) - A sharp cut clone.
* [huniq](https://github.com/koraa/huniq) - Command line utility to remove duplicates from the given input. Note that huniq does not sort the input, it just removes duplicates.
* [JsonGenius](https://github.com/semanser/JsonGenius) - Self-hosted scraping API that extracts structured data described by a JSON Schema.
* [kill-tabs](https://github.com/sindresorhus/kill-tabs) - Kill all Chrome tabs to improve performance, decrease battery usage, and save memory.
* [Line Select](https://github.com/urbanogilson/lineselect) - A powerful utility enabling interactive line selection from stdin, allowing to seamlessly integrate, pause, select, and refine your pipeline, enhancing data processing precision.
* [lolcat](https://github.com/busyloop/lolcat) - Ruby Gem to colorize the output of the cat command.
* [Normalize Country](https://github.com/sshaw/normalize_country) - Convert country names and codes to a standard.
* [Output as Format ](https://github.com/sshaw/output-as-format) - Output stdin as GitHub/Slack/Jira etc... formatted code, lists, or quotes.
* [pup](https://github.com/ericchiang/pup) - Parsing HTML at the command line.
* [rare](https://github.com/zix99/rare) - Realtime regex-extraction and aggregation into common formats such as histograms, bar graphs, numerical summaries, tables, and more!
* [rich](https://github.com/Textualize/rich-cli) - Rich-CLI is a command line toolbox for fancy output in the terminal, built with [Rich](https://github.com/Textualize/rich).
* [skroll](https://z3bra.org/skroll/) - A small utility that you can use to make a text scroll. Pipe text to it, and it will scroll a given number of letters from right to left.
* [squeeze](https://github.com/aymericbeaumet/squeeze) - Enables to extract rich information from any text (raw, JSON, HTML, YAML, etc).
* [swordfish-rs](https://github.com/vim-zz/swordfish-rs) - Mimics real person behavior with realtime typing into terminal uses a screenplay where text and timings are specified.
* [to-double-quotes](https://github.com/sindresorhus/to-double-quotes-cli) - Convert matching single-quotes to double-quotes.
* [to-single-quotes](https://github.com/sindresorhus/to-single-quotes-cli) - Convert matching double-quotes to single-quotes.
* [trurl](https://github.com/curl/trurl) - Command line tool for URL parsing and manipulation.
* [tuc](https://github.com/riquito/tuc) - You want to cut on more than just a character, perhaps using negative indexes or format the selected fields as you want... Maybe you want to cut on lines (ever needed to drop first and last line?)... That's where tuc can help.
* [Ultimate Plumber](https://github.com/akavel/up) - Helps to interactively and incrementally explore textual data in Linux, by making it easier to quickly build complex pipelines, thanks to a fast feedback loop.

## <a name="text-search"></a>Text search (alternatives to grep)

Search files and exploring directory trees to look for text or patterns (RegEx) contained in files; alternatives to the `grep` command.

* [ack](http://beyondgrep.com/) - A tool like `grep` optimized for programmers; written in Perl, it speeds up searches thanks to skipping non interesting directories, such as `.git`.
* [ag](https://github.com/ggreer/the_silver_searcher) - (The silver searcher) is a text search utility targeted to source code; it skips versioning systems data directories; it is inspired by `ack`, but faster.
* [ast-grep](https://github.com/ast-grep/ast-grep) - A CLI tool for code structrual search, lint and rewriting.
* [hypergrep](https://github.com/p-ranav/hypergrep) - Recursively search directories for a regex pattern using Intel Hypescan.
* [paragrep](http://software.clapper.org/paragrep/) - Greps regular expressions in a text file(s) and prints out the paragraphs containing those expressions, a paragraph is defined as a block of text delimited by an empty or blank line, fully customizable via command line parameters.
* [ripgrep](https://github.com/BurntSushi/ripgrep) - Recursively searches directories for a regex pattern.
* [ripgrep-all](https://github.com/phiresky/ripgrep-all) - grep in text files but also search in PDFs, E-Books, office documents, zip, tar.gz, etc.
* [sift](https://sift-tool.org/) - Fast and powerful open source alternative to grep; it targets flexibility and performance: can be as fast as "regular" grep and allows to specify complex expressions to find text.
* [ugrep](https://github.com/Genivia/ugrep) - Ultra fast grep with interactive TUI, fuzzy search, boolean queries, hexdumps and more.
* [vgrep](https://github.com/vrothberg/vgrep) - User-friendly pager for grep.

## <a name="text-search-replace"></a>Text search and replace (alternatives to sed)

Tools to search text within files and perform operations on it, such as text replacement; alternatives to `sed`.

* [amber](https://github.com/dalance/amber) - Code search / replace tool.
* [repgrep](https://github.com/acheronfail/repgrep) - A replacer that uses ripgrep for finding and provides an interactive interface to replace the text.
* [sd](https://github.com/chmln/sd) - s[earch] & d[isplace] - An intuitive find & replace CLI a possible replacement for sed.
* [teip](https://github.com/greymd/teip) - Select partial standard input and replace with the result of another command.

## <a name="time-tracker"></a>Time trackers

Time and habit trackers to measure the amount of time spent on different activities.

* [arbtt](http://arbtt.nomeata.de/) - (automatic, rule-based time tracker) runs in background, collecting information regarding open windows, focussed ones, etc.; it can be configured to display statistics on the collected data, e.g., figuring out the time spent on one specific window.
* [Bartib](https://github.com/nikolassv/bartib) - Easy to use time tracking tool for the command line. It saves a log of all tracked activities as a plaintext file and allows you to create flexible reports.
* [dijo](https://github.com/NerdyPepper/dijo) - Scriptable, curses-based, digital habit tracker.
* [doing](https://github.com/ttscoff/doing) - A command line tool for remembering what you were doing and tracking what you've done.
* [habitctl](https://github.com/blinry/habitctl) - Minimalist command line tool you can use to track and examine your habits.
* [habitmap](https://github.com/shuu-wasseo/habitmap) - A command-line app to track your habits and visualise how committed you are to making or maintaining them with colorful heatmaps.
* [Moro](https://github.com/getmoro/moro) - A command line tool for tracking work hours, as simple as it can get.
* [MyTimer](https://github.com/sepandhaghighi/mytimer) - Simple timer for the terminal with timer-mode and alarm.
* [Productivity Timer](https://github.com/h-sifat/productivity-timer) - A CLI/TUI Pomodoro timer and todo (coming soon) application for keyboard addicts and terminal fans that makes you more productive.
* [Timer-CLI](https://github.com/1Blademaster/timer-cli) - A very simple countdown timer.
* [Timetrap](https://github.com/samg/timetrap) - A simple command line time tracker written in Ruby. It provides an easy to use command line interface for tracking what you spend your time on.
* [Timewarrior](https://github.com/GothenburgBitFactory/timewarrior) - A time tracking utility that offers simple stopwatch features as well as sophisticated calendar-based backfill, along with flexible reporting.
* [tmux-pomodoro-plus](https://github.com/olimorris/tmux-pomodoro-plus) - Pomodoro technique into your tmux workflow
* [utt](https://github.com/larose/utt) - Ultimate Time Tracker - A simple command-line time tracker written in Python.
* [Watson](https://github.com/TailorDev/Watson) - Time tracking CLI to know how much time you are spending on your projects. It can generate nice reports for clients.

## <a name="todo-manager"></a>Todo managers

Todo list and task managers.

* [boards](https://github.com/benrutter/boards) - Recursive kanban boards based around the filesystem.
* [CLI-Manager](https://github.com/MikyStar/CLI-Manager) - Command Line Interface for managing tasks locally on the fly.
* [devtodo](https://swapoff.org/devtodo.html) - A hierarchical command-line task manager, with data storage in JSON format.
* [Dooit](https://github.com/kraanzu/dooit) - Todo manager with interactive and beautiful UI, and vim keybindings.
* [dstask](https://github.com/naggie/dstask) - Single binary terminal-based TODO manager with git-based sync + markdown notes per task.
* [geek-life](https://github.com/ajaxray/geek-life) - A full featured TUI task manager.
* [grit](https://github.com/climech/grit) - A multitree-based personal task manager.
* [iKog](https://sites.google.com/site/henspace/ikog/) - A fully-featured task manager incapsulated within a Python script (just carry around the script to retain all the TODOs). When the script is run, a Python shell is opened, where task-related commands can be entered (ADD, LIST, etc.); a pity that commands are uppercase, which requires the annoying use of the Shift key.
* [kabmat](https://github.com/PlankCipher/kabmat) - TUI program for managing kanban boards with vim-like keybindings.
* [kanban-python](https://github.com/Zaloog/kanban-python) - Kanban Terminal App written in Python.
* [mayhem](https://github.com/BOTbkcd/mayhem) - A minimal TUI based task tracker.
* [mdt](https://github.com/basilioss/mdt) - A simple command-line markdown todo list manager inspired by t.
* [memo](https://www.byteptr.com/memo/) - Memo is a Unix-style note-taking software for POSIX compatible systems.
* [Redo.vc](https://redo.vc) - Redo.vc is a tool for command line fans that allows you to track your tasks. It is a full featured todo manager with tagging, projects, recurring tasks and much more, all stored in a JSON file so it is super portable and tooling new apps for the data format is super easy.
* [t](https://github.com/sjl/t) - A command-line todo list manager for people that want to finish tasks, not organize them.
* [taskbook](https://github.com/klaudiosinani/taskbook) - Tasks, boards & notes for the command-line habitat.
* [taskell](https://github.com/smallhadroncollider/taskell) - Interactive kanban board/task manager.
* [TaskWarrior](https://taskwarrior.org/) - Todo manager with advanced features, dedicated synchronization server available, many plugins and related tools, healthy software project.
* [td](https://github.com/wolandark/td) - Simple & elegant To Do list manager written In Bash.
* [td-cli](https://github.com/darrikonn/td-cli) - A command line todo manager, where you can organize and manage your todos across multiple projects.
* [todo.txt](http://todotxt.org/) - Minimalistic todo manager that uses a simple plain text file to keep track of items, implemented as a shell script.
* [Todoman](https://github.com/pimutils/todoman) - A simple, standards-based, cli todo (aka: task) manager.
* [todotxt-machine](https://pypi.org/project/todotxt-machine/) - Interfacce for todo.txt.
* [topydo](https://github.com/topydo/topydo) - A powerful todo list application for the console, using the todo.txt format.
* [tsk](https://github.com/kakengloh/tsk) - Terminal task management app with an emphasis on simplicity, efficiency and ease of use.
* [TuDu](https://code.meskio.net/tudu/) - A comand line interface to manage hierarchical todos.  Each task has a title, a long text description, a deadline (tudu warns you when the date is close), and a scheduled date. There are categories and priorities.
* [Ultralist](https://ultralist.io/) - A simple, powerful, open source task management system for the command line.
* [wish](https://github.com/levkush/wish) - A delightful wish list manager to keep track of your dreams and desires!
* [xit](https://github.com/jotaen/xit) - A plain-text file format for todos and check lists. So, not really a program, but I believe it is worth to list :-)
* [Yokadi](https://yokadi.github.io/) - Project-based todo manager: every task must be specified with a mandatory project indication. Tasks are stored within a SQLlite DB. Written in Python.  

## <a name="torrent"></a>Torrent

Clients and download managers using the BitTorrent protocol.

* [Deluge](http://deluge-torrent.org/) - A lightweight, Free Software, cross-platform BitTorrent client; a terminal curses interface, web interface and command line client can connect to a running daemon to manage torrent downloads.
* [Mabel](https://github.com/smmr-software/mabel) - A fancy BitTorrent client for the terminal built with Go and the Bubbletea library.
* [rtorrent](https://github.com/rakshasa/rtorrent) - Bittorrent client uses ncurses and is ideal for use with tmux, screen or dtach.
* [Stig](https://github.com/rndusr/stig) - Stig is a client application to connect and control the BitTorrent Transmission client app.
* [torrentCLI](https://github.com/amogusussy/torrentCLI) - Get torrents from the Terminal.
* [Transgression TUI](https://github.com/PanAeon/transg-tui) - A remote TUI client for the Transmission bittorrent program.
* [Transmission](https://transmissionbt.com/) - Fast, easy and free bittorrent client.

## <a name="typing"></a>Typing test and practice

Games and utilities to measure and/or improve the typing ability.

* [fasttyper](https://github.com/ickyicky/fasttyper) - Fasttyper is minimalistic typing test based on user provided exercising text.
* [kboard](https://github.com/CamiloGarciaLaRotta/kboard) - Terminal game to practice keyboard typing.
* [termtyper](https://github.com/kraanzu/termtyper) - A typing application to level up your fingers!
* [thokr](https://github.com/jrnxf/thokr) - Sleek typing tui with visualized results and historical logging.
* [toipe](https://github.com/Samyak2/toipe) - Yet another typing test, but crab flavoured.
* [Typespeed](http://typespeed.sourceforge.net/) - Type words that are flying by from left to right as fast as you can; features different word sets, e.g., UNIX commands, English words, Non-English words.
* [typetype](https://github.com/ahmet8zer/typetype) - Minimalistic command line typing game.
* [Typr](https://github.com/DriftingOtter/Typr) - `typr` is a Python-based application that utilizes the 'rich' module to provide you with a simple yet satisfying tui when typing, `typr` is designed to be simple and easy to use.

## <a name="utility"></a>Utilities

Miscellaneous utilities that are not do not fit in other categories and they are not numerous enough that they do not require a dedicated category.

* [asciit](https://github.com/Q1CHENL/asciit) - A more compact and intuitive ASCII table in your terminal: an alternative to "man 7 ascii" and "ascii".
* [Autocomplete](https://github.com/withfig/autocomplete) - IDE-style autocomplete for your existing terminal & shell.
* [bash-cache](https://github.com/dimo414/bash-cache) - A function memoisation / caching library for bash scripts and shells
* [bkt](https://bkt.rs) - bkt is a subprocess caching utility that makes it easy to reuse past invocations of slow commands
* [dasht](http://sunaku.github.io/dasht/man/man0/README.html) - Search API docs offline, in your terminal or browser.
* [flog](https://github.com/mingrammer/flog) - A fake log generator for log formats such as apache-common, apache error and RFC3164 syslog.
* [fzf-tab-completion](https://github.com/lincheney/fzf-tab-completion) - Tab completion using fzf.
* [GoTTY](https://github.com/yudai/gotty) - A program to turn CLI tools into web applications; basically, it runs a command and starts a server so that the output can be displayed in a web page.
* [guesswidth](https://github.com/noborus/guesswidth) - Guess the width output without delimiters in commands that output to the terminal.
* [Keep](https://github.com/keephq/keep) - Simple alerting tool, with declarative syntax and builtin providers.
* [minicloze](https://github.com/benmanone/minicloze) - Rust-based command-line language-learning game using the Tatoeba database.
* [mkdesk](https://gitlab.com/mr-draxs/mkdesk) - A program/command to create .desktop files (program launchers) using the terminal.
* [movie](https://github.com/mayankchd/movie) - A CLI for getting information about a movies and comparing two movies.
* [moviemon](https://github.com/iCHAIT/moviemon) - A Python program that displays all the information about all your movies in the command line.
* [oji](https://github.com/xxczaki/oji) - Interactive text emoji creator.
* [ora](https://github.com/sindresorhus/ora) - Elegant terminal spinner.
* [pangran](https://github.com/BimoT/pangran) - A simple TUI program that checks if you've typed a pangram.
* [plzz](https://github.com/deep5050/plzz) - A python CLI to automate daily tasks of both common and advanced users. It allows to easily launch common and different types of operations such as creating random files or check hashes.
* [Polykill](https://github.com/Bdeering1/polykill) - Lightweight command line utility for removing dependencies and build artifacts from unused local projects.
* [ps1palette](https://github.com/WDoyle123/ps1palette) - Streamline Bash PS1 customisation through script automation for prompt colour coding and .bashrc integration.
* [Python re(gex)? exercises](https://github.com/learnbyexample/TUI-apps/tree/main/PyRegexExercises) - TUI application intended to help you practice Python regular expressions there are more than 100 exercises covering both the builtin re and third-party regex module.
* [sauce](https://github.com/cadecuddy/sauce) - A novelty CLI tool that identifies an anime from an image and yields key data about it.
* [Skylab](https://github.com/SerhiiStets/skylab) - A text user interface (TUI) tool that displays upcoming space launches in a user-friendly way.
* [sprinkles](https://github.com/KhalilOuali/sprinkles) - Randomly colors input text and outputs it to the terminal.
* [teetail](https://github.com/sl236/teetail) - Like tee, but only the tail goes in the file.
* [tmux-fingers](https://github.com/morantron/tmux-fingers) - Copy pasting in terminal with vimium/vimperator like hints.
* [ttyscheme](https://github.com/kolunmi/ttyscheme) - Collection of Color Schemes for the TTY.
* [Various Scripts](https://github.com/xkcd386at/scripts) - Various script, mainly in shell and perl, to perform tasks such as combining head and tail, or other common tools accessed using fzf.
* [weather-cli](https://github.com/riyadhalnur/weather-cli) - Check the weather for your city from the terminal.
* [yank](https://github.com/mptre/yank) - Reads input from stdin and display a selection interface that allows a field to be selected and copied to the clipboard.
* [Zsh Angel IQ System](https://github.com/psprint/zsh-angel-iq-system) - A bunch of intelligent extensions to Zsh, including an in-shell Ctags browser, an extension to Zinit plugin manager and Angel Swiss Knife.

## <a name="versioning"></a>Versioning

Tools for file versioning that are not related to git.

* [Bazaar](http://bazaar.canonical.com/en/) - Multiplatform version control system supporting diffferent workflows; it is part of the GNU Project, and it is free software sponsored by Canonical.
* [fossil](https://fossil-scm.org/) - A simple, high-reliability, distributed software configuration management system with these advanced features: project management, built-in web interface, friendly self-hosting, simple networking, all-in-one standalone executable, and much more.
* [gee](https://github.com/human37/gee) - CLI repository manager and automation tool written in rust.
* [Gistup](https://github.com/mbostock/gistup) - Create a gist from terminal, then use git to update it.
* [Mercurial](https://www.mercurial-scm.org/) - Free, distributed source control management tool.
* [SnowFS](https://github.com/snowtrack/snowfs) - A high-performance application and node library for binary file versioning, initially made for the graphics industry.

## <a name="video"></a>Video

Programs to process and manage video files (downloader, editing, players, etc.).

* [CreateVideoMeme](https://github.com/hache0099/CreateMemeVideo) - Bash tool to add captions to the top of videos.
* [Editly](https://github.com/mifi/editly) - A tool and framework for declarative NLE (non-linear video editing) using Node.js and ffmpeg.
* [ffmpeg](https://ffmpeg.org/) - The Swiss knife of video editing from the command line.
* [FFMPerative](https://github.com/remyxai/FFMPerative) - Powered by Large Language Models (LLMs) through an intuitive chat interface, now you can compose video edits in natural language.
* [ffscreencast](https://github.com/cytopia/ffscreencast) - A ffmpeg screencast with video overlay and multi monitor support.
* [invidtui](https://github.com/darkhz/invidtui) - Invidious TUI client, which fetches data from invidious instances and displays a user interface in the terminal, and allows for selecting and playing Youtube audio and video.
* [lotc](https://github.com/ranelpadon/lord-of-the-clips) - (Lord Of The Clips) Video downloader, trimmer, and merger using the terminal. Supports YouTube, Facebook, Reddit, Twitter, etc. Downloads/trims at multiple points. Merges multiple clips.
* [Streamlink](https://github.com/streamlink/streamlink) - Streamlink is a CLI utility which pipes video streams from various services into a video player.
* [videoinfox](https://github.com/powerhousepro69/videoinfox) - Find videos fast. Powerful playlist building and editing. A play queue to load up unlimited playlists. Index unlimited video libraries and find videos by keyword. Download list building without leaving the browser and a Download Queue.
* [YouTube TUI](https://siriusmart.github.io/youtube-tui/) - A lightweight and user friendly TUI for browsing YouTube content from the terminal.
* [yt-splitter](https://github.com/redsolver/yt-splitter) - Downloads and splits audio tracks from a YouTube video according to the chapters/tracks. Useful for compilations or full album uploads.

## <a name="viewers"></a>Viewers

File viewers for images and other formats (e.g., e-books).

* [baca](https://github.com/wustho/baca) - Lets you indulge in your favorite e-books in the comfort of your terminal.
* [bat](https://github.com/sharkdp/bat) - A cat clone with syntax highlighting and Git integration.
* [cacaview](http://caca.zoy.org/wiki/libcaca) - A library and a program to display JPG, PNG, GIF or BMP images in the terminal using ASCII characters.
* [CAVA](https://github.com/karlstav/cava) - Cross-platform Audio Visualizer.
* [ccat](https://github.com/owenthereal/ccat) - A `cat` command with colorized output.  
* [haxor-news](https://github.com/donnemartin/haxor-news) - Browse Hacker News like a haxor: A Hacker News command line interface (CLI).
* [hexyl](https://github.com/sharkdp/hexyl) - Command-line hex viewer.
* [medium-cli](https://github.com/djadmin/medium-cli) - Medium for Hackers - Read [medium.com](https://medium.com/) stories in the terminal.
* [mplayer](http://www.mplayerhq.hu/design7/news.html) - One of the most popular video/audio players around, plays most audio and video formats (using ASCII characters) in the shell, provides a GUI for graphical visualization.
* [mpv](https://mpv.io/) - A cross-platform media player with many features such as frame timing, MKV chapters and subtitles. It is a responsive video player with minimal layout customizable with themes. A good alternative media player to VLC since it can handle almost all the media formats as VLC, but using much less resources.
* [ov](https://github.com/noborus/ov) - Feature-rich terminal-based text viewer.
* [Oyomu](https://github.com/EruEri/oyomu) - A command line comic reader and collection manager.
* [reader](https://github.com/mrusme/reader) - Reader parses a web page for its actual content and displays it in nicely highlighted text on the command line
* [TerminalImageViewer](https://github.com/stefanhaustein/TerminalImageViewer) - Small C++ program to display images in a (modern) terminal using RGB ANSI codes and unicode block graphics characters.
* [termv](https://github.com/Roshan-R/termv) - A terminal iptv player written in bash.
* [texel](https://github.com/Lauriat/texel) - Command line interface for reading spreadsheets inside terminal.
* [TubiTui](https://codeberg.org/777/TubiTui.git) - A lightweight, libre, TUI-based YouTube client
* [ucollage](https://github.com/ckardaris/ucollage) - An extensible command line image viewer inspired by vim.
* [viu](https://github.com/learn-anything/command-line-tools) - Command-line application to view images from the terminal written in Rust.
* [youtube-viewer](https://github.com/trizen/youtube-viewer) - Lightweight application that searches and streams videos from YouTube.

## <a name="browser"></a>Web browser

Web browsers with textual interface.

* [Amfora](https://github.com/makew0rld/amfora) - Amfora aims to be the best looking Gemini client with the most features. It does not support Gopher or other non-Web protocols.
* [asuka](https://git.sr.ht/~julienxx/asuka) - A Gemini Project client written in Rust with NCurses.
* [Bombadillo](https://bombadillo.colorfield.space/) - A non-web browser, designed for a growing list of protocols operating outside of the web. Currently supports Gemini, Finger and Gopher.
* [browsh](https://www.brow.sh/) - It renders anything that a modern browser can; HTML5, CSS3, JS, video and even WebGL. Its main purpose is to be run on a remote server and accessed via SSH/Mosh or the in-browser HTML service in order to significantly reduce bandwidth and thus both increase browsing speeds and decrease bandwidth costs.
* [cli-arxiv](https://github.com/knguyenanhoa/cli-arxiv) - CLI tool for exploring arXiv.
* [Elinks](http://elinks.cz/) - "Advanced and well-established feature-rich text mode web browser"; started as a fork of `Links`; it supports background download with queueing, some support from CSS, text box editing in external text editor.
* [gplaces](https://github.com/dimkr/gplaces) - Simple but powerful terminal Gemini client.
* [Graphene](https://github.com/atsepkov/Graphene) - A text-based web browser that's a joy to use.
* [Gremlin](https://github.com/actuday6418/gremlin) - Gemini browser for the terminal.
* [Links](http://www.jikos.cz/~mikulas/links//) - A textual Web browser with tables and frames.  
* [Litter](https://github.com/tuxcanfly/litter) - Litter is a minimalistic, terminal-based read-only browser that allows users to browse the web without the bloat and distractions of modern web browsers.
* [Lynx](http://lynx.invisible-island.net/) - A highly configurable text-based web browser, one of the oldest CLI browser I'm aware of.
* [min](https://github.com/a-h/min) - A Gemini browser with Vim style keyboard navigation, client certificate support and history and bookmarks saved in TSV files.
* [Romulus](https://github.com/LukeEmmet/Romulus) - A cross platform Gemini console client in C# with a simple user interface, interactive menus and mouse support.
* [s](https://github.com/zquestz/s) - Web search from the terminal. Just opens in your browser.
* [Telescope](https://telescope.omarpolo.com/) - Gemini client with UI that is strongly inspired from Emacs and W3M.
* [w3m](http://w3m.sourceforge.net/) - A text-based web browser as well as a pager like `less`, it can be used as a text formatting tool which typesets HTML into plain text.

## <a name="webdev"></a>Web development

Web development tools, including load test tools, API clients and managers, link checkers and extractors, etc..

* [ain](https://github.com/jonaslu/ain) - An HTTP API client for the terminal.
* [crawley](https://github.com/s0rg/crawley) - Unix-way web crawler: crawls web pages and prints any link it can find.
* [Discharge](https://github.com/brandonweiss/discharge) - Deploy static websites to Amazon S3.
* [dummy](https://github.com/sterrasec/dummy) - Generator of static files for testing file upload. It can generate the png file of any number of bytes!
* [http-tanker](https://github.com/PierreKieffer/http-tanker) - Terminal application used for API testing; easily create, manage and execute http requests from the terminal.
* [HTTPie](https://github.com/httpie/httpie) - HTTPie for Terminal: human-friendly CLI HTTP client for the API era.
* [Hugo](https://gohugo.io/) - The world's fastest framework for building websites.
* [iola](https://github.com/pvarentsov/iola) - A command-line socket client with REST API. It helps to work with socket servers using your favorite REST client.
* [is-up-cli](https://github.com/sindresorhus/is-up-cli) - Check whether a website is up or down using the [isitup.org](https://isitup.org/) API.
* [kanha](https://github.com/pwnwriter/kanha) - A web-app pentesting suite written in Rust.
* [linkchecker](https://github.com/linkchecker/linkchecker) - Check links in web documents or full websites.
* [lychee](https://github.com/lycheeverse/lychee) - Fast, async, resource-friendly link checker written in Rust.
* [Metalsmith](http://www.metalsmith.io/) - An extremely simple static site generator, all functionalities are provided by plugins that can be combined and chained, written and extendable in Javascript.
* [Mycorrhiza Wiki](https://mycorrhiza.wiki/) - A lightweight file-system wiki engine that uses Git for keeping history.
* [nanoc](http://nanoc.ws/) - Static site generator written in Ruby, extremely powerful and customizable, support many formats to generate HTML content.
* [pageres-cli](https://github.com/sindresorhus/pageres-cli) - Capture screenshots of websites in various resolutions. A good way to make sure your websites are responsive.
* [Reachable](https://github.com/italolelis/reachable) - Check if a domain is up.
* [s3cmd](https://github.com/s3tools/s3cmd) - Command line tool for managing Amazon S3 and CloudFront services.
* [Shopify Development Tools](https://github.com/ScreenStaring/shopify-dev-tools/) - Tools to assist with the development and/or maintenance of Shopify apps and stores.
* [siege](https://www.joedog.org/siege-home/) - An http load testing and benchmarking utility designed to let web developers stress their code.  
* [snallygaster](https://github.com/hannob/snallygaster) - Tool to scan for secret files on HTTP servers.
* [surge](https://surge.sh) - Static web publishing on surge.sh CDN.
* [Tsung](http://tsung.erlang-projects.org/) - A multi-protocol distributed load testing tool that can be used to stress HTTP, WebDAV, SOAP, PostgreSQL, MySQL, LDAP and Jabber/XMPP servers.
* [urlhunter](https://github.com/utkusen/urlhunter) - Recon tool that allows searching on URLs that are exposed via shortener services.
* [xpe](https://github.com/charmparticle/xpe) - A commandline xpath tool that is easy to use.

## <a name="writing"></a>Writing

Tools to assist the writing of text and documents, including translation, spell checking, etc..

* [alex](https://github.com/get-alex/alex) - Catch insensitive, inconsiderate writing, by finding gender favoring, polarizing, race related, or other unequal phrasing in text.
* [cambd-cli](https://github.com/rocktimsaikia/cambd) - A CLI tool to automate the process to access the Cambridge dictionary.
* [CLI-Dictionary](https://github.com/Lodobo/dict.py) - Scripts for downloading and viewing wiktionary entries from Kaikki.org.
* [Grammatical](https://github.com/pncnmnp/grammatical) - Corrects the spelling and grammar of your text using ChatGPT.
* [GTT - Google Translate TUI](https://github.com/eeeXun/GTT) - A TUI interface to bring Google Translation in the terminal.
* [Translate Shell](https://www.soimort.org/translate-shell/) - Command-line translator using Google Translate, Bing Translator, Yandex.Translate, etc.
* [trino](https://github.com/eneserdogan/trino) - Quick and easy translation of words and phrases entered in the command line.  
* [VocabCLI](https://github.com/HighnessAtharva/VocabCLI) - Lightweight CLI that allows users to look up word definitions, examples, synonyms and antonyms directly via the command line; it also offers advanced Text Classification and Processing via the use of Natural Language Processing and Machine Learning algorithms.
* [write good](https://github.com/btford/write-good) - Naive linter for English prose.


# <a name="resources"></a>Related resources

A list of some online resoures that contribute interesting links to apps and info.

[Toolleeo’s CLIpedia](https://robot.unipv.it/clipedia/) - Blog with information on CLI apps, screenshots and other details (license, author, etc.).

[The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) - A wonderful summary from Joshua Levy regarding command line (Bash in particular) tools, programs, tips and tricks; contains many pointers to resources and repositories, in the form of "to do this you must know that", which gives great pointers but requires further investigation from different sources; translated in many languages.

[Inconsolation blog](https://inconsolation.wordpress.com/) - "Adventures with lightweight and minimalist software for Linux": reviews of many command-line programs; many programs reviewed (400+, at least), with screenshots and animated GIFs; the style of presentation is ironic and funny, but requires some effort to figure out the real contribution of a program.

[A little collection of cool unix terminal/console/curses tools](https://kkovacs.eu/cool-but-obscure-unix-tools) - "Some are little-known, some are just too useful to miss, some are pure obscure..." from Kristof Kovacs; nice list with screenshot; mostly oriented to system administration; unfortunately there are no clickable links.

[Caleb Xu shell awesome](https://github.com/alebcay/awesome-shell) - Focused on UNIX shell tools.

[Adam Harris awesome CLI apps](https://github.com/aharris88/awesome-cli-apps) - Nice list of tools; somehow too much Javascript/Node.js-centered for my tastes.

[Marcel Bischoff awesome commandd line apps](https://github.com/herrbischoff/awesome-command-line-apps) - Nice up-to-date list of useful tools.

[Awesome CLI by sintaxi](https://github.com/sintaxi/awesome-cli) - Relatively short list with short descriptions; with some original entries.

[awesome-ttygames](https://ligurio.github.io/awesome-ttygames/) - Large awesome list of terminal games. The collection is maintained in a YAML format. Each item contains a description and an optional screencast.

[Site Generators](https://jamstack.org/generators/) - A comprehensive list of Static Site Generators.

[Awesome git addons](https://github.com/stevemao/awesome-git-addons) - A curated list of add-ons that extend/enhance the git CLI.

[Terminals Are Sexy](https://github.com/k4m4/terminals-are-sexy) - A curated list of Terminal frameworks, plugins & resources for CLI lovers.

[Awesome Terminal Recorder](https://github.com/orangekame3/awesome-terminal-recorder) - Curated list of outstanding terminal Recorder that make your day brighter! Each item is associated with an animated GIF that shows some examples of usage.

[commandlinefu.com](https://www.commandlinefu.com/commands/browse) - The place to record those command-line gems that you return to again and again. That way others can gain from your CLI wisdom and you from theirs too.

[cli.club](https://cli.club/) - A collection of the best CLI/Ncurses software covering a wide range of categories from messaging, music, text editing and more.



# <a name="contribute"></a>How to contribute

If you have any suggestion or want your project included in the list, you can contribute in the following ways.

## Open an issue

To suggest a new program, check the existence of the program in the list.
If it is not present, you can open an issue including the following list:

- `name`: Name of the program
- `homepage`: URL of the homepage (if it exists)
- `git`: URL of a clonable git repository (if it exists)
- `description`: Text to the description of the program

One or both of the two item `homepage` or `git` must be present.

## Pull request on `data/apps.csv`

The peculiarity of this repository is that the source of information is structured into CSV files with a simple structure.
See the `data/` directory.

If you want to contribute using a pull request, add the new entry to `data/apps.csv`.
In the CSV file, the `git` field refers to a **clonable git URL**.

Please make changes **to the CSV file only**, **not to the README file**.
I will review the request and, upon acceptance, I will take care of generating the README and updating the list.

## Contribution via email

If you prefer an email, contact me at `toolleeo@gmail.com` by sending the same information required for the "open an issue" method.

# Generation of the README file

If necessary, this `README` file can be (re-)generated from the CSV files.
To build `README.md` run:

```
make
```

`python3` is required for building. And `make`, of course. :-)

