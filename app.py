import pandas as pd
import requests
from bs4 import BeautifulSoup

# Read txt file and add to array
citiesUrls = []
with open('bookingcom.txt') as webSet:
    for url in webSet:
        citiesUrls.append(url.replace('\n', ''))


scrapedAccommodations = []

# Start web scraping
for url in citiesUrls:
    # Check if page gives a response back
    getPage = requests.get(url)
    statusCode = getPage.status_code

    if(statusCode == 200):
        soup = BeautifulSoup(getPage.text, 'html.parser')

        for item in soup.findAll('div', class_="sr__card"):
            hotelName = item.find('span', class_="bui-card__title").text
            totalReviewsText = item.find('div', class_="bui-review-score__text").text

            totalReviews = totalReviewsText.split(' ', 1)[0]
            totalReviews = totalReviews.replace(',', '')

            scrapedAccommodations.append([hotelName, int(totalReviews)])

        print("Total Accommodations Scraped: ", len(scrapedAccommodations))
    else:
        print("Page doesn't respond")

accommodationsDF = pd.DataFrame(scrapedAccommodations, columns=['hotel_name', 'total_reviews'])
print(accommodationsDF)

# Example links
# https://www.booking.com/city/au/sydney.html?label=gen173nr-1FCAEoggI46AdIM1gEaKkBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKS5rj0BcACAQ;sid=039f0596b9e50f9a848985bd1f37b65c;srpvid=1b4c52acac3b0105&
# https://www.booking.com/city/gb/london.html?label=gen173nr-1FCAEoggI46AdIM1gEaKkBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKS5rj0BcACAQ;sid=039f0596b9e50f9a848985bd1f37b65c;breadcrumb=searchresults_irene;srpvid=1b4c52acac3b0105&
# https://www.booking.com/city/nl/amsterdam.html?label=gen173nr-1FCAEoggI46AdIM1gEaKkBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKS5rj0BcACAQ;sid=039f0596b9e50f9a848985bd1f37b65c;srpvid=1b4c52acac3b0105&
# https://www.booking.com/city/ae/dubai.html?label=gen173nr-1FCAEoggI46AdIM1gEaKkBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKS5rj0BcACAQ;sid=039f0596b9e50f9a848985bd1f37b65c;srpvid=1b4c52acac3b0105&
