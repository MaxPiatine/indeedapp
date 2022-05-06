import job_search
import time

US = ["Seattle", "Sacramento", "San Francisco", "San Jose", "Los Angeles", "San Diego", "Las Vegas", "Phoenix Arizona",
"Dallas Texas", "San Antonio", "Denver", "Austin Texas", "Houston", "Oklahoma City", "New Orleans", "Atlanta", "Tampa Florida",
"Miami", "Washington DC", "Philadelphia", "New York, NY", "Boston", "Buffalo", "Cleveland", "Chicago", "Milwaukee","Pittsburgh"]
CAD = ["Vancouver", "Calgary", "Edmonton", "Toronto", "Ottawa", "Montreal"]
AUS = ["Sydney", "Melbourne"]

website = job_search.Indeed("Physics", "Toronto")
website.search()
website.signin()
time.sleep(1)
website.interest()
time.sleep(1)
website.apply()
website.apply2()
website.information()
