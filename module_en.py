from library import *

content_en = []
def speak_en(self, text_en):
    print("Bot: {}".format(text_en))
    self.uic.bot_chat.setText("")
    content_en.append(text_en)
    for x in content_en:
        self.uic.bot_chat.append("Me: " + str(x) +"\n" + "____________________________________________________________")
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say(text_en)
    engine.runAndWait()

content_voice_en = []
def get_voice_en(self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Me: ", end='')
        print("")
        audio_en = r.listen(source, phrase_time_limit=5)
        try:
            text_en = r.recognize_google(audio_en, language="en-US")
            self.uic.me_chat.setText("")
            content_voice_en.append(text_en)
            for x in content_voice_en:
                self.uic.me_chat.append("Bot: " + str(x) +"\n" + "_____________________________________________________________")
            print(text_en)
            return text_en
        except:
            self.uic.me_chat.setText("...")
            print("...")
            return 0

def stop_en(self):
    self.speak_en("Goodbye, see you again!")

def get_text_en(self):
    for i in range(3):
        text_en = self.get_voice_en()
        if text_en:
            return text_en.lower()
        elif i < 2:
            self.speak_en("I can't hear, Can you repeat?")
    return 0


def talk_en(self, name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        self.speak_en("Good morning {}. Have a good day!".format(name))
    elif day_time < 18:
        self.speak_en("Good afternoon {}!".format(name))
    else:
        self.speak_en("Good evening {}!".format(name))
    time.sleep(2)
    self.speak_en("How are you?")
    time.sleep(2)
    ans = self.get_voice_en()
    if ans:
        if "yes" in ans or "I'm fine" in ans:
            self.speak_en("Very good!")
        else:
            self.speak_en("I think you should have a rest!")

def get_time_en(self, text_en):
    now = datetime.datetime.now()
    if "hour" in text_en:
        self.speak_en("It's %d o'clock %d minutes" % (now.hour, now.minute))
    elif "day" in text_en:
        self.speak_en("Today is %d %d, %d" % (now.month, now.day, now.year))

def open_application_en(self, text_en):
    if "Google Chrome" in text_en:
        self.speak_en("I will open it now!")
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        time.sleep(3)
    elif "word" in text_en:
        self.speak_en("I will open it now!")
        os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
        time.sleep(3)
    elif "excel" in text_en:
        self.speak_en("I will open it now!")
        os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE')
        time.sleep(3)
    else:
        self.speak_en("The application is not installed. Please try again!")


def tell_me_about_en(seft):
    try:
        seft.speak_en("What do you want to hear about ?")
        text = seft.get_text_en()
        wikipedia.set_lang("en")
        contents = wikipedia.summary(text).split('\n')
        seft.speak_en(contents[0])
        time.sleep(10)
        for content in contents[1:]:
            seft.speak_en("Do you want to hear more??")
            ans = seft.get_text_en()
            if "yes" not in ans:
                break
            seft.speak_en(content)
            time.sleep(10)

        seft.speak_en('Thank you for listening!!!')
    except:
        seft.speak_en("I don't define your term. Please say it again!")

def open_website_en(self, text_en):
    reg_ex = re.search('access (.+)', text_en)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain + '.com'
        webbrowser.open(url)
        self.speak_en("The website you requested has been opened.")
        return True
    else:
        return False

def open_google_and_search_en(seft, text_en):
    search_for = text_en.split("search", 1)[1]
    seft.speak_en("Here it is, I found it.")
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)

def play_youtube_en(self):
    self.speak_en('Please choose the name of the song!')
    mysong = self.get_text_en()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    self.speak_en("The song you requested has been opened!")

def read_news_en(seft):
    seft.speak_vi("What do you want to read about?")
    queue = seft.get_text_en()
    params = {
        'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
        "q": queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    for number, result in enumerate(api_response['articles'], start=1):
        seft.uic.bot_chat.setText(
            f"""New {number}:\nTitle: {result['title']}\nQuote: {result['description']}\nLink: {result['url']}""")
        if number <= 3:
            webbrowser.open(result['url'])

def change_wallpaper_en(self):
    api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
    url = 'https://api.unsplash.com/photos/random?client_id=' + api_key
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    urllib2.urlretrieve(photo, "C:/Users/hiepp/Desktop/Design/bg.jpg")
    image = os.path.join("C:/Users/hiepp/Desktop/Design/bg.jpg")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 3)
    self.speak_en('The desktop wallpaper has been changed!')




