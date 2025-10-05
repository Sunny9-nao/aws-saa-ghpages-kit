
import csv, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(__file__))
INPUT = os.path.join(ROOT, "progress.csv")
OUTPUT = os.path.join(ROOT, "docs", "Progress Weekly Summary.md")

def main():
    if not os.path.exists(INPUT):
        open(OUTPUT, "w", encoding="utf-8").write("# Progress Weekly Summary\n\nデータがありません。progress.csv を更新してください。")
        return

    by_week = defaultdict(lambda: {"planned":0.0,"actual":0.0,"answered":0,"correct":0,"sessions":0})
    with open(INPUT, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            w = r["week"] or "Unspecified"
            by_week[w]["planned"] += float(r["planned_hours"] or 0)
            by_week[w]["actual"] += float(r["actual_hours"] or 0)
            by_week[w]["answered"] += int(r["questions_answered"] or 0)
            by_week[w]["correct"] += int(r["questions_correct"] or 0)
            by_week[w]["sessions"] += 1

    lines = ["# Progress Weekly Summary", ""]
    for w in sorted(by_week.keys()):
        a = by_week[w]
        acc = a["correct"]/a["answered"]*100 if a["answered"] else 0
        eff = a["actual"]/a["planned"]*100 if a["planned"] else 0
        lines += [
            f"## {w}",
            f"- Sessions: **{a['sessions']}**",
            f"- Planned: **{a['planned']:.1f}h** / Actual: **{a['actual']:.1f}h** (達成率 {eff:.0f}%)",
            f"- Answered: **{a['answered']}** / Correct: **{a['correct']}** (正答率 {acc:.0f}%)",
            ""
        ]
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    main()
