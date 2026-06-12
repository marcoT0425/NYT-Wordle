def play_wordle_generated():
    print("--- Wordle ---")
    current_guess = "TARSE"

    while True:
        print(f"Current Guess: {current_guess}")
        feedback = input(f"Enter feedback for {current_guess}: ").strip().lower()
        if feedback == "ggggg":
            print(f"SOLVED! Word is {current_guess}")
            return

        if current_guess == "AARGH":
            if feedback == "gyy__":
                current_guess = "AWARD"
            elif feedback == "y_y__":
                current_guess = "FRAUD"
            elif feedback == "y_y_y":
                current_guess = "CHARD"
            elif feedback == "y_yy_":
                current_guess = "GUARD"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABACK":
            if feedback == "__g__":
                current_guess = "GLAND"
            elif feedback == "__g_g":
                current_guess = "FLANK"
            elif feedback == "_yg__":
                current_guess = "BLAND"
            elif feedback == "_yg_g":
                current_guess = "BLANK"
            elif feedback == "g____":
                current_guess = "ANNUL"
            elif feedback == "g_y__":
                current_guess = "ANNAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABACS":
            if feedback == "__g_g":
                current_guess = "GRASS"
            elif feedback == "__g_y":
                current_guess = "GRASP"
            elif feedback == "__gyg":
                current_guess = "CRASS"
            elif feedback == "__gyy":
                current_guess = "CRASH"
            elif feedback == "_yg_g":
                current_guess = "BRASS"
            elif feedback == "_yg_y":
                current_guess = "BRASH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABAFT":
            if feedback == "_____":
                current_guess = "PLUSH"
            elif feedback == "___y_":
                current_guess = "FLUSH"
            elif feedback == "_y___":
                current_guess = "BLUSH"
            elif feedback == "g__gg":
                current_guess = "ALOFT"
            elif feedback == "y___g":
                current_guess = "GLOAT"
            elif feedback == "y___y":
                current_guess = "TATTY"
            elif feedback == "y__gy":
                current_guess = "TAFFY"
            elif feedback == "y__yg":
                current_guess = "FLOAT"
            elif feedback == "yy__g":
                current_guess = "BLOAT"
            elif feedback == "yy__y":
                current_guess = "TABBY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABETS":
            if feedback == "___g_":
                current_guess = "TUFTY"
            elif feedback == "___y_":
                current_guess = "TUMMY"
            elif feedback == "_y_y_":
                current_guess = "TUBBY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABHOR":
            if feedback == "_____":
                current_guess = "MUGGY"
            elif feedback == "___y_":
                current_guess = "FUNGO"
            elif feedback == "__y__":
                current_guess = "HUGGY"
            elif feedback == "_y___":
                current_guess = "BUGGY"
            elif feedback == "gy_gg":
                current_guess = "ARBOR"
            elif feedback == "yy_yy":
                current_guess = "COBRA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABIDE":
            if feedback == "gg_gg":
                current_guess = "ABODE"
            elif feedback == "gy_yg":
                current_guess = "ADOBE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABJUD":
            if feedback == "g____":
                current_guess = "AVAIL"
            elif feedback == "y____":
                current_guess = "FLAIL"
            elif feedback == "y___g":
                current_guess = "PLAID"
            elif feedback == "y__y_":
                current_guess = "QUAIL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABLET":
            if feedback == "___y_":
                current_guess = "PROVE"
            elif feedback == "__yy_":
                current_guess = "PROLE"
            elif feedback == "_y_y_":
                current_guess = "PROBE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABLOW":
            if feedback == "__g__":
                current_guess = "FILLY"
            elif feedback == "__g_y":
                current_guess = "WILLY"
            elif feedback == "__y__":
                current_guess = "IMPLY"
            elif feedback == "_yg__":
                current_guess = "BILLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABOMA":
            if feedback == "g____":
                current_guess = "ACUTE"
            elif feedback == "g___y":
                current_guess = "AGATE"
            elif feedback == "g_g__":
                current_guess = "ATONE"
            elif feedback == "gg__y":
                current_guess = "ABATE"
            elif feedback == "y____":
                current_guess = "ELATE"
            elif feedback == "y_y__":
                current_guess = "OVATE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABOUT":
            if feedback == "g_g_g":
                current_guess = "AFOOT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABOVE":
            if feedback == "g_g_g":
                current_guess = "AWOKE"
            elif feedback == "y___g":
                current_guess = "PUPAE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ABYSM":
            if feedback == "y____":
                current_guess = "LADLE"
            elif feedback == "y___y":
                current_guess = "MAPLE"
            elif feedback == "yy___":
                current_guess = "FABLE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ACCOY":
            if feedback == "___y_":
                current_guess = "MOUTH"
            elif feedback == "___yg":
                current_guess = "POUTY"
            elif feedback == "___yy":
                current_guess = "YOUTH"
            elif feedback == "_y_y_":
                current_guess = "COUTH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ACHED":
            if feedback == "___y_":
                current_guess = "PRESS"
            elif feedback == "___yy":
                current_guess = "DRESS"
            elif feedback == "__yy_":
                current_guess = "FRESH"
            elif feedback == "_y_y_":
                current_guess = "CRESS"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ACING":
            if feedback == "y____":
                current_guess = "ORATE"
            elif feedback == "y___y":
                current_guess = "GRATE"
            elif feedback == "y_y__":
                current_guess = "IRATE"
            elif feedback == "yy___":
                current_guess = "CRATE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ACMES":
            if feedback == "_____":
                current_guess = "FOUNT"
            elif feedback == "___y_":
                current_guess = "PRIZE"
            elif feedback == "__y__":
                current_guess = "MOUNT"
            elif feedback == "__yy_":
                current_guess = "PRIME"
            elif feedback == "_y___":
                current_guess = "COUNT"
            elif feedback == "_y_y_":
                current_guess = "PRICE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ACORN":
            if feedback == "y_gyg":
                current_guess = "GROAN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ADAPT":
            if feedback == "g____":
                current_guess = "AGING"
            elif feedback == "g__y_":
                current_guess = "APING"
            elif feedback == "g_y__":
                current_guess = "ANIMA"
            elif feedback == "y____":
                current_guess = "NINJA"
            elif feedback == "yy___":
                current_guess = "KINDA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ADEEM":
            if feedback == "_____":
                current_guess = "STUCK"
            elif feedback == "____y":
                current_guess = "STUMP"
            elif feedback == "__y__":
                current_guess = "SLICE"
            elif feedback == "__y_y":
                current_guess = "SLIME"
            elif feedback == "_y___":
                current_guess = "STUDY"
            elif feedback == "_yy__":
                current_guess = "SLIDE"
            elif feedback == "y__g_":
                current_guess = "RATER"
            elif feedback == "y_yg_":
                current_guess = "EATER"
            elif feedback == "yy_g_":
                current_guess = "DATER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ADEPT":
            if feedback == "y_yyg":
                current_guess = "EXPAT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ADIOS":
            if feedback == "g___y":
                current_guess = "ASSAY"
            elif feedback == "y___y":
                current_guess = "SQUAB"
            elif feedback == "y_g_y":
                current_guess = "SHIVA"
            elif feedback == "y_y_y":
                current_guess = "SIGMA"
            elif feedback == "yy__y":
                current_guess = "SQUAD"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ADLIB":
            if feedback == "_____":
                current_guess = "GUSTY"
            elif feedback == "____y":
                current_guess = "BUSTY"
            elif feedback == "___y_":
                current_guess = "SITUP"
            elif feedback == "__y__":
                current_guess = "LUSTY"
            elif feedback == "_y___":
                current_guess = "DUSTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ADMIN":
            if feedback == "g__gg":
                current_guess = "AGAIN"
            elif feedback == "gg___":
                current_guess = "ADDER"
            elif feedback == "gy___":
                current_guess = "ALDER"
            elif feedback == "gy_y_":
                current_guess = "AIDER"
            elif feedback == "y____":
                current_guess = "PAYEE"
            elif feedback == "y__y_":
                current_guess = "WAIVE"
            elif feedback == "y__yy":
                current_guess = "NAIVE"
            elif feedback == "y_y__":
                current_guess = "MAYBE"
            elif feedback == "y_yy_":
                current_guess = "MAIZE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ADMIT":
            if feedback == "g___g":
                current_guess = "ASSET"
            elif feedback == "g__gg":
                current_guess = "AWAIT"
            elif feedback == "g_ygg":
                current_guess = "AMBIT"
            elif feedback == "gy_gg":
                current_guess = "AUDIT"
            elif feedback == "y___g":
                current_guess = "SWEAT"
            elif feedback == "y___y":
                current_guess = "STEAK"
            elif feedback == "y_y_y":
                current_guess = "STEAM"
            elif feedback == "yy__y":
                current_guess = "STEAD"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ADSUM":
            if feedback == "__gy_":
                current_guess = "HUSKY"
            elif feedback == "__gyy":
                current_guess = "MUSKY"
            elif feedback == "_ygy_":
                current_guess = "DUSKY"
            elif feedback == "_yyy_":
                current_guess = "KUDOS"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ADVEW":
            if feedback == "___g_":
                current_guess = "LONER"
            elif feedback == "___gy":
                current_guess = "LOWER"
            elif feedback == "__gg_":
                current_guess = "LOVER"
            elif feedback == "__yg_":
                current_guess = "VIPER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AERIE":
            if feedback == "gyg_g":
                current_guess = "AGREE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AFALD":
            if feedback == "g__gg":
                current_guess = "AHOLD"
            elif feedback == "g__yg":
                current_guess = "ALOUD"
            elif feedback == "g_yy_":
                current_guess = "ALOHA"
            elif feedback == "gg_y_":
                current_guess = "AFOUL"
            elif feedback == "gy_y_":
                current_guess = "ALOOF"
            elif feedback == "y__y_":
                current_guess = "GLOAM"
            elif feedback == "yg_y_":
                current_guess = "OFFAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AFFIX":
            if feedback == "g__g_":
                current_guess = "APHID"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AFFLY":
            if feedback == "y____":
                current_guess = "BEAST"
            elif feedback == "y___y":
                current_guess = "YEAST"
            elif feedback == "y__y_":
                current_guess = "LEAST"
            elif feedback == "yy___":
                current_guess = "FEAST"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AFION":
            if feedback == "__g__":
                current_guess = "PLIER"
            elif feedback == "__y__":
                current_guess = "LIVER"
            elif feedback == "__y_y":
                current_guess = "LINER"
            elif feedback == "_yg__":
                current_guess = "FLIER"
            elif feedback == "_yy__":
                current_guess = "LIFER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AFIRE":
            if feedback == "g__gg":
                current_guess = "AZURE"
            elif feedback == "gg_gg":
                current_guess = "AFORE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AFLAJ":
            if feedback == "_____":
                current_guess = "PUDGY"
            elif feedback == "____y":
                current_guess = "JUDGY"
            elif feedback == "_y___":
                current_guess = "FUDGY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AFLOW":
            if feedback == "_____":
                current_guess = "CINCH"
            elif feedback == "____y":
                current_guess = "WINCH"
            elif feedback == "_y___":
                current_guess = "FINCH"
            elif feedback == "y____":
                current_guess = "CREAK"
            elif feedback == "y___y":
                current_guess = "WREAK"
            elif feedback == "y_y__":
                current_guess = "CLEAR"
            elif feedback == "yy___":
                current_guess = "FREAK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AFOAM":
            if feedback == "y____":
                current_guess = "WALTZ"
            elif feedback == "y___y":
                current_guess = "MALTY"
            elif feedback == "y__g_":
                current_guess = "NATAL"
            elif feedback == "yy_g_":
                current_guess = "FATAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AGAPE":
            if feedback == "_yg_g":
                current_guess = "IMAGE"
            elif feedback == "_ygyg":
                current_guess = "PHAGE"
            elif feedback == "ggg_g":
                current_guess = "AGAVE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AGBAS":
            if feedback == "_____":
                current_guess = "QUILT"
            elif feedback == "__g__":
                current_guess = "CUBIT"
            elif feedback == "__y__":
                current_guess = "BUILT"
            elif feedback == "_y___":
                current_guess = "GUILT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AGING":
            if feedback == "g_ggg":
                current_guess = "AXING"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AGITA":
            if feedback == "g_gg_":
                current_guess = "AMITY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AGLEY":
            if feedback == "y__y_":
                current_guess = "RECAP"
            elif feedback == "y__yg":
                current_guess = "REPAY"
            elif feedback == "y_gy_":
                current_guess = "RELAX"
            elif feedback == "y_gyg":
                current_guess = "RELAY"
            elif feedback == "y_yy_":
                current_guess = "RENAL"
            elif feedback == "yyyy_":
                current_guess = "REGAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AGLOW":
            if feedback == "g_gg_":
                current_guess = "ALLOY"
            elif feedback == "g_ggg":
                current_guess = "ALLOW"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AGONY":
            if feedback == "g_yyg":
                current_guess = "ANNOY"
            elif feedback == "gygg_":
                current_guess = "AMONG"
            elif feedback == "yyyg_":
                current_guess = "GUANO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AGORA":
            if feedback == "g_gy_":
                current_guess = "AMOUR"
            elif feedback == "g_gyg":
                current_guess = "AROMA"
            elif feedback == "y_gy_":
                current_guess = "CROAK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AGUED":
            if feedback == "y____":
                current_guess = "SAVVY"
            elif feedback == "y_g__":
                current_guess = "SAUCY"
            elif feedback == "yy___":
                current_guess = "SAGGY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AHEAD":
            if feedback == "__ggg":
                current_guess = "KNEAD"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AHING":
            if feedback == "_____":
                current_guess = "MOOSE"
            elif feedback == "____y":
                current_guess = "GOOSE"
            elif feedback == "___y_":
                current_guess = "NOOSE"
            elif feedback == "_g___":
                current_guess = "WHOSE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AIOLI":
            if feedback == "yggg_":
                current_guess = "VIOLA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ALARM":
            if feedback == "_ggy_":
                current_guess = "FLAIR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ALERT":
            if feedback == "g_ggg":
                current_guess = "AVERT"
            elif feedback == "g_yyy":
                current_guess = "AFTER"
            elif feedback == "ggyyy":
                current_guess = "ALTER"
            elif feedback == "y_gyg":
                current_guess = "GREAT"
            elif feedback == "y_ygg":
                current_guess = "HEART"
            elif feedback == "y_ygy":
                current_guess = "EXTRA"
            elif feedback == "y_yyg":
                current_guess = "REACT"
            elif feedback == "y_yyy":
                current_guess = "RETAG"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ALIBI":
            if feedback == "gyg__":
                current_guess = "AXIAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ALIEN":
            if feedback == "gg_g_":
                current_guess = "ALLEY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ALIKE":
            if feedback == "ggg_g":
                current_guess = "ALIVE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ALLAY":
            if feedback == "__gg_":
                current_guess = "GULAG"
            elif feedback == "__ggy":
                current_guess = "BYLAW"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ALOIN":
            if feedback == "g____":
                current_guess = "ARRAY"
            elif feedback == "g__g_":
                current_guess = "ACRID"
            elif feedback == "g_y__":
                current_guess = "ARROW"
            elif feedback == "g_y_g":
                current_guess = "APRON"
            elif feedback == "gy___":
                current_guess = "AURAL"
            elif feedback == "y____":
                current_guess = "BURKA"
            elif feedback == "y___g":
                current_guess = "QURAN"
            elif feedback == "y__g_":
                current_guess = "CURIA"
            elif feedback == "y__y_":
                current_guess = "CIRCA"
            elif feedback == "y_y__":
                current_guess = "FORAY"
            elif feedback == "y_y_g":
                current_guess = "KORAN"
            elif feedback == "yy___":
                current_guess = "MURAL"
            elif feedback == "yy_y_":
                current_guess = "VIRAL"
            elif feedback == "yyy__":
                current_guess = "CORAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AMASS":
            if feedback == "_yggy":
                current_guess = "SPASM"
            elif feedback == "gg_gg":
                current_guess = "AMISS"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AMBAN":
            if feedback == "_____":
                current_guess = "GUPPY"
            elif feedback == "____y":
                current_guess = "GUNKY"
            elif feedback == "_y___":
                current_guess = "GUMMY"
            elif feedback == "_yy__":
                current_guess = "GUMBO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AMBLE":
            if feedback == "g__gg":
                current_guess = "APPLE"
            elif feedback == "gg_gg":
                current_guess = "AMPLE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AMBRY":
            if feedback == "___gg":
                current_guess = "FERRY"
            elif feedback == "___yg":
                current_guess = "JERKY"
            elif feedback == "__ygg":
                current_guess = "BERRY"
            elif feedback == "__yyg":
                current_guess = "DERBY"
            elif feedback == "_y_gg":
                current_guess = "MERRY"
            elif feedback == "_y_yg":
                current_guess = "GERMY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AMEND":
            if feedback == "yyg_y":
                current_guess = "EDEMA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AMIGO":
            if feedback == "gyg_y":
                current_guess = "AXIOM"
            elif feedback == "y_g_y":
                current_guess = "OUIJA"
            elif feedback == "y_y_y":
                current_guess = "OKAPI"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AMINO":
            if feedback == "y_ygg":
                current_guess = "PIANO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AMPED":
            if feedback == "y__y_":
                current_guess = "SHAVE"
            elif feedback == "y__yy":
                current_guess = "SHADE"
            elif feedback == "y_yy_":
                current_guess = "SHAPE"
            elif feedback == "yy_y_":
                current_guess = "SHAME"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AMPLY":
            if feedback == "g__y_":
                current_guess = "AWFUL"
            elif feedback == "g_ggg":
                current_guess = "APPLY"
            elif feedback == "g_gy_":
                current_guess = "ALPHA"
            elif feedback == "gy_y_":
                current_guess = "ALBUM"
            elif feedback == "y__g_":
                current_guess = "UVULA"
            elif feedback == "y__y_":
                current_guess = "FUGAL"
            elif feedback == "y__yg":
                current_guess = "FLAKY"
            elif feedback == "y_yy_":
                current_guess = "PLAZA"
            elif feedback == "y_yyy":
                current_guess = "PLAYA"
            elif feedback == "yy_g_":
                current_guess = "QUALM"
            elif feedback == "yy_y_":
                current_guess = "LLAMA"
            elif feedback == "yyyy_":
                current_guess = "GLAMP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AMUCK":
            if feedback == "g__gg":
                current_guess = "ABACK"
            elif feedback == "y__gg":
                current_guess = "WHACK"
            elif feedback == "y_yg_":
                current_guess = "YUCCA"
            elif feedback == "y_ygg":
                current_guess = "QUACK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ANCHO":
            if feedback == "y____":
                current_guess = "SPARE"
            elif feedback == "y__y_":
                current_guess = "SHARE"
            elif feedback == "y_y__":
                current_guess = "SCARE"
            elif feedback == "yg___":
                current_guess = "SNARE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ANGER":
            if feedback == "g_ggg":
                current_guess = "AUGER"
            elif feedback == "gy_yy":
                current_guess = "ARENA"
            elif feedback == "y__yy":
                current_guess = "OPERA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ANGRY":
            if feedback == "yg_g_":
                current_guess = "UNARM"
            elif feedback == "yy_y_":
                current_guess = "PRAWN"
            elif feedback == "yyyy_":
                current_guess = "GRAIN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ANKLE":
            if feedback == "gg_gg":
                current_guess = "ANOLE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ANNEX":
            if feedback == "g__g_":
                current_guess = "ABBEY"
            elif feedback == "g_gg_":
                current_guess = "APNEA"
            elif feedback == "yy_y_":
                current_guess = "HYENA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ANTIC":
            if feedback == "g_ggg":
                current_guess = "ATTIC"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ANVIL":
            if feedback == "y____":
                current_guess = "SABER"
            elif feedback == "y___y":
                current_guess = "LASER"
            elif feedback == "y_g__":
                current_guess = "SAVER"
            elif feedback == "yy___":
                current_guess = "SANER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AORTA":
            if feedback == "g_gyg":
                current_guess = "ATRIA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "APACE":
            if feedback == "y____":
                current_guess = "WARTY"
            elif feedback == "y_y__":
                current_guess = "KARAT"
            elif feedback == "y_yy_":
                current_guess = "CARAT"
            elif feedback == "yy___":
                current_guess = "PARTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "APAYD":
            if feedback == "y____":
                current_guess = "STRAW"
            elif feedback == "y__y_":
                current_guess = "STRAY"
            elif feedback == "yy___":
                current_guess = "STRAP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "APEEK":
            if feedback == "__g__":
                current_guess = "CHEWY"
            elif feedback == "__gy_":
                current_guess = "BEEFY"
            elif feedback == "__gyy":
                current_guess = "GEEKY"
            elif feedback == "_gy__":
                current_guess = "EPOXY"
            elif feedback == "_ygy_":
                current_guess = "WEEPY"
            elif feedback == "_yy__":
                current_guess = "PEPPY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "APHID":
            if feedback == "_____":
                current_guess = "SMELL"
            elif feedback == "__y__":
                current_guess = "SHELL"
            elif feedback == "_g___":
                current_guess = "SPELL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "APING":
            if feedback == "y____":
                current_guess = "FECAL"
            elif feedback == "y___y":
                current_guess = "LEGAL"
            elif feedback == "y__y_":
                current_guess = "VENAL"
            elif feedback == "yy_y_":
                current_guess = "PENAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "APIOL":
            if feedback == "_____":
                current_guess = "REUSE"
            elif feedback == "___g_":
                current_guess = "STOOD"
            elif feedback == "___gg":
                current_guess = "STOOL"
            elif feedback == "___y_":
                current_guess = "STOCK"
            elif feedback == "___yy":
                current_guess = "SLOTH"
            elif feedback == "__g__":
                current_guess = "FRISE"
            elif feedback == "__y__":
                current_guess = "RINSE"
            elif feedback == "__yy_":
                current_guess = "STOIC"
            elif feedback == "_y_g_":
                current_guess = "STOOP"
            elif feedback == "_y_y_":
                current_guess = "STOMP"
            elif feedback == "_yg__":
                current_guess = "PRISE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ARERE":
            if feedback == "yyy__":
                current_guess = "WAGER"
            elif feedback == "yyy_y":
                current_guess = "EAGER"
            elif feedback == "yyyy_":
                current_guess = "RAGER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ARGON":
            if feedback == "yggyg":
                current_guess = "ORGAN"
            elif feedback == "yy_yg":
                current_guess = "ROMAN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ARGOT":
            if feedback == "gy__g":
                current_guess = "APART"
            elif feedback == "gy__y":
                current_guess = "ALTAR"
            elif feedback == "gy_gy":
                current_guess = "ACTOR"
            elif feedback == "gy_yg":
                current_guess = "ABORT"
            elif feedback == "yg__g":
                current_guess = "CRAFT"
            elif feedback == "yg__y":
                current_guess = "WRATH"
            elif feedback == "ygy_g":
                current_guess = "GRAFT"
            elif feedback == "yy__g":
                current_guess = "CHART"
            elif feedback == "yy__y":
                current_guess = "ULTRA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ARISE":
            if feedback == "gg_gg":
                current_guess = "AROSE"
            elif feedback == "yg_gg":
                current_guess = "ERASE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ARSON":
            if feedback == "yyy__":
                current_guess = "SUGAR"
            elif feedback == "yyyyy":
                current_guess = "SONAR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ARTSY":
            if feedback == "yyyg_":
                current_guess = "ROAST"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AUDIO":
            if feedback == "g_ygy":
                current_guess = "AVOID"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AUGUR":
            if feedback == "y___g":
                current_guess = "FRIAR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AUMIL":
            if feedback == "_____":
                current_guess = "GREET"
            elif feedback == "___g_":
                current_guess = "REFIT"
            elif feedback == "___gy":
                current_guess = "RELIT"
            elif feedback == "___y_":
                current_guess = "RIVET"
            elif feedback == "__gg_":
                current_guess = "REMIT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AUNTY":
            if feedback == "yggg_":
                current_guess = "JUNTA"
            elif feedback == "yyyy_":
                current_guess = "UNTAG"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AVIAN":
            if feedback == "_yygg":
                current_guess = "DIVAN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "AWASH":
            if feedback == "__ggg":
                current_guess = "GNASH"
            elif feedback == "_gggg":
                current_guess = "SWASH"
            elif feedback == "g_ggg":
                current_guess = "ABASH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BACCY":
            if feedback == "_____":
                current_guess = "FLING"
            elif feedback == "____y":
                current_guess = "LYING"
            elif feedback == "__y__":
                current_guess = "CLING"
            elif feedback == "g____":
                current_guess = "BLING"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BADGE":
            if feedback == "_g_gg":
                current_guess = "MANGE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BADLY":
            if feedback == "_gggg":
                current_guess = "MADLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BAGEL":
            if feedback == "_g_gg":
                current_guess = "NAVEL"
            elif feedback == "_gygg":
                current_guess = "GAVEL"
            elif feedback == "gg_gg":
                current_guess = "BABEL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BAGIE":
            if feedback == "_____":
                current_guess = "FROWN"
            elif feedback == "__y__":
                current_guess = "GROWN"
            elif feedback == "__yg_":
                current_guess = "GROIN"
            elif feedback == "g____":
                current_guess = "BROWN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BAGUA":
            if feedback == "_g___":
                current_guess = "PANKO"
            elif feedback == "_g__g":
                current_guess = "MANIA"
            elif feedback == "_g__y":
                current_guess = "NAVAL"
            elif feedback == "_gg__":
                current_guess = "WAGON"
            elif feedback == "_gg_y":
                current_guess = "PAGAN"
            elif feedback == "_gy__":
                current_guess = "MANGO"
            elif feedback == "_gy_g":
                current_guess = "MANGA"
            elif feedback == "gg___":
                current_guess = "BANJO"
            elif feedback == "gg__y":
                current_guess = "BANAL"
            elif feedback == "yg___":
                current_guess = "NABOB"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BALER":
            if feedback == "_gygg":
                current_guess = "LAYER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BANDY":
            if feedback == "_gggg":
                current_guess = "DANDY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BASAL":
            if feedback == "ggg_g":
                current_guess = "BASIL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BASIC":
            if feedback == "gggg_":
                current_guess = "BASIS"
            elif feedback == "ygy__":
                current_guess = "SAMBA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BAWDY":
            if feedback == "_g_gg":
                current_guess = "GAUDY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEACH":
            if feedback == "_gg_y":
                current_guess = "HEAVY"
            elif feedback == "_gggg":
                current_guess = "PEACH"
            elif feedback == "_gy_y":
                current_guess = "HENNA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEADY":
            if feedback == "_gggg":
                current_guess = "HEADY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BECAP":
            if feedback == "_y___":
                current_guess = "WHOLE"
            elif feedback == "_y__y":
                current_guess = "ELOPE"
            elif feedback == "_yy__":
                current_guess = "CLOVE"
            elif feedback == "gy___":
                current_guess = "BLOKE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEDEW":
            if feedback == "__gg_":
                current_guess = "HIDER"
            elif feedback == "__ggy":
                current_guess = "WIDER"
            elif feedback == "__yg_":
                current_guess = "FRIED"
            elif feedback == "_gg__":
                current_guess = "REDID"
            elif feedback == "_gy_y":
                current_guess = "WEIRD"
            elif feedback == "_ygg_":
                current_guess = "EIDER"
            elif feedback == "ygy__":
                current_guess = "REBID"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEFIT":
            if feedback == "_g_yy":
                current_guess = "VENTI"
            elif feedback == "_gyyg":
                current_guess = "FEINT"
            elif feedback == "_y_gy":
                current_guess = "ETHIC"
            elif feedback == "_y_yg":
                current_guess = "EVICT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEFOG":
            if feedback == "_y___":
                current_guess = "CARVE"
            elif feedback == "_y__y":
                current_guess = "LARGE"
            elif feedback == "_yy__":
                current_guess = "FARCE"
            elif feedback == "gy___":
                current_guess = "BARRE"
            elif feedback == "gy__y":
                current_guess = "BARGE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEGAN":
            if feedback == "_g_gg":
                current_guess = "PECAN"
            elif feedback == "_gggg":
                current_guess = "VEGAN"
            elif feedback == "yg_g_":
                current_guess = "KEBAB"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEGAT":
            if feedback == "_y_gg":
                current_guess = "WHEAT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEGIN":
            if feedback == "_gyyg":
                current_guess = "FEIGN"
            elif feedback == "_gyyy":
                current_guess = "NEIGH"
            elif feedback == "_yyyy":
                current_guess = "EKING"
            elif feedback == "ggg_g":
                current_guess = "BEGUN"
            elif feedback == "ggyyy":
                current_guess = "BEING"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEGUN":
            if feedback == "_g___":
                current_guess = "REEDY"
            elif feedback == "_g_g_":
                current_guess = "REDUX"
            elif feedback == "_y___":
                current_guess = "FREED"
            elif feedback == "_y_y_":
                current_guess = "RUDER"
            elif feedback == "_y_yy":
                current_guess = "UNDER"
            elif feedback == "_yg__":
                current_guess = "EDGER"
            elif feedback == "_yy__":
                current_guess = "GREED"
            elif feedback == "gy___":
                current_guess = "BREED"
            elif feedback == "yg_g_":
                current_guess = "REDUB"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEIGE":
            if feedback == "__gyg":
                current_guess = "GUIDE"
            elif feedback == "__ygg":
                current_guess = "MIDGE"
            elif feedback == "__yyg":
                current_guess = "GIMME"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BELCH":
            if feedback == "_y___":
                current_guess = "PARER"
            elif feedback == "_y__y":
                current_guess = "HAREM"
            elif feedback == "_y_y_":
                current_guess = "CARER"
            elif feedback == "_yy__":
                current_guess = "EARLY"
            elif feedback == "gy___":
                current_guess = "BARER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BELLY":
            if feedback == "_gggg":
                current_guess = "JELLY"
            elif feedback == "_gy_g":
                current_guess = "LEGGY"
            elif feedback == "_yy_g":
                current_guess = "ELEGY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEMAD":
            if feedback == "_g_g_":
                current_guess = "AGLEY"
            elif feedback == "_g_gy":
                current_guess = "CEDAR"
            elif feedback == "_g_y_":
                current_guess = "LEARN"
            elif feedback == "_g_yg":
                current_guess = "HEARD"
            elif feedback == "_g_yy":
                current_guess = "READY"
            elif feedback == "_ggg_":
                current_guess = "REMAP"
            elif feedback == "_gyy_":
                current_guess = "REALM"
            elif feedback == "_y_g_":
                current_guess = "AFLOW"
            elif feedback == "_y_gg":
                current_guess = "DREAD"
            elif feedback == "_y_y_":
                current_guess = "ANGER"
            elif feedback == "_y_yy":
                current_guess = "ADMIN"
            elif feedback == "_ygyg":
                current_guess = "ARMED"
            elif feedback == "_yyg_":
                current_guess = "CREAM"
            elif feedback == "_yygy":
                current_guess = "DREAM"
            elif feedback == "_yyy_":
                current_guess = "CREMA"
            elif feedback == "gg_yg":
                current_guess = "BEARD"
            elif feedback == "gy_g_":
                current_guess = "BREAK"
            elif feedback == "gy_gg":
                current_guess = "BREAD"
            elif feedback == "gyyg_":
                current_guess = "BREAM"
            elif feedback == "yg_g_":
                current_guess = "REBAR"
            elif feedback == "yg_gy":
                current_guess = "DEBAR"
            elif feedback == "yg_y_":
                current_guess = "ZEBRA"
            elif feedback == "yyyy_":
                current_guess = "AMBER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BERET":
            if feedback == "_gg_g":
                current_guess = "MERIT"
            elif feedback == "_gg_y":
                current_guess = "HERTZ"
            elif feedback == "_yggg":
                current_guess = "EGRET"
            elif feedback == "ggg_y":
                current_guess = "BERTH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEVER":
            if feedback == "___gg":
                current_guess = "FLYER"
            elif feedback == "___gy":
                current_guess = "GRUEL"
            elif feedback == "_g__g":
                current_guess = "LEMUR"
            elif feedback == "_g__y":
                current_guess = "REPLY"
            elif feedback == "_g_gg":
                current_guess = "LEPER"
            elif feedback == "_g_gy":
                current_guess = "REPEL"
            elif feedback == "_g_yy":
                current_guess = "LEERY"
            elif feedback == "_gggg":
                current_guess = "LEVER"
            elif feedback == "_gggy":
                current_guess = "REVEL"
            elif feedback == "g__gg":
                current_guess = "BLUER"
            elif feedback == "yg_gy":
                current_guess = "REBEL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BEVUE":
            if feedback == "_g__y":
                current_guess = "JEWEL"
            elif feedback == "_gg_y":
                current_guess = "LEVEL"
            elif feedback == "_y___":
                current_guess = "IMPEL"
            elif feedback == "_y__y":
                current_guess = "EXCEL"
            elif feedback == "_y_y_":
                current_guess = "KUGEL"
            elif feedback == "_yg__":
                current_guess = "HOVEL"
            elif feedback == "_yy__":
                current_guess = "VOWEL"
            elif feedback == "gg__y":
                current_guess = "BEZEL"
            elif feedback == "ggg_y":
                current_guess = "BEVEL"
            elif feedback == "gy___":
                current_guess = "BOWEL"
            elif feedback == "yy___":
                current_guess = "LIBEL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BHANG":
            if feedback == "_____":
                current_guess = "FROZE"
            elif feedback == "____y":
                current_guess = "GROVE"
            elif feedback == "_g___":
                current_guess = "CHORE"
            elif feedback == "_y___":
                current_guess = "OCHRE"
            elif feedback == "g____":
                current_guess = "BROKE"
            elif feedback == "y____":
                current_guess = "OMBRE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BIACH":
            if feedback == "__g__":
                current_guess = "LEASE"
            elif feedback == "__g_y":
                current_guess = "PHASE"
            elif feedback == "__gy_":
                current_guess = "CEASE"
            elif feedback == "__gyy":
                current_guess = "CHASE"
            elif feedback == "__y__":
                current_guess = "AMUSE"
            elif feedback == "_yy__":
                current_guess = "ANISE"
            elif feedback == "g_g__":
                current_guess = "BLASE"
            elif feedback == "y_g__":
                current_guess = "ABASE"
            elif feedback == "y_y__":
                current_guess = "ABUSE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BICCY":
            if feedback == "_y___":
                current_guess = "OWING"
            elif feedback == "_y__y":
                current_guess = "VYING"
            elif feedback == "_yy__":
                current_guess = "ICING"
            elif feedback == "gy___":
                current_guess = "BOING"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BICEP":
            if feedback == "__yg_":
                current_guess = "CHEEK"
            elif feedback == "__ygg":
                current_guess = "CHEEP"
            elif feedback == "_yyg_":
                current_guess = "CHIEF"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BIFFY":
            if feedback == "_____":
                current_guess = "NORTH"
            elif feedback == "__y__":
                current_guess = "FORTH"
            elif feedback == "__y_g":
                current_guess = "FORTY"
            elif feedback == "_g___":
                current_guess = "GIRTH"
            elif feedback == "_g__g":
                current_guess = "DIRTY"
            elif feedback == "_gy__":
                current_guess = "FIRTH"
            elif feedback == "g____":
                current_guess = "BURNT"
            elif feedback == "gg___":
                current_guess = "BIRTH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BIGLY":
            if feedback == "_____":
                current_guess = "HUTCH"
            elif feedback == "____g":
                current_guess = "PUTTY"
            elif feedback == "___y_":
                current_guess = "KLUTZ"
            elif feedback == "__y_g":
                current_guess = "GUTTY"
            elif feedback == "g____":
                current_guess = "BUTCH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BIKER":
            if feedback == "_gggg":
                current_guess = "HIKER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BINGE":
            if feedback == "_gggg":
                current_guess = "HINGE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BINGO":
            if feedback == "_g_g_":
                current_guess = "PIGGY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BIOME":
            if feedback == "_gg_g":
                current_guess = "DIODE"
            elif feedback == "_yy_g":
                current_guess = "OXIDE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BIONT":
            if feedback == "____g":
                current_guess = "CRYPT"
            elif feedback == "___gg":
                current_guess = "GRUNT"
            elif feedback == "__g_g":
                current_guess = "GROUT"
            elif feedback == "__g_y":
                current_guess = "FROTH"
            elif feedback == "__ggg":
                current_guess = "FRONT"
            elif feedback == "__y_g":
                current_guess = "COURT"
            elif feedback == "__y_y":
                current_guess = "MOTOR"
            elif feedback == "_g__g":
                current_guess = "RIGHT"
            elif feedback == "_g__y":
                current_guess = "RITZY"
            elif feedback == "_gy_y":
                current_guess = "VITRO"
            elif feedback == "_gyyy":
                current_guess = "NITRO"
            elif feedback == "_y__g":
                current_guess = "DRIFT"
            elif feedback == "_y__y":
                current_guess = "FRITZ"
            elif feedback == "_y_gg":
                current_guess = "PRINT"
            elif feedback == "_yg_g":
                current_guess = "DROIT"
            elif feedback == "_yyyy":
                current_guess = "INTRO"
            elif feedback == "g___g":
                current_guess = "BLURT"
            elif feedback == "g__gg":
                current_guess = "BRUNT"
            elif feedback == "g_g_y":
                current_guess = "BROTH"
            elif feedback == "y_y_g":
                current_guess = "ROBOT"
            elif feedback == "yyy_g":
                current_guess = "ORBIT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BIOTA":
            if feedback == "___y_":
                current_guess = "METRE"
            elif feedback == "__gg_":
                current_guess = "WROTE"
            elif feedback == "__yg_":
                current_guess = "ROUTE"
            elif feedback == "__yy_":
                current_guess = "OUTRE"
            elif feedback == "_g_y_":
                current_guess = "LITRE"
            elif feedback == "_y_g_":
                current_guess = "WRITE"
            elif feedback == "_y_y_":
                current_guess = "RETIE"
            elif feedback == "g__g_":
                current_guess = "BRUTE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BIPOD":
            if feedback == "_g__g":
                current_guess = "VIVID"
            elif feedback == "_y_yg":
                current_guess = "OVOID"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BISON":
            if feedback == "__y_y":
                current_guess = "SYNCH"
            elif feedback == "__ygg":
                current_guess = "SWOON"
            elif feedback == "__ygy":
                current_guess = "SYNOD"
            elif feedback == "__yyg":
                current_guess = "SHOWN"
            elif feedback == "__yyy":
                current_guess = "SNOWY"
            elif feedback == "_yy_y":
                current_guess = "SNIFF"
            elif feedback == "_yygg":
                current_guess = "SCION"
            elif feedback == "_yyyy":
                current_guess = "SONIC"
            elif feedback == "g_ggg":
                current_guess = "BOSON"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BITER":
            if feedback == "_gggg":
                current_guess = "LITER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BITTY":
            if feedback == "_gggg":
                current_guess = "KITTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BLACK":
            if feedback == "_gggg":
                current_guess = "FLACK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BLADE":
            if feedback == "_gggg":
                current_guess = "CLADE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BLARE":
            if feedback == "__ggg":
                current_guess = "AWARE"
            elif feedback == "_gggg":
                current_guess = "FLARE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BLEEP":
            if feedback == "_y_g_":
                current_guess = "GOLEM"
            elif feedback == "_y_gg":
                current_guess = "JULEP"
            elif feedback == "yyyg_":
                current_guess = "CELEB"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BLIMP":
            if feedback == "_____":
                current_guess = "HONEY"
            elif feedback == "___y_":
                current_guess = "MONEY"
            elif feedback == "__y__":
                current_guess = "WINEY"
            elif feedback == "__y_y":
                current_guess = "PINEY"
            elif feedback == "g____":
                current_guess = "BONEY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BLINK":
            if feedback == "_gggg":
                current_guess = "PLINK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BLITZ":
            if feedback == "_gggg":
                current_guess = "GLITZ"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BLOCK":
            if feedback == "ggg__":
                current_guess = "BLOWN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BLOND":
            if feedback == "_____":
                current_guess = "CHARM"
            elif feedback == "____g":
                current_guess = "AARGH"
            elif feedback == "____y":
                current_guess = "DIARY"
            elif feedback == "___g_":
                current_guess = "FRANC"
            elif feedback == "___gg":
                current_guess = "GRAND"
            elif feedback == "___gy":
                current_guess = "DRANK"
            elif feedback == "___y_":
                current_guess = "ANGRY"
            elif feedback == "___yy":
                current_guess = "DRAIN"
            elif feedback == "__g__":
                current_guess = "AGORA"
            elif feedback == "__gy_":
                current_guess = "ACORN"
            elif feedback == "__gyy":
                current_guess = "ADORN"
            elif feedback == "__y__":
                current_guess = "HOARY"
            elif feedback == "__y_g":
                current_guess = "HOARD"
            elif feedback == "__y_y":
                current_guess = "ARDOR"
            elif feedback == "__yy_":
                current_guess = "ARGON"
            elif feedback == "_g___":
                current_guess = "ALARM"
            elif feedback == "_g_y_":
                current_guess = "ULNAR"
            elif feedback == "_gg__":
                current_guess = "FLORA"
            elif feedback == "_gg_g":
                current_guess = "FLOOD"
            elif feedback == "_y___":
                current_guess = "FRAIL"
            elif feedback == "_y__y":
                current_guess = "DRAWL"
            elif feedback == "_y_y_":
                current_guess = "GNARL"
            elif feedback == "_yy__":
                current_guess = "MOLAR"
            elif feedback == "g____":
                current_guess = "BRAVA"
            elif feedback == "g___g":
                current_guess = "BRAID"
            elif feedback == "g__gg":
                current_guess = "BRAND"
            elif feedback == "g__y_":
                current_guess = "BRAIN"
            elif feedback == "g_g_g":
                current_guess = "BROAD"
            elif feedback == "g_y__":
                current_guess = "BRAVO"
            elif feedback == "g_y_g":
                current_guess = "BOARD"
            elif feedback == "ggg_g":
                current_guess = "BLOOD"
            elif feedback == "gy___":
                current_guess = "BRAWL"
            elif feedback == "y____":
                current_guess = "RUMBA"
            elif feedback == "y__y_":
                current_guess = "URBAN"
            elif feedback == "y_y__":
                current_guess = "ABHOR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BLUFF":
            if feedback == "_gggg":
                current_guess = "FLUFF"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BLUNT":
            if feedback == "__yyg":
                current_guess = "UNFIT"
            elif feedback == "_yyyg":
                current_guess = "UNLIT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOAST":
            if feedback == "__ggg":
                current_guess = "AVAST"
            elif feedback == "__ggy":
                current_guess = "STASH"
            elif feedback == "__ygg":
                current_guess = "ANGST"
            elif feedback == "__ygy":
                current_guess = "ANTSY"
            elif feedback == "_gggg":
                current_guess = "COAST"
            elif feedback == "g_ggg":
                current_guess = "BLAST"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOBBY":
            if feedback == "_g__g":
                current_guess = "COCKY"
            elif feedback == "gg___":
                current_guess = "BOFFO"
            elif feedback == "gg__g":
                current_guess = "BONNY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOCCE":
            if feedback == "_gy_g":
                current_guess = "COUPE"
            elif feedback == "gg__g":
                current_guess = "BOOZE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOGEY":
            if feedback == "_g_gg":
                current_guess = "JOKEY"
            elif feedback == "_gggg":
                current_guess = "FOGEY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOGGY":
            if feedback == "__g_g":
                current_guess = "PYGMY"
            elif feedback == "_gggg":
                current_guess = "FOGGY"
            elif feedback == "gg_g_":
                current_guess = "BONGO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOGUE":
            if feedback == "_____":
                current_guess = "WRIST"
            elif feedback == "___y_":
                current_guess = "CRUST"
            elif feedback == "__y__":
                current_guess = "GRIST"
            elif feedback == "_g___":
                current_guess = "ROOST"
            elif feedback == "_g_y_":
                current_guess = "ROUST"
            elif feedback == "_y___":
                current_guess = "FROST"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOLUS":
            if feedback == "__gyy":
                current_guess = "SULLY"
            elif feedback == "_gygg":
                current_guess = "LOCUS"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOOBY":
            if feedback == "__g__":
                current_guess = "KNOCK"
            elif feedback == "_gg_g":
                current_guess = "KOOKY"
            elif feedback == "ggg_g":
                current_guess = "BOOZY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOOFY":
            if feedback == "_____":
                current_guess = "DATUM"
            elif feedback == "____g":
                current_guess = "NATTY"
            elif feedback == "___y_":
                current_guess = "FATWA"
            elif feedback == "___yg":
                current_guess = "FATTY"
            elif feedback == "_y___":
                current_guess = "MATZO"
            elif feedback == "g___g":
                current_guess = "BATTY"
            elif feedback == "gy___":
                current_guess = "BATON"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BORED":
            if feedback == "_ggg_":
                current_guess = "MOREL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BORIC":
            if feedback == "_gg_y":
                current_guess = "PORCH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOUGH":
            if feedback == "_gggg":
                current_guess = "COUGH"
            elif feedback == "_ggy_":
                current_guess = "YOUNG"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOULE":
            if feedback == "_gggg":
                current_guess = "JOULE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOWER":
            if feedback == "_gggg":
                current_guess = "ROWER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BOXER":
            if feedback == "_g_gg":
                current_guess = "ROVER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BRAIN":
            if feedback == "ggg_g":
                current_guess = "BRAWN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BRAVA":
            if feedback == "ggy__":
                current_guess = "BRIAR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BRICK":
            if feedback == "_ggg_":
                current_guess = "PRICY"
            elif feedback == "_gggg":
                current_guess = "PRICK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BRIDE":
            if feedback == "_ggyg":
                current_guess = "DRIVE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BRIEF":
            if feedback == "_gggg":
                current_guess = "GRIEF"
            elif feedback == "_yyy_":
                current_guess = "REMIX"
            elif feedback == "gggg_":
                current_guess = "BRIER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BRINE":
            if feedback == "_gggg":
                current_guess = "URINE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BROOM":
            if feedback == "_ggg_":
                current_guess = "PROOF"
            elif feedback == "_gggg":
                current_guess = "GROOM"
            elif feedback == "_ygg_":
                current_guess = "FLOOR"
            elif feedback == "gggg_":
                current_guess = "BROOK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BUCHU":
            if feedback == "_____":
                current_guess = "PASTE"
            elif feedback == "___y_":
                current_guess = "HASTE"
            elif feedback == "__y__":
                current_guess = "CASTE"
            elif feedback == "_y___":
                current_guess = "SAUTE"
            elif feedback == "g____":
                current_guess = "BASTE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BUGGY":
            if feedback == "__y__":
                current_guess = "WRING"
            elif feedback == "_g___":
                current_guess = "RUNUP"
            elif feedback == "_g__g":
                current_guess = "RUNNY"
            elif feedback == "_gy__":
                current_guess = "RUING"
            elif feedback == "_yy__":
                current_guess = "WRUNG"
            elif feedback == "g____":
                current_guess = "BRINK"
            elif feedback == "g___g":
                current_guess = "BRINY"
            elif feedback == "g_y__":
                current_guess = "BRING"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BUILD":
            if feedback == "_____":
                current_guess = "EMOTE"
            elif feedback == "__g__":
                current_guess = "WHITE"
            elif feedback == "__gy_":
                current_guess = "ELITE"
            elif feedback == "__yy_":
                current_guess = "LITHE"
            elif feedback == "_g___":
                current_guess = "QUOTE"
            elif feedback == "_gg__":
                current_guess = "QUITE"
            elif feedback == "_gy__":
                current_guess = "CUTIE"
            elif feedback == "_y___":
                current_guess = "CHUTE"
            elif feedback == "_y__y":
                current_guess = "ETUDE"
            elif feedback == "_y_y_":
                current_guess = "FLUTE"
            elif feedback == "_yg__":
                current_guess = "UNITE"
            elif feedback == "_ygg_":
                current_guess = "UTILE"
            elif feedback == "_yy__":
                current_guess = "UNTIE"
            elif feedback == "gg___":
                current_guess = "BUTTE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BULKY":
            if feedback == "_gg__":
                current_guess = "MULCH"
            elif feedback == "_gg_g":
                current_guess = "PULPY"
            elif feedback == "_gggg":
                current_guess = "HULKY"
            elif feedback == "_gy__":
                current_guess = "LUNCH"
            elif feedback == "_gy_g":
                current_guess = "LUMPY"
            elif feedback == "_gygg":
                current_guess = "LUCKY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BULLY":
            if feedback == "_gggg":
                current_guess = "FULLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BUMPH":
            if feedback == "_____":
                current_guess = "WEDGE"
            elif feedback == "____y":
                current_guess = "HEDGE"
            elif feedback == "_g___":
                current_guess = "FUDGE"
            elif feedback == "_g__g":
                current_guess = "HUNCH"
            elif feedback == "_g__y":
                current_guess = "HUFFY"
            elif feedback == "_g_g_":
                current_guess = "PUPPY"
            elif feedback == "_g_y_":
                current_guess = "PUDGE"
            elif feedback == "_g_yg":
                current_guess = "PUNCH"
            elif feedback == "_gg__":
                current_guess = "MUMMY"
            elif feedback == "_ggg_":
                current_guess = "JUMPY"
            elif feedback == "_gggg":
                current_guess = "HUMPH"
            elif feedback == "_gy__":
                current_guess = "MUCKY"
            elif feedback == "_gy_g":
                current_guess = "MUNCH"
            elif feedback == "_y___":
                current_guess = "FOUND"
            elif feedback == "_y__y":
                current_guess = "HOUND"
            elif feedback == "_y_y_":
                current_guess = "POUND"
            elif feedback == "_yy__":
                current_guess = "MOUND"
            elif feedback == "gg___":
                current_guess = "BUDGE"
            elif feedback == "gg__g":
                current_guess = "BUNCH"
            elif feedback == "gggg_":
                current_guess = "BUMPY"
            elif feedback == "ggy__":
                current_guess = "BUXOM"
            elif feedback == "gy___":
                current_guess = "BOUND"
            elif feedback == "yg___":
                current_guess = "CUBBY"
            elif feedback == "yg__y":
                current_guess = "HUBBY"
            elif feedback == "ygg__":
                current_guess = "JUMBO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BUNNY":
            if feedback == "gg__g":
                current_guess = "BUZZY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BURLY":
            if feedback == "__ggg":
                current_guess = "GIRLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "BURRO":
            if feedback == "__g_g":
                current_guess = "FORGO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CABAL":
            if feedback == "gg__g":
                current_guess = "CAVIL"
            elif feedback == "gg__y":
                current_guess = "CAULK"
            elif feedback == "gg_g_":
                current_guess = "CACAO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CABBY":
            if feedback == "gg__g":
                current_guess = "CAMPY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CADRE":
            if feedback == "_g_yg":
                current_guess = "RANGE"
            elif feedback == "_gggg":
                current_guess = "PADRE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CAMEO":
            if feedback == "_ggg_":
                current_guess = "FAMED"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CANON":
            if feedback == "gg__g":
                current_guess = "CABIN"
            elif feedback == "gg_gg":
                current_guess = "CAPON"
            elif feedback == "ggg__":
                current_guess = "CANAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CAPHS":
            if feedback == "____y":
                current_guess = "STOUT"
            elif feedback == "___yy":
                current_guess = "SHOUT"
            elif feedback == "__y_y":
                current_guess = "SPOUT"
            elif feedback == "y___y":
                current_guess = "SCOUT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CAPIZ":
            if feedback == "_y___":
                current_guess = "GRAVE"
            elif feedback == "_y__y":
                current_guess = "GRAZE"
            elif feedback == "_yy__":
                current_guess = "GRAPE"
            elif feedback == "yy___":
                current_guess = "GRACE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CAPRI":
            if feedback == "_g_yy":
                current_guess = "FAKIR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CARET":
            if feedback == "_ggyy":
                current_guess = "EARTH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CARNY":
            if feedback == "ggg_g":
                current_guess = "CARRY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CARVY":
            if feedback == "_gy__":
                current_guess = "PAPER"
            elif feedback == "_gy_y":
                current_guess = "PAYER"
            elif feedback == "_gyy_":
                current_guess = "PAVER"
            elif feedback == "ggy__":
                current_guess = "CAPER"
            elif feedback == "ygy__":
                current_guess = "PACER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CATCH":
            if feedback == "ggg__":
                current_guess = "CATTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHAFF":
            if feedback == "ggg__":
                current_guess = "CHAMP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHALK":
            if feedback == "__g__":
                current_guess = "SPADE"
            elif feedback == "__g_y":
                current_guess = "SNAKE"
            elif feedback == "__gg_":
                current_guess = "SWALE"
            elif feedback == "__gyy":
                current_guess = "SLAKE"
            elif feedback == "__y__":
                current_guess = "ASIDE"
            elif feedback == "__yg_":
                current_guess = "AISLE"
            elif feedback == "_gg__":
                current_guess = "AMPED"
            elif feedback == "_gg_y":
                current_guess = "SHAKE"
            elif feedback == "_ggg_":
                current_guess = "SHALE"
            elif feedback == "g_gy_":
                current_guess = "CLAMP"
            elif feedback == "g_gyg":
                current_guess = "CLACK"
            elif feedback == "y_g__":
                current_guess = "SCAPE"
            elif feedback == "y_gg_":
                current_guess = "SCALE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHANT":
            if feedback == "__ggg":
                current_guess = "QUANT"
            elif feedback == "y_y_g":
                current_guess = "DUCAT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHAOS":
            if feedback == "y_g_y":
                current_guess = "SMACK"
            elif feedback == "ygg_y":
                current_guess = "SHACK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHARM":
            if feedback == "__gg_":
                current_guess = "QUARK"
            elif feedback == "__gy_":
                current_guess = "GRAVY"
            elif feedback == "__yy_":
                current_guess = "AUGUR"
            elif feedback == "__yyy":
                current_guess = "PRIMA"
            elif feedback == "_ggg_":
                current_guess = "WHARF"
            elif feedback == "_ygy_":
                current_guess = "GRAPH"
            elif feedback == "g_gy_":
                current_guess = "CRACK"
            elif feedback == "g_gyy":
                current_guess = "CRAMP"
            elif feedback == "g_yy_":
                current_guess = "CIGAR"
            elif feedback == "gggg_":
                current_guess = "CHARY"
            elif feedback == "gggy_":
                current_guess = "CHAIR"
            elif feedback == "y_gy_":
                current_guess = "FRACK"
            elif feedback == "y_yy_":
                current_guess = "VICAR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHART":
            if feedback == "__ggg":
                current_guess = "QUART"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHAWL":
            if feedback == "__y__":
                current_guess = "ADEEM"
            elif feedback == "__y_y":
                current_guess = "LATER"
            elif feedback == "__yy_":
                current_guess = "WATER"
            elif feedback == "_yy__":
                current_guess = "HATER"
            elif feedback == "g_y__":
                current_guess = "CATER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHEAP":
            if feedback == "y_gg_":
                current_guess = "OCEAN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHEEK":
            if feedback == "___g_":
                current_guess = "INSET"
            elif feedback == "__g__":
                current_guess = "STENT"
            elif feedback == "__gg_":
                current_guess = "SWEET"
            elif feedback == "__ggy":
                current_guess = "SKEET"
            elif feedback == "__yg_":
                current_guess = "BESET"
            elif feedback == "_ggg_":
                current_guess = "SHEET"
            elif feedback == "y_g__":
                current_guess = "SCENT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHEEP":
            if feedback == "__y__":
                current_guess = "UNDUE"
            elif feedback == "__yy_":
                current_guess = "VENUE"
            elif feedback == "__yyy":
                current_guess = "PENNE"
            elif feedback == "y_y__":
                current_guess = "DUNCE"
            elif feedback == "y_yy_":
                current_guess = "FENCE"
            elif feedback == "y_yyy":
                current_guess = "PENCE"
            elif feedback == "yyyy_":
                current_guess = "HENCE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHILD":
            if feedback == "_____":
                current_guess = "TEPEE"
            elif feedback == "___g_":
                current_guess = "TULLE"
            elif feedback == "__g__":
                current_guess = "TWINE"
            elif feedback == "__y__":
                current_guess = "TINGE"
            elif feedback == "__yg_":
                current_guess = "TITLE"
            elif feedback == "__yyy":
                current_guess = "TILDE"
            elif feedback == "_g___":
                current_guess = "THEME"
            elif feedback == "_gg__":
                current_guess = "THINE"
            elif feedback == "_yy__":
                current_guess = "TITHE"
            elif feedback == "y_g__":
                current_guess = "TWICE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHILE":
            if feedback == "__ggg":
                current_guess = "EXILE"
            elif feedback == "__gyg":
                current_guess = "ELIDE"
            elif feedback == "__ygg":
                current_guess = "BIBLE"
            elif feedback == "_gggg":
                current_guess = "WHILE"
            elif feedback == "g_gyg":
                current_guess = "CLIME"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHILI":
            if feedback == "gggg_":
                current_guess = "CHILL"
            elif feedback == "y_ggy":
                current_guess = "ICILY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHIMB":
            if feedback == "_____":
                current_guess = "FLAKE"
            elif feedback == "____y":
                current_guess = "BLAZE"
            elif feedback == "___g_":
                current_guess = "FLAME"
            elif feedback == "___gy":
                current_guess = "BLAME"
            elif feedback == "___y_":
                current_guess = "MODUS"
            elif feedback == "__g__":
                current_guess = "FRISK"
            elif feedback == "__g_y":
                current_guess = "BRISK"
            elif feedback == "__gy_":
                current_guess = "PRISM"
            elif feedback == "_y___":
                current_guess = "FROSH"
            elif feedback == "_y__y":
                current_guess = "BRUSH"
            elif feedback == "_y_y_":
                current_guess = "HUMUS"
            elif feedback == "_yy__":
                current_guess = "SUSHI"
            elif feedback == "g____":
                current_guess = "CLAVE"
            elif feedback == "g_g__":
                current_guess = "CRISP"
            elif feedback == "gy___":
                current_guess = "CRUSH"
            elif feedback == "y____":
                current_guess = "PLACE"
            elif feedback == "y__y_":
                current_guess = "MUCUS"
            elif feedback == "y_y__":
                current_guess = "FICUS"
            elif feedback == "y_yy_":
                current_guess = "MUSIC"
            elif feedback == "yy___":
                current_guess = "HOCUS"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHIRP":
            if feedback == "g__y_":
                current_guess = "CRUMB"
            elif feedback == "g__yg":
                current_guess = "CRUMP"
            elif feedback == "g_gy_":
                current_guess = "CRICK"
            elif feedback == "g_gyg":
                current_guess = "CRIMP"
            elif feedback == "gg_g_":
                current_guess = "CHURL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHOKE":
            if feedback == "__ggg":
                current_guess = "EVOKE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHOMP":
            if feedback == "__g__":
                current_guess = "GOOEY"
            elif feedback == "__y__":
                current_guess = "BOGEY"
            elif feedback == "__y_y":
                current_guess = "POKEY"
            elif feedback == "__yyy":
                current_guess = "MOPEY"
            elif feedback == "_yg__":
                current_guess = "HOOEY"
            elif feedback == "_yy__":
                current_guess = "HOKEY"
            elif feedback == "_yyy_":
                current_guess = "HOMEY"
            elif feedback == "g_y__":
                current_guess = "COVEY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHORD":
            if feedback == "g_gyg":
                current_guess = "CROWD"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CHYND":
            if feedback == "_____":
                current_guess = "MAMBA"
            elif feedback == "____g":
                current_guess = "VALID"
            elif feedback == "____y":
                current_guess = "MADAM"
            elif feedback == "___g_":
                current_guess = "FAUNA"
            elif feedback == "___y_":
                current_guess = "BAGUA"
            elif feedback == "___yy":
                current_guess = "PANDA"
            elif feedback == "__g__":
                current_guess = "LAYUP"
            elif feedback == "__y__":
                current_guess = "GLUME"
            elif feedback == "__y_y":
                current_guess = "DALED"
            elif feedback == "__yg_":
                current_guess = "NANNY"
            elif feedback == "__yy_":
                current_guess = "MANLY"
            elif feedback == "__yyy":
                current_guess = "BANDY"
            elif feedback == "_y___":
                current_guess = "HAIKU"
            elif feedback == "_yy__":
                current_guess = "HAMMY"
            elif feedback == "_yyy_":
                current_guess = "HANKY"
            elif feedback == "_yyyy":
                current_guess = "HANDY"
            elif feedback == "g____":
                current_guess = "CABAL"
            elif feedback == "g__y_":
                current_guess = "CANON"
            elif feedback == "g_y__":
                current_guess = "CABBY"
            elif feedback == "g_y_y":
                current_guess = "CADDY"
            elif feedback == "g_yg_":
                current_guess = "CANNY"
            elif feedback == "g_yyy":
                current_guess = "CANDY"
            elif feedback == "y____":
                current_guess = "MAGIC"
            elif feedback == "y__y_":
                current_guess = "MANIC"
            elif feedback == "y_y__":
                current_guess = "WACKY"
            elif feedback == "y_yy_":
                current_guess = "FANCY"
            elif feedback == "yy___":
                current_guess = "HAVOC"
            elif feedback == "yy__y":
                current_guess = "DACHA"
            elif feedback == "yy_y_":
                current_guess = "NACHO"
            elif feedback == "yyy__":
                current_guess = "HACKY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CIDER":
            if feedback == "___gg":
                current_guess = "SURER"
            elif feedback == "___gy":
                current_guess = "SHREW"
            elif feedback == "___yy":
                current_guess = "SERUM"
            elif feedback == "__ygy":
                current_guess = "SHRED"
            elif feedback == "_g_gy":
                current_guess = "SIREN"
            elif feedback == "_y_yy":
                current_guess = "SERIF"
            elif feedback == "gyygy":
                current_guess = "CRIED"
            elif feedback == "y__gy":
                current_guess = "SCREW"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLAMP":
            if feedback == "__g__":
                current_guess = "SHARK"
            elif feedback == "__g_g":
                current_guess = "SHARP"
            elif feedback == "__g_y":
                current_guess = "SPARK"
            elif feedback == "__gy_":
                current_guess = "SMARM"
            elif feedback == "__y__":
                current_guess = "ARSON"
            elif feedback == "_yg__":
                current_guess = "SNARL"
            elif feedback == "_yy__":
                current_guess = "SOLAR"
            elif feedback == "y_g__":
                current_guess = "SCARF"
            elif feedback == "y_g_g":
                current_guess = "SCARP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLANG":
            if feedback == "gggg_":
                current_guess = "CLANK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLAPT":
            if feedback == "__g_g":
                current_guess = "SHAFT"
            elif feedback == "__g_y":
                current_guess = "STAND"
            elif feedback == "__ggy":
                current_guess = "STAPH"
            elif feedback == "__gyy":
                current_guess = "STAMP"
            elif feedback == "__y_g":
                current_guess = "SQUAT"
            elif feedback == "__y_y":
                current_guess = "STOMA"
            elif feedback == "_gg_g":
                current_guess = "SLANT"
            elif feedback == "_yg_g":
                current_guess = "SHALT"
            elif feedback == "_yg_y":
                current_guess = "STALK"
            elif feedback == "_yy_y":
                current_guess = "ATLAS"
            elif feedback == "_yyyg":
                current_guess = "SPLAT"
            elif feedback == "y_g_g":
                current_guess = "SCANT"
            elif feedback == "y_g_y":
                current_guess = "STACK"
            elif feedback == "y_y_g":
                current_guess = "ASCOT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLASP":
            if feedback == "gggg_":
                current_guess = "CLASS"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLEAN":
            if feedback == "_ggg_":
                current_guess = "BLEAK"
            elif feedback == "_gggg":
                current_guess = "GLEAN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLERK":
            if feedback == "gyyy_":
                current_guess = "CRUEL"
            elif feedback == "ygyy_":
                current_guess = "ULCER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLINT":
            if feedback == "____y":
                current_guess = "TRAMP"
            elif feedback == "__g_y":
                current_guess = "TRIAD"
            elif feedback == "__y_g":
                current_guess = "TRAIT"
            elif feedback == "__y_y":
                current_guess = "TIARA"
            elif feedback == "__yyy":
                current_guess = "TRAIN"
            elif feedback == "_y__y":
                current_guess = "TRAWL"
            elif feedback == "_yg_y":
                current_guess = "TRIAL"
            elif feedback == "_yy_y":
                current_guess = "TRAIL"
            elif feedback == "y___g":
                current_guess = "TRACT"
            elif feedback == "y___y":
                current_guess = "TRACK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLIPT":
            if feedback == "____g":
                current_guess = "DOUGH"
            elif feedback == "____y":
                current_guess = "BOOFY"
            elif feedback == "___yg":
                current_guess = "KAPUT"
            elif feedback == "___yy":
                current_guess = "PANTY"
            elif feedback == "__g_g":
                current_guess = "FAINT"
            elif feedback == "__g_y":
                current_guess = "FAITH"
            elif feedback == "__gyg":
                current_guess = "PAINT"
            elif feedback == "__y_g":
                current_guess = "HABIT"
            elif feedback == "__y_y":
                current_guess = "BATIK"
            elif feedback == "__yyy":
                current_guess = "PATIO"
            elif feedback == "_y__g":
                current_guess = "FAULT"
            elif feedback == "_y__y":
                current_guess = "AFOAM"
            elif feedback == "_yg_y":
                current_guess = "LAITY"
            elif feedback == "g___y":
                current_guess = "CATCH"
            elif feedback == "g__yg":
                current_guess = "CAPUT"
            elif feedback == "g_y_y":
                current_guess = "CACTI"
            elif feedback == "y___g":
                current_guess = "YACHT"
            elif feedback == "y___y":
                current_guess = "EMBOW"
            elif feedback == "y__yy":
                current_guess = "PATCH"
            elif feedback == "yy__y":
                current_guess = "LATCH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLOCK":
            if feedback == "_gg__":
                current_guess = "FLOWN"
            elif feedback == "_gggg":
                current_guess = "FLOCK"
            elif feedback == "ggg__":
                current_guess = "CLOWN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLONK":
            if feedback == "_____":
                current_guess = "USURP"
            elif feedback == "____g":
                current_guess = "SHIRK"
            elif feedback == "____y":
                current_guess = "RISKY"
            elif feedback == "___y_":
                current_guess = "SPURN"
            elif feedback == "__g__":
                current_guess = "SWORD"
            elif feedback == "__g_g":
                current_guess = "SPORK"
            elif feedback == "__gy_":
                current_guess = "SHORN"
            elif feedback == "__y__":
                current_guess = "VISOR"
            elif feedback == "__yy_":
                current_guess = "ROSIN"
            elif feedback == "_g___":
                current_guess = "SLURP"
            elif feedback == "_y___":
                current_guess = "SWIRL"
            elif feedback == "y_g__":
                current_guess = "SCOUR"
            elif feedback == "y_gy_":
                current_guess = "SCORN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLOTH":
            if feedback == "___g_":
                current_guess = "MATTE"
            elif feedback == "___gy":
                current_guess = "HAUTE"
            elif feedback == "___yy":
                current_guess = "BATHE"
            elif feedback == "__ggy":
                current_guess = "PHOTO"
            elif feedback == "_y_g_":
                current_guess = "LATTE"
            elif feedback == "_y_y_":
                current_guess = "LATKE"
            elif feedback == "_y_yy":
                current_guess = "LATHE"
            elif feedback == "y_yy_":
                current_guess = "OPTIC"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLOUD":
            if feedback == "_____":
                current_guess = "GEESE"
            elif feedback == "____y":
                current_guess = "DENSE"
            elif feedback == "___y_":
                current_guess = "GUISE"
            elif feedback == "__g__":
                current_guess = "AHING"
            elif feedback == "__y__":
                current_guess = "NOISE"
            elif feedback == "__y_y":
                current_guess = "DOWSE"
            elif feedback == "__yy_":
                current_guess = "HOUSE"
            elif feedback == "__yyy":
                current_guess = "DOUSE"
            elif feedback == "_y_y_":
                current_guess = "PULSE"
            elif feedback == "_yg__":
                current_guess = "LOOSE"
            elif feedback == "_yyy_":
                current_guess = "LOUSE"
            elif feedback == "g_g__":
                current_guess = "CHOSE"
            elif feedback == "g_y__":
                current_guess = "COPSE"
            elif feedback == "ggg__":
                current_guess = "CLOSE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLOUT":
            if feedback == "_gggg":
                current_guess = "FLOUT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CLUNG":
            if feedback == "_gggg":
                current_guess = "FLUNG"
            elif feedback == "_yy_y":
                current_guess = "MOGUL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COCOA":
            if feedback == "gg__g":
                current_guess = "COMMA"
            elif feedback == "gg__y":
                current_guess = "COPAY"
            elif feedback == "ggy_y":
                current_guess = "COACH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CODON":
            if feedback == "_____":
                current_guess = "FUGLY"
            elif feedback == "____g":
                current_guess = "BRUIN"
            elif feedback == "____y":
                current_guess = "BUGGY"
            elif feedback == "___g_":
                current_guess = "PRIOR"
            elif feedback == "___gg":
                current_guess = "PRION"
            elif feedback == "___gy":
                current_guess = "MINOR"
            elif feedback == "__g__":
                current_guess = "RUDDY"
            elif feedback == "__y__":
                current_guess = "DRILL"
            elif feedback == "__y_y":
                current_guess = "DRINK"
            elif feedback == "_g___":
                current_guess = "ROUGH"
            elif feedback == "_g__g":
                current_guess = "MOURN"
            elif feedback == "_g_gy":
                current_guess = "HONOR"
            elif feedback == "_g_y_":
                current_guess = "ROOMY"
            elif feedback == "_gy__":
                current_guess = "DOWRY"
            elif feedback == "_gy_y":
                current_guess = "ROUND"
            elif feedback == "_gygy":
                current_guess = "DONOR"
            elif feedback == "_y___":
                current_guess = "GROWL"
            elif feedback == "_y__g":
                current_guess = "BAGIE"
            elif feedback == "_y__y":
                current_guess = "PRONG"
            elif feedback == "_y_g_":
                current_guess = "BROOM"
            elif feedback == "_y_y_":
                current_guess = "PROMO"
            elif feedback == "_yg__":
                current_guess = "HYDRO"
            elif feedback == "_yy__":
                current_guess = "DROID"
            elif feedback == "_yy_g":
                current_guess = "DROWN"
            elif feedback == "_yy_y":
                current_guess = "FROND"
            elif feedback == "_yyg_":
                current_guess = "DROOL"
            elif feedback == "g____":
                current_guess = "CHIRP"
            elif feedback == "g___g":
                current_guess = "CHURN"
            elif feedback == "gg_g_":
                current_guess = "COLOR"
            elif feedback == "gy___":
                current_guess = "CROCK"
            elif feedback == "gy__g":
                current_guess = "CROWN"
            elif feedback == "gy__y":
                current_guess = "CRONY"
            elif feedback == "gy_g_":
                current_guess = "CROOK"
            elif feedback == "gy_gg":
                current_guess = "CROON"
            elif feedback == "gyy__":
                current_guess = "CHORD"
            elif feedback == "y____":
                current_guess = "BRICK"
            elif feedback == "y___g":
                current_guess = "RICIN"
            elif feedback == "y___y":
                current_guess = "INCUR"
            elif feedback == "yg___":
                current_guess = "ROCKY"
            elif feedback == "yy___":
                current_guess = "MICRO"
            elif feedback == "yy__y":
                current_guess = "BRONC"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COLIN":
            if feedback == "_____":
                current_guess = "GUAVA"
            elif feedback == "____g":
                current_guess = "HUMAN"
            elif feedback == "____y":
                current_guess = "UNJAM"
            elif feedback == "___g_":
                current_guess = "AFFIX"
            elif feedback == "___gg":
                current_guess = "ADMIN"
            elif feedback == "___y_":
                current_guess = "HIJAB"
            elif feedback == "___yg":
                current_guess = "AVIAN"
            elif feedback == "___yy":
                current_guess = "ADAPT"
            elif feedback == "__g__":
                current_guess = "ALLAY"
            elif feedback == "__gy_":
                current_guess = "PILAF"
            elif feedback == "__gyy":
                current_guess = "INLAY"
            elif feedback == "__y__":
                current_guess = "AMPLY"
            elif feedback == "__y_y":
                current_guess = "ABACK"
            elif feedback == "__yg_":
                current_guess = "ABJUD"
            elif feedback == "__ygg":
                current_guess = "PLAIN"
            elif feedback == "__ygy":
                current_guess = "ANVIL"
            elif feedback == "__yy_":
                current_guess = "ALIBI"
            elif feedback == "__yyg":
                current_guess = "ALIGN"
            elif feedback == "__yyy":
                current_guess = "FINAL"
            elif feedback == "_g___":
                current_guess = "DOGMA"
            elif feedback == "_g__g":
                current_guess = "WOMAN"
            elif feedback == "_g__y":
                current_guess = "GONAD"
            elif feedback == "_gg__":
                current_guess = "POLKA"
            elif feedback == "_gy__":
                current_guess = "LOAMY"
            elif feedback == "_gy_y":
                current_guess = "NODAL"
            elif feedback == "_gyy_":
                current_guess = "VOILA"
            elif feedback == "_y___":
                current_guess = "ADOBO"
            elif feedback == "_y__y":
                current_guess = "AGONY"
            elif feedback == "_y_g_":
                current_guess = "AUDIO"
            elif feedback == "_y_y_":
                current_guess = "AMIGO"
            elif feedback == "_y_yg":
                current_guess = "AXION"
            elif feedback == "_y_yy":
                current_guess = "AMINO"
            elif feedback == "_yg__":
                current_guess = "AGLOW"
            elif feedback == "_yy__":
                current_guess = "AFALD"
            elif feedback == "_yy_y":
                current_guess = "ALONG"
            elif feedback == "_yyg_":
                current_guess = "ABOIL"
            elif feedback == "_yyy_":
                current_guess = "AIOLI"
            elif feedback == "g____":
                current_guess = "CHAFF"
            elif feedback == "g__gg":
                current_guess = "CHAIN"
            elif feedback == "g__yy":
                current_guess = "CHINA"
            elif feedback == "g_gg_":
                current_guess = "CILIA"
            elif feedback == "g_y__":
                current_guess = "CHALK"
            elif feedback == "g_y_y":
                current_guess = "CLANG"
            elif feedback == "g_yg_":
                current_guess = "CLAIM"
            elif feedback == "gg___":
                current_guess = "COCOA"
            elif feedback == "gg__y":
                current_guess = "CONGA"
            elif feedback == "gyy__":
                current_guess = "CLOAK"
            elif feedback == "y____":
                current_guess = "AMUCK"
            elif feedback == "y___y":
                current_guess = "KNACK"
            elif feedback == "y__yy":
                current_guess = "ACING"
            elif feedback == "y_gy_":
                current_guess = "LILAC"
            elif feedback == "y_y__":
                current_guess = "BLACK"
            elif feedback == "y_yy_":
                current_guess = "ILIAC"
            elif feedback == "yg___":
                current_guess = "MOCHA"
            elif feedback == "ygy__":
                current_guess = "FALLS"
            elif feedback == "yy___":
                current_guess = "ACHOO"
            elif feedback == "yy__y":
                current_guess = "ANCHO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COMBO":
            if feedback == "ggg__":
                current_guess = "COMFY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COMET":
            if feedback == "___gg":
                current_guess = "BEGET"
            elif feedback == "__ggg":
                current_guess = "UNMET"
            elif feedback == "_y_gy":
                current_guess = "OFTEN"
            elif feedback == "gg_gg":
                current_guess = "COVET"
            elif feedback == "yy_gg":
                current_guess = "OCTET"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COMFY":
            if feedback == "_____":
                current_guess = "WHIZZ"
            elif feedback == "____g":
                current_guess = "WHINY"
            elif feedback == "____y":
                current_guess = "VINYL"
            elif feedback == "___g_":
                current_guess = "WHIFF"
            elif feedback == "__y_g":
                current_guess = "MILKY"
            elif feedback == "__yyg":
                current_guess = "FILMY"
            elif feedback == "_g___":
                current_guess = "POLIO"
            elif feedback == "_g_y_":
                current_guess = "FOLIO"
            elif feedback == "_y___":
                current_guess = "ONION"
            elif feedback == "_yg__":
                current_guess = "LIMBO"
            elif feedback == "g____":
                current_guess = "CHICK"
            elif feedback == "g_y__":
                current_guess = "CHIMP"
            elif feedback == "gg___":
                current_guess = "COLIC"
            elif feedback == "gy___":
                current_guess = "CHINO"
            elif feedback == "y____":
                current_guess = "WHICH"
            elif feedback == "y__y_":
                current_guess = "FILCH"
            elif feedback == "yg_y_":
                current_guess = "FOLIC"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COMIC":
            if feedback == "__ggg":
                current_guess = "MIMIC"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CONCH":
            if feedback == "_g__y":
                current_guess = "HOBBY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CONIC":
            if feedback == "_gggg":
                current_guess = "IONIC"
            elif feedback == "_yyy_":
                current_guess = "INBOX"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COOLY":
            if feedback == "_g___":
                current_guess = "MOTIF"
            elif feedback == "_g__g":
                current_guess = "POTTY"
            elif feedback == "_g_gg":
                current_guess = "HOTLY"
            elif feedback == "_g_yg":
                current_guess = "LOFTY"
            elif feedback == "_gg__":
                current_guess = "BOOTH"
            elif feedback == "_gg_g":
                current_guess = "BOOTY"
            elif feedback == "_gy__":
                current_guess = "MOTTO"
            elif feedback == "_gyy_":
                current_guess = "LOTTO"
            elif feedback == "yg___":
                current_guess = "BOTCH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COPEN":
            if feedback == "_g___":
                current_guess = "HOKUM"
            elif feedback == "_gg__":
                current_guess = "POPUP"
            elif feedback == "_y__y":
                current_guess = "UNBOX"
            elif feedback == "g____":
                current_guess = "CHUCK"
            elif feedback == "g___y":
                current_guess = "CHUNK"
            elif feedback == "g_y__":
                current_guess = "CHUMP"
            elif feedback == "gg___":
                current_guess = "COUCH"
            elif feedback == "gy___":
                current_guess = "CHOUX"
            elif feedback == "yg___":
                current_guess = "VOUCH"
            elif feedback == "ygy__":
                current_guess = "POUCH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CORAL":
            if feedback == "_gggg":
                current_guess = "MORAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CORGI":
            if feedback == "gyg_y":
                current_guess = "CURIO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CORKY":
            if feedback == "ggg_g":
                current_guess = "CORNY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COUGH":
            if feedback == "_____":
                current_guess = "VERSE"
            elif feedback == "__y__":
                current_guess = "NURSE"
            elif feedback == "_g___":
                current_guess = "WORSE"
            elif feedback == "_g__y":
                current_guess = "HORSE"
            elif feedback == "_g_y_":
                current_guess = "GORSE"
            elif feedback == "g_y__":
                current_guess = "CURSE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COURT":
            if feedback == "___gg":
                current_guess = "EVERT"
            elif feedback == "___gy":
                current_guess = "ENTRY"
            elif feedback == "___yg":
                current_guess = "AUMIL"
            elif feedback == "___yy":
                current_guess = "DENIM"
            elif feedback == "__gyg":
                current_guess = "ERUPT"
            elif feedback == "__yyg":
                current_guess = "REBUT"
            elif feedback == "__yyy":
                current_guess = "UTTER"
            elif feedback == "_g_yy":
                current_guess = "VOTER"
            elif feedback == "_y_gg":
                current_guess = "OVERT"
            elif feedback == "_y_gy":
                current_guess = "METRO"
            elif feedback == "_y_yg":
                current_guess = "REPOT"
            elif feedback == "_y_yy":
                current_guess = "OTHER"
            elif feedback == "_yyyy":
                current_guess = "OUTER"
            elif feedback == "g__yg":
                current_guess = "CREPT"
            elif feedback == "g_gyg":
                current_guess = "CRUET"
            elif feedback == "g_yyy":
                current_guess = "CUTER"
            elif feedback == "y__yg":
                current_guess = "ERECT"
            elif feedback == "y__yy":
                current_guess = "RETCH"
            elif feedback == "y_yyg":
                current_guess = "RECUT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COVEN":
            if feedback == "___gg":
                current_guess = "QUEEN"
            elif feedback == "__ggg":
                current_guess = "GIVEN"
            elif feedback == "__ygg":
                current_guess = "VIXEN"
            elif feedback == "_g_gg":
                current_guess = "WOKEN"
            elif feedback == "_gggg":
                current_guess = "WOVEN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COVER":
            if feedback == "gg_gg":
                current_guess = "COWER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COWLS":
            if feedback == "____g":
                current_guess = "GUESS"
            elif feedback == "____y":
                current_guess = "MESSY"
            elif feedback == "___yg":
                current_guess = "BLESS"
            elif feedback == "___yy":
                current_guess = "FLESH"
            elif feedback == "__g_y":
                current_guess = "NEWSY"
            elif feedback == "_g__y":
                current_guess = "POESY"
            elif feedback == "_g_yg":
                current_guess = "LOESS"
            elif feedback == "_y__y":
                current_guess = "QUESO"
            elif feedback == "g___g":
                current_guess = "CHESS"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "COYLY":
            if feedback == "_g_gg":
                current_guess = "NOBLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CRACK":
            if feedback == "ggg__":
                current_guess = "CRAZY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CRAFT":
            if feedback == "_gggg":
                current_guess = "DRAFT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CREEK":
            if feedback == "gggg_":
                current_guess = "CREEP"
            elif feedback == "gy_g_":
                current_guess = "CYBER"
            elif feedback == "gygg_":
                current_guess = "CHEER"
            elif feedback == "yyy__":
                current_guess = "RECUR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CREME":
            if feedback == "_y__g":
                current_guess = "RUBLE"
            elif feedback == "_y_gg":
                current_guess = "RHYME"
            elif feedback == "_yg_g":
                current_guess = "WHERE"
            elif feedback == "_yy_g":
                current_guess = "REVUE"
            elif feedback == "yy__g":
                current_guess = "LUCRE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CREPE":
            if feedback == "_yyyg":
                current_guess = "RUPEE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CREST":
            if feedback == "_gggg":
                current_guess = "WREST"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CRIER":
            if feedback == "y_ggg":
                current_guess = "ICIER"
            elif feedback == "y_ygg":
                current_guess = "NICER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CRIME":
            if feedback == "_gg_g":
                current_guess = "BRIBE"
            elif feedback == "_gggg":
                current_guess = "GRIME"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CROCK":
            if feedback == "ggg__":
                current_guess = "CROUP"
            elif feedback == "gyg__":
                current_guess = "CHOIR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CUBIC":
            if feedback == "_gggg":
                current_guess = "PUBIC"
            elif feedback == "gg_g_":
                current_guess = "CUMIN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CUING":
            if feedback == "_____":
                current_guess = "TODDY"
            elif feedback == "___gg":
                current_guess = "THONG"
            elif feedback == "__g__":
                current_guess = "TWILL"
            elif feedback == "__g_y":
                current_guess = "THIGH"
            elif feedback == "__gg_":
                current_guess = "THINK"
            elif feedback == "__ggg":
                current_guess = "THING"
            elif feedback == "__y__":
                current_guess = "TIMID"
            elif feedback == "__y_y":
                current_guess = "TIGHT"
            elif feedback == "__yg_":
                current_guess = "TINNY"
            elif feedback == "__yy_":
                current_guess = "TOXIN"
            elif feedback == "_g___":
                current_guess = "ABETS"
            elif feedback == "_gy__":
                current_guess = "TULIP"
            elif feedback == "_y___":
                current_guess = "THUMB"
            elif feedback == "_y__y":
                current_guess = "TOUGH"
            elif feedback == "y_g__":
                current_guess = "THICK"
            elif feedback == "y_y__":
                current_guess = "TOPIC"
            elif feedback == "y_yy_":
                current_guess = "TONIC"
            elif feedback == "ygyy_":
                current_guess = "TUNIC"
            elif feedback == "yy___":
                current_guess = "TOUCH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CUPID":
            if feedback == "_g_gg":
                current_guess = "HUMID"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CURRY":
            if feedback == "ggg_g":
                current_guess = "CURVY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CURVE":
            if feedback == "_gg_g":
                current_guess = "PUREE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "CYMOL":
            if feedback == "_____":
                current_guess = "PARKA"
            elif feedback == "____y":
                current_guess = "LARVA"
            elif feedback == "___g_":
                current_guess = "BARON"
            elif feedback == "___y_":
                current_guess = "BURRO"
            elif feedback == "___yy":
                current_guess = "WORLD"
            elif feedback == "__y__":
                current_guess = "KARMA"
            elif feedback == "__yg_":
                current_guess = "MORON"
            elif feedback == "__yy_":
                current_guess = "FORUM"
            elif feedback == "_gy__":
                current_guess = "MYRRH"
            elif feedback == "_y___":
                current_guess = "PARRY"
            elif feedback == "_y__y":
                current_guess = "BURLY"
            elif feedback == "_y_y_":
                current_guess = "DWANG"
            elif feedback == "_y_yy":
                current_guess = "LORDY"
            elif feedback == "_yy__":
                current_guess = "MARRY"
            elif feedback == "_yyy_":
                current_guess = "WORMY"
            elif feedback == "g__g_":
                current_guess = "CAROB"
            elif feedback == "g__gg":
                current_guess = "CAROL"
            elif feedback == "g__y_":
                current_guess = "CARGO"
            elif feedback == "g_yg_":
                current_guess = "CAROM"
            elif feedback == "gy___":
                current_guess = "CARNY"
            elif feedback == "gy__y":
                current_guess = "CURLY"
            elif feedback == "gy_y_":
                current_guess = "CORKY"
            elif feedback == "y____":
                current_guess = "PARCH"
            elif feedback == "y___y":
                current_guess = "LARCH"
            elif feedback == "y__y_":
                current_guess = "BORIC"
            elif feedback == "y_y__":
                current_guess = "MARCH"
            elif feedback == "yg__y":
                current_guess = "LYRIC"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DALED":
            if feedback == "gg___":
                current_guess = "DAFFY"
            elif feedback == "gg__y":
                current_guess = "DADDY"
            elif feedback == "ggg__":
                current_guess = "DALLY"
            elif feedback == "ggy__":
                current_guess = "DAILY"
            elif feedback == "yg___":
                current_guess = "BAWDY"
            elif feedback == "yg__y":
                current_guess = "PADDY"
            elif feedback == "ygg__":
                current_guess = "BALDY"
            elif feedback == "ygy__":
                current_guess = "BADLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DEALT":
            if feedback == "_yggg":
                current_guess = "EXALT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DEATH":
            if feedback == "_ggg_":
                current_guess = "MEATY"
            elif feedback == "_gggg":
                current_guess = "HEATH"
            elif feedback == "_ggy_":
                current_guess = "BEAUT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DEBIT":
            if feedback == "gg_yy":
                current_guess = "DEITY"
            elif feedback == "yy_yg":
                current_guess = "EDICT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DEBUG":
            if feedback == "gg__g":
                current_guess = "DEFOG"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DEBUT":
            if feedback == "gg__y":
                current_guess = "DETOX"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DECAF":
            if feedback == "gggg_":
                current_guess = "DECAY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DECOY":
            if feedback == "gg__g":
                current_guess = "DEIFY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DEFER":
            if feedback == "g__gg":
                current_guess = "DRYER"
            elif feedback == "gg__g":
                current_guess = "DEMUR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DEIGN":
            if feedback == "gg__g":
                current_guess = "DEMON"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DENIM":
            if feedback == "_g___":
                current_guess = "PETER"
            elif feedback == "_g__y":
                current_guess = "METER"
            elif feedback == "_y___":
                current_guess = "ETHER"
            elif feedback == "_y_y_":
                current_guess = "BITER"
            elif feedback == "_y_yy":
                current_guess = "MITER"
            elif feedback == "_yy__":
                current_guess = "ENTER"
            elif feedback == "_yyy_":
                current_guess = "INTER"
            elif feedback == "gg___":
                current_guess = "DETER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DEPOT":
            if feedback == "ggg_y":
                current_guess = "DEPTH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DEVIL":
            if feedback == "gy__g":
                current_guess = "DWELL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DEVON":
            if feedback == "g____":
                current_guess = "DIPPY"
            elif feedback == "g___y":
                current_guess = "DINKY"
            elif feedback == "g_g__":
                current_guess = "DIVVY"
            elif feedback == "y____":
                current_guess = "BIDDY"
            elif feedback == "y___y":
                current_guess = "WINDY"
            elif feedback == "y__g_":
                current_guess = "WIDOW"
            elif feedback == "y__y_":
                current_guess = "KIDDO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DIARY":
            if feedback == "g_gg_":
                current_guess = "DWARF"
            elif feedback == "g_gy_":
                current_guess = "DRAMA"
            elif feedback == "y_ygy":
                current_guess = "HYDRA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DICEY":
            if feedback == "g__gg":
                current_guess = "DOPEY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DIGHT":
            if feedback == "____g":
                current_guess = "QUEST"
            elif feedback == "___yg":
                current_guess = "CHEST"
            elif feedback == "__y_g":
                current_guess = "GUEST"
            elif feedback == "_y__g":
                current_guess = "EXIST"
            elif feedback == "_y_yg":
                current_guess = "HEIST"
            elif feedback == "gy__g":
                current_guess = "DEIST"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DILLY":
            if feedback == "gg_gg":
                current_guess = "DIMLY"
            elif feedback == "yyygy":
                current_guess = "IDYLL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DINER":
            if feedback == "gg_gg":
                current_guess = "DIVER"
            elif feedback == "gy_gg":
                current_guess = "DRIER"
            elif feedback == "gy_gy":
                current_guess = "DRIED"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DINGO":
            if feedback == "gggg_":
                current_guess = "DINGY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DIPPY":
            if feedback == "gg__g":
                current_guess = "DIZZY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DISHY":
            if feedback == "__g__":
                current_guess = "BOSOM"
            elif feedback == "__y__":
                current_guess = "SCOFF"
            elif feedback == "__y_g":
                current_guess = "SOGGY"
            elif feedback == "__yyg":
                current_guess = "SHOWY"
            elif feedback == "_gggg":
                current_guess = "FISHY"
            elif feedback == "ggg__":
                current_guess = "DISCO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DITTY":
            if feedback == "ggg__":
                current_guess = "DITCH"
            elif feedback == "ggg_g":
                current_guess = "DITZY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DODGE":
            if feedback == "_g_gg":
                current_guess = "GOUGE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DODGY":
            if feedback == "gg_gg":
                current_guess = "DOGGY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DOGAN":
            if feedback == "___g_":
                current_guess = "TUBAL"
            elif feedback == "___gg":
                current_guess = "TITAN"
            elif feedback == "___y_":
                current_guess = "TIBIA"
            elif feedback == "___yg":
                current_guess = "TWAIN"
            elif feedback == "___yy":
                current_guess = "THANK"
            elif feedback == "__yyy":
                current_guess = "TWANG"
            elif feedback == "_g_g_":
                current_guess = "TOPAZ"
            elif feedback == "_g_gy":
                current_guess = "TONAL"
            elif feedback == "_gyyy":
                current_guess = "TONGA"
            elif feedback == "y__g_":
                current_guess = "TIDAL"
            elif feedback == "yg_g_":
                current_guess = "TODAY"
            elif feedback == "yg_y_":
                current_guess = "TOADY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DOGMA":
            if feedback == "_g_gg":
                current_guess = "MOMMA"
            elif feedback == "_g_gy":
                current_guess = "FOAMY"
            elif feedback == "yg__g":
                current_guess = "VODKA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DOING":
            if feedback == "g_ggg":
                current_guess = "DYING"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DOLCI":
            if feedback == "_____":
                current_guess = "RUMPY"
            elif feedback == "____g":
                current_guess = "REIKI"
            elif feedback == "____y":
                current_guess = "PINKY"
            elif feedback == "___g_":
                current_guess = "WRECK"
            elif feedback == "___y_":
                current_guess = "CREEK"
            elif feedback == "___yy":
                current_guess = "CRIER"
            elif feedback == "__g__":
                current_guess = "RULER"
            elif feedback == "__g_y":
                current_guess = "FILER"
            elif feedback == "__gyy":
                current_guess = "RELIC"
            elif feedback == "__y__":
                current_guess = "BEVER"
            elif feedback == "__y_y":
                current_guess = "AFION"
            elif feedback == "__yy_":
                current_guess = "CLERK"
            elif feedback == "_g___":
                current_guess = "WHOMP"
            elif feedback == "_g_y_":
                current_guess = "COVER"
            elif feedback == "_gy__":
                current_guess = "ADVEW"
            elif feedback == "_y___":
                current_guess = "OFFER"
            elif feedback == "_y_y_":
                current_guess = "OCHER"
            elif feedback == "_yg__":
                current_guess = "OGLER"
            elif feedback == "_yg_y":
                current_guess = "OILER"
            elif feedback == "g____":
                current_guess = "DEFER"
            elif feedback == "g___y":
                current_guess = "DINER"
            elif feedback == "g__g_":
                current_guess = "DRECK"
            elif feedback == "g__y_":
                current_guess = "DECRY"
            elif feedback == "g__yy":
                current_guess = "DICER"
            elif feedback == "gg___":
                current_guess = "DOPER"
            elif feedback == "gy_y_":
                current_guess = "DECOR"
            elif feedback == "y____":
                current_guess = "BEGUN"
            elif feedback == "y___y":
                current_guess = "BEDEW"
            elif feedback == "y__y_":
                current_guess = "CREED"
            elif feedback == "y__yy":
                current_guess = "CIDER"
            elif feedback == "y_g_y":
                current_guess = "IDLER"
            elif feedback == "y_y__":
                current_guess = "ELDER"
            elif feedback == "yg___":
                current_guess = "RODEO"
            elif feedback == "yg_y_":
                current_guess = "CODER"
            elif feedback == "yy___":
                current_guess = "ODDER"
            elif feedback == "yy_y_":
                current_guess = "CREDO"
            elif feedback == "yyy__":
                current_guess = "OLDER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DOLLY":
            if feedback == "yy_gg":
                current_guess = "ODDLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DOMED":
            if feedback == "g__g_":
                current_guess = "DWEEB"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DONUT":
            if feedback == "____g":
                current_guess = "FILMI"
            elif feedback == "____y":
                current_guess = "WIFTY"
            elif feedback == "___gy":
                current_guess = "CUTUP"
            elif feedback == "___yg":
                current_guess = "AGBAS"
            elif feedback == "___yy":
                current_guess = "BIGLY"
            elif feedback == "__g_y":
                current_guess = "MINTY"
            elif feedback == "__y_g":
                current_guess = "FLINT"
            elif feedback == "__y_y":
                current_guess = "NIFTY"
            elif feedback == "__ygg":
                current_guess = "INPUT"
            elif feedback == "__yyg":
                current_guess = "BLUNT"
            elif feedback == "__yyy":
                current_guess = "NUTTY"
            elif feedback == "_g__g":
                current_guess = "VOMIT"
            elif feedback == "_g__y":
                current_guess = "COOLY"
            elif feedback == "_g_yg":
                current_guess = "MOULT"
            elif feedback == "_g_yy":
                current_guess = "ACCOY"
            elif feedback == "_gg_y":
                current_guess = "MONTH"
            elif feedback == "_gy_g":
                current_guess = "JOINT"
            elif feedback == "_gy_y":
                current_guess = "NOTCH"
            elif feedback == "_gyyg":
                current_guess = "ACMES"
            elif feedback == "_y__g":
                current_guess = "PILOT"
            elif feedback == "_y__y":
                current_guess = "CLOTH"
            elif feedback == "_y_gg":
                current_guess = "CLOUT"
            elif feedback == "_y_yg":
                current_guess = "OUGHT"
            elif feedback == "_y_yy":
                current_guess = "OUTGO"
            elif feedback == "_yg_g":
                current_guess = "PINOT"
            elif feedback == "_yg_y":
                current_guess = "PINTO"
            elif feedback == "_ygyy":
                current_guess = "JUNTO"
            elif feedback == "_yy_g":
                current_guess = "INGOT"
            elif feedback == "_yyyy":
                current_guess = "FUTON"
            elif feedback == "g___g":
                current_guess = "DIGIT"
            elif feedback == "g___y":
                current_guess = "DITTY"
            elif feedback == "g__yy":
                current_guess = "DUTCH"
            elif feedback == "gg__y":
                current_guess = "DOTTY"
            elif feedback == "gg_yg":
                current_guess = "DOUBT"
            elif feedback == "gy__g":
                current_guess = "DIVOT"
            elif feedback == "gy__y":
                current_guess = "DITTO"
            elif feedback == "y___y":
                current_guess = "WIDTH"
            elif feedback == "yy__g":
                current_guess = "IDIOT"
            elif feedback == "yy_yy":
                current_guess = "OUTDO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DOPER":
            if feedback == "gg_gg":
                current_guess = "DOZER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DOUGH":
            if feedback == "__g__":
                current_guess = "JAUNT"
            elif feedback == "__g_y":
                current_guess = "HAUNT"
            elif feedback == "__gy_":
                current_guess = "GAUNT"
            elif feedback == "__yy_":
                current_guess = "GAMUT"
            elif feedback == "g_g__":
                current_guess = "DAUNT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DOWRY":
            if feedback == "yg_g_":
                current_guess = "GOURD"
            elif feedback == "yggyg":
                current_guess = "ROWDY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DRAIN":
            if feedback == "ggg_g":
                current_guess = "DRAWN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DRAKE":
            if feedback == "ggg_g":
                current_guess = "DRAPE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DRIFT":
            if feedback == "_gggg":
                current_guess = "GRIFT"
            elif feedback == "_gyyg":
                current_guess = "FRUIT"
            elif feedback == "_ygyg":
                current_guess = "FLIRT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DRILL":
            if feedback == "gg_g_":
                current_guess = "DRYLY"
            elif feedback == "ggy__":
                current_guess = "DRUID"
            elif feedback == "yyy__":
                current_guess = "RIGID"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DRINK":
            if feedback == "gg_gg":
                current_guess = "DRUNK"
            elif feedback == "yggg_":
                current_guess = "GRIND"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DROID":
            if feedback == "_gg_g":
                current_guess = "PROUD"
            elif feedback == "_yg_g":
                current_guess = "FJORD"
            elif feedback == "ggg__":
                current_guess = "DROLL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DROOL":
            if feedback == "gggg_":
                current_guess = "DROOP"
            elif feedback == "yggg_":
                current_guess = "BROOD"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DROSS":
            if feedback == "_gggg":
                current_guess = "GROSS"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DROVE":
            if feedback == "ygg_g":
                current_guess = "ERODE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DUCHY":
            if feedback == "ggg_g":
                current_guess = "DUCKY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DUMMY":
            if feedback == "gg__g":
                current_guess = "DUCHY"
            elif feedback == "ggg_g":
                current_guess = "DUMPY"
            elif feedback == "yg___":
                current_guess = "KUDZU"
            elif feedback == "yg__g":
                current_guess = "BUDDY"
            elif feedback == "ygy_g":
                current_guess = "MUDDY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DUMPS":
            if feedback == "_____":
                current_guess = "CHIVE"
            elif feedback == "___y_":
                current_guess = "PIECE"
            elif feedback == "__y__":
                current_guess = "CHIME"
            elif feedback == "_g___":
                current_guess = "JUICE"
            elif feedback == "_y_y_":
                current_guess = "PIQUE"
            elif feedback == "_yy__":
                current_guess = "IMBUE"
            elif feedback == "y____":
                current_guess = "CHIDE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DUMPY":
            if feedback == "_____":
                current_guess = "BELLE"
            elif feedback == "____y":
                current_guess = "CYCLE"
            elif feedback == "___y_":
                current_guess = "PLEBE"
            elif feedback == "__y__":
                current_guess = "MELEE"
            elif feedback == "_y___":
                current_guess = "FLUKE"
            elif feedback == "_yy__":
                current_guess = "FLUME"
            elif feedback == "_yyy_":
                current_guess = "PLUME"
            elif feedback == "g____":
                current_guess = "DELVE"
            elif feedback == "yy___":
                current_guess = "ELUDE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DWANG":
            if feedback == "_____":
                current_guess = "PORKY"
            elif feedback == "____y":
                current_guess = "PORGY"
            elif feedback == "___g_":
                current_guess = "HORNY"
            elif feedback == "_y___":
                current_guess = "WORRY"
            elif feedback == "g____":
                current_guess = "DORKY"
            elif feedback == "yy___":
                current_guess = "WORDY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "DYNEL":
            if feedback == "___g_":
                current_guess = "BICEP"
            elif feedback == "___gg":
                current_guess = "BEVUE"
            elif feedback == "___gy":
                current_guess = "BLEEP"
            elif feedback == "___y_":
                current_guess = "GECKO"
            elif feedback == "___yg":
                current_guess = "KVELL"
            elif feedback == "___yy":
                current_guess = "PHLOX"
            elif feedback == "__ggy":
                current_guess = "LINEN"
            elif feedback == "__gy_":
                current_guess = "VENOM"
            elif feedback == "__yg_":
                current_guess = "COVEN"
            elif feedback == "__ygg":
                current_guess = "INCEL"
            elif feedback == "__ygy":
                current_guess = "LIKEN"
            elif feedback == "__yy_":
                current_guess = "BEGIN"
            elif feedback == "__yyg":
                current_guess = "KNELL"
            elif feedback == "__yyy":
                current_guess = "FELON"
            elif feedback == "_gyg_":
                current_guess = "HYMEN"
            elif feedback == "_gyy_":
                current_guess = "EYING"
            elif feedback == "_y_g_":
                current_guess = "CHOMP"
            elif feedback == "_y_gg":
                current_guess = "YOKEL"
            elif feedback == "_y_gy":
                current_guess = "GLUEY"
            elif feedback == "_y_y_":
                current_guess = "APEEK"
            elif feedback == "_y_yy":
                current_guess = "BELLY"
            elif feedback == "_ygg_":
                current_guess = "BLIMP"
            elif feedback == "_ygy_":
                current_guess = "PENNY"
            elif feedback == "_yyy_":
                current_guess = "ENJOY"
            elif feedback == "_yyyy":
                current_guess = "NEWLY"
            elif feedback == "g__g_":
                current_guess = "DOMED"
            elif feedback == "g__gg":
                current_guess = "DOWEL"
            elif feedback == "g__y_":
                current_guess = "DEBUG"
            elif feedback == "g__yg":
                current_guess = "DEVIL"
            elif feedback == "g_gy_":
                current_guess = "DENIM"
            elif feedback == "g_yg_":
                current_guess = "DOZEN"
            elif feedback == "g_yy_":
                current_guess = "DEIGN"
            elif feedback == "gy_g_":
                current_guess = "DICEY"
            elif feedback == "gy_y_":
                current_guess = "DECOY"
            elif feedback == "y__g_":
                current_guess = "MOPED"
            elif feedback == "y__gg":
                current_guess = "MODEL"
            elif feedback == "y__gy":
                current_guess = "BLEED"
            elif feedback == "y__y_":
                current_guess = "MEDIC"
            elif feedback == "y__yy":
                current_guess = "FIELD"
            elif feedback == "y_yg_":
                current_guess = "UNFED"
            elif feedback == "y_ygy":
                current_guess = "OLDEN"
            elif feedback == "y_yy_":
                current_guess = "FIEND"
            elif feedback == "y_yyy":
                current_guess = "BLEND"
            elif feedback == "yy_gg":
                current_guess = "YODEL"
            elif feedback == "yy_y_":
                current_guess = "EDIFY"
            elif feedback == "yy_yy":
                current_guess = "YIELD"
            elif feedback == "yygy_":
                current_guess = "BENDY"
            elif feedback == "yyyy_":
                current_guess = "NEEDY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "EASEL":
            if feedback == "_gyg_":
                current_guess = "SAMEY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "EDIFY":
            if feedback == "yy__g":
                current_guess = "WEEDY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ELATE":
            if feedback == "_gggg":
                current_guess = "PLATE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "EMBOW":
            if feedback == "_____":
                current_guess = "HATCH"
            elif feedback == "____y":
                current_guess = "WATCH"
            elif feedback == "__y__":
                current_guess = "BATCH"
            elif feedback == "_y___":
                current_guess = "MATCH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "EMCEE":
            if feedback == "g___g":
                current_guess = "EXUDE"
            elif feedback == "g_y_g":
                current_guess = "EDUCE"
            elif feedback == "y___g":
                current_guess = "QUEUE"
            elif feedback == "y__yg":
                current_guess = "PEEVE"
            elif feedback == "y_y_g":
                current_guess = "DEUCE"
            elif feedback == "yy__g":
                current_guess = "FEMME"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "EMPTY":
            if feedback == "y_yy_":
                current_guess = "GETUP"
            elif feedback == "yyyy_":
                current_guess = "KEMPT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ENEMA":
            if feedback == "__gyg":
                current_guess = "OMEGA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ENJOY":
            if feedback == "gg__g":
                current_guess = "ENEMY"
            elif feedback == "gg_gg":
                current_guess = "ENVOY"
            elif feedback == "gy_yg":
                current_guess = "EBONY"
            elif feedback == "yy__g":
                current_guess = "VEINY"
            elif feedback == "yy_yg":
                current_guess = "PEONY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ENSUE":
            if feedback == "yggyg":
                current_guess = "UNSEE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ENTRY":
            if feedback == "y_gg_":
                current_guess = "PETRI"
            elif feedback == "y_ggg":
                current_guess = "RETRY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ESTER":
            if feedback == "yyy_y":
                current_guess = "STERN"
            elif feedback == "yyygg":
                current_guess = "STEER"
            elif feedback == "yyygy":
                current_guess = "RESET"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "EVERT":
            if feedback == "__ggg":
                current_guess = "INERT"
            elif feedback == "g_ggg":
                current_guess = "EXERT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "EXCEL":
            if feedback == "gg_gg":
                current_guess = "EXPEL"
            elif feedback == "y__gg":
                current_guess = "WHEEL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "EXULT":
            if feedback == "g__yg":
                current_guess = "ELECT"
            elif feedback == "g__yy":
                current_guess = "ETHYL"
            elif feedback == "gg_yy":
                current_guess = "EXTOL"
            elif feedback == "y__gg":
                current_guess = "KNELT"
            elif feedback == "y__yg":
                current_guess = "CLEFT"
            elif feedback == "y__yy":
                current_guess = "LEFTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FADER":
            if feedback == "_g_gg":
                current_guess = "RAVER"
            elif feedback == "_g_gy":
                current_guess = "RAVEN"
            elif feedback == "_gggg":
                current_guess = "WADER"
            elif feedback == "gg_gg":
                current_guess = "FAKER"
            elif feedback == "yg_gg":
                current_guess = "WAFER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FAIRY":
            if feedback == "_gggg":
                current_guess = "HAIRY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FALLS":
            if feedback == "_yy__":
                current_guess = "VOCAL"
            elif feedback == "_yyy_":
                current_guess = "LOCAL"
            elif feedback == "gyy__":
                current_guess = "FOCAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FAULT":
            if feedback == "_gggg":
                current_guess = "VAULT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FAUNA":
            if feedback == "_g_gg":
                current_guess = "MANNA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FEHME":
            if feedback == "_____":
                current_guess = "JOLLY"
            elif feedback == "___y_":
                current_guess = "MOLLY"
            elif feedback == "__y__":
                current_guess = "HOLLY"
            elif feedback == "g____":
                current_guess = "FOLLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FELON":
            if feedback == "_gggg":
                current_guess = "MELON"
            elif feedback == "_gygg":
                current_guess = "LEMON"
            elif feedback == "yyy_g":
                current_guess = "ELFIN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FERAL":
            if feedback == "_ggg_":
                current_guess = "RERAN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FETAL":
            if feedback == "_gggg":
                current_guess = "METAL"
            elif feedback == "_gyyy":
                current_guess = "DELTA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FEVER":
            if feedback == "_g_gg":
                current_guess = "NEWER"
            elif feedback == "_gggg":
                current_guess = "NEVER"
            elif feedback == "_y_gy":
                current_guess = "GREEN"
            elif feedback == "gg_gg":
                current_guess = "FEWER"
            elif feedback == "gy_gg":
                current_guess = "FREER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FIELD":
            if feedback == "_gggg":
                current_guess = "WIELD"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FIEND":
            if feedback == "__ggg":
                current_guess = "UPEND"
            elif feedback == "__yyy":
                current_guess = "ENDOW"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FILER":
            if feedback == "_gggg":
                current_guess = "MILER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FILLY":
            if feedback == "_gggg":
                current_guess = "HILLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FILMI":
            if feedback == "_g___":
                current_guess = "WIGHT"
            elif feedback == "_g_y_":
                current_guess = "MIGHT"
            elif feedback == "_gy__":
                current_guess = "LIGHT"
            elif feedback == "_gy_y":
                current_guess = "LICIT"
            elif feedback == "_gyyy":
                current_guess = "LIMIT"
            elif feedback == "gg___":
                current_guess = "FIGHT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FINER":
            if feedback == "_gggg":
                current_guess = "MINER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FIZZY":
            if feedback == "yg__g":
                current_guess = "JIFFY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FLANK":
            if feedback == "_gggg":
                current_guess = "PLANK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FLASH":
            if feedback == "_gggg":
                current_guess = "SLASH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FLASK":
            if feedback == "_ggg_":
                current_guess = "GLASS"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FLICK":
            if feedback == "_gg__":
                current_guess = "BLIMP"
            elif feedback == "_gg_g":
                current_guess = "BLINK"
            elif feedback == "_gggg":
                current_guess = "CLICK"
            elif feedback == "_ggy_":
                current_guess = "CLIMB"
            elif feedback == "_ggyg":
                current_guess = "CLINK"
            elif feedback == "yggy_":
                current_guess = "CLIFF"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FLINT":
            if feedback == "__yyg":
                current_guess = "NIGHT"
            elif feedback == "_gggg":
                current_guess = "GLINT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FLOSS":
            if feedback == "_gggg":
                current_guess = "GLOSS"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FLUTE":
            if feedback == "_gggg":
                current_guess = "GLUTE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FLYER":
            if feedback == "_y_gg":
                current_guess = "LUGER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FOIST":
            if feedback == "_gggg":
                current_guess = "JOIST"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FORAY":
            if feedback == "_ggg_":
                current_guess = "BORAX"
            elif feedback == "_gggg":
                current_guess = "MORAY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FORCE":
            if feedback == "_gg_g":
                current_guess = "HORDE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FORUM":
            if feedback == "_gg_y":
                current_guess = "MORPH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FOUND":
            if feedback == "_gggg":
                current_guess = "WOUND"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FOUNT":
            if feedback == "____g":
                current_guess = "SPILT"
            elif feedback == "____y":
                current_guess = "SILTY"
            elif feedback == "___gg":
                current_guess = "STINT"
            elif feedback == "___gy":
                current_guess = "STING"
            elif feedback == "___yy":
                current_guess = "SYNTH"
            elif feedback == "__g_y":
                current_guess = "ADEEM"
            elif feedback == "__ggg":
                current_guess = "SHUNT"
            elif feedback == "__ggy":
                current_guess = "STUNG"
            elif feedback == "__y_y":
                current_guess = "ADLIB"
            elif feedback == "_g__g":
                current_guess = "POSIT"
            elif feedback == "_g__y":
                current_guess = "SOOTH"
            elif feedback == "_gg_y":
                current_guess = "SOUTH"
            elif feedback == "_gy_y":
                current_guess = "LOTUS"
            elif feedback == "_y__g":
                current_guess = "SCOOT"
            elif feedback == "_y__y":
                current_guess = "APIOL"
            elif feedback == "_y_gy":
                current_guess = "STONY"
            elif feedback == "_y_yg":
                current_guess = "SNOOT"
            elif feedback == "_yy_g":
                current_guess = "CAPHS"
            elif feedback == "_yy_y":
                current_guess = "GUSTO"
            elif feedback == "_yyyg":
                current_guess = "SNOUT"
            elif feedback == "g_y_y":
                current_guess = "FUSTY"
            elif feedback == "y___g":
                current_guess = "SHIFT"
            elif feedback == "y___y":
                current_guess = "STIFF"
            elif feedback == "y_g_y":
                current_guess = "STUFF"
            elif feedback == "yg__y":
                current_guess = "SOFTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FRACK":
            if feedback == "_gggg":
                current_guess = "WRACK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FRAIL":
            if feedback == "_gg_g":
                current_guess = "CRAWL"
            elif feedback == "_gggg":
                current_guess = "GRAIL"
            elif feedback == "_yyyg":
                current_guess = "RIVAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FRANC":
            if feedback == "_ggg_":
                current_guess = "PRANK"
            elif feedback == "_gggy":
                current_guess = "CRANK"
            elif feedback == "gggg_":
                current_guess = "FRANK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FRIED":
            if feedback == "_gggg":
                current_guess = "PRIED"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FUDGE":
            if feedback == "_gggg":
                current_guess = "JUDGE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FUGLY":
            if feedback == "_____":
                current_guess = "PRIMP"
            elif feedback == "____g":
                current_guess = "PRIVY"
            elif feedback == "___g_":
                current_guess = "KRILL"
            elif feedback == "___gg":
                current_guess = "WRYLY"
            elif feedback == "___y_":
                current_guess = "WHIRL"
            elif feedback == "__y_g":
                current_guess = "GRIMY"
            elif feedback == "__yg_":
                current_guess = "GRILL"
            elif feedback == "_g___":
                current_guess = "QUIRK"
            elif feedback == "_g__g":
                current_guess = "RUMMY"
            elif feedback == "_gg_g":
                current_guess = "RUGBY"
            elif feedback == "_y_y_":
                current_guess = "BLURB"
            elif feedback == "_yy__":
                current_guess = "GRUMP"
            elif feedback == "g____":
                current_guess = "FRIZZ"
            elif feedback == "g__g_":
                current_guess = "FRILL"
            elif feedback == "gy___":
                current_guess = "FRUMP"
            elif feedback == "yyy__":
                current_guess = "GRUFF"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FUNKY":
            if feedback == "_g_gg":
                current_guess = "YUCKY"
            elif feedback == "_gggg":
                current_guess = "JUNKY"
            elif feedback == "gg__g":
                current_guess = "FUZZY"
            elif feedback == "ggg_g":
                current_guess = "FUNNY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FUROR":
            if feedback == "__gg_":
                current_guess = "BORON"
            elif feedback == "_gggg":
                current_guess = "JUROR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FURRY":
            if feedback == "_gggg":
                current_guess = "HURRY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "FUSSY":
            if feedback == "__ggg":
                current_guess = "BOSSY"
            elif feedback == "_gggg":
                current_guess = "GUSSY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GABBY":
            if feedback == "gg__g":
                current_guess = "GAWKY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GATOR":
            if feedback == "_gg_y":
                current_guess = "RATTY"
            elif feedback == "_ggyy":
                current_guess = "RATIO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GAUGE":
            if feedback == "ggg_g":
                current_guess = "GAUZE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GAYER":
            if feedback == "gg_gg":
                current_guess = "GAZER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GECKO":
            if feedback == "_g__g":
                current_guess = "MEZZO"
            elif feedback == "_g__y":
                current_guess = "BEBOP"
            elif feedback == "_gy__":
                current_guess = "BEECH"
            elif feedback == "_y___":
                current_guess = "EQUIP"
            elif feedback == "_y__y":
                current_guess = "EMOJI"
            elif feedback == "_y_yy":
                current_guess = "EBOOK"
            elif feedback == "_yy_g":
                current_guess = "CHEMO"
            elif feedback == "_yy_y":
                current_guess = "EPOCH"
            elif feedback == "_yyy_":
                current_guess = "CHECK"
            elif feedback == "yg___":
                current_guess = "WEIGH"
            elif feedback == "yg__y":
                current_guess = "BEFOG"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GEESE":
            if feedback == "_g_gg":
                current_guess = "SENSE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GENIO":
            if feedback == "_g___":
                current_guess = "VERVE"
            elif feedback == "_g_g_":
                current_guess = "EERIE"
            elif feedback == "_gy__":
                current_guess = "NERVE"
            elif feedback == "_y___":
                current_guess = "CURVE"
            elif feedback == "_y__y":
                current_guess = "FORCE"
            elif feedback == "_yy_y":
                current_guess = "BORNE"
            elif feedback == "gy__y":
                current_guess = "GORGE"
            elif feedback == "yg___":
                current_guess = "MERGE"
            elif feedback == "yy___":
                current_guess = "PURGE"
            elif feedback == "yy__y":
                current_guess = "FORGE"
            elif feedback == "yy_y_":
                current_guess = "DIRGE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GIRTH":
            if feedback == "_gggg":
                current_guess = "MIRTH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GLACE":
            if feedback == "ggg_g":
                current_guess = "GLAZE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GLAMP":
            if feedback == "__y__":
                current_guess = "FADER"
            elif feedback == "__y_y":
                current_guess = "CARVY"
            elif feedback == "__yy_":
                current_guess = "MAKER"
            elif feedback == "_yy__":
                current_guess = "BALER"
            elif feedback == "_yy_y":
                current_guess = "PALER"
            elif feedback == "_yyy_":
                current_guess = "LAMER"
            elif feedback == "g_y__":
                current_guess = "GAYER"
            elif feedback == "g_yy_":
                current_guess = "GAMER"
            elif feedback == "y_y__":
                current_guess = "ARERE"
            elif feedback == "y_y_y":
                current_guess = "PAGER"
            elif feedback == "yyy__":
                current_guess = "LAGER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GLAND":
            if feedback == "__g__":
                current_guess = "KACHA"
            elif feedback == "__g_y":
                current_guess = "EVADE"
            elif feedback == "__gg_":
                current_guess = "INANE"
            elif feedback == "__gy_":
                current_guess = "KNAVE"
            elif feedback == "__y__":
                current_guess = "ABOVE"
            elif feedback == "__y_y":
                current_guess = "ABIDE"
            elif feedback == "__yy_":
                current_guess = "ANIME"
            elif feedback == "__yyy":
                current_guess = "ANODE"
            elif feedback == "_gg__":
                current_guess = "CHIMB"
            elif feedback == "_gg_y":
                current_guess = "BLADE"
            elif feedback == "_ggg_":
                current_guess = "PLANE"
            elif feedback == "_gy__":
                current_guess = "ALIKE"
            elif feedback == "_gyg_":
                current_guess = "ALONE"
            elif feedback == "_yg__":
                current_guess = "LEAVE"
            elif feedback == "_yy__":
                current_guess = "AMBLE"
            elif feedback == "_yy_y":
                current_guess = "ADDLE"
            elif feedback == "_yyy_":
                current_guess = "ANKLE"
            elif feedback == "ggg__":
                current_guess = "GLACE"
            elif feedback == "ggg_y":
                current_guess = "GLADE"
            elif feedback == "y_g__":
                current_guess = "AGAPE"
            elif feedback == "y_g_y":
                current_guess = "ADAGE"
            elif feedback == "ygy__":
                current_guess = "ALGAE"
            elif feedback == "yyy__":
                current_guess = "AGILE"
            elif feedback == "yyyy_":
                current_guess = "ANGLE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GLIDE":
            if feedback == "gyg_g":
                current_guess = "GUILE"
            elif feedback == "yyy_g":
                current_guess = "BILGE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GLOBE":
            if feedback == "ggg_g":
                current_guess = "GLOVE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GLOOM":
            if feedback == "gg___":
                current_guess = "GLYPH"
            elif feedback == "ggg__":
                current_guess = "GLOWY"
            elif feedback == "gggg_":
                current_guess = "GLOOP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GLUEY":
            if feedback == "_y_gg":
                current_guess = "HOLEY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GLUME":
            if feedback == "_____":
                current_guess = "JAZZY"
            elif feedback == "___g_":
                current_guess = "JAMMY"
            elif feedback == "___y_":
                current_guess = "VAMPY"
            elif feedback == "_y___":
                current_guess = "BALKY"
            elif feedback == "_y_g_":
                current_guess = "BALMY"
            elif feedback == "g____":
                current_guess = "GABBY"
            elif feedback == "g_g__":
                current_guess = "GAUZY"
            elif feedback == "gy___":
                current_guess = "GAILY"
            elif feedback == "y____":
                current_guess = "BAGGY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GNARL":
            if feedback == "_yyyy":
                current_guess = "LUNAR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GONAD":
            if feedback == "_gygg":
                current_guess = "NOMAD"
            elif feedback == "gggy_":
                current_guess = "GONNA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GOOFY":
            if feedback == "ggg_g":
                current_guess = "GOOPY"
            elif feedback == "ggy__":
                current_guess = "GONZO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GRAFT":
            if feedback == "ggg_g":
                current_guess = "GRANT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GRAND":
            if feedback == "_gg__":
                current_guess = "VOCAB"
            elif feedback == "_gg_y":
                current_guess = "DRAKE"
            elif feedback == "_ggg_":
                current_guess = "CRANE"
            elif feedback == "_yg__":
                current_guess = "BLARE"
            elif feedback == "_yy__":
                current_guess = "AFIRE"
            elif feedback == "_yy_y":
                current_guess = "ADORE"
            elif feedback == "ggg__":
                current_guess = "CAPIZ"
            elif feedback == "ggg_y":
                current_guess = "GRADE"
            elif feedback == "gyg__":
                current_guess = "GLARE"
            elif feedback == "ygy__":
                current_guess = "ARGUE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GROOM":
            if feedback == "_gggg":
                current_guess = "VROOM"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GROWL":
            if feedback == "_gg__":
                current_guess = "PROXY"
            elif feedback == "_gg_g":
                current_guess = "BROIL"
            elif feedback == "_gggg":
                current_guess = "PROWL"
            elif feedback == "_gy__":
                current_guess = "PRIMO"
            elif feedback == "_yg__":
                current_guess = "IVORY"
            elif feedback == "_yg_y":
                current_guess = "FLOUR"
            elif feedback == "_ygyg":
                current_guess = "WHORL"
            elif feedback == "ggg__":
                current_guess = "GROUP"
            elif feedback == "gyg_y":
                current_guess = "GLORY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GUAVA":
            if feedback == "__y__":
                current_guess = "BYWAY"
            elif feedback == "_gg__":
                current_guess = "QUAFF"
            elif feedback == "_yy__":
                current_guess = "ABUZZ"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GUILD":
            if feedback == "_____":
                current_guess = "WHOMP"
            elif feedback == "____y":
                current_guess = "HOWDY"
            elif feedback == "___g_":
                current_guess = "LOWLY"
            elif feedback == "___gy":
                current_guess = "DOLLY"
            elif feedback == "___y_":
                current_guess = "POBOY"
            elif feedback == "___yg":
                current_guess = "BLOND"
            elif feedback == "___yy":
                current_guess = "MOLDY"
            elif feedback == "__g__":
                current_guess = "COMFY"
            elif feedback == "__g_y":
                current_guess = "IDIOM"
            elif feedback == "__gg_":
                current_guess = "CHILI"
            elif feedback == "__ggg":
                current_guess = "CHILD"
            elif feedback == "__ggy":
                current_guess = "DOILY"
            elif feedback == "__gy_":
                current_guess = "FLICK"
            elif feedback == "__gyg":
                current_guess = "BLIND"
            elif feedback == "__y__":
                current_guess = "NYMPH"
            elif feedback == "__y_g":
                current_guess = "BIPOD"
            elif feedback == "__y_y":
                current_guess = "DEVON"
            elif feedback == "__yg_":
                current_guess = "ABLOW"
            elif feedback == "__ygy":
                current_guess = "DILLY"
            elif feedback == "__yy_":
                current_guess = "COMFY"
            elif feedback == "__yyg":
                current_guess = "LIPID"
            elif feedback == "_g___":
                current_guess = "BUMPH"
            elif feedback == "_g__y":
                current_guess = "DUMMY"
            elif feedback == "_g_g_":
                current_guess = "BULLY"
            elif feedback == "_g_gy":
                current_guess = "DULLY"
            elif feedback == "_g_y_":
                current_guess = "BULKY"
            elif feedback == "_gg__":
                current_guess = "JUICY"
            elif feedback == "_ggg_":
                current_guess = "QUILL"
            elif feedback == "_gggg":
                current_guess = "BUILD"
            elif feedback == "_gy__":
                current_guess = "CUBIC"
            elif feedback == "_gy_g":
                current_guess = "CUPID"
            elif feedback == "_gyy_":
                current_guess = "PUPIL"
            elif feedback == "_gyyg":
                current_guess = "LUCID"
            elif feedback == "_y___":
                current_guess = "COPEN"
            elif feedback == "_y__g":
                current_guess = "BUMPH"
            elif feedback == "_y_gg":
                current_guess = "ACMES"
            elif feedback == "_y_y_":
                current_guess = "PLUCK"
            elif feedback == "_y_yg":
                current_guess = "CLOUD"
            elif feedback == "_yg__":
                current_guess = "OPIUM"
            elif feedback == "_yy__":
                current_guess = "UNHIP"
            elif feedback == "_yy_g":
                current_guess = "UNDID"
            elif feedback == "_yyyg":
                current_guess = "FLUID"
            elif feedback == "g____":
                current_guess = "GOOFY"
            elif feedback == "g___y":
                current_guess = "GOODY"
            elif feedback == "g__g_":
                current_guess = "GOLLY"
            elif feedback == "g__gy":
                current_guess = "GODLY"
            elif feedback == "g__y_":
                current_guess = "GLOOM"
            elif feedback == "g_g__":
                current_guess = "GOING"
            elif feedback == "g_y__":
                current_guess = "GIZMO"
            elif feedback == "g_y_y":
                current_guess = "GIDDY"
            elif feedback == "gg___":
                current_guess = "AMBAN"
            elif feedback == "gg_g_":
                current_guess = "GULLY"
            elif feedback == "gg_y_":
                current_guess = "GULCH"
            elif feedback == "gy_y_":
                current_guess = "GHOUL"
            elif feedback == "y____":
                current_guess = "BOGGY"
            elif feedback == "y___y":
                current_guess = "DODGY"
            elif feedback == "y__y_":
                current_guess = "LOGON"
            elif feedback == "y_g__":
                current_guess = "BICCY"
            elif feedback == "y_g_y":
                current_guess = "DOING"
            elif feedback == "y_gy_":
                current_guess = "BACCY"
            elif feedback == "y_y__":
                current_guess = "BINGO"
            elif feedback == "y_y_y":
                current_guess = "DINGO"
            elif feedback == "y_yy_":
                current_guess = "LINGO"
            elif feedback == "yg___":
                current_guess = "ABHOR"
            elif feedback == "yg__y":
                current_guess = "AFLAJ"
            elif feedback == "yg_y_":
                current_guess = "BULGY"
            elif feedback == "ygg__":
                current_guess = "CUING"
            elif feedback == "ygy__":
                current_guess = "FUNGI"
            elif feedback == "yy___":
                current_guess = "BOUGH"
            elif feedback == "yy__y":
                current_guess = "DOUGH"
            elif feedback == "yy_y_":
                current_guess = "CLUNG"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GULCH":
            if feedback == "_____":
                current_guess = "ADMIN"
            elif feedback == "___g_":
                current_guess = "DANCE"
            elif feedback == "___y_":
                current_guess = "CANOE"
            elif feedback == "___yy":
                current_guess = "CACHE"
            elif feedback == "__g__":
                current_guess = "VALVE"
            elif feedback == "__g_y":
                current_guess = "HALVE"
            elif feedback == "__gy_":
                current_guess = "CALVE"
            elif feedback == "__y__":
                current_guess = "ABYSM"
            elif feedback == "__yg_":
                current_guess = "LANCE"
            elif feedback == "__yy_":
                current_guess = "CABLE"
            elif feedback == "_y___":
                current_guess = "MAUVE"
            elif feedback == "_yg__":
                current_guess = "VALUE"
            elif feedback == "g____":
                current_guess = "GAFFE"
            elif feedback == "g_y__":
                current_guess = "GABLE"
            elif feedback == "gy___":
                current_guess = "GAUGE"
            elif feedback == "y____":
                current_guess = "BADGE"
            elif feedback == "y__y_":
                current_guess = "CADGE"
            elif feedback == "y_y__":
                current_guess = "EAGLE"
            elif feedback == "yy___":
                current_guess = "VAGUE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GUNKY":
            if feedback == "_____":
                current_guess = "BOXER"
            elif feedback == "____y":
                current_guess = "FOYER"
            elif feedback == "___y_":
                current_guess = "JOKER"
            elif feedback == "__g__":
                current_guess = "BONER"
            elif feedback == "g____":
                current_guess = "GOFER"
            elif feedback == "g_g__":
                current_guess = "GONER"
            elif feedback == "y____":
                current_guess = "ROGER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "GUSTY":
            if feedback == "_gggg":
                current_guess = "MUSTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HAIKU":
            if feedback == "gg___":
                current_guess = "HALAL"
            elif feedback == "yg__y":
                current_guess = "LAUGH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HAMMY":
            if feedback == "gg__g":
                current_guess = "HAPPY"
            elif feedback == "yg__y":
                current_guess = "YAHOO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HARSH":
            if feedback == "_gggg":
                current_guess = "MARSH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HAVOC":
            if feedback == "yg_yy":
                current_guess = "MACHO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HIDER":
            if feedback == "_gggg":
                current_guess = "RIDER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HIJAB":
            if feedback == "_g_y_":
                current_guess = "PIZZA"
            elif feedback == "_y_y_":
                current_guess = "UMAMI"
            elif feedback == "yy_y_":
                current_guess = "KHAKI"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HIMBO":
            if feedback == "_____":
                current_guess = "GUTSY"
            elif feedback == "____g":
                current_guess = "NUTSO"
            elif feedback == "____y":
                current_guess = "JOUST"
            elif feedback == "___yy":
                current_guess = "BOOST"
            elif feedback == "_g___":
                current_guess = "DITSY"
            elif feedback == "_g_y_":
                current_guess = "BITSY"
            elif feedback == "_gy__":
                current_guess = "MIDST"
            elif feedback == "_y__y":
                current_guess = "FOIST"
            elif feedback == "_yy_y":
                current_guess = "MOIST"
            elif feedback == "gy__y":
                current_guess = "HOIST"
            elif feedback == "y___y":
                current_guess = "GHOST"
            elif feedback == "yy___":
                current_guess = "WHIST"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HITCH":
            if feedback == "_gggg":
                current_guess = "PITCH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HOARY":
            if feedback == "_ygg_":
                current_guess = "AMARO"
            elif feedback == "_yggg":
                current_guess = "OVARY"
            elif feedback == "_yyy_":
                current_guess = "ARMOR"
            elif feedback == "yggy_":
                current_guess = "ROACH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HOKUM":
            if feedback == "_____":
                current_guess = "TRILL"
            elif feedback == "___y_":
                current_guess = "TRULY"
            elif feedback == "___yy":
                current_guess = "TRUMP"
            elif feedback == "__y__":
                current_guess = "TRICK"
            elif feedback == "__yy_":
                current_guess = "TRUCK"
            elif feedback == "_y___":
                current_guess = "TROLL"
            elif feedback == "_y__y":
                current_guess = "TROMP"
            elif feedback == "_y_g_":
                current_guess = "TROUT"
            elif feedback == "_y_y_":
                current_guess = "TUTOR"
            elif feedback == "_y_yy":
                current_guess = "TUMOR"
            elif feedback == "y____":
                current_guess = "THIRD"
            elif feedback == "y__y_":
                current_guess = "TRUTH"
            elif feedback == "yy___":
                current_guess = "THORN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HONED":
            if feedback == "___g_":
                current_guess = "TWEET"
            elif feedback == "___gg":
                current_guess = "TWEED"
            elif feedback == "___y_":
                current_guess = "TEMPT"
            elif feedback == "___yg":
                current_guess = "TEPID"
            elif feedback == "___yy":
                current_guess = "TEDDY"
            elif feedback == "__gg_":
                current_guess = "TENET"
            elif feedback == "__yg_":
                current_guess = "TWEEN"
            elif feedback == "__yy_":
                current_guess = "TEENY"
            elif feedback == "_g_g_":
                current_guess = "TOTEM"
            elif feedback == "_ggg_":
                current_guess = "TONEY"
            elif feedback == "_gyg_":
                current_guess = "TOKEN"
            elif feedback == "_y_y_":
                current_guess = "TEMPO"
            elif feedback == "y__g_":
                current_guess = "THIEF"
            elif feedback == "y__y_":
                current_guess = "TEETH"
            elif feedback == "y_gy_":
                current_guess = "TENTH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HONKY":
            if feedback == "_____":
                current_guess = "SPURT"
            elif feedback == "____g":
                current_guess = "RUSTY"
            elif feedback == "___y_":
                current_guess = "SKIRT"
            elif feedback == "_y___":
                current_guess = "SPORT"
            elif feedback == "_y__g":
                current_guess = "STORY"
            elif feedback == "_y_y_":
                current_guess = "STORK"
            elif feedback == "_yy__":
                current_guess = "SNORT"
            elif feedback == "y____":
                current_guess = "SHIRT"
            elif feedback == "yy___":
                current_guess = "SHORT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HOOCH":
            if feedback == "ggg__":
                current_guess = "HOOKY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HOTEL":
            if feedback == "__ggg":
                current_guess = "BETEL"
            elif feedback == "__ygy":
                current_guess = "FLEET"
            elif feedback == "_gggg":
                current_guess = "MOTEL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HOUSE":
            if feedback == "_gggg":
                current_guess = "MOUSE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HOWDY":
            if feedback == "_g_g_":
                current_guess = "CONDO"
            elif feedback == "_g_gg":
                current_guess = "MOODY"
            elif feedback == "_g_yg":
                current_guess = "DOOZY"
            elif feedback == "_gggg":
                current_guess = "DOWDY"
            elif feedback == "_ggyg":
                current_guess = "DOWNY"
            elif feedback == "_gygg":
                current_guess = "WOODY"
            elif feedback == "gg_gg":
                current_guess = "HOODY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HUFFY":
            if feedback == "gg__g":
                current_guess = "HUNKY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "HUMUS":
            if feedback == "ygy_y":
                current_guess = "MUSHY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "IMPEL":
            if feedback == "y_ygg":
                current_guess = "PIXEL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "INCEL":
            if feedback == "_g_gg":
                current_guess = "KNEEL"
            elif feedback == "_y_gg":
                current_guess = "NOVEL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "INFER":
            if feedback == "yy_yy":
                current_guess = "REIGN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "INPUT":
            if feedback == "_g_gg":
                current_guess = "UNCUT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ISLET":
            if feedback == "_yyyg":
                current_guess = "SMELT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ISSUE":
            if feedback == "yy__g":
                current_guess = "SIEVE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "JAUNT":
            if feedback == "_gggg":
                current_guess = "VAUNT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "JAZZY":
            if feedback == "_g__g":
                current_guess = "YAPPY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "JETTY":
            if feedback == "_g_g_":
                current_guess = "BENTO"
            elif feedback == "_g_gg":
                current_guess = "HEFTY"
            elif feedback == "_gg__":
                current_guess = "FETCH"
            elif feedback == "_gy__":
                current_guess = "BEGOT"
            elif feedback == "_yy__":
                current_guess = "EVENT"
            elif feedback == "yyy__":
                current_guess = "EJECT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "JOINT":
            if feedback == "_gggg":
                current_guess = "POINT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "JUICY":
            if feedback == "_ggg_":
                current_guess = "QUICK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "KACHA":
            if feedback == "_y___":
                current_guess = "WEAVE"
            elif feedback == "_y__y":
                current_guess = "AMAZE"
            elif feedback == "_y_y_":
                current_guess = "HEAVE"
            elif feedback == "_yy__":
                current_guess = "PEACE"
            elif feedback == "_yy_y":
                current_guess = "APACE"
            elif feedback == "_yyy_":
                current_guess = "CHAFE"
            elif feedback == "yy___":
                current_guess = "QUAKE"
            elif feedback == "yy__y":
                current_guess = "AWAKE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "KEMPS":
            if feedback == "_y___":
                current_guess = "TATER"
            elif feedback == "_y_y_":
                current_guess = "TAPER"
            elif feedback == "_yg__":
                current_guess = "TAMER"
            elif feedback == "yy___":
                current_guess = "TAKER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "KLETT":
            if feedback == "__yg_":
                current_guess = "SPATE"
            elif feedback == "__ygy":
                current_guess = "STATE"
            elif feedback == "__yy_":
                current_guess = "STAGE"
            elif feedback == "_gyg_":
                current_guess = "SLATE"
            elif feedback == "_yyy_":
                current_guess = "STALE"
            elif feedback == "y_yg_":
                current_guess = "SKATE"
            elif feedback == "y_yy_":
                current_guess = "STAKE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "KNACK":
            if feedback == "_gyy_":
                current_guess = "UNCAP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "KVELL":
            if feedback == "__ggg":
                current_guess = "QUELL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LABEL":
            if feedback == "gg_g_":
                current_guess = "LADEN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LAYUP":
            if feedback == "_gg__":
                current_guess = "KAYAK"
            elif feedback == "_ggy_":
                current_guess = "BAYOU"
            elif feedback == "ygg__":
                current_guess = "GAYLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LEAFY":
            if feedback == "ggg__":
                current_guess = "LEACH"
            elif feedback == "ggg_g":
                current_guess = "LEAKY"
            elif feedback == "ygyy_":
                current_guess = "FELLA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LEARN":
            if feedback == "_ggg_":
                current_guess = "WEARY"
            elif feedback == "_gggg":
                current_guess = "YEARN"
            elif feedback == "_ggy_":
                current_guess = "REACH"
            elif feedback == "yggg_":
                current_guess = "PEARL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LEAVE":
            if feedback == "y_g_g":
                current_guess = "WHALE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LEMED":
            if feedback == "___g_":
                current_guess = "FACET"
            elif feedback == "___gg":
                current_guess = "GATED"
            elif feedback == "___gy":
                current_guess = "CADET"
            elif feedback == "__yg_":
                current_guess = "MATEY"
            elif feedback == "_y_g_":
                current_guess = "EATEN"
            elif feedback == "g__g_":
                current_guess = "LATEX"
            elif feedback == "y__g_":
                current_guess = "VALET"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LIKEN":
            if feedback == "g__gg":
                current_guess = "LUMEN"
            elif feedback == "gg_gg":
                current_guess = "LIVEN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LINGO":
            if feedback == "gy_yy":
                current_guess = "LOGIC"
            elif feedback == "gyyyy":
                current_guess = "LOGIN"
            elif feedback == "yg_y_":
                current_guess = "VIGIL"
            elif feedback == "yy_yg":
                current_guess = "IGLOO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LINKY":
            if feedback == "_____":
                current_guess = "TABOO"
            elif feedback == "____g":
                current_guess = "ABAFT"
            elif feedback == "___gg":
                current_guess = "TACKY"
            elif feedback == "__g__":
                current_guess = "TANGO"
            elif feedback == "__g_g":
                current_guess = "TANGY"
            elif feedback == "__y__":
                current_guess = "TAUNT"
            elif feedback == "__y_g":
                current_guess = "TAWNY"
            elif feedback == "_y___":
                current_guess = "TACIT"
            elif feedback == "_yy__":
                current_guess = "TAINT"
            elif feedback == "y___g":
                current_guess = "TALLY"
            elif feedback == "y__gg":
                current_guess = "TALKY"
            elif feedback == "y_y__":
                current_guess = "TALON"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LIPID":
            if feedback == "gg_gg":
                current_guess = "LIVID"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LOAMY":
            if feedback == "ggy_y":
                current_guess = "LOYAL"
            elif feedback == "ygg__":
                current_guess = "KOALA"
            elif feedback == "ygy__":
                current_guess = "DOULA"
            elif feedback == "ygyy_":
                current_guess = "MODAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LOATH":
            if feedback == "yyyy_":
                current_guess = "OCTAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LOGIN":
            if feedback == "_____":
                current_guess = "EMCEE"
            elif feedback == "____y":
                current_guess = "CHEEP"
            elif feedback == "___g_":
                current_guess = "PIXIE"
            elif feedback == "___gy":
                current_guess = "INDIE"
            elif feedback == "___y_":
                current_guess = "DUMPS"
            elif feedback == "___yy":
                current_guess = "WINCE"
            elif feedback == "__g__":
                current_guess = "FUGUE"
            elif feedback == "__y__":
                current_guess = "BUMPH"
            elif feedback == "__y_y":
                current_guess = "NUDGE"
            elif feedback == "__ygy":
                current_guess = "GENIE"
            elif feedback == "__yy_":
                current_guess = "BEIGE"
            elif feedback == "__yyy":
                current_guess = "BINGE"
            elif feedback == "_g___":
                current_guess = "BOCCE"
            elif feedback == "_g_g_":
                current_guess = "MOVIE"
            elif feedback == "_g_y_":
                current_guess = "VOICE"
            elif feedback == "_gg__":
                current_guess = "VOGUE"
            elif feedback == "_ggg_":
                current_guess = "BOGIE"
            elif feedback == "_gy__":
                current_guess = "DODGE"
            elif feedback == "_y___":
                current_guess = "CHOKE"
            elif feedback == "_y__y":
                current_guess = "OUNCE"
            elif feedback == "_y_y_":
                current_guess = "BIOME"
            elif feedback == "_y_yy":
                current_guess = "OPINE"
            elif feedback == "_yy__":
                current_guess = "GEODE"
            elif feedback == "_yy_y":
                current_guess = "GNOME"
            elif feedback == "g____":
                current_guess = "LEVEE"
            elif feedback == "g_y__":
                current_guess = "LEDGE"
            elif feedback == "g_y_y":
                current_guess = "LUNGE"
            elif feedback == "g_yy_":
                current_guess = "LIEGE"
            elif feedback == "gg___":
                current_guess = "LOUPE"
            elif feedback == "ggy__":
                current_guess = "LODGE"
            elif feedback == "y____":
                current_guess = "DUMPY"
            elif feedback == "y___y":
                current_guess = "UNCLE"
            elif feedback == "y__g_":
                current_guess = "BELIE"
            elif feedback == "y__y_":
                current_guess = "CHILE"
            elif feedback == "y_g__":
                current_guess = "BUGLE"
            elif feedback == "y_y__":
                current_guess = "BULGE"
            elif feedback == "y_yy_":
                current_guess = "GLIDE"
            elif feedback == "yg___":
                current_guess = "BOULE"
            elif feedback == "yg__y":
                current_guess = "NOBLE"
            elif feedback == "yg_y_":
                current_guess = "VOILE"
            elif feedback == "yy___":
                current_guess = "BECAP"
            elif feedback == "yy__y":
                current_guess = "CLONE"
            elif feedback == "yy_g_":
                current_guess = "OLDIE"
            elif feedback == "yy_y_":
                current_guess = "OLIVE"
            elif feedback == "yyy__":
                current_guess = "GLOBE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LORDY":
            if feedback == "ggg_g":
                current_guess = "LORRY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LOWLY":
            if feedback == "_g_gg":
                current_guess = "COYLY"
            elif feedback == "_gggg":
                current_guess = "JOWLY"
            elif feedback == "_gygg":
                current_guess = "WOOLY"
            elif feedback == "gg_gg":
                current_guess = "LOLLY"
            elif feedback == "yg_gg":
                current_guess = "FEHME"
            elif feedback == "yy_g_":
                current_guess = "KNOLL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LUPIN":
            if feedback == "_____":
                current_guess = "MASSE"
            elif feedback == "____y":
                current_guess = "MANSE"
            elif feedback == "__y__":
                current_guess = "PASSE"
            elif feedback == "_y___":
                current_guess = "CAUSE"
            elif feedback == "_yy__":
                current_guess = "PAUSE"
            elif feedback == "g_g__":
                current_guess = "LAPSE"
            elif feedback == "y____":
                current_guess = "FALSE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "LYMPH":
            if feedback == "_____":
                current_guess = "OAKEN"
            elif feedback == "____y":
                current_guess = "HAVEN"
            elif feedback == "___y_":
                current_guess = "PAEAN"
            elif feedback == "__g__":
                current_guess = "CAMEO"
            elif feedback == "__y__":
                current_guess = "MAVEN"
            elif feedback == "_y___":
                current_guess = "CAGEY"
            elif feedback == "_yg__":
                current_guess = "GAMEY"
            elif feedback == "g____":
                current_guess = "LABEL"
            elif feedback == "g__y_":
                current_guess = "LAPEL"
            elif feedback == "gy___":
                current_guess = "LACEY"
            elif feedback == "y____":
                current_guess = "BAGEL"
            elif feedback == "y___y":
                current_guess = "HAZEL"
            elif feedback == "y__y_":
                current_guess = "PANEL"
            elif feedback == "y_g__":
                current_guess = "CAMEL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MAGIC":
            if feedback == "_g__y":
                current_guess = "WACKO"
            elif feedback == "gg__y":
                current_guess = "MACAW"
            elif feedback == "gg_gg":
                current_guess = "MALIC"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MAKER":
            if feedback == "yg_gy":
                current_guess = "RAMEN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MAMBA":
            if feedback == "_g___":
                current_guess = "KAZOO"
            elif feedback == "_g__g":
                current_guess = "KAPPA"
            elif feedback == "_g__y":
                current_guess = "PAPAL"
            elif feedback == "_g_y_":
                current_guess = "KABOB"
            elif feedback == "_g_yg":
                current_guess = "BABKA"
            elif feedback == "gg__g":
                current_guess = "MAFIA"
            elif feedback == "ggg_g":
                current_guess = "MAMMA"
            elif feedback == "gggg_":
                current_guess = "MAMBO"
            elif feedback == "ggy__":
                current_guess = "MAXIM"
            elif feedback == "ggy_g":
                current_guess = "MAGMA"
            elif feedback == "ygg_g":
                current_guess = "GAMMA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MANIC":
            if feedback == "_gggg":
                current_guess = "PANIC"
            elif feedback == "_gy_y":
                current_guess = "BACON"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MANLY":
            if feedback == "_gg_g":
                current_guess = "JANKY"
            elif feedback == "_gggg":
                current_guess = "WANLY"
            elif feedback == "_ggyg":
                current_guess = "LANKY"
            elif feedback == "_gy_g":
                current_guess = "NAGGY"
            elif feedback == "ggg_g":
                current_guess = "MANGY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MEDAL":
            if feedback == "_g_g_":
                current_guess = "BEGAN"
            elif feedback == "_g_gg":
                current_guess = "APING"
            elif feedback == "_g_gy":
                current_guess = "BELAY"
            elif feedback == "_g_y_":
                current_guess = "BEACH"
            elif feedback == "_g_yy":
                current_guess = "LEAFY"
            elif feedback == "_gggg":
                current_guess = "PEDAL"
            elif feedback == "_gyg_":
                current_guess = "DECAF"
            elif feedback == "_gygg":
                current_guess = "DECAL"
            elif feedback == "_gygy":
                current_guess = "DELAY"
            elif feedback == "_gyy_":
                current_guess = "BEADY"
            elif feedback == "_y_g_":
                current_guess = "CHEAP"
            elif feedback == "_y_gg":
                current_guess = "EQUAL"
            elif feedback == "_y_gy":
                current_guess = "CLEAN"
            elif feedback == "_y_y_":
                current_guess = "ANNEX"
            elif feedback == "_y_yg":
                current_guess = "ANGEL"
            elif feedback == "_y_yy":
                current_guess = "ALIEN"
            elif feedback == "_yyg_":
                current_guess = "AHEAD"
            elif feedback == "_yygg":
                current_guess = "IDEAL"
            elif feedback == "_yygy":
                current_guess = "PLEAD"
            elif feedback == "_yyy_":
                current_guess = "ADIEU"
            elif feedback == "gg_y_":
                current_guess = "MECCA"
            elif feedback == "gg_yy":
                current_guess = "MEALY"
            elif feedback == "gggy_":
                current_guess = "MEDIA"
            elif feedback == "yg_yy":
                current_guess = "LEMMA"
            elif feedback == "yy_gy":
                current_guess = "GLEAM"
            elif feedback == "yy_y_":
                current_guess = "ENEMA"
            elif feedback == "yy_yg":
                current_guess = "EMAIL"
            elif feedback == "yyyy_":
                current_guess = "AMEND"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MERGE":
            if feedback == "_gggg":
                current_guess = "VERGE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MESHY":
            if feedback == "_gg_g":
                current_guess = "PESKY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "METRO":
            if feedback == "_gggg":
                current_guess = "RETRO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MICRO":
            if feedback == "__gyy":
                current_guess = "OCCUR"
            elif feedback == "__yyy":
                current_guess = "FROCK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MILKO":
            if feedback == "____y":
                current_guess = "STONE"
            elif feedback == "___gy":
                current_guess = "STOKE"
            elif feedback == "__y__":
                current_guess = "STELE"
            elif feedback == "__y_y":
                current_guess = "STOLE"
            elif feedback == "_g___":
                current_guess = "PISTE"
            elif feedback == "_y___":
                current_guess = "SPITE"
            elif feedback == "_yy__":
                current_guess = "STILE"
            elif feedback == "y___y":
                current_guess = "SMOTE"
            elif feedback == "yy___":
                current_guess = "SMITE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MINOR":
            if feedback == "____g":
                current_guess = "TRUER"
            elif feedback == "____y":
                current_guess = "TWERK"
            elif feedback == "___yg":
                current_guess = "TOWER"
            elif feedback == "__g_g":
                current_guess = "TUNER"
            elif feedback == "__ggg":
                current_guess = "TENOR"
            elif feedback == "__gyg":
                current_guess = "TONER"
            elif feedback == "__y_y":
                current_guess = "TREND"
            elif feedback == "_g__g":
                current_guess = "TIGER"
            elif feedback == "_y__g":
                current_guess = "THEIR"
            elif feedback == "_y__y":
                current_guess = "TRIED"
            elif feedback == "yg__g":
                current_guess = "TIMER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MINTY":
            if feedback == "_ggg_":
                current_guess = "NINTH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MINUS":
            if feedback == "__ggg":
                current_guess = "BONUS"
            elif feedback == "_gggg":
                current_guess = "SINUS"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MISER":
            if feedback == "__ggg":
                current_guess = "LOSER"
            elif feedback == "__ygg":
                current_guess = "SOBER"
            elif feedback == "_gggg":
                current_guess = "RISER"
            elif feedback == "_gggy":
                current_guess = "RISEN"
            elif feedback == "_yygg":
                current_guess = "SKIER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MOCHA":
            if feedback == "_gyyy":
                current_guess = "POACH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MOLAR":
            if feedback == "_gggg":
                current_guess = "POLAR"
            elif feedback == "_gygy":
                current_guess = "ROYAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MOPED":
            if feedback == "___gg":
                current_guess = "IVIED"
            elif feedback == "__ggg":
                current_guess = "BIPED"
            elif feedback == "_g_gy":
                current_guess = "CODEX"
            elif feedback == "_y_gy":
                current_guess = "VIDEO"
            elif feedback == "gg_gy":
                current_guess = "MODEM"
            elif feedback == "y__gg":
                current_guess = "EMBED"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MOTOR":
            if feedback == "_gggg":
                current_guess = "ROTOR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MOURN":
            if feedback == "_g_yg":
                current_guess = "ROBIN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MOVIE":
            if feedback == "gg_gg":
                current_guess = "MOXIE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MULCH":
            if feedback == "_____":
                current_guess = "ABYSS"
            elif feedback == "____g":
                current_guess = "AWASH"
            elif feedback == "__y__":
                current_guess = "FLASK"
            elif feedback == "__y_g":
                current_guess = "FLASH"
            elif feedback == "__yy_":
                current_guess = "CLASP"
            elif feedback == "__yyg":
                current_guess = "CLASH"
            elif feedback == "_g___":
                current_guess = "QUASI"
            elif feedback == "_g__g":
                current_guess = "QUASH"
            elif feedback == "y____":
                current_guess = "AMASS"
            elif feedback == "y___g":
                current_guess = "SMASH"
            elif feedback == "y__yy":
                current_guess = "CHASM"
            elif feedback == "y_y__":
                current_guess = "PLASM"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MUMMY":
            if feedback == "_gggg":
                current_guess = "YUMMY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "MURAL":
            if feedback == "_gggg":
                current_guess = "RURAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "NAGGY":
            if feedback == "gg__g":
                current_guess = "NAPPY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "NERDY":
            if feedback == "ggg_g":
                current_guess = "NERVY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "NEWEL":
            if feedback == "___g_":
                current_guess = "SHIED"
            elif feedback == "___gg":
                current_guess = "SPIEL"
            elif feedback == "_g___":
                current_guess = "MESHY"
            elif feedback == "_g__y":
                current_guess = "LEXIS"
            elif feedback == "_g_g_":
                current_guess = "FECES"
            elif feedback == "_g_y_":
                current_guess = "SEEDY"
            elif feedback == "_y___":
                current_guess = "SHEIK"
            elif feedback == "_y__g":
                current_guess = "APHID"
            elif feedback == "_y__y":
                current_guess = "SHELF"
            elif feedback == "_y_g_":
                current_guess = "SHEEP"
            elif feedback == "_y_gy":
                current_guess = "SLEEK"
            elif feedback == "_yy_g":
                current_guess = "SWELL"
            elif feedback == "_yyg_":
                current_guess = "SWEEP"
            elif feedback == "g__g_":
                current_guess = "NOSEY"
            elif feedback == "gg___":
                current_guess = "NEXUS"
            elif feedback == "y_yg_":
                current_guess = "SINEW"
            elif feedback == "yg___":
                current_guess = "GENUS"
            elif feedback == "yg_g_":
                current_guess = "SEVEN"
            elif feedback == "yy___":
                current_guess = "SKEIN"
            elif feedback == "yy_g_":
                current_guess = "SHEEN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "NODAL":
            if feedback == "yg_gg":
                current_guess = "ZONAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "NOISE":
            if feedback == "_g_gg":
                current_guess = "POSSE"
            elif feedback == "_gggg":
                current_guess = "POISE"
            elif feedback == "_y_gg":
                current_guess = "OBESE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "NORTH":
            if feedback == "_gggg":
                current_guess = "WORTH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "NURSE":
            if feedback == "_gggg":
                current_guess = "PURSE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "NUTTY":
            if feedback == "yy_gg":
                current_guess = "UNITY"
            elif feedback == "yyg__":
                current_guess = "UNTIL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "NYMPH":
            if feedback == "_____":
                current_guess = "CIVIC"
            elif feedback == "___gy":
                current_guess = "HIPPO"
            elif feedback == "__g__":
                current_guess = "COMIC"
            elif feedback == "__y_y":
                current_guess = "MOCHI"
            elif feedback == "_y___":
                current_guess = "FIZZY"
            elif feedback == "_y_g_":
                current_guess = "ZIPPY"
            elif feedback == "_y_gy":
                current_guess = "HIPPY"
            elif feedback == "_y_y_":
                current_guess = "PICKY"
            elif feedback == "_yg__":
                current_guess = "JIMMY"
            elif feedback == "_ygg_":
                current_guess = "WIMPY"
            elif feedback == "gy___":
                current_guess = "NINNY"
            elif feedback == "gy_g_":
                current_guess = "NIPPY"
            elif feedback == "y____":
                current_guess = "CONIC"
            elif feedback == "y___g":
                current_guess = "AFLOW"
            elif feedback == "y__yg":
                current_guess = "PINCH"
            elif feedback == "y_y__":
                current_guess = "MINIM"
            elif feedback == "yg___":
                current_guess = "CYNIC"
            elif feedback == "yy___":
                current_guess = "KINKY"
            elif feedback == "yy__y":
                current_guess = "HINKY"
            elif feedback == "yy_y_":
                current_guess = "PINKY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "OAKEN":
            if feedback == "_g_g_":
                current_guess = "JADED"
            elif feedback == "_g_gg":
                current_guess = "WAXEN"
            elif feedback == "_ggg_":
                current_guess = "BAKED"
            elif feedback == "_gggg":
                current_guess = "WAKEN"
            elif feedback == "_gggy":
                current_guess = "NAKED"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "OCHER":
            if feedback == "yy_yy":
                current_guess = "RECON"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ODDER":
            if feedback == "g_ggg":
                current_guess = "ORDER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "OFFER":
            if feedback == "g__gg":
                current_guess = "OWNER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "OPINE":
            if feedback == "g_ggg":
                current_guess = "OVINE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "OPIUM":
            if feedback == "__gy_":
                current_guess = "UNIFY"
            elif feedback == "y_gy_":
                current_guess = "UNION"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "OTHER":
            if feedback == "gg_gg":
                current_guess = "OTTER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "OUNCE":
            if feedback == "g_y_g":
                current_guess = "OZONE"
            elif feedback == "y_y_g":
                current_guess = "PHONE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "OUTGO":
            if feedback == "ygy__":
                current_guess = "QUOTH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PANTY":
            if feedback == "gg_gg":
                current_guess = "PATTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PARER":
            if feedback == "_gggg":
                current_guess = "RARER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PARRY":
            if feedback == "_gg_g":
                current_guess = "HARDY"
            elif feedback == "_gggg":
                current_guess = "HARRY"
            elif feedback == "ygg_g":
                current_guess = "HARPY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PASTE":
            if feedback == "_gggg":
                current_guess = "WASTE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PATSY":
            if feedback == "_gyg_":
                current_guess = "WAIST"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PERIL":
            if feedback == "gyg__":
                current_guess = "PURER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PHISH":
            if feedback == "_ggg_":
                current_guess = "WHISK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PHLOX":
            if feedback == "__gg_":
                current_guess = "BELOW"
            elif feedback == "__gy_":
                current_guess = "CELLO"
            elif feedback == "__y__":
                current_guess = "FLECK"
            elif feedback == "__yg_":
                current_guess = "ELBOW"
            elif feedback == "_gy__":
                current_guess = "WHELK"
            elif feedback == "_yg__":
                current_guess = "BELCH"
            elif feedback == "_yg_g":
                current_guess = "HELIX"
            elif feedback == "_ygy_":
                current_guess = "HELLO"
            elif feedback == "_yy__":
                current_guess = "LEECH"
            elif feedback == "ygy__":
                current_guess = "WHELP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PILAF":
            if feedback == "_ggy_":
                current_guess = "VILLA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PILED":
            if feedback == "___g_":
                current_guess = "COMET"
            elif feedback == "___gy":
                current_guess = "DUVET"
            elif feedback == "___y_":
                current_guess = "JETTY"
            elif feedback == "___yy":
                current_guess = "DEBUT"
            elif feedback == "__gy_":
                current_guess = "MELTY"
            elif feedback == "__gyy":
                current_guess = "VELDT"
            elif feedback == "__yg_":
                current_guess = "HOTEL"
            elif feedback == "__yy_":
                current_guess = "EXULT"
            elif feedback == "__yyy":
                current_guess = "DWELT"
            elif feedback == "_g_g_":
                current_guess = "CIVET"
            elif feedback == "_g_gy":
                current_guess = "BIDET"
            elif feedback == "_g_y_":
                current_guess = "EIGHT"
            elif feedback == "_ggg_":
                current_guess = "FILET"
            elif feedback == "_y_g_":
                current_guess = "QUIET"
            elif feedback == "_y_y_":
                current_guess = "BEFIT"
            elif feedback == "_y_yg":
                current_guess = "FETID"
            elif feedback == "_y_yy":
                current_guess = "DEBIT"
            elif feedback == "_ygg_":
                current_guess = "INLET"
            elif feedback == "_yyg_":
                current_guess = "INTEL"
            elif feedback == "_yyy_":
                current_guess = "LEGIT"
            elif feedback == "g__y_":
                current_guess = "PETTY"
            elif feedback == "gg_g_":
                current_guess = "PIPET"
            elif feedback == "gg_y_":
                current_guess = "PIETY"
            elif feedback == "gy_y_":
                current_guess = "PETIT"
            elif feedback == "y__y_":
                current_guess = "EMPTY"
            elif feedback == "y__yy":
                current_guess = "DEPOT"
            elif feedback == "y_yy_":
                current_guess = "LETUP"
            elif feedback == "yy_y_":
                current_guess = "INEPT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PILOT":
            if feedback == "_g_gg":
                current_guess = "BIGOT"
            elif feedback == "gg_gg":
                current_guess = "PIVOT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PINCH":
            if feedback == "_____":
                current_guess = "SWORE"
            elif feedback == "____y":
                current_guess = "SHORE"
            elif feedback == "___y_":
                current_guess = "SCORE"
            elif feedback == "__y__":
                current_guess = "SNORE"
            elif feedback == "_y__y":
                current_guess = "SHIRE"
            elif feedback == "y____":
                current_guess = "SPORE"
            elif feedback == "yy___":
                current_guess = "SPIRE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PINKY":
            if feedback == "_g___":
                current_guess = "REFIX"
            elif feedback == "_g__g":
                current_guess = "FIERY"
            elif feedback == "_g_y_":
                current_guess = "BIKER"
            elif feedback == "_gg__":
                current_guess = "FINER"
            elif feedback == "_gy__":
                current_guess = "RIVEN"
            elif feedback == "_y___":
                current_guess = "BRIEF"
            elif feedback == "_y__g":
                current_guess = "REIFY"
            elif feedback == "_y_y_":
                current_guess = "KEFIR"
            elif feedback == "_yg__":
                current_guess = "INNER"
            elif feedback == "_yy__":
                current_guess = "INFER"
            elif feedback == "gg___":
                current_guess = "PIPER"
            elif feedback == "gg_y_":
                current_guess = "PIKER"
            elif feedback == "yg___":
                current_guess = "ADVEW"
            elif feedback == "ygy__":
                current_guess = "RIPEN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PIOUS":
            if feedback == "g__yy":
                current_guess = "PUSHY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PLANC":
            if feedback == "__g__":
                current_guess = "DEATH"
            elif feedback == "__g_y":
                current_guess = "EXACT"
            elif feedback == "__gg_":
                current_guess = "MEANT"
            elif feedback == "__gy_":
                current_guess = "SNAFU"
            elif feedback == "__gyy":
                current_guess = "ENACT"
            elif feedback == "__y__":
                current_guess = "BEGAT"
            elif feedback == "__y_g":
                current_guess = "SUMAC"
            elif feedback == "__y_y":
                current_guess = "CHEAT"
            elif feedback == "__yg_":
                current_guess = "AGENT"
            elif feedback == "__yy_":
                current_guess = "UNSAY"
            elif feedback == "_gg_y":
                current_guess = "SLACK"
            elif feedback == "_ggg_":
                current_guess = "SLANG"
            elif feedback == "_ggy_":
                current_guess = "SLAIN"
            elif feedback == "_gy__":
                current_guess = "BLEAT"
            elif feedback == "_gy_y":
                current_guess = "CLEAT"
            elif feedback == "_yg__":
                current_guess = "DEALT"
            elif feedback == "_yg_y":
                current_guess = "SCALD"
            elif feedback == "_ygg_":
                current_guess = "LEANT"
            elif feedback == "_ygy_":
                current_guess = "SNAIL"
            elif feedback == "_yy__":
                current_guess = "FETAL"
            elif feedback == "_yy_y":
                current_guess = "ECLAT"
            elif feedback == "g_g__":
                current_guess = "PEATY"
            elif feedback == "ggy__":
                current_guess = "PLEAT"
            elif feedback == "gyg__":
                current_guess = "PSALM"
            elif feedback == "gyy__":
                current_guess = "PETAL"
            elif feedback == "y_g__":
                current_guess = "SOAPY"
            elif feedback == "y_g_y":
                current_guess = "SCAMP"
            elif feedback == "y_gg_":
                current_guess = "SPANK"
            elif feedback == "y_gy_":
                current_guess = "SPAWN"
            elif feedback == "y_y__":
                current_guess = "ADEPT"
            elif feedback == "y_y_g":
                current_guess = "ASPIC"
            elif feedback == "yyg__":
                current_guess = "LEAPT"
            elif feedback == "yyg_y":
                current_guess = "SCALP"
            elif feedback == "yyy__":
                current_guess = "SPLAY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PLING":
            if feedback == "_____":
                current_guess = "SHOVE"
            elif feedback == "____y":
                current_guess = "SEDGE"
            elif feedback == "___g_":
                current_guess = "SCENE"
            elif feedback == "___y_":
                current_guess = "ENSUE"
            elif feedback == "__g__":
                current_guess = "SEIZE"
            elif feedback == "__gg_":
                current_guess = "SHINE"
            elif feedback == "__gy_":
                current_guess = "SNIDE"
            elif feedback == "__y__":
                current_guess = "ISSUE"
            elif feedback == "__y_y":
                current_guess = "SIEGE"
            elif feedback == "__yy_":
                current_guess = "SINCE"
            elif feedback == "__yyy":
                current_guess = "SINGE"
            elif feedback == "_gg__":
                current_guess = "ADEEM"
            elif feedback == "_y___":
                current_guess = "SOLVE"
            elif feedback == "_yg__":
                current_guess = "SMILE"
            elif feedback == "_yy__":
                current_guess = "SIDLE"
            elif feedback == "y____":
                current_guess = "SCOPE"
            elif feedback == "y_g__":
                current_guess = "SPICE"
            elif feedback == "y_gg_":
                current_guess = "SPINE"
            elif feedback == "y_gy_":
                current_guess = "SNIPE"
            elif feedback == "yg___":
                current_guess = "SLOPE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PLOIT":
            if feedback == "____g":
                current_guess = "CHANT"
            elif feedback == "____y":
                current_guess = "AUNTY"
            elif feedback == "___gg":
                current_guess = "ADMIT"
            elif feedback == "___gy":
                current_guess = "ANTIC"
            elif feedback == "___yg":
                current_guess = "GIANT"
            elif feedback == "___yy":
                current_guess = "AGITA"
            elif feedback == "__g_g":
                current_guess = "ABOUT"
            elif feedback == "__g_y":
                current_guess = "QUOTA"
            elif feedback == "__y_g":
                current_guess = "ABBOT"
            elif feedback == "__y_y":
                current_guess = "GOTTA"
            elif feedback == "__yyy":
                current_guess = "COATI"
            elif feedback == "_gg_g":
                current_guess = "ABAFT"
            elif feedback == "_gy_g":
                current_guess = "ALLOT"
            elif feedback == "_y__g":
                current_guess = "ADULT"
            elif feedback == "_y_yy":
                current_guess = "VITAL"
            elif feedback == "_yg_y":
                current_guess = "ATOLL"
            elif feedback == "_yy_y":
                current_guess = "LOATH"
            elif feedback == "gg__g":
                current_guess = "PLANT"
            elif feedback == "gg_gg":
                current_guess = "PLAIT"
            elif feedback == "y___g":
                current_guess = "ADAPT"
            elif feedback == "y__yg":
                current_guess = "INAPT"
            elif feedback == "y_g_g":
                current_guess = "ADOPT"
            elif feedback == "yy__y":
                current_guess = "APTLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PLUCK":
            if feedback == "_gg__":
                current_guess = "BLUFF"
            elif feedback == "_gg_g":
                current_guess = "FLUNK"
            elif feedback == "_gg_y":
                current_guess = "FLUKY"
            elif feedback == "_gggg":
                current_guess = "CLUCK"
            elif feedback == "_ggyg":
                current_guess = "CLUNK"
            elif feedback == "ggg__":
                current_guess = "PLUMB"
            elif feedback == "ggg_g":
                current_guess = "PLUNK"
            elif feedback == "yggy_":
                current_guess = "CLUMP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PLUMB":
            if feedback == "gggg_":
                current_guess = "PLUMP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PLUNK":
            if feedback == "_____":
                current_guess = "DISHY"
            elif feedback == "____g":
                current_guess = "SHOCK"
            elif feedback == "____y":
                current_guess = "SKIFF"
            elif feedback == "___g_":
                current_guess = "SHINY"
            elif feedback == "___y_":
                current_guess = "BISON"
            elif feedback == "__g__":
                current_guess = "SQUIB"
            elif feedback == "__g_g":
                current_guess = "SHUCK"
            elif feedback == "__gg_":
                current_guess = "SOUND"
            elif feedback == "__ggg":
                current_guess = "SKUNK"
            elif feedback == "__gy_":
                current_guess = "SNUFF"
            elif feedback == "__gyg":
                current_guess = "SNUCK"
            elif feedback == "__y__":
                current_guess = "CHIMB"
            elif feedback == "__y_y":
                current_guess = "ADSUM"
            elif feedback == "__yg_":
                current_guess = "SUING"
            elif feedback == "__yy_":
                current_guess = "MINUS"
            elif feedback == "_g___":
                current_guess = "SLIMY"
            elif feedback == "_g__g":
                current_guess = "SLICK"
            elif feedback == "_g_g_":
                current_guess = "SLING"
            elif feedback == "_g_gg":
                current_guess = "SLINK"
            elif feedback == "_ggg_":
                current_guess = "SLUNG"
            elif feedback == "_gggg":
                current_guess = "SLUNK"
            elif feedback == "_y___":
                current_guess = "SHILL"
            elif feedback == "_y__y":
                current_guess = "SILKY"
            elif feedback == "_yg__":
                current_guess = "SCULL"
            elif feedback == "_yg_g":
                current_guess = "SKULK"
            elif feedback == "_yg_y":
                current_guess = "SKULL"
            elif feedback == "_yy__":
                current_guess = "BOLUS"
            elif feedback == "_yy_y":
                current_guess = "SULKY"
            elif feedback == "g____":
                current_guess = "PSYCH"
            elif feedback == "g_y__":
                current_guess = "PIOUS"
            elif feedback == "gy___":
                current_guess = "POLIS"
            elif feedback == "y____":
                current_guess = "SCOOP"
            elif feedback == "y___g":
                current_guess = "SPOOK"
            elif feedback == "y___y":
                current_guess = "SKIMP"
            elif feedback == "y__g_":
                current_guess = "SPINY"
            elif feedback == "y__y_":
                current_guess = "SNOOP"
            elif feedback == "y_g__":
                current_guess = "SOUPY"
            elif feedback == "y_ggg":
                current_guess = "SPUNK"
            elif feedback == "y_yy_":
                current_guess = "SUNUP"
            elif feedback == "yg___":
                current_guess = "SLOOP"
            elif feedback == "ygg__":
                current_guess = "SLUMP"
            elif feedback == "yy___":
                current_guess = "SPILL"
            elif feedback == "yyy__":
                current_guess = "LUPUS"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PLUOT":
            if feedback == "____g":
                current_guess = "CHEEK"
            elif feedback == "____y":
                current_guess = "STEED"
            elif feedback == "___gg":
                current_guess = "BESOT"
            elif feedback == "___gy":
                current_guess = "ETHOS"
            elif feedback == "___yg":
                current_guess = "ONSET"
            elif feedback == "___yy":
                current_guess = "STENO"
            elif feedback == "__y_g":
                current_guess = "UNSET"
            elif feedback == "__y_y":
                current_guess = "FETUS"
            elif feedback == "_g__g":
                current_guess = "SLEET"
            elif feedback == "_y__g":
                current_guess = "ISLET"
            elif feedback == "_y__y":
                current_guess = "STEEL"
            elif feedback == "g__yy":
                current_guess = "PESTO"
            elif feedback == "y___g":
                current_guess = "SPENT"
            elif feedback == "y___y":
                current_guess = "STEEP"
            elif feedback == "y_y_g":
                current_guess = "UPSET"
            elif feedback == "y_y_y":
                current_guess = "SETUP"
            elif feedback == "yg__g":
                current_guess = "SLEPT"
            elif feedback == "yy__g":
                current_guess = "SPELT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "POBOY":
            if feedback == "___gy":
                current_guess = "NYLON"
            elif feedback == "__y_g":
                current_guess = "FLYBY"
            elif feedback == "_g__g":
                current_guess = "FOLKY"
            elif feedback == "_g_g_":
                current_guess = "COLON"
            elif feedback == "_g_yg":
                current_guess = "LOONY"
            elif feedback == "_gg_g":
                current_guess = "LOBBY"
            elif feedback == "_y___":
                current_guess = "CLOCK"
            elif feedback == "_y__g":
                current_guess = "FLOWY"
            elif feedback == "_yy__":
                current_guess = "BLOCK"
            elif feedback == "_yyg_":
                current_guess = "BLOOM"
            elif feedback == "g__gy":
                current_guess = "PYLON"
            elif feedback == "gg__y":
                current_guess = "POLYP"
            elif feedback == "gy___":
                current_guess = "PLONK"
            elif feedback == "y___y":
                current_guess = "LYMPH"
            elif feedback == "yg_yg":
                current_guess = "LOOPY"
            elif feedback == "yy___":
                current_guess = "CLOMP"
            elif feedback == "yyyg_":
                current_guess = "BLOOP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "POIND":
            if feedback == "_____":
                current_guess = "CREME"
            elif feedback == "____y":
                current_guess = "CRUDE"
            elif feedback == "___y_":
                current_guess = "GENRE"
            elif feedback == "__g__":
                current_guess = "CRIME"
            elif feedback == "__g_y":
                current_guess = "BRIDE"
            elif feedback == "__gg_":
                current_guess = "BRINE"
            elif feedback == "__y__":
                current_guess = "RIFLE"
            elif feedback == "__y_y":
                current_guess = "RIDGE"
            elif feedback == "__yy_":
                current_guess = "INURE"
            elif feedback == "_g___":
                current_guess = "ROGUE"
            elif feedback == "_y___":
                current_guess = "BHANG"
            elif feedback == "_y__y":
                current_guess = "DROVE"
            elif feedback == "_y_g_":
                current_guess = "CRONE"
            elif feedback == "_y_gy":
                current_guess = "DRONE"
            elif feedback == "g___y":
                current_guess = "PRUDE"
            elif feedback == "g__g_":
                current_guess = "PRUNE"
            elif feedback == "g_g__":
                current_guess = "ACMES"
            elif feedback == "g_g_y":
                current_guess = "PRIDE"
            elif feedback == "gy___":
                current_guess = "ABLET"
            elif feedback == "gy_g_":
                current_guess = "PRONE"
            elif feedback == "y____":
                current_guess = "CREPE"
            elif feedback == "y_g__":
                current_guess = "GRIPE"
            elif feedback == "yy___":
                current_guess = "GROPE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "POKER":
            if feedback == "yg_gg":
                current_guess = "ROPER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PONCY":
            if feedback == "_____":
                current_guess = "HIRER"
            elif feedback == "____g":
                current_guess = "AMBRY"
            elif feedback == "____y":
                current_guess = "BERYL"
            elif feedback == "___g_":
                current_guess = "MERCH"
            elif feedback == "___gg":
                current_guess = "MERCY"
            elif feedback == "___y_":
                current_guess = "CURER"
            elif feedback == "__y__":
                current_guess = "RERUN"
            elif feedback == "__y_g":
                current_guess = "NERDY"
            elif feedback == "_g___":
                current_guess = "BORED"
            elif feedback == "_g_y_":
                current_guess = "CORER"
            elif feedback == "_y___":
                current_guess = "ERROR"
            elif feedback == "_yy__":
                current_guess = "HERON"
            elif feedback == "g____":
                current_guess = "PERIL"
            elif feedback == "g___g":
                current_guess = "PERKY"
            elif feedback == "g__g_":
                current_guess = "PERCH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "POSER":
            if feedback == "y_ygg":
                current_guess = "SUPER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PRICK":
            if feedback == "_g___":
                current_guess = "TROVE"
            elif feedback == "_g_g_":
                current_guess = "TRUCE"
            elif feedback == "_gg__":
                current_guess = "TRIBE"
            elif feedback == "_gg_y":
                current_guess = "TRIKE"
            elif feedback == "_ggg_":
                current_guess = "TRICE"
            elif feedback == "_y___":
                current_guess = "THERE"
            elif feedback == "yg___":
                current_guess = "TROPE"
            elif feedback == "ygg__":
                current_guess = "TRIPE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PRIMP":
            if feedback == "_yg__":
                current_guess = "WHIRR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PRIOR":
            if feedback == "___gg":
                current_guess = "HUMOR"
            elif feedback == "__ygg":
                current_guess = "VIGOR"
            elif feedback == "_y_gg":
                current_guess = "RUMOR"
            elif feedback == "_yygg":
                current_guess = "RIGOR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PRONG":
            if feedback == "_ggg_":
                current_guess = "IRONY"
            elif feedback == "_gggg":
                current_guess = "WRONG"
            elif feedback == "_yyg_":
                current_guess = "RHINO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PSHAW":
            if feedback == "_g_y_":
                current_guess = "ASKER"
            elif feedback == "_y_g_":
                current_guess = "SMEAR"
            elif feedback == "_y_gg":
                current_guess = "RESAW"
            elif feedback == "_y_gy":
                current_guess = "SWEAR"
            elif feedback == "_yyg_":
                current_guess = "SHEAR"
            elif feedback == "yy_g_":
                current_guess = "SPEAR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PUBIC":
            if feedback == "_____":
                current_guess = "SORRY"
            elif feedback == "____y":
                current_guess = "SCROD"
            elif feedback == "___g_":
                current_guess = "LORIS"
            elif feedback == "___gy":
                current_guess = "SCRIM"
            elif feedback == "_g___":
                current_guess = "SURLY"
            elif feedback == "_y___":
                current_guess = "SHRUG"
            elif feedback == "_y__y":
                current_guess = "SCRUM"
            elif feedback == "_y_y_":
                current_guess = "VIRUS"
            elif feedback == "_yy__":
                current_guess = "SHRUB"
            elif feedback == "_yy_y":
                current_guess = "SCRUB"
            elif feedback == "y___y":
                current_guess = "CORPS"
            elif feedback == "y__g_":
                current_guess = "SPRIG"
            elif feedback == "y__gy":
                current_guess = "SCRIP"
            elif feedback == "yy___":
                current_guess = "SYRUP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PUNKY":
            if feedback == "gg__g":
                current_guess = "PUFFY"
            elif feedback == "ggg_g":
                current_guess = "PUNNY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "PYLON":
            if feedback == "_____":
                current_guess = "BASIC"
            elif feedback == "____g":
                current_guess = "BASIN"
            elif feedback == "____y":
                current_guess = "SAUNA"
            elif feedback == "___gg":
                current_guess = "MASON"
            elif feedback == "___y_":
                current_guess = "OASIS"
            elif feedback == "__g__":
                current_guess = "SALAD"
            elif feedback == "__ggg":
                current_guess = "SALON"
            elif feedback == "__gy_":
                current_guess = "SALVO"
            elif feedback == "__y__":
                current_guess = "BASAL"
            elif feedback == "__y_y":
                current_guess = "NASAL"
            elif feedback == "_y___":
                current_guess = "AGUED"
            elif feedback == "_y__y":
                current_guess = "SANDY"
            elif feedback == "_y_g_":
                current_guess = "SAVOY"
            elif feedback == "_yg__":
                current_guess = "SALLY"
            elif feedback == "_yy__":
                current_guess = "SADLY"
            elif feedback == "yy___":
                current_guess = "SAPPY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "RABID":
            if feedback == "gg_gg":
                current_guess = "RAPID"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "RADAR":
            if feedback == "ggg__":
                current_guess = "RADII"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "RAJAH":
            if feedback == "gg___":
                current_guess = "RABBI"
            elif feedback == "gg__g":
                current_guess = "RALPH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "RASPY":
            if feedback == "ygy__":
                current_guess = "SAVOR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "RAVER":
            if feedback == "_g_gg":
                current_guess = "BAKER"
            elif feedback == "_gggg":
                current_guess = "WAVER"
            elif feedback == "gg_gg":
                current_guess = "RACER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "REALM":
            if feedback == "ggg_g":
                current_guess = "REARM"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "REBAR":
            if feedback == "ggyg_":
                current_guess = "REHAB"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "REBUS":
            if feedback == "gg__y":
                current_guess = "RESIN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "REFER":
            if feedback == "gg_g_":
                current_guess = "RENEW"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "REFIX":
            if feedback == "gy_y_":
                current_guess = "RIVER"
            elif feedback == "yy_y_":
                current_guess = "GIVER"
            elif feedback == "yy_yy":
                current_guess = "MIXER"
            elif feedback == "yyyy_":
                current_guess = "FIBER"
            elif feedback == "yyyyy":
                current_guess = "FIXER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "RODNY":
            if feedback == "g____":
                current_guess = "RAJAH"
            elif feedback == "g___g":
                current_guess = "RALLY"
            elif feedback == "g__gg":
                current_guess = "RAINY"
            elif feedback == "g__y_":
                current_guess = "RANCH"
            elif feedback == "g__yg":
                current_guess = "RANGY"
            elif feedback == "g_g__":
                current_guess = "RADAR"
            elif feedback == "g_y__":
                current_guess = "RABID"
            elif feedback == "g_yyg":
                current_guess = "RANDY"
            elif feedback == "gy___":
                current_guess = "RAZOR"
            elif feedback == "gy_yy":
                current_guess = "RAYON"
            elif feedback == "gyg__":
                current_guess = "RADIO"
            elif feedback == "gygy_":
                current_guess = "RADON"
            elif feedback == "y____":
                current_guess = "CAPRI"
            elif feedback == "y___g":
                current_guess = "FAIRY"
            elif feedback == "y__y_":
                current_guess = "CAIRN"
            elif feedback == "y_gy_":
                current_guess = "NADIR"
            elif feedback == "y_y_g":
                current_guess = "DAIRY"
            elif feedback == "yy___":
                current_guess = "VALOR"
            elif feedback == "yy__y":
                current_guess = "MAYOR"
            elif feedback == "yy_y_":
                current_guess = "MANOR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "ROGUE":
            if feedback == "ggyyg":
                current_guess = "ROUGE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "RUDER":
            if feedback == "_yggg":
                current_guess = "UDDER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "RUMBA":
            if feedback == "yyyyg":
                current_guess = "UMBRA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "RUMPY":
            if feedback == "g____":
                current_guess = "REFER"
            elif feedback == "g___g":
                current_guess = "REFRY"
            elif feedback == "gy__g":
                current_guess = "REBUY"
            elif feedback == "gyy__":
                current_guess = "RHEUM"
            elif feedback == "y____":
                current_guess = "FEVER"
            elif feedback == "y___g":
                current_guess = "EVERY"
            elif feedback == "y___y":
                current_guess = "FRYER"
            elif feedback == "y__y_":
                current_guess = "PREEN"
            elif feedback == "y__yy":
                current_guess = "HYPER"
            elif feedback == "y_y__":
                current_guess = "EMBER"
            elif feedback == "y_y_g":
                current_guess = "EMERY"
            elif feedback == "yg___":
                current_guess = "QUEER"
            elif feedback == "yg__g":
                current_guess = "QUERY"
            elif feedback == "yg__y":
                current_guess = "BUYER"
            elif feedback == "yy___":
                current_guess = "EXURB"
            elif feedback == "yy_y_":
                current_guess = "UPPER"
            elif feedback == "yyg__":
                current_guess = "FEMUR"
            elif feedback == "yyy__":
                current_guess = "UMBER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SABER":
            if feedback == "gg_gg":
                current_guess = "SAFER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SABLE":
            if feedback == "gg__g":
                current_guess = "SAUCE"
            elif feedback == "gg_yg":
                current_guess = "SALVE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SALPS":
            if feedback == "gg__y":
                current_guess = "SASSY"
            elif feedback == "ggg_y":
                current_guess = "SALSA"
            elif feedback == "yg___":
                current_guess = "DAISY"
            elif feedback == "yg__y":
                current_guess = "GASSY"
            elif feedback == "yg_y_":
                current_guess = "PANSY"
            elif feedback == "ygg__":
                current_guess = "BALSA"
            elif feedback == "yggy_":
                current_guess = "PALSY"
            elif feedback == "ygy_y":
                current_guess = "LASSO"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SAPAN":
            if feedback == "gg___":
                current_guess = "SALTY"
            elif feedback == "gg__g":
                current_guess = "SATIN"
            elif feedback == "gg__y":
                current_guess = "SAINT"
            elif feedback == "gg_g_":
                current_guess = "SATAY"
            elif feedback == "yg___":
                current_guess = "HASTY"
            elif feedback == "yg__y":
                current_guess = "NASTY"
            elif feedback == "ygy__":
                current_guess = "PASTY"
            elif feedback == "ygyy_":
                current_guess = "PASTA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SCALD":
            if feedback == "gggg_":
                current_guess = "SCALY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SCAPE":
            if feedback == "gygyg":
                current_guess = "SPACE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SCARF":
            if feedback == "gggg_":
                current_guess = "SCARY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SCENE":
            if feedback == "g__gg":
                current_guess = "SHONE"
            elif feedback == "gg_gg":
                current_guess = "SCONE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SCHWA":
            if feedback == "gg__g":
                current_guess = "SCUBA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SCOOP":
            if feedback == "g___y":
                current_guess = "SPIFF"
            elif feedback == "g_ggg":
                current_guess = "SWOOP"
            elif feedback == "g_ggy":
                current_guess = "SPOOF"
            elif feedback == "g_y_y":
                current_guess = "SOPPY"
            elif feedback == "gy__y":
                current_guess = "SPICY"
            elif feedback == "y___y":
                current_guess = "WISPY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SCOOT":
            if feedback == "g_ggg":
                current_guess = "SHOOT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SCOPE":
            if feedback == "g__yg":
                current_guess = "SPUME"
            elif feedback == "g_gyg":
                current_guess = "SPOKE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SCRAM":
            if feedback == "g_gg_":
                current_guess = "SPRAY"
            elif feedback == "gggg_":
                current_guess = "SCRAP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SCREE":
            if feedback == "g_g_g":
                current_guess = "SURGE"
            elif feedback == "g_ggg":
                current_guess = "SPREE"
            elif feedback == "g_gyg":
                current_guess = "SERVE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SEDER":
            if feedback == "gg_gg":
                current_guess = "SEVER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SEDGE":
            if feedback == "gg_yg":
                current_guess = "SEGUE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHADY":
            if feedback == "g_g__":
                current_guess = "SWAMI"
            elif feedback == "ggg_g":
                current_guess = "SHAKY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHALL":
            if feedback == "g_ggg":
                current_guess = "SMALL"
            elif feedback == "ggg_g":
                current_guess = "SHAWL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHANK":
            if feedback == "g_gg_":
                current_guess = "SWANG"
            elif feedback == "g_ggg":
                current_guess = "SWANK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHARK":
            if feedback == "g_gg_":
                current_guess = "SNARF"
            elif feedback == "g_ggg":
                current_guess = "SNARK"
            elif feedback == "gggg_":
                current_guess = "SHARD"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHEEP":
            if feedback == "g_ggy":
                current_guess = "SPEED"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHEIK":
            if feedback == "g_g_g":
                current_guess = "SPECK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHIED":
            if feedback == "g_ggg":
                current_guess = "SPIED"
            elif feedback == "y__g_":
                current_guess = "MOSEY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHIFT":
            if feedback == "g_ggg":
                current_guess = "SWIFT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHILL":
            if feedback == "g___g":
                current_guess = "SCOWL"
            elif feedback == "g__g_":
                current_guess = "SCOLD"
            elif feedback == "g_ggg":
                current_guess = "SWILL"
            elif feedback == "g_ygy":
                current_guess = "SILLY"
            elif feedback == "g_yy_":
                current_guess = "SOLID"
            elif feedback == "gg_g_":
                current_guess = "SHYLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHIMS":
            if feedback == "g___y":
                current_guess = "SUDSY"
            elif feedback == "g_y_y":
                current_guess = "SISSY"
            elif feedback == "gg__y":
                current_guess = "SHUSH"
            elif feedback == "gy__y":
                current_guess = "SLOSH"
            elif feedback == "gy_yy":
                current_guess = "SMUSH"
            elif feedback == "gyg_y":
                current_guess = "SWISH"
            elif feedback == "y____":
                current_guess = "LOUSY"
            elif feedback == "y___g":
                current_guess = "FLOSS"
            elif feedback == "y___y":
                current_guess = "FUSSY"
            elif feedback == "y__y_":
                current_guess = "MOUSY"
            elif feedback == "y__yy":
                current_guess = "MOSSY"
            elif feedback == "y_g__":
                current_guess = "NOISY"
            elif feedback == "y_g_g":
                current_guess = "BLISS"
            elif feedback == "y_y__":
                current_guess = "KIOSK"
            elif feedback == "y_y_y":
                current_guess = "KISSY"
            elif feedback == "y_yyy":
                current_guess = "MISSY"
            elif feedback == "ygg__":
                current_guess = "PHISH"
            elif feedback == "yy___":
                current_guess = "ABAFT"
            elif feedback == "yy__y":
                current_guess = "HUSSY"
            elif feedback == "yyg__":
                current_guess = "KNISH"
            elif feedback == "yyy_y":
                current_guess = "HISSY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHINE":
            if feedback == "g_ggg":
                current_guess = "SWINE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHINY":
            if feedback == "g_gg_":
                current_guess = "SWING"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHIRK":
            if feedback == "g_ggg":
                current_guess = "SMIRK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHOAL":
            if feedback == "y__gg":
                current_guess = "USUAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHOCK":
            if feedback == "g_ggg":
                current_guess = "SMOCK"
            elif feedback == "ggg_g":
                current_guess = "SHOOK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHORN":
            if feedback == "g_ggg":
                current_guess = "SWORN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHOVE":
            if feedback == "g___g":
                current_guess = "SUEDE"
            elif feedback == "g_g_g":
                current_guess = "SMOKE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SHUNT":
            if feedback == "g_ggg":
                current_guess = "STUNT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SILKY":
            if feedback == "gyyy_":
                current_guess = "SKILL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SILTY":
            if feedback == "gg_g_":
                current_guess = "SIXTH"
            elif feedback == "gg_gg":
                current_guess = "SIXTY"
            elif feedback == "gy_g_":
                current_guess = "SMITH"
            elif feedback == "gy_y_":
                current_guess = "STICK"
            elif feedback == "gyyy_":
                current_guess = "STILL"
            elif feedback == "yg_gg":
                current_guess = "MISTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SKEIN":
            if feedback == "g_g_y":
                current_guess = "SPEND"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SKIFF":
            if feedback == "gy___":
                current_guess = "SMOKY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SKIMP":
            if feedback == "gyg_y":
                current_guess = "SPIKY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SLEEK":
            if feedback == "gggg_":
                current_guess = "SLEEP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SLIMY":
            if feedback == "gg__g":
                current_guess = "SLYLY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SLOSH":
            if feedback == "gg_gg":
                current_guess = "SLUSH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SMARM":
            if feedback == "g_ggg":
                current_guess = "SWARM"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SMART":
            if feedback == "g_ggg":
                current_guess = "START"
            elif feedback == "g_ggy":
                current_guess = "STARK"
            elif feedback == "g_gyy":
                current_guess = "STAIR"
            elif feedback == "g_yyy":
                current_guess = "SITAR"
            elif feedback == "y_yyy":
                current_guess = "ASTIR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SNAFU":
            if feedback == "ggg__":
                current_guess = "SNAKY"
            elif feedback == "gyg__":
                current_guess = "SWAIN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SNIPY":
            if feedback == "g____":
                current_guess = "SHEAF"
            elif feedback == "g___g":
                current_guess = "SEAMY"
            elif feedback == "g__y_":
                current_guess = "SPEAK"
            elif feedback == "g_yy_":
                current_guess = "SEPIA"
            elif feedback == "gg___":
                current_guess = "SNEAK"
            elif feedback == "gy___":
                current_guess = "SEDAN"
            elif feedback == "y____":
                current_guess = "ASKEW"
            elif feedback == "y___g":
                current_guess = "ESSAY"
            elif feedback == "y_y__":
                current_guess = "AEGIS"
            elif feedback == "yy___":
                current_guess = "ASHEN"
            elif feedback == "yy_y_":
                current_guess = "ASPEN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SNOOP":
            if feedback == "gyggy":
                current_guess = "SPOON"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SOAPY":
            if feedback == "g_gy_":
                current_guess = "SWAMP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SOOTH":
            if feedback == "gggg_":
                current_guess = "SOOTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SOUND":
            if feedback == "g_gg_":
                current_guess = "SWUNG"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SPADE":
            if feedback == "g_g_g":
                current_guess = "SUAVE"
            elif feedback == "y_g_g":
                current_guess = "USAGE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SPENT":
            if feedback == "gyg_g":
                current_guess = "SWEPT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SPICE":
            if feedback == "ggg_g":
                current_guess = "SPIKE"
            elif feedback == "gyg_g":
                current_guess = "SWIPE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SPILL":
            if feedback == "gg__g":
                current_guess = "SPOOL"
            elif feedback == "ggy_g":
                current_guess = "SPOIL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SPILT":
            if feedback == "g_ggg":
                current_guess = "STILT"
            elif feedback == "g_y_g":
                current_guess = "SIGHT"
            elif feedback == "ggyyg":
                current_guess = "SPLIT"
            elif feedback == "y_y_g":
                current_guess = "VISIT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SPITE":
            if feedback == "g_ggg":
                current_guess = "SUITE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SPORT":
            if feedback == "g_ggy":
                current_guess = "STORM"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SQUIB":
            if feedback == "g_g__":
                current_guess = "SCUFF"
            elif feedback == "gggg_":
                current_guess = "SQUID"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "STAGE":
            if feedback == "ggg_g":
                current_guess = "STAVE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "STALK":
            if feedback == "gggg_":
                current_guess = "STALL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "STAND":
            if feedback == "ggg__":
                current_guess = "STAFF"
            elif feedback == "ggg_g":
                current_guess = "STAID"
            elif feedback == "gggg_":
                current_guess = "STANK"
            elif feedback == "gggy_":
                current_guess = "STAIN"
            elif feedback == "gyg__":
                current_guess = "SWATH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "STEAK":
            if feedback == "gggg_":
                current_guess = "STEAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "STEED":
            if feedback == "ggg__":
                current_guess = "STEIN"
            elif feedback == "yyy__":
                current_guess = "ZESTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "STELE":
            if feedback == "gg_gg":
                current_guess = "STYLE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "STING":
            if feedback == "gggg_":
                current_guess = "STINK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "STOMA":
            if feedback == "yy__g":
                current_guess = "VISTA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "STONE":
            if feedback == "ggg_g":
                current_guess = "STOVE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "STREP":
            if feedback == "gggg_":
                current_guess = "STREW"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "STRUM":
            if feedback == "ggg__":
                current_guess = "STRIP"
            elif feedback == "gggg_":
                current_guess = "STRUT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "STUNG":
            if feedback == "gggg_":
                current_guess = "STUNK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "SUING":
            if feedback == "gg_g_":
                current_guess = "SUNNY"
            elif feedback == "yyggg":
                current_guess = "USING"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TABLE":
            if feedback == "gg__g":
                current_guess = "TAUPE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TALUS":
            if feedback == "gg__y":
                current_guess = "TASTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TARDY":
            if feedback == "ggg__":
                current_guess = "TAROT"
            elif feedback == "ggg_g":
                current_guess = "TARRY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TARSE":
            if feedback == "_____":
                current_guess = "GUILD"
            elif feedback == "____g":
                current_guess = "LOGIN"
            elif feedback == "____y":
                current_guess = "DYNEL"
            elif feedback == "___g_":
                current_guess = "SHIMS"
            elif feedback == "___gg":
                current_guess = "CLOUD"
            elif feedback == "___gy":
                current_guess = "COWLS"
            elif feedback == "___y_":
                current_guess = "PLUNK"
            elif feedback == "___yg":
                current_guess = "PLING"
            elif feedback == "___yy":
                current_guess = "NEWEL"
            elif feedback == "__g__":
                current_guess = "CYMOL"
            elif feedback == "__g_g":
                current_guess = "GENIO"
            elif feedback == "__g_y":
                current_guess = "PONCY"
            elif feedback == "__ggg":
                current_guess = "COUGH"
            elif feedback == "__ggy":
                current_guess = "VERSO"
            elif feedback == "__gy_":
                current_guess = "PUBIC"
            elif feedback == "__gyg":
                current_guess = "SCREE"
            elif feedback == "__gyy":
                current_guess = "CIDER"
            elif feedback == "__y__":
                current_guess = "CODON"
            elif feedback == "__y_g":
                current_guess = "POIND"
            elif feedback == "__y_y":
                current_guess = "DOLCI"
            elif feedback == "__yg_":
                current_guess = "CHIMB"
            elif feedback == "__ygg":
                current_guess = "APIOL"
            elif feedback == "__ygy":
                current_guess = "ACHED"
            elif feedback == "__yy_":
                current_guess = "CLONK"
            elif feedback == "__yyg":
                current_guess = "PINCH"
            elif feedback == "__yyy":
                current_guess = "WHEEP"
            elif feedback == "_g___":
                current_guess = "CHYND"
            elif feedback == "_g__g":
                current_guess = "GULCH"
            elif feedback == "_g__y":
                current_guess = "LYMPH"
            elif feedback == "_g_g_":
                current_guess = "SALPS"
            elif feedback == "_g_gg":
                current_guess = "LUPIN"
            elif feedback == "_g_y_":
                current_guess = "PYLON"
            elif feedback == "_g_yg":
                current_guess = "SABLE"
            elif feedback == "_g_yy":
                current_guess = "EASEL"
            elif feedback == "_gg__":
                current_guess = "CYMOL"
            elif feedback == "_gg_g":
                current_guess = "BEFOG"
            elif feedback == "_gg_y":
                current_guess = "BELCH"
            elif feedback == "_ggg_":
                current_guess = "HARSH"
            elif feedback == "_gggg":
                current_guess = "PARSE"
            elif feedback == "_gy__":
                current_guess = "RODNY"
            elif feedback == "_gy_g":
                current_guess = "CADRE"
            elif feedback == "_gy_y":
                current_guess = "GLAMP"
            elif feedback == "_gygg":
                current_guess = "RAISE"
            elif feedback == "_gyy_":
                current_guess = "RASPY"
            elif feedback == "_gyyg":
                current_guess = "SABRE"
            elif feedback == "_gyyy":
                current_guess = "ANVIL"
            elif feedback == "_y___":
                current_guess = "COLIN"
            elif feedback == "_y__g":
                current_guess = "GLAND"
            elif feedback == "_y__y":
                current_guess = "MEDAL"
            elif feedback == "_y_g_":
                current_guess = "MULCH"
            elif feedback == "_y_gg":
                current_guess = "BIACH"
            elif feedback == "_y_gy":
                current_guess = "LEASH"
            elif feedback == "_y_y_":
                current_guess = "PLANC"
            elif feedback == "_y_yg":
                current_guess = "CHALK"
            elif feedback == "_y_yy":
                current_guess = "SNIPY"
            elif feedback == "_yg__":
                current_guess = "ALOIN"
            elif feedback == "_yg_g":
                current_guess = "AERIE"
            elif feedback == "_yg_y":
                current_guess = "FERAL"
            elif feedback == "_ygg_":
                current_guess = "BURSA"
            elif feedback == "_ygy_":
                current_guess = "SCRAM"
            elif feedback == "_yy__":
                current_guess = "BLOND"
            elif feedback == "_yy_g":
                current_guess = "GRAND"
            elif feedback == "_yy_y":
                current_guess = "BEMAD"
            elif feedback == "_yyg_":
                current_guess = "ABACS"
            elif feedback == "_yygg":
                current_guess = "ARISE"
            elif feedback == "_yyy_":
                current_guess = "CLAMP"
            elif feedback == "_yyyg":
                current_guess = "ANCHO"
            elif feedback == "_yyyy":
                current_guess = "PSHAW"
            elif feedback == "g____":
                current_guess = "CUING"
            elif feedback == "g___g":
                current_guess = "CHILD"
            elif feedback == "g___y":
                current_guess = "HONED"
            elif feedback == "g__g_":
                current_guess = "TIPSY"
            elif feedback == "g__gg":
                current_guess = "TENSE"
            elif feedback == "g__yy":
                current_guess = "TELOS"
            elif feedback == "g_g__":
                current_guess = "THROB"
            elif feedback == "g_g_g":
                current_guess = "THREE"
            elif feedback == "g_g_y":
                current_guess = "THREW"
            elif feedback == "g_gg_":
                current_guess = "TORSO"
            elif feedback == "g_ggg":
                current_guess = "TERSE"
            elif feedback == "g_gy_":
                current_guess = "TORUS"
            elif feedback == "g_y__":
                current_guess = "HOKUM"
            elif feedback == "g_y_g":
                current_guess = "PRICK"
            elif feedback == "g_y_y":
                current_guess = "MINOR"
            elif feedback == "g_yg_":
                current_guess = "TRUSS"
            elif feedback == "g_ygy":
                current_guess = "TRESS"
            elif feedback == "gg___":
                current_guess = "LINKY"
            elif feedback == "gg__g":
                current_guess = "TABLE"
            elif feedback == "gg__y":
                current_guess = "TAKEN"
            elif feedback == "gg_y_":
                current_guess = "TALUS"
            elif feedback == "gg_yg":
                current_guess = "TASTE"
            elif feedback == "ggg__":
                current_guess = "TARDY"
            elif feedback == "ggy__":
                current_guess = "TAPIR"
            elif feedback == "ggy_y":
                current_guess = "KEMPS"
            elif feedback == "ggyyy":
                current_guess = "TASER"
            elif feedback == "gy___":
                current_guess = "DOGAN"
            elif feedback == "gy__y":
                current_guess = "TEACH"
            elif feedback == "gy_g_":
                current_guess = "TOAST"
            elif feedback == "gy_gg":
                current_guess = "TEASE"
            elif feedback == "gyg__":
                current_guess = "TORAH"
            elif feedback == "gyg_y":
                current_guess = "TERRA"
            elif feedback == "gyy__":
                current_guess = "CLINT"
            elif feedback == "gyy_g":
                current_guess = "TRACE"
            elif feedback == "gyy_y":
                current_guess = "TETRA"
            elif feedback == "gyyg_":
                current_guess = "TRASH"
            elif feedback == "gyyy_":
                current_guess = "TRANS"
            elif feedback == "y____":
                current_guess = "DONUT"
            elif feedback == "y___g":
                current_guess = "BUILD"
            elif feedback == "y___y":
                current_guess = "PILED"
            elif feedback == "y__g_":
                current_guess = "HIMBO"
            elif feedback == "y__gy":
                current_guess = "DIGHT"
            elif feedback == "y__y_":
                current_guess = "FOUNT"
            elif feedback == "y__yg":
                current_guess = "MILKO"
            elif feedback == "y__yy":
                current_guess = "PLUOT"
            elif feedback == "y_g__":
                current_guess = "BIFFY"
            elif feedback == "y_g_g":
                current_guess = "FORTE"
            elif feedback == "y_g_y":
                current_guess = "BERET"
            elif feedback == "y_gg_":
                current_guess = "WURST"
            elif feedback == "y_gy_":
                current_guess = "STRUM"
            elif feedback == "y_gyy":
                current_guess = "STREP"
            elif feedback == "y_y__":
                current_guess = "BIONT"
            elif feedback == "y_y_g":
                current_guess = "BIOTA"
            elif feedback == "y_y_y":
                current_guess = "COURT"
            elif feedback == "y_yg_":
                current_guess = "BOGUE"
            elif feedback == "y_ygy":
                current_guess = "CREST"
            elif feedback == "y_yy_":
                current_guess = "HONKY"
            elif feedback == "y_yyg":
                current_guess = "STORE"
            elif feedback == "y_yyy":
                current_guess = "ESTER"
            elif feedback == "yg___":
                current_guess = "CLIPT"
            elif feedback == "yg__g":
                current_guess = "CLOTH"
            elif feedback == "yg__y":
                current_guess = "LEMED"
            elif feedback == "yg_g_":
                current_guess = "PATSY"
            elif feedback == "yg_y_":
                current_guess = "SAPAN"
            elif feedback == "yg_yg":
                current_guess = "BUCHU"
            elif feedback == "ygg__":
                current_guess = "APACE"
            elif feedback == "ygg_g":
                current_guess = "CARTE"
            elif feedback == "ygg_y":
                current_guess = "CARET"
            elif feedback == "ygy__":
                current_guess = "GATOR"
            elif feedback == "ygy_y":
                current_guess = "CHAWL"
            elif feedback == "ygyy_":
                current_guess = "SATYR"
            elif feedback == "yy___":
                current_guess = "PLOIT"
            elif feedback == "yy__g":
                current_guess = "ABOMA"
            elif feedback == "yy__y":
                current_guess = "PLANC"
            elif feedback == "yy_g_":
                current_guess = "BOAST"
            elif feedback == "yy_gy":
                current_guess = "AFFLY"
            elif feedback == "yy_y_":
                current_guess = "CLAPT"
            elif feedback == "yy_yg":
                current_guess = "KLETT"
            elif feedback == "yy_yy":
                current_guess = "ADMIT"
            elif feedback == "yyg__":
                current_guess = "AORTA"
            elif feedback == "yygy_":
                current_guess = "APAYD"
            elif feedback == "yyy__":
                current_guess = "ARGOT"
            elif feedback == "yyy_g":
                current_guess = "ACING"
            elif feedback == "yyy_y":
                current_guess = "ALERT"
            elif feedback == "yyyg_":
                current_guess = "ARTSY"
            elif feedback == "yyyy_":
                current_guess = "SMART"
            elif feedback == "yyyyg":
                current_guess = "STARE"
            elif feedback == "yyyyy":
                current_guess = "ASTER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TEACH":
            if feedback == "gyy__":
                current_guess = "TWEAK"
            elif feedback == "gyy_y":
                current_guess = "THETA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TEETH":
            if feedback == "g_gyy":
                current_guess = "THEFT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TELOS":
            if feedback == "gg__y":
                current_guess = "TESTY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TENSE":
            if feedback == "g__gg":
                current_guess = "THOSE"
            elif feedback == "gy_gg":
                current_guess = "THESE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TETRA":
            if feedback == "gg_gy":
                current_guess = "TEARY"
            elif feedback == "gy_yy":
                current_guess = "TREAD"
            elif feedback == "gyyyy":
                current_guess = "TREAT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "THEIR":
            if feedback == "g_yyg":
                current_guess = "TRIER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "THEME":
            if feedback == "gg_gg":
                current_guess = "THYME"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "THING":
            if feedback == "g_ggg":
                current_guess = "TYING"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "THREE":
            if feedback == "g_g_g":
                current_guess = "TORTE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "THREW":
            if feedback == "g_gg_":
                current_guess = "TIRED"
            elif feedback == "g_gy_":
                current_guess = "TERRY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "THROB":
            if feedback == "g_gyy":
                current_guess = "TURBO"
            elif feedback == "ggg__":
                current_guess = "THRUM"
            elif feedback == "gggg_":
                current_guess = "THROW"
            elif feedback == "gygy_":
                current_guess = "TORCH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "THUMB":
            if feedback == "gggg_":
                current_guess = "THUMP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TIGER":
            if feedback == "gg_gg":
                current_guess = "TITER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TIMID":
            if feedback == "gg___":
                current_guess = "TIZZY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TIPSY":
            if feedback == "gy_g_":
                current_guess = "TWIST"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TODDY":
            if feedback == "gg___":
                current_guess = "TOOTH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TOPAZ":
            if feedback == "gg_g_":
                current_guess = "TOTAL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TOPIC":
            if feedback == "gg_gg":
                current_guess = "TOXIC"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TORAH":
            if feedback == "gggy_":
                current_guess = "TORTA"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TOTEM":
            if feedback == "gg_g_":
                current_guess = "TOWEL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TRACE":
            if feedback == "ggg_g":
                current_guess = "TRADE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TRIBE":
            if feedback == "ggg_g":
                current_guess = "TRITE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TRILL":
            if feedback == "gyg_g":
                current_guess = "TWIRL"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TROLL":
            if feedback == "ggg__":
                current_guess = "TROOP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TRUCK":
            if feedback == "ggg_g":
                current_guess = "TRUNK"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TRUER":
            if feedback == "g_ygg":
                current_guess = "TUBER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TRUSS":
            if feedback == "gg_g_":
                current_guess = "TRYST"
            elif feedback == "gggg_":
                current_guess = "TRUST"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TWERK":
            if feedback == "gggg_":
                current_guess = "TWERP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "TWILL":
            if feedback == "ggg__":
                current_guess = "TWIXT"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "UNFED":
            if feedback == "_g_gy":
                current_guess = "INDEX"
            elif feedback == "_y_gy":
                current_guess = "WIDEN"
            elif feedback == "gg_gg":
                current_guess = "UNWED"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "UNHIP":
            if feedback == "gg_gg":
                current_guess = "UNZIP"
            elif feedback == "gg_gy":
                current_guess = "UNPIN"
            elif feedback == "y__yg":
                current_guess = "MIXUP"
            elif feedback == "yy_yg":
                current_guess = "PINUP"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "USURP":
            if feedback == "gggg_":
                current_guess = "USURY"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "VALID":
            if feedback == "gg_gg":
                current_guess = "VAPID"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "VALOR":
            if feedback == "_g_gg":
                current_guess = "MAJOR"
            elif feedback == "_g_yy":
                current_guess = "MACRO"
            elif feedback == "_gygg":
                current_guess = "LABOR"
            elif feedback == "gg_gg":
                current_guess = "VAPOR"
            elif feedback == "yg_gg":
                current_guess = "FAVOR"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "VENOM":
            if feedback == "_gg__":
                current_guess = "BENCH"
            elif feedback == "_ggg_":
                current_guess = "XENON"
            elif feedback == "_yg__":
                current_guess = "ENNUI"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "VOCAB":
            if feedback == "___y_":
                current_guess = "FRAME"
            elif feedback == "___yy":
                current_guess = "BRAKE"
            elif feedback == "__yy_":
                current_guess = "CRAZE"
            elif feedback == "__yyy":
                current_guess = "BRACE"
            elif feedback == "y__yy":
                current_guess = "BRAVE"
            elif feedback == "y_yy_":
                current_guess = "CRAVE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "WHEEP":
            if feedback == "___g_":
                current_guess = "MISER"
            elif feedback == "___gy":
                current_guess = "POSER"
            elif feedback == "__g_y":
                current_guess = "SPERM"
            elif feedback == "__gg_":
                current_guess = "SNEER"
            elif feedback == "__y__":
                current_guess = "REBUS"
            elif feedback == "__yg_":
                current_guess = "SEDER"
            elif feedback == "_g_g_":
                current_guess = "SHYER"
            elif feedback == "_ggg_":
                current_guess = "SHEER"
            elif feedback == "_y_g_":
                current_guess = "USHER"
            elif feedback == "g__g_":
                current_guess = "WISER"
            elif feedback == "y__g_":
                current_guess = "SOWER"
            elif feedback == "y_yg_":
                current_guess = "SEWER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "WHOMP":
            if feedback == "__g__":
                current_guess = "BOOBY"
            elif feedback == "__g_y":
                current_guess = "POOFY"
            elif feedback == "__gy_":
                current_guess = "MOONY"
            elif feedback == "__y__":
                current_guess = "GUNKY"
            elif feedback == "__y_y":
                current_guess = "POKER"
            elif feedback == "__yg_":
                current_guess = "MOMMY"
            elif feedback == "__yy_":
                current_guess = "MOVER"
            elif feedback == "__yyy":
                current_guess = "MOPER"
            elif feedback == "_gg__":
                current_guess = "CHOCK"
            elif feedback == "_gg_y":
                current_guess = "PHONY"
            elif feedback == "_gggg":
                current_guess = "CHOMP"
            elif feedback == "_y_yy":
                current_guess = "NYMPH"
            elif feedback == "_yg__":
                current_guess = "HOOCH"
            elif feedback == "_yg_y":
                current_guess = "POOCH"
            elif feedback == "_ygy_":
                current_guess = "MOOCH"
            elif feedback == "_yy__":
                current_guess = "HOVER"
            elif feedback == "_yy_y":
                current_guess = "HOPPY"
            elif feedback == "_yyy_":
                current_guess = "HOMER"
            elif feedback == "_yyyy":
                current_guess = "OOMPH"
            elif feedback == "g_g__":
                current_guess = "WOOER"
            elif feedback == "g_y__":
                current_guess = "WONKY"
            elif feedback == "ggg_g":
                current_guess = "WHOOP"
            elif feedback == "y_g__":
                current_guess = "KNOWN"
            elif feedback == "y_y__":
                current_guess = "BOWER"
            elif feedback == "y_y_y":
                current_guess = "POWER"
            elif feedback == "y_yy_":
                current_guess = "MOWER"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "WIFTY":
            if feedback == "_g_gg":
                current_guess = "BITTY"
            elif feedback == "_g_y_":
                current_guess = "HITCH"
            elif feedback == "_g_yg":
                current_guess = "PITHY"
            elif feedback == "_ggg_":
                current_guess = "FIFTH"
            elif feedback == "_gggg":
                current_guess = "FIFTY"
            elif feedback == "_gyg_":
                current_guess = "FILTH"
            elif feedback == "_y_g_":
                current_guess = "BLITZ"
            elif feedback == "_y_yg":
                current_guess = "ITCHY"
            elif feedback == "gg_gg":
                current_guess = "WITTY"
            elif feedback == "gg_y_":
                current_guess = "WITCH"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "WINCE":
            if feedback == "_gggg":
                current_guess = "MINCE"
            elif feedback == "_gygg":
                current_guess = "NIECE"
            elif feedback == "_gyyg":
                current_guess = "NICHE"
            elif feedback == "_yy_g":
                current_guess = "KNIFE"
            elif feedback == "gyy_g":
                current_guess = "WHINE"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "WOKEN":
            if feedback == "gg_gg":
                current_guess = "WOMEN"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_guess == "WURST":
            if feedback == "__ggg":
                current_guess = "FIRST"
            elif feedback == "_gggg":
                current_guess = "BURST"
            elif feedback == "g_ggg":
                current_guess = "WORST"
            else:
                print("Pattern variant not found in tree paths.")
                return
        else:
            print("Pattern variant not found in tree paths.")
            return

if __name__ == "__main__":
    play_wordle_generated()
