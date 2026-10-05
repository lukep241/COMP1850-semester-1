# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

music = {
    "A$AP Rocky" : [("Live.Love.A$AP", 2011), ("Long.Live.A$AP", 2013), ("AT.LONG.LAST.A$AP", 2015), ("Testing", 2018), ("Don't Be Dumb", 2026)],
    "Bruno Mars" : ["Doo-Wops & Hooligans", "Unorthodox Jukebox", "24K Magic", "An Evening With Silk Sonic", "The Romantic"],
    "Kanye West" : ["The College Dropout", "Late Registration", "Graduation", "808s and Heartbreak", "My Beautiful Dark Twisted Fantasy", "The Life of Pablo", "Ye", "Jesus Is King", "Donda", "Vultures", "Vultures 2", "BULLY"]
}


# Pretty-print the data structure
pprint(music)

# Display details of one album recorded by a specific artist
print(music["A$AP Rocky"][0])