from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
import os
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from youtube_search import YoutubeSearch
import pyttsx3

path = ChromeDriverManager().install()