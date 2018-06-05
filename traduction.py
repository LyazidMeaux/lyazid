#!/usr/bin/env python
# -*- coding: latin-1 -*-

import android
import urllib2

droid = android.Android()

def translate(to_translate, to_langage="auto", langage="auto"):
 '''Return the translation using google translate
 you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
 if you don't define anything it will detect it or use english by default
 Example:
 print(translate("salut tu vas bien?", "en"))
 hello you alright?'''
 agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
 before_trans = 'class="t0">'
 link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
 request = urllib2.Request(link, headers=agents)
 page = urllib2.urlopen(request).read()
 result = page[page.find(before_trans)+len(before_trans):]
 result = result.split("<")[0]
 return result

def main():
 texte = droid.dialogGetInput('pyTranslate', 'to translate:', '').result
 to = droid.dialogGetInput('To which langage?', 'fr/en/es/de ...', 'fr').result
 droid.dialogCreateSpinnerProgress(None, None, 100)
 droid.dialogShow()
 try:
  trans = translate(texte, to)
  droid.setClipboard(trans)
  droid.makeToast('Copied to clipboard')
  droid.dialogCreateAlert('Translation:', trans)
  droid.ttsSpeak(trans)
 except urllib2.URLError:
  droid.dialogCreateAlert('Error', 'Connection issue')
 droid.dialogShow()

if __name__ == '__main__':
 main()