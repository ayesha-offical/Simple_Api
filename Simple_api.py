from fastapi import FastAPI
import random

app = FastAPI() # is mien sare fastapi k method is app variable  mien store ho jaen is lye is FastAPI ko use kia hai 

# we build two simple get end FloatingPointError
# 1: side_hustles
# 2: money_quotes

side_hustles =[
"Freelancing - Offer development services on Upwork or Fiverr!",  
"Subscription Service - Create tools and charge monthly fees!",  
"Stock Market Data - Provide real-time stock price updates!",  
"Crypto Data - Build a platform for live crypto market info!",  
"Social Media Automation - Automate LinkedIn, Twitter, or Instagram!",  
"E-commerce Tools - Develop solutions for product listing and inventory!",  
"AI Services - Sell tools for text generation, image recognition!",  
"Resume Tools - Extract details from resumes for HR platforms!",  
"Weather Updates - Provide accurate real-time weather data!",  
"Travel Info - Create solutions for flights, hotels, and destinations!",  
"Sports Scores - Deliver live sports updates for apps!",  
"Finance Tools - Offer solutions for expense tracking and invoicing!",  
"Job Listings - Scrape and serve job openings data!",  
"SEO Analytics - Provide insights on website rankings!",  
"URL Shortener - Create a paid service for link shortening!"  
]

money_quotes = [
"The way to get started is to quit talking and begin doing.", 
"Opportunities don’t happen. You create them." ,  
"If you don’t find a way to make money while you sleep, you will work until you die." ,  
"Formal education will make you a living; self-education will make you a fortune." ,  
"Don’t be afraid to give up the good to go for the great." ,  
"It’s not about ideas. It’s about making ideas happen." ,  
"Success is not in what you have, but who you are.",  
"Work like hell. I mean you just have to put in 80 to 100 hour weeks." ,  
"Do what you love and the money will follow.",  
"A business that makes nothing but money is a poor business."  
]

# specific funtion mien add on funtionality hone ka km decorator anjam dete hain

@app.get("/")
def read_root():
    return {
        "message": "Hello World, Go to /side_hustles or /money_quotes to get a random side hustle or money quote"
    }

@app.get("/side_hustles") #route handler
def get_side_hustles():
    """Return a random side hustle idea"""

    return {"side_hustles": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
    """Return a random money quote"""
    return {"money_quotes": random.choice(money_quotes)}

