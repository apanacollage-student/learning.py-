# write a probram to ccreate a dictionary of hindi 
# words with values as their engish translations provide user with an option
# to look up a word

words = {
    "namaste": "hello",
    "dost": "friend",
    "paani": "water",
    "pustak": "book",
    "madad": "help",
"shukriya": "thank you",
"kalam": "pen",
    "mez": "table",
    "roti": "bread",
    "doodh": "milk",
    "pankha": "fan",
    "kapda": "cloth",
    "dost": "friend",
    "khana": "food",
    "khana": "food",
    "andar": "inside",
    "kal": "tomorrow",
    "kal": "tomorrow",
    "bitta_kal": "yesterday",
    "aadmi": "man",
    "ladka": "boy",
    "ladki": "girl",
    "nadi": "river",
    "pahad": "mountain",
    "gharana": "family",
    "bazar": "market",
    "bazaar": "market",
    "gaadi": "vehicle",
    "sadak": "road",
    "school": "school",
    "shahar": "city",
    "gaon": "village",
    "mandir": "temple",
    "masjid": "mosque",
    "path": "lesson",
    "khidki": "window",
    "darwaza": "door",
    "charpai": "cot",
    "kursi": "chair",
    "kamra": "room",
    "dariya": "sea",
    "phool": "flower",
    "ped": "tree",
    "patta": "leaf",
    "dharti": "earth",
    "suraj": "sun",
    "chand": "moon",
    "taara": "star",
    "aag": "fire",
    "hawa": "air",
    "mitti": "soil",
    "pathar": "stone",
    "rail": "train",
    "naukri": "job",
    "paisa": "money",
    "kela": "banana",
    "aam": "mango",
    "angoor": "grapes",
    "papita": "papaya",
    "gajar": "carrot",
    "tamatar": "tomato",
    "pyaz": "onion",
    "adrak": "ginger",
    "lehsun": "garlic",
    "namak": "salt",
    "chini": "sugar",
    "haldi": "turmeric",
    "mirch": "chilli",
    "daliya": "porridge",
    "billi": "cat",
    "kutta": "dog",
    "ghoda": "horse",
    "gai": "cow",
    "bhains": "buffalo",
    "machhli": "fish",
    "pakshi": "bird",
    "kabutar": "pigeon",
    "mor": "peacock",
    "haathi": "elephant",
    "bhalu": "bear",
    "sher": "lion",
    "bagh": "tiger",
    "hath": "hand",
    "pair": "foot",
    "aankh": "eye",
    "naak": "nose",
    "kaal": "time",
    "gussa": "anger",
    "khushi": "happiness",
    "dukhi": "sad",
    "bhookh": "hunger",
    "pyaas": "thirst",
    "safed": "white",
    "kala": "black",
    "neela": "blue",
    "laal": "red",
    "peela": "yellow",
    "hara": "green",
    "zindagi": "life",
    "mohabbat": "love",
}
words_input = input("welcome ayush hindi and english dictionary:",)
print("the meaning of your word is:", words.get(words_input, "word not procesing in dictionary"))

# 2 question = input eight number from user and display all the unique numbers
s=set()
for i in range(1,8):
    s.add(int(input("enter the number:")))
print("the unique numbers are:", s)


# 3 question can we set with interger and string
# yes we can create sets with interger and string both
s=set()
s.add(18)
s.add("18")
print(s, type(s))


# 4 question what will be lenth of following sets
s=set()
s.add(20)
s.add(20.0)   # same value hai interger and float ka than ye data type ko ignore kar dega
s.add("20")
print(s, len(s))

# 5 question {} what is the type of this
a={}
print(type(a))

# create an empty dictionary allow 4 user to enter their fevorite language as value use 
# key as their name assume the names are unique

l={}
for i in range(1,5):
 name =input("enter your name:")
 lang=input("enter your fevorite language:")
 l.update({name:lang})  # es me name or lang ake pair me add ho jaaye ga
  #ex :name=ayush lang=python  => {ayush:python}
 print(l)