import webbrowser

favSites = {"google": "www.google.com",
            "facebook": "www.facebook.com", "linkedin": "www.linkedin.com"}


def openInNewTap(link):
    webbrowser.open_new_tab(link)
