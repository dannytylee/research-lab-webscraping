# research-lab-webscraping
This was a project for the Economics Research Lab I'm a part of. Goal is to scrape data from the U.S. Department of Agriculture collected on the highest level of educational attainment by county and state over time.

Tableau viz link: https://public.tableau.com/app/profile/danny.lee8249/viz/USDAHighestEducationAttainment/Dashboard2?publish=yes

Few notes:
- this was my first experience with web scraping
- data is not stored in the page source - cannot use Beautiful Soup
- I use firefox
- SeleniumWebscraper.py downloads everything into the downloads folder, doesn't separate by highest level of educational attainment
- delete the first 4 files downloaded, those are high-level overviews
- Use SeparateData.py to separate them, but create new folders in your file directory first
- for transform, lots of strange gimmicks on the USDA data
- the '2000' column is strange because it's a merged column
- have to skip the 1st row and last 3 because they aren't relevant
- the final output are tens of thousands of rows long
