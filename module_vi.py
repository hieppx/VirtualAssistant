from library import *

def get_text_vi(self):
    for i in range(3):
        text_vi = self.get_voice_vi()
        if text_vi:
            return text_vi.lower()
        elif i < 2:
            self.speak_vi("Bot không nghe rõ. Bạn nói lại được không!")
    return 0
content_vi = []
def speak_vi(self, text_vi):
    print("Bot: {}".format(text_vi))
    self.uic.bot_chat.setText("")
    content_vi.append(text_vi)
    for x in content_vi:
        self.uic.bot_chat.append("Bot: " + str(x) +"\n" + "____________________________________________________________")
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(text_vi)
    engine.runAndWait()
content_voice_vi = []
def get_voice_vi(self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Me: ", end='')
        audio_vi = r.listen(source, phrase_time_limit=5)
        try:
            text_vi = r.recognize_google(audio_vi, language="vi-VN")
            self.uic.me_chat.setText("")
            content_voice_vi.append(text_vi)
            for x in content_voice_vi:
                self.uic.me_chat.append("Me: " + str(x) +"\n" + "_____________________________________________________________")
            print(text_vi, end = '')
            print("")
            return text_vi
        except:
            self.uic.me_chat.setText("...")
            print("")
            return 0

def change_wallpaper_vi(self):
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
    self.speak_vi('Hình nền máy tính đã được thay đổi!')

def stop_vi(self):
    self.speak_vi("Tạm biệt bạn, hẹn gặp lại bạn sau nhé!")

def talk_vi(self, name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        self.speak_vi("Chào buổi sáng {}. Chúc bạn ngày mới tốt lành! Bạn khỏe không?".format(name))
    elif day_time < 18:
        self.speak_vi("Chào buổi chiều {}! Bạn khỏe không?".format(name))
    else:
        self.speak_vi("Chào buổi tối {}! Bạn khỏe không?".format(name))
    ans = self.get_voice_vi()
    if ans:
        if "có" in ans or "khỏe" in ans:
            self.speak_vi("Rất tốt! Chúc bạn luôn luôn khỏe mạnh!")
        else:
            self.speak_vi("Bạn nên nghỉ ngơi đi!")

def get_time_vi(self, text_vi):
    now = datetime.datetime.now()
    if "giờ" in text_vi:
        self.speak_vi('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text_vi:
        self.speak_vi("Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year))

def open_website_vi(self, text_vi):
    reg_ex = re.search('truy cập (.+)', text_vi)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain + '.com'
        webbrowser.open(url)
        self.speak_vi("Trang web bạn yêu cầu đã được mở.")
        return True
        time.sleep(3)
    else:
        return False

def open_application_vi(self, text_vi):
    if "Google Chrome" in text_vi:
        self.speak_vi("Tôi sẽ mở nó ngay!")
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        time.sleep(3)
    elif "word" in text_vi:
        self.speak_vi("Tôi sẽ mở nó ngay!")
        os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
        time.sleep(3)
    elif "excel" in text_vi:
        self.speak_vi("Tôi sẽ mở nó ngay!")
        os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE')
        time.sleep(3)
    else:
        self.speak_vi("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")

def open_google_and_search_vi(seft, text):
    search_for = text.split("tìm kiếm", 1)[1]
    seft.speak_vi("Đây rồi, tôi đã tìm được nó.")
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    time.sleep(3)

def tell_me_about_vi(seft):
    try:
        seft.speak_vi("Bạn muốn nghe về gì ạ")
        text = seft.get_text_vi()
        wikipedia.set_lang("vi")
        contents = wikipedia.summary(text).split('\n')
        seft.speak_vi(contents[0])
        time.sleep(5)
        for content in contents[1:]:
            seft.speak_vi("Bạn muốn nghe thêm không")
            ans = seft.get_text_vi()
            if "có" not in ans:
                break
            seft.speak_vi(content)
            time.sleep(10)
        seft.speak_vi('Cảm ơn bạn đã lắng nghe!!!')
    except:
        seft.speak_vi("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")


def play_youtube_vi(self):
    self.speak_vi('Xin mời bạn chọn tên bài hát!')
    mysong = self.get_text_vi()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    self.speak_vi("Bài hát bạn yêu cầu đã được mở!")

def read_news_vi(seft):
    seft.speak_vi("Bạn muốn xem tin tức gì?")
    queue = seft.get_voice_vi()
    params = {
        'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
        "q": queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()

    for number, result in enumerate(api_response['articles'], start=1):
        seft.uic.bot_chat.setText(
            f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
        """)
        if number <= 3:
            webbrowser.open(result['url'])

