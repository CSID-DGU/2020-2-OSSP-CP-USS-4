from konlpy.tag import Mecab
mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")
print(mecab.morphs("아버지가방에들어가신다"))
