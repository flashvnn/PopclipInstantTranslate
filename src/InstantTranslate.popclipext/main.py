# coding=utf-8
import os, urllib2

LANG_CODES = {
    "Arabic": "ar",
    "Bosnian (Latin)": "bs-Latn",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Chinese Simplified": "zh-CHS",
    "Chinese Traditional": "zh-CHT",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Estonian": "et",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Haitian Creole": "ht",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hmong Daw": "mww",
    "Hungarian": "hu",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Klingon": "tlh",
    "Klingon (pIqaD)": "tlh-Qaak",
    "Korean": "ko",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Malay": "ms",
    "Maltese": "mt",
    "Norwegian": "no",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Querétaro Otomi": "otq",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian (Cyrillic)": "sr-Cyrl",
    "Serbian (Latin)": "sr-Latn",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Spanish": "es",
    "Swedish": "sv",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Yucatec Maya": "yua"
}

def translate(to_translate, to_langage="auto", langage="auto"):
	'''Return the translation using google translate
	you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
	if you don't define anything it will detect it or use english by default
	Example:
	print(translate("salut tu vas bien?", "en"))
	hello you alright?'''
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	before_trans = 'result-container">'
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	return result

print translate(os.environ['POPCLIP_TEXT'], LANG_CODES[os.environ['POPCLIP_OPTION_DESTLANG']], "auto");
