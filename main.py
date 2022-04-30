import job_search
import word

url = 'https://ca.indeed.com/?from=gnav-resume--myind'
email = "maximpiatine@hotmail.com"

job_search.Search(url, "Statistics", "Toronto", email, 50000).search()

