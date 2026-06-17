import sys
import os
import random
import math
import time
from functools import lru_cache

# --- CONFIGURATION ENGINE ---
MAX_TURNS = 6  # Dynamic Max Turn setting (Default: 6)

# --- PDF ENGINE IMPORTS ---
try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors

    HAS_PDF = True
except ImportError:
    HAS_PDF = False

# --- 1. DATA LOADING ---
proper_word, word_list, full_dictionary = [], [], []


def load_data(choice):
    global proper_word, word_list, full_dictionary
    try:
        if choice == 1:
            with open("proper word.txt", "r", encoding="utf-8") as f:
                proper_word = [line.strip().lower() for line in f if len(line.strip()) == 5]
            with open("word list.txt", "r", encoding="utf-8") as f:
                word_list = [line.strip().lower() for line in f if len(line.strip()) == 5]
        elif choice == 2:
            with open("NYT WordleBot Answers (1).txt", "r", encoding="utf-8") as f:
                proper_word = [line.strip().lower() for line in f if len(line.strip()) == 5]
            with open("wordlist_nyt20220830_all (1).txt", "r", encoding="utf-8") as f:
                word_list = [line.strip().lower() for line in f if len(line.strip()) == 5]
        elif choice == 3:
            with open("wordlist_nyt20230701_hidden (2).txt", "r", encoding="utf-8") as f:
                proper_word = [line.strip().lower() for line in f if len(line.strip()) == 5]
            with open("wordlist_nyt20220830_all (1).txt", "r", encoding="utf-8") as f:
                word_list = [line.strip().lower() for line in f if len(line.strip()) == 5]
        elif choice == 4:
            with open("proper word.txt", "r", encoding="utf-8") as f:
                proper_word = [line.strip().lower() for line in f if len(line.strip()) == 5]
            with open("proper word.txt", "r", encoding="utf-8") as f:
                word_list = [line.strip().lower() for line in f if len(line.strip()) == 5]
        elif choice == 5:
            with open("NYT WordleBot Answers (1).txt", "r", encoding="utf-8") as f:
                proper_word = [line.strip().lower() for line in f if len(line.strip()) == 5]
            with open("NYT WordleBot Answers (2).txt", "r", encoding="utf-8") as f:
                word_list = [line.strip().lower() for line in f if len(line.strip()) == 5]
        elif choice == 6:
            with open("wordlist_nyt20220830_hidden.txt", "r", encoding="utf-8") as f:
                proper_word = [line.strip().lower() for line in f if len(line.strip()) == 5]
            with open("wordlist_nyt20220830_all (1).txt", "r", encoding="utf-8") as f:
                word_list = [line.strip().lower() for line in f if len(line.strip()) == 5]
        full_dictionary = list(set(proper_word + word_list))
    except FileNotFoundError:
        sys.exit("CRITICAL ERROR: Dictionary files missing.")


# Global Feedback Matrix Lookup for ultra-high speed tree iterations
GLOBAL_FEEDBACK_CACHE = {}
# Unified Memorization Matrix to track coexistence paths across all permutations
UNIFIED_COEXISTENCE_CACHE = {}


# --- 2. CORE PATTERN ENGINE ---
@lru_cache(maxsize=445)
def get_feedback(secret, guess):
    pair = (secret, guess)
    if pair in GLOBAL_FEEDBACK_CACHE:
        return GLOBAL_FEEDBACK_CACHE[pair]

    if secret == guess:
        GLOBAL_FEEDBACK_CACHE[pair] = "ggggg"
        return "ggggg"

    res, s_list, g_list = ['_'] * 5, list(secret), list(guess)
    for i in range(5):
        if g_list[i] == s_list[i]:
            res[i] = 'g'
            s_list[i] = g_list[i] = None
    for i in range(5):
        if g_list[i] is not None:
            char = g_list[i]
            for j in range(5):
                if s_list[j] == char:
                    res[i] = 'y'
                    s_list[j] = None
                    break
    out = "".join(res)
    GLOBAL_FEEDBACK_CACHE[pair] = out
    return out


def get_color_terminal(word, pattern):
    bg_green, bg_yellow, bg_gray = "\033[48;2;83;141;78m", "\033[48;2;181;159;59m", "\033[48;2;58;58;60m"
    text_white, reset = "\033[1;97m", "\033[0m"
    colored_word = ""
    for char, p in zip(word.upper(), pattern):
        if p == 'g':
            colored_word += f"{bg_green}{text_white} {char} {reset}"
        elif p == 'y':
            colored_word += f"{bg_yellow}{text_white} {char} {reset}"
        else:
            colored_word += f"{bg_gray}{text_white} {char} {reset}"
    return colored_word


def get_emoji_pattern(pattern):
    emoji_map = {'g': '▓', 'y': '▒', '_': '░'}
    return "".join(emoji_map[c] for c in pattern)


# --- 3. PDF & TEXT TREE LOGIC ---
def print_distribution(dist):
    print("\nDISTRIBUTION")
    hex_colors = [
        "74;162;230",  # 1: Soft Blue
        "139;211;235",  # 2: Sky Blue
        "134;227;139",  # 3: Mint Green
        "182;240;130",  # 4: Chartreuse
        "240;229;140",  # 5: Straw Yellow
        "230;145;120",  # 6: Muted Terracotta Coral
        "242;162;177",  # 7 / X: Rose Pink
        "200;150;250"  # Extra slot security
    ]
    reset = "\033[0m"
    max_count = max(dist) if max(dist) > 0 else 1
    max_bar_width = 30

    for i in range(len(dist)):
        if i < MAX_TURNS:
            label = str(i + 1)
        else:
            label = "X"
        count = dist[i]

        raw_width = (count / max_count) * max_bar_width
        whole_blocks = int(raw_width)
        remainder = raw_width - whole_blocks

        fractional_char = ""
        if count > 0 and whole_blocks == 0:
            fractional_char = "▏"
        elif remainder > 0:
            fractions = ["", "▏", "▎", "▍", "▌", "▋", "▊", "▉"]
            frac_idx = int(remainder * 8)
            fractional_char = fractions[frac_idx]

        bar_str = "█" * whole_blocks + fractional_char
        rgb = hex_colors[i] if i < len(hex_colors) else "150;150;150"
        color_ansi = f"\033[38;2;{rgb}m"

        print(f"{label} {color_ansi}{bar_str:<31}{reset}{count}")


def export_tree_txt(start_word, results_dict):
    p_map = {'_': 0, 'y': 1, 'g': 2}
    sorted_targets = sorted(results_dict.keys(), key=lambda t: [[p_map.get(c) for c in s[1]] for s in results_dict[t]])

    filename = f"{start_word.upper()}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for target in sorted_targets:
            history = results_dict[target]
            words_path = [step[0] for step in history]
            f.write(",".join(words_path) + "\n")


def generate_tree_pdf(start_word, results_dict):
    if not HAS_PDF: return
    p_map = {'_': 0, 'y': 1, 'g': 2}
    sorted_targets = sorted(results_dict.keys(), key=lambda t: [[p_map.get(c) for c in s[1]] for s in results_dict[t]])
    c = canvas.Canvas(f"{start_word.upper()}_Answer_tree.pdf", pagesize=A4)
    w, h = A4
    y, box, margin = h - 80, 10, 1.5
    word_w, col_w = (box + margin) * 5, (box + margin) * 5 + 35
    colors_map = {'g': colors.HexColor("#538d4e"), 'y': colors.HexColor("#b59f3b"), '_': colors.HexColor("#3a3a3c")}
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, h - 40, f"WORDLE DECISION TREE: {start_word.upper()}")
    prev_h = None
    for target in sorted_targets:
        if y < 50: c.showPage(); y, prev_h = h - 60, None
        history, x = results_dict[target], 40
        for i, (word, pattern) in enumerate(history):
            is_rep = prev_h and i < len(prev_h) and prev_h[i] == (word, pattern)
            if is_rep:
                c.setFillColor(colors.black);
                c.setFont("Helvetica-Bold", 10);
                c.drawCentredString(x + word_w / 2, y + 2, "↓")
            else:
                for ci, pc in enumerate(pattern):
                    bx = x + (ci * (box + margin))
                    c.setFillColor(colors_map.get(pc, colors.gray));
                    c.rect(bx, y, box, box, stroke=0, fill=1)
                    c.setFillColor(colors.white);
                    c.setFont("Helvetica", 7);
                    c.drawCentredString(bx + box / 2, y + 2.5, word[ci].upper())
            if i < len(history) - 1:
                arrow = "↓" if prev_h and i + 1 < len(prev_h) and history[i] == prev_h[i] and history[i + 1] == prev_h[
                    i + 1] else "→"
                if is_rep and not (prev_h and i + 1 < len(prev_h) and prev_h[i + 1] == history[i + 1]): arrow = "→"
                c.setFillColor(colors.black);
                c.setFont("Helvetica-Bold", 10);
                c.drawCentredString(x + word_w + 15, y + 2, arrow)
            x += col_w
        prev_h, y = history, y - 18
    c.save()


# --- 4. CORE ANALYTICS ---
tree_memory = {}
SUBPOOL_SOLVER_CACHE = {}
BRANCH_PREDICTION_MATRIX = {}


@lru_cache(maxsize=445)
def get_entropy_score(word, pool_tuple):
    groups = {}
    for secret in pool_tuple:
        p = get_feedback(secret, word)
        groups[p] = groups.get(p, 0) + 1
    score = len(groups) - (sum(v * v for v in groups.values()) / 100000)
    if word in pool_tuple: score += 0.4
    return score


def calculate_analytics(candidate, pool, turn, history, limit_depth=10, show_limit=10, active_mode=1):
    total_turns, missed, stats, max_turn_achieved = 0, [], [0] * (MAX_TURNS + 2), 0
    missed_histories = {}
    pool_list = list(pool)
    eval_turn = turn + 1

    buckets = {}
    largest_group = 0
    for secret in pool_list:
        p = get_feedback(secret, candidate)
        if p not in buckets:
            buckets[p] = []
        buckets[p].append(secret)

    if buckets:
        largest_group = max(len(sub) for sub in buckets.values())

    for p, sub_pool in buckets.items():
        if p == "ggggg":
            total_turns += eval_turn * len(sub_pool)
            if eval_turn - 1 < len(stats):
                stats[eval_turn - 1] += len(sub_pool)
            if eval_turn > max_turn_achieved:
                max_turn_achieved = eval_turn
            continue

        if len(sub_pool) == 1:
            res_t = eval_turn + 1
            if res_t > MAX_TURNS:
                secret_word = sub_pool[0]
                missed.append(secret_word)
                current_full_history = [step[0] for step in history] + [candidate, secret_word]
                missed_histories[secret_word] = current_full_history

                total_turns += (MAX_TURNS + 1) * len(sub_pool)
                if MAX_TURNS < len(stats): stats[MAX_TURNS] += len(sub_pool)
                max_turn_achieved = MAX_TURNS + 1
            else:
                total_turns += res_t * len(sub_pool)
                if res_t - 1 < len(stats): stats[res_t - 1] += len(sub_pool)
                if res_t > max_turn_achieved: max_turn_achieved = res_t
            continue

        child_guess = get_best_move(tuple(sub_pool), candidate, p, tuple(history + [(candidate, p)]),
                                    limit_depth=limit_depth, show_limit=show_limit, active_mode=0)

        for secret in sub_pool:
            s_p, s_g, s_t, s_hist = sub_pool.copy(), child_guess, eval_turn + 1, list(history) + [(candidate, p)]
            while s_t <= MAX_TURNS:
                sp_p = get_feedback(secret, s_g)
                s_hist.append((s_g, sp_p))
                if sp_p == "ggggg":
                    total_turns += s_t
                    if s_t - 1 < len(stats): stats[s_t - 1] += 1
                    if s_t > max_turn_achieved: max_turn_achieved = s_t
                    break
                s_p = [w for w in s_p if get_feedback(w, s_g) == sp_p]
                if not s_p: break
                if len(s_p) == 1:
                    res_t = s_t + 1
                    if res_t > MAX_TURNS:
                        if secret not in missed:
                            missed.append(secret)
                            current_full_history = [step[0] for step in s_hist] + [s_p[0]]
                            missed_histories[secret] = current_full_history
                        total_turns += (MAX_TURNS + 1)
                        if MAX_TURNS < len(stats): stats[MAX_TURNS] += 1
                        max_turn_achieved = MAX_TURNS + 1
                    else:
                        total_turns += res_t
                        if res_t - 1 < len(stats): stats[res_t - 1] += 1
                        if res_t > max_turn_achieved: max_turn_achieved = res_t
                    break
                s_t += 1
                if s_t > MAX_TURNS:
                    if secret not in missed:
                        missed.append(secret)
                        current_full_history = [step[0] for step in s_hist]
                        missed_histories[secret] = current_full_history
                    total_turns += (MAX_TURNS + 1)
                    if MAX_TURNS < len(stats): stats[MAX_TURNS] += 1
                    max_turn_achieved = MAX_TURNS + 1
                    break

                s_g = get_best_move(tuple(s_p), s_g, sp_p, tuple(s_hist), limit_depth=limit_depth, show_limit=show_limit, active_mode=0)

    win_p = (len(pool) - len(missed)) / len(pool) * 100 if pool else 0
    avg_t = total_turns / len(pool) if pool else 0
    pool_tuple = tuple(pool)

    if max_turn_achieved > MAX_TURNS or len(missed) > 0 or win_p < 100.0:
        true_max_turn = max(max_turn_achieved, MAX_TURNS + 1)
    else:
        true_max_turn = max_turn_achieved

    return win_p, avg_t, true_max_turn, missed, stats, (candidate in pool), get_entropy_score(candidate,
                                                                                              pool_tuple), largest_group, missed_histories


def evaluate_and_rank_moves(pool, final_word, p, turn, history, limit, show_limit=10, active_mode=1):
    pool_tuple = tuple(pool)

    if len(pool_tuple) <= 2:
        return [{
            'word': pool_tuple[0], 'win_p': 100.0, 'exp': 1.0, 'worst': 1,
            'missed': [], 'stats': [0] * (MAX_TURNS + 2), 'isa': 1, 'entropy': 0.0, 'six_games': 0, 'five_p': 0,
            'largest': 0, 'will_lose': False, 'missed_histories': {}
        }]

    cache_matrix_key = (pool_tuple, limit, turn, show_limit)
    if cache_matrix_key in BRANCH_PREDICTION_MATRIX:
        if len(BRANCH_PREDICTION_MATRIX[cache_matrix_key]) >= show_limit:
            return BRANCH_PREDICTION_MATRIX[cache_matrix_key]

    active_pool = full_dictionary
    entropy_list = sorted([(w, get_entropy_score(w, pool_tuple)) for w in active_pool], key=lambda x: x[1],
                          reverse=True)

    enriched = []
    total_to_evaluate = min(show_limit, len(entropy_list))

    for i, (w, ent) in enumerate(entropy_list[:show_limit], 1):
        if active_mode == 1:
            # Displays custom limit readout properly (e.g., Progress: Evaluating candidate 1/20, 1/50, etc.)
            sys.stdout.write(f"\rProgress: Evaluating candidate {i}/{total_to_evaluate} ({w.upper()})...")
            sys.stdout.flush()

        res = calculate_analytics(w, pool, turn, history, limit_depth=limit, show_limit=show_limit, active_mode=active_mode)
        six_count = res[4][5] if len(res[4]) > 5 else 0
        five_p_and_above = sum(res[4][4:]) if len(res[4]) > 4 else 0

        is_loss_risk = len(res[3]) > 0 or res[2] > MAX_TURNS or res[0] < 100.0

        enriched.append({
            'word': w, 'win_p': res[0], 'exp': res[1], 'worst': res[2],
            'missed': res[3], 'stats': res[4], 'isa': int(res[5]), 'entropy': res[6],
            'six_games': six_count, 'five_p': five_p_and_above, 'largest': res[7],
            'will_lose': is_loss_risk, 'missed_histories': res[8]
        })

    if active_mode == 1:
        sys.stdout.write("\r\033[K")
        sys.stdout.flush()

    if len(enriched) < show_limit:
        needed = show_limit - len(enriched)
        for _ in range(needed):
            enriched.append({
                'word': "-----", 'win_p': 0.0, 'exp': 0.0, 'worst': 99,
                'missed': [], 'stats': [0] * (MAX_TURNS + 2), 'isa': 0, 'entropy': 0.0,
                'six_games': 99999, 'five_p': 99999, 'largest': 99999, 'will_lose': True, 'missed_histories': {}
            })

    enriched.sort(
        key=lambda x: (
            x['will_lose'],
            -x['win_p'],
            x['exp'],
            x['worst'],
            x['six_games'],
            x['five_p'],
            x['largest'],
            x['word']
        )
    )

    BRANCH_PREDICTION_MATRIX[cache_matrix_key] = enriched
    return enriched


def get_best_move(pool, prev_guess, last_p, history_tuple, limit_depth=10, show_limit=10, fixed_sequence=None,
                  active_mode=1):
    current_turn_index = len(history_tuple)
    if fixed_sequence and current_turn_index < len(fixed_sequence):
        return fixed_sequence[current_turn_index]

    if len(pool) <= 2:
        return pool[0]

    cache_key = (history_tuple, limit_depth, current_turn_index, show_limit)
    if cache_key in tree_memory: return tree_memory[cache_key]

    enriched = evaluate_and_rank_moves(list(pool), prev_guess, last_p, current_turn_index, list(history_tuple),
                                       limit=limit_depth, show_limit=show_limit, active_mode=active_mode)
    best_word = enriched[0]['word']
    tree_memory[cache_key] = best_word
    return best_word


def get_share_stats(turns, history):
    emoji_map = {'g': '🟩', 'y': '🟨', '_': '⬛'}
    grid = "".join(["".join(emoji_map[c] for c in p) + "\n" for _, p in history])
    score = "X" if turns > MAX_TURNS else turns
    return f"WOBOT {score}/{MAX_TURNS}\n\n{grid}"


# --- 5. STARTING WORD TEST LOGIC ---
def run_starting_word_test(start_word, limit, show_limit=10):
    print(f"\n--- Starting Word Test: {start_word.upper()} ---")
    groups = {}
    for word in proper_word:
        p = get_feedback(word, start_word)
        if p not in groups: groups[p] = []
        groups[p].append(word)

    p_rank = {'_': '0', 'y': '1', 'g': '2'}
    sorted_patterns = sorted(groups.keys(), key=lambda p: "".join(p_rank[c] for c in p))

    total_proper = len(proper_word)
    for p in sorted_patterns:
        sub_pool = groups[p]
        history = ((start_word, p),)
        bits = math.log2(total_proper / len(sub_pool))
        next_move = get_best_move(tuple(sub_pool), start_word, p, history, limit_depth=limit, show_limit=show_limit, active_mode=5)
        res = calculate_analytics(next_move, sub_pool, 1, history, limit_depth=limit, show_limit=show_limit, active_mode=5)
        avg_left = res[1] - 1
        loss_marker = " [WILL LOSE!]" if (len(res[3]) > 0 or res[2] > MAX_TURNS or res[0] < 100.0) else ""

        print(f"{start_word.upper()} {get_emoji_pattern(p)} -> {next_move.upper()} "
              f"(≤{avg_left:.2f} left, {len(sub_pool)} words left, ~{bits:.2f} bits){loss_marker}")


# --- 6. EXECUTION ---
def run_game(mode, limit, start_word, target=None, fixed_sequence=None, show_limit=10):
    pool, turn, history = proper_word.copy(), 0, []
    solve_path_plain, solve_path_colored, full_history = [], [], []
    current_guess, user_manual_guess = start_word, None

    while turn < MAX_TURNS:
        turn += 1
        if mode in [2, 3, 4, 6, 7]:
            p = get_feedback(target, current_guess)
        else:
            while True:
                user_input = input(f"\nPattern for '{current_guess.upper()}': ").lower().strip()
                raw = user_input.split()
                if not raw: continue
                user_manual_guess, p = (raw[0].lower(), raw[1]) if len(raw) > 1 else (None, raw[0])
                if len(p) == 5 and all(c in 'gy_' for c in p): break

        final_word = user_manual_guess if user_manual_guess else current_guess
        solve_path_plain.append(final_word)
        solve_path_colored.append(get_color_terminal(final_word, p))
        full_history.append((final_word, p))

        if mode == 1 and turn > 1:
            u_res = calculate_analytics(final_word, pool, turn - 1, history, limit_depth=limit, show_limit=show_limit, active_mode=mode)
            print(f"Your guess {final_word.upper()} needs an average of ≤{u_res[1] - (turn - 1):.3f}")

        if p == "ggggg": break
        pool = [w for w in pool if get_feedback(w, final_word) == p]
        history.append((final_word, p))

        if turn < MAX_TURNS:
            if fixed_sequence and turn < len(fixed_sequence):
                current_guess = fixed_sequence[turn]
            else:
                state_key = (tuple(pool), limit, final_word, p, turn, show_limit)
                if mode == 7 and state_key in UNIFIED_COEXISTENCE_CACHE:
                    current_guess = UNIFIED_COEXISTENCE_CACHE[state_key]
                else:
                    enriched = evaluate_and_rank_moves(pool, final_word, p, turn, history, limit, show_limit=show_limit,
                                                       active_mode=mode)
                    if mode == 1:
                        print("Progress: 100%")
                        print(
                            f"\nWORD          | WIN %   | EXP (DIFF)         | WORST | ANS?   | LOSE? | STATS\n" + "-" * 85)
                        base_exp = enriched[0]['exp']

                        for item in enriched[:show_limit]:
                            diff = item['exp'] - base_exp
                            lose_str = "YES" if item['will_lose'] else "NO"
                            print(
                                f"{item['word'].upper():13} | {item['win_p']:7.1f} | {item['exp']:6.3f} ({diff:+.3f})  | {str(item['worst']):5} | {str(bool(item['isa'])):6} | {lose_str:5} | {item['stats']}")

                        print("\nDETAILED ANALYSIS DISCOVERIES:")
                        for item in enriched[:show_limit]:
                            w_upper = item['word'].upper()
                            if not item['missed_histories']:
                                print(f"{w_upper}: MIGHT'VE LOST ON: — (nothing)")
                            else:
                                fail_segments = []
                                for m_word, path_list in sorted(item['missed_histories'].items()):
                                    path_str = ", ".join(w.upper() for w in path_list)
                                    fail_segments.append(f"{m_word.upper()} [{path_str}]")
                                print(f"{w_upper}: MIGHT'VE LOST ON: {', '.join(fail_segments)}")

                    current_guess = enriched[0]['word']
                    if mode == 7:
                        UNIFIED_COEXISTENCE_CACHE[state_key] = current_guess

    res_turns = turn if (full_history and full_history[-1][1] == "ggggg") else (MAX_TURNS + 1)
    if mode in [1, 3]: print("\n" + get_share_stats(res_turns, full_history))
    return res_turns, solve_path_colored, solve_path_plain, full_history, pool


def main():
    global MAX_TURNS
    print(
        "WOBOT - The Wordle Solver\nWORDLISTS (1: Orig, 2: NYT, 3: Alex Selby, 4: Answers only, 5: WordleBot, 6: NYT release for the 2309 wordlist)")
    try:
        wl_choice = int(input("Select Wordlist: "))
        load_data(wl_choice)

        try:
            max_input = input("Set Max Guess limit (Press Enter for default 6): ").strip()
            if max_input:
                MAX_TURNS = int(max_input)
        except ValueError:
            print("Invalid bound value. Defaulting to 6.")
            MAX_TURNS = 6

        print(
            "\n1: Analysis\n2: 500 Random Tests\n3: Bot Playthrough\n4: Cumulative\n5: Starting Word Test\n6: Test Word Pairs Sequence\n7: Exhaustive Whole Cumulative")
        mode = int(input("Select Mode: "))
        limit = int(input("LIMIT (Depth): "))

        show_limit = 10
        try:
            show_input = input("How many words to show in analysis list? (Press Enter for default 10): ").strip()
            if show_input:
                show_limit = int(show_input)
        except ValueError:
            show_limit = 10

        fixed_sequence = None
        if mode == 6:
            pair_input = input(
                "Type your explicit test sequence (e.g., parse,clint or stare,cloud,pinky): ").lower().strip()
            fixed_sequence = [w.strip() for w in pair_input.split(",") if len(w.strip()) == 5]
            if not fixed_sequence:
                sys.exit("Error: No valid words found in entry string sequence pattern.")
            start_w = fixed_sequence[0]
        elif mode == 7:
            start_w = ""
        else:
            start_w = input("Starting Word: ").lower().strip()

    except ValueError:
        sys.exit("Invalid Input.")

    if mode == 5:
        run_starting_word_test(start_w, limit, show_limit=show_limit)
    elif mode == 1:
        run_game(1, limit, start_w, show_limit=show_limit)
    elif mode == 7:
        total_wordlist_len = len(word_list)
        total_proper_len = len(proper_word)
        print(
            f"\nExecuting Exhaustive Matrix Mode... (Evaluating {total_wordlist_len} Starters × {total_proper_len} Answers)")
        exhaustive_results = []

        global_start_time = time.perf_counter()

        for s_idx, starter in enumerate(word_list):
            total_turns = 0
            stats = [0] * (MAX_TURNS + 2)
            missed_count = 0
            worst_turn = 0

            puzzle_start_time = time.perf_counter()

            buckets = {}
            for target in proper_word:
                p = get_feedback(target, starter)
                if p not in buckets:
                    buckets[p] = []
                buckets[p].append(target)
            starter_largest_group = max(len(sub) for sub in buckets.values()) if buckets else 0

            for t_idx, target in enumerate(proper_word):
                turns, path_col, path_plain, hist, final_pool = run_game(7, limit, starter, target=target,
                                                                         show_limit=show_limit)

                if turns > MAX_TURNS:
                    missed_count += 1
                    total_turns += (MAX_TURNS + 1)
                    stats[MAX_TURNS] += 1
                    if (MAX_TURNS + 1) > worst_turn:
                        worst_turn = MAX_TURNS + 1
                else:
                    total_turns += turns
                    stats[turns - 1] += 1
                    if turns > worst_turn:
                        worst_turn = turns

                completed_starters = s_idx
                current_starter_progress = (t_idx + 1) / total_proper_len
                effective_starters = completed_starters + current_starter_progress
                pct = (effective_starters / total_wordlist_len) * 100

                bar_len = 20
                filled_len = int(bar_len * pct / 100)
                p_bar = "█" * filled_len + "-" * (bar_len - filled_len)

                # Added an explicit '/100%' numerical output readout string hook right after the floating-point token tracker
                sys.stdout.write(
                    f"\r\033[KProgress: {pct:5.2f}%/100% |[{p_bar}]| STARTER: {starter.upper()} ({s_idx + 1}/{total_wordlist_len}) | TARGET: {target.upper()} ({t_idx + 1}/{total_proper_len})")
                sys.stdout.flush()

            puzzle_end_time = time.perf_counter()
            puzzle_duration_ms = (puzzle_end_time - puzzle_start_time) * 1000

            win_p = ((len(proper_word) - missed_count) / len(proper_word)) * 100
            avg_turns = total_turns / len(proper_word)
            six_games_count = stats[5] if len(stats) > 5 else 0
            five_p_and_above = sum(stats[4:])
            isa_flag = int(starter in proper_word)
            has_loss = "YES" if (missed_count > 0 or worst_turn > MAX_TURNS or win_p < 100.0) else "NO"

            formatted_stats = {}
            for i in range(MAX_TURNS):
                if stats[i] > 0:
                    formatted_stats[i + 1] = stats[i]
            if stats[MAX_TURNS] > 0:
                formatted_stats[MAX_TURNS + 1] = stats[MAX_TURNS]

            sorted_stats_dict = dict(sorted(formatted_stats.items()))

            entry = {
                'word': starter,
                'win_p': win_p,
                'exp': avg_turns,
                'worst': worst_turn,
                'six_games': six_games_count,
                'five_p': five_p_and_above,
                'largest': starter_largest_group,
                'isa': isa_flag,
                'stats_str': str(sorted_stats_dict),
                'total_guesses': total_turns,
                'will_lose_flag': has_loss
            }
            exhaustive_results.append(entry)

            print(
                f"\n>>> FINISHED: {starter.upper()} ({s_idx + 1}/{total_wordlist_len}) Total Guesses: {total_turns} | Avg: {avg_turns:.14f} | Lose Risk: {has_loss} | Time: {puzzle_duration_ms:.2f} ms\n" + "=" * 50)

        exhaustive_results.sort(
            key=lambda x: (x['will_lose_flag'] == "YES", -x['win_p'], x['exp'], x['worst'], x['six_games'], x['five_p'],
                           x['largest'], x['word']))

        global_end_time = time.perf_counter()
        global_duration_secs = global_end_time - global_start_time

        output_filename = "exhaustive_stats.txt"
        with open(output_filename, "w", encoding="utf-8") as f:
            for item in exhaustive_results:
                f.write(
                    f"{item['word'].upper()} ({item['word']}, {item['exp']:.14f}, LOSE_RISK: {item['will_lose_flag']}, {item['stats_str']}) Total Guesses: {item['total_guesses']}\n")

        print(f"\nExhaustive Run Complete! Master stats successfully exported to '{output_filename}'.")
        print(f"Total Processing Time Taken: {global_duration_secs:.4f} seconds.")
    else:
        targets = []
        if mode == 2:
            targets = random.sample(proper_word, min(500, len(proper_word)))
        elif mode == 3:
            targets = [input("Target word: ").lower().strip()]
        elif mode in [4, 6]:
            targets = proper_word

        total_turns, pdf_data, dist = 0, {}, [0] * (MAX_TURNS + 1)
        batch_start_time = time.perf_counter()

        for i, t in enumerate(targets):
            pct = (i / len(targets)) * 100
            bar_len = 20
            filled_len = int(bar_len * pct / 100)
            p_bar = "█" * filled_len + "-" * (bar_len - filled_len)

            # Added explicit '/100%' format tracker readout inside the classic simulation loop configuration blocks
            sys.stdout.write(
                f"\r\033[KProgress: {pct:.1f}%/100% |[{p_bar}]| Simulating target {i + 1}/{len(targets)} ({t.upper()})...")
            sys.stdout.flush()

            turns, path_col, path_plain, hist, final_pool = run_game(mode, limit, start_w, target=t,
                                                                     fixed_sequence=fixed_sequence,
                                                                     show_limit=show_limit)

            idx = min(turns - 1, MAX_TURNS)
            dist[idx] += 1
            total_turns += turns
            pdf_data[t] = hist

        sys.stdout.write("\r\033[K")
        sys.stdout.flush()

        print("Progress: 100%/100% [Complete]")
        batch_duration = time.perf_counter() - batch_start_time

        if mode in [2, 4, 6]:
            print(f"\nFINAL STATISTICS")
            print(f"Total Guesses Taken for {start_w.lower()}: {total_turns}")
            print(f"Avg Steps: {total_turns / len(targets):.4f}")
            print(f"Total Processing Time Taken: {batch_duration:.4f} seconds.")
            print_distribution(dist)
            generate_tree_pdf(start_w, pdf_data)
            export_tree_txt(start_w, pdf_data)


if __name__ == "__main__":
    main()
