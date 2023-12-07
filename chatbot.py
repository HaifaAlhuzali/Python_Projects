import nltk
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.util import ngrams
from tkinter import *

#patterns 
city = [
["makkah","riyadh","dammam","alula","abha"],
["For many Muslims around the world, an opportunity to visit Makkah is the ultimate blessing. This is the holiest city in Islam: the birthplace of the Prophet Muhammad and the city where the Quran was first revealed to him. It’s also a fixture in observant Muslims’ daily lives, as they orient themselves toward Makkah to pray five times a day."
,"Riyadh’s blend of medieval and millennial makes for a beguiling cultural union — one where Arabia’s first roots can be traced, and where its bold future can be envisioned."
,"Boasting endless views of the tranquil Arabian Gulf, Dammam is a modern metropolis that thrives on its coastal location. "
,"Deep in the beautiful deserts of the northwestern region of the country, AlUla is home to countless historic treasures, including the Nabatean city of Hegra - Saudi Arabia’s first UNESCO World Heritage site, the tombs of Dadan - the stone-built capital of the Dadanite and Lihyanite Kingdoms, and the ancient ruins of AlUla Old Town - a prominent pitstop for pilgrims in the 12th century. "
,"Part of the marvel of the trip to Abha, which is full of breath-taking natural sights, is seeing its fog that penetrates its mountains and touches its land in Al-Dabab Walkway, which spans over 7 km. This experience, amidst a panoramic painting that showcases the greenery of the Sarawat Mountains, is worth travelling for."
]]
#shrooq 
restaurant = [
    ["restaurant","food","eat","meal","dinner"],
    [["Gurkan Chef Steak House Restaurant(location_link): \nhttps://g.page/gurkansefmecca?share", "albaik restaurant(location_link): \nhttps://goo.gl/maps/HmUTk4ew7Mb3NUzC6"]
    ,["Mirage Restaurant(location_link): \nhttps://goo.gl/maps/7bMaYuSv7EU6ScdW9", "Najd Village Restaurant(location_link): \nhttps://g.page/najdvillagetak?share"]
    ,["Steakhouse Restaurant(location_link): \nhttps://g.page/SteakHouseSA-Dammam?share", "red dragon restaurant(loaction_link): \nhttps://goo.gl/maps/x3dnojcQcf6Pb8WR6"]
    ,["Al Ula Palace restaurants and kitchens(location_link): \nhttps://goo.gl/maps/9xkBewtFxAQXaSQP8", "Tetra Pizza Restaurant(location_link): \nhttps://goo.gl/maps/jFqRNXahrHrG9dR46"]
    ,["Al-Sinara Restaurant(location_link): \nhttps://goo.gl/maps/pyVfmyN2g6v4HT1M9", "Al Sinara Restaurant Maharaj Indian Restaurant(location_link): \nhttps://goo.gl/maps/RGRgRfChRYnpQUgP9"]
    ]]
#Ghaida
hotels = [["hotel","hostel","motel","house","lodging"],
[
["Park Inn by Radisson: \nYou will enjoy the beauty and spirituality of Makkah Al Karma during your stay at the Park Inn by Radisson Makkah Al Naseem facility, as this facility features a stunning view of Al Rajhi Mosque, and is surrounded by the Lak Abdullaa Zamzam project and the Al-Ram Mosque\nRating:5 stars\nServices: Free Wi-Fi, Disabled Facilities, Shuttle Service, Parking, shops, gym\nLocation: 15 minutes' drive from Al Rajhi Mosque and Makkah Mall\n", "Retaj Al Rayyan Hotel Makkah: \nEnjoy the beauty and spirituality of Makkah Al Karma during your stay at the Retaj Al Rayyan Hotel Makkah to live an unforgettable soil when you visit the Kaaba, Al-Ram Mosque and Al-Siniyah Garden\nRating: 4 stars\nServices: Free Wi-Fi, Gym, Parking, Spa, sauna, car rental service\nLocation: Al Rawda Street, Shisha"]
,["Mövenpick Hotel & Residences Riyadh: \nThis elegant hotel features elegant rooms with floor-to-ceiling windows, Nespresso machines and mini-fridges. The higher-class rooms feature access to the Executive Lounge. Studios and one- and two-bedroom apartments have kitchens.\nRating: 5 stars\nServices:Free WiFi, Spa, Gift shop, Babysitting service, Facilities for disabled guests, Outdoor pool, Airport shuttle, Parking\nLocation: 5 minutes' drive from Azizia Mall and Riyadh Park Mall\n", "Hilton Garden Inn Riyadh, King Abdullah Financial District:\nThis upscale hotel features simple rooms with floor-to-ceiling windows, flat-screen TVs and mini-fridges. The superior rooms feature sofa beds and/or city views. Room service is provided.\nRating: 4 stars\nServices: Free Wi-Fi, facilities for people with special needs, parking, markets and shops, gym\nLocation: In a facility in the business district, a 15-minute drive from Dr. Sulaiman Al Habib Hospital and the Riyadh International Convention and Exhibition Center"]
,["Radisson Hotel & Apartments in Dammam Industrial City: \nYou are now about to discover the breathtaking beauty of the city of Dammam when you stay at the Park Inn by Radisson Hotel & Apartments Dammam Industrial Area 2, to live an unforgettable experience when you visit Half Moon Beach and the US Consulate General in Dhahran\nRating: 4 stars\nServices: Wi-Fi, Disabled Facilities, Swimming Pool, Outdoor Pool, Airport Shuttle, Parking, Tennis Court, Gym, Spa, Massage, Salon\nLocation: The location of the Radisson Hotel & Apartments in Dammam Industrial City in Dammam places you within a 15-minute drive of Prince Muhammad Bin Fahd Theme Park and Half Moon Beach", "Lavona Taiba Hotel: \nWhen you stay at Lavona Taiba Hotel in Dammam, you'll be within a 10-minute drive of Dhahran International Exhibition Center. This hotel is 11.3 km (11.3 km) from King Fahd Park and 11.8 km from Dammam Public Library and National Museum.\n Rating: 3 stars\nServices: Wifi, Parking, Kid-friendly buffet\nLocation: 17 km from Radisson Hotel & Apartments in Dammam Industrial City"]
,["Shaden Resort: \nShaden Resort is one of the best places in AlUla where you can have a good stay at an economical price\nRating: 4 stars\nServices: Free Wi-Fi, Parking, Swimming pool, Accessible for disabled guests, Laundry service, Kitchens in some rooms, Airport shuttle service for a fee\nLocation: Shaden Resort is 22 km from the tombs of Madain Saleh, 9.2 km from the city of Al-Ula, and 45 km from Prince Abdul Majeed bin Abdulaziz Domestic Airport\n", "Waad Al Ula Hotel: \nA great choice for a stay in Al-'Ula, Waad Al Ula Hotel features a rooftop terrace\nRating: 3 stars\nServices: Free Wi-Fi, Airport shuttle, Laundry service, Parking\nLocation: 15 minutes' drive from AlUla Museum and AlUla Old Town\n"]
,["Boudl Abha: \nRating: An amazing stay awaits you at Boudl Abha facility located in Abha, where you will enjoy visiting Abu Khayal Park and Al Salam Park amusement park\n3 stars\nServices: Free Wi-Fi, Disabled Facilities, Gym, Parking\nLocation: 3 minutes' drive from Andalusia Park and 6 minutes' drive from Shada Palace\n", "Eber Abha: \nTake the opportunity to explore the most prominent tourist attractions in AbhaAbha Mall, Waterfall Park and Agrab Complex when you stay in Aber Abha\nRating: 3 stars\nServices: Free Wi-Fi, Disabled Facilities, Gym, Parking\nLocation: Ibrahim Al-Hadith Street, Shamsan District"]
]]
#TaifAlshrif
archaeologicalMonuments = [["museum","monument","archaeological","ancient","heritage"],
[
["Al-Zaher Palace: \nThe museum displays the history of Makkah and houses many archaeological collections from the different periods of Islamic history in the region.","Jabal Al Nour: \nThe first verses of the Holy Quran were revealed to the Prophet Muhammad (P.B.U.H) inside the cave at the summit of this hill. The Prophet used to  spend time in the cave and meditate. According to Muslim belief, it was here that the angel Gabriel gave the Prophet Muhammad (P.B.U.H) his first revelation during the month of Ramadan in 610 C.E."]
,["Al-Masmak Palace: \nwhich is a vast castle made of mud and bricks, and it is preferred by tourists who want to go back in time and explore the roots of Saudi Arabia.","The Saudi National Museum:\ncontains more than 3,700 artifacts on display, documenting the ancient history of Saudi Arabia over thousands of years."]
,["Heritage Village: \nThe 5-storey Heritage Village is the perfect place to discover Saudi culture and heritage. Fascinating artifacts, manuscripts, and other items are on display.","Tarout Castle: \nFort Tarout or Tarout Castle is situated in the centre of Tarout Island in Qatif. The fort goes way back — around 5000 years ago — made evident by the Mesopotamian God’s statues and inscriptions found there. In the 16th century, it was invaded by the Portuguese, who used it as a military base. Today, the castle provides a memorable glimpse into the Kingdom’s past."]
,["Al-Hijr: \nwhich is the first UNESCO World Heritage property to be inscribed in the Kingdom of Saudi Arabia. This site is known with its famous tombs, along with the “Dadan” civilization, which dates back beyond the 1st millennium"," Mount Elephant: \nThis rock is classified as very viscous and takes the shape of an elephant, reaching a height of 52 meters above the ground. Elephant Mountain, also known as Elephant Rock, is one of the best tourist attractions in Al-Ula city"]
,["Al-Muftahha Palace: \nwhich displays archaeological holdings dating back to the Jurassic period and weapons dating back to the 16th century, in addition to manuscripts and old printed copies of the Holy Quran.","Al-Raqdi Museum: \nCalled the Museum of the Quarter of a Century, which makes it one of the most ancient museums of Abha and the most important of its holdings and rare manuscripts of up to two thousand pieces."]
]]
#Haifa 
Events =[["event","activity","fun","entertainment"],
[["A Weekend with the Kids at KAEC: KAEC is a city of the future. Its charming villas and condos, greenery, and varied activities make it perfect for a family staycation. Register on KAEC for access to this coastal getaway, just an hour and a half off Jeddah. Location Information : https://www.google.com/maps/place/Exclusive+Desert+Camps/@22.3688514,39.0976655,314m/data=!3m1!1e3!4m6!3m5!1s0x15c0e3d4b6f0c0b9:0xdf581e65abdb1b0d!8m2!3d22.368452!4d39.0974724!16s%2Fg%2F11f7q_y983","The Makkah Province :The city of Makkah itself is only accessible to Muslims. Each year, it bears witness to the Hajj pilgrimage, a religious duty that must be performed by every able Muslim at least once in their lifetime, and which draws millions each year. Holy sites in the city include the sacred Ka’aba, located in the heart of the Masjid al-Haram, or Grand Mosque, while the circling mountains house the historic Cave of Thawr, where the Prophet sought refuge from the Quraysh tribe, and the revered Jabal Rahmah, where he delivered his last sermon."]
,["Boulevard Riyadh City is one of the biggest zones in the season. Triple in size this year, each of the sub-areas features its own set of activities, restaurants, events, and outlets that are catered to all visitors. , Date :29 Oct 2021 - 26 Dec 2022 Working Hours :09:00 PM - 08:00 AM Category : Themed Attractions Audience: All , Location Information: https://www.google.com/maps/place/24%C2%B045'51.1%22N+46%C2%B036'13.9%22E/@24.7641944,46.6038611,17z/data=!3m1!4b1!4m4!3m3!8m2!3d24.7641944!4d46.6038611 ","XP Music Futures: About this event Date 28 Nov 2022 - 30 Nov 2022 Working Hours 11:00 AM - 01:00 AM Category Convention & Exhibition Audience AdultsXP Music Futures will be back in Riyadh this November 28, 29 & 30! Join us as we kick off the loudest week in Riyadh with our annual music conference. Step into interactive workshops, participate in discussions and immerse yourself in our music regional scene. XP Music Futures was established to accelerate MENA’s music industry."]
,["Half Moon Bay :A short drive south from Dammam, Half Moon Bay was a stop for many of the Arab traders from the Arabian Gulf area. It has become a top draw for recreation thanks to its family-friendly setup: The entrances to the cove are very shallow and tranquil, and the average water depth reaches about 7 meters, so it’s an ideal location to learn how to scuba dive, or just dip your toes on a warm winter day."]
,["AlUla Moments : Unlock the wonders of AlUla and partake in four unique events and festivals starting September 2022, where beyond extraordinary landscapes, there will be more to remember — moments of excitement, moments of freedom, moments of discovery, and moments of delight.Date 22 Sep 2022 - 20 Jan 2023 Working Hours 12:00 AM - 12:00 AM Activities Themed Attractions Audience All Location Information https://www.google.com/maps/place/26%C2%B037'39.6%22N+37%C2%B055'06.4%22E/@26.6275992,37.9138999,16z/data=!4m4!3m3!8m2!3d26.6276667!4d37.9184444","Winter at Tantora: About this event Winter at Tantora is returning for its fourth season. Being the region’s longest-running music and arts festival, Winter at Tantora features intimate concerts with world-renowned musicians and hosts multiple events and activations across culture, heritage, gastronomy and more. Join us for a full month and experience the best of AlUla.Date 20 Dec 2022 - 20 Jan 2023 Working Hours 12:00 AM - 12:00 AM Category Shows & Performing Arts Audience All"]
,["Soar Through the Festival above the mountains! Come explore the magical Village hidden in the mists of Abha’s Summer Festival, a destination designed to meet your every whim, where culture meets connection. Packed with a variety of activities from carnival games to concerts and everything in between! Expect exciting performances from popular and emerging artists as you go on a musical adventure in the misty mountains. Awaken your tastebuds to the fusion of exotic and familiar tastes of dishes from all around the world. 28 July 2022 until 24 September 2022"]
]]
End=['bye', 'goodbye','thanks']



#Method for selecting the city of the user
flagCity= True
indexCity=0 
def selectCity(cityselected):

    global indexCity
    word = word_tokenize(cityselected.lower())
    stopword = set(stopwords.words('english'))
    wordFilter = [w for w in word if not w in stopword]
    for w in wordFilter:
        i=0
        for c in city[0]:
            if(w==c):
                indexCity = i
                return(city[1][i])
            i=i+1 

#Method for selecting Request of the User 
indexRequest=0
flagRequest= False

def selectRequest(request):
    global indexRequest
    global indexCity

    word = word_tokenize(request.lower())
    stopword = set(stopwords.words('english'))
    wordFilter = [w for w in word if not w in stopword]
    
    for w in wordFilter:
        # if the user select Restaurant
        if(w in restaurant[0]):
             indexRequest = 1
             return(restaurant[1][indexCity][0])    
        # if the user select Hotel
        if(w in hotels[0]):
             indexRequest = 2
             return(hotels[1][indexCity][0])
         # if the user select Archaeological monument
        if(w in archaeologicalMonuments[0]):
             indexRequest = 3
             return(archaeologicalMonuments[1][indexCity][0])
        # if the user select Event
        if(w in Events[0]):
             indexRequest = 4
             return(Events[1][indexCity][0])
        # if the user wants end chat
        if(w in End):
             return(request)





root=Tk()
root.config(bg="#fff")
root.title("Tour Guide for saudi arabia")
root.maxsize(400, 500)


#Method for moving to the second page
def start():

     canvas.destroy()
     canvas2.pack()


#UI for the first page 
imgbg=PhotoImage(file="first.png")
canvas=Canvas(root,width=400,height=500, bd=0)
canvas.create_image(0,0,anchor="nw", image=imgbg)
canvas.pack()
imgbtn=PhotoImage(file="start.png")
btn=Button(canvas,image=imgbtn, relief="flat", bg="#fff", activebackground="#fff", command=start)
canvas.create_window(145,389,anchor="nw", window=btn)

#Method for starting a chat with bot

def send():
    question = entry.get()
    insert(question)
    
def  insert(question):
      
      entry.delete(0,END)
      text.insert(END,'You: '+question+'\n\n')
      answer=getResponse(question)
      text.insert(END,'Bot: '+answer+'\n\n')


def getResponse(massage):
    global flagCity
    global flagRequest
    if(flagCity):
         if(selectCity(massage)!=None):
             flagCity = False
             return(selectCity(massage)+"\n\nPlease tell me what you want to know about this city? Places to at or stay... ")
         else:
             return("Sorry, I can't help you with this city, But ask me about another city.")
    elif(flagRequest):
              flagRequest=False
              word=word_tokenize(massage.lower())
              bigram=[' '.join(e) for e in ngrams(word, 2)]
              for bi in bigram: 
                 if(bi=="not enough"):
                      if(indexRequest == 1):
                         return("This is another result\n"+restaurant[1][indexCity][1]+"\nPlease tell me again what you want to know about this city?")
                      if(indexRequest == 2):
                         return("This is another result\n"+hotels[1][indexCity][1]+"\nPlease tell me again what you want to know about this city?")
                      if(indexRequest == 3):
                         return("This is another result\n"+archaeologicalMonuments[1][indexCity][1]+"\nPlease tell me again what you want to know about this city?")
                      if(indexRequest == 4):
                         return("This is another result\n"+Events[1][indexCity][1]+"\nPlease tell me again what you want to know about this city?")
              return("great!!, \nPlease tell me again what you want to know about this city?")                      
    else:
         if(selectRequest(massage)!=None):
            if(selectRequest(massage) in End):
                 return("Bay! Have a nice journey")
            else:
                 flagRequest=True
                 return(selectRequest(massage)+"\n Please tell me are the result enough?")
                 
         else:
             return("Sorry your question is unclear, Please clarify what you want to know about the city.")        



     

    
     
#UI for the second page 
imgbg2=PhotoImage(file="second.png")
canvas2=Canvas(root,width=400,height=500, bd=0)
canvas2.create_image(0,0,anchor="nw", image=imgbg2)
imgbtn2=PhotoImage(file="send.png")
btn2=Button(canvas2,image=imgbtn2, relief="flat", bg="#fff", activebackground="#fff", command=send)
canvas2.create_window(275,432,anchor="nw", window=btn2)
entry = Entry(canvas2, font=('calibre',20,'normal'),bg="#D4E9EE",relief="flat",width=15)
canvas2.create_window(26,442,anchor="nw", window=entry)
text = Text(canvas2, font=('calibre',10,'normal'),bg="#D4E9EE",relief="flat",width=50,height=16)
canvas2.create_window(205,270,anchor=CENTER, window=text)
text.insert(END,"Bot: Welcome, In Saudi Arabia, I am your tour guide. \nPlease tell me what is your tourist destination? Makkah - Riyadh - Dammam - AlUla - Abha \n\n")


root.mainloop()