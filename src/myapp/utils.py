c='АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщьЮюЯя'
l=('A','a','B','b','V','v','H','h','G','g','D','d','E','e','Ye','ie',
'Zh','zh','Z','z','Y','y','I','i','Yi','i','Y','i','K','k','L','l',
'M','m','N','n','O','o','P','p','R','r','S','s','T','t','U','u',
'F','f','Kh','kh','Ts','ts','Ch','ch','Sh','sh','Shch','shch','',
'Yu','iu','Ya','ia')
cyr = dict(zip(c, l))

def text_lat(text_cyr: str):
    text_cyr = text_cyr.replace('_','').lower()
    text_lat = ''
    for i in text_cyr:
        text_lat += cyr.get(i, i)
    return text_lat
