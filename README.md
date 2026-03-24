import { useState, useCallback, useEffect } from "react";

const FONTS = `@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');`;

const CSS = `
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #080b14; color: #e2e8f0; font-family: 'Outfit', sans-serif; }

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #1e2a45; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #2a3a5c; }

@keyframes fadeUp { from { opacity:0; transform:translateY(16px); } to { opacity:1; transform:translateY(0); } }
@keyframes shimmer { 0%,100% { opacity:.4; } 50% { opacity:1; } }
@keyframes pulse-ring { 0% { box-shadow: 0 0 0 0 rgba(99,102,241,.4); } 70% { box-shadow: 0 0 0 8px rgba(99,102,241,0); } 100% { box-shadow: 0 0 0 0 rgba(99,102,241,0); } }
@keyframes slide-in { from { opacity:0; transform:translateX(-12px); } to { opacity:1; transform:translateX(0); } }
@keyframes glow-pulse { 0%,100% { text-shadow: 0 0 10px #6366f180; } 50% { text-shadow: 0 0 24px #6366f1cc, 0 0 48px #6366f140; } }

.app-shell {
  display: flex; height: 100vh; overflow: hidden;
  background: #080b14;
}

/* SIDEBAR */
.sidebar {
  width: 260px; flex-shrink: 0;
  background: linear-gradient(180deg, #0d1120 0%, #090d1a 100%);
  border-right: 1px solid rgba(99,102,241,.15);
  display: flex; flex-direction: column;
  position: relative; overflow: hidden;
}
.sidebar::before {
  content:''; position:absolute; top:-80px; left:-80px;
  width:240px; height:240px; border-radius:50%;
  background: radial-gradient(circle, rgba(99,102,241,.12) 0%, transparent 70%);
  pointer-events:none;
}
.brand {
  padding: 20px 20px 16px;
  border-bottom: 1px solid rgba(99,102,241,.1);
}
.brand-name {
  font-size: 15px; font-weight: 800; letter-spacing: -.01em;
  background: linear-gradient(135deg, #a78bfa, #6366f1);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  animation: glow-pulse 3s ease-in-out infinite;
}
.brand-sub { font-size: 10px; color: #3d4f70; letter-spacing: .12em; text-transform: uppercase; margin-top: 2px; }

.nav-section-label {
  font-size: 9px; color: #2a3a5c; letter-spacing: .16em;
  text-transform: uppercase; padding: 14px 20px 6px; font-weight: 600;
}
.nav-item {
  display: flex; align-items: center; gap: 10px;
  padding: 9px 20px; cursor: pointer;
  border-left: 2px solid transparent;
  transition: all .2s ease; position: relative; overflow: hidden;
  font-size: 13px; font-weight: 500; color: #3d4f70;
}
.nav-item::after {
  content:''; position:absolute; inset:0;
  background: linear-gradient(90deg, rgba(99,102,241,.08), transparent);
  opacity:0; transition: opacity .2s;
}
.nav-item:hover { color: #94a3b8; }
.nav-item:hover::after { opacity: 1; }
.nav-item.active {
  border-left-color: #6366f1; color: #a78bfa;
  background: rgba(99,102,241,.08);
}
.nav-item.active::after { opacity: 1; }
.nav-icon {
  width: 28px; height: 28px; border-radius: 7px;
  display: flex; align-items: center; justify-content: center;
  font-size: 14px; flex-shrink: 0;
  background: rgba(99,102,241,.06);
  border: 1px solid rgba(99,102,241,.1);
}
.nav-item.active .nav-icon {
  background: rgba(99,102,241,.18);
  border-color: rgba(99,102,241,.3);
}
.nav-badge {
  margin-left: auto; font-size: 9px; font-weight: 700;
  background: rgba(99,102,241,.2); color: #6366f1;
  border-radius: 20px; padding: 1px 7px; border: 1px solid rgba(99,102,241,.2);
}

.sidebar-footer {
  margin-top: auto; padding: 14px 20px;
  border-top: 1px solid rgba(99,102,241,.08);
}
.preview-toggle {
  display: flex; gap: 4px;
  background: #0d1120; border-radius: 8px; padding: 3px;
  border: 1px solid rgba(99,102,241,.12);
}
.pt-btn {
  flex: 1; padding: 6px; border-radius: 6px; font-size: 11px;
  font-weight: 600; font-family: 'Outfit', sans-serif;
  border: none; cursor: pointer; transition: all .2s; letter-spacing: .03em;
  background: transparent; color: #3d4f70;
}
.pt-btn.active { background: rgba(99,102,241,.25); color: #a78bfa; }

/* MAIN */
.main {
  flex: 1; display: flex; flex-direction: column; overflow: hidden;
}

.topbar {
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 24px; flex-shrink: 0;
  background: rgba(13,17,32,.8);
  border-bottom: 1px solid rgba(99,102,241,.1);
  backdrop-filter: blur(12px);
}
.topbar-left { display: flex; align-items: center; gap: 12px; }
.section-title { font-size: 16px; font-weight: 700; color: #e2e8f0; }
.section-sub { font-size: 11px; color: #2a3a5c; margin-top: 1px; }
.topbar-actions { display: flex; gap: 8px; align-items: center; }

.btn {
  display: flex; align-items: center; gap: 6px;
  padding: 8px 16px; border-radius: 9px; cursor: pointer;
  font-family: 'Outfit', sans-serif; font-size: 12px; font-weight: 600;
  border: none; transition: all .2s; letter-spacing: .02em;
}
.btn-ghost {
  background: rgba(99,102,241,.06); color: #4a5a7a;
  border: 1px solid rgba(99,102,241,.12);
}
.btn-ghost:hover { background: rgba(99,102,241,.12); color: #a78bfa; border-color: rgba(99,102,241,.25); }
.btn-primary {
  background: linear-gradient(135deg, #6366f1, #4f46e5);
  color: #fff;
  box-shadow: 0 0 16px rgba(99,102,241,.3);
}
.btn-primary:hover { box-shadow: 0 0 24px rgba(99,102,241,.5); transform: translateY(-1px); }
.btn-success {
  background: linear-gradient(135deg, #059669, #047857);
  color: #fff; box-shadow: 0 0 12px rgba(5,150,105,.25);
}
.btn-success:hover { box-shadow: 0 0 20px rgba(5,150,105,.4); transform: translateY(-1px); }

.toast-badge {
  font-size: 11px; font-weight: 700; padding: 6px 14px;
  background: rgba(5,150,105,.2); color: #34d399;
  border-radius: 20px; border: 1px solid rgba(52,211,153,.2);
  animation: pulse-ring .6s ease;
}

/* CONTENT AREA */
.content-area {
  flex: 1; display: flex; overflow: hidden;
}
.edit-panel {
  flex: 1; overflow-y: auto; padding: 24px;
  animation: fadeUp .3s ease;
}
.preview-panel {
  flex: 1; overflow: hidden; display: flex; flex-direction: column;
  border-left: 1px solid rgba(99,102,241,.1);
}
.preview-header {
  padding: 10px 16px; font-size: 10px; font-weight: 700;
  color: #2a3a5c; letter-spacing: .14em; text-transform: uppercase;
  border-bottom: 1px solid rgba(99,102,241,.08);
  background: rgba(13,17,32,.6); display: flex; align-items: center; gap: 8px;
}
.preview-dot { width: 6px; height: 6px; border-radius: 50%; background: #6366f1; animation: shimmer 2s ease-in-out infinite; }
.preview-body {
  flex: 1; overflow-y: auto; padding: 16px;
  font-family: 'JetBrains Mono', monospace; font-size: 11px; line-height: 1.9;
  color: #3d4f70; background: #080b14;
  white-space: pre-wrap; word-break: break-word;
}

/* FORM ELEMENTS */
.form-section {
  background: rgba(13,17,32,.8); border: 1px solid rgba(99,102,241,.1);
  border-radius: 14px; padding: 20px; margin-bottom: 16px;
  animation: slide-in .25s ease both;
  backdrop-filter: blur(8px);
}
.form-section:hover { border-color: rgba(99,102,241,.2); }
.form-section-header {
  display: flex; align-items: center; gap: 8px; margin-bottom: 16px;
}
.form-section-icon {
  width: 32px; height: 32px; border-radius: 9px; display: flex;
  align-items: center; justify-content: center; font-size: 15px;
  background: rgba(99,102,241,.12); border: 1px solid rgba(99,102,241,.18);
}
.form-section-title { font-size: 13px; font-weight: 700; color: #a78bfa; letter-spacing: .03em; }
.form-section-sub { font-size: 10px; color: #2a3a5c; margin-top: 1px; }

.field { margin-bottom: 14px; }
.field-label {
  display: block; font-size: 10px; font-weight: 600;
  color: #3d4f70; letter-spacing: .1em; text-transform: uppercase; margin-bottom: 6px;
}
.field-input {
  width: 100%; background: rgba(8,11,20,.8);
  border: 1px solid rgba(99,102,241,.15); border-radius: 9px;
  color: #e2e8f0; padding: 9px 13px;
  font-size: 13px; font-family: 'Outfit', sans-serif;
  transition: border .2s, box-shadow .2s; outline: none;
}
.field-input:focus {
  border-color: rgba(99,102,241,.45);
  box-shadow: 0 0 0 3px rgba(99,102,241,.08);
}
.field-input::placeholder { color: #1e2a45; }
textarea.field-input { resize: vertical; min-height: 72px; line-height: 1.6; }

.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; }

/* PROGRESS ROWS */
.prog-row {
  display: flex; align-items: center; gap: 10px; padding: 8px 10px;
  border-radius: 9px; margin-bottom: 4px;
  background: rgba(8,11,20,.6); border: 1px solid rgba(99,102,241,.07);
  transition: border .2s;
}
.prog-row:hover { border-color: rgba(99,102,241,.18); }
.prog-label { font-size: 12px; font-weight: 500; color: #94a3b8; min-width: 130px; }
.prog-track { flex: 1; height: 5px; background: #0d1120; border-radius: 3px; overflow: hidden; cursor: pointer; position: relative; }
.prog-fill { height: 100%; border-radius: 3px; transition: width .4s cubic-bezier(.34,1.56,.64,1); }
.prog-num {
  width: 44px; background: rgba(8,11,20,.8);
  border: 1px solid rgba(99,102,241,.15); border-radius: 6px;
  color: #e2e8f0; padding: 3px 6px; font-size: 11px;
  font-family: 'JetBrains Mono', monospace; text-align: center; outline: none;
}
.status-pill {
  font-size: 9px; font-weight: 700; border-radius: 20px; padding: 2px 8px;
  border: 1px solid; white-space: nowrap; letter-spacing: .04em;
}

/* ROADMAP */
.rm-domain {
  background: rgba(8,11,20,.6); border: 1px solid rgba(99,102,241,.1);
  border-radius: 11px; padding: 12px; margin-bottom: 10px;
  transition: border .2s;
}
.rm-domain:hover { border-color: rgba(99,102,241,.2); }
.rm-domain-title { font-size: 12px; font-weight: 700; color: #a78bfa; margin-bottom: 8px; }
.rm-item { display: flex; align-items: center; gap: 8px; margin-bottom: 5px; }
.rm-check { accent-color: #6366f1; cursor: pointer; width: 13px; height: 13px; }
.rm-input {
  flex: 1; background: rgba(13,17,32,.8); border: 1px solid rgba(99,102,241,.1);
  border-radius: 6px; color: #94a3b8; padding: 3px 9px;
  font-size: 11px; font-family: 'Outfit', sans-serif; outline: none;
  transition: border .15s;
}
.rm-input:focus { border-color: rgba(99,102,241,.35); color: #e2e8f0; }

/* PROJECTS */
.proj-card {
  background: rgba(8,11,20,.7); border: 1px solid rgba(99,102,241,.1);
  border-radius: 12px; overflow: hidden; margin-bottom: 12px;
  transition: border .2s;
}
.proj-card:hover { border-color: rgba(99,102,241,.25); }
.proj-header { padding: 12px 14px; border-bottom: 1px solid rgba(99,102,241,.08); display: flex; align-items: center; gap: 8px; }
.proj-name { font-size: 13px; font-weight: 700; color: #e2e8f0; flex: 1; }
.proj-body { padding: 10px 14px; }
.proj-stack { font-size: 10px; color: #2a3a5c; font-family: 'JetBrains Mono', monospace; margin-bottom: 10px; }
.phase-row { display: flex; align-items: center; gap: 8px; padding: 4px 0; }
.phase-label { font-size: 11px; color: #4a5a7a; flex: 1; }
.phase-status { font-size: 9px; font-weight: 700; }

/* STACK */
.stack-grid { display: flex; flex-wrap: wrap; gap: 6px; }
.stack-chip {
  display: flex; align-items: center; gap: 5px; padding: 5px 11px;
  border-radius: 8px; font-size: 11px; font-weight: 600; cursor: pointer;
  border: 1px solid rgba(99,102,241,.15); background: rgba(13,17,32,.8);
  color: #3d4f70; transition: all .2s; user-select: none;
}
.stack-chip:hover { border-color: rgba(99,102,241,.35); color: #94a3b8; }
.stack-chip.on { background: rgba(99,102,241,.15); border-color: rgba(99,102,241,.4); color: #a78bfa; }
.stack-chip-dot { width: 6px; height: 6px; border-radius: 50%; background: #6366f1; }

/* SYNTAX HIGHLIGHT in preview */
.md-heading { color: #a78bfa; font-weight: 700; }
.md-keyword { color: #5DCAA5; }
.md-badge { color: #f59e0b; }
.md-link { color: #85B7EB; }
.md-code { color: #f0997b; }
.md-check { color: #4ade80; }
.md-empty { color: #2a3a5c; }
`;

// ── DATA ────────────────────────────────────────────────────
const DOMAINS = [
  { key:"python",  label:"🐍 Python",          pct:60,  status:"ongoing"     },
  { key:"pandas",  label:"🐼 Pandas / EDA",    pct:30,  status:"learning"    },
  { key:"sql",     label:"🗄️ SQL",             pct:20,  status:"learning"    },
  { key:"stats",   label:"📐 Statistics",      pct:0,   status:"not-started" },
  { key:"ml",      label:"🤖 Machine Learning", pct:0,  status:"not-started" },
  { key:"dl",      label:"🧠 Deep Learning",   pct:0,   status:"not-started" },
  { key:"mlops",   label:"⚙️ MLOps",           pct:0,   status:"not-started" },
  { key:"genai",   label:"✨ Generative AI",   pct:20,  status:"learning"    },
  { key:"agentic", label:"🤖 Agentic AI",      pct:0,   status:"not-started" },
  { key:"projects",label:"🚀 Projects",        pct:25,  status:"ongoing"     },
];

const ROADMAP_DATA = [
  { key:"python",  title:"Python",         emoji:"🐍", items:["Loops, Functions","Lists, Dictionary","Advanced Python","File Handling"],           done:[true,true,false,false] },
  { key:"pandas",  title:"Pandas / EDA",   emoji:"📊", items:["Data Loading","Data Cleaning","Missing Values","GroupBy","Visualization"],          done:[true,false,false,false,false] },
  { key:"sql",     title:"SQL",            emoji:"🗄️", items:["SELECT, WHERE","GROUP BY","JOIN","Subqueries"],                                      done:[true,false,false,false] },
  { key:"stats",   title:"Statistics",     emoji:"📐", items:["Mean, Median, Mode","Probability","Distributions","Hypothesis Testing"],             done:[false,false,false,false] },
  { key:"ml",      title:"Machine Learning",emoji:"🤖",items:["Regression","Classification","Trees & Ensemble","Model Evaluation"],                done:[false,false,false,false] },
  { key:"genai",   title:"Generative AI",  emoji:"✨", items:["LLM Basics","Prompt Engineering","RAG","LangChain"],                                done:[true,false,false,false] },
  { key:"mlops",   title:"MLOps",          emoji:"⚙️", items:["Deployment","Docker","CI/CD"],                                                      done:[false,false,false] },
];

const PROJECTS_DATA = [
  { key:"fake",  title:"Fake News Detection",  emoji:"🧠", stack:"Python · NLP · Scikit-learn · Streamlit",    phases:["Idea & Scope","Dataset Collection","Data Cleaning","Model Building","Deployment"],  done:[true,false,false,false,false] },
  { key:"airbnb",title:"Airbnb EDA Analysis",  emoji:"📊", stack:"Python · Pandas · Seaborn · Matplotlib",     phases:["Dataset","Data Cleaning","EDA","Visualization","Insights"],                        done:[true,false,false,false,false] },
  { key:"rag",   title:"Gen AI — RAG Project", emoji:"🤖", stack:"LangChain · OpenAI · ChromaDB · FastAPI",    phases:["RAG Architecture","Vector DB Setup","LLM Integration","Deployment"],               done:[false,false,false,false] },
];

const ALL_STACK = ["Python","Pandas","NumPy","SQL","Scikit-learn","LangChain","OpenAI","Git","VS Code","Jupyter","Docker","FastAPI","Streamlit","TensorFlow","PyTorch","HuggingFace","Matplotlib","Seaborn"];
const BADGE_COLORS = { Python:"3776AB",Pandas:"150458",NumPy:"013243",SQL:"4479A1","Scikit-learn":"F7931E",LangChain:"1C3C3C",OpenAI:"412991",Git:"F05032","VS Code":"007ACC",Jupyter:"F37626",Docker:"2496ED",FastAPI:"009688",Streamlit:"FF4B4B",TensorFlow:"FF6F00",PyTorch:"EE4C2C",HuggingFace:"FFD21E",Matplotlib:"11557C",Seaborn:"4C72B0" };

const NAV = [
  { id:"profile",  label:"Profile",     icon:"👤", sub:"Name, goal, bio" },
  { id:"progress", label:"Progress",    icon:"📊", sub:"% per domain" },
  { id:"roadmap",  label:"Roadmap",     icon:"🗺️", sub:"Topics + checkboxes" },
  { id:"projects", label:"Projects",    icon:"🚀", sub:"Phases + status" },
  { id:"stack",    label:"Tech Stack",  icon:"🛠️", sub:"Badge picker" },
  { id:"social",   label:"Social",      icon:"🔗", sub:"Links + username" },
];

const statusMeta = {
  "ongoing":     { color:"#4ade80", bg:"rgba(74,222,128,.12)", border:"rgba(74,222,128,.25)", emoji:"🟢", label:"Ongoing" },
  "learning":    { color:"#f59e0b", bg:"rgba(245,158,11,.12)", border:"rgba(245,158,11,.25)", emoji:"🟡", label:"Learning" },
  "not-started": { color:"#3d4f70", bg:"rgba(61,79,112,.12)",  border:"rgba(61,79,112,.25)",  emoji:"🔴", label:"Not Started" },
};

function barColor(pct) {
  if (pct === 0) return "#1e2a45";
  if (pct < 30)  return "#f87171";
  if (pct < 60)  return "#f59e0b";
  if (pct < 90)  return "#34d399";
  return "#6366f1";
}

// ── README GENERATOR ──────────────────────────────────────
function generateReadme({ profile, domains, roadmap, projects, stack, social }) {
  const { name, github, goal, started, tagline, bio } = profile;
  const lines = [
    `🚀 ${goal} in Progress...`,
    `🧠 Building with Generative AI`,
    `📊 Data Science | ML | LLMs`,
    `⚡ ${tagline}`
  ].join(";");

  let md = `<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=${encodeURIComponent(name)}&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=${encodeURIComponent(goal)}&descAlignY=58&descSize=20&animation=fadeIn" width="100%"/>

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=A78BFA&center=true&vCenter=true&width=600&lines=${encodeURIComponent(lines)}" alt="Typing SVG" /></a>

<br/>

![Started](https://img.shields.io/badge/Started-${encodeURIComponent(started)}-6366f1?style=for-the-badge)
![Goal](https://img.shields.io/badge/Goal-${encodeURIComponent(goal.replace(/ /g,"%20"))}-8b5cf6?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Actively%20Learning-22c55e?style=for-the-badge)
![Open To](https://img.shields.io/badge/Open%20To-Internships-f59e0b?style=for-the-badge)

</div>

---

## 🎯 Mission

${bio.split("\n").filter(Boolean).map(l => `> ${l}`).join("\n")}

---

## 📊 Progress Dashboard

<div align="center">

| Domain | Status | Progress |
|:-------|:------:|:--------:|
`;

  domains.forEach(d => {
    const pct = Math.min(100, Math.max(0, d.pct));
    const c = pct===0?"c4b5fd":pct<30?"f87171":pct<60?"f59e0b":"22c55e";
    const sm = statusMeta[d.status];
    md += `| ${d.label} | ${sm.emoji} ${sm.label} | ![${pct}%](https://progress-bar.xyz/${pct}?title=&width=160&color=${c}) |\n`;
  });

  md += `\n</div>\n\n---\n\n## 🗺️ Learning Roadmap\n\n`;

  roadmap.forEach(r => {
    const done = r.done.filter(Boolean).length;
    const pct = Math.round(done / r.items.length * 100);
    md += `<details${pct > 0 ? " open" : ""}>\n<summary><b>${r.emoji} ${r.title} — ${pct}% Complete</b></summary>\n\n\`\`\`\n`;
    r.items.forEach((item, i) => { md += `${r.done[i] ? "✅" : "⬜"} ${item}\n`; });
    md += `\`\`\`\n</details>\n\n`;
  });

  md += `---\n\n## 🚀 Projects\n\n`;

  projects.forEach(p => {
    md += `### ${p.emoji} ${p.title}\n> **Stack:** ${p.stack}\n\n| Phase | Status |\n|:------|:------:|\n`;
    p.phases.forEach((ph, i) => { md += `| ${ph} | ${p.done[i] ? "✅ Done" : "⬜ Pending"} |\n`; });
    md += `\n---\n\n`;
  });

  if (stack.length > 0) {
    md += `## 🛠️ Tech Stack\n\n<div align="center">\n\n`;
    stack.forEach(s => {
      const c = BADGE_COLORS[s] || "6366f1";
      md += `![${s}](https://img.shields.io/badge/${encodeURIComponent(s)}-${c}?style=for-the-badge&logoColor=white)\n`;
    });
    md += `\n</div>\n\n---\n\n`;
  }

  md += `## 📈 GitHub Stats

<div align="center">

<img height="180em" src="https://github-readme-stats.vercel.app/api?username=${github}&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=a78bfa&icon_color=6366f1"/>
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=${github}&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=a78bfa"/>

[![GitHub Streak](https://streak-stats.demolab.com?user=${github}&theme=tokyonight&hide_border=true&background=0D1117&ring=6366f1&fire=f59e0b)](https://git.io/streak-stats)

![Snake](https://raw.githubusercontent.com/${github}/${github}/output/github-contribution-grid-snake-dark.svg)

</div>

---

## 💭 Current Focus

\`\`\`python
class ${name.replace(/\s+/g, "")}:
    def __init__(self):
        self.name    = "${name}"
        self.goal    = "${goal}"
        self.started = "${started}"
        self.focus   = [${domains.filter(d => d.status !== "not-started").map(d => `"${d.label.replace(/[^\w\s/]/g,"").trim()}"`).join(", ")}]
        self.belief  = "${tagline}"
\`\`\`

---

## 🤝 Connect

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](${social.linkedin})
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](${social.twitter})
[![Gmail](https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:${social.email})
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](${social.kaggle})

![Visitor Count](https://komarev.com/ghpvc/?username=${github}&color=6366f1&style=for-the-badge)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,100:0f0c29&height=100&section=footer" width="100%"/>
`;
  return md;
}

// ── SYNTAX HIGHLIGHTER ────────────────────────────────────
function highlightMd(text) {
  return text
    .split("\n")
    .map(line => {
      const esc = line.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
      if (/^#{1,3} /.test(line)) return `<span class="md-heading">${esc}</span>`;
      if (/^✅/.test(line))      return `<span class="md-check">${esc}</span>`;
      if (/^⬜/.test(line))      return `<span class="md-empty">${esc}</span>`;
      if (/^!\[/.test(line))     return `<span class="md-badge">${esc}</span>`;
      if (/^\[/.test(line))      return `<span class="md-link">${esc}</span>`;
      if (/^>/.test(line))       return `<span class="md-code">${esc}</span>`;
      if (/^\`\`\`/.test(line))  return `<span class="md-keyword">${esc}</span>`;
      return esc;
    })
    .join("\n");
}

// ── MAIN COMPONENT ────────────────────────────────────────
export default function App() {
  const [activeNav, setActiveNav] = useState("profile");
  const [showPreview, setShowPreview] = useState(true);
  const [toast, setToast] = useState(false);

  const [profile, setProfile] = useState({
    name: "Rakesh Rawat", github: "rakeshrawat",
    goal: "AI/ML Engineer", started: "March 2026",
    tagline: "Consistency + Projects + Gen AI",
    bio: "Goal: Become a production-ready AI/ML Engineer — building real systems, not just notebooks.\n\nPhilosophy: Consistency beats intensity. Ship > Perfect. Learn by doing.",
  });
  const [domains, setDomains] = useState(DOMAINS.map(d => ({ ...d })));
  const [roadmap, setRoadmap] = useState(ROADMAP_DATA.map(r => ({ ...r, done: [...r.done] })));
  const [projects, setProjects] = useState(PROJECTS_DATA.map(p => ({ ...p, done: [...p.done] })));
  const [stack, setStack] = useState(new Set(["Python","Pandas","NumPy","SQL","Scikit-learn","LangChain","OpenAI","Git","VS Code","Jupyter","Docker","FastAPI"]));
  const [social, setSocial] = useState({ linkedin:"https://linkedin.com/in/rakeshrawat", twitter:"https://twitter.com/rakeshrawat", email:"rakeshrawat@gmail.com", kaggle:"https://kaggle.com/rakeshrawat" });

  const readme = generateReadme({ profile, domains, roadmap, projects, stack:[...stack], social });

  const copyReadme = useCallback(() => {
    navigator.clipboard.writeText(readme).then(() => {
      setToast(true); setTimeout(() => setToast(false), 2200);
    });
  }, [readme]);

  const downloadReadme = useCallback(() => {
    const blob = new Blob([readme], { type:"text/markdown" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "README.md"; a.click();
  }, [readme]);

  const setDomain = (i, field, val) => setDomains(prev => { const n=[...prev]; n[i]={...n[i],[field]:val}; return n; });
  const setRmDone = (ri, ii, val) => setRoadmap(prev => { const n=prev.map(r=>({...r,done:[...r.done]})); n[ri].done[ii]=val; return n; });
  const setRmItem = (ri, ii, val) => setRoadmap(prev => { const n=prev.map(r=>({...r,items:[...r.items]})); n[ri].items[ii]=val; return n; });
  const setProjDone = (pi, phi, val) => setProjects(prev => { const n=prev.map(p=>({...p,done:[...p.done]})); n[pi].done[phi]=val; return n; });
  const toggleStack = (s) => setStack(prev => { const n=new Set(prev); n.has(s)?n.delete(s):n.add(s); return n; });

  const navLabel = NAV.find(n => n.id === activeNav);

  return (
    <>
      <style>{FONTS}{CSS}</style>
      <div className="app-shell">

        {/* SIDEBAR */}
        <aside className="sidebar">
          <div className="brand">
            <div className="brand-name">README Studio</div>
            <div className="brand-sub">AI/ML Tracker Builder</div>
          </div>
          <div className="nav-section-label">Sections</div>
          {NAV.map(n => (
            <div key={n.id} className={`nav-item${activeNav===n.id?" active":""}`} onClick={() => setActiveNav(n.id)}>
              <div className="nav-icon">{n.icon}</div>
              <div>
                <div>{n.label}</div>
                <div style={{fontSize:9,color:"#2a3a5c",marginTop:1}}>{n.sub}</div>
              </div>
              {activeNav===n.id && <div className="nav-badge">●</div>}
            </div>
          ))}
          <div className="sidebar-footer">
            <div style={{fontSize:10,color:"#2a3a5c",letterSpacing:".1em",textTransform:"uppercase",marginBottom:8}}>View Mode</div>
            <div className="preview-toggle">
              <button className={`pt-btn${!showPreview?" active":""}`} onClick={() => setShowPreview(false)}>Edit only</button>
              <button className={`pt-btn${showPreview?" active":""}`} onClick={() => setShowPreview(true)}>Split view</button>
            </div>
          </div>
        </aside>

        {/* MAIN */}
        <div className="main">
          <div className="topbar">
            <div className="topbar-left">
              <div>
                <div className="section-title">{navLabel?.icon} {navLabel?.label}</div>
                <div className="section-sub">{navLabel?.sub}</div>
              </div>
            </div>
            <div className="topbar-actions">
              {toast && <span className="toast-badge">✓ Copied to clipboard!</span>}
              <button className="btn btn-ghost" onClick={copyReadme}>Copy README</button>
              <button className="btn btn-success" onClick={downloadReadme}>⬇ Download .md</button>
            </div>
          </div>

          <div className="content-area">
            {/* EDIT PANEL */}
            <div className="edit-panel">

              {/* PROFILE */}
              {activeNav === "profile" && (
                <div>
                  <div className="form-section">
                    <div className="form-section-header">
                      <div className="form-section-icon">👤</div>
                      <div>
                        <div className="form-section-title">Personal Info</div>
                        <div className="form-section-sub">Your identity on GitHub</div>
                      </div>
                    </div>
                    <div className="grid-2">
                      <div className="field"><label className="field-label">Full Name</label><input className="field-input" value={profile.name} onChange={e=>setProfile(p=>({...p,name:e.target.value}))} placeholder="Rakesh Rawat"/></div>
                      <div className="field"><label className="field-label">GitHub Username</label><input className="field-input" value={profile.github} onChange={e=>setProfile(p=>({...p,github:e.target.value}))} placeholder="rakeshrawat"/></div>
                    </div>
                    <div className="grid-2">
                      <div className="field"><label className="field-label">Career Goal</label><input className="field-input" value={profile.goal} onChange={e=>setProfile(p=>({...p,goal:e.target.value}))} placeholder="AI/ML Engineer"/></div>
                      <div className="field"><label className="field-label">Journey Started</label><input className="field-input" value={profile.started} onChange={e=>setProfile(p=>({...p,started:e.target.value}))} placeholder="March 2026"/></div>
                    </div>
                    <div className="field"><label className="field-label">Tagline (typing animation)</label><input className="field-input" value={profile.tagline} onChange={e=>setProfile(p=>({...p,tagline:e.target.value}))} placeholder="Consistency + Projects + Gen AI"/></div>
                    <div className="field"><label className="field-label">Bio / Mission Statement</label><textarea className="field-input" value={profile.bio} onChange={e=>setProfile(p=>({...p,bio:e.target.value}))} rows={4}/></div>
                  </div>
                </div>
              )}

              {/* PROGRESS */}
              {activeNav === "progress" && (
                <div className="form-section">
                  <div className="form-section-header">
                    <div className="form-section-icon">📊</div>
                    <div><div className="form-section-title">Learning Progress</div><div className="form-section-sub">Drag slider or type % value</div></div>
                  </div>
                  {domains.map((d, i) => {
                    const pct = Math.min(100, Math.max(0, d.pct));
                    const sm = statusMeta[d.status];
                    return (
                      <div className="prog-row" key={d.key}>
                        <span className="prog-label">{d.label}</span>
                        <div className="prog-track" onClick={e => {
                          const rect = e.currentTarget.getBoundingClientRect();
                          const newPct = Math.round((e.clientX - rect.left) / rect.width * 100 / 5) * 5;
                          setDomain(i, "pct", Math.min(100, Math.max(0, newPct)));
                        }}>
                          <div className="prog-fill" style={{width:`${pct}%`,background:barColor(pct)}}/>
                        </div>
                        <input className="prog-num" type="number" min="0" max="100" value={pct} onChange={e=>setDomain(i,"pct",Math.min(100,Math.max(0,+e.target.value)))}/>
                        <span style={{fontSize:11,color:"#2a3a5c",width:14}}>%</span>
                        <select style={{background:"rgba(8,11,20,.8)",border:`1px solid ${sm.border}`,borderRadius:7,color:sm.color,fontSize:10,padding:"3px 7px",fontFamily:"'Outfit',sans-serif",outline:"none"}}
                          value={d.status} onChange={e=>setDomain(i,"status",e.target.value)}>
                          <option value="ongoing">🟢 Ongoing</option>
                          <option value="learning">🟡 Learning</option>
                          <option value="not-started">🔴 Not Started</option>
                        </select>
                      </div>
                    );
                  })}
                </div>
              )}

              {/* ROADMAP */}
              {activeNav === "roadmap" && (
                <div className="form-section">
                  <div className="form-section-header">
                    <div className="form-section-icon">🗺️</div>
                    <div><div className="form-section-title">Learning Roadmap</div><div className="form-section-sub">Check topics you've completed</div></div>
                  </div>
                  {roadmap.map((r, ri) => (
                    <div className="rm-domain" key={r.key}>
                      <div className="rm-domain-title">{r.emoji} {r.title} — {Math.round(r.done.filter(Boolean).length/r.items.length*100)}%</div>
                      {r.items.map((item, ii) => (
                        <div className="rm-item" key={ii}>
                          <input type="checkbox" className="rm-check" checked={r.done[ii]} onChange={e=>setRmDone(ri,ii,e.target.checked)}/>
                          <input className="rm-input" value={item} onChange={e=>setRmItem(ri,ii,e.target.value)}/>
                          <span style={{fontSize:10,color:r.done[ii]?"#4ade80":"#2a3a5c",width:42,textAlign:"right"}}>{r.done[ii]?"✅ Done":"⬜"}</span>
                        </div>
                      ))}
                    </div>
                  ))}
                </div>
              )}

              {/* PROJECTS */}
              {activeNav === "projects" && (
                <div>
                  {projects.map((p, pi) => (
                    <div className="proj-card" key={p.key}>
                      <div className="proj-header">
                        <span style={{fontSize:18}}>{p.emoji}</span>
                        <div>
                          <div className="proj-name">{p.title}</div>
                          <div className="proj-stack">{p.stack}</div>
                        </div>
                        <div style={{marginLeft:"auto",fontSize:11,color:"#4ade80",fontWeight:700}}>
                          {p.done.filter(Boolean).length}/{p.phases.length} done
                        </div>
                      </div>
                      <div className="proj-body">
                        {p.phases.map((ph, phi) => (
                          <div className="phase-row" key={phi} style={{cursor:"pointer"}} onClick={()=>setProjDone(pi,phi,!p.done[phi])}>
                            <input type="checkbox" className="rm-check" checked={p.done[phi]} onChange={()=>{}} readOnly/>
                            <span className="phase-label">{ph}</span>
                            <span className="phase-status" style={{color:p.done[phi]?"#4ade80":"#2a3a5c"}}>{p.done[phi]?"✅ Done":"⬜ Pending"}</span>
                          </div>
                        ))}
                        <div style={{marginTop:10,height:4,background:"#0d1120",borderRadius:2,overflow:"hidden"}}>
                          <div style={{height:"100%",borderRadius:2,background:"linear-gradient(90deg,#6366f1,#a78bfa)",width:`${Math.round(p.done.filter(Boolean).length/p.phases.length*100)}%`,transition:"width .5s cubic-bezier(.34,1.56,.64,1)"}}/>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}

              {/* STACK */}
              {activeNav === "stack" && (
                <div className="form-section">
                  <div className="form-section-header">
                    <div className="form-section-icon">🛠️</div>
                    <div><div className="form-section-title">Tech Stack</div><div className="form-section-sub">Click to toggle badges</div></div>
                  </div>
                  <div className="stack-grid">
                    {ALL_STACK.map(s => (
                      <div key={s} className={`stack-chip${stack.has(s)?" on":""}`} onClick={()=>toggleStack(s)}>
                        {stack.has(s) && <div className="stack-chip-dot"/>}
                        {s}
                      </div>
                    ))}
                  </div>
                  <div style={{marginTop:14,fontSize:11,color:"#2a3a5c"}}>{stack.size} technologies selected</div>
                </div>
              )}

              {/* SOCIAL */}
              {activeNav === "social" && (
                <div className="form-section">
                  <div className="form-section-header">
                    <div className="form-section-icon">🔗</div>
                    <div><div className="form-section-title">Social Links</div><div className="form-section-sub">Full URLs for your profiles</div></div>
                  </div>
                  {[["linkedin","LinkedIn URL"],["twitter","Twitter / X URL"],["email","Email Address"],["kaggle","Kaggle URL"]].map(([k,lbl])=>(
                    <div className="field" key={k}>
                      <label className="field-label">{lbl}</label>
                      <input className="field-input" value={social[k]} onChange={e=>setSocial(p=>({...p,[k]:e.target.value}))} placeholder={`Your ${lbl}`}/>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* PREVIEW */}
            {showPreview && (
              <div className="preview-panel">
                <div className="preview-header">
                  <div className="preview-dot"/>
                  Live Preview — README.md
                  <span style={{marginLeft:"auto",color:"#1e2a45"}}>{readme.length} chars</span>
                </div>
                <div className="preview-body" dangerouslySetInnerHTML={{__html: highlightMd(readme)}}/>
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  );
}
