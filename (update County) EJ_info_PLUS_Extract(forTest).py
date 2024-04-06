#list of cities in Tennessee
tennesse_cities = ["Adams", "Adamsville", "Alamo", "Alcoa", "Alexandria", "Allardt", "Altamont", "Ardmore", "Arlington", "Ashland City", "Athens", "Atoka", "Atwood", "Auburntown", "Baxter", "Beersheba Springs", "Bell Buckle", "Bells", "Benton", "Bethel Springs", "Big Sandy", "Blaine", "Blountville", "Bluff City", "Bolivar", "Braden", "Bradford", "Brentwood", "Brighton", "Bristol", "Brownsville", "Bruceton", "Bulls Gap", "Burlison", "Burns", "Byrdstown", "Calhoun", "Camden", "Carthage", "Caryville", "Cedar Hill", "Celina", "Centerville", "Chapel Hill", "Charleston", "Charlotte", "Chattanooga", "Church Hill", "Clarksburg", "Clarksville", "Cleveland", "Clifton", "Clinton", "Coalmont", "Collegedale", "Collierville", "Collinwood", "Columbia", "Cookeville", "Copperhill", "Cornersville", "Covington", "Cowan", "Crab Orchard", "Cross Plains", "Crossville", "Crump", "Cumberland City", "Cumberland Gap", "Dandridge", "Dayton", "Decatur", "Decaturville", "Decherd", "Dickson", "Dover", "Dowelltown", "Doyle", "Dresden", "Ducktown", "Dunlap", "Dyer", "Dyersburg", "Eagleville", "Elizabethton", "Elkton", "Englewood", "Enville", "Erin", "Erwin", "Estill Springs", "Ethridge", "Etowah", "Fairview", "Fall Branch", "Fayetteville", "Finger", "Franklin", "Friendship", "Friendsville", "Gadsden", "Gainesboro", "Gallatin", "Gallaway", "Gates", "Gatlinburg", "Germantown", "Gibson", "Gleason", "Goodlettsville", "Goodlettsville Demographi", "Gordonsville", "Grand Junction", "Graysville", "Greenback", "Greenbrier", "Greeneville", "Greenfield", "Gruetli Laager", "Guys", "Halls", "Harriman", "Harrison", "Harrogate", "Hartsville", "Helenwood", "Henderson", "Hendersonville", "Henning", "Henry", "Hohenwald", "Hollow Rock", "Hornbeak", "Hornsby", "Humboldt", "Huntingdon", "Huntland", "Huntsville", "Iron City", "Jacksboro", "Jackson", "Jamestown", "Jasper", "Jefferson City", "Jellico", "Johnson City", "Jonesborough", "Kenton", "Kingsport", "Kingston Springs", "Kingston", "La Follette", "La Vergne", "Lafayette", "Lake City", "Lawrenceburg", "Lebanon", "Lenoir City", "Lewisburg", "Lexington", "Liberty", "Linden", "Livingston", "Lobelville", "Lookout Mountain", "Loretto", "Loudon", "Louisville", "Luttrell", "Lynchburg", "Lynnville", "Madisonville", "Manchester", "Martin", "Maryville", "Mascot", "Mason", "Maury City", "Maynardville", "Mc Ewen", "Mc Kenzie", "Mc Lemoresville", "Mc Minnville", "Medina", "Memphis", "Michie", "Middleton", "Midway", "Milan", "Milledgeville", "Millington", "Minor Hill", "Mitchellville", "Monteagle", "Monterey", "Morrison", "Morristown", "Moscow", "Mosheim", "Mount Carmel", "Mount Juliet", "Mount Pleasant", "Mountain City", "Munford", "Murfreesboro", "Nashville", "New Johnsonville", "New Market", "New Tazewell", "Newbern", "Newport", "Niota", "Nolensville", "Norris", "Oakdale", "Oakland", "Obion", "Oliver Springs", "Oneida", "Ooltewah", "Orlinda", "Palmer", "Paris", "Parrottsville", "Parsons", "Pegram", "Petersburg", "Philadelphia", "Pigeon Forge", "Pikeville", "Pleasant Hill", "Pleasant View", "Portland", "Pulaski", "Puryear", "Ramer", "Red Boiling Springs", "Ridgely", "Ridgetop", "Ripley", "Rives", "Roan Mountain", "Rockford", "Rockwood", "Rogersville", "Rossville", "Rutherford", "Rutledge", "Saint Joseph", "Saltillo", "Samburg", "Sardis", "Savannah", "Scotts Hill", "Selmer", "Sevierville", "Sewanee", "Seymour", "Sharon", "Shelbyville", "Signal Mountain", "Smithville", "Smyrna", "Sneedville", "Soddy Daisy", "Somerville", "South Fulton", "South Pittsburg", "Sparta", "Spencer", "Spring City", "Spring Hill", "Springfield", "Stanton", "Stantonville", "Sunbright", "Surgoinsville", "Sweetwater", "Tazewell", "Tellico Plains", "Tennessee Ridge", "Tiptonville", "Toone", "Townsend", "Tracy City", "Trenton", "Trezevant", "Trimble", "Troy", "Tullahoma", "Unicoi", "Union City", "Vanleer", "Vonore", "Wartburg", "Wartrace", "Watauga", "Watertown", "Waverly", "Waynesboro", "Westmoreland", "White Bluff", "White House", "White Pine", "Whiteville", "Whitwell", "Williston", "Winchester", "Winfield", "Woodbury", "Woodland Mills", "Yorkville"]

#list of terms
terms = ["water", "air", "noise", "waste", "soil"]

#list of keywords
keywords = ["pollution event", "environmental protection", "pollution accident", "health perception", "public health", "pollution event investigation", "water pollution", "water quality", "heavy metals", "industrial discharge", "drinking water", "harmful algal blooms", "air pollution", "air quality", "air gas", "air pollution breath", "pm2.5", "pm10", "sulfur dioxide", "nitrogen dioxide", "ozone", "carbon monoxide", "noise pollution", "environmental noise", "noise levels", "noise measurement", "health effects of noise", "noise-induced hearing", "quiet zones", "noise abatement ", "waste pollution", "waste management", "solid waste", "municipal waste", "industrial waste", "hazardous waste"]


#Gets and returns the content from URL if it's valid, otherwise will retun None
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def extract_text_from_url(url):
    # Fetch the HTML content of the webpage
    response = requests.get(url,timeout=10)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from the parsed HTML
        text = soup.get_text()

        return text
    else:
        print("Failed to retrieve content from the URL:", response.status_code)
        return None

def find_date(text):
    # Define a list of regular expression patterns to match various date formats
    date_patterns = [
        r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b',  # MM/DD/YYYY or MM/DD/YY
        r'\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b',     # MM-DD-YYYY or MM-DD-YY
        r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2}\b',      # MM-DD-YY
        r'\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b',     # YYYY-MM-DD
        r'\b(?:january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2},\s+\d{4}\b'
    ]

    # Find all occurrences of the date patterns in the text
    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))

    return " ".join(dates)

#import the CSV file where the titles and links are saved
df = pd.read_csv("2-PM10.csv", header = None, names = ["title", "link"])

#looking for city names inside the URL
cities_names_from_URL = [] 
terms_from_URL = [] 
keywords_from_URL = [] 
dates_from_URL = [] 
links = df["link"] 
i = 1 
for link in links:    
  print("link", i, link) 
  i += 1 
  try: 
    link_text = extract_text_from_url(link) 
  except: #in case the link fails
    print("fail") 
    cities_names_from_URL.append("") 
    terms_from_URL.append("") 
    keywords_from_URL.append("") 
    dates_from_URL.append("") 
    continue 
  cities_to_add = "" 
  for city in tennesse_cities: 
    for sub_city in city.split(): 
      if link_text is not None and sub_city.lower() in link_text.lower() and sub_city.lower() not in cities_to_add: 
        if cities_to_add != "":
            cities_to_add += ", " + city.lower()
        else:
            cities_to_add += city.lower()
  cities_names_from_URL.append(cities_to_add) 
  

  #look for terms in the article
  terms_to_add = ""
  for term in terms:
    if link_text is not None and term in link_text.lower() and term not in terms_to_add:
      if terms_to_add != "":
          terms_to_add += ", " + term
      else:
          terms_to_add += term
  terms_from_URL.append(terms_to_add)

  
  #look for keywords in the article
  keywords_to_add = ""
  for keyword in keywords:
    if link_text is not None and keyword in link_text.lower() and keyword not in keywords_to_add:
      if keywords_to_add != "":
          keywords_to_add += ", " + keyword
      else:
          keywords_to_add += keyword
  keywords_from_URL.append(keywords_to_add)
  
  if link_text is not None:
    dates_from_URL.append(find_date(link_text.lower()))
  else:
    dates_from_URL.append("")

# Define a dictionary mapping each city to its county
city_to_county = {
       city.lower(): county for city, county in {
    "Clinton": "Anderson County",
    "Norris": "Anderson County",
    "Oak Ridge": "Anderson County",
    "Oliver Springs": "Anderson County",
    "Rocky Top": "Anderson County",
    "Bell Buckle": "Bedford County",
    "Normandy": "Bedford County",
    "Shelbyville": "Bedford County",
    "Wartrace": "Bedford County",
    "Big Sandy": "Benton County",
    "Camden": "Benton County",
    "Pikeville": "Bledsoe County",
    "Alcoa": "Blount County",
    "Friendsville": "Blount County",
    "Louisville": "Blount County",
    "Maryville": "Blount County",
    "Rockford": "Blount County",
    "Townsend": "Blount County",
    "Charleston": "Bradley County",
    "Cleveland": "Bradley County",
    "Caryville": "Campbell County",
    "Jacksboro": "Campbell County",
    "Jellico": "Campbell County",
    "LaFollette": "Campbell County",
    "Auburntown": "Cannon County",
    "Woodbury": "Cannon County",
    "Atwood": "Carroll County",
    "Bruceton": "Carroll County",
    "Clarksburg": "Carroll County",
    "Hollow Rock": "Carroll County",
    "Huntingdon": "Carroll County",
    "McKenzie": "Carroll County",
    "McLemoresville": "Carroll County",
    "Trezevant": "Carroll County",
    "Elizabethton": "Carter County",
    "Johnson City": "Carter County",
    "Watauga": "Carter County",
    "Ashland City": "Cheatham County",
    "Kingston Springs": "Cheatham County",
    "Pegram": "Cheatham County",
    "Pleasant View": "Cheatham County",
    "Enville": "Chester County",
    "Henderson": "Chester County",
    "Milledgeville": "Chester County",
    "Silerton": "Chester County",
    "Cumberland Gap": "Claiborne County",
    "Harrogate": "Claiborne County",
    "New Tazewell": "Claiborne County",
    "Tazewell": "Claiborne County",
    "Celina": "Clay County",
    "Newport": "Cocke County",
    "Parrottsville": "Cocke County",
    "Manchester": "Coffee County",
    "Tullahoma": "Coffee County",
    "Alamo": "Crockett County",
    "Bells": "Crockett County",
    "Friendship": "Crockett County",
    "Gadsden": "Crockett County",
    "Maury City": "Crockett County",
    "Crab Orchard": "Cumberland County",
    "Crossville": "Cumberland County",
    "Pleasant Hill": "Cumberland County",
    "Belle Meade": "Davidson County",
    "Berry Hill": "Davidson County",
    "Forest Hills": "Davidson County",
    "Goodlettsville": "Davidson County",
    "Nashville": "Davidson County",
    "Oak Hill": "Davidson County",
    "Ridgetop": "Davidson County",
    "Bean Station": "Grainger County",
    "Blaine": "Grainger County",
    "Rutledge": "Grainger County",
    "Greeneville": "Greene County",
    "Mosheim": "Greene County",
    "Tusculum": "Greene County",
    "Altamont": "Grundy County",
    "Beersheba Springs": "Grundy County",
    "Coalmont": "Grundy County",
    "Gruetli-Laager": "Grundy County",
    "Monteagle": "Grundy County",
    "Palmer": "Grundy County",
    "Tracy City": "Grundy County",
    "Morristown": "Hamblen County",
    "Chattanooga": "Hamilton County",
    "Collegedale": "Hamilton County",
    "East Ridge": "Hamilton County",
    "Lakesite": "Hamilton County",
    "Lookout Mountain": "Hamilton County",
    "Red Bank": "Hamilton County",
    "Ridgeside": "Hamilton County",
    "Signal Mountain": "Hamilton County",
    "Soddy-Daisy": "Hamilton County",
    "Walden": "Hamilton County",
    "Sneedville": "Hancock County",
    "Bolivar": "Hardeman County",
    "Grand Junction": "Hardeman County",
    "Hickory Valley": "Hardeman County",
    "Hornsby": "Hardeman County",
    "Middleton": "Hardeman County",
    "Saulsbury": "Hardeman County",
    "Silerton": "Hardeman County",
    "Toone": "Hardeman County",
    "Whiteville": "Hardeman County",
    "Adamsville": "Hardin County",
    "Crump": "Hardin County",
    "Milledgeville": "Hardin County",
    "Saltillo": "Hardin County",
    "Savannah": "Hardin County",
    "Bulls Gap": "Hawkins County",
    "Church Hill": "Hawkins County",
    "Kingsport": "Hawkins County",
    "Mount Carmel": "Hawkins County",
    "Rogersville": "Hawkins County",
    "Surgoinsville": "Hawkins County",
    "Brownsville": "Haywood County",
    "Stanton": "Haywood County",
    "Lexington": "Henderson County",
    "Parker's Crossroads": "Henderson County",
    "Sardis": "Henderson County",
    "Scotts Hill": "Henderson County",
    "Cottage Grove": "Henry County",
    "Henry": "Henry County",
    "McKenzie": "Henry County",
    "Paris": "Henry County",
    "Puryear": "Henry County",
    "Centerville": "Hickman County",
    "Erin": "Houston County",
    "Tennessee Ridge": "Houston County",
    "McEwen": "Humphreys County",
    "New Johnsonville": "Humphreys County",
    "Waverly": "Humphreys County",
    "Gainesboro": "Jackson County",
    "Baneberry": "Jefferson County",
    "Dandridge": "Jefferson County",
    "Jefferson City": "Jefferson County",
    "New Market": "Jefferson County",
    "White Pine": "Jefferson County",
    "Mountain City": "Johnson County",
    "Farragut": "Knox County",
    "Knoxville": "Knox County",
    "Ridgely": "Lake County",
    "Tiptonville": "Lake County",
    "Gates": "Lauderdale County",
    "Halls": "Lauderdale County",
    "Henning": "Lauderdale County",
    "Ripley": "Lauderdale County",
    "Ethridge": "Lawrence County",
    "Lawrenceburg": "Lawrence County",
    "Loretto": "Lawrence County",
    "St. Joseph": "Lawrence County",
    "Hohenwald": "Lewis County",
    "Fayetteville": "Lincoln County",
    "Petersburg": "Lincoln County",
    "Greenback": "Loudon County",
    "Lenoir City": "Loudon County",
    "Loudon": "Loudon County",
    "Philadelphia": "Loudon County",
    "Lafayette": "Macon County",
    "Red Boiling Springs": "Macon County",
    "Jackson": "Madison County",
    "Medon": "Madison County",
    "Three Way": "Madison County",
    "Jasper": "Marion County",
    "Kimball": "Marion County",
    "Monteagle": "Marion County",
    "New Hope": "Marion County",
    "Orme": "Marion County",
    "Powell's Crossroads": "Marion County",
    "South Pittsburg": "Marion County",
    "Whitwell": "Marion County",
    "Chapel Hill": "Marshall County",
    "Cornersville": "Marshall County",
    "Lewisburg": "Marshall County",
    "Petersburg": "Marshall County",
    "Columbia": "Maury County",
    "Mount Pleasant": "Maury County",
    "Spring Hill": "Maury County",
    "Athens": "McMinn County",
    "Calhoun": "McMinn County",
    "Englewood": "McMinn County",
    "Etowah": "McMinn County",
    "Niota": "McMinn County",
    "Sweetwater": "McMinn County",
    "Adamsville": "McNairy County",
    "Bethel Springs": "McNairy County",
    "Eastview": "McNairy County",
    "Enville": "McNairy County",
    "Finger": "McNairy County",
    "Guys": "McNairy County",
    "Michie": "McNairy County",
    "Milledgeville": "McNairy County",
    "Ramer": "McNairy County",
    "Selmer": "McNairy County",
    "Stantonville": "McNairy County",
    "Decatur": "Meigs County",
    "Madisonville": "Monroe County",
    "Sweetwater": "Monroe County",
    "Tellico Plains": "Monroe County",
    "Vonore": "Monroe County",
    "Clarksville": "Montgomery County",
    "Lynchburg": "Moore County",
    "Oakdale": "Morgan County",
    "Oliver Springs": "Morgan County",
    "Sunbright": "Morgan County",
    "Wartburg": "Morgan County",
    "Hornbeak": "Obion County",
    "Kenton": "Obion County",
    "Obion": "Obion County",
    "Rives": "Obion County",
    "Samburg": "Obion County",
    "South Fulton": "Obion County",
    "Trimble": "Obion County",
    "Troy": "Obion County",
    "Union City": "Obion County",
    "Woodland Mills": "Obion County",
    "Livingston": "Overton County",
    "Linden": "Perry County",
    "Lobelville": "Perry County",
    "Byrdstown": "Pickett County",
    "Benton": "Polk County",
    "Copperhill": "Polk County",
    "Ducktown": "Polk County",
    "Algood": "Putnam County",
    "Baxter": "Putnam County",
    "Cookeville": "Putnam County",
    "Monterey": "Putnam County",
    "Dayton": "Rhea County",
    "Graysville": "Rhea County",
    "Spring City": "Rhea County",
    "Harriman": "Roane County",
    "Kingston": "Roane County",
    "Oak Ridge": "Roane County",
    "Oliver Springs": "Roane County",
    "Rockwood": "Roane County",
    "Adams": "Robertson County",
    "Cedar Hill": "Robertson County",
    "Coopertown": "Robertson County",
    "Cross Plains": "Robertson County",
    "Greenbrier": "Robertson County",
    "Millersville": "Robertson County",
    "Orlinda": "Robertson County",
    "Ridgetop": "Robertson County",
    "Springfield": "Robertson County",
    "White House": "Robertson County",
    "Eagleville": "Rutherford County",
    "La Vergne": "Rutherford County",
    "Murfreesboro": "Rutherford County",
    "Smyrna": "Rutherford County",
    "Huntsville": "Scott County",
    "Oneida": "Scott County",
    "Winfield": "Scott County",
    "Dunlap": "Sequatchie County",
    "Gatlinburg": "Sevier County",
    "Pigeon Forge": "Sevier County",
    "Pittman Center": "Sevier County",
    "Sevierville": "Sevier County",
    "Arlington": "Shelby County",
    "Bartlett": "Shelby County",
    "Collierville": "Shelby County",
    "Germantown": "Shelby County",
    "Lakeland": "Shelby County",
    "Memphis": "Shelby County",
    "Millington": "Shelby County",
    "Erwin": "Unicoi County",
    "Unicoi": "Unicoi County",
    "Luttrell": "Union County",
    "Maynardville": "Union County",
    "Plainview": "Union County",
    "Spencer": "Van Buren County",
    "Centertown": "Warren County",
    "McMinnville": "Warren County",
    "Morrison": "Warren County",
    "Viola": "Warren County",
    "Johnson City": "Washington County",
    "Jonesborough": "Washington County",
    "Clifton": "Wayne County",
    "Collinwood": "Wayne County",
    "Waynesboro": "Wayne County",
    "Dresden": "Weakley County",
    "Gleason": "Weakley County",
    "Greenfield": "Weakley County",
    "Martin": "Weakley County",
    "McKenzie": "Weak"}.items()
}

# map cities to counties
def map_city_to_county(city_names):
    counties = []
    for city in city_names.split(","):
        county = city_to_county.get(city.strip(), "")
        if county:
            counties.append(county)
    return ", ".join(counties)
  
#add the collected information to the dataframe (data table)
df["terms"] = terms_from_URL
df["keywords"] = keywords_from_URL
df["cities from URL"] = cities_names_from_URL
df["dates from URL"] = dates_from_URL

# Add a new column for county name and map city names to counties
def map_city_to_county(city):
    return city_to_county.get(city.strip(), "Unknown")

df["county"] = df["cities from URL"].apply(lambda x: ", ".join([map_city_to_county(city.strip()) for city in x.split(",") if city.strip() != ""]))

#save the results in a CSV file
df.to_csv("out.csv")
