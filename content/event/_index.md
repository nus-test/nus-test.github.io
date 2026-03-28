---
title: Recent & Upcoming Events

# View.
#   1 = List
#   2 = Compact
#   3 = Card
view: 1

# Optional header image (relative to `static/media/` folder).
header:
  caption: ""
  image: ""
---

`If you want to give a talk or attend the seminar, please reach out to` [Yibo](mailto:dongyibo@u.nus.edu?subject=NUS%20TEST%20Seminar).



Timetable for upcoming events in AY25/26 (subject to changes):

| Date   | Title                                                        | Host      | Invitee    |
| ------ | ------------------------------------------------------------ | --------- | ---------- |
| May 6 | <font color=brown>Group Discussion</font> | --- | ---|
| April 29 |  | --- | ---|
| April 22 | <font color=blue>Once-for-All: Skeleton-Guided SMT Solver Fuzzing with LLM-Synthesized Generators</font> | Suyang | Maolin Sun |
| April 15 | <font color=blue>Argus: Automated Discovery of Test Oracles for Database Management Systems Using LLMs</font> | Test Lab | Qiuyang|
| April 8 | <font color=brown>Beyond Correctness: Exposing LLM-generated Logical Flaws in Reasoning via Multi-step Automated Theorem Proving</font> | Ningke | Ningke |
| April 1 | <font color=blue>VDBFuzz: Understanding and Detecting Crash Bugs in Vector Database Management Systems</font> | Ningke | Shenao Wang |
| March 25 |  | <font color=brown>Group Discussion</font> | ---| ---|
| March 24 | <font color=green>Reading Group</font> | Yuancheng | ---|
| March 18 | <font color=blue>Comparables XAI: Faithful Example-based AI Explanations with Counterfactual Trace Adjustments</font> | Yibo | Yifan Zhang|
| March 11 | <font color=brown>How Should Applications Choose Optimal Isolation Levels</font> | Qiyu | Qiyu|
| March 10 | <font color=green>Reading Group</font> | Yibo | ---|
| March 4 | <font color=blue>Software-Style Hardware Testing: Information-Flow Tracking, Fuzzing, and What ML Might Add.</font> | TEST-lab | Flavien Solt|
| Feb 25 | <font color=gray>Recess Week</font> | --- | ---|
| Feb 18 | <font color=gray>Skip: Chinese New Year</font> | --- | ---|
| Feb 11 | <font color=blue>From Empirical Study to Runtime Mitigation: Addressing Integration Failures in LLM-Enabled Software</font> | Yibo Dong | Yuchen Shao |
| Feb 10 | <font color=green>Reading Group</font> | Junwen | ---|
| Feb 4 | <font color=brown>Suyang Dry Run</font> | --- | ---|
| Jan 28 | <font color=gray>Skip</font> | --- | ---|
| Jan 27 | <font color=green>Reading Group</font> | Ningke | ---|
| Jan 21 | <font color=brown>Group Discussion</font> | --- | ---|
| --- |  Winter Break   |  ---  |  ---  |
| Dec 2 | <font color=brown>Group Discussion</font> |           |            |
| Nov 25 | Canceled for Final Exams |           |            |
| Nov 18 | <font color=brown>Zhaokun Presentation</font> | Zhaokun | \ |
| Nov 11 | <font color=brown>FYP Presentation Dry Run</font>  |   |   |
| Nov 4 | <font color=brown>Group Discussion: Insight behind current/previous research </font> |           |            |
| Oct 28  | <font color=blue>Finding Bugs in MLIR Compiler Infrastructure via Lowering Space Exploration </font> | Yibo Dong | Jingjing Liang |
| Oct 21  | <font color=gray>PUBLIC HOLIDAY </font> | \ | \ |
| Oct 14  | <font color=gray>OOPSLA Week </font> | \ | \ |
| Oct 10  | <font color=blue>Linalg is All Your Need</font>  |  TEST Lab | Ivan Ho | 
| Oct 7  |  <font color=brown>OOPSLA SRC Dry Run</font>   |           |            |
| Sep 30  | <font color=blue>"My productivity is boosted, but ..." Demystifying Users' Perception on Al Coding Assistants </font> | Junwen An | Yunbo Lyu  |
| Sep 23 | <font color=gray>Recess Week</font> |  |  |
| Sep 16 | <font color=brown>Group Discussion: Self Introduction</font> |   |            |
| Sep 9  | Canceled | \ | \  |
| Sep 2  | <font color=blue>Static bug detection in the era of LLMs</font> | Yibo Dong | Yiling Lou |
| Aug 26 | <font color=blue>Why the Proof Fails in Different Versions of Theorem Provers: An Empirical Study of Compatibility Issues in Isabelle </font> | Ningke Li | Xiaokun Luan |
| Aug 19 | <font color=blue>AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents</font> | Ningke Li | Haoyu Wang |


Details of upcoming and past talks below.

<style>
.past-events-toggle {
  margin: 0.8rem 0;
  padding: 0.4rem 1rem;
  font-size: 0.9rem;
  cursor: pointer;
  background: transparent;
  border: 1px solid #1565c0;
  color: #1565c0;
  border-radius: 4px;
  transition: background 0.2s, color 0.2s;
}
.past-events-toggle:hover {
  background: #1565c0;
  color: #fff;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var MONTHS = {
    'jan': 0, 'feb': 1, 'mar': 2, 'apr': 3,
    'may': 4, 'jun': 5, 'jul': 6, 'aug': 7,
    'sep': 8, 'oct': 9, 'nov': 10, 'dec': 11
  };

  var table = document.querySelector('.article-style table');
  if (!table) return;

  var rows = table.querySelectorAll('tbody tr');
  if (!rows.length) return;

  var today = new Date();
  today.setHours(0, 0, 0, 0);

  // Infer year for each row: the table is reverse-chronological.
  // When month jumps upward (e.g. Jan → Dec going down), we crossed into the previous calendar year.
  var year = today.getFullYear();
  var prevMonth = null;
  var rowData = [];

  for (var i = 0; i < rows.length; i++) {
    var cells = rows[i].querySelectorAll('td');
    if (!cells.length) continue;

    var dateText = cells[0].textContent.trim();
    var match = dateText.match(/^(\w+)\s+(\d+)/);

    if (match) {
      var monthNum = MONTHS[match[1].toLowerCase().substring(0, 3)];
      var day = parseInt(match[2]);

      if (monthNum !== undefined) {
        if (prevMonth !== null && monthNum > prevMonth) year--;
        prevMonth = monthNum;
        rowData.push({ row: rows[i], date: new Date(year, monthNum, day) });
        continue;
      }
    }
    rowData.push({ row: rows[i], date: null });
  }

  // Find the first row whose date is strictly before today
  var splitIndex = -1;
  for (var i = 0; i < rowData.length; i++) {
    if (rowData[i].date && rowData[i].date < today) {
      splitIndex = i;
      break;
    }
  }

  if (splitIndex <= 0) return;

  var pastCount = rowData.length - splitIndex;
  for (var i = splitIndex; i < rowData.length; i++) {
    rowData[i].row.classList.add('past-event');
    rowData[i].row.style.display = 'none';
  }

  var btn = document.createElement('button');
  btn.textContent = '\u25B6 Show Past Events (' + pastCount + ')';
  btn.className = 'past-events-toggle';
  btn.addEventListener('click', function() {
    var pastRows = table.querySelectorAll('.past-event');
    var isHidden = pastRows[0] && pastRows[0].style.display === 'none';
    for (var j = 0; j < pastRows.length; j++) {
      pastRows[j].style.display = isHidden ? '' : 'none';
    }
    btn.textContent = isHidden
      ? '\u25B2 Hide Past Events'
      : '\u25B6 Show Past Events (' + pastRows.length + ')';
  });

  table.parentNode.insertBefore(btn, table.nextSibling);
});
</script>
