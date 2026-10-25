/* UPPCS Polity Master Test — Single Page Application */
const STATE = {
  lang: "both",
  section: null,
  pool: [],
  index: 0,
  score: 0,
  answers: [],
  wrongSections: []
};

const shell = {};   // static elements present in index.html
const card = {};    // dynamic elements built by render()

function cacheShell() {
  const ids = [
    "sectionList","sectionTitle","qCounter","curQ","totQ","scoreDisplay",
    "progressFill","quizArea","overlay","sidebar","menuBtn","closeBtn","langToggle"
  ];
  ids.forEach(function(id){ shell[id] = document.getElementById(id); });
}

function esc(text){
  var d=document.createElement("div"); d.textContent=text; return d.innerHTML;
}

function buildSidebar(){
  var list = shell.sectionList;
  list.innerHTML = "";
  function add(name, count, isAll){
    var active = STATE.section === (isAll ? "__all__" : name) ? " active" : "";
    var li = document.createElement("li");
    li.innerHTML = '<button class="sec-btn'+active+'" data-section="'+esc(isAll?"__all__":name)+'">'
      + '<span>'+esc(name)+'</span>'
      + '<span class="count">'+count+'</span>'
      + '</button>';
    list.appendChild(li);
    return li.querySelector("button");
  }
  add("Full Test — All Sections", window.ALL_QUESTIONS.length, true);
  for (var i=0; i<window.SECTION_ORDER.length; i++){
    var sec = window.SECTION_ORDER[i];
    add(sec, window.SECTIONS[sec].length, false);
  }
  list.querySelectorAll("button[data-section]").forEach(function(btn){
    btn.addEventListener("click", function(){
      var name = btn.getAttribute("data-section");
      selectSection(name === "__all__" ? "__all__" : name);
      if (window.innerWidth < 768){
        shell.sidebar.classList.remove("open");
        shell.overlay.classList.remove("open");
      }
    });
  });
}

function selectSection(name){
  STATE.section = name;
  STATE.pool = name === "__all__"
    ? window.ALL_QUESTIONS.slice()
    : (window.SECTIONS[name] || []).slice();
  STATE.pool.sort(function(){ return Math.random() - 0.5; });
  STATE.pool = STATE.pool.slice(0, Math.min(10, STATE.pool.length));
  STATE.index = 0; STATE.score = 0; STATE.answers = []; STATE.wrongSections = [];
  document.getElementById("sectionTitle").textContent = name === "__all__" ? "Full Test — All Sections" : name;
  render();
}

function applyLang(){
  var showEn = STATE.lang === "both" || STATE.lang === "en";
  var showHi = STATE.lang === "both" || STATE.lang === "hi";
  document.querySelectorAll(".opt-text-en").forEach(function(o){ o.style.display = showEn ? "inline" : "none"; });
  document.querySelectorAll(".opt-text-hi").forEach(function(o){ o.style.display = showHi ? "inline" : "none"; });
  if(card.qEn) card.qEn.style.display = showEn ? "block" : "none";
  if(card.qHi) card.qHi.style.display = showHi ? "block" : "none";
  document.querySelectorAll(".lang-btn").forEach(function(b){
    b.classList.toggle("active", b.dataset.lang === STATE.lang);
  });
}

function render(){
  buildSidebar();
  applyLang();
  var q = STATE.pool[STATE.index];
  if(!q){ showResult(); return; }

  shell.qCounter.textContent = "Question " + (STATE.index + 1) + " of " + STATE.pool.length;
  shell.curQ.textContent = STATE.index + 1;
  shell.totQ.textContent = STATE.pool.length;
  shell.scoreDisplay.textContent = "Score: " + STATE.score;
  shell.progressFill.style.width = ((STATE.index) / STATE.pool.length * 100) + "%";

  // Build the question-card DOM (these elements don't exist in static HTML)
  shell.quizArea.innerHTML = ''
    + '<div class="question-card">'
    + '  <div class="q-section" id="qSection"></div>'
    + '  <div class="q-number" id="qNumber"></div>'
    + '  <div class="q-en" id="qEn"></div>'
    + '  <div class="q-hi" id="qHi"></div>'
    + '  <div class="options" id="optionsArea"></div>'
    + '  <div class="feedback" id="feedback">'
    + '    <h4 id="fbTitle"></h4>'
    + '    <div class="tag" id="fbTag"></div>'
    + '    <p id="fbEn"></p>'
    + '    <p id="fbHi"></p>'
    + '    <div class="ref" id="fbRef"></div>'
    + '  </div>'
    + '  <button class="btn-next" id="btnNext" disabled>Next Question</button>'
    + '</div>';

  // Re-query the dynamically-built card elements
  card.qSection = document.getElementById('qSection');
  card.qNumber = document.getElementById('qNumber');
  card.qEn = document.getElementById('qEn');
  card.qHi = document.getElementById('qHi');
  card.optionsArea = document.getElementById('optionsArea');
  card.feedback = document.getElementById('feedback');
  card.fbTitle = document.getElementById('fbTitle');
  card.fbTag = document.getElementById('fbTag');
  card.fbEn = document.getElementById('fbEn');
  card.fbHi = document.getElementById('fbHi');
  card.fbRef = document.getElementById('fbRef');
  card.btnNext = document.getElementById('btnNext');

  // Populate card
  card.qSection.textContent = q.section + (q.sub ? " > " + q.sub : "");
  card.qEn.textContent = q.qEn;
  card.qHi.textContent = q.qHi;

  card.optionsArea.innerHTML = "";
  q.opts.forEach(function(opt, i){
    var lab = document.createElement("label");
    lab.className = "option";
    lab.innerHTML = '<input type="radio" name="opt" value="'+i+'">'
      + '<span class="opt-letter">'+String.fromCharCode(65+i)+'.</span>'
      + '<span class="opt-text-en">'+esc(opt.en)+'</span>'
      + '<span class="opt-text-hi">'+esc(opt.hi)+'</span>';
    lab.querySelector("input").addEventListener("click", function(){ handleSelect(i); });
    card.optionsArea.appendChild(lab);
  });

  applyLang();  // now hide/show en/hi for the created option elements

  card.feedback.style.display = "none";
  card.feedback.className = "feedback";
  card.fbTitle.textContent = ""; card.fbTag.textContent = "";
  card.fbEn.textContent = ""; card.fbHi.textContent = ""; card.fbRef.textContent = "";
  card.btnNext.disabled = true;

  card.btnNext.onclick = function(){
    STATE.index++;
    if(STATE.index >= STATE.pool.length){ showResult(); return; }
    render();
  };
}

function handleSelect(i){
  var q = STATE.pool[STATE.index];
  var isCorrect = i === q.correct;
  if(isCorrect){ STATE.score++; } else { STATE.wrongSections.push(q.section); }
  STATE.answers.push({ id:q.id, chosen:i, correct:q.correct, isCorrect:isCorrect, section:q.section });

  var labs = card.optionsArea.querySelectorAll("label.option");
  labs.forEach(function(lab, j){
    var inp = lab.querySelector("input");
    inp.disabled = true;
    lab.classList.remove("selected","correct","wrong");
    if(j === q.correct) lab.classList.add("correct");
    if(j === i && !isCorrect) lab.classList.add("wrong");
    if(j === i && isCorrect) lab.classList.add("correct");
  });

  card.feedback.style.display = "block";
  if(isCorrect){
    card.feedback.className = "feedback correct";
    card.fbTitle.textContent = "Correct Answer";
    card.fbTag.textContent = "Explanation";
    card.fbEn.textContent = q.eEn;
    card.fbHi.textContent = q.eHi;
  } else {
    card.feedback.className = "feedback wrong";
    card.fbTitle.textContent = "Incorrect Answer";
    card.fbTag.textContent = "Correct Answer & Explanation";
    card.fbEn.textContent = "Correct: " + q.cEn + ". " + q.eEn;
    card.fbHi.textContent = "सही: " + q.cHi + ". " + q.eHi;
  }
  card.fbRef.textContent = q.ref;
  shell.scoreDisplay.textContent = "Score: " + STATE.score;
  card.btnNext.disabled = false;
}

function showResult(){
  shell.quizArea.innerHTML = "";
  var pct = STATE.score / STATE.pool.length * 100;
  var msg = pct >= 80 ? "Excellent! Strong grasp of Polity."
    : pct >= 60 ? "Good! Revise the weak topics below."
    : "Needs improvement. Focus on the revision list.";
  var uniqueWrong = [];
  STATE.wrongSections.forEach(function(ch){ if(uniqueWrong.indexOf(ch)===-1) uniqueWrong.push(ch); });
  var weakHtml = "";
  if(uniqueWrong.length){
    weakHtml = uniqueWrong.map(function(ch){ return "<li>"+esc(ch)+"</li>"; }).join("");
  } else {
    weakHtml = "<li style='color:#15803d'>No weak topics! Great job.</li>";
  }
  var html = ''
    + '<div class="result-card">'
    + '<div class="score-big">'+STATE.score+' / '+STATE.pool.length+'</div>'
    + '<div class="result-msg">'+esc(msg)+'</div>'
    + '<div class="weak-list">'
    + '<h4>Weak Topics &amp; Revision</h4>'
    + '<ul>'+weakHtml+'</ul>'
    + '</div>'
    + '<div class="result-actions">'
    + '<button class="btn-outline" onclick="location.reload()">Choose Another Section</button>'
    + '<button class="btn-primary" onclick="selectSection(\''+esc(STATE.section)+'\')">Retry This Section</button>'
    + '</div>'
    + '</div>';
  shell.quizArea.innerHTML = html;
  shell.progressFill.style.width = "100%";
  shell.qCounter.textContent = "Completed";
  shell.curQ.textContent = STATE.pool.length;
  shell.totQ.textContent = STATE.pool.length;
}

window.restartSection = function(){ selectSection(STATE.section); };

function init(){
  cacheShell();
  buildSidebar();
  shell.menuBtn.addEventListener("click", function(){
    shell.sidebar.classList.add("open");
    shell.overlay.classList.add("open");
  });
  shell.closeBtn.addEventListener("click", function(){
    shell.sidebar.classList.remove("open");
    shell.overlay.classList.remove("open");
  });
  shell.overlay.addEventListener("click", function(){
    shell.sidebar.classList.remove("open");
    shell.overlay.classList.remove("open");
  });
  shell.langToggle.addEventListener("click", function(e){
    var btn = e.target.closest(".lang-btn");
    if(!btn) return;
    STATE.lang = btn.dataset.lang;
    applyLang();
  });
  if(window.SECTION_ORDER && window.SECTION_ORDER.length){
    selectSection(window.SECTION_ORDER[0]);
  }
}
document.addEventListener("DOMContentLoaded", init);
