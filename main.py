import time

from library import *

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.Button_Vietnamese.clicked.connect(lambda: self.call_sen_vi())
        self.uic.Button_English.clicked.connect(lambda: self.call_sen_en1())
        self.uic.Button_Clear.clicked.connect(lambda: self.clear_text())
        self.uic.Button_Exit.clicked.connect(lambda: self.exit_app())

    from module_vi import get_text_vi, speak_vi, get_voice_vi, stop_vi, talk_vi, get_time_vi, change_wallpaper_vi, open_website_vi, \
        open_application_vi, open_google_and_search_vi, tell_me_about_vi, play_youtube_vi, read_news_vi
    from module_en import get_text_en, speak_en, get_voice_en, stop_en, talk_en, get_time_en, change_wallpaper_en, open_website_en, \
        open_application_en, open_google_and_search_en, tell_me_about_en, play_youtube_en, read_news_en
    def clear_text(self):
        self.uic.bot_chat.setText("")
        self.uic.me_chat.setText("")

    def call_sen_en(self, name):
        self.speak_en("Hello {}! Can i help you?".format(name))
        while True:
            text_en = self.get_text_en()
            if not text_en:
                break
            elif "talk" in text_en or "conversation" in text_en:
                self.talk_en(name)
            elif "now" in text_en:
                self.get_time_en(text_en)
            elif "open" in text_en:
                self.open_application_en(text_en)
            elif "vietnamese" in text_en:
                self.speak_vi("Vâng tôi có thể nói tiếng Việt!")
                time.sleep(1)
                self.call_sen_vi1(name)
                break
            elif "desktop" in text_en or "change" in text_en:
                self.change_wallpaper_en()
            elif "access" in text_en:
                self.open_website_en()
            elif "search" in text_en:
                self.open_google_and_search_en()
            elif "define" in text_en:
                self.tell_me_about_en()
            elif "youtube" in text_en:
                self.play_youtube_en()
            elif "read" in text_en:
                self.read_news_en()
            elif "off" in text_en:
                self.speak_en("Goodbye {}, see you again!".format(name))
                time.sleep(1)
                sys.exit(app.exec_())
            elif "stop" in text_en or "goodbye" in text_en:
                self.stop_en()
                break
            else:
                self.speak_en("I don't have this function")

    def call_sen_vi(self):
        self.speak_vi("Chào bạn! Tôi là trợ lý ảo của bạn! Bạn tên là gì?")
        name = self.get_text_vi()
        if name:
            self.speak_vi("Chào {}! Bạn cần tôi giúp gì?".format(name))
            while True:
                text_vi = self.get_text_vi()
                if not text_vi:
                    break
                elif "chuyện" in text_vi:
                    self.talk_vi(name)
                elif "hiện tại" in text_vi:
                    self.get_time_vi(text_vi)
                elif "mở" in text_vi:
                    self.open_application_vi(text_vi)
                elif "truy cập" in text_vi:
                    self.open_website_vi(text_vi)
                    time.sleep(10)
                elif "tìm kiếm" in text_vi:
                    self.open_google_and_search_vi(text_vi)
                    time.sleep(10)
                elif "youtube" in text_vi:
                    self.play_youtube_vi()
                elif "định nghĩa" in text_vi:
                    self.tell_me_about_vi()
                elif "đổi" in text_vi:
                    self.change_wallpaper_vi()
                elif "đọc" in text_vi:
                    self.read_news_vi()
                elif "tiếng anh" in text_vi:
                    self.speak_en("Yes, I can speak English!")
                    time.sleep(1)
                    self.call_sen_en(name)
                    break
                elif "tắt" in text_vi:
                    self.speak_vi("Tạm biệt {}, hẹn gặp lại sau nhé!".format(name))
                    time.sleep(1)
                    sys.exit(app.exec_())
                elif "dừng" in text_vi:
                    self.stop_vi()
                    break
                else:
                    self.speak_vi("Tôi không có chức năng này!")

    def call_sen_vi1(self, name):
        self.speak_vi("Chào {}! Bạn cần tôi giúp gì?".format(name))
        while True:
            text_vi = self.get_text_vi()
            if not text_vi:
                break
            elif "chuyện" in text_vi:
                self.talk_vi(name)
            elif "giờ" in text_vi:
                self.get_time_vi(text_vi)
            elif "mở" in text_vi:
                self.open_application_vi(text_vi)
            elif "truy cập" in text_vi:
                self.open_website_vi(text_vi)
                time.sleep(10)
            elif "tìm kiếm" in text_vi:
                self.open_google_and_search_vi(text_vi)
                time.sleep(10)
            elif "youtube" in text_vi:
                self.play_youtube_vi()
            elif "định nghĩa" in text_vi:
                self.tell_me_about_vi()
            elif "đọc" in text_vi:
                self.read_news_vi()
            elif "tiếng anh" in text_vi:
                self.speak_en("Yes, I can speak English!")
                time.sleep(1)
                self.call_sen_en(name)
                break
            elif "tắt" in text_vi:
                self.speak_vi("Tạm biệt {}, Hẹn gặp lại sau nhé!".format(name))
                time.sleep(1)
                sys.exit(app.exec_())
            elif "đổi" in text_vi:
                self.change_wallpaper_vi()
            elif "dừng" in text_vi or "thôi" in text_vi or "tạm biệt" in text_vi:
                self.stop_vi()
                break
            else:
                self.speak_vi("Tôi không có chức năng này!")

    def call_sen_en1(self):
        self.speak_en("Hello ! I'm your virtual assistant! What is your name?")
        name = self.get_text_en()
        if name:
            self.speak_en("Hello {}!".format(name))
            self.speak_en("Can I help you?")
            time.sleep(1)
            while True:
                text_en = self.get_text_en()
                if not text_en:
                    break
                elif "talk" in text_en or "conversation" in text_en:
                    self.talk_en(name)
                elif "now" in text_en:
                    self.get_time_en(text_en)
                elif "open" in text_en:
                    self.open_application_en(text_en)
                elif "vietnamese" in text_en:
                    self.speak_vi("Vâng tôi có thể nói tiếng Việt!")
                    self.call_sen_vi1(name)
                    break
                elif "desktop" in text_en or "change" in text_en:
                    self.change_wallpaper_en()
                elif "access" in text_en:
                    self.open_website_en()
                elif "search" in text_en:
                    self.open_google_and_search_en()
                elif "define" in text_en:
                    self.tell_me_about_en()
                elif "youtube" in text_en:
                    self.play_youtube_en()
                elif "read" in text_en:
                    self.read_news_en()
                elif "off" in text_en:
                    self.speak_en("Goodbye {}, see you again!".format(name))
                    time.sleep(1)
                    sys.exit(app.exec_())
                elif "stop" in text_en or "goodbye" in text_en:
                    self.stop_en()
                    break
                else:
                    self.speak_en("I don't have this function")

    def show(self):
        self.main_win.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())