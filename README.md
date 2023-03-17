# Party_recommender
Spiced final project Party finder/ recommender app

In this project I built a club recommender for party people in Berlin.

I am currently working on this project with hopes to launch it in 2023 so all of the updated code and programming is not in this repo.

This project works with a data scraping libary called [pyppeteer](https://miyakogi.github.io/pyppeteer/reference.html).

Firstly I scrape the [Resident Advisor](www.ra.co/events/de/berlin) website to collect the club events for the coming days.
Scraped data includes: Event name, Club name, artists (Djs) at th event.
This can be found in the events.ipynb file
This data is then stored in a pandas dataframe. After this I use the spoitpy API to search for the artists each event and from the JSON file returned I extract the genres associated with the artists and then add them to column in the DF in row of the event name.

Next I use get_dummies to build a new DF with binary format ( required for the regression model) with the genre names as column names and 1 or 0 in the columns where the genre is found and the club/event name as the index.

Then I train a RandomForestClassifier model on this dataFrame to use as the model.

The next step is in the get_track.ipynb notebook.

In this notebook I call the users recently played songs from the spoitipy API. The concept behind this is so that if a user is having a party at their house or listening to a specific type of music and wishes to find somewhere to go out and continue listening to that style of music they can.

The api returns the 20 recently played tracks in JSON format, from this I extract the artist name and artist id and then do another API call on the artist ID. This returns the info I need which is the genres associated with the artist.

This is then added to a list, save it in pickle format and I call it back into the events notebook where I convert it to a data frame and then use the predict fuction in the model to return which club is the best fit for those genres.

The ongoing project is slightly more complicated. It ustilises a PostgreSQL database to store all the data collected form the scraping activities. I also incorporate pyppeteer steath and use a headless browser to avoid detection. I also scrape multiple website which do not have APIs to collect more data on events and artists and their genres.
The user data api call is made through svelte-kit which operates the website and provides a GUI for the user to login to their own Spotify account, select their top artists or top/recently played songs. To much more details and I give away everything so I'll leave it here. Please feel free to contact
