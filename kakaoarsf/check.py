from konlpy.tag import Mecab
mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")
def mecab_ch(string):
    tokens_ko = mecab.pos(string)
    return [str(pos[0]) + '/' + str(pos[1]) for pos in tokens_ko]