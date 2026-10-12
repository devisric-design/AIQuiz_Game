"""
AI Quiz Arena - DSC401-6 Artificial Intelligence (Units I & II)
Interactive quiz game built with Streamlit.

Features: difficulty levels, topic filter, random questions, per-question timer,
progress bar, immediate feedback with explanations, lifelines (50-50, Hint, Skip),
streak bonus, final report with topic analysis, leaderboard, CSV download.

Run:  streamlit run app.py
"""
import copy
import datetime
import json
import os
import random
import time

import pandas as pd
import streamlit as st

from questions import QUESTIONS

st.set_page_config(page_title="AI Quiz Arena", page_icon="🤖", layout="centered")

# ----------------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------------
LB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leaderboard.json")
BASE_POINTS = {"Easy": 10, "Medium": 15, "Hard": 20}
HINT_COST, FIFTY_COST, STREAK_BONUS, MIN_POINTS = 3, 5, 5, 2
TOPICS = sorted({q["topic"] for q in QUESTIONS})
PLACEHOLDER = "-- choose --"
LEVEL_ICON = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

# ----------------------------------------------------------------------------
# Leaderboard (JSON file; falls back to session if the file system is read-only)
# ----------------------------------------------------------------------------
def load_leaderboard():
    try:
        with open(LB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return st.session_state.get("_lb_fallback", [])


def save_leaderboard(entries):
    st.session_state["_lb_fallback"] = entries
    try:
        with open(LB_FILE, "w", encoding="utf-8") as f:
            json.dump(entries, f, indent=2)
    except Exception:
        pass


# ----------------------------------------------------------------------------
# Session state
# ----------------------------------------------------------------------------
def reset_game():
    keep = {k: st.session_state[k] for k in ("_lb_fallback",) if k in st.session_state}
    st.session_state.clear()
    st.session_state.update(keep)
    st.session_state.update(
        stage="start", qs=[], i=0, score=0, streak=0, best_streak=0, correct=0,
        results=[], phase="answering", started=0.0, timer=30,
        hints_left=3, fifty_left=2, skip_left=1,
        hint_used=False, fifty_used=False, removed=[], name="Player",
        level="All", lb_saved=False, last=None,
    )


if "stage" not in st.session_state:
    reset_game()

S = st.session_state


# ----------------------------------------------------------------------------
# Game logic
# ----------------------------------------------------------------------------
def build_quiz(name, level, n, timer, topics, shuffle_q):
    pool = [q for q in QUESTIONS
            if (level == "All" or q["level"] == level) and q["topic"] in topics]
    if shuffle_q:
        random.shuffle(pool)
    pool = pool[:n]
    quiz = []
    for q in pool:
        q = copy.deepcopy(q)
        if q["type"] in ("MCQ", "Scenario", "Problem Solving"):
            q["opts"] = random.sample(q["options"], len(q["options"]))
        elif q.get("options"):
            q["opts"] = list(q["options"])      # True/False & Assertion-Reason keep fixed order
        if q["type"] == "Match the Following":
            q["rights"] = random.sample([r for _, r in q["pairs"]], len(q["pairs"]))
        quiz.append(q)
    S.update(stage="quiz", qs=quiz, i=0, score=0, streak=0, best_streak=0, correct=0,
             results=[], phase="answering", timer=timer, name=name or "Player",
             level=level, hints_left=3, fifty_left=2, skip_left=1, lb_saved=False,
             last=None)
    start_question()


def start_question():
    S.phase = "answering"
    S.started = time.time()
    S.hint_used = False
    S.fifty_used = False
    S.removed = []


def current():
    return S.qs[S.i]


def collect_answer(q):
    """Read the user's current answer from widget state."""
    i = S.i
    if q["type"] == "Fill in the Blanks":
        return (S.get(f"ans_{i}") or "").strip()
    if q["type"] == "Match the Following":
        ans = {}
        for j, (left, _) in enumerate(q["pairs"]):
            ans[left] = S.get(f"m_{i}_{j}", PLACEHOLDER)
        return ans
    return S.get(f"ans_{i}")


def is_answered(q, ans):
    if q["type"] == "Match the Following":
        return all(v != PLACEHOLDER for v in ans.values())
    return bool(ans)


def check(q, ans):
    if q["type"] == "Fill in the Blanks":
        return ans.strip().lower() in [a.lower() for a in q["accept"]]
    if q["type"] == "Match the Following":
        return all(dict(q["pairs"])[left] == right for left, right in ans.items())
    return ans == q["answer"]


def remaining_time():
    if not S.timer:
        return None
    return S.timer - (time.time() - S.started)


def resolve(ans=None, timeout=False):
    q = current()
    rem = remaining_time()
    correct = False if timeout or ans is None else check(q, ans)
    pts, detail = 0, []
    if correct:
        base = BASE_POINTS[q["level"]]
        pts = base
        detail.append(f"Base ({q['level']}): +{base}")
        if S.hint_used:
            pts -= HINT_COST
            detail.append(f"Hint used: -{HINT_COST}")
        if S.fifty_used:
            pts -= FIFTY_COST
            detail.append(f"50-50 used: -{FIFTY_COST}")
        pts = max(pts, MIN_POINTS)
        if rem is not None and rem > 0:
            tb = int(rem // 10)
            if tb:
                pts += tb
                detail.append(f"Speed bonus: +{tb}")
        S.streak += 1
        S.best_streak = max(S.best_streak, S.streak)
        if S.streak >= 3:
            pts += STREAK_BONUS
            detail.append(f"Streak x{S.streak}: +{STREAK_BONUS}")
        S.correct += 1
    else:
        S.streak = 0
    S.score += pts
    S.results.append(dict(
        no=S.i + 1, topic=q["topic"], level=q["level"], type=q["type"], q=q["q"],
        correct=correct, timeout=timeout, skipped=False, points=pts,
        answer=q["answer"], exp=q["exp"],
    ))
    S.last = dict(correct=correct, timeout=timeout, points=pts, detail=detail)
    S.phase = "feedback"


def go_next():
    if S.i + 1 >= len(S.qs):
        S.stage = "result"
    else:
        S.i += 1
        start_question()


def use_hint():
    if S.hints_left > 0 and not S.hint_used:
        S.hints_left -= 1
        S.hint_used = True


def use_fifty():
    q = current()
    if S.fifty_left > 0 and not S.fifty_used and q.get("opts") and len(q["opts"]) > 2:
        wrong = [o for o in q["opts"] if o != q["answer"]]
        S.removed = random.sample(wrong, 2)
        S.fifty_left -= 1
        S.fifty_used = True


def use_skip():
    if S.skip_left > 0:
        S.skip_left -= 1
        q = current()
        S.results.append(dict(
            no=S.i + 1, topic=q["topic"], level=q["level"], type=q["type"], q=q["q"],
            correct=False, timeout=False, skipped=True, points=0,
            answer=q["answer"], exp=q["exp"],
        ))
        S.streak = 0
        go_next()


# ----------------------------------------------------------------------------
# UI pieces
# ----------------------------------------------------------------------------
def start_screen():
    st.title("🤖 AI Quiz Arena")
    st.caption("DSC401-6 Artificial Intelligence · Units I & II · Christ (Deemed to be University)")
    st.markdown(
        "Test your knowledge of **agents, search, heuristics, CSPs and more**. "
        "Earn points for correct answers, speed and streaks - but lifelines cost points!"
    )

    name = st.text_input("Your name", value=S.name if S.name != "Player" else "")
    c1, c2 = st.columns(2)
    level = c1.selectbox("Difficulty level", ["All", "Easy", "Medium", "Hard"])
    timer = c2.selectbox("Time per question", [30, 45, 60, 90, 0],
                         format_func=lambda x: "No timer" if x == 0 else f"{x} seconds")
    topics = st.multiselect("Topics", TOPICS, default=TOPICS)
    pool_size = len([q for q in QUESTIONS
                     if (level == "All" or q["level"] == level) and q["topic"] in topics])
    if pool_size == 0:
        st.warning("No questions match this selection. Choose more topics or another level.")
        return
    options = sorted({min(n, pool_size) for n in (10, 20, 30, 50, pool_size)})
    n = st.select_slider("Number of questions", options=options, value=min(10, pool_size))
    shuffle_q = st.checkbox("Randomise question order", value=True)

    with st.expander("📜 Rules, scoring & lifelines"):
        st.markdown(
            f"""
- **Points:** Easy {BASE_POINTS['Easy']} · Medium {BASE_POINTS['Medium']} · Hard {BASE_POINTS['Hard']}
- **Speed bonus:** +1 point for every 10 seconds left when you answer correctly
- **Streak bonus:** +{STREAK_BONUS} points from the 3rd correct answer in a row
- **Lifelines:** 💡 Hint ×3 (−{HINT_COST} pts) · ✂️ 50-50 ×2 (−{FIFTY_COST} pts, choice questions only) · ⏭️ Skip ×1 (no points)
- When time runs out the question is marked wrong.
- Final score is saved to the **leaderboard**.
            """
        )
    st.info(f"Question bank: **{len(QUESTIONS)}** questions across **{len(TOPICS)}** topics.")
    if st.button("🚀 Start Quiz", type="primary", use_container_width=True):
        build_quiz(name.strip(), level, n, timer, topics, shuffle_q)
        st.rerun()

    show_leaderboard(compact=True)


def sidebar_panel():
    with st.sidebar:
        st.header(f"👤 {S.name}")
        st.metric("Score", S.score)
        c1, c2 = st.columns(2)
        c1.metric("Correct", f"{S.correct}/{len(S.results)}")
        c2.metric("Streak 🔥", S.streak)
        st.divider()
        st.subheader("Lifelines")
        st.write(f"💡 Hints left: **{S.hints_left}**")
        st.write(f"✂️ 50-50 left: **{S.fifty_left}**")
        st.write(f"⏭️ Skips left: **{S.skip_left}**")
        st.divider()
        if st.button("🔄 Quit & restart"):
            reset_game()
            st.rerun()


@st.fragment(run_every=1)
def timer_box():
    """Countdown that refreshes every second without re-running the whole app."""
    if S.stage != "quiz" or S.phase != "answering" or not S.timer:
        return
    rem = remaining_time()
    if rem <= 0:
        resolve(ans=None, timeout=True)
        st.rerun()
    ratio = max(0.0, min(1.0, rem / S.timer))
    st.progress(ratio, text=f"⏱️ {int(rem)} s left")


def answer_widgets(q):
    i = S.i
    t = q["type"]
    if t == "Fill in the Blanks":
        st.text_input("Type your answer", key=f"ans_{i}")
    elif t == "Match the Following":
        for j, (left, _) in enumerate(q["pairs"]):
            st.selectbox(f"**{left}**", [PLACEHOLDER] + q["rights"], key=f"m_{i}_{j}")
    else:
        opts = [o for o in q["opts"] if o not in S.removed]
        if t == "Assertion-Reason":
            st.radio("Choose the correct option", opts, index=None, key=f"ans_{i}")
        else:
            st.radio("Choose one", opts, index=None, key=f"ans_{i}")


def quiz_screen():
    sidebar_panel()
    q = current()
    total = len(S.qs)
    st.progress(S.i / total, text=f"Question {S.i + 1} of {total}")
    st.caption(f"{LEVEL_ICON[q['level']]} {q['level']} · 📚 {q['topic']} · 🧩 {q['type']}")

    if S.phase == "answering":
        timer_box()
    st.markdown(f"### {q['q']}" if "\n" not in q["q"] and "```" not in q["q"] else q["q"])

    if S.phase == "answering":
        if S.hint_used:
            st.info(f"💡 **Hint:** {q['hint']}")
        answer_widgets(q)

        c1, c2, c3, c4 = st.columns([2, 1.2, 1.2, 1.2])
        if c1.button("✅ Submit answer", type="primary", use_container_width=True):
            ans = collect_answer(q)
            if not is_answered(q, ans):
                st.warning("Please answer before submitting.")
            else:
                resolve(ans)
                st.rerun()
        c2.button("💡 Hint", on_click=use_hint, disabled=S.hints_left == 0 or S.hint_used,
                  use_container_width=True)
        can_fifty = (S.fifty_left > 0 and not S.fifty_used
                     and bool(q.get("opts")) and len(q["opts"]) > 2)
        c3.button("✂️ 50-50", on_click=use_fifty, disabled=not can_fifty,
                  use_container_width=True)
        c4.button("⏭️ Skip", on_click=use_skip, disabled=S.skip_left == 0,
                  use_container_width=True)
    else:
        feedback_view(q)


def feedback_view(q):
    last = S.last
    if last["timeout"]:
        st.error("⏰ Time's up!")
    elif last["correct"]:
        st.success(f"✅ Correct!  +{last['points']} points")
        if last["detail"]:
            st.caption(" · ".join(last["detail"]))
    else:
        st.error("❌ Incorrect")

    if q["type"] == "Match the Following":
        st.markdown("**Correct matches:**")
        for left, right in q["pairs"]:
            st.markdown(f"- **{left}** → {right}")
    else:
        st.markdown(f"**Correct answer:** {q['answer']}")
    st.info(f"📖 **Explanation:** {q['exp']}")

    label = "🏁 Finish quiz" if S.i + 1 >= len(S.qs) else "➡️ Next question"
    if st.button(label, type="primary", use_container_width=True):
        go_next()
        st.rerun()


def rank_title(acc):
    if acc >= 90:
        return "🏆 AI Grandmaster"
    if acc >= 75:
        return "🥇 Search Strategist"
    if acc >= 50:
        return "🥈 Rational Agent"
    return "🥉 Learning Agent - keep training!"


def show_leaderboard(compact=False):
    entries = sorted(load_leaderboard(), key=lambda e: (-e["score"], -e["accuracy"]))
    if not entries:
        return
    st.subheader("🏅 Leaderboard")
    df = pd.DataFrame(entries[:10 if not compact else 5])
    df.index = range(1, len(df) + 1)
    df = df[["name", "score", "correct", "total", "accuracy", "level", "date"]]
    df.columns = ["Player", "Score", "Correct", "Questions", "Accuracy %", "Level", "Date"]
    st.dataframe(df, use_container_width=True)


def result_screen():
    sidebar_panel()
    total = len(S.qs)
    answered = len(S.results)
    acc = round(100 * S.correct / total, 1) if total else 0
    st.title("🎉 Quiz complete!")
    st.subheader(rank_title(acc))
    if acc >= 75 and not S.get("_balloons"):
        st.balloons()
        S["_balloons"] = True

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Final score", S.score)
    c2.metric("Correct", f"{S.correct}/{total}")
    c3.metric("Accuracy", f"{acc}%")
    c4.metric("Best streak", S.best_streak)

    if not S.lb_saved:
        entries = load_leaderboard()
        entries.append(dict(name=S.name, score=S.score, correct=S.correct, total=total,
                            accuracy=acc, level=S.level,
                            date=datetime.date.today().isoformat()))
        save_leaderboard(entries)
        S.lb_saved = True

    df = pd.DataFrame(S.results)
    st.subheader("📊 Topic-wise performance")
    topic_df = (df.groupby("topic")["correct"].agg(["sum", "count"]).reset_index())
    topic_df["Accuracy %"] = (100 * topic_df["sum"] / topic_df["count"]).round(0)
    topic_df.columns = ["Topic", "Correct", "Attempted", "Accuracy %"]
    st.bar_chart(topic_df.set_index("Topic")["Accuracy %"])
    weak = topic_df[topic_df["Accuracy %"] < 60]["Topic"].tolist()
    if weak:
        st.warning("📌 Revise these topics: " + ", ".join(weak))
    else:
        st.success("Great coverage - no weak topics detected!")

    wrong = [r for r in S.results if not r["correct"]]
    if wrong:
        with st.expander(f"🔍 Review {len(wrong)} question(s) you missed or skipped"):
            for r in wrong:
                tag = "⏭️ skipped" if r["skipped"] else ("⏰ timed out" if r["timeout"] else "❌ wrong")
                st.markdown(f"**Q{r['no']}. {r['q']}**  \n_{r['topic']} · {tag}_")
                if r["type"] == "Match the Following":
                    st.markdown("Correct: see the question bank for the pairs.")
                else:
                    st.markdown(f"**Answer:** {r['answer']}")
                st.caption(r["exp"])
                st.divider()

    csv = df.drop(columns=["q", "exp"]).to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download my result (CSV)", csv, file_name="ai_quiz_result.csv",
                       mime="text/csv")
    show_leaderboard()
    if st.button("🔁 Play again", type="primary", use_container_width=True):
        reset_game()
        st.rerun()


# ----------------------------------------------------------------------------
# Router
# ----------------------------------------------------------------------------
if S.stage == "start":
    start_screen()
elif S.stage == "quiz":
    quiz_screen()
else:
    result_screen()
