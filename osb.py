import os
import sys
import shutil

def main():
    ev = "Events & Organizations"
    soft = "Softball"
    milb = "Minor League Baseball"
    golf = "Golf"
    soc = "Soccer"
    uni = "College"
    mlb = "MLB"
    hock = "Hockey"
    nfl = "NFL"
    nba = "NBA"
    hs = "High School"
    og = "Organizations"
    namesonly = {ev, milb, uni, hs, og, soc}
    root = "Z:/Marketing_Iconik/Graphics/Assets/Sports Logos/"
    args = [
        ["{1AFDCA30-B717-4865-AEBD-7536031A203E}", "fort gibson", "tigers", hs],
        ["{36DFF14C-3EB6-44D1-A2D7-E21909A5DA50}", "tonkawa", "buccaneers", hs],
        ["{81E6E2B9-898F-4255-806C-DA151465500A}", "preston", "", hs],
        ["east_central", "east central", "", uni],
        ["cordell_blue_devils", "cordell", "blue devils", uni],
        ["{4B49041A-449F-4D75-9F36-6E7668479880}", "stillwell", "indians", hs],
        ["{1E34EF67-29E4-4F6E-BAF6-8860B46A83E7}", "mannford", "pirates", hs],
        ["{69EE053B-179E-42A8-B328-1122CB5CE8CE}", "del city", "", hs],
        ["{413F56B5-93FD-4FA9-9463-A97B4CA5C494}", "florida gulf coast university", "", uni],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["chl_playoffs", "ChL Playoffs", "", ev],
        ["denver_cutthroats", "denver", "cutthroats", hock],
        ["baltimore_ravens_2", "baltimore", "ravens", nfl],
        ["{C87630F6-B39A-402E-ADC2-A1DFE99BECD7}", "dewey", "bulldoggers", hs],
        ["{FE0AAABA-0858-4F11-AB33-5B2C7E20C7DF}", "bethany", "", hs],
        ["{033D2E75-8DEB-448E-9E10-BE13BF029262}", "elgin", "", hs],
        ["{9534B3CC-757C-4ECA-AEFC-38A31498B436}", "marlow", "", hs],
        ["{7DA830DC-ECA0-4992-B8C5-FBB3331826CC}", "checotah", "", hs],
        ["{A01CD9B9-3D0B-44A1-87C8-C9C4F5A43EEE}", "chandler", "", hs],
        ["{0041FE8E-95E7-4C59-B254-F79AC35BC3CB}", "jones", "", hs],
        ["{8A307FD2-E092-441E-8D7C-5C5898BA55EF}", "kansas city", "", hs],
        ["san_antonio_spurs_logo", "san antonio", "spurs", nba],
        ["{D940BC17-BFD2-438F-8772-2357CA3132E6}", "tuttle", "tigers", hs],
        ["dale_high_school_pirate_logo_osb", "dale", "pirates2", hs],
        ["{65CE42F9-D443-4DB0-9486-1101BC986239}", "glenpool", "warriors", hs],
        ["charlotte_hornets_logo", "charlotte", "hornets", mlb],
        ["{D40F67E3-E41C-4B1A-B624-BBAC1CB21E0C}", "cleveland", "indians", mlb],
        ["{A747B1E1-0258-47C0-BECB-FD7597BC2C7A}", "cf monterrey", "", soc],
        ["pittsburg_pirates_n", "pittsburgh", "pirates", mlb],
        ["anaheim_ducks", "annaheim", "ducks", hock],
        ["minnesota_wild", "minnesota", "wild", hock],
        ["colorado_avalanche", "colorado", "avalanche", hock],
        ["montreal_canadiens", "montreal", "canadians", hock],
        ["san_jose_sharks", "san jose", "sharks", hock],
        ["tampa_bay_lightning", "tampa bay", "tighning", hock],
        ["boston_bruins", "boston", "bruins", hock],
        ["lakers", "los angeles", "lakers", nba],
        ["la_tech", "louisiana tech", "bulldogs", uni],
        ["missouri_state", "missouri state", "", uni],
        ["n_dakota_state_bison", "north dekota state", "bison", uni],
        ["buffalo_bills", "buffalo", "bills", nfl],
        ["philadelphia_eagles", "philadelphia", "eagles", nfl],
        ["{337312F7-69E4-4ACC-80E3-26B214D10539}", "fort hays state", "tigers", uni],
        ["{81745ECA-70F0-4340-81AD-1E1A17573B3A}", "alva", "goldbugs", hs],
        ["louisville_university_cardinals_logo", "louisville university", "cardinals", uni],
        ["michigan_state_spartans_logo", "michigan state", "spartans", uni]]
    

    for argv in args:
        name = argv[0] + ".png"
        place = argv[1].upper()
        mascot = argv[2].title()
        org = argv[3]

        if not os.path.exists(f"{root}Orig/{name}"):
            print(f"Files for {place} {mascot} do not exist")
            continue
        elif (os.path.exists(f"{root}{org}/{place}/OSB_{place} {mascot}.png") or
            os.path.exists(f"{root}{org}/{place}/{place} {mascot} Logo.png") or
            os.path.exists(f"{root}{org}/{place}/OSB_{place}.png") or
            os.path.exists(f"{root}{org}/{place}/{place} Logo.png")):
            print(f"files for {place} {mascot} already exist, skipping")
            continue
        if os.path.exists(f"{root}{org}/{place}"):
            print(f"Path already exists: {name} / {org} {place} {mascot}, continuing")
        elif org in (namesonly):
            if argv[2]:
                if os.path.exists(f"{root}{org}/{place}"):
                    print(f"Path already exists: {name} / {org} {place} {mascot}, continuing")
                else:
                    os.mkdir(f"{root}{org}/{place}")
                shutil.move(f"{root}Orig/{name}", f"{root}{org}/{place}/OSB_{place} {mascot}.png")
                shutil.move(f"{root}Conv/{name}", f"{root}{org}/{place}/{place} {mascot} Logo.png")
            else:
                if os.path.exists(f"{root}{org}/{place}"):
                    print(f"Path already exists: {name} / {org} {place} {mascot}, continuing")
                else:
                    os.mkdir(f"{root}{org}/{place}")
                shutil.move(f"{root}Orig/{name}", f"{root}{org}/{place}/OSB_{place}.png")
                shutil.move(f"{root}Conv/{name}", f"{root}{org}/{place}/{place} Logo.png")                
        else:
            if os.path.exists(f"{root}{org}/{place}"):
                print(f"Path already exists: {name} / {org} {place} {mascot}, continuing")
            else:
                os.mkdir(f"{root}{org}/{place}")
            shutil.move(f"{root}Orig/{name}", f"{root}{org}/{place} {mascot}/OSB_{place} {mascot}.png")
            shutil.move(f"{root}Conv/{name}", f"{root}{org}/{place} {mascot}/{place} {mascot} Logo.png")

if __name__ == "__main__":
    main()