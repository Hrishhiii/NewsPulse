# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

# # Function to extract text from an element
# def extract_text(driver, selector, default="Not available"):
#     try:
#         return driver.find_element(By.CSS_SELECTOR, selector).text.strip()
#     except:
#         return default

# # Function to extract an attribute (e.g., image URL, timestamp)
# def extract_attribute(driver, selector, attribute, default="Not available"):
#     try:
#         return driver.find_element(By.CSS_SELECTOR, selector).get_attribute(attribute)
#     except:
#         return default

# # Function to extract multiple paragraphs for article content
# def extract_multiple_text(driver, selector):
#     try:
#         elements = driver.find_elements(By.CSS_SELECTOR, selector)
#         return "\n".join([el.text.strip() for el in elements if el.text.strip()])
#     except:
#         return "No content available"

# # Set up Selenium WebDriver
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# # Category page (BBC News main page)
# category = "news"  # Change this to any other category if needed
# category_url = f"https://www.bbc.com/{category}"
# driver.get(category_url)

# print(f"🔍 Scraper started for {category}...")

# # Wait for the page to load and find all article links
# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="internal-link"]')))
# articles = driver.find_elements(By.CSS_SELECTOR, '[data-testid="internal-link"]')

# article_links = set()  # Use a set to avoid duplicates
# for article in articles:
#     link = article.get_attribute("href")
#     if link and "news/" in link:  # Filter only news articles
#         full_link = link if link.startswith("http") else "https://www.bbc.com" + link
#         article_links.add(full_link)

# # Print total articles found
# total_articles = len(article_links)
# print(f"Total articles found: {total_articles}")

# scraped_data = []  # Store extracted article data

# # Iterate through each article link
# for index, article_url in enumerate(article_links, start=1):
#     try:
#         print(f"Scraping Article {index} of {total_articles}: {article_url}")
#         driver.get(article_url)
        
#         # Wait for the article to load
#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))

#         # Extract article details
#         article_data = {
#             "title": extract_text(driver, "h1", "No title"),
#             "description": extract_text(driver, "p", "No description available"),
#             "author": extract_text(driver, ".sc-b42e7a8f-7.khDNZq", "Unknown Author"),
#             "timestamp": extract_attribute(driver, "time.sc-b42e7a8f-2.bGezbH", "datetime", "No timestamp"),
#             "imageUrl": extract_attribute(driver, "article img", "src", "No image available"),
#             "content": extract_multiple_text(driver, "article p"),
#             "source": article_url
#         }

#         # Append data to list
#         scraped_data.append(article_data)

#     except Exception as e:
#         print(f"❌ Error scraping {article_url}: {e}")

# # Save scraped data to a JSON file
# with open("bbc_articles.json", "w", encoding="utf-8") as json_file:
#     json.dump(scraped_data, json_file, ensure_ascii=False, indent=4)

# # Close the browser
# driver.quit()

# print(f"✅ Scraping completed. {total_articles} articles saved to bbc_articles.json")


# #2nd Working Code
# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from pymongo import MongoClient

# # MongoDB connection setup
# client = MongoClient("mongodb://localhost:27017/")  # Change URL if needed
# db = client["bbc_news"]
# collection = db["articles"]

# # Function to extract text from an element
# def extract_text(driver, selector, default="Not available"):
#     try:
#         return driver.find_element(By.CSS_SELECTOR, selector).text.strip()
#     except:
#         return default

# # Function to extract an attribute (e.g., image URL, timestamp)
# def extract_attribute(driver, selector, attribute, default="Not available"):
#     try:
#         return driver.find_element(By.CSS_SELECTOR, selector).get_attribute(attribute)
#     except:
#         return default

# # Function to extract multiple paragraphs for article content
# def extract_multiple_text(driver, selector):
#     try:
#         elements = driver.find_elements(By.CSS_SELECTOR, selector)
#         return "\n".join([el.text.strip() for el in elements if el.text.strip()])
#     except:
#         return "No content available"

# # Set up Selenium WebDriver
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# # Category page (BBC News main page)
# category = "news"  # Change this to any other category if needed
# category_url = f"https://www.bbc.com/{category}"
# driver.get(category_url)

# print(f"🔍 Scraper started for {category}...")

# # Wait for the page to load and find all article links
# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="internal-link"]')))
# articles = driver.find_elements(By.CSS_SELECTOR, '[data-testid="internal-link"]')

# article_links = set()  # Use a set to avoid duplicates
# for article in articles:
#     link = article.get_attribute("href")
#     if link and "news/" in link:  # Filter only news articles
#         full_link = link if link.startswith("http") else "https://www.bbc.com" + link
#         article_links.add(full_link)

# # Print total articles found
# total_articles = len(article_links)
# print(f"Total articles found: {total_articles}")

# # Iterate through each article link
# for index, article_url in enumerate(article_links, start=1):
#     try:
#         print(f"Scraping Article {index} of {total_articles}: {article_url}")
#         driver.get(article_url)

#         # Wait for the article to load
#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))

#         # Extract article details
#         article_data = {
#             "title": extract_text(driver, "h1", "No title"),
#             "description": extract_text(driver, "p", "No description available"),
#             "author": extract_text(driver, ".sc-b42e7a8f-7.khDNZq", "Unknown Author"),
#             "timestamp": extract_attribute(driver, "time.sc-b42e7a8f-2.bGezbH", "datetime", "No timestamp"),
#             "imageUrl": extract_attribute(driver, "article img", "src", "No image available"),
#             "content": extract_multiple_text(driver, "article p"),
#             "source": article_url
#         }

#         # Insert into MongoDB
#         collection.insert_one(article_data)

#     except Exception as e:
#         print(f"❌ Error scraping {article_url}: {e}")

# # Close the browser
# driver.quit()

# print(f"✅ Scraping completed. Data stored in MongoDB.")



#3rd Working Code(Array of Articles)
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")  # Change URL if needed
db = client["news_scraper"]
collection = db["articles"]

# Websites and categories to scrape
websites = [
    {"url": "https://www.bbc.com/news", "category": "News"},
    {"url": "https://www.bbc.com/innovation", "category": "Innovation"},
    {"url": "https://www.bbc.com/business", "category": "Business"},
    {"url": "https://www.bbc.com/culture", "category": "Culture"},
    {"url": "https://www.bbc.com/arts", "category": "Arts"},
]

# Function to extract text from an element
def extract_text(driver, selector, default="Not available"):
    try:
        return driver.find_element(By.CSS_SELECTOR, selector).text.strip()
    except:
        return default

# Function to extract an attribute (e.g., image URL, timestamp)
def extract_attribute(driver, selector, attributes, default="Not available"):
    try:
        element = driver.find_element(By.CSS_SELECTOR, selector)
        for attribute in attributes:
            value = element.get_attribute(attribute)
            if value:
                return value  # Return the first valid attribute found
        return default
    except:
        return default

# Function to extract multiple paragraphs for article content
def extract_multiple_text(driver, selector):
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, selector)
        return "\n".join([el.text.strip() for el in elements if el.text.strip()])
    except:
        return "No content available"

# Set up Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

for site in websites:
    category_url = site["url"]
    category_label = site["category"]

    driver.get(category_url)
    print(f"🔍 Scraper started for {category_label}...")

    # Wait for the page to load and find all article links
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="internal-link"]')))
    articles = driver.find_elements(By.CSS_SELECTOR, '[data-testid="internal-link"]')

    article_links = set()  # Use a set to avoid duplicates
    for article in articles:
        link = article.get_attribute("href")
        if link and "/news/" in link:  # Filter only news articles
            full_link = link if link.startswith("http") else "https://www.bbc.com" + link
            article_links.add(full_link)

    print(f"Total articles found in {category_label}: {len(article_links)}")

    # Iterate through each article link
    for index, article_url in enumerate(article_links, start=1):
        try:
            print(f"Scraping Article {index}: {article_url}")
            driver.get(article_url)

            # Wait for the article to load
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))

            # Extract article details
            article_data = {
                "title": extract_text(driver, "h1", "No title"),
                "description": extract_text(driver, "p", "No description available"),
                "author": extract_text(driver, ".sc-b42e7a8f-7.khDNZq", "Unknown Author"),
                "timestamp": extract_attribute(driver, "time.sc-b42e7a8f-2.bGezbH", "datetime", "No timestamp"),
                "imageUrl": extract_attribute(driver, "article img", ["src", "srcset"], "No image available"),
                "content": extract_multiple_text(driver, "article p"),
                "source": article_url,
                "category": category_label  
            }

            # Insert into MongoDB
            collection.insert_one(article_data)

        except Exception as e:
            print(f"❌ Error scraping {article_url}: {e}")

# Close the browser
driver.quit()
print("✅ Scraping completed. Data stored in MongoDB.")

