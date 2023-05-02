# John Yehia Rutgers University
# we have to import urllib
# we have to use urllub.request, to get the data of the URL
# We then have to write a function that takes a URL then returns a response
#200 means it was able to access that URL
import urllib.request as urllib


def main(url):
    print("Checking connectivity.")
    # store in a response
    response = urllib.urlopen(url)
    print("Connected to ", url, "successfully")
    print("The response code was: ", response.getcode())


print("Site connectivity checker.")
# collects the url
input_url = input(
    "Input the URL of the site you'd like to check. Copy from the address bar please. ")

main(input_url)
