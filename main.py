from classes import *

def month_eng(month):
    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if month:
        return months[month]
    else:
        return None

def print_in_format(pub):
    jnl = pub.jnl.get_name(pub.year) if pub.jnl else None
    conf = "{} ({})".format(pub.conf.get_name(pub.year),pub.conf.get_name_abbr(pub.year)) if pub.conf else None
    page = "pp.{}-{}".format(pub.page_from,pub.page_to) if pub.page_from and pub.page_to else None
    strAll = ", ".join(filter(None, [
                pub.authors,
                '"{}"'.format(pub.title),
                jnl,
                conf,
                page,
                pub.city,
                pub.state,
                pub.country,
                month_eng(pub.month),
                str(pub.year),
            ])) + "."
    if pub.note:
        return "{}  {}".format(strAll, pub.note)
    else:
        return strAll

pe = Person()

categories = [
    Category(name="Journal",                   key="journal",   abbr="J"),
    Category(name="International Conferences", key="intl_conf", abbr="I"),
    Category(name="Domestic Conferences",      key="dmst_conf", abbr="D")
]

jnls = {
    "hcj":     Journal(name="Human Computation",
               ),
}

confs = {
    "cscw":    Conference(name="In Proc. of the {ord} ACM Conference on Computer-Supported Cooperative Work and Social Computing",
                          name_abbr="ACM CSCW {year}",
                          year_found=1998
               ),
    "icdsc":   Conference(name="In Proc. of the {ord} International Conference on Distributed Smart Cameras",
                          name_abbr="ICDSC '{year_lasttwo}",
                          year_found=2007
               ),
    "trecvid": Conference(name="In notebook paper of the TRECVID {year} workshop"
               ),
    "hcomp":   Conference(name="In Proc. of the {ord} AAAI Conference on Human Computation and Crowdsourcing",
                          name_abbr="AAAI HCOMP {year}",
                          year_found=2013
               ),
    "www":     Conference(name="In Proc. of The Web Conference {year}",
                          name_abbr="WWW '{year_lasttwo}"
               ),
    "ecplf":   Conference(name="In Proc. of the European Conference on Precision Livestock Farming {year}",
                          name_abbr="ECPLF {year}"
               ),
}

pubsAll = {
    "journal": [
        Publication(authors=[pe.susumu, pe.chun, pe.saiph, pe.nakano, pe.koba, pe.jeff],
                    title="Predicting the Working Time of Microtasks Based on Workers' Perception of Prediction Errors",
                    jnl=jnls["hcj"],
                    year=2019,
                    month=12,
                    page_from=192,
                    page_to=219,
        )
    ],
    "intl_conf": [
        Publication(authors=[pe.susumu, pe.nakano, pe.koba],
                    title="Towards a framework for collaborative video surveillance system using crowdsourcing",
                    conf=confs["cscw"],
                    year=2016,
                    month=2,
                    #day=29,
                    page_from=393,
                    page_to=396,
                    city="San Francisco",
                    state="CA",
                    country="USA",
        ),
        Publication(authors=[pe.susumu, pe.nakano, pe.akabane, pe.koba],
                    title="Evaluation of Collaborative Video Surveillance Platform: Prototype Development of Abandoned Object Detection",
                    conf=confs["icdsc"],
                    year=2016,
                    page_from=172,
                    page_to=177,
                    city="Paris",
                    country="France",
        ),
        Publication(authors=[pe.ueki, pe.kikuchi, pe.susumu, pe.koba],
                    title="Waseda at TRECVID 2016: Fully-automatic Ad-hoc Video Search",
                    conf=confs["trecvid"],
                    year=2016,
                    month=11,
                    #day=14,
                    city="Gaithersburg",
                    state="MD",
                    country="USA",
        ),
        Publication(authors=[pe.toni+"*", pe.susumu+"*", pe.kotaro, pe.jeff],
                    title="Striving to Earn More: A Survey of Work Strategies and Tool Use Among Crowd Worker",
                    conf=confs["hcomp"],
                    year=2018,
                    month=7,
                    page_from=70,
                    page_to=78,
                    city="Zurich",
                    country="Switzerland",
                    note="(* Equal contribution)",
        ),
        Publication(authors=[pe.susumu, pe.chun, pe.saiph, pe.nakano, pe.koba, pe.jeff],
                    title="TurkScanner: Predicting the Hourly Wage of Microtasks",
                    conf=confs["www"],
                    year=2019,
                    month=5,
                    page_from=3187,
                    page_to=3193,
                    city="San Francisco",
                    state="CA",
                    country="USA",
                    note="[Best Poster Honourable Mention (0.8%)]"
        ),
        Publication(authors=["Kazuma Sugawara", pe.susumu, pe.nakano, pe.akabane, pe.koba, pe.ogawa],
                    title="Calving prediction from video: Exploiting behavioral information relevant to calving signs in Japanese black beef cows",
                    conf=confs["ecplf"],
                    year=2019,
                    month=8,
                    page_from=663,
                    page_to=669,
                    city="Cork",
                    country="Ireland",
        ),
        Publication(authors=["Ryosuke Hyodo", "Saki Yasuda", "Yusuke Okimoto", pe.susumu, pe.nakano, pe.akabane, pe.koba, pe.ogawa],
                    title="Two-stage calving prediction system: Exploiting state-based information relevant to calving signs in Japanese black beef cows",
                    conf=confs["ecplf"],
                    year=2019,
                    month=8,
                    page_from=670,
                    page_to=676,
                    city="Cork",
                    country="Ireland",
        ),
        Publication(authors=[pe.susumu, pe.nakano, pe.koba, pe.jeff],
                    title="MicroLapse: Measuring Workers' Leniency To Prediction Errors of Microtasks' Working Times",
                    conf=confs["cscw"],
                    year=2019,
                    month=11,
                    page_from=352,
                    page_to=356,
                    city="Austin",
                    state="TX",
                    country="USA",
        ),
        Publication(authors=[pe.saiph, pe.chun, pe.susumu, "Carlos Toxtli", pe.jeff],
                    title="Increasing Wages via a Strategy from High Earning Workers",
                    conf=confs["www"],
                    year=2020,
                    city="Taipei",
                    country="Taiwan",
        ),
    ],
    "dmst_conf": [
    ]
}

if __name__=="__main__":
    for c in categories:
        key = c.key
        name = c.name
        abbr = c.abbr
        print(name)
        pubStr = ""
        for i,p in enumerate(pubsAll[key]):
            #pubStr = "[{}-{}]  {}\n".format(abbr, i+1, print_in_format(p)) + pubStr
            #pubStr = "[{}-{}]\n".format(abbr, i+1) + pubStr
            pubStr = "{}\n".format(print_in_format(p)) + pubStr
        print(pubStr)
