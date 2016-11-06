from menu import *

# Menu for top level pages on my website
TOP_LEVEL_MENU = Menu(
    # Specify root-relative URLs (so they always work regardless of what directory we are in)
    menu = [
        ("About", {"url":"/#about"}),
        #("Blog", {"url":"blog"}),
        ("Projects", {"url":"/projects"}),
        ("Resume", {"url":"/resume"})
        ])
