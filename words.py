import random

#the categories of words and the words being used
cat_animals = ["dog", "cat", "hamster", "mouse", "snake", "rabbit", "horse", "tiger", "shark", "giraffe", "zebra", "lion", "fish", "narwhal", "goat"]
cat_food = ["burger", "pizza", "steak", "cheese", "banana", "apple", "cauliflower", "broccoli", "sandwich", "eggs", "cookies", "cake", "rice", "bacon", "cupcakes"]
cat_vehicles = ["car", "bus", "truck", "plane", "train", "boat", "blimp", "bike", "wagon", "horse", "ship", "ferry", "motorcycle", "van", "rickshaw"]
cat_colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "black", "turquoise", "brown", "fuchsia", "maroon", "magenta", "gray", "lavender"]
cat_footwear = ["sneakers", "flats", "wedges", "heels", "loafers", "boots", "platforms", "sports", "sandals", "flipflops", "slippers", "mules", "trainers", "slides", "moccasins"]
cat_singers = ["madonna", "drake", "pink", "adele", "sting", "cher", "eminem", "halsey", "tupac", "prince", "shakira", "rihanna", "beyonce", "fergie", "pitbull"]
cat_designerBrands = ["gucci", "balenciaga", "prada", "hermes", "moschino", "chanel", "dior", "armani", "valentino", "versace", "balmain", "givenchy", "cartier", "fendi", "burberry"]
cat_streetwear = ["gosha", "bape", "offwhite", "supreme", "undefeated", "undercover", "fila", "nike", "adidas", "stussy", "kith", "thrasher", "palace", "obey", "carhartt"]
cat_indonesianCities = ["jakarta", "bandung", "bali", "solo", "yogyakarta", "palembang", "padang", "makassar", "medan", "surabaya", "semarang", "manado", "jayapura", "ambon", "banjarmasin"]
cat_capitalCities = ["rome", "jakarta", "canberra", "brasilia", "beijing", "tokyo", "paris", "london", "berlin", "moscow", "dublin", "tehran", "ottawa", "cairo", "riyadh"]
cat_socialMedia = ["youtube", "facebook", "instagram", "twitter", "snapchat", "whatsapp", "line", "pinterest", "tumblr", "skype", "myspace", "vimeo", "soundcloud", "reddit", "vimeo"]
cat_tvShows = ["supernatural", "revenge", "lucifer", "lost", "arrow", "gotham", "merlin", "dracula", "camelot", "daredevil", "heroes", "friends", "glee", "smallville", "macgyver"]

#all the categories
categories = [cat_animals, cat_food, cat_vehicles, cat_colors, cat_footwear, cat_singers, cat_designerBrands, cat_streetwear, cat_indonesianCities, cat_capitalCities, cat_socialMedia, cat_tvShows]

cat_random = random.choice(categories)