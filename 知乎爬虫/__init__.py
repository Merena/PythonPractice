#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import sys
import re

class zhihuSpider(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.homePageUrl = 'https://www.zhihu.com/'
        self.topic = 'JAVA'
        self.startUrl = 'https://www.zhihu.com/search?q=' + self.topic + '&type=topic'
        self.topicUrl = ''
        self.account = 'xxx'
        self.password = 'xxx'
        self.times = 0
        self.QueTitle = []
        self.QueFirstAns = []
        self.QueUrl = []
        self.QueDic = {
            'url': self.QueUrl,
            'title': self.QueTitle,
            'author': self.QueFirstAns
        }
        self.Ans = []

    def login(self):
        try:
            self.driver.get(self.homePageUrl)
            self.driver.find_element_by_name('username').send_keys(self.account)
            time.sleep(1)
            self.driver.find_element_by_name('password').send_keys(self.password)
            time.sleep(1)
            self.driver.find_element_by_class_name('SignFlow-submitButton').click()
            time.sleep(1)
        except:
            print('login error!:(')
            sys.exit(-1)

    def _getTopicPage(self, url=None):
        try:
            self.driver.get(url)
            return self.driver.page_source
        except:
            print('get topic failed!:(')
            sys.exit(-1)

    def _getTopicUrl(self, html=None):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            tag = soup.find('a', attrs={'class': 'TopicLink', 'target': '_blank'})
            url = 'https://www.zhihu.com' + tag.get('href')
            return url
        except:
            print('没有这个话题!请重新输入话题，启动爬虫!')
            sys.exit(-1)

    def _getTopicHtml(self, url=None):
        try:
            self.driver.get(url)
            self._windowScroll(self.times)
            return self.driver.page_source
        except:
            print('get question Html error!:(')
            return ""

    def _getQuestionInfo(self, html=None):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            queTag = soup.find_all('a', attrs={'class': 'question_link'})
            queFirstAnsTag = soup.find_all('a', attrs={'class': 'author-link'})
            for i in range(len(queTag)):
                try:
                    self.QueUrl.append(re.sub('\n', '', 'https://www.zhihu.com' + queTag[i]['href']))
                    self.QueTitle.append(re.sub('\n', '', queTag[i].string))
                    self.QueFirstAns.append(re.sub('\n', '', queFirstAnsTag[i].string))
                except:
                    continue
        except:
            print('get question url error!:(')
            sys.exit(-1)

    def _windowScroll(self, times):
        for i in range(times + 1):
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)

    def _saveQuestion(self):
        k = 1
        with open('question.txt', 'w', encoding='utf-8') as f:
            for i in range(len(self.QueUrl)):
                try:
                    f.write(str(k) + '\t' + '标题:' + str(self.QueTitle[i]) + '\n' +
                            '\t' + '回答者:' + str(self.QueFirstAns[i]) + '\n' +
                            '\t' + 'url:' + str(self.QueUrl[i]))
                    f.write('\n')
                    k = k + 1
                except:
                    continue

    def getQuestion(self):
        topichtml = self._getTopicPage(self.startUrl)
        self.topicUrl = self._getTopicUrl(topichtml)
        quehtml = self._getTopicHtml(self.topicUrl)
        self._getQuestionInfo(quehtml)
        self._saveQuestion()

    def _getAnswerHtml(self, url=None):
        try:
            self.driver.get(url)
            try:
                self.driver.find_element_by_class_name('QuestionRichText-more').click()
                time.sleep(1)
            except:
                pass
            self._windowScroll(self.times)
            return self.driver.page_source
        except:
            print('get answer html failed!:(')
            return ""

    def _getAnswerInfo(self, html=None):
        ansInfo = AnsPage(html)
        ansInfo.getAnsInfoDic()
        ansDic = ansInfo.ansInfoDic
        return ansDic

    def _saveAns(self, infoDic=None, i=0):
        fpath = './answer/answer' + str(i+1) + '.txt'
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write('问题 ' + str(i+1) + '\n')
            f.write('问题标题:' + '\t' + str(self.QueTitle[i]) + '\n')
            f.write('关注者:' + '\t' + str(infoDic['noticerNum'] + '\t' + '被浏览:' + '\t' + str(infoDic['lookNum']) + '\n'))
            f.write('问题描述:' + '\t' + str(infoDic['queDis']) + '\n\n')
            for j in range(len(infoDic['ansAuthor'])):
                try:
                    f.write('回答者' + str(j+1) + ':' + '\t' + str(infoDic['ansAuthor'][j]) + '\n')
                    f.write('点赞数:' + '\t\t' + str(infoDic['ansPraise'][j]) + '\n')
                    f.write('回答内容:' + '\t' + str(infoDic['ansText'][j]) + '\n\n')
                except:
                    continue

    def getAnswer(self):
        index = 0
        for url in self.QueUrl:
            html = self._getAnswerHtml(url)
            ansInfoDic = self._getAnswerInfo(html)
            self.Ans.append(ansInfoDic)
            self._saveAns(ansInfoDic, index)
            index = index + 1

    def stopSpider(self):
        print('Spider end!')
        sys.exit(-1)

    def runSpider(self):
        self.login()
        self.getQuestion()
        self.getAnswer()


class AnsPage(object):
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.queDis = ''
        self.noticerNum = ''
        self.lookNum = ''
        self.ansAuthor = []
        self.ansPraise = []
        self.ansText = []
        self.ansInfoDic = {
            'queDis': self.queDis,
            'noticerNum': self.noticerNum,
            'lookNum': self.lookNum,
            'ansAuthor': self.ansAuthor,
            'ansPraise': self.ansPraise,
            'ansText': self.ansText
        }

    def _getQueDiscribe(self):
        try:
            queDis = ''
            queDisTag = self.soup.find('span', attrs={'class': 'RichText', 'itemprop': 'text'})
            if queDisTag.get('class') == ['RichText']:
                for i in queDisTag.strings:
                    queDis = queDis + i
            else:
                queDis = None
            return queDis
        except:
            print('get question discription failed!')
            return None

    def _getNoticerAndLookNum(self):
        num = []
        try:
            Tag = self.soup.find_all('strong', attrs={'class': 'NumberBoard-itemValue'})
            for elem in Tag:
                num.append(elem.get('title'))
            return num
        except:
            num.append(None)
            num.append(None)
            return num

    def _getAnswerer(self):
        try:
            authorPic = self.soup.find_all('img', attrs={'class': ['Avatar', 'AuthorInfo-avatar'],
                                                         'width': '38', 'height': '38'})
            author = []
            for elem in authorPic:
                author.append(elem.get('alt'))
            return author
        except:
            print('get answerer failed!:(')
            return None

    def _getAnsPraise(self):
        try:
            praiseTag = self.soup.find_all('button', attrs={
                'class': ['Button', 'VoteButton', 'VoteButton--up'], 'aria-label': '赞同'})
            praiseNum = []
            for elem in praiseTag:
                try:
                    for string in elem.strings:
                        praiseNum.append(string)
                except:
                    continue
            return praiseNum
        except:
            print('get praise number failed!:(')
            return None

    def _getAnsText(self):
        try:
            ansTextTag = self.soup.find_all('span', attrs={'class': ['RichText', 'CopyrightRichText-richText'],
                                                      'itemprop': 'text'})
            ansTextTag = [elem for elem in ansTextTag
                          if elem.get('class') == ['RichText', 'CopyrightRichText-richText']]
            ansText = []
            tempText = ''
            for i in range(len(ansTextTag)):
                try:
                    try:
                        while True:
                            ansTextTag[i].figure.decompose()
                    except:
                        for child_str in ansTextTag[i].strings:
                            tempText = tempText + child_str
                        ansText.append(tempText)
                        tempText = ''
                except:
                    continue
            return ansText
        except:
            print('get answer text failed!:(')
            return None

    def getAnsInfoDic(self):
        num = self._getNoticerAndLookNum()
        self.queDis = self._getQueDiscribe()
        self.noticerNum = num[0]
        self.lookNum = num[1]
        self.ansAuthor = self._getAnswerer()
        self.ansPraise = self._getAnsPraise()
        self.ansText = self._getAnsText()
        self.ansInfoDic = {
            'queDis': self.queDis,
            'noticerNum': self.noticerNum,
            'lookNum': self.lookNum,
            'ansAuthor': self.ansAuthor,
            'ansPraise': self.ansPraise,
            'ansText': self.ansText
        }


if __name__ == '__main__':
    zhihu = zhihuSpider()
    zhihu.runSpider()
    print(len(zhihu.QueUrl))