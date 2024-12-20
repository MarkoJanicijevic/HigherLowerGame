import random

logo = '''



88        88 88             88                                88                                                               
88        88 ""             88                                88                                                               
88        88                88                                88                                                               
88aaaaaaaa88 88  ,adPPYb,d8 88,dPPYba,   ,adPPYba, 8b,dPPYba, 88          ,adPPYba,  8b      db      d8  ,adPPYba, 8b,dPPYba,  
88""""""""88 88 a8"    `Y88 88P'    "8a a8P_____88 88P'   "Y8 88         a8"     "8a `8b    d88b    d8' a8P_____88 88P'   "Y8  
88        88 88 8b       88 88       88 8PP""""""" 88         88         8b       d8  `8b  d8'`8b  d8'  8PP""""""" 88          
88        88 88 "8a,   ,d88 88       88 "8b,   ,aa 88         88         "8a,   ,a8"   `8bd8'  `8bd8'   "8b,   ,aa 88          
88        88 88  `"YbbdP"Y8 88       88  `"Ybbd8"' 88         88888888888 `"YbbdP"'      YP      YP      `"Ybbd8"' 88          
                 aa,    ,88                                                                                                    
                  "Y8bbdP"                                                                                     


'''

vs = '''


                             
8b           d8  ad88888ba   
`8b         d8' d8"     "8b  
 `8b       d8'  Y8,          
  `8b     d8'   `Y8aaaaa,    
   `8b   d8'      `"""""8b,  
    `8b d8'             `8b  
     `888'      Y8a     a8P  
      `8'        "Y88888P"   
                             
                             




'''


celebrities = {
    "Cristiano Ronaldo": [600_000_000, "Portugal", "Footballer"],
    "Lionel Messi": [500_000_000, "Argentina", "Footballer"],
    "Kim Kardashian": [350_000_000, "United States", "Reality TV Star/Entrepreneur"],
    "Beyoncé": [300_000_000, "United States", "Singer"],
    "Selena Gomez": [400_000_000, "United States", "Singer/Actress"],
    "Dwayne Johnson": [350_000_000, "United States", "Actor/Professional Wrestler"],
    "Kylie Jenner": [380_000_000, "United States", "Entrepreneur/Reality TV Star"],
    "Ariana Grande": [370_000_000, "United States", "Singer/Actress"],
    "Taylor Swift": [270_000_000, "United States", "Singer"],
    "Justin Bieber": [280_000_000, "Canada", "Singer"],
    "Zendaya": [160_000_000, "United States", "Actress/Singer"],
    "Billie Eilish": [100_000_000, "United States", "Singer"],
    "LeBron James": [150_000_000, "United States", "Basketball Player"],
    "Drake": [120_000_000, "Canada", "Rapper"],
    "Rihanna": [150_000_000, "Barbados", "Singer/Entrepreneur"],
    "Shawn Mendes": [70_000_000, "Canada", "Singer"],
    "Lady Gaga": [55_000_000, "United States", "Singer/Actress"],
    "Kanye West": [60_000_000, "United States", "Rapper/Entrepreneur"],
    "Tom Holland": [50_000_000, "United Kingdom", "Actor"],
    "Emma Watson": [70_000_000, "United Kingdom", "Actress"],
    "Chris Hemsworth": [60_000_000, "Australia", "Actor"],
    "Gal Gadot": [90_000_000, "Israel", "Actress"],
    "Will Smith": [70_000_000, "United States", "Actor"],
    "Jennifer Lopez": [230_000_000, "United States", "Singer/Actress"],
    "The Weeknd": [50_000_000, "Canada", "Singer"],
    "David Beckham": [80_000_000, "United Kingdom", "Footballer"],
    "Elon Musk": [50_000_000, "United States", "Entrepreneur"],
    "Bill Gates": [60_000_000, "United States", "Entrepreneur/Philanthropist"],
    "Cristiano Ronaldo Jr.": [1_500_000, "Portugal", "Influencer"],
}

def rand_celebrity (x):
    return random.choice(list(celebrities.keys()))

def format_guess (x):
    return f"{x}, a {celebrities[x][2].lower()}, from {celebrities[x][1]}"


