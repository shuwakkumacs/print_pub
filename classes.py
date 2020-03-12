class Person():
    def __init__(self):
        self.susumu  = "Susumu Saito"
        self.jeff    = "Jeffrey P. Bigham"
        self.koba    = "Tetsunori Kobayashi"
        self.nakano  = "Teppei Nakano"
        self.akabane = "Makoto Akabane"
        self.ogawa   = "Tetsuji Ogawa"
        self.saiph   = "Saiph Savage"
        self.chun    = "Chun-Wei Chiang"
        self.toni    = "Toni Kaplan"
        self.kotaro  = "Kotaro Hara"
        self.ueki    = "Kazuya Ueki"
        self.kikuchi = "Kotaro Kikuchi"

class Category():
    def __init__(self, name, key, abbr):
        self.name = name
        self.key = key
        self.abbr = abbr

class Journal():
    def __init__(self, name, name_abbr=None):
        self.name = name
        self.name_abbr = name_abbr

    def _get_format_kws(self,year):
        format_kws = {
            "year": year,
            "year_lasttwo": str(year)[-2:]
        }
        #if self.year_found:
        #    format_kws["ord"] = self._ord(year-self.year_found+1)
        return format_kws

    def get_name(self, year):
        return self.name.format(**self._get_format_kws(year))

    def get_name_abbr(self, year):
        if self.name_abbr:
            return self.name_abbr.format(**self._get_format_kws(year))
        else:
            return self.name.format(**self._get_format_kws(year))


class Conference():
    def __init__(self, name, name_abbr=None, year_found=None):
        self.year_found = year_found
        self.name = name
        self.name_abbr = name_abbr

    def _get_format_kws(self,year):
        format_kws = {
            "year": year,
            "year_lasttwo": str(year)[-2:]
        }
        if self.year_found:
            format_kws["ord"] = self._ord(year-self.year_found+1)
        return format_kws

    def _ord(self,num):
        if (num<=10 and num>=14) and (num%10>=1 and num%10<=3):
            if num%10==1:
                suffix = "st"
            elif num%10==2:
                suffix = "nd"
            elif num%10==3:
                suffix = "rd"
        else:
            suffix = "th"
        return str(num) + suffix

    def get_name(self, year):
        return self.name.format(**self._get_format_kws(year))

    def get_name_abbr(self, year):
        if self.name_abbr:
            return self.name_abbr.format(**self._get_format_kws(year))
        else:
            return self.name.format(**self._get_format_kws(year))

class Publication():
    def __init__(self, **kwargs):
        possible_kws = ["authors","title","jnl","conf","year","month","page_from","page_to","city","state","country","note"]

        authors = kwargs["authors"]
        if len(kwargs["authors"])>1:
            kwargs["authors"] = ", ".join(authors[:-1]+["and "+authors[-1]])
        else:
            kwargs["authors"] = authors[0]
        self.__dict__.update(kwargs)
        for kw in possible_kws:
            if kw not in self.__dict__:
                self.__dict__[kw] = None
