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
    root = "/mnt/Lucid/Marketing_Iconik/Graphics/Assets/Sports Logos/"
    args = [
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
        ["tulsa_oilers", "tulsa", "oilers", hock],
    

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