# Clippy
A shell error handler based on Microsoft's Clippy. 
Inspired by [this](https://www.reddit.com/r/linux/comments/s2e4h/ive_created_an_abomination/) thread, with help from /u/reverend.

## How to Install
### zsh
Put clippyscript.py in /usr/local/bin, then place clippy.cow in your cows directory. This is probably located in /usr/share. Add the following line to your .zshrc: 

```bash
function command_not_found_handler() { /path/to/clippyscript.py $1 | lolcat; } 
#the lolcat is optional; it makes the output rainbow.
```
