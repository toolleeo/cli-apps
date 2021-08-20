# Forewords

This repository contains a list of (mainly) CLI apps with links and a short description.

This updated version of the repository moves the format of data files from YAML to CSV.

This ``README`` file is automatically generated from the ``.csv`` files included in the repository.
To build `README.md` run (`python3` is required for building):

```
make
```

# How to contribute

If you have any suggestion or want your project listed here, drop me an email at `toolleeo@gmail.com`.

If you want to contribute through a pull request, make sure to add new entries to the correct `.csv` file under the `data/` directory.

# Summary

To date, **333** apps/tools covered, divided in **32** categories.

# Index

[Backup](#backup) (9) | [Chat and instant messaging](#chat) (7) | [Conversion](#conversion) (4) | [Data management](#data-management) (10) | [Data transfer](#transfer) (21) | [Editors](#editors) (14) | [Email](#email) (8) | [File and file system handling](#file-handling) (25) | [File manager](#file-manager) (8) | [File systems](#file-system) (3) | [Font management](#font) (2) | [Funny tools](#funny) (9) | [Games](#games) (17) | [Graphics](#graphics) (7) | [Networking](#networking) (7) | [Office tools](#office) (10) | [Organizers and calendars](#organizers) (21) | [Productivity](#productivity) (11) | [Programming](#programming) (3) | [Security and encryption](#security) (14) | [Shells](#shells) (3) | [Sound and music](#music) (14) | [System monitoring](#monitor) (20) | [System tools](#system) (7) | [Terminals](#terminal) (6) | [Text processing](#text-processing) (13) | [Text search](#text-search) (6) | [Utilities](#utility) (21) | [Versioning](#versioning) (9) | [Viewers](#viewers) (12) | [Web browser](#browser) (6) | [Web development](#webdev) (6)

Some links to [related resources](#resources).

## <a name="backup"></a>Backup

* [borg](https://github.com/borgbackup) - Encrypted backups with a clean and simple interface; easy to use and set up; possibility to mount the backup archive with FUSE and inspect it as a regular file system.  
* [bupstash](https://github.com/andrewchambers/bupstash) - Easy and efficient encrypted backups.
* [duplicity](http://duplicity.nongnu.org/) - Creates GPG encrypted, compressed backups; client-side encryption allows to upload the backup onto untrusted servers.
* [Duply](http://duply.net/) - Simplifies the use of [duplicity](http://duplicity.nongnu.org/) by keeping clean configuration files to automate the backup.  
* [paperbackup](https://github.com/intra2net/paperbackup) - Create a pdf with barcodes to backup text files on paper.
* [rclone](https://rclone.org/) - Rclone manages file synchronization on cloud storage.
* [Unison](https://www.cis.upenn.edu/~bcpierce/unison/) - File synchronizer.
* [Zaloha.sh](https://github.com/Fitus/Zaloha.sh) - Shellscript for synchronization of files and directories.
* [zbackup](http://zbackup.org/) - A globally-deduplicating backup tool, based on the ideas found in rsync.

## <a name="chat"></a>Chat and instant messaging

* [finch](http://www.pidgin.im/) - IM program supporting many protocols, including Yahoo!, AIM, IRC, or WLM; comes with the `Pidgin` project.
* [irssi](http://www.irssi.org) - The most popular IRC client for the command-line; a flexible program, with many options and supporting many protocols.
* [matterhorn](https://github.com/matterhorn-chat/matterhorn) - A terminal client for the Mattermost chat system.
* [RainbowStream](http://www.rainbowstream.org/) - Twitter client for the terminal; allows almost all the operations that can be done from GUI and Web clients.
* [ssh-chat](https://github.com/shazow/ssh-chat) - Custom SSH server written in Go. Instead of a shell, you get a chat prompt.
* [tiny](https://github.com/osa1/tiny) - tiny is an IRC client written in Rust.
* [WeeChat](http://weechat.org/) - A "fast, light and extensible chat client".

## <a name="conversion"></a>Conversion

* [catdoc](http://www.wagner.pp.ru/~vitus/software/catdoc/) - Command line converter from Microsoft Word to plain text; output is sent to the standard output.  
* [mdBook](https://github.com/rust-lang/mdBook) - Create book from markdown files.
* [Pandoc](http://pandoc.org/) - Universal document file converter; handles input output from/to a number of formats: HTML, PDF, LaTeX, docx, odt, AsciiDoc, Markdown, Textile, just to mention a few; the quality of conversion strongly depends on the combination of input/output formats.
* [xls2csv](http://www.wagner.pp.ru/~vitus/software/catdoc/) - Command line converter from Excel to CSV file format.  

## <a name="data-management"></a>Data management

* [csvkit](https://github.com/wireservice/csvkit) - A suite of command-line tools for converting to and working with CSV, the king of tabular file formats.
* [datadash](https://github.com/keithknott26/datadash) - Visualize and graph data in the terminal.
* [Dolt](https://github.com/dolthub/dolt) - Dolt is Git for Data! Dolt is a SQL database that you can fork, clone, branch, merge, push and pull just like a git repository.
* [GNU Recutils](https://www.gnu.org/software/recutils/manual/) - Set of tools and libraries to access human-editable, text-based databases called recfiles.
* [jtc](https://github.com/ldn-softdev/jtc) - JSON manipulation and transformation.
* [tabview](https://github.com/TabViewer/tabview) - Python curses command line CSV and tabular data viewer.
* [TSV Utilities](https://github.com/eBay/tsv-utils) - Command line tools for large, tabular data files.
* [usql](https://github.com/xo/usql) - Universal command-line interface for SQL databases.
* [VisiData](https://www.visidata.org/) - Interactive multitool for tabular data. It combines the clarity of a spreadsheet, the efficiency of the terminal, and the power of Python, into a lightweight utility which can handle millions of rows with ease.
* [xsv](https://www.johndcook.com/blog/2019/12/31/sql-join-csv-files/) - Doing a SQL join with CSV files.

## <a name="transfer"></a>Data transfer

* [aria2](https://github.com/aria2/aria2) - Lightweight and easy-to-use download utility; it supports HTTP/HTTPS, FTP, SFTP, BitTorrent, Metalink and multiple sources; cross-platform.
* [croc](https://github.com/schollz/croc) - Easily and securely send things from one computer to another.
* [curl](https://curl.haxx.se/) - A tool and library for transferring data with URL syntax; supports a lot of protocols.  
* [Deluge](http://deluge-torrent.org/) - A lightweight, Free Software, cross-platform BitTorrent client; a terminal curses interface, web interface and command line client can connect to a running daemon to manage torrent downloads.
* [lftp](https://lftp.yar.ru/) - "Sophisticated ftp/http client, and a file transfer program supporting a number of network protocols"; support for bookmarks and mirroring features.
* [Magic Wormhole](https://github.com/warner/magic-wormhole) - The program allows transfer arbitrary-sized files and directories (or short pieces of text) from one computer to another The two endpoints are identified by using identical human-readable codes.  
* [OnionShare](https://onionshare.org/) - "An open source tool that lets you securely and anonymously share a file of any size." 
* [qr-filetransfer](https://github.com/sdushantha/qr-filetransfer) - Transfer files over WiFi between your computer and your smartphone from the terminal.
* [qrcp](https://www.linuxuprising.com/2020/07/qrcp-transfer-files-between-desktop-and.html) - Transfer Files Between Desktop And Mobile Devices Over Wi-Fi By Scanning A QR Code.
* [rsync](https://download.samba.org/pub/rsync/rsync.html) - Mirror directories across networked machines; handles diffs/changed files; works across SSH; plenty of parameters.  
* [rtorrent](https://github.com/rakshasa/rtorrent) - Bittorrent client uses ncurses and is ideal for use with tmux, screen or dtach.
* [sitecopy](http://www.manyfish.co.uk/sitecopy/) - Synchronizes a local copy of a website with a remote copy on a server; does not use SSH/`scp` but FTP for file copy; useful when the remote server does not support secure copy.  
* [stftp](http://stftp.sourceforge.net/) - (simple terminal FTP) aims to be a "easy-to-use and unbloated client for the UNIX (and UNIX-like) console".
* [Transmission](https://transmissionbt.com/) - Fast, easy and free bittorrent client.
* [Woof](http://www.home.unix-ag.org/simon/woof.html) - (Web Offer One File) sets up an HTTP webserver to serve files from a given local directory; all the users connected to the network can see and download the files.  
* [xh](https://github.com/ducaale/xh) - xh is a friendly and fast tool for sending HTTP requests. It reimplements as much as possible of HTTPie's excellent design.
* [youtube-dl](http://rg3.github.io/youtube-dl/) - Downloads videos from [YouTube](https://www.youtube.com/) and some other sites; useful for automated bulk downloads.  
* [youtube-viewer](https://github.com/trizen/youtube-viewer) - Lightweight application that searches and streams videos from YouTube.
* [yt-splitter](https://github.com/redsolver/yt-splitter) - Downloads and splits audio tracks from a YouTube video according to the chapters/tracks. Useful for compilations or full album uploads.
* [ytfzf](https://github.com/pystardust/ytfzf) - A POSIX script that helps you find Youtube videos (without API) and opens/downloads them using mpv/youtube-dl.
* [ytmdl](https://github.com/deepjyoti30/ytmdl) - Get songs from Youtube in mp3 format.

## <a name="editors"></a>Editors

* [Emacs](https://www.gnu.org/software/emacs/) - One of the godfathers of text editors; free long-standing software project; tons of extensions and funcionalities; the biggest drawback (my taste): it needs [E-Lisp](https://www.gnu.org/software/emacs/manual/eintr.html) for being programmed.  
* [eon](https://github.com/tomas/eon) - A light, modern editor for your terminal that doesn't want to be vim.
* [jed](http://www.jedsoft.org/jed/index.html) - A text editor with a drop-down menu facility that make it especially user-friendly.  
* [joe](http://joe-editor.sourceforge.net/) - (Joe's Own Editor) is a compact text editor written in C; a detailed list of features and missing ones is explicitly reported in the website; this editor is mentioned in several web sources for its capability in handling large files.  
* [Kakoune](http://kakoune.org/) - Modal editor, faster as in less keystrokes, multiple selections, orthogonal design.
* [micro](https://github.com/zyedidia/micro/) - A terminal-based text editor written in Go that aims to be easy to use and intuitive, while also taking advantage of the full capabilities of modern terminals.
* [nano](https://www.nano-editor.org/) - Easy to use, lightweigth text editor; no complex keybindings to remember.
* [neovim](https://neovim.io/) - A work in progress attempt to improve [vim](http://www.vim.org/), dropping older/unused OS compatibility, improving the codebase readability, modularity and maintainability; it has chances to become the next choice of vim users.
* [slap](https://github.com/slap-editor/slap) - Text editor inspired by [Sublime Text](https://www.sublimetext.com/) written in NodeJS; extedable in Javascript.  
* [vai](https://github.com/stefanoborini/vai) - A text editor similar to `vim` written in Python; many feature are nicely replicated, some are still missing; however, the advantage of this implementation is its simplicity, maintainability and extensibility, thanks to the Python implementation.
* [vim](http://www.vim.org/) - Historically one of the preferred text editors; behavior based on editing modes; plenty of plugins and tips to address every possible editing problem.  
* [vis](https://github.com/martanne/vis) - "a modern, legacy free, simple yet efficient vim-like editor", and more: "The intention is not to be bug for bug compatible with vim, instead a similar editing experience should be provided. The goal could thus be summarized as 80% of vim's features implemented in roughly 1% of the code"; the editor is scriptable in LUA and supports editing large files.
* [vy](https://github.com/vyapp/vy) - A vim-like in python made from scratch.
* [WordGrinder](https://cowlark.com/wordgrinder/) - From the website: "WordGrinder is a word processor for processing words. It is not WYSIWYG. It is not point and click. It is not a desktop publisher. It is not a text editor. It does not do fonts and it barely does styles. What it does do is words. It's designed for writing text. It gets out of your way and lets you type." 

## <a name="email"></a>Email

* [alot](https://github.com/pazz/alot) - MUA written in Python using the [NotMuch](https://notmuchmail.org/) backend; MailDir format support.  
* [alpine](http://www.washington.edu/alpine/) - Mail client which aims at being "fast, easy to use email client that is suitable for both the inexperienced email user as well as for the most demanding of power users".
* [mbsync](http://isync.sourceforge.net/mbsync.html) - Mailboxes synchronization tool; allows to download email locally; MailDir format supported.  
* [Mutt](http://www.mutt.org/) - Mail client with tons of features, customization chances, support for IMAP, POP3, multiple storage formats.
* [NeoMutt](https://neomutt.org/) - Patched and up-to-dated mutt fork.
* [Newsbeuter](http://newsbeuter.org/) - "The Mutt of RSS Feed Readers": Newsbeuter is an open-source RSS/Atom feed reader for text terminals. Has great configurability and vast number of features, making it a slick and fast feed reader that can be completely controlled via keyboard.
* [nmail](https://github.com/d99kris/nmail) - nmail is a console-based email client for Linux and macOS with a user interface similar to alpine / pine.
* [sup](http://sup-heliotrope.github.io/) - MUA written in Ruby; specifically developed for accounts with "a lot of emails"; nice thread-based presentation.

## <a name="file-handling"></a>File and file system handling

* [alder](https://github.com/aweary/alder) - Directory tree visualizer.
* [broot](https://dystroy.org/broot/) - A new way to navigate directory trees on linux, made in rust.
* [classifier](https://github.com/bhrigu123/classifier) - Organize files in your current directory, by classifying them into folders of music, pdfs, images, etc.
* [detox](http://detox.sourceforge.net/) - A utility designed to easily clean up filenames; it replaces characters like spaces with standard equivalents; it also replace UTF-8 or Latin-1 (or CP 1252) characters with more handy ones.  
* [dtrx](https://brettcsmith.org/2007/dtrx/) - (Do The Right eXtraction) aims at taking "all the hassle out of extracting archives"; allows to use one command to extract archives in different formats, recursive extraction (files into file) and extracts files into dedicated directories.
* [dua](https://github.com/Byron/dua-cli) - Disk Usage Analyzer. Learn about the usage of disk space of a given directory with parallel access to max out SSD exploration.
* [duf](https://github.com/muesli/duf) - Disk Usage/Free Utility.
* [dutree](https://github.com/nachoparker/dutree) - A tool to analyze file system usage written in Rust.
* [exa](https://the.exa.website/) - Replacement for 'ls' written in Rust, with colors and several additional "views".
* [F2](https://github.com/ayoisaiah/f2) - Cross-platform command-line tool for batch renaming files and directories quickly and safely.
* [fasd](https://github.com/clvv/fasd) - A Commandline Tool That Offers Quick Access to Files and Directories. It offers quick access to files and directories for POSIX shells.  It is inspired by tools like autojump, z and v. Fasd keeps track of files and directories you have accessed, so that you can quickly reference them in the command line.
* [fd](https://github.com/sharkdp/fd) - A simple, fast and user-friendly alternative to find. Written in Rust.
* [gcp](https://github.com/petronny/gcp) - `gcp` (Goffi’s cp) is an advanced file copier tool, heavily inspired from the traditional `cp` command utility, but with some additional features: Displays the copy progress indicator, with estimated time, current file speed; logs of all actions; resume of interrupted copy processes.
* [gdu](https://github.com/dundee/gdu) - Pretty fast disk usage analyzer written in Go. Gdu is intended primarily for SSD disks where it can fully utilize parallel processing. However HDDs work as well, but the performance gain is not so huge.
* [ncdu](https://dev.yorhel.nl/ncdu) - "A disk usage analyzer with an ncurses interface.  It is designed to find space hogs on a remote server where you don't have an entire graphical setup available."
* [PathPicker](https://facebook.github.io/PathPicker/) - A tool from Facebook that parses the output from a command and presents a UI to select files and directories; can be used to apply a command of a interactively selected files or to move across directories.  
* [rename](https://www.kernel.org/pub/linux/utils/util-linux/) - Included in `util-linux`, allows bulk rename of files with regex support.
* [renameutils](http://www.nongnu.org/renameutils/) - A set of programs to change file and directory names by editing them inplace; I find `imv` especially useful to edit a filename at the program prompt.  
* [rmlint](https://github.com/sahib/rmlint/) - A tool to recursively scan a directory tree looking for duplicate and broken files; it outputs statistics and save the list of files in JSON format; it produce a shell script that can be inspected before running it to delete the desire files.  
* [tree](http://mama.indstate.edu/users/ice/tree/) - "Recursive directory listing command that produces a depth indented listing of files".
* [twf](https://github.com/wvanlint/twf) - Standalone tree view file explorer.
* [vidir](https://github.com/trapd00r/vidir) - vidir allows editing of the contents of a directory in a text editor.
* [vizex](https://github.com/bexxmodd/vizex) - Visualize the disk space usage for every partition and media on the user's machine.
* [xplr](https://github.com/sayanarijit/xplr) - A hackable, minimal, fast TUI file explorer, stealing ideas from nnn and fzf.
* [zoxide](https://github.com/ajeetdsouza/zoxide) - A faster way to navigate your filesystem.

## <a name="file-manager"></a>File manager

* [clifm](https://github.com/leo-arch/clifm) - A CLI-based, shell-like, and non-curses terminal file manager written in C: simple, fast, extensible, and lightweight as hell.
* [lfm](https://inigo.katxi.org/devel/lfm/) - (Last File Manager) is a file manager written in Python; it comes with lots of features, including 1-pane or 2-pane view, files filters and bookmarks, tree view, virtual file-systems to open compressed archives, search in files, customizable keybindings and themes.
* [Midnight Commander](http://www.midnight-commander.org/) - a visual file manager, full-screen text mode application that allows you to copy, move and delete files and whole directory trees and search for files; includes an internal viewer and editor.
* [ncursesFM](https://github.com/FedeDP/ncursesFM) - File manager written in C; rather complete in terms of features; especially lightweight and responsive.  
* [nnn](https://github.com/jarun/nnn) - "The missing terminal file browser for X". Provides only directory traversal and file visualization.  No delete/move operations are supported.
* [ranger](http://ranger.nongnu.org/) - Console file manager with vi key bindings; curses interface with a view on the directory hierarchy; comes a file launcher that automatically finds out which program to use for a given file type.  
* [rnr](https://github.com/bugnano/rnr) - The RNR File Manager (RNR's Not Ranger) is a text based file manager that combines the best features of Midnight Commander and Ranger.
* [vifm](https://vifm.info/) - "ncurses based file manager with vi like keybindings/modes/options/commands/configuration, which also borrows some useful ideas from mutt" (cit.).

## <a name="file-system"></a>File systems

* [sshfs](https://github.com/libfuse/sshfs) - Locally mount a remote file-system through SSH and access files and directory as they would be on the local machine.  
* [TMSU](http://tmsu.org/) - A tool for tagging files; it provides a simple command line tool for applying tags and a virtual filesystem so that you can get a tag-based view of your files from within any other program.  
* [wutag](https://github.com/wojciechkepka/wutag) - CLI Tool for tagging and organizing files by tags.

## <a name="font"></a>Font management

* [FIGlet](http://www.figlet.org/) - Not exactly a font manager, but a nice program for making large letters out of ordinary text; an astonishing number of different fonts is available.
* [toilet](http://caca.zoy.org/wiki/toilet) - A program that tries to improve `FIGlet`; can load FIGlet fonts; supports Unicode input and output, colour fonts and output, and various output formats, including HTML, IRC and ANSI; uses `libcaca` to produce nice textual effects.

## <a name="funny"></a>Funny tools

* [asciiacquarium](http://www.robobunny.com/projects/asciiquarium/html/) - Enjoy the mysteries of the sea from the safety of your own terminal!
* [cbonsai](https://gitlab.com/jallbrit/cbonsai) - A bonsai tree generator, written in C using ncurses. It intelligently creates, colors, and positions a bonsai tree.
* [cmatrix](http://www.asty.org/cmatrix/) - ncurses program that display the scrolling lines found in the movie `The matrix`.
* [cowsay](https://en.wikipedia.org/wiki/Cowsay) - A program that generates a ASCII art of a cow with a bubble containing the specified message (I provide the Wikipedia link since at the moment the link to the author's homepage results to be unreachable).  
* [cowthink](https://en.wikipedia.org/wiki/Cowsay) - Same as `cowsay`, but uses a "think" bubble instead of a speech bubble.
* [fortune](http://software.clapper.org/fortune/) - Generates random messages feched from a quotation database.  
* [sha256-animation](https://github.com/in3rsha/sha256-animation) - Animation of the SHA-256 hash function in your terminal.
* [Steam Locomotive](http://www.cyberciti.biz/tips/displays-animations-when-accidentally-you-type-sl-instead-of-ls.html) - A steam locomotive traverses the screen from right to left if `sl` is typed instead of `ls`.  
* [ternimal](https://github.com/p-e-w/ternimal) - Simulate a lifeform in the terminal.

## <a name="games"></a>Games

* [bastet](http://fph.altervista.org/prog/bastet.html) - (Bastard Tetris) implements the classical Tetris but with a logic to generate the next block which maximizes the difficulty for the player.  
* [Cataclysm: Dark Days Ahead](https://cataclysmdda.org/) - Open source turn-based survival RPG development project.
* [chs](https://github.com/nickzuber/chs) - Play chess against the Stockfish engine in your terminal.
* [crappybird-py](https://github.com/JonPizza/crappybird-py) - Flappy bird.
* [Dwarf fortress](http://www.bay12games.com/dwarves/) - A fantasy game using ASCII art graphical representation of the game environment; it features a rich environment with many options and possibilities.  
* [freesweep](http://www.upl.cs.wisc.edu/~hartmann/sweep/) - A Minesweeper clone for the terminal which allows you to configure settings such as table rows and columns up to 1024x1024!), percentage of bombs, colors and also has a highscores table.
* [Language-games](https://github.com/Hellisotherpeople/Language-games) - Dead simple games made with word vectors.
* [minesweeper](https://github.com/gazpachoking/minesweeper) - Cross-platform terminal based minesweeper.
* [Nethack](http://nethack.org/) - Single player rogue-like dungeon exploration game.
* [Oldrunner](http://culot.org/public/Code/oldrunner.html) - Character-based remake of Lode Runner; includes all the original 150 levels.  
* [rpg-cli](https://github.com/facundoolano/rpg-cli) - Your filesystem as a dungeon!
* [Slash'EM](http://slashem.sourceforge.net/) - Rogue-like game derived from `nethack` offering extra features, monsters, and items; includes a GUI version.
* StarWars vision - See Star Wars in ASCII with ``telnet towel.blinkenlights.nl``.  
* [Terminal Phase](https://dustycloud.org/blog/terminal-phase-1.0/) - A space shooter game you can play in your terminal.
* [terminal_board_games](https://github.com/salt-die/terminally_bored_terminal_board_games) - Board games for the terminal.
* [Typespeed](http://typespeed.sourceforge.net/) - Type words that are flying by from left to right as fast as you can; features different word sets, e.g., UNIX commands, English words, Non-English words.
* [usolitaire](https://github.com/eliasdorneles/usolitaire) - Solitaire in your terminal.

## <a name="graphics"></a>Graphics

* [chafa](https://github.com/hpjansson/chafa) - Terminal graphics for the 21st century.
* [ImageMagick](http://www.imagemagick.org/script/index.php) - Software suite to create, edit, compose, or convert bitmap images; it handles many file formats (including PDF and SVG) and provides processing tools to "resize, flip, mirror, rotate, distort, shear and transform images, adjust image colors, apply various special effects, or draw text, lines, polygons, ellipses and Bézier curves".
* [imgcat](https://github.com/trashhalo/imgcat) - Tool to output images in the terminal. Built with bubbletea.
* [imgp](https://github.com/jarun/imgp) - A command line image resizer and rotator for JPEG and PNG images. It can resize (or thumbnail) and rotate thousands of images in a go, at lightning speed, while saving significantly on storage.
* [pastel](https://github.com/sharkdp/pastel) - A command-line tool to generate, analyze, convert and manipulate colors.
* [scrot](https://github.com/dreamer/scrot) - A simple CLI tool to capture screenshots.  
* [TerminalImageViewer](https://github.com/stefanhaustein/TerminalImageViewer) - Small C++ program to display images in a (modern) terminal using RGB ANSI codes and unicode block graphics characters.

## <a name="networking"></a>Networking

* [bandwhich](https://github.com/imsnif/bandwhich) - Terminal bandwidth utilization tool.
* [geoiplookup](https://github.com/maxmind/geoip-api-c) - a little application to find geographical and network information of an IP address based no the geoip C API.
* [ipcalc](http://jodies.de/ipcalc) - "ipcalc takes an IP address and netmask and calculates the resulting broadcast, network, Cisco wildcard mask, and host range." 
* [mitmproxy](https://mitmproxy.org/) - An interactive HTTPS proxy.
* [PSSH](https://code.google.com/archive/p/parallel-ssh/) - PSSH provides parallel versions of OpenSSH and related tools. Included are pssh, pscp, prsync, pnuke, and pslurp. The project includes psshlib which can be used within custom applications.
* [quickserve](https://github.com/charliesome/quickserve) - Quickserve is a very simple HTTP server written in Python that is intended for quickly sharing files on an ad-hoc basis. Aside from opening a port in your firewall if you have one, quickserve requires no set-up and should work with no hassle.
* [rtop](http://www.rtop-monitor.org/) - rtop is a simple, agent-less, remote server monitoring tool that works over plain SSH. Written in golang, it does not need any software to be installed on the server that you want to monitor. It works by establishing an SSH session, and running commands on the remote server to collect system metrics.

## <a name="office"></a>Office tools

* [bib.awk](https://github.com/huijunchen9260/bib.awk) - Bibliography manager written in awk.
* [conrad](https://github.com/vinayak-mehta/conrad) - Track conferences and meetups.
* [sc-im](https://github.com/andmarti1424/sc-im) - Spreadsheet Calculator Improvised -- An ncurses spreadsheet program for terminal. It is rich in functionalities, but the syntax of functions and other details are different from the common spreadsheets such as Excel and Calc, making difficult to "re-cycle" existing knowledge on these programs to work proficiently with sc-im. Neverthless, a nice piece of software."
* [scholarref](https://adamsgaard.dk/scholarref.html) - Tools to never deal with journal webpages again.
* [Teapot](https://www.syntax-k.de/projekte/teapot/) - Compact ncurses-based spreadsheet with original syntax, 3D-style and built-in functions.
* [Ticker](https://github.com/achannarasappa/ticker) - Terminal stock watcher and stock position tracker.
* [tpp](http://www.ngolde.de/tpp.html) - (text presentation program) a ncurses Ruby program that allows to produce nice text-based presentation with simple markup language.
* [translate-shell](https://github.com/soimort/translate-shell) - Command-line translator using Google Translate or other online services.
* [trino](https://github.com/eneserdogan/trino) - Quick and easy translation of words and phrases entered in the command line.  
* [wikit](https://github.com/KorySchneider/wikit) - A command line program for getting Wikipedia summaries easily.

## <a name="organizers"></a>Organizers and calendars

* [buku](https://github.com/jarun/buku) - A powerful bookmark manager written in Python3 and SQLite3.
* [calcurse](https://calcurse.org/) - A calendar and scheduling application for the command line. It helps keep track of events, appointments and everyday tasks.
* [dstask](https://github.com/naggie/dstask) - Single binary terminal-based TODO manager with git-based sync + markdown notes per task.
* [gcalcli](https://github.com/insanum/gcalcli) - CLI to access Google Calendars; allows to do the main tasks: create, delete, and list events.
* [goobook](https://gitlab.com/goobook/goobook) - The purpose of GooBook is to make it possible to use your Google Contacts from the command-line and from MUAs such as Mutt.  It can be used from Mutt the same way as abook.
* [grit](https://github.com/climech/grit) - A multitree-based personal task manager.
* [iKog](https://sites.google.com/site/henspace/ikog/) - A fully-featured task manager incapsulated within a Python script (just carry around the script to retain all the TODOs). When the script is run, a Python shell is opened, where task-related commands can be entered (ADD, LIST, etc.); a pity that commands are uppercase, which requires the annoying use of the Shift key.
* [kb](https://github.com/gnebbia/kb) - A minimalist knowledge base manager.
* [khal](https://github.com/pimutils/khal) - CLI and terminal calendar program, able to synchronize with CalDAV servers through [vdirsyncer](https://github.com/pimutils/vdirsyncer).
* [khard](https://github.com/lucc/khard) - Console carddav client written in Pyhton.  
* [Org mode](http://orgmode.org/) - Super-powerful [Emacs](https://www.gnu.org/software/emacs/) plugin to manage outlines with associated timestamps, priorities, labels, etc.; available views grouped by time (agenda), tags, etc.; plain text storage format.
* [pal](http://palcal.sourceforge.net/) - Calendar program for Unix/Linux systems that can keep track of events; custom, plain text storage format; interesting and fully functional.
* [ppl addressbook](http://ppladdressbook.org/) - ``ppl`` is free software made out of other free software.  It's built on top of Ruby and Git, and the completely free vcard address book format.
* [Remind](https://www.roaringpenguin.com/products/remind) - Calendar program with possibility to set complex rules to define events; custom, powerful text-based storage format.
* [TaskWarrior](https://taskwarrior.org/) - Todo manager with advanced features; dedicated synchronization server available; many plugins and related tools; healthy software project.  
* [todo.txt](http://todotxt.org/) - Minimalistic todo manager that uses a simple plain text file to keep track of items; implemented as a shell script.  
* [todolist](http://todolist.site/) - A minimal clone of [Wunderlist](https://www.wunderlist.com/), with 30% of its features. GTD oriented. It stores the task list in a hidden JSON file in the home directory, making it easy to backup or share them.
* [todotxt-machine](https://pypi.org/project/todotxt-machine/) - Interfacce for todo.txt.
* [TuDu](https://code.meskio.net/tudu/) - A comand line interface to manage hierarchical todos.  Each task has a title, a long text description, a deadline (tudu warns you when the date is close), and a scheduled date. There are categories and priorities.
* [Wyrd](http://freecode.com/projects/wyrd/) - Curses front-end for [Remind](https://www.roaringpenguin.com/products/remind) written in OCaml with vertically scrollable time table.  
* [Yokadi](https://yokadi.github.io/) - Project-based todo manager: every task must be specified with a mandatory project indication. Tasks are stored within a SQLlite DB. Written in Python.  

## <a name="productivity"></a>Productivity

* [arbtt](http://arbtt.nomeata.de/) - (automatic, rule-based time tracker) runs in background, collecting information regarding open windows, focussed ones, etc.; it can be configured to display statistics on the collected data, e.g., figuring out the time spent on one specific window.
* [cadmus](https://github.com/RyanGreenup/cadmus) - Shell Scripts to Facilitate Effective Note Taking.
* [dijo](https://github.com/NerdyPepper/dijo) - Scriptable, curses-based, digital habit tracker.
* [dn](https://github.com/tomlockwood/dn) - Daily notes command line tool.
* [jnrl](https://github.com/maebert/jrnl) - Collect your thoughts and notes without leaving the command line.
* [ledger](http://ledger-cli.org/) - A powerful, double-entry accounting system from the command-line; it uses a simple yet powerful text syntax to specify the items to account.
* [posce](https://github.com/posce/posce) - A note-taking toolkit for your command line.
* [Qalculate](https://qalculate.github.io/) - Multi-purpose calculator with customizable functions, units, arbitrary precision, plotting (it includes a GUI).
* [Standard Unix Notes](https://github.com/Standard-Unix-Notes/unix-notes) - GPG Encrypted Notes/Notebook manager for BSD/Linux.
* [Translate Shell](https://www.soimort.org/translate-shell/) - Command-line translator using Google Translate, Bing Translator, Yandex.Translate, etc.
* [tuxi](https://github.com/Bugswriter/tuxi) - A CLI tool that scrapes Google search results and SERPs that provides instant and concise answers.

## <a name="programming"></a>Programming

* [gdb-dashboard](https://github.com/cyrus-and/gdb-dashboard) - Modular visual interface for GDB in Python.
* [nbterm](https://github.com/davidbrochart/nbterm) - Jupyter Notebooks in the terminal.
* [rr](https://rr-project.org/) - Debug the recording, deterministically, as many times as you want.

## <a name="security"></a>Security and encryption

* [cipher](https://github.com/ash-shell/cipher) - An Ash module that makes it easy to perform aes-256-cbc encryption for files and directories.  
* [dpg](https://github.com/62726164/dpg) - The Deterministic Password Generator - Generates passwords based on a master password and the indication of the website/service/username, without the need of storing anything.
* [encfs](http://www.arg0.net/#!encfs/c1awt) - Encrypted filesystem in user-space based on [FUSE](https://it.wikipedia.org/wiki/FUSE); mounts an encrypted directory into a clear one.  
* [Firejail](https://firejail.wordpress.com/) - A SUID program that reduces the risk of security breaches by restricting the running environment of untrusted applications using Linux namespaces and seccomp-bpf.
* [GnuPG](https://gnupg.org/) - GnuPG is a complete and free implementation of the OpenPGP standard as defined by RFC4880 (also known as PGP).
* [gopass](https://www.gopass.pw/) - gopass is a rewrite of the pass password manager in Go with the aim of making it cross-platform and adding additional features. The target audience are professional developers and sysadmins (and especially teams of those) who are well versed with a command line interface.
* [hashcat](https://hashcat.net/hashcat/) - A robust and efficient password cracking tool that can help you recover lost passwords, audit password security, benchmark, or just figure out what data is stored in a hash.
* [hide](https://github.com/whatl3y/hide) - AES-256 bit encrypted password manager with all encrypted passwords stored locally on your machine
* [kpcli](http://kpcli.sourceforge.net/) - A command line interface for KeePass.
* [LUKS](https://guardianproject.info/code/luks/) - Hard disk encryption tool; it stores all setup information in the partition header, enabling easy data transport or migration.
* [pass](https://www.passwordstore.org/) - With pass, each password lives inside of a gpg encrypted file whose filename is the title of the website or resource that requires the password. These encrypted files may be organized into meaningful folder hierarchies, copied from computer to computer, and, in general, manipulated using standard command line file management utilities.
* [safe.sh](https://github.com/windowsrefund/safe) - Pure Bash script to manage secure archives; simple and clean; uses [gnugpg](https://gnupg.org/) for encryption/decryption, thus can leverage tools like [GPG Agent](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html).
* [SpicyPass](https://github.com/JFreegman/SpicyPass) - A light-weight password manager with a focus on simplicity and security.
* [titan](https://www.byteptr.com/titan/) - Password management belongs to the command line, deep into the Unix heartland, the shell. Titan is written in C and is available under the MIT license.

## <a name="shells"></a>Shells

* [Bash](https://www.gnu.org/software/bash/) - (Bourne Again SHell) The most widespread system shell to date.  
* [Fish](https://fishshell.com/) - "A command line shell for the 90s"; focused on user-friendliness, with powerful autosuggestions, colors, "sane scripting" (w.r.t. to Bash).
* [Zsh](http://www.zsh.org/) - Alternative shell designed for interactive use.  

## <a name="music"></a>Sound and music

* [Alsamixer](http://www.alsa-project.org/main/index.php/Main_Page) - ALSA mixer with curses interfaces.  
* [castero](https://github.com/xgi/castero) - A TUI podcast client for the terminal.
* [cmus](https://cmus.github.io/) - A fast and lightweight audio player with configurable keybindings and playlist support.  
* [espeak](http://espeak.sourceforge.net/) - A compact open source software speech synthesizer for English and other languages.
* [kord](https://github.com/synestematic/kord) - A python framework that provides programmers with a simple api for the creation of music-based applications.
* [MOC](https://moc.daper.net/) - (music on console) is a powerful and easy to use console audio player; user interface a la Midnight Commander; plenty of features; fully controllable from the keyboard.  
* [Mp3blaster](http://www.mp3blaster.org/?m=1) - Audio player for the text console.
* [mpg123](http://mpg123.org/) - Quick `mp3` sound file player; no visual interface, just a command-line audio file player for `mp3` files.
* [mps-youtube](https://github.com/mps-youtube/mps-youtube) - A curses player for music tracks from Youtube; it allows to search for songs and playlists; it downloads the video, extracts the audio track and plays it; handles local playlists and many configuration parameters.
* [muCLIar](https://github.com/aayush1205/muCLIar) - YouTube automator bringing you your music right on your CLI.
* [ncmpcpp](https://rybczak.net/ncmpcpp/) - NCurses Music Player Client (Plus Plus) - featureful ncurses based MPD client inspired by ncmpc. Relevant features: tag editor, playlist editor, easy to use search engine, media library, music visualizer, ability to fetch artist info from [last.fm](https://www.last.fm/), new display mode, alternative user interface, ability to browse and add files from outside of MPD music directory.
* [ogg123](https://www.xiph.org/downloads/) - Quick `ogg` sound file player; no visual interface, just a command-line audio file player for the free and open `ogg` file format.
* [Siren](https://www.kariliq.nl/siren/) - Siren is a text-based audio player for UNIX-like operating systems.
* [yt-audio](https://github.com/pseudoroot/yt-audio) - A simple, configurable youtube-dl wrapper to download and manage youtube audio.

## <a name="monitor"></a>System monitoring

* [below](https://github.com/facebookincubator/below) - A time traveling resource monitor for modern Linux systems
* [bpytop](https://github.com/aristocratos/bpytop) - Linux/OSX/FreeBSD resource monitor with a nice interface.
* [cv](https://github.com/Xfennec/progress) - (Coreutils Progress Viewer) "looks for coreutils basic commands (`cp`, `mv`, `dd`, `tar`, `gzip/gunzip`, `cat`, etc.) currently running on your system and displays the percentage of copied data. It can also show estimated time and throughput".
* [dmidecode](https://www.nongnu.org/dmidecode/) - System information utility.
* [glances](https://nicolargo.github.io/glances/) - A comprehensive and detailed system monitoring tool; monitored parameters include: CPU, memory, load, process list, network interfaces, disk I/O, sensors, filesystems, docker, system info, uptime.
* [GoTTY](https://github.com/yudai/gotty) - A program to turn CLI tools into web applications; basically, it runs a command and starts a server so that the output can be displayed in a web page.
* [htop](http://hisham.hm/htop/) - An interactive process viewer for Unix; improves the UI of `top`, by adding real-time meters and colors.
* [inxi](http://smxi.org/docs/inxi.htm) - A comprehensive system information script; provides information about CPU, graphics, audio and network devices, drives and partitions, sensors; implemented as a Bash script.
* [iotop](http://guichaz.free.fr/iotop/) - "A Python program with a top like UI used to show of behalf of which process is the I/O going on".
* [lfs](https://github.com/Canop/lfs) - A thing to get information on your mounted disks
* [multitail](https://www.vanheusden.com/multitail/) - A command to open multiple log files in a single terminal window and monitor them in real-time.  
* [ngrep](http://ngrep.sourceforge.net/) - (Network grep) applies the `grep` logic to the network layer, allowing to match regular expressions against data payloads of packets; it recognizes IPv4/6, TCP, UDP, ICMPv4/6, IGMP and Raw across Ethernet, PPP, SLIP, FDDI, Token Ring and null interfaces.
* [powertop](https://01.org/powertop) - A `top`-like utility to monitor the sources of power consumption; allows to turn on/off many components; quite useful to track possible power-related issues.  
* [progress](https://github.com/Xfennec/progress) - A tool to monitor the progress of common Coreutils command-line tools (`cp`, `mv`, `dd`, `tar`, `rsync`, etc.); it uses an ncurses interface to display the percentage of data copied; it works by reading from system files and retrieving the necessary information for the estimation.
* [smem](https://www.selenic.com/smem/) - Python program that reports memory usage; it can report the "proportional set size" (PSS), a meaningful representation of the amount of memory used by libraries and applications in a virtual memory system; it has built-in chart generation.
* [sysdig](https://www.sysdig.org/) - Sysdig captures system calls and events from the Linux kernel.  You can save, filter, and analyze the data with our CLI or our desktop app.  Think of sysdig as strace + tcpdump + htop + iftop + lsof + wireshark for your entire system.
* [top](http://www.unixtop.org/) - The classical Unix utility that provides a rolling display of top cpu using processes.  
* [watch](http://www.linfo.org/watch.html) - Periodically runs a command in the console while temporarily clearing the screen content; it makes it easy to check differences between the output of two subsequent commands; it provides "diff" functionality to highlight the changing characters between outputs.
* [whowatch](https://www.tecmint.com/whowatch-monitor-linux-users-and-processes-in-real-time/) - Monitor Linux Users and Processes in Real Time.
* [wtf](https://github.com/wtfutil/wtf) - The personal information dashboard for your terminal.

## <a name="system"></a>System tools

* [conspy](http://conspy.sourceforge.net/) - "Conspy allows a (possibly remote) user to see what is displayed on a Linux virtual console, and send keystrokes to it." 
* [hstr](https://github.com/dvorka/hstr) - A tool for managing the history; powerful visual search and execution of previous commands; history editing capabilities.  
* [lshw](http://www.ezix.org/project/wiki/HardwareLiSter) - A small tool to provide detailed information on the hardware configuration of the machine. It can report exact memory configuration, firmware version, mainboard configuration, CPU version and speed, cache configuration, bus speed, etc.
* [Ntfy](https://github.com/dschep/ntfy) - Ntfy is a simple yet serviceable cross-platform Python utility that enables you to automatically get desktop notifications on demand or when long running commands complete. It can as well send push notifications to your phone once a particular command completes.  
* [parallel](https://www.gnu.org/software/parallel/) - A shell tool from GNU for executing jobs in parallel using one or more computers; it can split the input and pipe it into commands in parallel.  
* [task-spooler](http://vicerveza.homeunix.net/~viric/soft/ts/) - As the name implies, Task spooler is a Unix batch system that can be used to add the Linux commands to the queue and execute them one after the other in numerical order (ascending order, to be precise). This can be very useful when you have to run a lots of commands, but you don't want to waste time waiting for one command to finish and run the next command. You can queue it all up and Task Spooler will execute them one by one. In the mean time, you can do other activities.
* [ttyload](http://www.daveltd.com/src/util/ttyload/) - ttyload is a lightweight utility which is intended to offer a color-coded graph of load averages over time on Linux and other Unix-like systems. It enables a graphical tracking of system load average in a terminal (“tty“).  

## <a name="terminal"></a>Terminals

* [byobu](http://byobu.co/) - A text-based window manager and terminal multiplexer; it features enhanced profiles, convenient keybindings, configuration utilities, and toggle-able system status notifications; compatible with `screen` and `tmux`.
* [dtach](https://github.com/crigler/dtach) - A program written in C that emulates the detach feature of screen.
* [screen](https://www.gnu.org/software/screen/) - Terminal multiplexer that split a physical terminal between several processes, typically interactive shells.
* [Tmate](https://tmate.io/) - A fork of tmux that allows to share the terminal with other users. AFAIK, it connects to a centralized server to establish the connection. Someone may see this inconvenient for privacy issues.
* [tmux](https://tmux.github.io/) - Terminal multiplexer; born to improve `screen`; client-server architecture, `vi` and `emacs` key-bindings, search in window feature and many more.
* [warp](https://github.com/spolu/warp) - Secure and simple terminal sharing.  

## <a name="text-processing"></a>Text processing

* [BaFi](https://mmalcek.github.io/bafi/) - Universal JSON, BSON, YAML, CSV, XML translator to ANY format using templates.
* [ccat](https://github.com/jingweno/ccat) - A `cat` command with colorized output.  
* [delta](https://github.com/dandavison/delta) - A syntax-highlighter for git and diff output.
* [diff-so-fancy](https://github.com/so-fancy/diff-so-fancy) - Make your diffs human readable instead of machine readable.
* [fzf](https://github.com/junegunn/fzf) - (FuZzy Finder) is a general-purpose command-line finder with fuzzy search/filter capabilities; good integration with `vim`.  
* [Graphtage](https://github.com/trailofbits/graphtage) - Graphtage is a commandline utility and underlying library for semantically comparing and merging tree-like structures, such as JSON, XML, HTML, YAML, plist, and CSS files.
* [grc](https://github.com/pengwynn/grc) - (Generic Colouriser) can be configured to parse a given text stream and to colorize it according to regexp written in configuration files; different patterns can be associated to file types.  
* [hck](https://github.com/sstadick/hck) - A sharp cut clone.
* [jq](https://stedolan.github.io/jq/) - (JSON Query?) is sed-like processor for JSON data; can be used to process JSON files and data streams and perform operations such as those allowed by `cat`, `sed`, `grep` and `awk` on regular text files.
* [percol](https://github.com/mooz/percol) - A Python script that "1) receives input lines from `stdin` or a file, 2) lists the input lines and waits for input that filter/select the line(s), 3) outputs the selected line(s) to `stdout`"; can be used to add interactivity to many regular shell commands.
* [pick](https://github.com/calleerlandsson/pick) - Utility that allows users to choose one option from a set of choices using an interface with fuzzy search functionality.  
* [q](http://harelba.github.io/q/) - Executes SQL-like queries on CSVs/TSVs tabular data files; each tabular file is treated as a database table; support to all SQL constructs (`WHERE`, `GROUP BY`, `JOIN`).
* [ydiff](https://github.com/ymattw/ydiff) - View colored, incremental diff.

## <a name="text-search"></a>Text search

* [ack](http://beyondgrep.com/) - A tool like `grep` optimized for programmers; written in Perl, it speeds up searches thanks to skipping non interesting directories, such as `.git`.
* [ag](https://github.com/ggreer/the_silver_searcher) - (The silver searcher) is a text search utility targeted to source code; it skips versioning systems data directories; it is inspired by `ack`, but faster.
* [paragrep](http://software.clapper.org/paragrep/) - Greps regular expressions in a text file(s) and prints out the paragraphs containing those expressions; a paragraph is defined as a block of text delimited by an empty or blank line; fully customizable via command line parameters.  
* [ripgrep](https://github.com/BurntSushi/ripgrep) - Recursively searches directories for a regex pattern.
* [ripgrep-all](https://github.com/phiresky/ripgrep-all) - grep in text files but also search in PDFs, E-Books, office documents, zip, tar.gz, etc.
* [sift](https://sift-tool.org/) - Fast and powerful open source alternative to grep; it targets flexibility and performance: can be as fast as "regular" grep and allows to specify complex expressions to find text.

## <a name="utility"></a>Utilities

* [arch-wiki](https://github.com/deadhead420/arch-wiki) - Search the Arch Wiki anywhere from the command line.  
* [asciinema](https://github.com/asciinema/asciinema) - Terminal session recorder.
* [dasht](http://sunaku.github.io/dasht/man/man0/README.html) - Search API docs offline, in your terminal or browser.
* [dateutils](http://www.fresse.org/dateutils/) - Dateutils are a bunch of tools that revolve around fiddling with dates and times in the command line with a strong focus on use cases that arise when dealing with large amounts of financial data.
* [ddgr](https://github.com/jarun/ddgr) - A command line utility to search DuckDuckGo (html version) from the terminal.
* [eg](https://github.com/srsudar/eg) - Useful examples at the command line.
* [element](https://github.com/gennaro-tedesco/element) - Periodic table on the command line.
* [googler](https://github.com/jarun/googler) - Google Search, Google Site Search, Google News from the terminal.
* [kmdr-cli](https://github.com/ediardo/kmdr-cli#supported-programs) - The CLI tool for explaining commands from your terminal.
* [lolcat](https://github.com/busyloop/lolcat) - Ruby Gem to colorize the output of the cat command.
* [navi](https://github.com/denisidoro/navi) - An interactive cheatsheet tool for the command-line.
* [neofetch](https://github.com/dylanaraps/neofetch) - Neofetch is a CLI system information tool written in BASH. Neofetch displays information about your system next to an image, your OS logo, or any ASCII file of your choice.
* [Nota](https://kary.us/nota/) - Terminal calculator with rich notation.
* [pdd](https://github.com/jarun/pdd) - Tiny date, time diff calculator.
* [pire](https://github.com/johannestaas/pire) - Python Interactive Regular Expressions.
* [pmenu](https://github.com/sgtpep/pmenu) - A dynamic terminal-based menu inspired by dmenu.
* [powerline](https://github.com/powerline/powerline) - Powerline is a statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile.
* [rofi](https://github.com/davatorium/rofi) - A window switcher, application launcher and dmenu replacement.
* [socli](https://github.com/gautamkrishnar/socli) - Stack overflow command line client written in Python.  Search and browse stack overflow without leaving the terminal 
* [Starship](https://starship.rs/) - The cross-shell prompt for astronauts.
* [termsaver](http://termsaver.brunobraga.net/) - termsaver to enjoy fancy ASCII screensavers like matrix, clock, starwars, and a couple of not-safe-for-work screens.

## <a name="versioning"></a>Versioning

* [forgit](https://github.com/wfxr/forgit) - A utility tool powered by fzf for using git interactively.
* [git](https://git-scm.com/) - The winner across all the existing file versioning tools; distributed versioning; fully controllable from the command-line; plenty of configuration and usage options; behind a number of related project that leverage git as backend.  
* [git-annex](https://git-annex.branchable.com/) - Manages files with `git`, without checking the file contents into git; very useful to manage large/binary files.
* [git-peek](https://github.com/Jarred-Sumner/git-peek) - git peek is the fastest way to open a remote git repository in your local text editor.
* [git-stats](https://github.com/IonicaBizau/git-stats) - Local git statistics including GitHub-like contributions calendars.
* [gitui](https://github.com/extrawurst/gitui) - GitUI provides you with the comfort of a git GUI but right in your terminal
* [Mercurial](https://www.mercurial-scm.org/) - Free, distributed source control management tool.
* [onefetch](https://github.com/o2sh/onefetch) - Git repository summary on your terminal.
* [tig](https://github.com/jonas/tig) - An ncurses-based text-mode interface for `git` that can act as a repository browser, but can also assist in staging changes for commit at chunk level.

## <a name="viewers"></a>Viewers

* [cacaview](http://caca.zoy.org/wiki/libcaca) - A library and a program to display JPG, PNG, GIF or BMP images in the terminal using ASCII characters.
* [feh](https://feh.finalrewind.org/) - "X11 image viewer aimed mostly at console users" (cit.); with no fancy GUI, it is controlled via commandline arguments and configurable key/mouse actions.
* [glow](https://github.com/charmbracelet/glow) - Render markdown on the CLI, with pizzazz!
* [jc](https://github.com/kellyjonbrazil/jc) - Serializes the output of command line tools to JSON.
* [jqview](https://github.com/fiatjaf/jqview) - Simplest possible native GUI for inspecting JSON.
* [mdt](https://github.com/robolab-pavia/mdt) - MarkDown in the Terminal. A markdown viewer with themes defined by JSON files and interactive mode to open links and word-wrapping adaptable to the terminal width.
* [mplayer](http://www.mplayerhq.hu/design7/news.html) - One of the most popular video/audio players around; plays most audio and video formats (using ASCII characters) in the shell; provides a GUI for graphical visualization.  
* [mpv](https://mpv.io/) - A cross-platform media player with many features such as frame timing, MKV chapters and subtitles. It is a responsive video player with minimal layout customizable with themes. A good alternative media player to VLC since it can handle almost all the media formats as VLC, but using much less resources.
* [mupdf](http://mupdf.com/) - Lightweight graphical PDF visualizer; strong key-based control; fast and accurate rendering.  
* [Terminal Markdown Viewer](https://github.com/axiros/terminal_markdown_viewer) - Python based Markdown viewer for the terminal.
* [termv](https://github.com/Roshan-R/termv) - A terminal iptv player written in bash.
* [zathura](https://pwmt.org/projects/zathura/) - Plugin based document file visualizer (PDF, DejaVu, PS); strongly key-based control.

## <a name="browser"></a>Web browser

* [cli-arxiv](https://github.com/knguyenanhoa/cli-arxiv) - CLI tool for exploring arXiv.
* [Elinks](http://elinks.cz/) - "Advanced and well-established feature-rich text mode web browser"; started as a fork of `Links`; it supports background download with queueing, some support from CSS, text box editing in external text editor.
* [Graphene](https://github.com/atsepkov/Graphene) - A text-based web browser that's a joy to use.
* [Links](http://www.jikos.cz/~mikulas/links//) - A textual Web browser with tables and frames.  
* [Lynx](http://lynx.invisible-island.net/) - A highly configurable text-based web browser; one of the oldest CLI browser I'm aware of.  
* [w3m](http://w3m.sourceforge.net/) - A text-based web browser as well as a pager like `less`; it can be used as a text formatting tool which typesets HTML into plain text.  

## <a name="webdev"></a>Web development

* [ain](https://github.com/jonaslu/ain) - An HTTP API client for the terminal.
* [Hugo](https://gohugo.io/) - The world’s fastest framework for building websites.
* [Metalsmith](http://www.metalsmith.io/) - An extremely simple static site generator; all functionalities are provided by plugins that can be combined and chained; written and extendable in Javascript.  
* [nanoc](http://nanoc.ws/) - Static site generator written in Ruby; extremely powerful and customizable; support many formats to generate HTML content.  
* [siege](https://www.joedog.org/siege-home/) - An http load testing and benchmarking utility designed to let web developers stress their code.  
* [Tsung](http://tsung.erlang-projects.org/) - A multi-protocol distributed load testing tool that can be used to stress HTTP, WebDAV, SOAP, PostgreSQL, MySQL, LDAP and Jabber/XMPP servers.


# <a name="resources"></a>Related resources

A list of some online resoures that contribute interesting links to apps and info.

[The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) - A wonderful summary from Joshua Levy regarding command line (Bash in particular) tools, programs, tips and tricks; contains many pointers to resources and repositories, in the form of "to do this you must know that", which gives great pointers but requires further investigation from different sources; translated in many languages.

[Inconsolation blog](https://inconsolation.wordpress.com/) - "Adventures with lightweight and minimalist software for Linux": reviews of many command-line programs; many programs reviewed (400+, at least), with screenshots and animated GIFs; the style of presentation is ironic and funny, but requires some effort to figure out the real contribution of a program.

[A little collection of cool unix terminal/console/curses tools](https://kkovacs.eu/cool-but-obscure-unix-tools) - "Some are little-known, some are just too useful to miss, some are pure obscure..." from Kristof Kovacs; nice list with screenshot; mostly oriented to system administration; unfortunately there are no clickable links.

[Caleb Xu shell awesome](https://github.com/alebcay/awesome-shell) - Focused on UNIX shell tools.

[Adam Harris awesome CLI apps](https://github.com/aharris88/awesome-cli-apps) - Nice list of tools; somehow too much Javascript/Node.js-centered for my tastes.

[Marcel Bischoff awesome commandd line apps](https://github.com/herrbischoff/awesome-command-line-apps) - Nice up-to-date list of useful tools.

[Awesome CLI by sintaxi](https://github.com/sintaxi/awesome-cli/blob/master/README.md) - Relatively short list with short descriptions; with some original entries.



