def play_wordle_generated():
    print("--- Wordle ---")
    current_state = "TARSE_1"

    while True:
        # Extract the real word from the turn-tracked state label
        current_guess = current_state.split("_")[0]
        print(f"Current Guess: {current_guess}")
        feedback = input(f"Enter feedback for {current_guess}: ").strip().lower()
        if feedback == "ggggg":
            print(f"SOLVED! Word is {current_guess}")
            return

        if current_state == "AARGH_3":
            if feedback == "gyy__":
                current_state = "AWARD_4"
            elif feedback == "y_y__":
                current_state = "FRAUD_4"
            elif feedback == "y_y_y":
                current_state = "CHARD_4"
            elif feedback == "y_yy_":
                current_state = "GUARD_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABACK_3":
            if feedback == "__g__":
                current_state = "GLAND_4"
            elif feedback == "__g_g":
                current_state = "FLANK_4"
            elif feedback == "_yg__":
                current_state = "BLAND_4"
            elif feedback == "_yg_g":
                current_state = "BLANK_4"
            elif feedback == "g____":
                current_state = "ANNUL_4"
            elif feedback == "g_y__":
                current_state = "ANNAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABACS_2":
            if feedback == "__g_g":
                current_state = "GRASS_3"
            elif feedback == "__g_y":
                current_state = "GRASP_3"
            elif feedback == "__gyg":
                current_state = "CRASS_3"
            elif feedback == "__gyy":
                current_state = "CRASH_3"
            elif feedback == "_yg_g":
                current_state = "BRASS_3"
            elif feedback == "_yg_y":
                current_state = "BRASH_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABAFT_3":
            if feedback == "_____":
                current_state = "PLUSH_4"
            elif feedback == "___y_":
                current_state = "FLUSH_4"
            elif feedback == "_y___":
                current_state = "BLUSH_4"
            elif feedback == "g__gg":
                current_state = "ALOFT_4"
            elif feedback == "y___g":
                current_state = "GLOAT_4"
            elif feedback == "y___y":
                current_state = "TATTY_4"
            elif feedback == "y__gy":
                current_state = "TAFFY_4"
            elif feedback == "y__yg":
                current_state = "FLOAT_4"
            elif feedback == "yy__g":
                current_state = "BLOAT_4"
            elif feedback == "yy__y":
                current_state = "TABBY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABETS_3":
            if feedback == "___g_":
                current_state = "TUFTY_4"
            elif feedback == "___y_":
                current_state = "TUMMY_4"
            elif feedback == "_y_y_":
                current_state = "TUBBY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABHOR_3":
            if feedback == "_____":
                current_state = "MUGGY_4"
            elif feedback == "___y_":
                current_state = "FUNGO_4"
            elif feedback == "__y__":
                current_state = "HUGGY_4"
            elif feedback == "_y___":
                current_state = "BUGGY_4"
            elif feedback == "gy_gg":
                current_state = "ARBOR_4"
            elif feedback == "yy_yy":
                current_state = "COBRA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABIDE_3":
            if feedback == "gg_gg":
                current_state = "ABODE_4"
            elif feedback == "gy_yg":
                current_state = "ADOBE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABJUD_3":
            if feedback == "g____":
                current_state = "AVAIL_4"
            elif feedback == "y____":
                current_state = "FLAIL_4"
            elif feedback == "y___g":
                current_state = "PLAID_4"
            elif feedback == "y__y_":
                current_state = "QUAIL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABLET_3":
            if feedback == "___y_":
                current_state = "PROVE_4"
            elif feedback == "__yy_":
                current_state = "PROLE_4"
            elif feedback == "_y_y_":
                current_state = "PROBE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABLOW_3":
            if feedback == "__g__":
                current_state = "FILLY_4"
            elif feedback == "__g_y":
                current_state = "WILLY_4"
            elif feedback == "__y__":
                current_state = "IMPLY_4"
            elif feedback == "_yg__":
                current_state = "BILLY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABOMA_2":
            if feedback == "g____":
                current_state = "ACUTE_3"
            elif feedback == "g___y":
                current_state = "AGATE_3"
            elif feedback == "g_g__":
                current_state = "ATONE_3"
            elif feedback == "gg__y":
                current_state = "ABATE_3"
            elif feedback == "y____":
                current_state = "ELATE_3"
            elif feedback == "y_y__":
                current_state = "OVATE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABOUT_3":
            if feedback == "g_g_g":
                current_state = "AFOOT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABOVE_3":
            if feedback == "g_g_g":
                current_state = "AWOKE_4"
            elif feedback == "y___g":
                current_state = "PUPAE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ABYSM_3":
            if feedback == "y____":
                current_state = "LADLE_4"
            elif feedback == "y___y":
                current_state = "MAPLE_4"
            elif feedback == "yy___":
                current_state = "FABLE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ACCOY_3":
            if feedback == "___y_":
                current_state = "MOUTH_4"
            elif feedback == "___yg":
                current_state = "POUTY_4"
            elif feedback == "___yy":
                current_state = "YOUTH_4"
            elif feedback == "_y_y_":
                current_state = "COUTH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ACHED_2":
            if feedback == "___y_":
                current_state = "PRESS_3"
            elif feedback == "___yy":
                current_state = "DRESS_3"
            elif feedback == "__yy_":
                current_state = "FRESH_3"
            elif feedback == "_y_y_":
                current_state = "CRESS_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ACING_2":
            if feedback == "y____":
                current_state = "ORATE_3"
            elif feedback == "y___y":
                current_state = "GRATE_3"
            elif feedback == "y_y__":
                current_state = "IRATE_3"
            elif feedback == "yy___":
                current_state = "CRATE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ACMES_3":
            if feedback == "_____":
                current_state = "FOUNT_4"
            elif feedback == "___y_":
                current_state = "PRIZE_4"
            elif feedback == "__y__":
                current_state = "MOUNT_4"
            elif feedback == "__yy_":
                current_state = "PRIME_4"
            elif feedback == "_y___":
                current_state = "COUNT_4"
            elif feedback == "_y_y_":
                current_state = "PRICE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ACORN_3":
            if feedback == "y_gyg":
                current_state = "GROAN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ADAPT_3":
            if feedback == "g____":
                current_state = "AGING_4"
            elif feedback == "g__y_":
                current_state = "APING_4"
            elif feedback == "g_y__":
                current_state = "ANIMA_4"
            elif feedback == "y____":
                current_state = "NINJA_4"
            elif feedback == "yy___":
                current_state = "KINDA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ADEEM_3":
            if feedback == "_____":
                current_state = "STUCK_4"
            elif feedback == "____y":
                current_state = "STUMP_4"
            elif feedback == "__y__":
                current_state = "SLICE_4"
            elif feedback == "__y_y":
                current_state = "SLIME_4"
            elif feedback == "_y___":
                current_state = "STUDY_4"
            elif feedback == "_yy__":
                current_state = "SLIDE_4"
            elif feedback == "y__g_":
                current_state = "RATER_4"
            elif feedback == "y_yg_":
                current_state = "EATER_4"
            elif feedback == "yy_g_":
                current_state = "DATER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ADEPT_3":
            if feedback == "y_yyg":
                current_state = "EXPAT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ADIOS_3":
            if feedback == "g___y":
                current_state = "ASSAY_4"
            elif feedback == "y___y":
                current_state = "SQUAB_4"
            elif feedback == "y_g_y":
                current_state = "SHIVA_4"
            elif feedback == "y_y_y":
                current_state = "SIGMA_4"
            elif feedback == "yy__y":
                current_state = "SQUAD_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ADLIB_3":
            if feedback == "_____":
                current_state = "GUSTY_4"
            elif feedback == "____y":
                current_state = "BUSTY_4"
            elif feedback == "___y_":
                current_state = "SITUP_4"
            elif feedback == "__y__":
                current_state = "LUSTY_4"
            elif feedback == "_y___":
                current_state = "DUSTY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ADMIN_3":
            if feedback == "g__gg":
                current_state = "AGAIN_4"
            elif feedback == "gg___":
                current_state = "ADDER_4"
            elif feedback == "gy___":
                current_state = "ALDER_4"
            elif feedback == "gy_y_":
                current_state = "AIDER_4"
            elif feedback == "y____":
                current_state = "PAYEE_4"
            elif feedback == "y__y_":
                current_state = "WAIVE_4"
            elif feedback == "y__yy":
                current_state = "NAIVE_4"
            elif feedback == "y_y__":
                current_state = "MAYBE_4"
            elif feedback == "y_yy_":
                current_state = "MAIZE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ADMIT_2":
            if feedback == "g___g":
                current_state = "ASSET_3"
            elif feedback == "y___g":
                current_state = "SWEAT_3"
            elif feedback == "y___y":
                current_state = "STEAK_3"
            elif feedback == "y_y_y":
                current_state = "STEAM_3"
            elif feedback == "yy__y":
                current_state = "STEAD_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ADMIT_3":
            if feedback == "g__gg":
                current_state = "AWAIT_4"
            elif feedback == "g_ygg":
                current_state = "AMBIT_4"
            elif feedback == "gy_gg":
                current_state = "AUDIT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ADSUM_3":
            if feedback == "__gy_":
                current_state = "HUSKY_4"
            elif feedback == "__gyy":
                current_state = "MUSKY_4"
            elif feedback == "_ygy_":
                current_state = "DUSKY_4"
            elif feedback == "_yyy_":
                current_state = "KUDOS_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ADVEW_3":
            if feedback == "___g_":
                current_state = "LONER_4"
            elif feedback == "___gy":
                current_state = "LOWER_4"
            elif feedback == "__gg_":
                current_state = "LOVER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ADVEW_4":
            if feedback == "___g_":
                current_state = "RIPER_5"
            elif feedback == "___gy":
                current_state = "WIPER_5"
            elif feedback == "__yg_":
                current_state = "VIPER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AERIE_2":
            if feedback == "gyg_g":
                current_state = "AGREE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AFALD_3":
            if feedback == "g__gg":
                current_state = "AHOLD_4"
            elif feedback == "g__yg":
                current_state = "ALOUD_4"
            elif feedback == "g_yy_":
                current_state = "ALOHA_4"
            elif feedback == "gg_y_":
                current_state = "AFOUL_4"
            elif feedback == "gy_y_":
                current_state = "ALOOF_4"
            elif feedback == "y__y_":
                current_state = "GLOAM_4"
            elif feedback == "yg_y_":
                current_state = "OFFAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AFFIX_3":
            if feedback == "g__g_":
                current_state = "APHID_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AFFLY_2":
            if feedback == "y____":
                current_state = "BEAST_3"
            elif feedback == "y___y":
                current_state = "YEAST_3"
            elif feedback == "y__y_":
                current_state = "LEAST_3"
            elif feedback == "yy___":
                current_state = "FEAST_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AFION_3":
            if feedback == "__g__":
                current_state = "PLIER_4"
            elif feedback == "__y__":
                current_state = "LIVER_4"
            elif feedback == "__y_y":
                current_state = "LINER_4"
            elif feedback == "_yg__":
                current_state = "FLIER_4"
            elif feedback == "_yy__":
                current_state = "LIFER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AFIRE_3":
            if feedback == "g__gg":
                current_state = "AZURE_4"
            elif feedback == "gg_gg":
                current_state = "AFORE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AFLAJ_3":
            if feedback == "_____":
                current_state = "PUDGY_4"
            elif feedback == "____y":
                current_state = "JUDGY_4"
            elif feedback == "_y___":
                current_state = "FUDGY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AFLOW_3":
            if feedback == "y____":
                current_state = "CREAK_4"
            elif feedback == "y___y":
                current_state = "WREAK_4"
            elif feedback == "y_y__":
                current_state = "CLEAR_4"
            elif feedback == "yy___":
                current_state = "FREAK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AFLOW_4":
            if feedback == "_____":
                current_state = "CINCH_5"
            elif feedback == "____y":
                current_state = "WINCH_5"
            elif feedback == "_y___":
                current_state = "FINCH_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AFOAM_3":
            if feedback == "y____":
                current_state = "WALTZ_4"
            elif feedback == "y___y":
                current_state = "MALTY_4"
            elif feedback == "y__g_":
                current_state = "NATAL_4"
            elif feedback == "yy_g_":
                current_state = "FATAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AGAPE_3":
            if feedback == "_yg_g":
                current_state = "IMAGE_4"
            elif feedback == "_ygyg":
                current_state = "PHAGE_4"
            elif feedback == "ggg_g":
                current_state = "AGAVE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AGBAS_3":
            if feedback == "_____":
                current_state = "QUILT_4"
            elif feedback == "__g__":
                current_state = "CUBIT_4"
            elif feedback == "__y__":
                current_state = "BUILT_4"
            elif feedback == "_y___":
                current_state = "GUILT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AGING_4":
            if feedback == "g_ggg":
                current_state = "AXING_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AGITA_3":
            if feedback == "g_gg_":
                current_state = "AMITY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AGLEY_3":
            if feedback == "y__y_":
                current_state = "RECAP_4"
            elif feedback == "y__yg":
                current_state = "REPAY_4"
            elif feedback == "y_gy_":
                current_state = "RELAX_4"
            elif feedback == "y_gyg":
                current_state = "RELAY_4"
            elif feedback == "y_yy_":
                current_state = "RENAL_4"
            elif feedback == "yyyy_":
                current_state = "REGAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AGLOW_3":
            if feedback == "g_gg_":
                current_state = "ALLOY_4"
            elif feedback == "g_ggg":
                current_state = "ALLOW_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AGONY_3":
            if feedback == "g_yyg":
                current_state = "ANNOY_4"
            elif feedback == "gygg_":
                current_state = "AMONG_4"
            elif feedback == "yyyg_":
                current_state = "GUANO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AGORA_3":
            if feedback == "g_gy_":
                current_state = "AMOUR_4"
            elif feedback == "g_gyg":
                current_state = "AROMA_4"
            elif feedback == "y_gy_":
                current_state = "CROAK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AGUED_3":
            if feedback == "y____":
                current_state = "SAVVY_4"
            elif feedback == "y_g__":
                current_state = "SAUCY_4"
            elif feedback == "yy___":
                current_state = "SAGGY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AHEAD_3":
            if feedback == "__ggg":
                current_state = "KNEAD_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AHING_3":
            if feedback == "_____":
                current_state = "MOOSE_4"
            elif feedback == "____y":
                current_state = "GOOSE_4"
            elif feedback == "___y_":
                current_state = "NOOSE_4"
            elif feedback == "_g___":
                current_state = "WHOSE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AIOLI_3":
            if feedback == "yggg_":
                current_state = "VIOLA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ALARM_3":
            if feedback == "_ggy_":
                current_state = "FLAIR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ALERT_2":
            if feedback == "g_ggg":
                current_state = "AVERT_3"
            elif feedback == "g_yyy":
                current_state = "AFTER_3"
            elif feedback == "ggyyy":
                current_state = "ALTER_3"
            elif feedback == "y_gyg":
                current_state = "GREAT_3"
            elif feedback == "y_ygg":
                current_state = "HEART_3"
            elif feedback == "y_ygy":
                current_state = "EXTRA_3"
            elif feedback == "y_yyg":
                current_state = "REACT_3"
            elif feedback == "y_yyy":
                current_state = "RETAG_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ALIBI_3":
            if feedback == "gyg__":
                current_state = "AXIAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ALIEN_3":
            if feedback == "gg_g_":
                current_state = "ALLEY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ALIKE_3":
            if feedback == "ggg_g":
                current_state = "ALIVE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ALLAY_3":
            if feedback == "__gg_":
                current_state = "GULAG_4"
            elif feedback == "__ggy":
                current_state = "BYLAW_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ALOIN_2":
            if feedback == "g____":
                current_state = "ARRAY_3"
            elif feedback == "g__g_":
                current_state = "ACRID_3"
            elif feedback == "g_y__":
                current_state = "ARROW_3"
            elif feedback == "g_y_g":
                current_state = "APRON_3"
            elif feedback == "gy___":
                current_state = "AURAL_3"
            elif feedback == "y____":
                current_state = "BURKA_3"
            elif feedback == "y___g":
                current_state = "QURAN_3"
            elif feedback == "y__g_":
                current_state = "CURIA_3"
            elif feedback == "y__y_":
                current_state = "CIRCA_3"
            elif feedback == "y_y__":
                current_state = "FORAY_3"
            elif feedback == "y_y_g":
                current_state = "KORAN_3"
            elif feedback == "yy___":
                current_state = "MURAL_3"
            elif feedback == "yy_y_":
                current_state = "VIRAL_3"
            elif feedback == "yyy__":
                current_state = "CORAL_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AMASS_3":
            if feedback == "_yggy":
                current_state = "SPASM_4"
            elif feedback == "gg_gg":
                current_state = "AMISS_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AMBAN_3":
            if feedback == "_____":
                current_state = "GUPPY_4"
            elif feedback == "____y":
                current_state = "GUNKY_4"
            elif feedback == "_y___":
                current_state = "GUMMY_4"
            elif feedback == "_yy__":
                current_state = "GUMBO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AMBLE_3":
            if feedback == "g__gg":
                current_state = "APPLE_4"
            elif feedback == "gg_gg":
                current_state = "AMPLE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AMBRY_3":
            if feedback == "___gg":
                current_state = "FERRY_4"
            elif feedback == "___yg":
                current_state = "JERKY_4"
            elif feedback == "__ygg":
                current_state = "BERRY_4"
            elif feedback == "__yyg":
                current_state = "DERBY_4"
            elif feedback == "_y_gg":
                current_state = "MERRY_4"
            elif feedback == "_y_yg":
                current_state = "GERMY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AMEND_3":
            if feedback == "yyg_y":
                current_state = "EDEMA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AMIGO_3":
            if feedback == "gyg_y":
                current_state = "AXIOM_4"
            elif feedback == "y_g_y":
                current_state = "OUIJA_4"
            elif feedback == "y_y_y":
                current_state = "OKAPI_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AMINO_3":
            if feedback == "y_ygg":
                current_state = "PIANO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AMPED_3":
            if feedback == "y__y_":
                current_state = "SHAVE_4"
            elif feedback == "y__yy":
                current_state = "SHADE_4"
            elif feedback == "y_yy_":
                current_state = "SHAPE_4"
            elif feedback == "yy_y_":
                current_state = "SHAME_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AMPLY_3":
            if feedback == "g__y_":
                current_state = "AWFUL_4"
            elif feedback == "g_ggg":
                current_state = "APPLY_4"
            elif feedback == "g_gy_":
                current_state = "ALPHA_4"
            elif feedback == "gy_y_":
                current_state = "ALBUM_4"
            elif feedback == "y__g_":
                current_state = "UVULA_4"
            elif feedback == "y__y_":
                current_state = "FUGAL_4"
            elif feedback == "y__yg":
                current_state = "FLAKY_4"
            elif feedback == "y_yy_":
                current_state = "PLAZA_4"
            elif feedback == "y_yyy":
                current_state = "PLAYA_4"
            elif feedback == "yy_g_":
                current_state = "QUALM_4"
            elif feedback == "yy_y_":
                current_state = "LLAMA_4"
            elif feedback == "yyyy_":
                current_state = "GLAMP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AMUCK_3":
            if feedback == "g__gg":
                current_state = "ABACK_4"
            elif feedback == "y__gg":
                current_state = "WHACK_4"
            elif feedback == "y_yg_":
                current_state = "YUCCA_4"
            elif feedback == "y_ygg":
                current_state = "QUACK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ANCHO_2":
            if feedback == "y____":
                current_state = "SPARE_3"
            elif feedback == "y__y_":
                current_state = "SHARE_3"
            elif feedback == "y_y__":
                current_state = "SCARE_3"
            elif feedback == "yg___":
                current_state = "SNARE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ANGER_3":
            if feedback == "g_ggg":
                current_state = "AUGER_4"
            elif feedback == "gy_yy":
                current_state = "ARENA_4"
            elif feedback == "y__yy":
                current_state = "OPERA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ANGRY_3":
            if feedback == "yg_g_":
                current_state = "UNARM_4"
            elif feedback == "yy_y_":
                current_state = "PRAWN_4"
            elif feedback == "yyyy_":
                current_state = "GRAIN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ANKLE_3":
            if feedback == "gg_gg":
                current_state = "ANOLE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ANNEX_3":
            if feedback == "g__g_":
                current_state = "ABBEY_4"
            elif feedback == "g_gg_":
                current_state = "APNEA_4"
            elif feedback == "yy_y_":
                current_state = "HYENA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ANTIC_3":
            if feedback == "g_ggg":
                current_state = "ATTIC_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ANVIL_2":
            if feedback == "y____":
                current_state = "SABER_3"
            elif feedback == "y___y":
                current_state = "LASER_3"
            elif feedback == "y_g__":
                current_state = "SAVER_3"
            elif feedback == "yy___":
                current_state = "SANER_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AORTA_2":
            if feedback == "g_gyg":
                current_state = "ATRIA_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "APACE_2":
            if feedback == "y____":
                current_state = "WARTY_3"
            elif feedback == "y_y__":
                current_state = "KARAT_3"
            elif feedback == "y_yy_":
                current_state = "CARAT_3"
            elif feedback == "yy___":
                current_state = "PARTY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "APAYD_2":
            if feedback == "y____":
                current_state = "STRAW_3"
            elif feedback == "y__y_":
                current_state = "STRAY_3"
            elif feedback == "yy___":
                current_state = "STRAP_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "APEEK_3":
            if feedback == "__g__":
                current_state = "CHEWY_4"
            elif feedback == "__gy_":
                current_state = "BEEFY_4"
            elif feedback == "__gyy":
                current_state = "GEEKY_4"
            elif feedback == "_gy__":
                current_state = "EPOXY_4"
            elif feedback == "_ygy_":
                current_state = "WEEPY_4"
            elif feedback == "_yy__":
                current_state = "PEPPY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "APHID_3":
            if feedback == "_____":
                current_state = "SMELL_4"
            elif feedback == "__y__":
                current_state = "SHELL_4"
            elif feedback == "_g___":
                current_state = "SPELL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "APING_3":
            if feedback == "y____":
                current_state = "FECAL_4"
            elif feedback == "y___y":
                current_state = "LEGAL_4"
            elif feedback == "y__y_":
                current_state = "VENAL_4"
            elif feedback == "yy_y_":
                current_state = "PENAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "APIOL_2":
            if feedback == "_____":
                current_state = "REUSE_3"
            elif feedback == "___y_":
                current_state = "ROUSE_3"
            elif feedback == "__g__":
                current_state = "FRISE_3"
            elif feedback == "__y__":
                current_state = "RINSE_3"
            elif feedback == "_y_y_":
                current_state = "PROSE_3"
            elif feedback == "_yg__":
                current_state = "PRISE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "APIOL_3":
            if feedback == "___g_":
                current_state = "STOOD_4"
            elif feedback == "___gg":
                current_state = "STOOL_4"
            elif feedback == "___y_":
                current_state = "STOCK_4"
            elif feedback == "___yy":
                current_state = "SLOTH_4"
            elif feedback == "__yy_":
                current_state = "STOIC_4"
            elif feedback == "_y_g_":
                current_state = "STOOP_4"
            elif feedback == "_y_y_":
                current_state = "STOMP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ARERE_3":
            if feedback == "yyy__":
                current_state = "WAGER_4"
            elif feedback == "yyy_y":
                current_state = "EAGER_4"
            elif feedback == "yyyy_":
                current_state = "RAGER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ARGON_3":
            if feedback == "yggyg":
                current_state = "ORGAN_4"
            elif feedback == "yy_yg":
                current_state = "ROMAN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ARGOT_2":
            if feedback == "gy__g":
                current_state = "APART_3"
            elif feedback == "gy__y":
                current_state = "ALTAR_3"
            elif feedback == "gy_gy":
                current_state = "ACTOR_3"
            elif feedback == "gy_yg":
                current_state = "ABORT_3"
            elif feedback == "yg__g":
                current_state = "CRAFT_3"
            elif feedback == "yg__y":
                current_state = "WRATH_3"
            elif feedback == "ygy_g":
                current_state = "GRAFT_3"
            elif feedback == "yy__g":
                current_state = "CHART_3"
            elif feedback == "yy__y":
                current_state = "ULTRA_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ARISE_2":
            if feedback == "gg_gg":
                current_state = "AROSE_3"
            elif feedback == "yg_gg":
                current_state = "ERASE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ARSON_3":
            if feedback == "yyy__":
                current_state = "SUGAR_4"
            elif feedback == "yyyyy":
                current_state = "SONAR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ARTSY_2":
            if feedback == "yyyg_":
                current_state = "ROAST_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AUDIO_3":
            if feedback == "g_ygy":
                current_state = "AVOID_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AUGUR_4":
            if feedback == "y___g":
                current_state = "FRIAR_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AUMIL_3":
            if feedback == "_____":
                current_state = "GREET_4"
            elif feedback == "___g_":
                current_state = "REFIT_4"
            elif feedback == "___gy":
                current_state = "RELIT_4"
            elif feedback == "___y_":
                current_state = "RIVET_4"
            elif feedback == "__gg_":
                current_state = "REMIT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AUNTY_3":
            if feedback == "yggg_":
                current_state = "JUNTA_4"
            elif feedback == "yyyy_":
                current_state = "UNTAG_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AVIAN_3":
            if feedback == "_yygg":
                current_state = "DIVAN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "AWASH_3":
            if feedback == "__ggg":
                current_state = "GNASH_4"
            elif feedback == "_gggg":
                current_state = "SWASH_4"
            elif feedback == "g_ggg":
                current_state = "ABASH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BACCY_3":
            if feedback == "_____":
                current_state = "FLING_4"
            elif feedback == "____y":
                current_state = "LYING_4"
            elif feedback == "__y__":
                current_state = "CLING_4"
            elif feedback == "g____":
                current_state = "BLING_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BADGE_3":
            if feedback == "_g_gg":
                current_state = "MANGE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BADLY_4":
            if feedback == "_gggg":
                current_state = "MADLY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BAGEL_3":
            if feedback == "_g_gg":
                current_state = "NAVEL_4"
            elif feedback == "_gygg":
                current_state = "GAVEL_4"
            elif feedback == "gg_gg":
                current_state = "BABEL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BAGIE_3":
            if feedback == "_____":
                current_state = "FROWN_4"
            elif feedback == "__y__":
                current_state = "GROWN_4"
            elif feedback == "__yg_":
                current_state = "GROIN_4"
            elif feedback == "g____":
                current_state = "BROWN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BAGUA_3":
            if feedback == "_g___":
                current_state = "PANKO_4"
            elif feedback == "_g__g":
                current_state = "MANIA_4"
            elif feedback == "_g__y":
                current_state = "NAVAL_4"
            elif feedback == "_gg__":
                current_state = "WAGON_4"
            elif feedback == "_gg_y":
                current_state = "PAGAN_4"
            elif feedback == "_gy__":
                current_state = "MANGO_4"
            elif feedback == "_gy_g":
                current_state = "MANGA_4"
            elif feedback == "gg___":
                current_state = "BANJO_4"
            elif feedback == "gg__y":
                current_state = "BANAL_4"
            elif feedback == "yg___":
                current_state = "NABOB_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BALER_3":
            if feedback == "_gygg":
                current_state = "LAYER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BANDY_3":
            if feedback == "_gggg":
                current_state = "DANDY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BASAL_3":
            if feedback == "ggg_g":
                current_state = "BASIL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BASIC_3":
            if feedback == "gggg_":
                current_state = "BASIS_4"
            elif feedback == "ygy__":
                current_state = "SAMBA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BAWDY_4":
            if feedback == "_g_gg":
                current_state = "GAUDY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEACH_3":
            if feedback == "_gg_y":
                current_state = "HEAVY_4"
            elif feedback == "_gggg":
                current_state = "PEACH_4"
            elif feedback == "_gy_y":
                current_state = "HENNA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEADY_3":
            if feedback == "_gggg":
                current_state = "HEADY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BECAP_3":
            if feedback == "_y___":
                current_state = "WHOLE_4"
            elif feedback == "_y__y":
                current_state = "ELOPE_4"
            elif feedback == "_yy__":
                current_state = "CLOVE_4"
            elif feedback == "gy___":
                current_state = "BLOKE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEDEW_3":
            if feedback == "__gg_":
                current_state = "HIDER_4"
            elif feedback == "__ggy":
                current_state = "WIDER_4"
            elif feedback == "__yg_":
                current_state = "FRIED_4"
            elif feedback == "_gg__":
                current_state = "REDID_4"
            elif feedback == "_gy_y":
                current_state = "WEIRD_4"
            elif feedback == "_ygg_":
                current_state = "EIDER_4"
            elif feedback == "ygy__":
                current_state = "REBID_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEFIT_3":
            if feedback == "_g_yy":
                current_state = "VENTI_4"
            elif feedback == "_gyyg":
                current_state = "FEINT_4"
            elif feedback == "_y_gy":
                current_state = "ETHIC_4"
            elif feedback == "_y_yg":
                current_state = "EVICT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEFOG_2":
            if feedback == "_y___":
                current_state = "CARVE_3"
            elif feedback == "_y__y":
                current_state = "LARGE_3"
            elif feedback == "_yy__":
                current_state = "FARCE_3"
            elif feedback == "gy___":
                current_state = "BARRE_3"
            elif feedback == "gy__y":
                current_state = "BARGE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEGAN_3":
            if feedback == "_g_gg":
                current_state = "PECAN_4"
            elif feedback == "_gggg":
                current_state = "VEGAN_4"
            elif feedback == "yg_g_":
                current_state = "KEBAB_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEGAT_3":
            if feedback == "_y_gg":
                current_state = "WHEAT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEGIN_3":
            if feedback == "_gyyg":
                current_state = "FEIGN_4"
            elif feedback == "_gyyy":
                current_state = "NEIGH_4"
            elif feedback == "_yyyy":
                current_state = "EKING_4"
            elif feedback == "ggg_g":
                current_state = "BEGUN_4"
            elif feedback == "ggyyy":
                current_state = "BEING_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEGUN_3":
            if feedback == "_g___":
                current_state = "REEDY_4"
            elif feedback == "_g_g_":
                current_state = "REDUX_4"
            elif feedback == "_y___":
                current_state = "FREED_4"
            elif feedback == "_y_y_":
                current_state = "RUDER_4"
            elif feedback == "_y_yy":
                current_state = "UNDER_4"
            elif feedback == "_yg__":
                current_state = "EDGER_4"
            elif feedback == "_yy__":
                current_state = "GREED_4"
            elif feedback == "gy___":
                current_state = "BREED_4"
            elif feedback == "yg_g_":
                current_state = "REDUB_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEIGE_3":
            if feedback == "__gyg":
                current_state = "GUIDE_4"
            elif feedback == "__ygg":
                current_state = "MIDGE_4"
            elif feedback == "__yyg":
                current_state = "GIMME_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BELCH_2":
            if feedback == "_y___":
                current_state = "PARER_3"
            elif feedback == "_y__y":
                current_state = "HAREM_3"
            elif feedback == "_y_y_":
                current_state = "CARER_3"
            elif feedback == "_yy__":
                current_state = "EARLY_3"
            elif feedback == "gy___":
                current_state = "BARER_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BELLY_3":
            if feedback == "_gggg":
                current_state = "JELLY_4"
            elif feedback == "_gy_g":
                current_state = "LEGGY_4"
            elif feedback == "_yy_g":
                current_state = "ELEGY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEMAD_2":
            if feedback == "_g_g_":
                current_state = "AGLEY_3"
            elif feedback == "_g_gy":
                current_state = "CEDAR_3"
            elif feedback == "_g_y_":
                current_state = "LEARN_3"
            elif feedback == "_g_yg":
                current_state = "HEARD_3"
            elif feedback == "_g_yy":
                current_state = "READY_3"
            elif feedback == "_ggg_":
                current_state = "REMAP_3"
            elif feedback == "_gyy_":
                current_state = "REALM_3"
            elif feedback == "_y_g_":
                current_state = "AFLOW_3"
            elif feedback == "_y_gg":
                current_state = "DREAD_3"
            elif feedback == "_y_y_":
                current_state = "ANGER_3"
            elif feedback == "_y_yy":
                current_state = "ADMIN_3"
            elif feedback == "_ygyg":
                current_state = "ARMED_3"
            elif feedback == "_yyg_":
                current_state = "CREAM_3"
            elif feedback == "_yygy":
                current_state = "DREAM_3"
            elif feedback == "_yyy_":
                current_state = "CREMA_3"
            elif feedback == "gg_yg":
                current_state = "BEARD_3"
            elif feedback == "gy_g_":
                current_state = "BREAK_3"
            elif feedback == "gy_gg":
                current_state = "BREAD_3"
            elif feedback == "gyyg_":
                current_state = "BREAM_3"
            elif feedback == "yg_g_":
                current_state = "REBAR_3"
            elif feedback == "yg_gy":
                current_state = "DEBAR_3"
            elif feedback == "yg_y_":
                current_state = "ZEBRA_3"
            elif feedback == "yyyy_":
                current_state = "AMBER_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BERET_2":
            if feedback == "_gg_g":
                current_state = "MERIT_3"
            elif feedback == "_gg_y":
                current_state = "HERTZ_3"
            elif feedback == "_yggg":
                current_state = "EGRET_3"
            elif feedback == "ggg_y":
                current_state = "BERTH_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEVER_3":
            if feedback == "___gg":
                current_state = "FLYER_4"
            elif feedback == "___gy":
                current_state = "GRUEL_4"
            elif feedback == "_g__g":
                current_state = "LEMUR_4"
            elif feedback == "_g__y":
                current_state = "REPLY_4"
            elif feedback == "_g_gg":
                current_state = "LEPER_4"
            elif feedback == "_g_gy":
                current_state = "REPEL_4"
            elif feedback == "_g_yy":
                current_state = "LEERY_4"
            elif feedback == "_gggg":
                current_state = "LEVER_4"
            elif feedback == "_gggy":
                current_state = "REVEL_4"
            elif feedback == "g__gg":
                current_state = "BLUER_4"
            elif feedback == "yg_gy":
                current_state = "REBEL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BEVUE_3":
            if feedback == "_g__y":
                current_state = "JEWEL_4"
            elif feedback == "_gg_y":
                current_state = "LEVEL_4"
            elif feedback == "_y___":
                current_state = "IMPEL_4"
            elif feedback == "_y__y":
                current_state = "EXCEL_4"
            elif feedback == "_y_y_":
                current_state = "KUGEL_4"
            elif feedback == "_yg__":
                current_state = "HOVEL_4"
            elif feedback == "_yy__":
                current_state = "VOWEL_4"
            elif feedback == "gg__y":
                current_state = "BEZEL_4"
            elif feedback == "ggg_y":
                current_state = "BEVEL_4"
            elif feedback == "gy___":
                current_state = "BOWEL_4"
            elif feedback == "yy___":
                current_state = "LIBEL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BHANG_3":
            if feedback == "_____":
                current_state = "FROZE_4"
            elif feedback == "____y":
                current_state = "GROVE_4"
            elif feedback == "_g___":
                current_state = "CHORE_4"
            elif feedback == "_y___":
                current_state = "OCHRE_4"
            elif feedback == "g____":
                current_state = "BROKE_4"
            elif feedback == "y____":
                current_state = "OMBRE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BIACH_2":
            if feedback == "__g__":
                current_state = "LEASE_3"
            elif feedback == "__g_y":
                current_state = "PHASE_3"
            elif feedback == "__gy_":
                current_state = "CEASE_3"
            elif feedback == "__gyy":
                current_state = "CHASE_3"
            elif feedback == "__y__":
                current_state = "AMUSE_3"
            elif feedback == "_yy__":
                current_state = "ANISE_3"
            elif feedback == "g_g__":
                current_state = "BLASE_3"
            elif feedback == "y_g__":
                current_state = "ABASE_3"
            elif feedback == "y_y__":
                current_state = "ABUSE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BICCY_3":
            if feedback == "_y___":
                current_state = "OWING_4"
            elif feedback == "_y__y":
                current_state = "VYING_4"
            elif feedback == "_yy__":
                current_state = "ICING_4"
            elif feedback == "gy___":
                current_state = "BOING_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BICEP_3":
            if feedback == "__yg_":
                current_state = "CHEEK_4"
            elif feedback == "__ygg":
                current_state = "CHEEP_4"
            elif feedback == "_yyg_":
                current_state = "CHIEF_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BIFFY_2":
            if feedback == "_____":
                current_state = "NORTH_3"
            elif feedback == "__y__":
                current_state = "FORTH_3"
            elif feedback == "__y_g":
                current_state = "FORTY_3"
            elif feedback == "_g___":
                current_state = "GIRTH_3"
            elif feedback == "_g__g":
                current_state = "DIRTY_3"
            elif feedback == "_gy__":
                current_state = "FIRTH_3"
            elif feedback == "g____":
                current_state = "BURNT_3"
            elif feedback == "gg___":
                current_state = "BIRTH_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BIGLY_3":
            if feedback == "_____":
                current_state = "HUTCH_4"
            elif feedback == "____g":
                current_state = "PUTTY_4"
            elif feedback == "___y_":
                current_state = "KLUTZ_4"
            elif feedback == "__y_g":
                current_state = "GUTTY_4"
            elif feedback == "g____":
                current_state = "BUTCH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BIKER_4":
            if feedback == "_gggg":
                current_state = "HIKER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BINGE_3":
            if feedback == "_gggg":
                current_state = "HINGE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BINGO_3":
            if feedback == "_g_g_":
                current_state = "PIGGY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BIOME_3":
            if feedback == "_gg_g":
                current_state = "DIODE_4"
            elif feedback == "_yy_g":
                current_state = "OXIDE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BIONT_2":
            if feedback == "____g":
                current_state = "CRYPT_3"
            elif feedback == "___gg":
                current_state = "GRUNT_3"
            elif feedback == "__g_g":
                current_state = "GROUT_3"
            elif feedback == "__g_y":
                current_state = "FROTH_3"
            elif feedback == "__ggg":
                current_state = "FRONT_3"
            elif feedback == "__y_g":
                current_state = "COURT_3"
            elif feedback == "__y_y":
                current_state = "MOTOR_3"
            elif feedback == "_g__g":
                current_state = "RIGHT_3"
            elif feedback == "_g__y":
                current_state = "RITZY_3"
            elif feedback == "_gy_y":
                current_state = "VITRO_3"
            elif feedback == "_gyyy":
                current_state = "NITRO_3"
            elif feedback == "_y__g":
                current_state = "DRIFT_3"
            elif feedback == "_y__y":
                current_state = "FRITZ_3"
            elif feedback == "_y_gg":
                current_state = "PRINT_3"
            elif feedback == "_yg_g":
                current_state = "DROIT_3"
            elif feedback == "_yyyy":
                current_state = "INTRO_3"
            elif feedback == "g___g":
                current_state = "BLURT_3"
            elif feedback == "g__gg":
                current_state = "BRUNT_3"
            elif feedback == "g_g_y":
                current_state = "BROTH_3"
            elif feedback == "y_y_g":
                current_state = "ROBOT_3"
            elif feedback == "yyy_g":
                current_state = "ORBIT_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BIOTA_2":
            if feedback == "___y_":
                current_state = "METRE_3"
            elif feedback == "__gg_":
                current_state = "WROTE_3"
            elif feedback == "__yg_":
                current_state = "ROUTE_3"
            elif feedback == "__yy_":
                current_state = "OUTRE_3"
            elif feedback == "_g_y_":
                current_state = "LITRE_3"
            elif feedback == "_y_g_":
                current_state = "WRITE_3"
            elif feedback == "_y_y_":
                current_state = "RETIE_3"
            elif feedback == "g__g_":
                current_state = "BRUTE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BIPOD_3":
            if feedback == "_g__g":
                current_state = "VIVID_4"
            elif feedback == "_y_yg":
                current_state = "OVOID_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BISON_3":
            if feedback == "__y_y":
                current_state = "SYNCH_4"
            elif feedback == "__ygg":
                current_state = "SWOON_4"
            elif feedback == "__ygy":
                current_state = "SYNOD_4"
            elif feedback == "__yyg":
                current_state = "SHOWN_4"
            elif feedback == "__yyy":
                current_state = "SNOWY_4"
            elif feedback == "_yy_y":
                current_state = "SNIFF_4"
            elif feedback == "_yygg":
                current_state = "SCION_4"
            elif feedback == "_yyyy":
                current_state = "SONIC_4"
            elif feedback == "g_ggg":
                current_state = "BOSON_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BITER_4":
            if feedback == "_gggg":
                current_state = "LITER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BITTY_4":
            if feedback == "_gggg":
                current_state = "KITTY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BLACK_3":
            if feedback == "_gggg":
                current_state = "FLACK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BLADE_3":
            if feedback == "_gggg":
                current_state = "CLADE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BLARE_3":
            if feedback == "__ggg":
                current_state = "AWARE_4"
            elif feedback == "_gggg":
                current_state = "FLARE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BLEEP_3":
            if feedback == "_y_g_":
                current_state = "GOLEM_4"
            elif feedback == "_y_gg":
                current_state = "JULEP_4"
            elif feedback == "yyyg_":
                current_state = "CELEB_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BLIMP_3":
            if feedback == "_____":
                current_state = "HONEY_4"
            elif feedback == "___y_":
                current_state = "MONEY_4"
            elif feedback == "__y__":
                current_state = "WINEY_4"
            elif feedback == "__y_y":
                current_state = "PINEY_4"
            elif feedback == "g____":
                current_state = "BONEY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BLINK_4":
            if feedback == "_gggg":
                current_state = "PLINK_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BLITZ_4":
            if feedback == "_gggg":
                current_state = "GLITZ_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BLOCK_4":
            if feedback == "ggg__":
                current_state = "BLOWN_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BLOND_2":
            if feedback == "_____":
                current_state = "CHARM_3"
            elif feedback == "____g":
                current_state = "AARGH_3"
            elif feedback == "____y":
                current_state = "DIARY_3"
            elif feedback == "___g_":
                current_state = "FRANC_3"
            elif feedback == "___gg":
                current_state = "GRAND_3"
            elif feedback == "___gy":
                current_state = "DRANK_3"
            elif feedback == "___y_":
                current_state = "ANGRY_3"
            elif feedback == "___yy":
                current_state = "DRAIN_3"
            elif feedback == "__g__":
                current_state = "AGORA_3"
            elif feedback == "__gy_":
                current_state = "ACORN_3"
            elif feedback == "__gyy":
                current_state = "ADORN_3"
            elif feedback == "__y__":
                current_state = "HOARY_3"
            elif feedback == "__y_g":
                current_state = "HOARD_3"
            elif feedback == "__y_y":
                current_state = "ARDOR_3"
            elif feedback == "__yy_":
                current_state = "ARGON_3"
            elif feedback == "_g___":
                current_state = "ALARM_3"
            elif feedback == "_g_y_":
                current_state = "ULNAR_3"
            elif feedback == "_gg__":
                current_state = "FLORA_3"
            elif feedback == "_y___":
                current_state = "FRAIL_3"
            elif feedback == "_y__y":
                current_state = "DRAWL_3"
            elif feedback == "_y_y_":
                current_state = "GNARL_3"
            elif feedback == "_yy__":
                current_state = "MOLAR_3"
            elif feedback == "g____":
                current_state = "BRAVA_3"
            elif feedback == "g___g":
                current_state = "BRAID_3"
            elif feedback == "g__gg":
                current_state = "BRAND_3"
            elif feedback == "g__y_":
                current_state = "BRAIN_3"
            elif feedback == "g_g_g":
                current_state = "BROAD_3"
            elif feedback == "g_y__":
                current_state = "BRAVO_3"
            elif feedback == "g_y_g":
                current_state = "BOARD_3"
            elif feedback == "gy___":
                current_state = "BRAWL_3"
            elif feedback == "y____":
                current_state = "RUMBA_3"
            elif feedback == "y__y_":
                current_state = "URBAN_3"
            elif feedback == "y_y__":
                current_state = "ABHOR_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BLOND_3":
            if feedback == "_gg_g":
                current_state = "FLOOD_4"
            elif feedback == "ggg_g":
                current_state = "BLOOD_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BLUFF_4":
            if feedback == "_gggg":
                current_state = "FLUFF_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BLUNT_3":
            if feedback == "__yyg":
                current_state = "UNFIT_4"
            elif feedback == "_yyyg":
                current_state = "UNLIT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOAST_2":
            if feedback == "__ggg":
                current_state = "AVAST_3"
            elif feedback == "__ggy":
                current_state = "STASH_3"
            elif feedback == "__ygg":
                current_state = "ANGST_3"
            elif feedback == "__ygy":
                current_state = "ANTSY_3"
            elif feedback == "_gggg":
                current_state = "COAST_3"
            elif feedback == "g_ggg":
                current_state = "BLAST_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOBBY_4":
            if feedback == "_g__g":
                current_state = "COCKY_5"
            elif feedback == "gg___":
                current_state = "BOFFO_5"
            elif feedback == "gg__g":
                current_state = "BONNY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOCCE_3":
            if feedback == "_gy_g":
                current_state = "COUPE_4"
            elif feedback == "gg__g":
                current_state = "BOOZE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOGEY_4":
            if feedback == "_g_gg":
                current_state = "JOKEY_5"
            elif feedback == "_gggg":
                current_state = "FOGEY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOGGY_3":
            if feedback == "__g_g":
                current_state = "PYGMY_4"
            elif feedback == "_gggg":
                current_state = "FOGGY_4"
            elif feedback == "gg_g_":
                current_state = "BONGO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOGUE_2":
            if feedback == "_____":
                current_state = "WRIST_3"
            elif feedback == "___y_":
                current_state = "CRUST_3"
            elif feedback == "__y__":
                current_state = "GRIST_3"
            elif feedback == "_g___":
                current_state = "ROOST_3"
            elif feedback == "_g_y_":
                current_state = "ROUST_3"
            elif feedback == "_y___":
                current_state = "FROST_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOLUS_3":
            if feedback == "__gyy":
                current_state = "SULLY_4"
            elif feedback == "_gygg":
                current_state = "LOCUS_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOOBY_4":
            if feedback == "__g__":
                current_state = "KNOCK_5"
            elif feedback == "_gg_g":
                current_state = "KOOKY_5"
            elif feedback == "ggg_g":
                current_state = "BOOZY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOOFY_3":
            if feedback == "_____":
                current_state = "DATUM_4"
            elif feedback == "____g":
                current_state = "NATTY_4"
            elif feedback == "___y_":
                current_state = "FATWA_4"
            elif feedback == "___yg":
                current_state = "FATTY_4"
            elif feedback == "_y___":
                current_state = "MATZO_4"
            elif feedback == "g___g":
                current_state = "BATTY_4"
            elif feedback == "gy___":
                current_state = "BATON_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BORED_3":
            if feedback == "_ggg_":
                current_state = "MOREL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BORIC_3":
            if feedback == "_gg_y":
                current_state = "PORCH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOUGH_3":
            if feedback == "_gggg":
                current_state = "COUGH_4"
            elif feedback == "_ggy_":
                current_state = "YOUNG_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOULE_3":
            if feedback == "_gggg":
                current_state = "JOULE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOWER_4":
            if feedback == "_gggg":
                current_state = "ROWER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BOXER_5":
            if feedback == "_g_gg":
                current_state = "ROVER_6"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BRAIN_3":
            if feedback == "ggg_g":
                current_state = "BRAWN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BRAVA_3":
            if feedback == "ggy__":
                current_state = "BRIAR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BRICK_3":
            if feedback == "_ggg_":
                current_state = "PRICY_4"
            elif feedback == "_gggg":
                current_state = "PRICK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BRIDE_3":
            if feedback == "_ggyg":
                current_state = "DRIVE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BRIEF_4":
            if feedback == "_gggg":
                current_state = "GRIEF_5"
            elif feedback == "_yyy_":
                current_state = "REMIX_5"
            elif feedback == "gggg_":
                current_state = "BRIER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BRINE_3":
            if feedback == "_gggg":
                current_state = "URINE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BROOM_3":
            if feedback == "_ggg_":
                current_state = "PROOF_4"
            elif feedback == "_gggg":
                current_state = "GROOM_4"
            elif feedback == "_ygg_":
                current_state = "FLOOR_4"
            elif feedback == "gggg_":
                current_state = "BROOK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BUCHU_2":
            if feedback == "_____":
                current_state = "PASTE_3"
            elif feedback == "___y_":
                current_state = "HASTE_3"
            elif feedback == "__y__":
                current_state = "CASTE_3"
            elif feedback == "_y___":
                current_state = "SAUTE_3"
            elif feedback == "g____":
                current_state = "BASTE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BUGGY_3":
            if feedback == "__y__":
                current_state = "WRING_4"
            elif feedback == "_g___":
                current_state = "RUNUP_4"
            elif feedback == "_g__g":
                current_state = "RUNNY_4"
            elif feedback == "_gy__":
                current_state = "RUING_4"
            elif feedback == "_yy__":
                current_state = "WRUNG_4"
            elif feedback == "g____":
                current_state = "BRINK_4"
            elif feedback == "g___g":
                current_state = "BRINY_4"
            elif feedback == "g_y__":
                current_state = "BRING_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BUILD_2":
            if feedback == "_____":
                current_state = "EMOTE_3"
            elif feedback == "__g__":
                current_state = "WHITE_3"
            elif feedback == "__gy_":
                current_state = "ELITE_3"
            elif feedback == "__yy_":
                current_state = "LITHE_3"
            elif feedback == "_g___":
                current_state = "QUOTE_3"
            elif feedback == "_gg__":
                current_state = "QUITE_3"
            elif feedback == "_gy__":
                current_state = "CUTIE_3"
            elif feedback == "_y___":
                current_state = "CHUTE_3"
            elif feedback == "_y__y":
                current_state = "ETUDE_3"
            elif feedback == "_y_y_":
                current_state = "FLUTE_3"
            elif feedback == "_yg__":
                current_state = "UNITE_3"
            elif feedback == "_ygg_":
                current_state = "UTILE_3"
            elif feedback == "_yy__":
                current_state = "UNTIE_3"
            elif feedback == "gg___":
                current_state = "BUTTE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BULKY_3":
            if feedback == "_gg__":
                current_state = "MULCH_4"
            elif feedback == "_gg_g":
                current_state = "PULPY_4"
            elif feedback == "_gggg":
                current_state = "HULKY_4"
            elif feedback == "_gy__":
                current_state = "LUNCH_4"
            elif feedback == "_gy_g":
                current_state = "LUMPY_4"
            elif feedback == "_gygg":
                current_state = "LUCKY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BULLY_3":
            if feedback == "_gggg":
                current_state = "FULLY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BUMPH_3":
            if feedback == "_____":
                current_state = "WEDGE_4"
            elif feedback == "____y":
                current_state = "HEDGE_4"
            elif feedback == "_g___":
                current_state = "FUDGE_4"
            elif feedback == "_g__g":
                current_state = "HUNCH_4"
            elif feedback == "_g__y":
                current_state = "HUFFY_4"
            elif feedback == "_g_g_":
                current_state = "PUPPY_4"
            elif feedback == "_g_y_":
                current_state = "PUDGE_4"
            elif feedback == "_g_yg":
                current_state = "PUNCH_4"
            elif feedback == "_gg__":
                current_state = "MUMMY_4"
            elif feedback == "_ggg_":
                current_state = "JUMPY_4"
            elif feedback == "_gggg":
                current_state = "HUMPH_4"
            elif feedback == "_gy__":
                current_state = "MUCKY_4"
            elif feedback == "_gy_g":
                current_state = "MUNCH_4"
            elif feedback == "_y___":
                current_state = "FOUND_4"
            elif feedback == "_y__y":
                current_state = "HOUND_4"
            elif feedback == "_y_y_":
                current_state = "POUND_4"
            elif feedback == "_yy__":
                current_state = "MOUND_4"
            elif feedback == "gg___":
                current_state = "BUDGE_4"
            elif feedback == "gg__g":
                current_state = "BUNCH_4"
            elif feedback == "gggg_":
                current_state = "BUMPY_4"
            elif feedback == "ggy__":
                current_state = "BUXOM_4"
            elif feedback == "gy___":
                current_state = "BOUND_4"
            elif feedback == "yg___":
                current_state = "CUBBY_4"
            elif feedback == "yg__y":
                current_state = "HUBBY_4"
            elif feedback == "ygg__":
                current_state = "JUMBO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BUNNY_4":
            if feedback == "gg__g":
                current_state = "BUZZY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BURLY_3":
            if feedback == "__ggg":
                current_state = "GIRLY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "BURRO_3":
            if feedback == "__g_g":
                current_state = "FORGO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CABAL_3":
            if feedback == "gg__g":
                current_state = "CAVIL_4"
            elif feedback == "gg__y":
                current_state = "CAULK_4"
            elif feedback == "gg_g_":
                current_state = "CACAO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CABBY_3":
            if feedback == "gg__g":
                current_state = "CAMPY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CADRE_2":
            if feedback == "_g_yg":
                current_state = "RANGE_3"
            elif feedback == "_gggg":
                current_state = "PADRE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CAMEO_3":
            if feedback == "_ggg_":
                current_state = "FAMED_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CANON_3":
            if feedback == "gg__g":
                current_state = "CABIN_4"
            elif feedback == "gg_gg":
                current_state = "CAPON_4"
            elif feedback == "ggg__":
                current_state = "CANAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CAPHS_3":
            if feedback == "____y":
                current_state = "STOUT_4"
            elif feedback == "___yy":
                current_state = "SHOUT_4"
            elif feedback == "__y_y":
                current_state = "SPOUT_4"
            elif feedback == "y___y":
                current_state = "SCOUT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CAPIZ_3":
            if feedback == "_y___":
                current_state = "GRAVE_4"
            elif feedback == "_y__y":
                current_state = "GRAZE_4"
            elif feedback == "_yy__":
                current_state = "GRAPE_4"
            elif feedback == "yy___":
                current_state = "GRACE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CAPRI_3":
            if feedback == "_g_yy":
                current_state = "FAKIR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CARET_2":
            if feedback == "_ggyy":
                current_state = "EARTH_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CARNY_3":
            if feedback == "ggg_g":
                current_state = "CARRY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CARVY_3":
            if feedback == "_gy__":
                current_state = "PAPER_4"
            elif feedback == "_gy_y":
                current_state = "PAYER_4"
            elif feedback == "_gyy_":
                current_state = "PAVER_4"
            elif feedback == "ggy__":
                current_state = "CAPER_4"
            elif feedback == "ygy__":
                current_state = "PACER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CATCH_3":
            if feedback == "ggg__":
                current_state = "CATTY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHAFF_3":
            if feedback == "ggg__":
                current_state = "CHAMP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHALK_2":
            if feedback == "__g__":
                current_state = "SPADE_3"
            elif feedback == "__g_y":
                current_state = "SNAKE_3"
            elif feedback == "__gg_":
                current_state = "SWALE_3"
            elif feedback == "__gyy":
                current_state = "SLAKE_3"
            elif feedback == "__y__":
                current_state = "ASIDE_3"
            elif feedback == "__yg_":
                current_state = "AISLE_3"
            elif feedback == "_gg__":
                current_state = "AMPED_3"
            elif feedback == "_gg_y":
                current_state = "SHAKE_3"
            elif feedback == "_ggg_":
                current_state = "SHALE_3"
            elif feedback == "y_g__":
                current_state = "SCAPE_3"
            elif feedback == "y_gg_":
                current_state = "SCALE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHALK_3":
            if feedback == "g_gy_":
                current_state = "CLAMP_4"
            elif feedback == "g_gyg":
                current_state = "CLACK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHANT_3":
            if feedback == "__ggg":
                current_state = "QUANT_4"
            elif feedback == "y_y_g":
                current_state = "DUCAT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHAOS_3":
            if feedback == "y_g_y":
                current_state = "SMACK_4"
            elif feedback == "ygg_y":
                current_state = "SHACK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHARM_3":
            if feedback == "__gg_":
                current_state = "QUARK_4"
            elif feedback == "__gy_":
                current_state = "GRAVY_4"
            elif feedback == "__yy_":
                current_state = "AUGUR_4"
            elif feedback == "__yyy":
                current_state = "PRIMA_4"
            elif feedback == "_ggg_":
                current_state = "WHARF_4"
            elif feedback == "_ygy_":
                current_state = "GRAPH_4"
            elif feedback == "g_gy_":
                current_state = "CRACK_4"
            elif feedback == "g_gyy":
                current_state = "CRAMP_4"
            elif feedback == "g_yy_":
                current_state = "CIGAR_4"
            elif feedback == "gggg_":
                current_state = "CHARY_4"
            elif feedback == "gggy_":
                current_state = "CHAIR_4"
            elif feedback == "y_gy_":
                current_state = "FRACK_4"
            elif feedback == "y_yy_":
                current_state = "VICAR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHART_3":
            if feedback == "__ggg":
                current_state = "QUART_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHAWL_2":
            if feedback == "__y__":
                current_state = "ADEEM_3"
            elif feedback == "__y_y":
                current_state = "LATER_3"
            elif feedback == "__yy_":
                current_state = "WATER_3"
            elif feedback == "_yy__":
                current_state = "HATER_3"
            elif feedback == "g_y__":
                current_state = "CATER_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHEAP_3":
            if feedback == "y_gg_":
                current_state = "OCEAN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHEEK_3":
            if feedback == "___g_":
                current_state = "INSET_4"
            elif feedback == "__g__":
                current_state = "STENT_4"
            elif feedback == "__gg_":
                current_state = "SWEET_4"
            elif feedback == "__ggy":
                current_state = "SKEET_4"
            elif feedback == "__yg_":
                current_state = "BESET_4"
            elif feedback == "_ggg_":
                current_state = "SHEET_4"
            elif feedback == "y_g__":
                current_state = "SCENT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHEEP_3":
            if feedback == "__y__":
                current_state = "UNDUE_4"
            elif feedback == "__yy_":
                current_state = "VENUE_4"
            elif feedback == "__yyy":
                current_state = "PENNE_4"
            elif feedback == "y_y__":
                current_state = "DUNCE_4"
            elif feedback == "y_yy_":
                current_state = "FENCE_4"
            elif feedback == "y_yyy":
                current_state = "PENCE_4"
            elif feedback == "yyyy_":
                current_state = "HENCE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHILD_2":
            if feedback == "_____":
                current_state = "TEPEE_3"
            elif feedback == "___g_":
                current_state = "TULLE_3"
            elif feedback == "__g__":
                current_state = "TWINE_3"
            elif feedback == "__y__":
                current_state = "TINGE_3"
            elif feedback == "__yg_":
                current_state = "TITLE_3"
            elif feedback == "__yyy":
                current_state = "TILDE_3"
            elif feedback == "_g___":
                current_state = "THEME_3"
            elif feedback == "_gg__":
                current_state = "THINE_3"
            elif feedback == "_yy__":
                current_state = "TITHE_3"
            elif feedback == "y_g__":
                current_state = "TWICE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHILE_3":
            if feedback == "__ggg":
                current_state = "EXILE_4"
            elif feedback == "__gyg":
                current_state = "ELIDE_4"
            elif feedback == "__ygg":
                current_state = "BIBLE_4"
            elif feedback == "_gggg":
                current_state = "WHILE_4"
            elif feedback == "g_gyg":
                current_state = "CLIME_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHILI_3":
            if feedback == "gggg_":
                current_state = "CHILL_4"
            elif feedback == "y_ggy":
                current_state = "ICILY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHIMB_2":
            if feedback == "_____":
                current_state = "DROSS_3"
            elif feedback == "____y":
                current_state = "BRUSK_3"
            elif feedback == "__g__":
                current_state = "FRISK_3"
            elif feedback == "__g_y":
                current_state = "BRISK_3"
            elif feedback == "__gy_":
                current_state = "PRISM_3"
            elif feedback == "_y___":
                current_state = "FROSH_3"
            elif feedback == "_y__y":
                current_state = "BRUSH_3"
            elif feedback == "g____":
                current_state = "CROSS_3"
            elif feedback == "g_g__":
                current_state = "CRISP_3"
            elif feedback == "gy___":
                current_state = "CRUSH_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHIMB_3":
            if feedback == "_____":
                current_state = "FLAKE_4"
            elif feedback == "____y":
                current_state = "BLAZE_4"
            elif feedback == "___g_":
                current_state = "FLAME_4"
            elif feedback == "___gy":
                current_state = "BLAME_4"
            elif feedback == "___y_":
                current_state = "MODUS_4"
            elif feedback == "_y___":
                current_state = "GUSHY_4"
            elif feedback == "_y__y":
                current_state = "BUSHY_4"
            elif feedback == "_y_y_":
                current_state = "HUMUS_4"
            elif feedback == "_yy__":
                current_state = "SUSHI_4"
            elif feedback == "g____":
                current_state = "CLAVE_4"
            elif feedback == "gy___":
                current_state = "CUSHY_4"
            elif feedback == "y____":
                current_state = "PLACE_4"
            elif feedback == "y__y_":
                current_state = "MUCUS_4"
            elif feedback == "y_y__":
                current_state = "FICUS_4"
            elif feedback == "y_yy_":
                current_state = "MUSIC_4"
            elif feedback == "yy___":
                current_state = "HOCUS_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHIRP_3":
            if feedback == "g__y_":
                current_state = "CRUMB_4"
            elif feedback == "g__yg":
                current_state = "CRUMP_4"
            elif feedback == "g_gy_":
                current_state = "CRICK_4"
            elif feedback == "g_gyg":
                current_state = "CRIMP_4"
            elif feedback == "gg_g_":
                current_state = "CHURL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHOKE_3":
            if feedback == "__ggg":
                current_state = "EVOKE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHOMP_3":
            if feedback == "__g__":
                current_state = "GOOEY_4"
            elif feedback == "__y__":
                current_state = "BOGEY_4"
            elif feedback == "__y_y":
                current_state = "POKEY_4"
            elif feedback == "__yyy":
                current_state = "MOPEY_4"
            elif feedback == "_yg__":
                current_state = "HOOEY_4"
            elif feedback == "_yy__":
                current_state = "HOKEY_4"
            elif feedback == "_yyy_":
                current_state = "HOMEY_4"
            elif feedback == "g_y__":
                current_state = "COVEY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHORD_3":
            if feedback == "g_gyg":
                current_state = "CROWD_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CHYND_2":
            if feedback == "_____":
                current_state = "MAMBA_3"
            elif feedback == "____g":
                current_state = "VALID_3"
            elif feedback == "____y":
                current_state = "MADAM_3"
            elif feedback == "___g_":
                current_state = "FAUNA_3"
            elif feedback == "___y_":
                current_state = "BAGUA_3"
            elif feedback == "___yy":
                current_state = "PANDA_3"
            elif feedback == "__g__":
                current_state = "LAYUP_3"
            elif feedback == "__y__":
                current_state = "GLUME_3"
            elif feedback == "__y_y":
                current_state = "DALED_3"
            elif feedback == "__yg_":
                current_state = "NANNY_3"
            elif feedback == "__yy_":
                current_state = "MANLY_3"
            elif feedback == "__yyy":
                current_state = "BANDY_3"
            elif feedback == "_y___":
                current_state = "HAIKU_3"
            elif feedback == "_yy__":
                current_state = "HAMMY_3"
            elif feedback == "_yyy_":
                current_state = "HANKY_3"
            elif feedback == "_yyyy":
                current_state = "HANDY_3"
            elif feedback == "g____":
                current_state = "CABAL_3"
            elif feedback == "g__y_":
                current_state = "CANON_3"
            elif feedback == "g_y__":
                current_state = "CABBY_3"
            elif feedback == "g_y_y":
                current_state = "CADDY_3"
            elif feedback == "g_yg_":
                current_state = "CANNY_3"
            elif feedback == "g_yyy":
                current_state = "CANDY_3"
            elif feedback == "y____":
                current_state = "MAGIC_3"
            elif feedback == "y__y_":
                current_state = "MANIC_3"
            elif feedback == "y_y__":
                current_state = "WACKY_3"
            elif feedback == "y_yy_":
                current_state = "FANCY_3"
            elif feedback == "yy___":
                current_state = "HAVOC_3"
            elif feedback == "yy__y":
                current_state = "DACHA_3"
            elif feedback == "yy_y_":
                current_state = "NACHO_3"
            elif feedback == "yyy__":
                current_state = "HACKY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CIDER_2":
            if feedback == "___gg":
                current_state = "SURER_3"
            elif feedback == "___gy":
                current_state = "SHREW_3"
            elif feedback == "___yy":
                current_state = "SERUM_3"
            elif feedback == "__ygy":
                current_state = "SHRED_3"
            elif feedback == "_g_gy":
                current_state = "SIREN_3"
            elif feedback == "_y_yy":
                current_state = "SERIF_3"
            elif feedback == "y__gy":
                current_state = "SCREW_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CIDER_3":
            if feedback == "gyygy":
                current_state = "CRIED_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLAMP_2":
            if feedback == "__g__":
                current_state = "SHARK_3"
            elif feedback == "__g_g":
                current_state = "SHARP_3"
            elif feedback == "__g_y":
                current_state = "SPARK_3"
            elif feedback == "__gy_":
                current_state = "SMARM_3"
            elif feedback == "__y__":
                current_state = "ARSON_3"
            elif feedback == "_yg__":
                current_state = "SNARL_3"
            elif feedback == "_yy__":
                current_state = "SOLAR_3"
            elif feedback == "y_g__":
                current_state = "SCARF_3"
            elif feedback == "y_g_g":
                current_state = "SCARP_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLANG_3":
            if feedback == "gggg_":
                current_state = "CLANK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLAPT_2":
            if feedback == "__g_g":
                current_state = "SHAFT_3"
            elif feedback == "__g_y":
                current_state = "STAND_3"
            elif feedback == "__ggy":
                current_state = "STAPH_3"
            elif feedback == "__gyy":
                current_state = "STAMP_3"
            elif feedback == "__y_g":
                current_state = "SQUAT_3"
            elif feedback == "__y_y":
                current_state = "STOMA_3"
            elif feedback == "_gg_g":
                current_state = "SLANT_3"
            elif feedback == "_yg_g":
                current_state = "SHALT_3"
            elif feedback == "_yg_y":
                current_state = "STALK_3"
            elif feedback == "_yy_y":
                current_state = "ATLAS_3"
            elif feedback == "_yyyg":
                current_state = "SPLAT_3"
            elif feedback == "y_g_g":
                current_state = "SCANT_3"
            elif feedback == "y_g_y":
                current_state = "STACK_3"
            elif feedback == "y_y_g":
                current_state = "ASCOT_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLASP_3":
            if feedback == "gggg_":
                current_state = "CLASS_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLEAN_3":
            if feedback == "_ggg_":
                current_state = "BLEAK_4"
            elif feedback == "_gggg":
                current_state = "GLEAN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLERK_3":
            if feedback == "gyyy_":
                current_state = "CRUEL_4"
            elif feedback == "ygyy_":
                current_state = "ULCER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLINT_2":
            if feedback == "____y":
                current_state = "TRAMP_3"
            elif feedback == "__g_y":
                current_state = "TRIAD_3"
            elif feedback == "__y_g":
                current_state = "TRAIT_3"
            elif feedback == "__y_y":
                current_state = "TIARA_3"
            elif feedback == "__yyy":
                current_state = "TRAIN_3"
            elif feedback == "_y__y":
                current_state = "TRAWL_3"
            elif feedback == "_yg_y":
                current_state = "TRIAL_3"
            elif feedback == "_yy_y":
                current_state = "TRAIL_3"
            elif feedback == "y___g":
                current_state = "TRACT_3"
            elif feedback == "y___y":
                current_state = "TRACK_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLIPT_2":
            if feedback == "____g":
                current_state = "DOUGH_3"
            elif feedback == "____y":
                current_state = "BOOFY_3"
            elif feedback == "___yg":
                current_state = "KAPUT_3"
            elif feedback == "___yy":
                current_state = "PANTY_3"
            elif feedback == "__g_g":
                current_state = "FAINT_3"
            elif feedback == "__g_y":
                current_state = "FAITH_3"
            elif feedback == "__gyg":
                current_state = "PAINT_3"
            elif feedback == "__y_g":
                current_state = "HABIT_3"
            elif feedback == "__y_y":
                current_state = "BATIK_3"
            elif feedback == "__yyy":
                current_state = "PATIO_3"
            elif feedback == "_y__g":
                current_state = "FAULT_3"
            elif feedback == "_y__y":
                current_state = "AFOAM_3"
            elif feedback == "_yg_y":
                current_state = "LAITY_3"
            elif feedback == "g___y":
                current_state = "CATCH_3"
            elif feedback == "g__yg":
                current_state = "CAPUT_3"
            elif feedback == "g_y_y":
                current_state = "CACTI_3"
            elif feedback == "y___g":
                current_state = "YACHT_3"
            elif feedback == "y___y":
                current_state = "EMBOW_3"
            elif feedback == "y__yy":
                current_state = "PATCH_3"
            elif feedback == "yy__y":
                current_state = "LATCH_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLOCK_4":
            if feedback == "_gg__":
                current_state = "FLOWN_5"
            elif feedback == "_gggg":
                current_state = "FLOCK_5"
            elif feedback == "ggg__":
                current_state = "CLOWN_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLONK_2":
            if feedback == "_____":
                current_state = "USURP_3"
            elif feedback == "____g":
                current_state = "SHIRK_3"
            elif feedback == "____y":
                current_state = "RISKY_3"
            elif feedback == "___y_":
                current_state = "SPURN_3"
            elif feedback == "__g__":
                current_state = "SWORD_3"
            elif feedback == "__g_g":
                current_state = "SPORK_3"
            elif feedback == "__gy_":
                current_state = "SHORN_3"
            elif feedback == "__y__":
                current_state = "VISOR_3"
            elif feedback == "__yy_":
                current_state = "ROSIN_3"
            elif feedback == "_g___":
                current_state = "SLURP_3"
            elif feedback == "_y___":
                current_state = "SWIRL_3"
            elif feedback == "y_g__":
                current_state = "SCOUR_3"
            elif feedback == "y_gy_":
                current_state = "SCORN_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLOTH_2":
            if feedback == "___g_":
                current_state = "MATTE_3"
            elif feedback == "___gy":
                current_state = "HAUTE_3"
            elif feedback == "___yy":
                current_state = "BATHE_3"
            elif feedback == "_y_g_":
                current_state = "LATTE_3"
            elif feedback == "_y_y_":
                current_state = "LATKE_3"
            elif feedback == "_y_yy":
                current_state = "LATHE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLOTH_3":
            if feedback == "__ggy":
                current_state = "PHOTO_4"
            elif feedback == "y_yy_":
                current_state = "OPTIC_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLOUD_2":
            if feedback == "_____":
                current_state = "GEESE_3"
            elif feedback == "____y":
                current_state = "DENSE_3"
            elif feedback == "___y_":
                current_state = "GUISE_3"
            elif feedback == "__g__":
                current_state = "AHING_3"
            elif feedback == "__y__":
                current_state = "NOISE_3"
            elif feedback == "__y_y":
                current_state = "DOWSE_3"
            elif feedback == "__yy_":
                current_state = "HOUSE_3"
            elif feedback == "__yyy":
                current_state = "DOUSE_3"
            elif feedback == "_y_y_":
                current_state = "PULSE_3"
            elif feedback == "_yg__":
                current_state = "LOOSE_3"
            elif feedback == "_yyy_":
                current_state = "LOUSE_3"
            elif feedback == "g_g__":
                current_state = "CHOSE_3"
            elif feedback == "g_y__":
                current_state = "COPSE_3"
            elif feedback == "ggg__":
                current_state = "CLOSE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLOUT_3":
            if feedback == "_gggg":
                current_state = "FLOUT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CLUNG_3":
            if feedback == "_gggg":
                current_state = "FLUNG_4"
            elif feedback == "_yy_y":
                current_state = "MOGUL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COCOA_3":
            if feedback == "gg__g":
                current_state = "COMMA_4"
            elif feedback == "gg__y":
                current_state = "COPAY_4"
            elif feedback == "ggy_y":
                current_state = "COACH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CODON_2":
            if feedback == "_____":
                current_state = "FUGLY_3"
            elif feedback == "____g":
                current_state = "BRUIN_3"
            elif feedback == "____y":
                current_state = "BUGGY_3"
            elif feedback == "___g_":
                current_state = "PRIOR_3"
            elif feedback == "___gg":
                current_state = "PRION_3"
            elif feedback == "___gy":
                current_state = "MINOR_3"
            elif feedback == "__g__":
                current_state = "RUDDY_3"
            elif feedback == "__y__":
                current_state = "DRILL_3"
            elif feedback == "__y_y":
                current_state = "DRINK_3"
            elif feedback == "_g___":
                current_state = "ROUGH_3"
            elif feedback == "_g__g":
                current_state = "MOURN_3"
            elif feedback == "_g_gy":
                current_state = "HONOR_3"
            elif feedback == "_g_y_":
                current_state = "ROOMY_3"
            elif feedback == "_gy__":
                current_state = "DOWRY_3"
            elif feedback == "_gy_y":
                current_state = "ROUND_3"
            elif feedback == "_gygy":
                current_state = "DONOR_3"
            elif feedback == "_y___":
                current_state = "GROWL_3"
            elif feedback == "_y__g":
                current_state = "BAGIE_3"
            elif feedback == "_y__y":
                current_state = "PRONG_3"
            elif feedback == "_y_g_":
                current_state = "BROOM_3"
            elif feedback == "_y_y_":
                current_state = "PROMO_3"
            elif feedback == "_yg__":
                current_state = "HYDRO_3"
            elif feedback == "_yy__":
                current_state = "DROID_3"
            elif feedback == "_yy_g":
                current_state = "DROWN_3"
            elif feedback == "_yy_y":
                current_state = "FROND_3"
            elif feedback == "_yyg_":
                current_state = "DROOL_3"
            elif feedback == "g____":
                current_state = "CHIRP_3"
            elif feedback == "g___g":
                current_state = "CHURN_3"
            elif feedback == "gg_g_":
                current_state = "COLOR_3"
            elif feedback == "gy___":
                current_state = "CROCK_3"
            elif feedback == "gy__g":
                current_state = "CROWN_3"
            elif feedback == "gy__y":
                current_state = "CRONY_3"
            elif feedback == "gy_g_":
                current_state = "CROOK_3"
            elif feedback == "gy_gg":
                current_state = "CROON_3"
            elif feedback == "gyy__":
                current_state = "CHORD_3"
            elif feedback == "y____":
                current_state = "BRICK_3"
            elif feedback == "y___g":
                current_state = "RICIN_3"
            elif feedback == "y___y":
                current_state = "INCUR_3"
            elif feedback == "yg___":
                current_state = "ROCKY_3"
            elif feedback == "yy___":
                current_state = "MICRO_3"
            elif feedback == "yy__y":
                current_state = "BRONC_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COLIN_2":
            if feedback == "_____":
                current_state = "GUAVA_3"
            elif feedback == "____g":
                current_state = "HUMAN_3"
            elif feedback == "____y":
                current_state = "UNJAM_3"
            elif feedback == "___g_":
                current_state = "AFFIX_3"
            elif feedback == "___gg":
                current_state = "ADMIN_3"
            elif feedback == "___y_":
                current_state = "HIJAB_3"
            elif feedback == "___yg":
                current_state = "AVIAN_3"
            elif feedback == "___yy":
                current_state = "ADAPT_3"
            elif feedback == "__g__":
                current_state = "ALLAY_3"
            elif feedback == "__gy_":
                current_state = "PILAF_3"
            elif feedback == "__gyy":
                current_state = "INLAY_3"
            elif feedback == "__y__":
                current_state = "AMPLY_3"
            elif feedback == "__y_y":
                current_state = "ABACK_3"
            elif feedback == "__yg_":
                current_state = "ABJUD_3"
            elif feedback == "__ygg":
                current_state = "PLAIN_3"
            elif feedback == "__ygy":
                current_state = "ANVIL_3"
            elif feedback == "__yy_":
                current_state = "ALIBI_3"
            elif feedback == "__yyg":
                current_state = "ALIGN_3"
            elif feedback == "__yyy":
                current_state = "FINAL_3"
            elif feedback == "_g___":
                current_state = "DOGMA_3"
            elif feedback == "_g__g":
                current_state = "WOMAN_3"
            elif feedback == "_g__y":
                current_state = "GONAD_3"
            elif feedback == "_gg__":
                current_state = "POLKA_3"
            elif feedback == "_gy__":
                current_state = "LOAMY_3"
            elif feedback == "_gy_y":
                current_state = "NODAL_3"
            elif feedback == "_gyy_":
                current_state = "VOILA_3"
            elif feedback == "_y___":
                current_state = "ADOBO_3"
            elif feedback == "_y__y":
                current_state = "AGONY_3"
            elif feedback == "_y_g_":
                current_state = "AUDIO_3"
            elif feedback == "_y_y_":
                current_state = "AMIGO_3"
            elif feedback == "_y_yg":
                current_state = "AXION_3"
            elif feedback == "_y_yy":
                current_state = "AMINO_3"
            elif feedback == "_yg__":
                current_state = "AGLOW_3"
            elif feedback == "_yy__":
                current_state = "AFALD_3"
            elif feedback == "_yy_y":
                current_state = "ALONG_3"
            elif feedback == "_yyg_":
                current_state = "ABOIL_3"
            elif feedback == "_yyy_":
                current_state = "AIOLI_3"
            elif feedback == "g____":
                current_state = "CHAFF_3"
            elif feedback == "g__gg":
                current_state = "CHAIN_3"
            elif feedback == "g__yy":
                current_state = "CHINA_3"
            elif feedback == "g_gg_":
                current_state = "CILIA_3"
            elif feedback == "g_y__":
                current_state = "CHALK_3"
            elif feedback == "g_y_y":
                current_state = "CLANG_3"
            elif feedback == "g_yg_":
                current_state = "CLAIM_3"
            elif feedback == "gg___":
                current_state = "COCOA_3"
            elif feedback == "gg__y":
                current_state = "CONGA_3"
            elif feedback == "gyy__":
                current_state = "CLOAK_3"
            elif feedback == "y____":
                current_state = "AMUCK_3"
            elif feedback == "y___y":
                current_state = "KNACK_3"
            elif feedback == "y__yy":
                current_state = "ACING_3"
            elif feedback == "y_gy_":
                current_state = "LILAC_3"
            elif feedback == "y_y__":
                current_state = "BLACK_3"
            elif feedback == "y_yy_":
                current_state = "ILIAC_3"
            elif feedback == "yg___":
                current_state = "MOCHA_3"
            elif feedback == "ygy__":
                current_state = "FALLS_3"
            elif feedback == "yy___":
                current_state = "ACHOO_3"
            elif feedback == "yy__y":
                current_state = "ANCHO_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COMBO_4":
            if feedback == "ggg__":
                current_state = "COMFY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COMET_3":
            if feedback == "___gg":
                current_state = "BEGET_4"
            elif feedback == "__ggg":
                current_state = "UNMET_4"
            elif feedback == "_y_gy":
                current_state = "OFTEN_4"
            elif feedback == "gg_gg":
                current_state = "COVET_4"
            elif feedback == "yy_gg":
                current_state = "OCTET_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COMFY_3":
            if feedback == "_____":
                current_state = "WHIZZ_4"
            elif feedback == "____g":
                current_state = "WHINY_4"
            elif feedback == "____y":
                current_state = "VINYL_4"
            elif feedback == "___g_":
                current_state = "WHIFF_4"
            elif feedback == "__y_g":
                current_state = "MILKY_4"
            elif feedback == "__yyg":
                current_state = "FILMY_4"
            elif feedback == "_g___":
                current_state = "POLIO_4"
            elif feedback == "_g_y_":
                current_state = "FOLIO_4"
            elif feedback == "_y___":
                current_state = "ONION_4"
            elif feedback == "_yg__":
                current_state = "LIMBO_4"
            elif feedback == "g____":
                current_state = "CHICK_4"
            elif feedback == "g_y__":
                current_state = "CHIMP_4"
            elif feedback == "gg___":
                current_state = "COLIC_4"
            elif feedback == "gy___":
                current_state = "CHINO_4"
            elif feedback == "y____":
                current_state = "WHICH_4"
            elif feedback == "y__y_":
                current_state = "FILCH_4"
            elif feedback == "yg_y_":
                current_state = "FOLIC_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COMIC_4":
            if feedback == "__ggg":
                current_state = "MIMIC_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CONCH_4":
            if feedback == "_g__y":
                current_state = "HOBBY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CONIC_4":
            if feedback == "_gggg":
                current_state = "IONIC_5"
            elif feedback == "_yyy_":
                current_state = "INBOX_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COOLY_3":
            if feedback == "_g___":
                current_state = "MOTIF_4"
            elif feedback == "_g__g":
                current_state = "POTTY_4"
            elif feedback == "_g_gg":
                current_state = "HOTLY_4"
            elif feedback == "_g_yg":
                current_state = "LOFTY_4"
            elif feedback == "_gg__":
                current_state = "BOOTH_4"
            elif feedback == "_gg_g":
                current_state = "BOOTY_4"
            elif feedback == "_gy__":
                current_state = "MOTTO_4"
            elif feedback == "_gyy_":
                current_state = "LOTTO_4"
            elif feedback == "yg___":
                current_state = "BOTCH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COPEN_3":
            if feedback == "_g___":
                current_state = "HOKUM_4"
            elif feedback == "_gg__":
                current_state = "POPUP_4"
            elif feedback == "_y__y":
                current_state = "UNBOX_4"
            elif feedback == "g____":
                current_state = "CHUCK_4"
            elif feedback == "g___y":
                current_state = "CHUNK_4"
            elif feedback == "g_y__":
                current_state = "CHUMP_4"
            elif feedback == "gg___":
                current_state = "COUCH_4"
            elif feedback == "gy___":
                current_state = "CHOUX_4"
            elif feedback == "yg___":
                current_state = "VOUCH_4"
            elif feedback == "ygy__":
                current_state = "POUCH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CORAL_3":
            if feedback == "_gggg":
                current_state = "MORAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CORGI_3":
            if feedback == "gyg_y":
                current_state = "CURIO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CORKY_3":
            if feedback == "ggg_g":
                current_state = "CORNY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COUGH_2":
            if feedback == "_____":
                current_state = "VERSE_3"
            elif feedback == "__y__":
                current_state = "NURSE_3"
            elif feedback == "_g___":
                current_state = "WORSE_3"
            elif feedback == "_g__y":
                current_state = "HORSE_3"
            elif feedback == "_g_y_":
                current_state = "GORSE_3"
            elif feedback == "g_y__":
                current_state = "CURSE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COURT_2":
            if feedback == "___gg":
                current_state = "EVERT_3"
            elif feedback == "___gy":
                current_state = "ENTRY_3"
            elif feedback == "___yg":
                current_state = "AUMIL_3"
            elif feedback == "___yy":
                current_state = "DENIM_3"
            elif feedback == "__gyg":
                current_state = "ERUPT_3"
            elif feedback == "__yyg":
                current_state = "REBUT_3"
            elif feedback == "__yyy":
                current_state = "UTTER_3"
            elif feedback == "_g_yy":
                current_state = "VOTER_3"
            elif feedback == "_y_gg":
                current_state = "OVERT_3"
            elif feedback == "_y_gy":
                current_state = "METRO_3"
            elif feedback == "_y_yg":
                current_state = "REPOT_3"
            elif feedback == "_y_yy":
                current_state = "OTHER_3"
            elif feedback == "_yyyy":
                current_state = "OUTER_3"
            elif feedback == "g__yg":
                current_state = "CREPT_3"
            elif feedback == "g_gyg":
                current_state = "CRUET_3"
            elif feedback == "g_yyy":
                current_state = "CUTER_3"
            elif feedback == "y__yg":
                current_state = "ERECT_3"
            elif feedback == "y__yy":
                current_state = "RETCH_3"
            elif feedback == "y_yyg":
                current_state = "RECUT_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COVEN_3":
            if feedback == "___gg":
                current_state = "QUEEN_4"
            elif feedback == "__ggg":
                current_state = "GIVEN_4"
            elif feedback == "__ygg":
                current_state = "VIXEN_4"
            elif feedback == "_g_gg":
                current_state = "WOKEN_4"
            elif feedback == "_gggg":
                current_state = "WOVEN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COVER_3":
            if feedback == "gg_gg":
                current_state = "COWER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COWLS_2":
            if feedback == "____g":
                current_state = "GUESS_3"
            elif feedback == "____y":
                current_state = "MESSY_3"
            elif feedback == "___yg":
                current_state = "BLESS_3"
            elif feedback == "___yy":
                current_state = "FLESH_3"
            elif feedback == "__g_y":
                current_state = "NEWSY_3"
            elif feedback == "_g__y":
                current_state = "POESY_3"
            elif feedback == "_g_yg":
                current_state = "LOESS_3"
            elif feedback == "_y__y":
                current_state = "QUESO_3"
            elif feedback == "g___g":
                current_state = "CHESS_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "COYLY_4":
            if feedback == "_g_gg":
                current_state = "NOBLY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CRACK_4":
            if feedback == "ggg__":
                current_state = "CRAZY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CRAFT_3":
            if feedback == "_gggg":
                current_state = "DRAFT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CREEK_3":
            if feedback == "gggg_":
                current_state = "CREEP_4"
            elif feedback == "gy_g_":
                current_state = "CYBER_4"
            elif feedback == "gygg_":
                current_state = "CHEER_4"
            elif feedback == "yyy__":
                current_state = "RECUR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CREME_3":
            if feedback == "_y__g":
                current_state = "RUBLE_4"
            elif feedback == "_y_gg":
                current_state = "RHYME_4"
            elif feedback == "_yg_g":
                current_state = "WHERE_4"
            elif feedback == "_yy_g":
                current_state = "REVUE_4"
            elif feedback == "yy__g":
                current_state = "LUCRE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CREPE_3":
            if feedback == "_yyyg":
                current_state = "RUPEE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CREST_2":
            if feedback == "_gggg":
                current_state = "WREST_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CRIER_3":
            if feedback == "y_ggg":
                current_state = "ICIER_4"
            elif feedback == "y_ygg":
                current_state = "NICER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CRIME_3":
            if feedback == "_gg_g":
                current_state = "BRIBE_4"
            elif feedback == "_gggg":
                current_state = "GRIME_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CROCK_3":
            if feedback == "ggg__":
                current_state = "CROUP_4"
            elif feedback == "gyg__":
                current_state = "CHOIR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CUBIC_3":
            if feedback == "_gggg":
                current_state = "PUBIC_4"
            elif feedback == "gg_g_":
                current_state = "CUMIN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CUING_2":
            if feedback == "_____":
                current_state = "TODDY_3"
            elif feedback == "___gg":
                current_state = "THONG_3"
            elif feedback == "__g__":
                current_state = "TWILL_3"
            elif feedback == "__g_y":
                current_state = "THIGH_3"
            elif feedback == "__gg_":
                current_state = "THINK_3"
            elif feedback == "__ggg":
                current_state = "THING_3"
            elif feedback == "__y__":
                current_state = "TIMID_3"
            elif feedback == "__y_y":
                current_state = "TIGHT_3"
            elif feedback == "__yg_":
                current_state = "TINNY_3"
            elif feedback == "__yy_":
                current_state = "TOXIN_3"
            elif feedback == "_g___":
                current_state = "ABETS_3"
            elif feedback == "_gy__":
                current_state = "TULIP_3"
            elif feedback == "_y___":
                current_state = "THUMB_3"
            elif feedback == "_y__y":
                current_state = "TOUGH_3"
            elif feedback == "y_g__":
                current_state = "THICK_3"
            elif feedback == "y_y__":
                current_state = "TOPIC_3"
            elif feedback == "y_yy_":
                current_state = "TONIC_3"
            elif feedback == "ygyy_":
                current_state = "TUNIC_3"
            elif feedback == "yy___":
                current_state = "TOUCH_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CUPID_3":
            if feedback == "_g_gg":
                current_state = "HUMID_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CURRY_3":
            if feedback == "ggg_g":
                current_state = "CURVY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CURVE_3":
            if feedback == "_gg_g":
                current_state = "PUREE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "CYMOL_2":
            if feedback == "_____":
                current_state = "PARKA_3"
            elif feedback == "____y":
                current_state = "LARVA_3"
            elif feedback == "___g_":
                current_state = "BARON_3"
            elif feedback == "___y_":
                current_state = "BURRO_3"
            elif feedback == "___yy":
                current_state = "WORLD_3"
            elif feedback == "__y__":
                current_state = "KARMA_3"
            elif feedback == "__yg_":
                current_state = "MORON_3"
            elif feedback == "__yy_":
                current_state = "FORUM_3"
            elif feedback == "_gy__":
                current_state = "MYRRH_3"
            elif feedback == "_y___":
                current_state = "PARRY_3"
            elif feedback == "_y__y":
                current_state = "BURLY_3"
            elif feedback == "_y_y_":
                current_state = "DWANG_3"
            elif feedback == "_y_yy":
                current_state = "LORDY_3"
            elif feedback == "_yy__":
                current_state = "MARRY_3"
            elif feedback == "_yyy_":
                current_state = "WORMY_3"
            elif feedback == "g__g_":
                current_state = "CAROB_3"
            elif feedback == "g__gg":
                current_state = "CAROL_3"
            elif feedback == "g__y_":
                current_state = "CARGO_3"
            elif feedback == "g_yg_":
                current_state = "CAROM_3"
            elif feedback == "gy___":
                current_state = "CARNY_3"
            elif feedback == "gy__y":
                current_state = "CURLY_3"
            elif feedback == "gy_y_":
                current_state = "CORKY_3"
            elif feedback == "y____":
                current_state = "PARCH_3"
            elif feedback == "y___y":
                current_state = "LARCH_3"
            elif feedback == "y__y_":
                current_state = "BORIC_3"
            elif feedback == "y_y__":
                current_state = "MARCH_3"
            elif feedback == "yg__y":
                current_state = "LYRIC_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DALED_3":
            if feedback == "gg___":
                current_state = "DAFFY_4"
            elif feedback == "gg__y":
                current_state = "DADDY_4"
            elif feedback == "ggg__":
                current_state = "DALLY_4"
            elif feedback == "ggy__":
                current_state = "DAILY_4"
            elif feedback == "yg___":
                current_state = "BAWDY_4"
            elif feedback == "yg__y":
                current_state = "PADDY_4"
            elif feedback == "ygg__":
                current_state = "BALDY_4"
            elif feedback == "ygy__":
                current_state = "BADLY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DEALT_3":
            if feedback == "_yggg":
                current_state = "EXALT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DEATH_3":
            if feedback == "_ggg_":
                current_state = "MEATY_4"
            elif feedback == "_gggg":
                current_state = "HEATH_4"
            elif feedback == "_ggy_":
                current_state = "BEAUT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DEBIT_3":
            if feedback == "gg_yy":
                current_state = "DEITY_4"
            elif feedback == "yy_yg":
                current_state = "EDICT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DEBUG_3":
            if feedback == "gg__g":
                current_state = "DEFOG_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DEBUT_3":
            if feedback == "gg__y":
                current_state = "DETOX_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DECAF_3":
            if feedback == "gggg_":
                current_state = "DECAY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DECOY_3":
            if feedback == "gg__g":
                current_state = "DEIFY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DEFER_3":
            if feedback == "g__gg":
                current_state = "DRYER_4"
            elif feedback == "gg__g":
                current_state = "DEMUR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DEIGN_3":
            if feedback == "gg__g":
                current_state = "DEMON_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DENIM_3":
            if feedback == "_g___":
                current_state = "PETER_4"
            elif feedback == "_g__y":
                current_state = "METER_4"
            elif feedback == "_y___":
                current_state = "ETHER_4"
            elif feedback == "_y_y_":
                current_state = "BITER_4"
            elif feedback == "_y_yy":
                current_state = "MITER_4"
            elif feedback == "_yy__":
                current_state = "ENTER_4"
            elif feedback == "_yyy_":
                current_state = "INTER_4"
            elif feedback == "gg___":
                current_state = "DETER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DEPOT_3":
            if feedback == "ggg_y":
                current_state = "DEPTH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DEVIL_3":
            if feedback == "gy__g":
                current_state = "DWELL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DEVON_3":
            if feedback == "g____":
                current_state = "DIPPY_4"
            elif feedback == "g___y":
                current_state = "DINKY_4"
            elif feedback == "g_g__":
                current_state = "DIVVY_4"
            elif feedback == "y____":
                current_state = "BIDDY_4"
            elif feedback == "y___y":
                current_state = "WINDY_4"
            elif feedback == "y__g_":
                current_state = "WIDOW_4"
            elif feedback == "y__y_":
                current_state = "KIDDO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DIARY_3":
            if feedback == "g_gg_":
                current_state = "DWARF_4"
            elif feedback == "g_gy_":
                current_state = "DRAMA_4"
            elif feedback == "y_ygy":
                current_state = "HYDRA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DICEY_3":
            if feedback == "g__gg":
                current_state = "DOPEY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DIGHT_2":
            if feedback == "____g":
                current_state = "QUEST_3"
            elif feedback == "___yg":
                current_state = "CHEST_3"
            elif feedback == "__y_g":
                current_state = "GUEST_3"
            elif feedback == "_y__g":
                current_state = "EXIST_3"
            elif feedback == "_y_yg":
                current_state = "HEIST_3"
            elif feedback == "gy__g":
                current_state = "DEIST_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DILLY_3":
            if feedback == "gg_gg":
                current_state = "DIMLY_4"
            elif feedback == "yyygy":
                current_state = "IDYLL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DINER_3":
            if feedback == "gg_gg":
                current_state = "DIVER_4"
            elif feedback == "gy_gg":
                current_state = "DRIER_4"
            elif feedback == "gy_gy":
                current_state = "DRIED_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DINGO_3":
            if feedback == "gggg_":
                current_state = "DINGY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DIPPY_4":
            if feedback == "gg__g":
                current_state = "DIZZY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DISHY_3":
            if feedback == "__g__":
                current_state = "BOSOM_4"
            elif feedback == "__y__":
                current_state = "SCOFF_4"
            elif feedback == "__y_g":
                current_state = "SOGGY_4"
            elif feedback == "__yyg":
                current_state = "SHOWY_4"
            elif feedback == "_gggg":
                current_state = "FISHY_4"
            elif feedback == "ggg__":
                current_state = "DISCO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DITTY_3":
            if feedback == "ggg__":
                current_state = "DITCH_4"
            elif feedback == "ggg_g":
                current_state = "DITZY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DODGE_3":
            if feedback == "_g_gg":
                current_state = "GOUGE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DODGY_3":
            if feedback == "gg_gg":
                current_state = "DOGGY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DOGAN_2":
            if feedback == "___g_":
                current_state = "TUBAL_3"
            elif feedback == "___gg":
                current_state = "TITAN_3"
            elif feedback == "___y_":
                current_state = "TIBIA_3"
            elif feedback == "___yg":
                current_state = "TWAIN_3"
            elif feedback == "___yy":
                current_state = "THANK_3"
            elif feedback == "__yyy":
                current_state = "TWANG_3"
            elif feedback == "_g_g_":
                current_state = "TOPAZ_3"
            elif feedback == "_g_gy":
                current_state = "TONAL_3"
            elif feedback == "_gyyy":
                current_state = "TONGA_3"
            elif feedback == "y__g_":
                current_state = "TIDAL_3"
            elif feedback == "yg_g_":
                current_state = "TODAY_3"
            elif feedback == "yg_y_":
                current_state = "TOADY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DOGMA_3":
            if feedback == "_g_gg":
                current_state = "MOMMA_4"
            elif feedback == "_g_gy":
                current_state = "FOAMY_4"
            elif feedback == "yg__g":
                current_state = "VODKA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DOING_3":
            if feedback == "g_ggg":
                current_state = "DYING_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DOLCI_2":
            if feedback == "_____":
                current_state = "RUMPY_3"
            elif feedback == "____g":
                current_state = "REIKI_3"
            elif feedback == "____y":
                current_state = "PINKY_3"
            elif feedback == "___g_":
                current_state = "WRECK_3"
            elif feedback == "___y_":
                current_state = "CREEK_3"
            elif feedback == "___yy":
                current_state = "CRIER_3"
            elif feedback == "__g__":
                current_state = "RULER_3"
            elif feedback == "__g_y":
                current_state = "FILER_3"
            elif feedback == "__gyy":
                current_state = "RELIC_3"
            elif feedback == "__y__":
                current_state = "BEVER_3"
            elif feedback == "__y_y":
                current_state = "AFION_3"
            elif feedback == "__yy_":
                current_state = "CLERK_3"
            elif feedback == "_g___":
                current_state = "WHOMP_3"
            elif feedback == "_g_y_":
                current_state = "COVER_3"
            elif feedback == "_gy__":
                current_state = "ADVEW_3"
            elif feedback == "_y___":
                current_state = "OFFER_3"
            elif feedback == "_y_y_":
                current_state = "OCHER_3"
            elif feedback == "_yg__":
                current_state = "OGLER_3"
            elif feedback == "_yg_y":
                current_state = "OILER_3"
            elif feedback == "g____":
                current_state = "DEFER_3"
            elif feedback == "g___y":
                current_state = "DINER_3"
            elif feedback == "g__g_":
                current_state = "DRECK_3"
            elif feedback == "g__y_":
                current_state = "DECRY_3"
            elif feedback == "g__yy":
                current_state = "DICER_3"
            elif feedback == "gg___":
                current_state = "DOPER_3"
            elif feedback == "gy_y_":
                current_state = "DECOR_3"
            elif feedback == "y____":
                current_state = "BEGUN_3"
            elif feedback == "y___y":
                current_state = "BEDEW_3"
            elif feedback == "y__y_":
                current_state = "CREED_3"
            elif feedback == "y__yy":
                current_state = "CIDER_3"
            elif feedback == "y_g_y":
                current_state = "IDLER_3"
            elif feedback == "y_y__":
                current_state = "ELDER_3"
            elif feedback == "yg___":
                current_state = "RODEO_3"
            elif feedback == "yg_y_":
                current_state = "CODER_3"
            elif feedback == "yy___":
                current_state = "ODDER_3"
            elif feedback == "yy_y_":
                current_state = "CREDO_3"
            elif feedback == "yyy__":
                current_state = "OLDER_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DOLLY_3":
            if feedback == "yy_gg":
                current_state = "ODDLY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DOMED_3":
            if feedback == "g__g_":
                current_state = "DWEEB_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DONUT_2":
            if feedback == "____g":
                current_state = "FILMI_3"
            elif feedback == "____y":
                current_state = "WIFTY_3"
            elif feedback == "___gy":
                current_state = "CUTUP_3"
            elif feedback == "___yg":
                current_state = "AGBAS_3"
            elif feedback == "___yy":
                current_state = "BIGLY_3"
            elif feedback == "__g_y":
                current_state = "MINTY_3"
            elif feedback == "__y_g":
                current_state = "FLINT_3"
            elif feedback == "__y_y":
                current_state = "NIFTY_3"
            elif feedback == "__ygg":
                current_state = "INPUT_3"
            elif feedback == "__yyg":
                current_state = "BLUNT_3"
            elif feedback == "__yyy":
                current_state = "NUTTY_3"
            elif feedback == "_g__g":
                current_state = "VOMIT_3"
            elif feedback == "_g__y":
                current_state = "COOLY_3"
            elif feedback == "_g_yg":
                current_state = "MOULT_3"
            elif feedback == "_g_yy":
                current_state = "ACCOY_3"
            elif feedback == "_gg_y":
                current_state = "MONTH_3"
            elif feedback == "_gy_g":
                current_state = "JOINT_3"
            elif feedback == "_gy_y":
                current_state = "NOTCH_3"
            elif feedback == "_gyyg":
                current_state = "ACMES_3"
            elif feedback == "_y__g":
                current_state = "PILOT_3"
            elif feedback == "_y__y":
                current_state = "CLOTH_3"
            elif feedback == "_y_gg":
                current_state = "CLOUT_3"
            elif feedback == "_y_yg":
                current_state = "OUGHT_3"
            elif feedback == "_y_yy":
                current_state = "OUTGO_3"
            elif feedback == "_yg_g":
                current_state = "PINOT_3"
            elif feedback == "_yg_y":
                current_state = "PINTO_3"
            elif feedback == "_ygyy":
                current_state = "JUNTO_3"
            elif feedback == "_yy_g":
                current_state = "INGOT_3"
            elif feedback == "_yyyy":
                current_state = "FUTON_3"
            elif feedback == "g___g":
                current_state = "DIGIT_3"
            elif feedback == "g___y":
                current_state = "DITTY_3"
            elif feedback == "g__yy":
                current_state = "DUTCH_3"
            elif feedback == "gg__y":
                current_state = "DOTTY_3"
            elif feedback == "gg_yg":
                current_state = "DOUBT_3"
            elif feedback == "gy__g":
                current_state = "DIVOT_3"
            elif feedback == "gy__y":
                current_state = "DITTO_3"
            elif feedback == "y___y":
                current_state = "WIDTH_3"
            elif feedback == "yy__g":
                current_state = "IDIOT_3"
            elif feedback == "yy_yy":
                current_state = "OUTDO_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DOPER_3":
            if feedback == "gg_gg":
                current_state = "DOZER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DOUGH_3":
            if feedback == "__g__":
                current_state = "JAUNT_4"
            elif feedback == "__g_y":
                current_state = "HAUNT_4"
            elif feedback == "__gy_":
                current_state = "GAUNT_4"
            elif feedback == "__yy_":
                current_state = "GAMUT_4"
            elif feedback == "g_g__":
                current_state = "DAUNT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DOWRY_3":
            if feedback == "yg_g_":
                current_state = "GOURD_4"
            elif feedback == "yggyg":
                current_state = "ROWDY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DRAIN_3":
            if feedback == "ggg_g":
                current_state = "DRAWN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DRAKE_3":
            if feedback == "ggg_g":
                current_state = "DRAPE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DRIFT_3":
            if feedback == "_gggg":
                current_state = "GRIFT_4"
            elif feedback == "_gyyg":
                current_state = "FRUIT_4"
            elif feedback == "_ygyg":
                current_state = "FLIRT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DRILL_3":
            if feedback == "gg_g_":
                current_state = "DRYLY_4"
            elif feedback == "ggy__":
                current_state = "DRUID_4"
            elif feedback == "yyy__":
                current_state = "RIGID_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DRINK_3":
            if feedback == "gg_gg":
                current_state = "DRUNK_4"
            elif feedback == "yggg_":
                current_state = "GRIND_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DROID_3":
            if feedback == "_gg_g":
                current_state = "PROUD_4"
            elif feedback == "_yg_g":
                current_state = "FJORD_4"
            elif feedback == "ggg__":
                current_state = "DROLL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DROOL_3":
            if feedback == "gggg_":
                current_state = "DROOP_4"
            elif feedback == "yggg_":
                current_state = "BROOD_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DROSS_3":
            if feedback == "_gggg":
                current_state = "GROSS_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DROVE_3":
            if feedback == "ygg_g":
                current_state = "ERODE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DUCHY_4":
            if feedback == "ggg_g":
                current_state = "DUCKY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DUMMY_3":
            if feedback == "gg__g":
                current_state = "DUCHY_4"
            elif feedback == "ggg_g":
                current_state = "DUMPY_4"
            elif feedback == "yg___":
                current_state = "KUDZU_4"
            elif feedback == "yg__g":
                current_state = "BUDDY_4"
            elif feedback == "ygy_g":
                current_state = "MUDDY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DUMPS_3":
            if feedback == "_____":
                current_state = "CHIVE_4"
            elif feedback == "___y_":
                current_state = "PIECE_4"
            elif feedback == "__y__":
                current_state = "CHIME_4"
            elif feedback == "_g___":
                current_state = "JUICE_4"
            elif feedback == "_y_y_":
                current_state = "PIQUE_4"
            elif feedback == "_yy__":
                current_state = "IMBUE_4"
            elif feedback == "y____":
                current_state = "CHIDE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DUMPY_3":
            if feedback == "_____":
                current_state = "BELLE_4"
            elif feedback == "____y":
                current_state = "CYCLE_4"
            elif feedback == "___y_":
                current_state = "PLEBE_4"
            elif feedback == "__y__":
                current_state = "MELEE_4"
            elif feedback == "_y___":
                current_state = "FLUKE_4"
            elif feedback == "_yy__":
                current_state = "FLUME_4"
            elif feedback == "_yyy_":
                current_state = "PLUME_4"
            elif feedback == "g____":
                current_state = "DELVE_4"
            elif feedback == "yy___":
                current_state = "ELUDE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DWANG_3":
            if feedback == "_____":
                current_state = "PORKY_4"
            elif feedback == "____y":
                current_state = "PORGY_4"
            elif feedback == "___g_":
                current_state = "HORNY_4"
            elif feedback == "_y___":
                current_state = "WORRY_4"
            elif feedback == "g____":
                current_state = "DORKY_4"
            elif feedback == "yy___":
                current_state = "WORDY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "DYNEL_2":
            if feedback == "___g_":
                current_state = "BICEP_3"
            elif feedback == "___gg":
                current_state = "BEVUE_3"
            elif feedback == "___gy":
                current_state = "BLEEP_3"
            elif feedback == "___y_":
                current_state = "GECKO_3"
            elif feedback == "___yg":
                current_state = "KVELL_3"
            elif feedback == "___yy":
                current_state = "PHLOX_3"
            elif feedback == "__ggy":
                current_state = "LINEN_3"
            elif feedback == "__gy_":
                current_state = "VENOM_3"
            elif feedback == "__yg_":
                current_state = "COVEN_3"
            elif feedback == "__ygg":
                current_state = "INCEL_3"
            elif feedback == "__ygy":
                current_state = "LIKEN_3"
            elif feedback == "__yy_":
                current_state = "BEGIN_3"
            elif feedback == "__yyg":
                current_state = "KNELL_3"
            elif feedback == "__yyy":
                current_state = "FELON_3"
            elif feedback == "_gyg_":
                current_state = "HYMEN_3"
            elif feedback == "_gyy_":
                current_state = "EYING_3"
            elif feedback == "_y_g_":
                current_state = "CHOMP_3"
            elif feedback == "_y_gg":
                current_state = "YOKEL_3"
            elif feedback == "_y_gy":
                current_state = "GLUEY_3"
            elif feedback == "_y_y_":
                current_state = "APEEK_3"
            elif feedback == "_y_yy":
                current_state = "BELLY_3"
            elif feedback == "_ygg_":
                current_state = "BLIMP_3"
            elif feedback == "_ygy_":
                current_state = "PENNY_3"
            elif feedback == "_yyy_":
                current_state = "ENJOY_3"
            elif feedback == "_yyyy":
                current_state = "NEWLY_3"
            elif feedback == "g__g_":
                current_state = "DOMED_3"
            elif feedback == "g__gg":
                current_state = "DOWEL_3"
            elif feedback == "g__y_":
                current_state = "DEBUG_3"
            elif feedback == "g__yg":
                current_state = "DEVIL_3"
            elif feedback == "g_gy_":
                current_state = "DENIM_3"
            elif feedback == "g_yg_":
                current_state = "DOZEN_3"
            elif feedback == "g_yy_":
                current_state = "DEIGN_3"
            elif feedback == "gy_g_":
                current_state = "DICEY_3"
            elif feedback == "gy_y_":
                current_state = "DECOY_3"
            elif feedback == "y__g_":
                current_state = "MOPED_3"
            elif feedback == "y__gg":
                current_state = "MODEL_3"
            elif feedback == "y__gy":
                current_state = "BLEED_3"
            elif feedback == "y__y_":
                current_state = "MEDIC_3"
            elif feedback == "y__yy":
                current_state = "FIELD_3"
            elif feedback == "y_yg_":
                current_state = "UNFED_3"
            elif feedback == "y_ygy":
                current_state = "OLDEN_3"
            elif feedback == "y_yy_":
                current_state = "FIEND_3"
            elif feedback == "y_yyy":
                current_state = "BLEND_3"
            elif feedback == "yy_gg":
                current_state = "YODEL_3"
            elif feedback == "yy_y_":
                current_state = "EDIFY_3"
            elif feedback == "yy_yy":
                current_state = "YIELD_3"
            elif feedback == "yygy_":
                current_state = "BENDY_3"
            elif feedback == "yyyy_":
                current_state = "NEEDY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "EASEL_2":
            if feedback == "_gyg_":
                current_state = "SAMEY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "EDIFY_3":
            if feedback == "yy__g":
                current_state = "WEEDY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ELATE_3":
            if feedback == "_gggg":
                current_state = "PLATE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "EMBOW_3":
            if feedback == "_____":
                current_state = "HATCH_4"
            elif feedback == "____y":
                current_state = "WATCH_4"
            elif feedback == "__y__":
                current_state = "BATCH_4"
            elif feedback == "_y___":
                current_state = "MATCH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "EMCEE_3":
            if feedback == "g___g":
                current_state = "EXUDE_4"
            elif feedback == "g_y_g":
                current_state = "EDUCE_4"
            elif feedback == "y___g":
                current_state = "QUEUE_4"
            elif feedback == "y__yg":
                current_state = "PEEVE_4"
            elif feedback == "y_y_g":
                current_state = "DEUCE_4"
            elif feedback == "yy__g":
                current_state = "FEMME_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "EMPTY_3":
            if feedback == "y_yy_":
                current_state = "GETUP_4"
            elif feedback == "yyyy_":
                current_state = "KEMPT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ENEMA_3":
            if feedback == "__gyg":
                current_state = "OMEGA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ENJOY_3":
            if feedback == "gg__g":
                current_state = "ENEMY_4"
            elif feedback == "gg_gg":
                current_state = "ENVOY_4"
            elif feedback == "gy_yg":
                current_state = "EBONY_4"
            elif feedback == "yy__g":
                current_state = "VEINY_4"
            elif feedback == "yy_yg":
                current_state = "PEONY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ENSUE_3":
            if feedback == "yggyg":
                current_state = "UNSEE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ENTRY_3":
            if feedback == "y_gg_":
                current_state = "PETRI_4"
            elif feedback == "y_ggg":
                current_state = "RETRY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ESTER_2":
            if feedback == "yyy_y":
                current_state = "STERN_3"
            elif feedback == "yyygg":
                current_state = "STEER_3"
            elif feedback == "yyygy":
                current_state = "RESET_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "EVERT_3":
            if feedback == "__ggg":
                current_state = "INERT_4"
            elif feedback == "g_ggg":
                current_state = "EXERT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "EXCEL_4":
            if feedback == "gg_gg":
                current_state = "EXPEL_5"
            elif feedback == "y__gg":
                current_state = "WHEEL_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "EXULT_3":
            if feedback == "g__yg":
                current_state = "ELECT_4"
            elif feedback == "g__yy":
                current_state = "ETHYL_4"
            elif feedback == "gg_yy":
                current_state = "EXTOL_4"
            elif feedback == "y__gg":
                current_state = "KNELT_4"
            elif feedback == "y__yg":
                current_state = "CLEFT_4"
            elif feedback == "y__yy":
                current_state = "LEFTY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FADER_3":
            if feedback == "_g_gg":
                current_state = "RAVER_4"
            elif feedback == "_g_gy":
                current_state = "RAVEN_4"
            elif feedback == "_gggg":
                current_state = "WADER_4"
            elif feedback == "gg_gg":
                current_state = "FAKER_4"
            elif feedback == "yg_gg":
                current_state = "WAFER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FAIRY_3":
            if feedback == "_gggg":
                current_state = "HAIRY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FALLS_3":
            if feedback == "_yy__":
                current_state = "VOCAL_4"
            elif feedback == "_yyy_":
                current_state = "LOCAL_4"
            elif feedback == "gyy__":
                current_state = "FOCAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FAULT_3":
            if feedback == "_gggg":
                current_state = "VAULT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FAUNA_3":
            if feedback == "_g_gg":
                current_state = "MANNA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FEHME_4":
            if feedback == "_____":
                current_state = "JOLLY_5"
            elif feedback == "___y_":
                current_state = "MOLLY_5"
            elif feedback == "__y__":
                current_state = "HOLLY_5"
            elif feedback == "g____":
                current_state = "FOLLY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FELON_3":
            if feedback == "_gggg":
                current_state = "MELON_4"
            elif feedback == "_gygg":
                current_state = "LEMON_4"
            elif feedback == "yyy_g":
                current_state = "ELFIN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FERAL_2":
            if feedback == "_ggg_":
                current_state = "RERAN_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FETAL_3":
            if feedback == "_gggg":
                current_state = "METAL_4"
            elif feedback == "_gyyy":
                current_state = "DELTA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FEVER_4":
            if feedback == "_g_gg":
                current_state = "NEWER_5"
            elif feedback == "_gggg":
                current_state = "NEVER_5"
            elif feedback == "_y_gy":
                current_state = "GREEN_5"
            elif feedback == "gg_gg":
                current_state = "FEWER_5"
            elif feedback == "gy_gg":
                current_state = "FREER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FIELD_3":
            if feedback == "_gggg":
                current_state = "WIELD_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FIEND_3":
            if feedback == "__ggg":
                current_state = "UPEND_4"
            elif feedback == "__yyy":
                current_state = "ENDOW_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FILER_3":
            if feedback == "_gggg":
                current_state = "MILER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FILLY_4":
            if feedback == "_gggg":
                current_state = "HILLY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FILMI_3":
            if feedback == "_g___":
                current_state = "WIGHT_4"
            elif feedback == "_g_y_":
                current_state = "MIGHT_4"
            elif feedback == "_gy__":
                current_state = "LIGHT_4"
            elif feedback == "_gy_y":
                current_state = "LICIT_4"
            elif feedback == "_gyyy":
                current_state = "LIMIT_4"
            elif feedback == "gg___":
                current_state = "FIGHT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FINER_4":
            if feedback == "_gggg":
                current_state = "MINER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FIZZY_4":
            if feedback == "yg__g":
                current_state = "JIFFY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FLANK_4":
            if feedback == "_gggg":
                current_state = "PLANK_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FLASH_3":
            if feedback == "_gggg":
                current_state = "SLASH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FLASK_3":
            if feedback == "_ggg_":
                current_state = "GLASS_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FLICK_3":
            if feedback == "_gg__":
                current_state = "BLIMP_4"
            elif feedback == "_gg_g":
                current_state = "BLINK_4"
            elif feedback == "_gggg":
                current_state = "CLICK_4"
            elif feedback == "_ggy_":
                current_state = "CLIMB_4"
            elif feedback == "_ggyg":
                current_state = "CLINK_4"
            elif feedback == "yggy_":
                current_state = "CLIFF_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FLINT_3":
            if feedback == "__yyg":
                current_state = "NIGHT_4"
            elif feedback == "_gggg":
                current_state = "GLINT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FLOSS_3":
            if feedback == "_gggg":
                current_state = "GLOSS_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FLUTE_3":
            if feedback == "_gggg":
                current_state = "GLUTE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FLYER_4":
            if feedback == "_y_gg":
                current_state = "LUGER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FOIST_3":
            if feedback == "_gggg":
                current_state = "JOIST_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FORAY_3":
            if feedback == "_ggg_":
                current_state = "BORAX_4"
            elif feedback == "_gggg":
                current_state = "MORAY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FORCE_3":
            if feedback == "_gg_g":
                current_state = "HORDE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FORUM_3":
            if feedback == "_gg_y":
                current_state = "MORPH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FOUND_4":
            if feedback == "_gggg":
                current_state = "WOUND_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FOUNT_2":
            if feedback == "____g":
                current_state = "SPILT_3"
            elif feedback == "____y":
                current_state = "SILTY_3"
            elif feedback == "___gg":
                current_state = "STINT_3"
            elif feedback == "___gy":
                current_state = "STING_3"
            elif feedback == "___yy":
                current_state = "SYNTH_3"
            elif feedback == "__g_y":
                current_state = "ADEEM_3"
            elif feedback == "__ggg":
                current_state = "SHUNT_3"
            elif feedback == "__ggy":
                current_state = "STUNG_3"
            elif feedback == "__y_y":
                current_state = "ADLIB_3"
            elif feedback == "_g__g":
                current_state = "POSIT_3"
            elif feedback == "_g__y":
                current_state = "SOOTH_3"
            elif feedback == "_gg_y":
                current_state = "SOUTH_3"
            elif feedback == "_gy_y":
                current_state = "LOTUS_3"
            elif feedback == "_y__g":
                current_state = "SCOOT_3"
            elif feedback == "_y__y":
                current_state = "APIOL_3"
            elif feedback == "_y_gy":
                current_state = "STONY_3"
            elif feedback == "_y_yg":
                current_state = "SNOOT_3"
            elif feedback == "_yy_g":
                current_state = "CAPHS_3"
            elif feedback == "_yy_y":
                current_state = "GUSTO_3"
            elif feedback == "_yyyg":
                current_state = "SNOUT_3"
            elif feedback == "g_y_y":
                current_state = "FUSTY_3"
            elif feedback == "y___g":
                current_state = "SHIFT_3"
            elif feedback == "y___y":
                current_state = "STIFF_3"
            elif feedback == "y_g_y":
                current_state = "STUFF_3"
            elif feedback == "yg__y":
                current_state = "SOFTY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FRACK_4":
            if feedback == "_gggg":
                current_state = "WRACK_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FRAIL_3":
            if feedback == "_gg_g":
                current_state = "CRAWL_4"
            elif feedback == "_gggg":
                current_state = "GRAIL_4"
            elif feedback == "_yyyg":
                current_state = "RIVAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FRANC_3":
            if feedback == "_ggg_":
                current_state = "PRANK_4"
            elif feedback == "_gggy":
                current_state = "CRANK_4"
            elif feedback == "gggg_":
                current_state = "FRANK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FRIED_4":
            if feedback == "_gggg":
                current_state = "PRIED_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FUDGE_4":
            if feedback == "_gggg":
                current_state = "JUDGE_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FUGLY_3":
            if feedback == "_____":
                current_state = "PRIMP_4"
            elif feedback == "____g":
                current_state = "PRIVY_4"
            elif feedback == "___g_":
                current_state = "KRILL_4"
            elif feedback == "___gg":
                current_state = "WRYLY_4"
            elif feedback == "___y_":
                current_state = "WHIRL_4"
            elif feedback == "__y_g":
                current_state = "GRIMY_4"
            elif feedback == "__yg_":
                current_state = "GRILL_4"
            elif feedback == "_g___":
                current_state = "QUIRK_4"
            elif feedback == "_g__g":
                current_state = "RUMMY_4"
            elif feedback == "_gg_g":
                current_state = "RUGBY_4"
            elif feedback == "_y_y_":
                current_state = "BLURB_4"
            elif feedback == "_yy__":
                current_state = "GRUMP_4"
            elif feedback == "g____":
                current_state = "FRIZZ_4"
            elif feedback == "g__g_":
                current_state = "FRILL_4"
            elif feedback == "gy___":
                current_state = "FRUMP_4"
            elif feedback == "yyy__":
                current_state = "GRUFF_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FUNKY_4":
            if feedback == "_g_gg":
                current_state = "YUCKY_5"
            elif feedback == "_gggg":
                current_state = "JUNKY_5"
            elif feedback == "gg__g":
                current_state = "FUZZY_5"
            elif feedback == "ggg_g":
                current_state = "FUNNY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FUROR_3":
            if feedback == "__gg_":
                current_state = "BORON_4"
            elif feedback == "_gggg":
                current_state = "JUROR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FURRY_3":
            if feedback == "_gggg":
                current_state = "HURRY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "FUSSY_3":
            if feedback == "__ggg":
                current_state = "BOSSY_4"
            elif feedback == "_gggg":
                current_state = "GUSSY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GABBY_4":
            if feedback == "gg__g":
                current_state = "GAWKY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GATOR_2":
            if feedback == "_gg_y":
                current_state = "RATTY_3"
            elif feedback == "_ggyy":
                current_state = "RATIO_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GAUGE_3":
            if feedback == "ggg_g":
                current_state = "GAUZE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GAYER_3":
            if feedback == "gg_gg":
                current_state = "GAZER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GECKO_3":
            if feedback == "_g__g":
                current_state = "MEZZO_4"
            elif feedback == "_g__y":
                current_state = "BEBOP_4"
            elif feedback == "_gy__":
                current_state = "BEECH_4"
            elif feedback == "_y___":
                current_state = "EQUIP_4"
            elif feedback == "_y__y":
                current_state = "EMOJI_4"
            elif feedback == "_y_yy":
                current_state = "EBOOK_4"
            elif feedback == "_yy_g":
                current_state = "CHEMO_4"
            elif feedback == "_yy_y":
                current_state = "EPOCH_4"
            elif feedback == "_yyy_":
                current_state = "CHECK_4"
            elif feedback == "yg___":
                current_state = "WEIGH_4"
            elif feedback == "yg__y":
                current_state = "BEFOG_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GEESE_3":
            if feedback == "_g_gg":
                current_state = "SENSE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GENIO_2":
            if feedback == "_g___":
                current_state = "VERVE_3"
            elif feedback == "_g_g_":
                current_state = "EERIE_3"
            elif feedback == "_gy__":
                current_state = "NERVE_3"
            elif feedback == "_y___":
                current_state = "CURVE_3"
            elif feedback == "_y__y":
                current_state = "FORCE_3"
            elif feedback == "_yy_y":
                current_state = "BORNE_3"
            elif feedback == "gy__y":
                current_state = "GORGE_3"
            elif feedback == "yg___":
                current_state = "MERGE_3"
            elif feedback == "yy___":
                current_state = "PURGE_3"
            elif feedback == "yy__y":
                current_state = "FORGE_3"
            elif feedback == "yy_y_":
                current_state = "DIRGE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GIRTH_3":
            if feedback == "_gggg":
                current_state = "MIRTH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GLACE_3":
            if feedback == "ggg_g":
                current_state = "GLAZE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GLAMP_2":
            if feedback == "__y__":
                current_state = "FADER_3"
            elif feedback == "__y_y":
                current_state = "CARVY_3"
            elif feedback == "__yy_":
                current_state = "MAKER_3"
            elif feedback == "_yy__":
                current_state = "BALER_3"
            elif feedback == "_yy_y":
                current_state = "PALER_3"
            elif feedback == "_yyy_":
                current_state = "LAMER_3"
            elif feedback == "g_y__":
                current_state = "GAYER_3"
            elif feedback == "g_yy_":
                current_state = "GAMER_3"
            elif feedback == "y_y__":
                current_state = "ARERE_3"
            elif feedback == "y_y_y":
                current_state = "PAGER_3"
            elif feedback == "yyy__":
                current_state = "LAGER_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GLAND_2":
            if feedback == "__g__":
                current_state = "KACHA_3"
            elif feedback == "__g_y":
                current_state = "EVADE_3"
            elif feedback == "__gg_":
                current_state = "INANE_3"
            elif feedback == "__gy_":
                current_state = "KNAVE_3"
            elif feedback == "__y__":
                current_state = "ABOVE_3"
            elif feedback == "__y_y":
                current_state = "ABIDE_3"
            elif feedback == "__yy_":
                current_state = "ANIME_3"
            elif feedback == "__yyy":
                current_state = "ANODE_3"
            elif feedback == "_gg__":
                current_state = "CHIMB_3"
            elif feedback == "_gg_y":
                current_state = "BLADE_3"
            elif feedback == "_ggg_":
                current_state = "PLANE_3"
            elif feedback == "_gy__":
                current_state = "ALIKE_3"
            elif feedback == "_gyg_":
                current_state = "ALONE_3"
            elif feedback == "_yg__":
                current_state = "LEAVE_3"
            elif feedback == "_yy__":
                current_state = "AMBLE_3"
            elif feedback == "_yy_y":
                current_state = "ADDLE_3"
            elif feedback == "_yyy_":
                current_state = "ANKLE_3"
            elif feedback == "ggg__":
                current_state = "GLACE_3"
            elif feedback == "ggg_y":
                current_state = "GLADE_3"
            elif feedback == "y_g__":
                current_state = "AGAPE_3"
            elif feedback == "y_g_y":
                current_state = "ADAGE_3"
            elif feedback == "ygy__":
                current_state = "ALGAE_3"
            elif feedback == "yyy__":
                current_state = "AGILE_3"
            elif feedback == "yyyy_":
                current_state = "ANGLE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GLIDE_3":
            if feedback == "gyg_g":
                current_state = "GUILE_4"
            elif feedback == "yyy_g":
                current_state = "BILGE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GLOBE_3":
            if feedback == "ggg_g":
                current_state = "GLOVE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GLOOM_3":
            if feedback == "gg___":
                current_state = "GLYPH_4"
            elif feedback == "ggg__":
                current_state = "GLOWY_4"
            elif feedback == "gggg_":
                current_state = "GLOOP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GLUEY_3":
            if feedback == "_y_gg":
                current_state = "HOLEY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GLUME_3":
            if feedback == "_____":
                current_state = "JAZZY_4"
            elif feedback == "___g_":
                current_state = "JAMMY_4"
            elif feedback == "___y_":
                current_state = "VAMPY_4"
            elif feedback == "_y___":
                current_state = "BALKY_4"
            elif feedback == "_y_g_":
                current_state = "BALMY_4"
            elif feedback == "g____":
                current_state = "GABBY_4"
            elif feedback == "g_g__":
                current_state = "GAUZY_4"
            elif feedback == "gy___":
                current_state = "GAILY_4"
            elif feedback == "y____":
                current_state = "BAGGY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GNARL_3":
            if feedback == "_yyyy":
                current_state = "LUNAR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GONAD_3":
            if feedback == "_gygg":
                current_state = "NOMAD_4"
            elif feedback == "gggy_":
                current_state = "GONNA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GOOFY_3":
            if feedback == "ggg_g":
                current_state = "GOOPY_4"
            elif feedback == "ggy__":
                current_state = "GONZO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GRAFT_3":
            if feedback == "ggg_g":
                current_state = "GRANT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GRAND_2":
            if feedback == "_gg__":
                current_state = "VOCAB_3"
            elif feedback == "_gg_y":
                current_state = "DRAKE_3"
            elif feedback == "_ggg_":
                current_state = "CRANE_3"
            elif feedback == "_yg__":
                current_state = "BLARE_3"
            elif feedback == "_yy__":
                current_state = "AFIRE_3"
            elif feedback == "_yy_y":
                current_state = "ADORE_3"
            elif feedback == "ggg__":
                current_state = "CAPIZ_3"
            elif feedback == "ggg_y":
                current_state = "GRADE_3"
            elif feedback == "gyg__":
                current_state = "GLARE_3"
            elif feedback == "ygy__":
                current_state = "ARGUE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GROOM_4":
            if feedback == "_gggg":
                current_state = "VROOM_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GROWL_3":
            if feedback == "_gg__":
                current_state = "PROXY_4"
            elif feedback == "_gg_g":
                current_state = "BROIL_4"
            elif feedback == "_gggg":
                current_state = "PROWL_4"
            elif feedback == "_gy__":
                current_state = "PRIMO_4"
            elif feedback == "_yg__":
                current_state = "IVORY_4"
            elif feedback == "_yg_y":
                current_state = "FLOUR_4"
            elif feedback == "_ygyg":
                current_state = "WHORL_4"
            elif feedback == "ggg__":
                current_state = "GROUP_4"
            elif feedback == "gyg_y":
                current_state = "GLORY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GUAVA_3":
            if feedback == "__y__":
                current_state = "BYWAY_4"
            elif feedback == "_gg__":
                current_state = "QUAFF_4"
            elif feedback == "_yy__":
                current_state = "ABUZZ_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GUILD_2":
            if feedback == "_____":
                current_state = "WHOMP_3"
            elif feedback == "____y":
                current_state = "HOWDY_3"
            elif feedback == "___g_":
                current_state = "LOWLY_3"
            elif feedback == "___gy":
                current_state = "DOLLY_3"
            elif feedback == "___y_":
                current_state = "POBOY_3"
            elif feedback == "___yg":
                current_state = "BLOND_3"
            elif feedback == "___yy":
                current_state = "MOLDY_3"
            elif feedback == "__g__":
                current_state = "COMFY_3"
            elif feedback == "__g_y":
                current_state = "IDIOM_3"
            elif feedback == "__gg_":
                current_state = "CHILI_3"
            elif feedback == "__ggg":
                current_state = "CHILD_3"
            elif feedback == "__ggy":
                current_state = "DOILY_3"
            elif feedback == "__gy_":
                current_state = "FLICK_3"
            elif feedback == "__gyg":
                current_state = "BLIND_3"
            elif feedback == "__y__":
                current_state = "NYMPH_3"
            elif feedback == "__y_g":
                current_state = "BIPOD_3"
            elif feedback == "__y_y":
                current_state = "DEVON_3"
            elif feedback == "__yg_":
                current_state = "ABLOW_3"
            elif feedback == "__ygy":
                current_state = "DILLY_3"
            elif feedback == "__yy_":
                current_state = "COMFY_3"
            elif feedback == "__yyg":
                current_state = "LIPID_3"
            elif feedback == "_g___":
                current_state = "BUMPH_3"
            elif feedback == "_g__y":
                current_state = "DUMMY_3"
            elif feedback == "_g_g_":
                current_state = "BULLY_3"
            elif feedback == "_g_gy":
                current_state = "DULLY_3"
            elif feedback == "_g_y_":
                current_state = "BULKY_3"
            elif feedback == "_gg__":
                current_state = "JUICY_3"
            elif feedback == "_ggg_":
                current_state = "QUILL_3"
            elif feedback == "_gggg":
                current_state = "BUILD_3"
            elif feedback == "_gy__":
                current_state = "CUBIC_3"
            elif feedback == "_gy_g":
                current_state = "CUPID_3"
            elif feedback == "_gyy_":
                current_state = "PUPIL_3"
            elif feedback == "_gyyg":
                current_state = "LUCID_3"
            elif feedback == "_y___":
                current_state = "COPEN_3"
            elif feedback == "_y__g":
                current_state = "BUMPH_3"
            elif feedback == "_y_gg":
                current_state = "ACMES_3"
            elif feedback == "_y_y_":
                current_state = "PLUCK_3"
            elif feedback == "_y_yg":
                current_state = "CLOUD_3"
            elif feedback == "_yg__":
                current_state = "OPIUM_3"
            elif feedback == "_yy__":
                current_state = "UNHIP_3"
            elif feedback == "_yy_g":
                current_state = "UNDID_3"
            elif feedback == "_yyyg":
                current_state = "FLUID_3"
            elif feedback == "g____":
                current_state = "GOOFY_3"
            elif feedback == "g___y":
                current_state = "GOODY_3"
            elif feedback == "g__g_":
                current_state = "GOLLY_3"
            elif feedback == "g__gy":
                current_state = "GODLY_3"
            elif feedback == "g__y_":
                current_state = "GLOOM_3"
            elif feedback == "g_g__":
                current_state = "GOING_3"
            elif feedback == "g_y__":
                current_state = "GIZMO_3"
            elif feedback == "g_y_y":
                current_state = "GIDDY_3"
            elif feedback == "gg___":
                current_state = "AMBAN_3"
            elif feedback == "gg_g_":
                current_state = "GULLY_3"
            elif feedback == "gg_y_":
                current_state = "GULCH_3"
            elif feedback == "gy_y_":
                current_state = "GHOUL_3"
            elif feedback == "y____":
                current_state = "BOGGY_3"
            elif feedback == "y___y":
                current_state = "DODGY_3"
            elif feedback == "y__y_":
                current_state = "LOGON_3"
            elif feedback == "y_g__":
                current_state = "BICCY_3"
            elif feedback == "y_g_y":
                current_state = "DOING_3"
            elif feedback == "y_gy_":
                current_state = "BACCY_3"
            elif feedback == "y_y__":
                current_state = "BINGO_3"
            elif feedback == "y_y_y":
                current_state = "DINGO_3"
            elif feedback == "y_yy_":
                current_state = "LINGO_3"
            elif feedback == "yg___":
                current_state = "ABHOR_3"
            elif feedback == "yg__y":
                current_state = "AFLAJ_3"
            elif feedback == "yg_y_":
                current_state = "BULGY_3"
            elif feedback == "ygg__":
                current_state = "CUING_3"
            elif feedback == "ygy__":
                current_state = "FUNGI_3"
            elif feedback == "yy___":
                current_state = "BOUGH_3"
            elif feedback == "yy__y":
                current_state = "DOUGH_3"
            elif feedback == "yy_y_":
                current_state = "CLUNG_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GULCH_2":
            if feedback == "_____":
                current_state = "ADMIN_3"
            elif feedback == "___g_":
                current_state = "DANCE_3"
            elif feedback == "___y_":
                current_state = "CANOE_3"
            elif feedback == "___yy":
                current_state = "CACHE_3"
            elif feedback == "__g__":
                current_state = "VALVE_3"
            elif feedback == "__g_y":
                current_state = "HALVE_3"
            elif feedback == "__gy_":
                current_state = "CALVE_3"
            elif feedback == "__y__":
                current_state = "ABYSM_3"
            elif feedback == "__yg_":
                current_state = "LANCE_3"
            elif feedback == "__yy_":
                current_state = "CABLE_3"
            elif feedback == "_y___":
                current_state = "MAUVE_3"
            elif feedback == "_yg__":
                current_state = "VALUE_3"
            elif feedback == "g____":
                current_state = "GAFFE_3"
            elif feedback == "g_y__":
                current_state = "GABLE_3"
            elif feedback == "gy___":
                current_state = "GAUGE_3"
            elif feedback == "y____":
                current_state = "BADGE_3"
            elif feedback == "y__y_":
                current_state = "CADGE_3"
            elif feedback == "y_y__":
                current_state = "EAGLE_3"
            elif feedback == "yy___":
                current_state = "VAGUE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GUNKY_4":
            if feedback == "_____":
                current_state = "BOXER_5"
            elif feedback == "____y":
                current_state = "FOYER_5"
            elif feedback == "___y_":
                current_state = "JOKER_5"
            elif feedback == "__g__":
                current_state = "BONER_5"
            elif feedback == "g____":
                current_state = "GOFER_5"
            elif feedback == "g_g__":
                current_state = "GONER_5"
            elif feedback == "y____":
                current_state = "ROGER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "GUSTY_4":
            if feedback == "_gggg":
                current_state = "MUSTY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HAIKU_3":
            if feedback == "gg___":
                current_state = "HALAL_4"
            elif feedback == "yg__y":
                current_state = "LAUGH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HAMMY_3":
            if feedback == "gg__g":
                current_state = "HAPPY_4"
            elif feedback == "yg__y":
                current_state = "YAHOO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HARSH_2":
            if feedback == "_gggg":
                current_state = "MARSH_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HAVOC_3":
            if feedback == "yg_yy":
                current_state = "MACHO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HIDER_4":
            if feedback == "_gggg":
                current_state = "RIDER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HIJAB_3":
            if feedback == "_g_y_":
                current_state = "PIZZA_4"
            elif feedback == "_y_y_":
                current_state = "UMAMI_4"
            elif feedback == "yy_y_":
                current_state = "KHAKI_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HIMBO_2":
            if feedback == "_____":
                current_state = "GUTSY_3"
            elif feedback == "____g":
                current_state = "NUTSO_3"
            elif feedback == "____y":
                current_state = "JOUST_3"
            elif feedback == "___yy":
                current_state = "BOOST_3"
            elif feedback == "_g___":
                current_state = "DITSY_3"
            elif feedback == "_g_y_":
                current_state = "BITSY_3"
            elif feedback == "_gy__":
                current_state = "MIDST_3"
            elif feedback == "_y__y":
                current_state = "FOIST_3"
            elif feedback == "_yy_y":
                current_state = "MOIST_3"
            elif feedback == "gy__y":
                current_state = "HOIST_3"
            elif feedback == "y___y":
                current_state = "GHOST_3"
            elif feedback == "yy___":
                current_state = "WHIST_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HITCH_4":
            if feedback == "_gggg":
                current_state = "PITCH_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HOARY_3":
            if feedback == "_ygg_":
                current_state = "AMARO_4"
            elif feedback == "_yggg":
                current_state = "OVARY_4"
            elif feedback == "_yyy_":
                current_state = "ARMOR_4"
            elif feedback == "yggy_":
                current_state = "ROACH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HOKUM_2":
            if feedback == "_____":
                current_state = "TRILL_3"
            elif feedback == "___y_":
                current_state = "TRULY_3"
            elif feedback == "___yy":
                current_state = "TRUMP_3"
            elif feedback == "__y__":
                current_state = "TRICK_3"
            elif feedback == "__yy_":
                current_state = "TRUCK_3"
            elif feedback == "_y___":
                current_state = "TROLL_3"
            elif feedback == "_y__y":
                current_state = "TROMP_3"
            elif feedback == "_y_g_":
                current_state = "TROUT_3"
            elif feedback == "_y_y_":
                current_state = "TUTOR_3"
            elif feedback == "_y_yy":
                current_state = "TUMOR_3"
            elif feedback == "y____":
                current_state = "THIRD_3"
            elif feedback == "y__y_":
                current_state = "TRUTH_3"
            elif feedback == "yy___":
                current_state = "THORN_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HONED_2":
            if feedback == "___g_":
                current_state = "TWEET_3"
            elif feedback == "___gg":
                current_state = "TWEED_3"
            elif feedback == "___y_":
                current_state = "TEMPT_3"
            elif feedback == "___yg":
                current_state = "TEPID_3"
            elif feedback == "___yy":
                current_state = "TEDDY_3"
            elif feedback == "__gg_":
                current_state = "TENET_3"
            elif feedback == "__yg_":
                current_state = "TWEEN_3"
            elif feedback == "__yy_":
                current_state = "TEENY_3"
            elif feedback == "_g_g_":
                current_state = "TOTEM_3"
            elif feedback == "_ggg_":
                current_state = "TONEY_3"
            elif feedback == "_gyg_":
                current_state = "TOKEN_3"
            elif feedback == "_y_y_":
                current_state = "TEMPO_3"
            elif feedback == "y__g_":
                current_state = "THIEF_3"
            elif feedback == "y__y_":
                current_state = "TEETH_3"
            elif feedback == "y_gy_":
                current_state = "TENTH_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HONKY_2":
            if feedback == "_____":
                current_state = "SPURT_3"
            elif feedback == "____g":
                current_state = "RUSTY_3"
            elif feedback == "___y_":
                current_state = "SKIRT_3"
            elif feedback == "_y___":
                current_state = "SPORT_3"
            elif feedback == "_y__g":
                current_state = "STORY_3"
            elif feedback == "_y_y_":
                current_state = "STORK_3"
            elif feedback == "_yy__":
                current_state = "SNORT_3"
            elif feedback == "y____":
                current_state = "SHIRT_3"
            elif feedback == "yy___":
                current_state = "SHORT_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HOOCH_4":
            if feedback == "ggg__":
                current_state = "HOOKY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HOTEL_3":
            if feedback == "__ggg":
                current_state = "BETEL_4"
            elif feedback == "__ygy":
                current_state = "FLEET_4"
            elif feedback == "_gggg":
                current_state = "MOTEL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HOUSE_3":
            if feedback == "_gggg":
                current_state = "MOUSE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HOWDY_3":
            if feedback == "_g_g_":
                current_state = "CONDO_4"
            elif feedback == "_g_gg":
                current_state = "MOODY_4"
            elif feedback == "_g_yg":
                current_state = "DOOZY_4"
            elif feedback == "_gggg":
                current_state = "DOWDY_4"
            elif feedback == "_ggyg":
                current_state = "DOWNY_4"
            elif feedback == "_gygg":
                current_state = "WOODY_4"
            elif feedback == "gg_gg":
                current_state = "HOODY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HUFFY_4":
            if feedback == "gg__g":
                current_state = "HUNKY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "HUMUS_4":
            if feedback == "ygy_y":
                current_state = "MUSHY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "IMPEL_4":
            if feedback == "y_ygg":
                current_state = "PIXEL_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "INCEL_3":
            if feedback == "_g_gg":
                current_state = "KNEEL_4"
            elif feedback == "_y_gg":
                current_state = "NOVEL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "INFER_4":
            if feedback == "yy_yy":
                current_state = "REIGN_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "INPUT_3":
            if feedback == "_g_gg":
                current_state = "UNCUT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ISLET_3":
            if feedback == "_yyyg":
                current_state = "SMELT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ISSUE_3":
            if feedback == "yy__g":
                current_state = "SIEVE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "JAUNT_4":
            if feedback == "_gggg":
                current_state = "VAUNT_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "JAZZY_4":
            if feedback == "_g__g":
                current_state = "YAPPY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "JETTY_3":
            if feedback == "_g_g_":
                current_state = "BENTO_4"
            elif feedback == "_g_gg":
                current_state = "HEFTY_4"
            elif feedback == "_gg__":
                current_state = "FETCH_4"
            elif feedback == "_gy__":
                current_state = "BEGOT_4"
            elif feedback == "_yy__":
                current_state = "EVENT_4"
            elif feedback == "yyy__":
                current_state = "EJECT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "JOINT_3":
            if feedback == "_gggg":
                current_state = "POINT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "JUICY_3":
            if feedback == "_ggg_":
                current_state = "QUICK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "KACHA_3":
            if feedback == "_y___":
                current_state = "WEAVE_4"
            elif feedback == "_y__y":
                current_state = "AMAZE_4"
            elif feedback == "_y_y_":
                current_state = "HEAVE_4"
            elif feedback == "_yy__":
                current_state = "PEACE_4"
            elif feedback == "_yy_y":
                current_state = "APACE_4"
            elif feedback == "_yyy_":
                current_state = "CHAFE_4"
            elif feedback == "yy___":
                current_state = "QUAKE_4"
            elif feedback == "yy__y":
                current_state = "AWAKE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "KEMPS_2":
            if feedback == "_y___":
                current_state = "TATER_3"
            elif feedback == "_y_y_":
                current_state = "TAPER_3"
            elif feedback == "_yg__":
                current_state = "TAMER_3"
            elif feedback == "yy___":
                current_state = "TAKER_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "KLETT_2":
            if feedback == "__yg_":
                current_state = "SPATE_3"
            elif feedback == "__ygy":
                current_state = "STATE_3"
            elif feedback == "__yy_":
                current_state = "STAGE_3"
            elif feedback == "_gyg_":
                current_state = "SLATE_3"
            elif feedback == "_yyy_":
                current_state = "STALE_3"
            elif feedback == "y_yg_":
                current_state = "SKATE_3"
            elif feedback == "y_yy_":
                current_state = "STAKE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "KNACK_3":
            if feedback == "_gyy_":
                current_state = "UNCAP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "KVELL_3":
            if feedback == "__ggg":
                current_state = "QUELL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LABEL_3":
            if feedback == "gg_g_":
                current_state = "LADEN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LAYUP_3":
            if feedback == "_gg__":
                current_state = "KAYAK_4"
            elif feedback == "_ggy_":
                current_state = "BAYOU_4"
            elif feedback == "ygg__":
                current_state = "GAYLY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LEAFY_3":
            if feedback == "ggg__":
                current_state = "LEACH_4"
            elif feedback == "ggg_g":
                current_state = "LEAKY_4"
            elif feedback == "ygyy_":
                current_state = "FELLA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LEARN_3":
            if feedback == "_ggg_":
                current_state = "WEARY_4"
            elif feedback == "_gggg":
                current_state = "YEARN_4"
            elif feedback == "_ggy_":
                current_state = "REACH_4"
            elif feedback == "yggg_":
                current_state = "PEARL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LEAVE_3":
            if feedback == "y_g_g":
                current_state = "WHALE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LEMED_2":
            if feedback == "___g_":
                current_state = "FACET_3"
            elif feedback == "___gg":
                current_state = "GATED_3"
            elif feedback == "___gy":
                current_state = "CADET_3"
            elif feedback == "__yg_":
                current_state = "MATEY_3"
            elif feedback == "_y_g_":
                current_state = "EATEN_3"
            elif feedback == "g__g_":
                current_state = "LATEX_3"
            elif feedback == "y__g_":
                current_state = "VALET_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LIKEN_3":
            if feedback == "g__gg":
                current_state = "LUMEN_4"
            elif feedback == "gg_gg":
                current_state = "LIVEN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LINGO_3":
            if feedback == "gy_yy":
                current_state = "LOGIC_4"
            elif feedback == "gyyyy":
                current_state = "LOGIN_4"
            elif feedback == "yg_y_":
                current_state = "VIGIL_4"
            elif feedback == "yy_yg":
                current_state = "IGLOO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LINKY_2":
            if feedback == "_____":
                current_state = "TABOO_3"
            elif feedback == "____g":
                current_state = "ABAFT_3"
            elif feedback == "___gg":
                current_state = "TACKY_3"
            elif feedback == "__g__":
                current_state = "TANGO_3"
            elif feedback == "__g_g":
                current_state = "TANGY_3"
            elif feedback == "__y__":
                current_state = "TAUNT_3"
            elif feedback == "__y_g":
                current_state = "TAWNY_3"
            elif feedback == "_y___":
                current_state = "TACIT_3"
            elif feedback == "_yy__":
                current_state = "TAINT_3"
            elif feedback == "y___g":
                current_state = "TALLY_3"
            elif feedback == "y__gg":
                current_state = "TALKY_3"
            elif feedback == "y_y__":
                current_state = "TALON_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LIPID_3":
            if feedback == "gg_gg":
                current_state = "LIVID_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LOAMY_3":
            if feedback == "ggy_y":
                current_state = "LOYAL_4"
            elif feedback == "ygg__":
                current_state = "KOALA_4"
            elif feedback == "ygy__":
                current_state = "DOULA_4"
            elif feedback == "ygyy_":
                current_state = "MODAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LOATH_3":
            if feedback == "yyyy_":
                current_state = "OCTAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LOGIN_2":
            if feedback == "_____":
                current_state = "EMCEE_3"
            elif feedback == "____y":
                current_state = "CHEEP_3"
            elif feedback == "___g_":
                current_state = "PIXIE_3"
            elif feedback == "___gy":
                current_state = "INDIE_3"
            elif feedback == "___y_":
                current_state = "DUMPS_3"
            elif feedback == "___yy":
                current_state = "WINCE_3"
            elif feedback == "__g__":
                current_state = "FUGUE_3"
            elif feedback == "__y__":
                current_state = "BUMPH_3"
            elif feedback == "__y_y":
                current_state = "NUDGE_3"
            elif feedback == "__ygy":
                current_state = "GENIE_3"
            elif feedback == "__yy_":
                current_state = "BEIGE_3"
            elif feedback == "__yyy":
                current_state = "BINGE_3"
            elif feedback == "_g___":
                current_state = "BOCCE_3"
            elif feedback == "_g_g_":
                current_state = "MOVIE_3"
            elif feedback == "_g_y_":
                current_state = "VOICE_3"
            elif feedback == "_gg__":
                current_state = "VOGUE_3"
            elif feedback == "_ggg_":
                current_state = "BOGIE_3"
            elif feedback == "_gy__":
                current_state = "DODGE_3"
            elif feedback == "_y___":
                current_state = "CHOKE_3"
            elif feedback == "_y__y":
                current_state = "OUNCE_3"
            elif feedback == "_y_y_":
                current_state = "BIOME_3"
            elif feedback == "_y_yy":
                current_state = "OPINE_3"
            elif feedback == "_yy__":
                current_state = "GEODE_3"
            elif feedback == "_yy_y":
                current_state = "GNOME_3"
            elif feedback == "g____":
                current_state = "LEVEE_3"
            elif feedback == "g_y__":
                current_state = "LEDGE_3"
            elif feedback == "g_y_y":
                current_state = "LUNGE_3"
            elif feedback == "g_yy_":
                current_state = "LIEGE_3"
            elif feedback == "gg___":
                current_state = "LOUPE_3"
            elif feedback == "ggy__":
                current_state = "LODGE_3"
            elif feedback == "y____":
                current_state = "DUMPY_3"
            elif feedback == "y___y":
                current_state = "UNCLE_3"
            elif feedback == "y__g_":
                current_state = "BELIE_3"
            elif feedback == "y__y_":
                current_state = "CHILE_3"
            elif feedback == "y_g__":
                current_state = "BUGLE_3"
            elif feedback == "y_y__":
                current_state = "BULGE_3"
            elif feedback == "y_yy_":
                current_state = "GLIDE_3"
            elif feedback == "yg___":
                current_state = "BOULE_3"
            elif feedback == "yg__y":
                current_state = "NOBLE_3"
            elif feedback == "yg_y_":
                current_state = "VOILE_3"
            elif feedback == "yy___":
                current_state = "BECAP_3"
            elif feedback == "yy__y":
                current_state = "CLONE_3"
            elif feedback == "yy_g_":
                current_state = "OLDIE_3"
            elif feedback == "yy_y_":
                current_state = "OLIVE_3"
            elif feedback == "yyy__":
                current_state = "GLOBE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LORDY_3":
            if feedback == "ggg_g":
                current_state = "LORRY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LOWLY_3":
            if feedback == "_g_gg":
                current_state = "COYLY_4"
            elif feedback == "_gggg":
                current_state = "JOWLY_4"
            elif feedback == "_gygg":
                current_state = "WOOLY_4"
            elif feedback == "gg_gg":
                current_state = "LOLLY_4"
            elif feedback == "yg_gg":
                current_state = "FEHME_4"
            elif feedback == "yy_g_":
                current_state = "KNOLL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LUPIN_2":
            if feedback == "_____":
                current_state = "MASSE_3"
            elif feedback == "____y":
                current_state = "MANSE_3"
            elif feedback == "__y__":
                current_state = "PASSE_3"
            elif feedback == "_y___":
                current_state = "CAUSE_3"
            elif feedback == "_yy__":
                current_state = "PAUSE_3"
            elif feedback == "g_g__":
                current_state = "LAPSE_3"
            elif feedback == "y____":
                current_state = "FALSE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "LYMPH_2":
            if feedback == "_____":
                current_state = "OAKEN_3"
            elif feedback == "____y":
                current_state = "HAVEN_3"
            elif feedback == "___y_":
                current_state = "PAEAN_3"
            elif feedback == "__g__":
                current_state = "CAMEO_3"
            elif feedback == "__y__":
                current_state = "MAVEN_3"
            elif feedback == "_y___":
                current_state = "CAGEY_3"
            elif feedback == "_yg__":
                current_state = "GAMEY_3"
            elif feedback == "g____":
                current_state = "LABEL_3"
            elif feedback == "g__y_":
                current_state = "LAPEL_3"
            elif feedback == "gy___":
                current_state = "LACEY_3"
            elif feedback == "y____":
                current_state = "BAGEL_3"
            elif feedback == "y___y":
                current_state = "HAZEL_3"
            elif feedback == "y__y_":
                current_state = "PANEL_3"
            elif feedback == "y_g__":
                current_state = "CAMEL_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MAGIC_3":
            if feedback == "_g__y":
                current_state = "WACKO_4"
            elif feedback == "gg__y":
                current_state = "MACAW_4"
            elif feedback == "gg_gg":
                current_state = "MALIC_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MAKER_3":
            if feedback == "yg_gy":
                current_state = "RAMEN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MAMBA_3":
            if feedback == "_g___":
                current_state = "KAZOO_4"
            elif feedback == "_g__g":
                current_state = "KAPPA_4"
            elif feedback == "_g__y":
                current_state = "PAPAL_4"
            elif feedback == "_g_y_":
                current_state = "KABOB_4"
            elif feedback == "_g_yg":
                current_state = "BABKA_4"
            elif feedback == "gg__g":
                current_state = "MAFIA_4"
            elif feedback == "ggg_g":
                current_state = "MAMMA_4"
            elif feedback == "gggg_":
                current_state = "MAMBO_4"
            elif feedback == "ggy__":
                current_state = "MAXIM_4"
            elif feedback == "ggy_g":
                current_state = "MAGMA_4"
            elif feedback == "ygg_g":
                current_state = "GAMMA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MANIC_3":
            if feedback == "_gggg":
                current_state = "PANIC_4"
            elif feedback == "_gy_y":
                current_state = "BACON_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MANLY_3":
            if feedback == "_gg_g":
                current_state = "JANKY_4"
            elif feedback == "_gggg":
                current_state = "WANLY_4"
            elif feedback == "_ggyg":
                current_state = "LANKY_4"
            elif feedback == "_gy_g":
                current_state = "NAGGY_4"
            elif feedback == "ggg_g":
                current_state = "MANGY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MEDAL_2":
            if feedback == "_g_g_":
                current_state = "BEGAN_3"
            elif feedback == "_g_gg":
                current_state = "APING_3"
            elif feedback == "_g_gy":
                current_state = "BELAY_3"
            elif feedback == "_g_y_":
                current_state = "BEACH_3"
            elif feedback == "_g_yy":
                current_state = "LEAFY_3"
            elif feedback == "_gggg":
                current_state = "PEDAL_3"
            elif feedback == "_gyg_":
                current_state = "DECAF_3"
            elif feedback == "_gygg":
                current_state = "DECAL_3"
            elif feedback == "_gygy":
                current_state = "DELAY_3"
            elif feedback == "_gyy_":
                current_state = "BEADY_3"
            elif feedback == "_y_g_":
                current_state = "CHEAP_3"
            elif feedback == "_y_gg":
                current_state = "EQUAL_3"
            elif feedback == "_y_gy":
                current_state = "CLEAN_3"
            elif feedback == "_y_y_":
                current_state = "ANNEX_3"
            elif feedback == "_y_yg":
                current_state = "ANGEL_3"
            elif feedback == "_y_yy":
                current_state = "ALIEN_3"
            elif feedback == "_yyg_":
                current_state = "AHEAD_3"
            elif feedback == "_yygg":
                current_state = "IDEAL_3"
            elif feedback == "_yygy":
                current_state = "PLEAD_3"
            elif feedback == "_yyy_":
                current_state = "ADIEU_3"
            elif feedback == "gg_y_":
                current_state = "MECCA_3"
            elif feedback == "gg_yy":
                current_state = "MEALY_3"
            elif feedback == "gggy_":
                current_state = "MEDIA_3"
            elif feedback == "yg_yy":
                current_state = "LEMMA_3"
            elif feedback == "yy_gy":
                current_state = "GLEAM_3"
            elif feedback == "yy_y_":
                current_state = "ENEMA_3"
            elif feedback == "yy_yg":
                current_state = "EMAIL_3"
            elif feedback == "yyyy_":
                current_state = "AMEND_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MERGE_3":
            if feedback == "_gggg":
                current_state = "VERGE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MESHY_3":
            if feedback == "_gg_g":
                current_state = "PESKY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "METRO_3":
            if feedback == "_gggg":
                current_state = "RETRO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MICRO_3":
            if feedback == "__gyy":
                current_state = "OCCUR_4"
            elif feedback == "__yyy":
                current_state = "FROCK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MILKO_2":
            if feedback == "____y":
                current_state = "STONE_3"
            elif feedback == "___gy":
                current_state = "STOKE_3"
            elif feedback == "__y__":
                current_state = "STELE_3"
            elif feedback == "__y_y":
                current_state = "STOLE_3"
            elif feedback == "_g___":
                current_state = "PISTE_3"
            elif feedback == "_y___":
                current_state = "SPITE_3"
            elif feedback == "_yy__":
                current_state = "STILE_3"
            elif feedback == "y___y":
                current_state = "SMOTE_3"
            elif feedback == "yy___":
                current_state = "SMITE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MINOR_2":
            if feedback == "____g":
                current_state = "TRUER_3"
            elif feedback == "____y":
                current_state = "TWERK_3"
            elif feedback == "___yg":
                current_state = "TOWER_3"
            elif feedback == "__g_g":
                current_state = "TUNER_3"
            elif feedback == "__ggg":
                current_state = "TENOR_3"
            elif feedback == "__gyg":
                current_state = "TONER_3"
            elif feedback == "__y_y":
                current_state = "TREND_3"
            elif feedback == "_g__g":
                current_state = "TIGER_3"
            elif feedback == "_y__g":
                current_state = "THEIR_3"
            elif feedback == "_y__y":
                current_state = "TRIED_3"
            elif feedback == "yg__g":
                current_state = "TIMER_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MINTY_3":
            if feedback == "_ggg_":
                current_state = "NINTH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MINUS_3":
            if feedback == "__ggg":
                current_state = "BONUS_4"
            elif feedback == "_gggg":
                current_state = "SINUS_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MISER_3":
            if feedback == "__ggg":
                current_state = "LOSER_4"
            elif feedback == "__ygg":
                current_state = "SOBER_4"
            elif feedback == "_gggg":
                current_state = "RISER_4"
            elif feedback == "_gggy":
                current_state = "RISEN_4"
            elif feedback == "_yygg":
                current_state = "SKIER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MOCHA_3":
            if feedback == "_gyyy":
                current_state = "POACH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MOLAR_3":
            if feedback == "_gggg":
                current_state = "POLAR_4"
            elif feedback == "_gygy":
                current_state = "ROYAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MOPED_3":
            if feedback == "___gg":
                current_state = "IVIED_4"
            elif feedback == "__ggg":
                current_state = "BIPED_4"
            elif feedback == "_g_gy":
                current_state = "CODEX_4"
            elif feedback == "_y_gy":
                current_state = "VIDEO_4"
            elif feedback == "gg_gy":
                current_state = "MODEM_4"
            elif feedback == "y__gg":
                current_state = "EMBED_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MOTOR_3":
            if feedback == "_gggg":
                current_state = "ROTOR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MOURN_3":
            if feedback == "_g_yg":
                current_state = "ROBIN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MOVIE_3":
            if feedback == "gg_gg":
                current_state = "MOXIE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MULCH_2":
            if feedback == "_____":
                current_state = "ABYSS_3"
            elif feedback == "____g":
                current_state = "AWASH_3"
            elif feedback == "__y__":
                current_state = "FLASK_3"
            elif feedback == "__y_g":
                current_state = "FLASH_3"
            elif feedback == "__yy_":
                current_state = "CLASP_3"
            elif feedback == "__yyg":
                current_state = "CLASH_3"
            elif feedback == "_g___":
                current_state = "QUASI_3"
            elif feedback == "_g__g":
                current_state = "QUASH_3"
            elif feedback == "y____":
                current_state = "AMASS_3"
            elif feedback == "y___g":
                current_state = "SMASH_3"
            elif feedback == "y__yy":
                current_state = "CHASM_3"
            elif feedback == "y_y__":
                current_state = "PLASM_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MUMMY_4":
            if feedback == "_gggg":
                current_state = "YUMMY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "MURAL_3":
            if feedback == "_gggg":
                current_state = "RURAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "NAGGY_4":
            if feedback == "gg__g":
                current_state = "NAPPY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "NERDY_3":
            if feedback == "ggg_g":
                current_state = "NERVY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "NEWEL_2":
            if feedback == "___g_":
                current_state = "SHIED_3"
            elif feedback == "___gg":
                current_state = "SPIEL_3"
            elif feedback == "_g___":
                current_state = "MESHY_3"
            elif feedback == "_g__y":
                current_state = "LEXIS_3"
            elif feedback == "_g_g_":
                current_state = "FECES_3"
            elif feedback == "_g_y_":
                current_state = "SEEDY_3"
            elif feedback == "_y___":
                current_state = "SHEIK_3"
            elif feedback == "_y__g":
                current_state = "APHID_3"
            elif feedback == "_y__y":
                current_state = "SHELF_3"
            elif feedback == "_y_g_":
                current_state = "SHEEP_3"
            elif feedback == "_y_gy":
                current_state = "SLEEK_3"
            elif feedback == "_yy_g":
                current_state = "SWELL_3"
            elif feedback == "_yyg_":
                current_state = "SWEEP_3"
            elif feedback == "g__g_":
                current_state = "NOSEY_3"
            elif feedback == "gg___":
                current_state = "NEXUS_3"
            elif feedback == "y_yg_":
                current_state = "SINEW_3"
            elif feedback == "yg___":
                current_state = "GENUS_3"
            elif feedback == "yg_g_":
                current_state = "SEVEN_3"
            elif feedback == "yy___":
                current_state = "SKEIN_3"
            elif feedback == "yy_g_":
                current_state = "SHEEN_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "NODAL_3":
            if feedback == "yg_gg":
                current_state = "ZONAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "NOISE_3":
            if feedback == "_g_gg":
                current_state = "POSSE_4"
            elif feedback == "_gggg":
                current_state = "POISE_4"
            elif feedback == "_y_gg":
                current_state = "OBESE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "NORTH_3":
            if feedback == "_gggg":
                current_state = "WORTH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "NURSE_3":
            if feedback == "_gggg":
                current_state = "PURSE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "NUTTY_3":
            if feedback == "yy_gg":
                current_state = "UNITY_4"
            elif feedback == "yyg__":
                current_state = "UNTIL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "NYMPH_3":
            if feedback == "_____":
                current_state = "CIVIC_4"
            elif feedback == "___gy":
                current_state = "HIPPO_4"
            elif feedback == "__g__":
                current_state = "COMIC_4"
            elif feedback == "__y_y":
                current_state = "MOCHI_4"
            elif feedback == "_y___":
                current_state = "FIZZY_4"
            elif feedback == "_y_g_":
                current_state = "ZIPPY_4"
            elif feedback == "_y_gy":
                current_state = "HIPPY_4"
            elif feedback == "_y_y_":
                current_state = "PICKY_4"
            elif feedback == "_yg__":
                current_state = "JIMMY_4"
            elif feedback == "_ygg_":
                current_state = "WIMPY_4"
            elif feedback == "gy___":
                current_state = "NINNY_4"
            elif feedback == "gy_g_":
                current_state = "NIPPY_4"
            elif feedback == "y____":
                current_state = "CONIC_4"
            elif feedback == "y___g":
                current_state = "AFLOW_4"
            elif feedback == "y__yg":
                current_state = "PINCH_4"
            elif feedback == "y_y__":
                current_state = "MINIM_4"
            elif feedback == "yg___":
                current_state = "CYNIC_4"
            elif feedback == "yy___":
                current_state = "KINKY_4"
            elif feedback == "yy__y":
                current_state = "HINKY_4"
            elif feedback == "yy_y_":
                current_state = "PINKY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "OAKEN_3":
            if feedback == "_g_g_":
                current_state = "JADED_4"
            elif feedback == "_g_gg":
                current_state = "WAXEN_4"
            elif feedback == "_ggg_":
                current_state = "BAKED_4"
            elif feedback == "_gggg":
                current_state = "WAKEN_4"
            elif feedback == "_gggy":
                current_state = "NAKED_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "OCHER_3":
            if feedback == "yy_yy":
                current_state = "RECON_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ODDER_3":
            if feedback == "g_ggg":
                current_state = "ORDER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "OFFER_3":
            if feedback == "g__gg":
                current_state = "OWNER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "OPINE_3":
            if feedback == "g_ggg":
                current_state = "OVINE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "OPIUM_3":
            if feedback == "__gy_":
                current_state = "UNIFY_4"
            elif feedback == "y_gy_":
                current_state = "UNION_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "OTHER_3":
            if feedback == "gg_gg":
                current_state = "OTTER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "OUNCE_3":
            if feedback == "g_y_g":
                current_state = "OZONE_4"
            elif feedback == "y_y_g":
                current_state = "PHONE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "OUTGO_3":
            if feedback == "ygy__":
                current_state = "QUOTH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PANTY_3":
            if feedback == "gg_gg":
                current_state = "PATTY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PARER_3":
            if feedback == "_gggg":
                current_state = "RARER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PARRY_3":
            if feedback == "_gg_g":
                current_state = "HARDY_4"
            elif feedback == "_gggg":
                current_state = "HARRY_4"
            elif feedback == "ygg_g":
                current_state = "HARPY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PASTE_3":
            if feedback == "_gggg":
                current_state = "WASTE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PATSY_2":
            if feedback == "_gyg_":
                current_state = "WAIST_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PERIL_3":
            if feedback == "gyg__":
                current_state = "PURER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PHISH_3":
            if feedback == "_ggg_":
                current_state = "WHISK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PHLOX_3":
            if feedback == "__gg_":
                current_state = "BELOW_4"
            elif feedback == "__gy_":
                current_state = "CELLO_4"
            elif feedback == "__y__":
                current_state = "FLECK_4"
            elif feedback == "__yg_":
                current_state = "ELBOW_4"
            elif feedback == "_gy__":
                current_state = "WHELK_4"
            elif feedback == "_yg__":
                current_state = "BELCH_4"
            elif feedback == "_yg_g":
                current_state = "HELIX_4"
            elif feedback == "_ygy_":
                current_state = "HELLO_4"
            elif feedback == "_yy__":
                current_state = "LEECH_4"
            elif feedback == "ygy__":
                current_state = "WHELP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PILAF_3":
            if feedback == "_ggy_":
                current_state = "VILLA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PILED_2":
            if feedback == "___g_":
                current_state = "COMET_3"
            elif feedback == "___gy":
                current_state = "DUVET_3"
            elif feedback == "___y_":
                current_state = "JETTY_3"
            elif feedback == "___yy":
                current_state = "DEBUT_3"
            elif feedback == "__gy_":
                current_state = "MELTY_3"
            elif feedback == "__gyy":
                current_state = "VELDT_3"
            elif feedback == "__yg_":
                current_state = "HOTEL_3"
            elif feedback == "__yy_":
                current_state = "EXULT_3"
            elif feedback == "__yyy":
                current_state = "DWELT_3"
            elif feedback == "_g_g_":
                current_state = "CIVET_3"
            elif feedback == "_g_gy":
                current_state = "BIDET_3"
            elif feedback == "_g_y_":
                current_state = "EIGHT_3"
            elif feedback == "_ggg_":
                current_state = "FILET_3"
            elif feedback == "_y_g_":
                current_state = "QUIET_3"
            elif feedback == "_y_y_":
                current_state = "BEFIT_3"
            elif feedback == "_y_yg":
                current_state = "FETID_3"
            elif feedback == "_y_yy":
                current_state = "DEBIT_3"
            elif feedback == "_ygg_":
                current_state = "INLET_3"
            elif feedback == "_yyg_":
                current_state = "INTEL_3"
            elif feedback == "_yyy_":
                current_state = "LEGIT_3"
            elif feedback == "g__y_":
                current_state = "PETTY_3"
            elif feedback == "gg_g_":
                current_state = "PIPET_3"
            elif feedback == "gg_y_":
                current_state = "PIETY_3"
            elif feedback == "gy_y_":
                current_state = "PETIT_3"
            elif feedback == "y__y_":
                current_state = "EMPTY_3"
            elif feedback == "y__yy":
                current_state = "DEPOT_3"
            elif feedback == "y_yy_":
                current_state = "LETUP_3"
            elif feedback == "yy_y_":
                current_state = "INEPT_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PILOT_3":
            if feedback == "_g_gg":
                current_state = "BIGOT_4"
            elif feedback == "gg_gg":
                current_state = "PIVOT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PINCH_2":
            if feedback == "_____":
                current_state = "SWORE_3"
            elif feedback == "____y":
                current_state = "SHORE_3"
            elif feedback == "___y_":
                current_state = "SCORE_3"
            elif feedback == "__y__":
                current_state = "SNORE_3"
            elif feedback == "_y__y":
                current_state = "SHIRE_3"
            elif feedback == "y____":
                current_state = "SPORE_3"
            elif feedback == "yy___":
                current_state = "SPIRE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PINKY_3":
            if feedback == "_g___":
                current_state = "REFIX_4"
            elif feedback == "_g__g":
                current_state = "FIERY_4"
            elif feedback == "_g_y_":
                current_state = "BIKER_4"
            elif feedback == "_gg__":
                current_state = "FINER_4"
            elif feedback == "_gy__":
                current_state = "RIVEN_4"
            elif feedback == "_y___":
                current_state = "BRIEF_4"
            elif feedback == "_y__g":
                current_state = "REIFY_4"
            elif feedback == "_y_y_":
                current_state = "KEFIR_4"
            elif feedback == "_yg__":
                current_state = "INNER_4"
            elif feedback == "_yy__":
                current_state = "INFER_4"
            elif feedback == "gg___":
                current_state = "PIPER_4"
            elif feedback == "gg_y_":
                current_state = "PIKER_4"
            elif feedback == "yg___":
                current_state = "ADVEW_4"
            elif feedback == "ygy__":
                current_state = "RIPEN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PIOUS_3":
            if feedback == "g__yy":
                current_state = "PUSHY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PLANC_2":
            if feedback == "__g__":
                current_state = "DEATH_3"
            elif feedback == "__g_y":
                current_state = "EXACT_3"
            elif feedback == "__gg_":
                current_state = "MEANT_3"
            elif feedback == "__gy_":
                current_state = "SNAFU_3"
            elif feedback == "__gyy":
                current_state = "ENACT_3"
            elif feedback == "__y__":
                current_state = "BEGAT_3"
            elif feedback == "__y_g":
                current_state = "SUMAC_3"
            elif feedback == "__y_y":
                current_state = "CHEAT_3"
            elif feedback == "__yg_":
                current_state = "AGENT_3"
            elif feedback == "__yy_":
                current_state = "UNSAY_3"
            elif feedback == "_gg_y":
                current_state = "SLACK_3"
            elif feedback == "_ggg_":
                current_state = "SLANG_3"
            elif feedback == "_ggy_":
                current_state = "SLAIN_3"
            elif feedback == "_gy__":
                current_state = "BLEAT_3"
            elif feedback == "_gy_y":
                current_state = "CLEAT_3"
            elif feedback == "_yg__":
                current_state = "DEALT_3"
            elif feedback == "_yg_y":
                current_state = "SCALD_3"
            elif feedback == "_ygg_":
                current_state = "LEANT_3"
            elif feedback == "_ygy_":
                current_state = "SNAIL_3"
            elif feedback == "_yy__":
                current_state = "FETAL_3"
            elif feedback == "_yy_y":
                current_state = "ECLAT_3"
            elif feedback == "g_g__":
                current_state = "PEATY_3"
            elif feedback == "ggy__":
                current_state = "PLEAT_3"
            elif feedback == "gyg__":
                current_state = "PSALM_3"
            elif feedback == "gyy__":
                current_state = "PETAL_3"
            elif feedback == "y_g__":
                current_state = "SOAPY_3"
            elif feedback == "y_g_y":
                current_state = "SCAMP_3"
            elif feedback == "y_gg_":
                current_state = "SPANK_3"
            elif feedback == "y_gy_":
                current_state = "SPAWN_3"
            elif feedback == "y_y__":
                current_state = "ADEPT_3"
            elif feedback == "y_y_g":
                current_state = "ASPIC_3"
            elif feedback == "yyg__":
                current_state = "LEAPT_3"
            elif feedback == "yyg_y":
                current_state = "SCALP_3"
            elif feedback == "yyy__":
                current_state = "SPLAY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PLING_2":
            if feedback == "_____":
                current_state = "SHOVE_3"
            elif feedback == "____y":
                current_state = "SEDGE_3"
            elif feedback == "___g_":
                current_state = "SCENE_3"
            elif feedback == "___y_":
                current_state = "ENSUE_3"
            elif feedback == "__g__":
                current_state = "SEIZE_3"
            elif feedback == "__gg_":
                current_state = "SHINE_3"
            elif feedback == "__gy_":
                current_state = "SNIDE_3"
            elif feedback == "__y__":
                current_state = "ISSUE_3"
            elif feedback == "__y_y":
                current_state = "SIEGE_3"
            elif feedback == "__yy_":
                current_state = "SINCE_3"
            elif feedback == "__yyy":
                current_state = "SINGE_3"
            elif feedback == "_gg__":
                current_state = "ADEEM_3"
            elif feedback == "_y___":
                current_state = "SOLVE_3"
            elif feedback == "_yg__":
                current_state = "SMILE_3"
            elif feedback == "_yy__":
                current_state = "SIDLE_3"
            elif feedback == "y____":
                current_state = "SCOPE_3"
            elif feedback == "y_g__":
                current_state = "SPICE_3"
            elif feedback == "y_gg_":
                current_state = "SPINE_3"
            elif feedback == "y_gy_":
                current_state = "SNIPE_3"
            elif feedback == "yg___":
                current_state = "SLOPE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PLOIT_2":
            if feedback == "____g":
                current_state = "CHANT_3"
            elif feedback == "____y":
                current_state = "AUNTY_3"
            elif feedback == "___gg":
                current_state = "ADMIT_3"
            elif feedback == "___gy":
                current_state = "ANTIC_3"
            elif feedback == "___yg":
                current_state = "GIANT_3"
            elif feedback == "___yy":
                current_state = "AGITA_3"
            elif feedback == "__g_g":
                current_state = "ABOUT_3"
            elif feedback == "__g_y":
                current_state = "QUOTA_3"
            elif feedback == "__y_g":
                current_state = "ABBOT_3"
            elif feedback == "__y_y":
                current_state = "GOTTA_3"
            elif feedback == "__yyy":
                current_state = "COATI_3"
            elif feedback == "_gg_g":
                current_state = "ABAFT_3"
            elif feedback == "_gy_g":
                current_state = "ALLOT_3"
            elif feedback == "_y__g":
                current_state = "ADULT_3"
            elif feedback == "_y_yy":
                current_state = "VITAL_3"
            elif feedback == "_yg_y":
                current_state = "ATOLL_3"
            elif feedback == "_yy_y":
                current_state = "LOATH_3"
            elif feedback == "gg__g":
                current_state = "PLANT_3"
            elif feedback == "gg_gg":
                current_state = "PLAIT_3"
            elif feedback == "y___g":
                current_state = "ADAPT_3"
            elif feedback == "y__yg":
                current_state = "INAPT_3"
            elif feedback == "y_g_g":
                current_state = "ADOPT_3"
            elif feedback == "yy__y":
                current_state = "APTLY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PLUCK_3":
            if feedback == "_gg__":
                current_state = "BLUFF_4"
            elif feedback == "_gg_g":
                current_state = "FLUNK_4"
            elif feedback == "_gg_y":
                current_state = "FLUKY_4"
            elif feedback == "_gggg":
                current_state = "CLUCK_4"
            elif feedback == "_ggyg":
                current_state = "CLUNK_4"
            elif feedback == "ggg__":
                current_state = "PLUMB_4"
            elif feedback == "ggg_g":
                current_state = "PLUNK_4"
            elif feedback == "yggy_":
                current_state = "CLUMP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PLUMB_4":
            if feedback == "gggg_":
                current_state = "PLUMP_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PLUNK_2":
            if feedback == "_____":
                current_state = "DISHY_3"
            elif feedback == "____g":
                current_state = "SHOCK_3"
            elif feedback == "____y":
                current_state = "SKIFF_3"
            elif feedback == "___g_":
                current_state = "SHINY_3"
            elif feedback == "___y_":
                current_state = "BISON_3"
            elif feedback == "__g__":
                current_state = "SQUIB_3"
            elif feedback == "__g_g":
                current_state = "SHUCK_3"
            elif feedback == "__gg_":
                current_state = "SOUND_3"
            elif feedback == "__ggg":
                current_state = "SKUNK_3"
            elif feedback == "__gy_":
                current_state = "SNUFF_3"
            elif feedback == "__gyg":
                current_state = "SNUCK_3"
            elif feedback == "__y__":
                current_state = "CHIMB_3"
            elif feedback == "__y_y":
                current_state = "ADSUM_3"
            elif feedback == "__yg_":
                current_state = "SUING_3"
            elif feedback == "__yy_":
                current_state = "MINUS_3"
            elif feedback == "_g___":
                current_state = "SLIMY_3"
            elif feedback == "_g__g":
                current_state = "SLICK_3"
            elif feedback == "_g_g_":
                current_state = "SLING_3"
            elif feedback == "_g_gg":
                current_state = "SLINK_3"
            elif feedback == "_ggg_":
                current_state = "SLUNG_3"
            elif feedback == "_gggg":
                current_state = "SLUNK_3"
            elif feedback == "_y___":
                current_state = "SHILL_3"
            elif feedback == "_y__y":
                current_state = "SILKY_3"
            elif feedback == "_yg__":
                current_state = "SCULL_3"
            elif feedback == "_yg_g":
                current_state = "SKULK_3"
            elif feedback == "_yg_y":
                current_state = "SKULL_3"
            elif feedback == "_yy__":
                current_state = "BOLUS_3"
            elif feedback == "_yy_y":
                current_state = "SULKY_3"
            elif feedback == "g____":
                current_state = "PSYCH_3"
            elif feedback == "g_y__":
                current_state = "PIOUS_3"
            elif feedback == "gy___":
                current_state = "POLIS_3"
            elif feedback == "y____":
                current_state = "SCOOP_3"
            elif feedback == "y___g":
                current_state = "SPOOK_3"
            elif feedback == "y___y":
                current_state = "SKIMP_3"
            elif feedback == "y__g_":
                current_state = "SPINY_3"
            elif feedback == "y__y_":
                current_state = "SNOOP_3"
            elif feedback == "y_g__":
                current_state = "SOUPY_3"
            elif feedback == "y_ggg":
                current_state = "SPUNK_3"
            elif feedback == "y_yy_":
                current_state = "SUNUP_3"
            elif feedback == "yg___":
                current_state = "SLOOP_3"
            elif feedback == "ygg__":
                current_state = "SLUMP_3"
            elif feedback == "yy___":
                current_state = "SPILL_3"
            elif feedback == "yyy__":
                current_state = "LUPUS_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PLUOT_2":
            if feedback == "____g":
                current_state = "CHEEK_3"
            elif feedback == "____y":
                current_state = "STEED_3"
            elif feedback == "___gg":
                current_state = "BESOT_3"
            elif feedback == "___gy":
                current_state = "ETHOS_3"
            elif feedback == "___yg":
                current_state = "ONSET_3"
            elif feedback == "___yy":
                current_state = "STENO_3"
            elif feedback == "__y_g":
                current_state = "UNSET_3"
            elif feedback == "__y_y":
                current_state = "FETUS_3"
            elif feedback == "_g__g":
                current_state = "SLEET_3"
            elif feedback == "_y__g":
                current_state = "ISLET_3"
            elif feedback == "_y__y":
                current_state = "STEEL_3"
            elif feedback == "g__yy":
                current_state = "PESTO_3"
            elif feedback == "y___g":
                current_state = "SPENT_3"
            elif feedback == "y___y":
                current_state = "STEEP_3"
            elif feedback == "y_y_g":
                current_state = "UPSET_3"
            elif feedback == "y_y_y":
                current_state = "SETUP_3"
            elif feedback == "yg__g":
                current_state = "SLEPT_3"
            elif feedback == "yy__g":
                current_state = "SPELT_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "POBOY_3":
            if feedback == "___gy":
                current_state = "NYLON_4"
            elif feedback == "__y_g":
                current_state = "FLYBY_4"
            elif feedback == "_g__g":
                current_state = "FOLKY_4"
            elif feedback == "_g_g_":
                current_state = "COLON_4"
            elif feedback == "_g_yg":
                current_state = "LOONY_4"
            elif feedback == "_gg_g":
                current_state = "LOBBY_4"
            elif feedback == "_y___":
                current_state = "CLOCK_4"
            elif feedback == "_y__g":
                current_state = "FLOWY_4"
            elif feedback == "_yy__":
                current_state = "BLOCK_4"
            elif feedback == "_yyg_":
                current_state = "BLOOM_4"
            elif feedback == "g__gy":
                current_state = "PYLON_4"
            elif feedback == "gg__y":
                current_state = "POLYP_4"
            elif feedback == "gy___":
                current_state = "PLONK_4"
            elif feedback == "y___y":
                current_state = "LYMPH_4"
            elif feedback == "yg_yg":
                current_state = "LOOPY_4"
            elif feedback == "yy___":
                current_state = "CLOMP_4"
            elif feedback == "yyyg_":
                current_state = "BLOOP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "POIND_2":
            if feedback == "_____":
                current_state = "CREME_3"
            elif feedback == "____y":
                current_state = "CRUDE_3"
            elif feedback == "___y_":
                current_state = "GENRE_3"
            elif feedback == "__g__":
                current_state = "CRIME_3"
            elif feedback == "__g_y":
                current_state = "BRIDE_3"
            elif feedback == "__gg_":
                current_state = "BRINE_3"
            elif feedback == "__y__":
                current_state = "RIFLE_3"
            elif feedback == "__y_y":
                current_state = "RIDGE_3"
            elif feedback == "__yy_":
                current_state = "INURE_3"
            elif feedback == "_g___":
                current_state = "ROGUE_3"
            elif feedback == "_y___":
                current_state = "BHANG_3"
            elif feedback == "_y__y":
                current_state = "DROVE_3"
            elif feedback == "_y_g_":
                current_state = "CRONE_3"
            elif feedback == "_y_gy":
                current_state = "DRONE_3"
            elif feedback == "g___y":
                current_state = "PRUDE_3"
            elif feedback == "g__g_":
                current_state = "PRUNE_3"
            elif feedback == "g_g__":
                current_state = "ACMES_3"
            elif feedback == "g_g_y":
                current_state = "PRIDE_3"
            elif feedback == "gy___":
                current_state = "ABLET_3"
            elif feedback == "gy_g_":
                current_state = "PRONE_3"
            elif feedback == "y____":
                current_state = "CREPE_3"
            elif feedback == "y_g__":
                current_state = "GRIPE_3"
            elif feedback == "yy___":
                current_state = "GROPE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "POKER_4":
            if feedback == "yg_gg":
                current_state = "ROPER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PONCY_2":
            if feedback == "_____":
                current_state = "HIRER_3"
            elif feedback == "____g":
                current_state = "AMBRY_3"
            elif feedback == "____y":
                current_state = "BERYL_3"
            elif feedback == "___g_":
                current_state = "MERCH_3"
            elif feedback == "___gg":
                current_state = "MERCY_3"
            elif feedback == "___y_":
                current_state = "CURER_3"
            elif feedback == "__y__":
                current_state = "RERUN_3"
            elif feedback == "__y_g":
                current_state = "NERDY_3"
            elif feedback == "_g___":
                current_state = "BORED_3"
            elif feedback == "_g_y_":
                current_state = "CORER_3"
            elif feedback == "_y___":
                current_state = "ERROR_3"
            elif feedback == "_yy__":
                current_state = "HERON_3"
            elif feedback == "g____":
                current_state = "PERIL_3"
            elif feedback == "g___g":
                current_state = "PERKY_3"
            elif feedback == "g__g_":
                current_state = "PERCH_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "POSER_3":
            if feedback == "y_ygg":
                current_state = "SUPER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PRICK_2":
            if feedback == "_g___":
                current_state = "TROVE_3"
            elif feedback == "_g_g_":
                current_state = "TRUCE_3"
            elif feedback == "_gg__":
                current_state = "TRIBE_3"
            elif feedback == "_gg_y":
                current_state = "TRIKE_3"
            elif feedback == "_ggg_":
                current_state = "TRICE_3"
            elif feedback == "_y___":
                current_state = "THERE_3"
            elif feedback == "yg___":
                current_state = "TROPE_3"
            elif feedback == "ygg__":
                current_state = "TRIPE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PRIMP_4":
            if feedback == "_yg__":
                current_state = "WHIRR_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PRIOR_3":
            if feedback == "___gg":
                current_state = "HUMOR_4"
            elif feedback == "__ygg":
                current_state = "VIGOR_4"
            elif feedback == "_y_gg":
                current_state = "RUMOR_4"
            elif feedback == "_yygg":
                current_state = "RIGOR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PRONG_3":
            if feedback == "_ggg_":
                current_state = "IRONY_4"
            elif feedback == "_gggg":
                current_state = "WRONG_4"
            elif feedback == "_yyg_":
                current_state = "RHINO_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PSHAW_2":
            if feedback == "_g_y_":
                current_state = "ASKER_3"
            elif feedback == "_y_g_":
                current_state = "SMEAR_3"
            elif feedback == "_y_gg":
                current_state = "RESAW_3"
            elif feedback == "_y_gy":
                current_state = "SWEAR_3"
            elif feedback == "_yyg_":
                current_state = "SHEAR_3"
            elif feedback == "yy_g_":
                current_state = "SPEAR_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PUBIC_2":
            if feedback == "_____":
                current_state = "SORRY_3"
            elif feedback == "____y":
                current_state = "SCROD_3"
            elif feedback == "___g_":
                current_state = "LORIS_3"
            elif feedback == "___gy":
                current_state = "SCRIM_3"
            elif feedback == "_g___":
                current_state = "SURLY_3"
            elif feedback == "_y___":
                current_state = "SHRUG_3"
            elif feedback == "_y__y":
                current_state = "SCRUM_3"
            elif feedback == "_y_y_":
                current_state = "VIRUS_3"
            elif feedback == "_yy__":
                current_state = "SHRUB_3"
            elif feedback == "_yy_y":
                current_state = "SCRUB_3"
            elif feedback == "y___y":
                current_state = "CORPS_3"
            elif feedback == "y__g_":
                current_state = "SPRIG_3"
            elif feedback == "y__gy":
                current_state = "SCRIP_3"
            elif feedback == "yy___":
                current_state = "SYRUP_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PUNKY_4":
            if feedback == "gg__g":
                current_state = "PUFFY_5"
            elif feedback == "ggg_g":
                current_state = "PUNNY_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "PYLON_2":
            if feedback == "_____":
                current_state = "BASIC_3"
            elif feedback == "____g":
                current_state = "BASIN_3"
            elif feedback == "____y":
                current_state = "SAUNA_3"
            elif feedback == "___gg":
                current_state = "MASON_3"
            elif feedback == "___y_":
                current_state = "OASIS_3"
            elif feedback == "__g__":
                current_state = "SALAD_3"
            elif feedback == "__ggg":
                current_state = "SALON_3"
            elif feedback == "__gy_":
                current_state = "SALVO_3"
            elif feedback == "__y__":
                current_state = "BASAL_3"
            elif feedback == "__y_y":
                current_state = "NASAL_3"
            elif feedback == "_y___":
                current_state = "AGUED_3"
            elif feedback == "_y__y":
                current_state = "SANDY_3"
            elif feedback == "_y_g_":
                current_state = "SAVOY_3"
            elif feedback == "_yg__":
                current_state = "SALLY_3"
            elif feedback == "_yy__":
                current_state = "SADLY_3"
            elif feedback == "yy___":
                current_state = "SAPPY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "RABID_3":
            if feedback == "gg_gg":
                current_state = "RAPID_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "RADAR_3":
            if feedback == "ggg__":
                current_state = "RADII_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "RAJAH_3":
            if feedback == "gg___":
                current_state = "RABBI_4"
            elif feedback == "gg__g":
                current_state = "RALPH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "RASPY_2":
            if feedback == "ygy__":
                current_state = "SAVOR_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "RAVER_4":
            if feedback == "_g_gg":
                current_state = "BAKER_5"
            elif feedback == "_gggg":
                current_state = "WAVER_5"
            elif feedback == "gg_gg":
                current_state = "RACER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "REALM_3":
            if feedback == "ggg_g":
                current_state = "REARM_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "REBAR_3":
            if feedback == "ggyg_":
                current_state = "REHAB_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "REBUS_3":
            if feedback == "gg__y":
                current_state = "RESIN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "REFER_4":
            if feedback == "gg_g_":
                current_state = "RENEW_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "REFIX_4":
            if feedback == "gy_y_":
                current_state = "RIVER_5"
            elif feedback == "yy_y_":
                current_state = "GIVER_5"
            elif feedback == "yy_yy":
                current_state = "MIXER_5"
            elif feedback == "yyyy_":
                current_state = "FIBER_5"
            elif feedback == "yyyyy":
                current_state = "FIXER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "RODNY_2":
            if feedback == "g____":
                current_state = "RAJAH_3"
            elif feedback == "g___g":
                current_state = "RALLY_3"
            elif feedback == "g__gg":
                current_state = "RAINY_3"
            elif feedback == "g__y_":
                current_state = "RANCH_3"
            elif feedback == "g__yg":
                current_state = "RANGY_3"
            elif feedback == "g_g__":
                current_state = "RADAR_3"
            elif feedback == "g_y__":
                current_state = "RABID_3"
            elif feedback == "g_yyg":
                current_state = "RANDY_3"
            elif feedback == "gy___":
                current_state = "RAZOR_3"
            elif feedback == "gy_yy":
                current_state = "RAYON_3"
            elif feedback == "gyg__":
                current_state = "RADIO_3"
            elif feedback == "gygy_":
                current_state = "RADON_3"
            elif feedback == "y____":
                current_state = "CAPRI_3"
            elif feedback == "y___g":
                current_state = "FAIRY_3"
            elif feedback == "y__y_":
                current_state = "CAIRN_3"
            elif feedback == "y_gy_":
                current_state = "NADIR_3"
            elif feedback == "y_y_g":
                current_state = "DAIRY_3"
            elif feedback == "yy___":
                current_state = "VALOR_3"
            elif feedback == "yy__y":
                current_state = "MAYOR_3"
            elif feedback == "yy_y_":
                current_state = "MANOR_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "ROGUE_3":
            if feedback == "ggyyg":
                current_state = "ROUGE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "RUDER_4":
            if feedback == "_yggg":
                current_state = "UDDER_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "RUMBA_3":
            if feedback == "yyyyg":
                current_state = "UMBRA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "RUMPY_3":
            if feedback == "g____":
                current_state = "REFER_4"
            elif feedback == "g___g":
                current_state = "REFRY_4"
            elif feedback == "gy__g":
                current_state = "REBUY_4"
            elif feedback == "gyy__":
                current_state = "RHEUM_4"
            elif feedback == "y____":
                current_state = "FEVER_4"
            elif feedback == "y___g":
                current_state = "EVERY_4"
            elif feedback == "y___y":
                current_state = "FRYER_4"
            elif feedback == "y__y_":
                current_state = "PREEN_4"
            elif feedback == "y__yy":
                current_state = "HYPER_4"
            elif feedback == "y_y__":
                current_state = "EMBER_4"
            elif feedback == "y_y_g":
                current_state = "EMERY_4"
            elif feedback == "yg___":
                current_state = "QUEER_4"
            elif feedback == "yg__g":
                current_state = "QUERY_4"
            elif feedback == "yg__y":
                current_state = "BUYER_4"
            elif feedback == "yy___":
                current_state = "EXURB_4"
            elif feedback == "yy_y_":
                current_state = "UPPER_4"
            elif feedback == "yyg__":
                current_state = "FEMUR_4"
            elif feedback == "yyy__":
                current_state = "UMBER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SABER_3":
            if feedback == "gg_gg":
                current_state = "SAFER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SABLE_2":
            if feedback == "gg__g":
                current_state = "SAUCE_3"
            elif feedback == "gg_yg":
                current_state = "SALVE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SALPS_2":
            if feedback == "gg__y":
                current_state = "SASSY_3"
            elif feedback == "ggg_y":
                current_state = "SALSA_3"
            elif feedback == "yg___":
                current_state = "DAISY_3"
            elif feedback == "yg__y":
                current_state = "GASSY_3"
            elif feedback == "yg_y_":
                current_state = "PANSY_3"
            elif feedback == "ygg__":
                current_state = "BALSA_3"
            elif feedback == "yggy_":
                current_state = "PALSY_3"
            elif feedback == "ygy_y":
                current_state = "LASSO_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SAPAN_2":
            if feedback == "gg___":
                current_state = "SALTY_3"
            elif feedback == "gg__g":
                current_state = "SATIN_3"
            elif feedback == "gg__y":
                current_state = "SAINT_3"
            elif feedback == "gg_g_":
                current_state = "SATAY_3"
            elif feedback == "yg___":
                current_state = "HASTY_3"
            elif feedback == "yg__y":
                current_state = "NASTY_3"
            elif feedback == "ygy__":
                current_state = "PASTY_3"
            elif feedback == "ygyy_":
                current_state = "PASTA_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SCALD_3":
            if feedback == "gggg_":
                current_state = "SCALY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SCAPE_3":
            if feedback == "gygyg":
                current_state = "SPACE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SCARF_3":
            if feedback == "gggg_":
                current_state = "SCARY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SCENE_3":
            if feedback == "g__gg":
                current_state = "SHONE_4"
            elif feedback == "gg_gg":
                current_state = "SCONE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SCHWA_3":
            if feedback == "gg__g":
                current_state = "SCUBA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SCOOP_3":
            if feedback == "g___y":
                current_state = "SPIFF_4"
            elif feedback == "g_ggg":
                current_state = "SWOOP_4"
            elif feedback == "g_ggy":
                current_state = "SPOOF_4"
            elif feedback == "g_y_y":
                current_state = "SOPPY_4"
            elif feedback == "gy__y":
                current_state = "SPICY_4"
            elif feedback == "y___y":
                current_state = "WISPY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SCOOT_3":
            if feedback == "g_ggg":
                current_state = "SHOOT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SCOPE_3":
            if feedback == "g__yg":
                current_state = "SPUME_4"
            elif feedback == "g_gyg":
                current_state = "SPOKE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SCRAM_2":
            if feedback == "g_gg_":
                current_state = "SPRAY_3"
            elif feedback == "gggg_":
                current_state = "SCRAP_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SCREE_2":
            if feedback == "g_g_g":
                current_state = "SURGE_3"
            elif feedback == "g_ggg":
                current_state = "SPREE_3"
            elif feedback == "g_gyg":
                current_state = "SERVE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SEDER_3":
            if feedback == "gg_gg":
                current_state = "SEVER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SEDGE_3":
            if feedback == "gg_yg":
                current_state = "SEGUE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHADY_3":
            if feedback == "g_g__":
                current_state = "SWAMI_4"
            elif feedback == "ggg_g":
                current_state = "SHAKY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHALL_3":
            if feedback == "g_ggg":
                current_state = "SMALL_4"
            elif feedback == "ggg_g":
                current_state = "SHAWL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHANK_3":
            if feedback == "g_gg_":
                current_state = "SWANG_4"
            elif feedback == "g_ggg":
                current_state = "SWANK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHARK_3":
            if feedback == "g_gg_":
                current_state = "SNARF_4"
            elif feedback == "g_ggg":
                current_state = "SNARK_4"
            elif feedback == "gggg_":
                current_state = "SHARD_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHEEP_3":
            if feedback == "g_ggy":
                current_state = "SPEED_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHEIK_3":
            if feedback == "g_g_g":
                current_state = "SPECK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHIED_3":
            if feedback == "g_ggg":
                current_state = "SPIED_4"
            elif feedback == "y__g_":
                current_state = "MOSEY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHIFT_3":
            if feedback == "g_ggg":
                current_state = "SWIFT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHILL_3":
            if feedback == "g___g":
                current_state = "SCOWL_4"
            elif feedback == "g__g_":
                current_state = "SCOLD_4"
            elif feedback == "g_ggg":
                current_state = "SWILL_4"
            elif feedback == "g_ygy":
                current_state = "SILLY_4"
            elif feedback == "g_yy_":
                current_state = "SOLID_4"
            elif feedback == "gg_g_":
                current_state = "SHYLY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHIMS_2":
            if feedback == "g___y":
                current_state = "SUDSY_3"
            elif feedback == "g_y_y":
                current_state = "SISSY_3"
            elif feedback == "gg__y":
                current_state = "SHUSH_3"
            elif feedback == "gy__y":
                current_state = "SLOSH_3"
            elif feedback == "gy_yy":
                current_state = "SMUSH_3"
            elif feedback == "gyg_y":
                current_state = "SWISH_3"
            elif feedback == "y____":
                current_state = "LOUSY_3"
            elif feedback == "y___g":
                current_state = "FLOSS_3"
            elif feedback == "y___y":
                current_state = "FUSSY_3"
            elif feedback == "y__y_":
                current_state = "MOUSY_3"
            elif feedback == "y__yy":
                current_state = "MOSSY_3"
            elif feedback == "y_g__":
                current_state = "NOISY_3"
            elif feedback == "y_g_g":
                current_state = "BLISS_3"
            elif feedback == "y_y__":
                current_state = "KIOSK_3"
            elif feedback == "y_y_y":
                current_state = "KISSY_3"
            elif feedback == "y_yyy":
                current_state = "MISSY_3"
            elif feedback == "ygg__":
                current_state = "PHISH_3"
            elif feedback == "yy___":
                current_state = "ABAFT_3"
            elif feedback == "yy__y":
                current_state = "HUSSY_3"
            elif feedback == "yyg__":
                current_state = "KNISH_3"
            elif feedback == "yyy_y":
                current_state = "HISSY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHINE_3":
            if feedback == "g_ggg":
                current_state = "SWINE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHINY_3":
            if feedback == "g_gg_":
                current_state = "SWING_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHIRK_3":
            if feedback == "g_ggg":
                current_state = "SMIRK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHOAL_3":
            if feedback == "y__gg":
                current_state = "USUAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHOCK_3":
            if feedback == "g_ggg":
                current_state = "SMOCK_4"
            elif feedback == "ggg_g":
                current_state = "SHOOK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHORN_3":
            if feedback == "g_ggg":
                current_state = "SWORN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHOVE_3":
            if feedback == "g___g":
                current_state = "SUEDE_4"
            elif feedback == "g_g_g":
                current_state = "SMOKE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SHUNT_3":
            if feedback == "g_ggg":
                current_state = "STUNT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SILKY_3":
            if feedback == "gyyy_":
                current_state = "SKILL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SILTY_3":
            if feedback == "gg_g_":
                current_state = "SIXTH_4"
            elif feedback == "gg_gg":
                current_state = "SIXTY_4"
            elif feedback == "gy_g_":
                current_state = "SMITH_4"
            elif feedback == "gy_y_":
                current_state = "STICK_4"
            elif feedback == "gyyy_":
                current_state = "STILL_4"
            elif feedback == "yg_gg":
                current_state = "MISTY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SKEIN_3":
            if feedback == "g_g_y":
                current_state = "SPEND_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SKIFF_3":
            if feedback == "gy___":
                current_state = "SMOKY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SKIMP_3":
            if feedback == "gyg_y":
                current_state = "SPIKY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SLEEK_3":
            if feedback == "gggg_":
                current_state = "SLEEP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SLIMY_3":
            if feedback == "gg__g":
                current_state = "SLYLY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SLOSH_3":
            if feedback == "gg_gg":
                current_state = "SLUSH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SMARM_3":
            if feedback == "g_ggg":
                current_state = "SWARM_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SMART_2":
            if feedback == "g_ggg":
                current_state = "START_3"
            elif feedback == "g_ggy":
                current_state = "STARK_3"
            elif feedback == "g_gyy":
                current_state = "STAIR_3"
            elif feedback == "g_yyy":
                current_state = "SITAR_3"
            elif feedback == "y_yyy":
                current_state = "ASTIR_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SNAFU_3":
            if feedback == "ggg__":
                current_state = "SNAKY_4"
            elif feedback == "gyg__":
                current_state = "SWAIN_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SNIPY_2":
            if feedback == "g____":
                current_state = "SHEAF_3"
            elif feedback == "g___g":
                current_state = "SEAMY_3"
            elif feedback == "g__y_":
                current_state = "SPEAK_3"
            elif feedback == "g_yy_":
                current_state = "SEPIA_3"
            elif feedback == "gg___":
                current_state = "SNEAK_3"
            elif feedback == "gy___":
                current_state = "SEDAN_3"
            elif feedback == "y____":
                current_state = "ASKEW_3"
            elif feedback == "y___g":
                current_state = "ESSAY_3"
            elif feedback == "y_y__":
                current_state = "AEGIS_3"
            elif feedback == "yy___":
                current_state = "ASHEN_3"
            elif feedback == "yy_y_":
                current_state = "ASPEN_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SNOOP_3":
            if feedback == "gyggy":
                current_state = "SPOON_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SOAPY_3":
            if feedback == "g_gy_":
                current_state = "SWAMP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SOOTH_3":
            if feedback == "gggg_":
                current_state = "SOOTY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SOUND_3":
            if feedback == "g_gg_":
                current_state = "SWUNG_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SPADE_3":
            if feedback == "g_g_g":
                current_state = "SUAVE_4"
            elif feedback == "y_g_g":
                current_state = "USAGE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SPENT_3":
            if feedback == "gyg_g":
                current_state = "SWEPT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SPICE_3":
            if feedback == "ggg_g":
                current_state = "SPIKE_4"
            elif feedback == "gyg_g":
                current_state = "SWIPE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SPILL_3":
            if feedback == "gg__g":
                current_state = "SPOOL_4"
            elif feedback == "ggy_g":
                current_state = "SPOIL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SPILT_3":
            if feedback == "g_ggg":
                current_state = "STILT_4"
            elif feedback == "g_y_g":
                current_state = "SIGHT_4"
            elif feedback == "ggyyg":
                current_state = "SPLIT_4"
            elif feedback == "y_y_g":
                current_state = "VISIT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SPITE_3":
            if feedback == "g_ggg":
                current_state = "SUITE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SPORT_3":
            if feedback == "g_ggy":
                current_state = "STORM_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SQUIB_3":
            if feedback == "g_g__":
                current_state = "SCUFF_4"
            elif feedback == "gggg_":
                current_state = "SQUID_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "STAGE_3":
            if feedback == "ggg_g":
                current_state = "STAVE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "STALK_3":
            if feedback == "gggg_":
                current_state = "STALL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "STAND_3":
            if feedback == "ggg__":
                current_state = "STAFF_4"
            elif feedback == "ggg_g":
                current_state = "STAID_4"
            elif feedback == "gggg_":
                current_state = "STANK_4"
            elif feedback == "gggy_":
                current_state = "STAIN_4"
            elif feedback == "gyg__":
                current_state = "SWATH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "STEAK_3":
            if feedback == "gggg_":
                current_state = "STEAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "STEED_3":
            if feedback == "ggg__":
                current_state = "STEIN_4"
            elif feedback == "yyy__":
                current_state = "ZESTY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "STELE_3":
            if feedback == "gg_gg":
                current_state = "STYLE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "STING_3":
            if feedback == "gggg_":
                current_state = "STINK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "STOMA_3":
            if feedback == "yy__g":
                current_state = "VISTA_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "STONE_3":
            if feedback == "ggg_g":
                current_state = "STOVE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "STREP_2":
            if feedback == "gggg_":
                current_state = "STREW_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "STRUM_2":
            if feedback == "ggg__":
                current_state = "STRIP_3"
            elif feedback == "gggg_":
                current_state = "STRUT_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "STUNG_3":
            if feedback == "gggg_":
                current_state = "STUNK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "SUING_3":
            if feedback == "gg_g_":
                current_state = "SUNNY_4"
            elif feedback == "yyggg":
                current_state = "USING_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TABLE_2":
            if feedback == "gg__g":
                current_state = "TAUPE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TALUS_2":
            if feedback == "gg__y":
                current_state = "TASTY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TARDY_2":
            if feedback == "ggg__":
                current_state = "TAROT_3"
            elif feedback == "ggg_g":
                current_state = "TARRY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TARSE_1":
            if feedback == "_____":
                current_state = "GUILD_2"
            elif feedback == "____g":
                current_state = "LOGIN_2"
            elif feedback == "____y":
                current_state = "DYNEL_2"
            elif feedback == "___g_":
                current_state = "SHIMS_2"
            elif feedback == "___gg":
                current_state = "CLOUD_2"
            elif feedback == "___gy":
                current_state = "COWLS_2"
            elif feedback == "___y_":
                current_state = "PLUNK_2"
            elif feedback == "___yg":
                current_state = "PLING_2"
            elif feedback == "___yy":
                current_state = "NEWEL_2"
            elif feedback == "__g__":
                current_state = "CYMOL_2"
            elif feedback == "__g_g":
                current_state = "GENIO_2"
            elif feedback == "__g_y":
                current_state = "PONCY_2"
            elif feedback == "__ggg":
                current_state = "COUGH_2"
            elif feedback == "__ggy":
                current_state = "VERSO_2"
            elif feedback == "__gy_":
                current_state = "PUBIC_2"
            elif feedback == "__gyg":
                current_state = "SCREE_2"
            elif feedback == "__gyy":
                current_state = "CIDER_2"
            elif feedback == "__y__":
                current_state = "CODON_2"
            elif feedback == "__y_g":
                current_state = "POIND_2"
            elif feedback == "__y_y":
                current_state = "DOLCI_2"
            elif feedback == "__yg_":
                current_state = "CHIMB_2"
            elif feedback == "__ygg":
                current_state = "APIOL_2"
            elif feedback == "__ygy":
                current_state = "ACHED_2"
            elif feedback == "__yy_":
                current_state = "CLONK_2"
            elif feedback == "__yyg":
                current_state = "PINCH_2"
            elif feedback == "__yyy":
                current_state = "WHEEP_2"
            elif feedback == "_g___":
                current_state = "CHYND_2"
            elif feedback == "_g__g":
                current_state = "GULCH_2"
            elif feedback == "_g__y":
                current_state = "LYMPH_2"
            elif feedback == "_g_g_":
                current_state = "SALPS_2"
            elif feedback == "_g_gg":
                current_state = "LUPIN_2"
            elif feedback == "_g_y_":
                current_state = "PYLON_2"
            elif feedback == "_g_yg":
                current_state = "SABLE_2"
            elif feedback == "_g_yy":
                current_state = "EASEL_2"
            elif feedback == "_gg__":
                current_state = "CYMOL_2"
            elif feedback == "_gg_g":
                current_state = "BEFOG_2"
            elif feedback == "_gg_y":
                current_state = "BELCH_2"
            elif feedback == "_ggg_":
                current_state = "HARSH_2"
            elif feedback == "_gggg":
                current_state = "PARSE_2"
            elif feedback == "_gy__":
                current_state = "RODNY_2"
            elif feedback == "_gy_g":
                current_state = "CADRE_2"
            elif feedback == "_gy_y":
                current_state = "GLAMP_2"
            elif feedback == "_gygg":
                current_state = "RAISE_2"
            elif feedback == "_gyy_":
                current_state = "RASPY_2"
            elif feedback == "_gyyg":
                current_state = "SABRE_2"
            elif feedback == "_gyyy":
                current_state = "ANVIL_2"
            elif feedback == "_y___":
                current_state = "COLIN_2"
            elif feedback == "_y__g":
                current_state = "GLAND_2"
            elif feedback == "_y__y":
                current_state = "MEDAL_2"
            elif feedback == "_y_g_":
                current_state = "MULCH_2"
            elif feedback == "_y_gg":
                current_state = "BIACH_2"
            elif feedback == "_y_gy":
                current_state = "LEASH_2"
            elif feedback == "_y_y_":
                current_state = "PLANC_2"
            elif feedback == "_y_yg":
                current_state = "CHALK_2"
            elif feedback == "_y_yy":
                current_state = "SNIPY_2"
            elif feedback == "_yg__":
                current_state = "ALOIN_2"
            elif feedback == "_yg_g":
                current_state = "AERIE_2"
            elif feedback == "_yg_y":
                current_state = "FERAL_2"
            elif feedback == "_ygg_":
                current_state = "BURSA_2"
            elif feedback == "_ygy_":
                current_state = "SCRAM_2"
            elif feedback == "_yy__":
                current_state = "BLOND_2"
            elif feedback == "_yy_g":
                current_state = "GRAND_2"
            elif feedback == "_yy_y":
                current_state = "BEMAD_2"
            elif feedback == "_yyg_":
                current_state = "ABACS_2"
            elif feedback == "_yygg":
                current_state = "ARISE_2"
            elif feedback == "_yyy_":
                current_state = "CLAMP_2"
            elif feedback == "_yyyg":
                current_state = "ANCHO_2"
            elif feedback == "_yyyy":
                current_state = "PSHAW_2"
            elif feedback == "g____":
                current_state = "CUING_2"
            elif feedback == "g___g":
                current_state = "CHILD_2"
            elif feedback == "g___y":
                current_state = "HONED_2"
            elif feedback == "g__g_":
                current_state = "TIPSY_2"
            elif feedback == "g__gg":
                current_state = "TENSE_2"
            elif feedback == "g__yy":
                current_state = "TELOS_2"
            elif feedback == "g_g__":
                current_state = "THROB_2"
            elif feedback == "g_g_g":
                current_state = "THREE_2"
            elif feedback == "g_g_y":
                current_state = "THREW_2"
            elif feedback == "g_gg_":
                current_state = "TORSO_2"
            elif feedback == "g_ggg":
                current_state = "TERSE_2"
            elif feedback == "g_gy_":
                current_state = "TORUS_2"
            elif feedback == "g_y__":
                current_state = "HOKUM_2"
            elif feedback == "g_y_g":
                current_state = "PRICK_2"
            elif feedback == "g_y_y":
                current_state = "MINOR_2"
            elif feedback == "g_yg_":
                current_state = "TRUSS_2"
            elif feedback == "g_ygy":
                current_state = "TRESS_2"
            elif feedback == "gg___":
                current_state = "LINKY_2"
            elif feedback == "gg__g":
                current_state = "TABLE_2"
            elif feedback == "gg__y":
                current_state = "TAKEN_2"
            elif feedback == "gg_y_":
                current_state = "TALUS_2"
            elif feedback == "gg_yg":
                current_state = "TASTE_2"
            elif feedback == "ggg__":
                current_state = "TARDY_2"
            elif feedback == "ggy__":
                current_state = "TAPIR_2"
            elif feedback == "ggy_y":
                current_state = "KEMPS_2"
            elif feedback == "ggyyy":
                current_state = "TASER_2"
            elif feedback == "gy___":
                current_state = "DOGAN_2"
            elif feedback == "gy__y":
                current_state = "TEACH_2"
            elif feedback == "gy_g_":
                current_state = "TOAST_2"
            elif feedback == "gy_gg":
                current_state = "TEASE_2"
            elif feedback == "gyg__":
                current_state = "TORAH_2"
            elif feedback == "gyg_y":
                current_state = "TERRA_2"
            elif feedback == "gyy__":
                current_state = "CLINT_2"
            elif feedback == "gyy_g":
                current_state = "TRACE_2"
            elif feedback == "gyy_y":
                current_state = "TETRA_2"
            elif feedback == "gyyg_":
                current_state = "TRASH_2"
            elif feedback == "gyyy_":
                current_state = "TRANS_2"
            elif feedback == "y____":
                current_state = "DONUT_2"
            elif feedback == "y___g":
                current_state = "BUILD_2"
            elif feedback == "y___y":
                current_state = "PILED_2"
            elif feedback == "y__g_":
                current_state = "HIMBO_2"
            elif feedback == "y__gy":
                current_state = "DIGHT_2"
            elif feedback == "y__y_":
                current_state = "FOUNT_2"
            elif feedback == "y__yg":
                current_state = "MILKO_2"
            elif feedback == "y__yy":
                current_state = "PLUOT_2"
            elif feedback == "y_g__":
                current_state = "BIFFY_2"
            elif feedback == "y_g_g":
                current_state = "FORTE_2"
            elif feedback == "y_g_y":
                current_state = "BERET_2"
            elif feedback == "y_gg_":
                current_state = "WURST_2"
            elif feedback == "y_gy_":
                current_state = "STRUM_2"
            elif feedback == "y_gyy":
                current_state = "STREP_2"
            elif feedback == "y_y__":
                current_state = "BIONT_2"
            elif feedback == "y_y_g":
                current_state = "BIOTA_2"
            elif feedback == "y_y_y":
                current_state = "COURT_2"
            elif feedback == "y_yg_":
                current_state = "BOGUE_2"
            elif feedback == "y_ygy":
                current_state = "CREST_2"
            elif feedback == "y_yy_":
                current_state = "HONKY_2"
            elif feedback == "y_yyg":
                current_state = "STORE_2"
            elif feedback == "y_yyy":
                current_state = "ESTER_2"
            elif feedback == "yg___":
                current_state = "CLIPT_2"
            elif feedback == "yg__g":
                current_state = "CLOTH_2"
            elif feedback == "yg__y":
                current_state = "LEMED_2"
            elif feedback == "yg_g_":
                current_state = "PATSY_2"
            elif feedback == "yg_y_":
                current_state = "SAPAN_2"
            elif feedback == "yg_yg":
                current_state = "BUCHU_2"
            elif feedback == "ygg__":
                current_state = "APACE_2"
            elif feedback == "ygg_g":
                current_state = "CARTE_2"
            elif feedback == "ygg_y":
                current_state = "CARET_2"
            elif feedback == "ygy__":
                current_state = "GATOR_2"
            elif feedback == "ygy_y":
                current_state = "CHAWL_2"
            elif feedback == "ygyy_":
                current_state = "SATYR_2"
            elif feedback == "yy___":
                current_state = "PLOIT_2"
            elif feedback == "yy__g":
                current_state = "ABOMA_2"
            elif feedback == "yy__y":
                current_state = "PLANC_2"
            elif feedback == "yy_g_":
                current_state = "BOAST_2"
            elif feedback == "yy_gy":
                current_state = "AFFLY_2"
            elif feedback == "yy_y_":
                current_state = "CLAPT_2"
            elif feedback == "yy_yg":
                current_state = "KLETT_2"
            elif feedback == "yy_yy":
                current_state = "ADMIT_2"
            elif feedback == "yyg__":
                current_state = "AORTA_2"
            elif feedback == "yygy_":
                current_state = "APAYD_2"
            elif feedback == "yyy__":
                current_state = "ARGOT_2"
            elif feedback == "yyy_g":
                current_state = "ACING_2"
            elif feedback == "yyy_y":
                current_state = "ALERT_2"
            elif feedback == "yyyg_":
                current_state = "ARTSY_2"
            elif feedback == "yyyy_":
                current_state = "SMART_2"
            elif feedback == "yyyyg":
                current_state = "STARE_2"
            elif feedback == "yyyyy":
                current_state = "ASTER_2"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TEACH_2":
            if feedback == "gyy__":
                current_state = "TWEAK_3"
            elif feedback == "gyy_y":
                current_state = "THETA_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TEETH_3":
            if feedback == "g_gyy":
                current_state = "THEFT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TELOS_2":
            if feedback == "gg__y":
                current_state = "TESTY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TENSE_2":
            if feedback == "g__gg":
                current_state = "THOSE_3"
            elif feedback == "gy_gg":
                current_state = "THESE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TETRA_2":
            if feedback == "gg_gy":
                current_state = "TEARY_3"
            elif feedback == "gy_yy":
                current_state = "TREAD_3"
            elif feedback == "gyyyy":
                current_state = "TREAT_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "THEIR_3":
            if feedback == "g_yyg":
                current_state = "TRIER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "THEME_3":
            if feedback == "gg_gg":
                current_state = "THYME_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "THING_3":
            if feedback == "g_ggg":
                current_state = "TYING_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "THREE_2":
            if feedback == "g_g_g":
                current_state = "TORTE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "THREW_2":
            if feedback == "g_gg_":
                current_state = "TIRED_3"
            elif feedback == "g_gy_":
                current_state = "TERRY_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "THROB_2":
            if feedback == "g_gyy":
                current_state = "TURBO_3"
            elif feedback == "ggg__":
                current_state = "THRUM_3"
            elif feedback == "gggg_":
                current_state = "THROW_3"
            elif feedback == "gygy_":
                current_state = "TORCH_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "THUMB_3":
            if feedback == "gggg_":
                current_state = "THUMP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TIGER_3":
            if feedback == "gg_gg":
                current_state = "TITER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TIMID_3":
            if feedback == "gg___":
                current_state = "TIZZY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TIPSY_2":
            if feedback == "gy_g_":
                current_state = "TWIST_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TODDY_3":
            if feedback == "gg___":
                current_state = "TOOTH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TOPAZ_3":
            if feedback == "gg_g_":
                current_state = "TOTAL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TOPIC_3":
            if feedback == "gg_gg":
                current_state = "TOXIC_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TORAH_2":
            if feedback == "gggy_":
                current_state = "TORTA_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TOTEM_3":
            if feedback == "gg_g_":
                current_state = "TOWEL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TRACE_2":
            if feedback == "ggg_g":
                current_state = "TRADE_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TRIBE_3":
            if feedback == "ggg_g":
                current_state = "TRITE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TRILL_3":
            if feedback == "gyg_g":
                current_state = "TWIRL_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TROLL_3":
            if feedback == "ggg__":
                current_state = "TROOP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TRUCK_3":
            if feedback == "ggg_g":
                current_state = "TRUNK_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TRUER_3":
            if feedback == "g_ygg":
                current_state = "TUBER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TRUSS_2":
            if feedback == "gg_g_":
                current_state = "TRYST_3"
            elif feedback == "gggg_":
                current_state = "TRUST_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TWERK_3":
            if feedback == "gggg_":
                current_state = "TWERP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "TWILL_3":
            if feedback == "ggg__":
                current_state = "TWIXT_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "UNFED_3":
            if feedback == "_g_gy":
                current_state = "INDEX_4"
            elif feedback == "_y_gy":
                current_state = "WIDEN_4"
            elif feedback == "gg_gg":
                current_state = "UNWED_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "UNHIP_3":
            if feedback == "gg_gg":
                current_state = "UNZIP_4"
            elif feedback == "gg_gy":
                current_state = "UNPIN_4"
            elif feedback == "y__yg":
                current_state = "MIXUP_4"
            elif feedback == "yy_yg":
                current_state = "PINUP_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "USURP_3":
            if feedback == "gggg_":
                current_state = "USURY_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "VALID_3":
            if feedback == "gg_gg":
                current_state = "VAPID_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "VALOR_3":
            if feedback == "_g_gg":
                current_state = "MAJOR_4"
            elif feedback == "_g_yy":
                current_state = "MACRO_4"
            elif feedback == "_gygg":
                current_state = "LABOR_4"
            elif feedback == "gg_gg":
                current_state = "VAPOR_4"
            elif feedback == "yg_gg":
                current_state = "FAVOR_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "VENOM_3":
            if feedback == "_gg__":
                current_state = "BENCH_4"
            elif feedback == "_ggg_":
                current_state = "XENON_4"
            elif feedback == "_yg__":
                current_state = "ENNUI_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "VOCAB_3":
            if feedback == "___y_":
                current_state = "FRAME_4"
            elif feedback == "___yy":
                current_state = "BRAKE_4"
            elif feedback == "__yy_":
                current_state = "CRAZE_4"
            elif feedback == "__yyy":
                current_state = "BRACE_4"
            elif feedback == "y__yy":
                current_state = "BRAVE_4"
            elif feedback == "y_yy_":
                current_state = "CRAVE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "WHEEP_2":
            if feedback == "___g_":
                current_state = "MISER_3"
            elif feedback == "___gy":
                current_state = "POSER_3"
            elif feedback == "__g_y":
                current_state = "SPERM_3"
            elif feedback == "__gg_":
                current_state = "SNEER_3"
            elif feedback == "__y__":
                current_state = "REBUS_3"
            elif feedback == "__yg_":
                current_state = "SEDER_3"
            elif feedback == "_g_g_":
                current_state = "SHYER_3"
            elif feedback == "_ggg_":
                current_state = "SHEER_3"
            elif feedback == "_y_g_":
                current_state = "USHER_3"
            elif feedback == "g__g_":
                current_state = "WISER_3"
            elif feedback == "y__g_":
                current_state = "SOWER_3"
            elif feedback == "y_yg_":
                current_state = "SEWER_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "WHOMP_3":
            if feedback == "__g__":
                current_state = "BOOBY_4"
            elif feedback == "__g_y":
                current_state = "POOFY_4"
            elif feedback == "__gy_":
                current_state = "MOONY_4"
            elif feedback == "__y__":
                current_state = "GUNKY_4"
            elif feedback == "__y_y":
                current_state = "POKER_4"
            elif feedback == "__yg_":
                current_state = "MOMMY_4"
            elif feedback == "__yy_":
                current_state = "MOVER_4"
            elif feedback == "__yyy":
                current_state = "MOPER_4"
            elif feedback == "_gg__":
                current_state = "CHOCK_4"
            elif feedback == "_gg_y":
                current_state = "PHONY_4"
            elif feedback == "_gggg":
                current_state = "CHOMP_4"
            elif feedback == "_y_yy":
                current_state = "NYMPH_4"
            elif feedback == "_yg__":
                current_state = "HOOCH_4"
            elif feedback == "_yg_y":
                current_state = "POOCH_4"
            elif feedback == "_ygy_":
                current_state = "MOOCH_4"
            elif feedback == "_yy__":
                current_state = "HOVER_4"
            elif feedback == "_yy_y":
                current_state = "HOPPY_4"
            elif feedback == "_yyy_":
                current_state = "HOMER_4"
            elif feedback == "_yyyy":
                current_state = "OOMPH_4"
            elif feedback == "g_g__":
                current_state = "WOOER_4"
            elif feedback == "g_y__":
                current_state = "WONKY_4"
            elif feedback == "ggg_g":
                current_state = "WHOOP_4"
            elif feedback == "y_g__":
                current_state = "KNOWN_4"
            elif feedback == "y_y__":
                current_state = "BOWER_4"
            elif feedback == "y_y_y":
                current_state = "POWER_4"
            elif feedback == "y_yy_":
                current_state = "MOWER_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "WIFTY_3":
            if feedback == "_g_gg":
                current_state = "BITTY_4"
            elif feedback == "_g_y_":
                current_state = "HITCH_4"
            elif feedback == "_g_yg":
                current_state = "PITHY_4"
            elif feedback == "_ggg_":
                current_state = "FIFTH_4"
            elif feedback == "_gggg":
                current_state = "FIFTY_4"
            elif feedback == "_gyg_":
                current_state = "FILTH_4"
            elif feedback == "_y_g_":
                current_state = "BLITZ_4"
            elif feedback == "_y_yg":
                current_state = "ITCHY_4"
            elif feedback == "gg_gg":
                current_state = "WITTY_4"
            elif feedback == "gg_y_":
                current_state = "WITCH_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "WINCE_3":
            if feedback == "_gggg":
                current_state = "MINCE_4"
            elif feedback == "_gygg":
                current_state = "NIECE_4"
            elif feedback == "_gyyg":
                current_state = "NICHE_4"
            elif feedback == "_yy_g":
                current_state = "KNIFE_4"
            elif feedback == "gyy_g":
                current_state = "WHINE_4"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "WOKEN_4":
            if feedback == "gg_gg":
                current_state = "WOMEN_5"
            else:
                print("Pattern variant not found in tree paths.")
                return
        elif current_state == "WURST_2":
            if feedback == "__ggg":
                current_state = "FIRST_3"
            elif feedback == "_gggg":
                current_state = "BURST_3"
            elif feedback == "g_ggg":
                current_state = "WORST_3"
            else:
                print("Pattern variant not found in tree paths.")
                return
        else:
            print("Pattern variant not found in tree paths.")
            return

if __name__ == "__main__":
    play_wordle_generated()
