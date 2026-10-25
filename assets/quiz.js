/* Question bank (const Q) is defined per-section in each HTML page. */

/* ============ STATE ============ *//* ============ STATE ============ *//* ============ STATE ============ */
let STATE = {
  lang: "both",
  sectionFilter: "all",
  pool: [],
  index: 0,
  score: 0,
  total: 10,
  answers: [],
  wrongChapters: [],
  mastery: {}
};

// Per-question answering state, reset on every render()
let currentAnswered = false;
let currentSelection = null; // number | number[] | {col1Idx: col2Idx}

function letterOf(i) { return String.fromCharCode(65 + i); }

function getSections() {
  const seen = new Set(); const out = [];
  Q.forEach(q => { if (!seen.has(q.section)) { seen.add(q.section); out.push(q.section); } });
  return out;
}
function renderSectionButtons() {
  const container = document.getElementById("sectionButtons");
  if (!container) return;
  container.innerHTML = "";
  getSections().forEach(sec => {
    const b = document.createElement("button");
    b.className = "sec-btn" + (STATE.sectionFilter === sec ? " active" : "");
    b.textContent = sec;
    b.addEventListener("click", function() {
      STATE.sectionFilter = sec; STATE.index = 0; STATE.score = 0;
      document.querySelectorAll(".sec-btn").forEach(x => x.classList.remove("active"));
      b.classList.add("active");
      render();
    });
    container.appendChild(b);
  });
}
function buildPool() {
  if (STATE.sectionFilter === "all") STATE.pool = Q.slice();
  else STATE.pool = Q.filter(q => q.section === STATE.sectionFilter);
  STATE.pool.sort(() => Math.random() - 0.5);
  STATE.pool = STATE.pool.slice(0, Math.min(STATE.total, STATE.pool.length));
}

let els = {};
function cacheElements() {
  els = {
    qCounter: document.getElementById("qCounter"),
    curQ: document.getElementById("curQ"),
    totQ: document.getElementById("totQ"),
    scoreDisplay: document.getElementById("scoreDisplay"),
    progressFill: document.getElementById("progressFill"),
    qSection: document.getElementById("qSection"),
    qNumber: document.getElementById("qNumber"),
    qEn: document.getElementById("qEn"),
    qHi: document.getElementById("qHi"),
    optionsArea: document.getElementById("optionsArea"),
    feedback: document.getElementById("feedback"),
    fbTitle: document.getElementById("fbTitle"),
    fbTag: document.getElementById("fbTag"),
    fbEn: document.getElementById("fbEn"),
    fbHi: document.getElementById("fbHi"),
    fbRef: document.getElementById("fbRef"),
    btnNext: document.getElementById("btnNext"),
    quizArea: document.getElementById("quizArea"),
    resultArea: document.getElementById("resultArea"),
    finalScore: document.getElementById("finalScore"),
    finalMsg: document.getElementById("finalMsg"),
    weakList: document.getElementById("weakList")
  };
}

function applyLang() {
  const showEn = STATE.lang === "both" || STATE.lang === "en";
  const showHi = STATE.lang === "both" || STATE.lang === "hi";
  document.querySelectorAll(".opt-text-en").forEach(o => o.style.display = showEn ? "inline" : "none");
  document.querySelectorAll(".opt-text-hi").forEach(o => o.style.display = showHi ? "inline" : "none");
  if (els.qEn) els.qEn.style.display = showEn ? "block" : "none";
  if (els.qHi) els.qHi.style.display = showHi ? "block" : "none";
}

function computeCorrect(q, sel) {
  if (q.type === "mcq_multi") {
    var correctSet = new Set(q.correct);
    var selSet = new Set(sel);
    if (selSet.size !== correctSet.size) return false;
    for (var k = 0; k < correctSet.size; k++) { /* no-op, kept for clarity */ }
    var correctArr = Array.from(correctSet);
    for (var i = 0; i < correctArr.length; i++) if (!selSet.has(correctArr[i])) return false;
    return true;
  }
  if (q.type === "matching") {
    var mapping = q.correct;
    var keys = Object.keys(mapping);
    for (var i = 0; i < keys.length; i++) {
      var v = sel[keys[i]];
      if (v == null || v === "") return false;
      if (String(v) !== String(mapping[keys[i]])) return false;
    }
    return true;
  }
  return sel == q.correct;
}

function correctIndices(q) {
  if (q.type === "mcq_multi") return q.correct.slice();
  return [q.correct];
}

function correctAnswerText(q) {
  if (q.type === "mcq_single" || q.type === "assertion_reason") {
    return q.opts[q.correct].en;
  }
  if (q.type === "mcq_multi") {
    var out = [];
    for (var i = 0; i < q.correct.length; i++) out.push(q.opts[q.correct[i]].en);
    return out.join(", ");
  }
  return null;
}

function render() {
  buildPool();
  renderSectionButtons();
  const q = STATE.pool[STATE.index];
  if (!q) return;
  currentAnswered = false;
  currentSelection = (q.type === "matching") ? {} : null;

  els.qCounter.textContent = "Question " + (STATE.index + 1) + " of " + STATE.pool.length;
  els.curQ.textContent = STATE.index + 1;
  els.totQ.textContent = STATE.pool.length;
  els.scoreDisplay.textContent = "Score: " + STATE.score;
  els.progressFill.style.width = ((STATE.index) / STATE.pool.length * 100) + "%";
  els.qSection.textContent = q.section + (q.sub ? " > " + q.sub : "");

  var arHeader = document.getElementById("arHeader");
  if (q.type === "assertion_reason") {
    if (arHeader) {
      arHeader.classList.remove("hide");
      arHeader.innerHTML = '<div style="font-weight:700;color:#38bdf8;margin-bottom:4px;">Assertion:</div>'
        + '<div style="margin-bottom:4px;">' + q.assertionEn + '</div>'
        + '<div style="font-weight:700;color:#38bdf8;margin-bottom:4px;margin-top:8px;">Reason:</div>'
        + '<div style="margin-bottom:10px;">' + q.reasonEn + '</div>';
    }
    els.qEn.style.display = "none";
    els.qHi.style.display = "none";
  } else {
    if (arHeader) arHeader.classList.add("hide");
    if (STATE.lang === "both") { els.qEn.style.display = "block"; els.qHi.style.display = "block"; }
    else if (STATE.lang === "en") { els.qEn.style.display = "block"; els.qHi.style.display = "none"; }
    else { els.qEn.style.display = "none"; els.qHi.style.display = "block"; }
    els.qEn.textContent = q.qEn;
    els.qHi.textContent = q.qHi;
  }

  els.optionsArea.innerHTML = "";
  els.feedback.style.display = "none";
  els.feedback.className = "feedback";
  els.fbTitle.textContent = ""; els.fbTag.textContent = ""; els.fbEn.textContent = ""; els.fbHi.textContent = ""; els.fbRef.textContent = "";
  els.btnNext.disabled = true;
  els.btnNext.textContent = "Submit Answer";

  if (q.type === "matching") {
    q.col1.forEach(function(item, ci) {
      var row = document.createElement("div");
      row.className = "option match-row";
      row.style.cssText = "display:flex;align-items:center;gap:10px;padding:10px 14px;border:1px solid #334155;border-radius:8px;margin-bottom:8px;";
      var label = document.createElement("span");
      label.style.cssText = "flex:0 0 44%;font-weight:600;";
      label.textContent = letterOf(ci) + ". " + item.en;
      var sel = document.createElement("select");
      sel.className = "match-select";
      sel.style.cssText = "flex:1;padding:6px 10px;border-radius:6px;border:1px solid #334155;background:#0f172a;color:#e2e8f0;";
      var empty = document.createElement("option"); empty.value = ""; empty.textContent = "— select —"; sel.appendChild(empty);
      q.col2.forEach(function(opt, ti) {
        var o = document.createElement("option"); o.value = ti; o.textContent = opt.en; sel.appendChild(o);
      });
      sel.addEventListener("change", function() {
        currentSelection[ci] = sel.value;
        var allFilled = true;
        for (var k = 0; k < q.col1.length; k++) {
          var val = currentSelection[k];
          if (val == null || val === "") { allFilled = false; break; }
        }
        els.btnNext.disabled = !allFilled;
      });
      row.appendChild(label); row.appendChild(sel);
      els.optionsArea.appendChild(row);
    });
    applyLang();
    return;
  }

  // mcq_single, mcq_multi, assertion_reason
  var inputType = (q.type === "mcq_multi") ? "checkbox" : "radio";
  var inputName = (q.type === "mcq_multi") ? "opt[]" : "opt";
  q.opts.forEach(function(opt, i) {
    var lab = document.createElement("label");
    lab.className = "option";
    var inp = document.createElement("input");
    inp.type = inputType; inp.name = inputName; inp.value = i;
    lab.innerHTML = '<span class="opt-letter">' + letterOf(i) + ".</span>"
      + '<span class="opt-text-en">' + opt.en + '</span>'
      + '<span class="opt-text-hi">' + opt.hi + '</span>';
    lab.insertBefore(inp, lab.firstChild);
    inp.addEventListener("change", function() {
      if (q.type === "mcq_multi") {
        var checks = els.optionsArea.querySelectorAll('input[name="opt[]"]:checked');
        currentSelection = Array.from(checks).map(function(c) { return parseInt(c.value, 10); });
        els.btnNext.disabled = currentSelection.length === 0;
      } else {
        currentSelection = parseInt(inp.value, 10);
        submitAnswer();
      }
    });
    els.optionsArea.appendChild(lab);
  });
  applyLang();
}

function submitAnswer() {
  if (currentAnswered) return;
  var q = STATE.pool[STATE.index];
  var isCorrect = computeCorrect(q, currentSelection);
  var m = STATE.mastery[q.id] || { streak: 0, attempts: 0, correct: 0 };
  m.attempts++;
  if (isCorrect) { m.correct++; m.streak++; STATE.score++; } else { m.streak = 0; }
  STATE.mastery[q.id] = m;
  STATE.answers.push({ id: q.id, chosen: currentSelection, correct: q.correct, isCorrect: isCorrect, section: q.section, type: q.type });
  if (!isCorrect && STATE.wrongChapters.indexOf(q.section) === -1) STATE.wrongChapters.push(q.section);

  if (q.type === "matching") {
    for (var ci = 0; ci < q.col1.length; ci++) {
      var row = els.optionsArea.children[ci];
      var sel = row.querySelector("select");
      sel.disabled = true;
      row.classList.remove("correct", "wrong");
      if (String(sel.value) === String(q.correct[String(ci)])) {
        row.classList.add("correct");
      } else {
        row.classList.add("wrong");
      }
    }
  } else {
    var labs = els.optionsArea.querySelectorAll("label.option");
    var correctSet = new Set(correctIndices(q));
    var selArr = Array.isArray(currentSelection) ? currentSelection : [currentSelection];
    var selSet = new Set(selArr);
    labs.forEach(function(lab, j) {
      var inp = lab.querySelector("input");
      inp.disabled = true;
      lab.classList.remove("selected", "correct", "wrong");
      if (correctSet.has(j)) lab.classList.add("correct");
      if (selSet.has(j) && !correctSet.has(j)) lab.classList.add("wrong");
    });
  }

  currentAnswered = true;
  els.btnNext.textContent = "Next Question";
  els.btnNext.disabled = false;
  els.scoreDisplay.textContent = "Score: " + STATE.score;

  els.feedback.style.display = "block";
  if (isCorrect) {
    els.feedback.className = "feedback correct";
    els.fbTitle.textContent = "Correct Answer";
    els.fbTag.textContent = "Fact / Explanation";
    els.fbEn.textContent = q.eEn;
    els.fbHi.textContent = q.eHi;
  } else {
    els.feedback.className = "feedback wrong";
    els.fbTitle.textContent = "Incorrect Answer";
    els.fbTag.textContent = "Correct Answer & Explanation";
    var cat = correctAnswerText(q);
    els.fbEn.textContent = (cat ? "Correct: " + cat + ". " : "") + q.eEn;
    els.fbHi.textContent = (cat ? "सही उत्तर: " + cat + ". " : "") + q.eHi;
  }
  els.fbRef.textContent = q.ref;
}

function showResult() {
  els.quizArea.style.display = "none";
  els.resultArea.classList.remove("hide");
  els.finalScore.textContent = STATE.score + " / " + STATE.pool.length;
  var pct = STATE.score / STATE.pool.length * 100;
  els.finalMsg.textContent = pct >= 80 ? "Excellent! Strong grasp of Polity."
    : pct >= 60 ? "Good! Revise the weak topics below."
    : "Needs improvement. Focus on the revision list.";
  els.weakList.innerHTML = "";
  STATE.wrongChapters.forEach(function(ch) {
    var li = document.createElement("li"); li.textContent = ch; els.weakList.appendChild(li);
  });
  if (STATE.wrongChapters.length === 0) els.weakList.innerHTML = "<li style='color:#4ade80'>No weak topics! Great job.</li>";
  els.progressFill.style.width = "100%";
}

window.restartTest = function() {
  STATE.index = 0; STATE.score = 0; STATE.answers = []; STATE.wrongChapters = [];
  currentAnswered = false; currentSelection = null;
  els.resultArea.classList.add("hide");
  els.quizArea.style.display = "block";
  render();
};

document.getElementById("btnAll").addEventListener("click", function() {
  STATE.sectionFilter = "all"; STATE.index = 0; STATE.score = 0;
  document.querySelectorAll(".sec-btn").forEach(function(x) { x.classList.remove("active"); });
  document.getElementById("btnAll").classList.add("active");
  render();
});
document.getElementById("btnReset").addEventListener("click", function() {
  STATE.sectionFilter = "all"; STATE.mastery = {}; STATE.index = 0; STATE.score = 0; STATE.answers = []; STATE.wrongChapters = [];
  currentAnswered = false; currentSelection = null;
  document.querySelectorAll(".sec-btn").forEach(function(x) { x.classList.remove("active"); });
  document.getElementById("btnAll").classList.add("active");
  render();
});
document.getElementById("btnNext").addEventListener("click", function() {
  if (currentAnswered) {
    STATE.index++;
    if (STATE.index >= STATE.pool.length) { showResult(); return; }
    render();
  } else {
    submitAnswer();
  }
});
["langBoth","langEn","langHi"].forEach(function(id) {
  document.getElementById(id).addEventListener("click", function() {
    STATE.lang = (id === "langBoth") ? "both" : (id === "langEn") ? "en" : "hi";
    ["langBoth","langEn","langHi"].forEach(function(x) { document.getElementById(x).classList.remove("active"); });
    document.getElementById(id).classList.add("active");
    applyLang();
  });
});

cacheElements();
render();