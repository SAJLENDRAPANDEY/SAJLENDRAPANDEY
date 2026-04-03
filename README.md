<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Sajlendra Pandey — Portfolio</title>
  <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Sora:wght@300;400;600;700&display=swap" rel="stylesheet"/>
  <style>
    *{margin:0;padding:0;box-sizing:border-box}
    body{background:#0d0d1a;min-height:100vh;display:flex;justify-content:center;padding:2rem 1rem;font-family:'Sora',sans-serif;color:#e2e8f0}
    .pf{max-width:860px;width:100%}

    /* HERO */
    .hero{position:relative;background:linear-gradient(135deg,#0f0c29,#1a1a4e,#12002a);border-radius:20px;padding:3rem 2.5rem 2.5rem;margin-bottom:2rem;overflow:hidden}
    .hero::before{content:'';position:absolute;top:-60px;right:-60px;width:220px;height:220px;border-radius:50%;background:rgba(131,58,180,0.25);filter:blur(60px)}
    .hero::after{content:'';position:absolute;bottom:-40px;left:30%;width:160px;height:160px;border-radius:50%;background:rgba(29,161,242,0.18);filter:blur(50px)}
    .hero-grid{display:grid;grid-template-columns:1fr auto;gap:2rem;align-items:center;position:relative;z-index:1}
    .greeting{font-size:13px;letter-spacing:3px;text-transform:uppercase;color:#a78bfa;font-weight:400;margin-bottom:0.5rem;font-family:'Space Mono',monospace}
    .hero-name{font-size:2.8rem;font-weight:700;color:#fff;line-height:1.1;margin-bottom:0.5rem}
    .hero-title{font-size:1rem;color:#c4b5fd;font-weight:300;margin-bottom:1.2rem}
    .hero-tags{display:flex;flex-wrap:wrap;gap:8px}
    .tag{background:rgba(167,139,250,0.15);border:1px solid rgba(167,139,250,0.3);color:#c4b5fd;font-size:11px;padding:4px 12px;border-radius:20px;letter-spacing:0.5px}
    .avatar{width:100px;height:100px;border-radius:50%;background:linear-gradient(135deg,#7c3aed,#2563eb);display:flex;align-items:center;justify-content:center;font-size:2rem;font-weight:700;color:#fff;font-family:'Space Mono',monospace;border:3px solid rgba(167,139,250,0.4);flex-shrink:0}

    /* STATS */
    .stats-row{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:2rem}
    .stat-card{background:#1a1a2e;border:0.5px solid rgba(255,255,255,0.08);border-radius:14px;padding:1.2rem 1rem;text-align:center;position:relative;overflow:hidden}
    .stat-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;border-radius:14px 14px 0 0}
    .stat-card.purple::before{background:linear-gradient(90deg,#7c3aed,#a78bfa)}
    .stat-card.blue::before{background:linear-gradient(90deg,#2563eb,#60a5fa)}
    .stat-card.teal::before{background:linear-gradient(90deg,#0d9488,#5eead4)}
    .stat-num{font-size:2rem;font-weight:700;color:#f1f5f9;font-family:'Space Mono',monospace}
    .stat-label{font-size:11px;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;margin-top:4px}

    /* SECTION TITLE */
    .section-title{font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#64748b;margin-bottom:1rem;font-family:'Space Mono',monospace;display:flex;align-items:center;gap:8px}
    .section-title::after{content:'';flex:1;height:0.5px;background:rgba(255,255,255,0.08)}

    /* SKILLS */
    .skills-section{margin-bottom:2rem}
    .skills-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
    .skill-item{background:#1a1a2e;border:0.5px solid rgba(255,255,255,0.08);border-radius:10px;padding:12px 14px}
    .skill-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
    .skill-name{font-size:13px;font-weight:600;color:#e2e8f0}
    .skill-pct{font-size:11px;color:#94a3b8;font-family:'Space Mono',monospace}
    .skill-bar{height:4px;border-radius:4px;background:rgba(255,255,255,0.08);overflow:hidden}
    .skill-fill{height:100%;border-radius:4px;width:0;transition:width 1.2s ease}
    .s-py{background:linear-gradient(90deg,#3b82f6,#8b5cf6)}
    .s-cpp{background:linear-gradient(90deg,#0891b2,#06b6d4)}
    .s-sql{background:linear-gradient(90deg,#f59e0b,#ef4444)}
    .s-bi{background:linear-gradient(90deg,#10b981,#3b82f6)}
    .s-dsa{background:linear-gradient(90deg,#8b5cf6,#ec4899)}
    .s-np{background:linear-gradient(90deg,#f97316,#fbbf24)}

    /* CURRENTLY */
    .currently-section{margin-bottom:2rem}
    .doing-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
    .doing-card{background:#1a1a2e;border:0.5px solid rgba(255,255,255,0.08);border-radius:12px;padding:1rem;text-align:center}
    .doing-icon{font-size:22px;margin-bottom:8px;display:block}
    .doing-text{font-size:12px;color:#94a3b8;line-height:1.5}

    /* PROJECTS */
    .projects-section{margin-bottom:2rem}
    .proj-card{background:#1a1a2e;border:0.5px solid rgba(255,255,255,0.08);border-radius:14px;padding:1.4rem;margin-bottom:12px;cursor:pointer;transition:border-color 0.2s,transform 0.2s;position:relative;overflow:hidden}
    .proj-card:hover{border-color:rgba(124,58,237,0.5);transform:translateY(-2px)}
    .proj-accent{position:absolute;top:0;left:0;bottom:0;width:3px;border-radius:14px 0 0 14px}
    .pa-purple{background:linear-gradient(180deg,#7c3aed,#a78bfa)}
    .pa-teal{background:linear-gradient(180deg,#0d9488,#5eead4)}
    .proj-inner{padding-left:10px}
    .proj-name{font-size:15px;font-weight:600;color:#f1f5f9;margin-bottom:4px}
    .proj-desc{font-size:13px;color:#94a3b8;line-height:1.5;margin-bottom:10px}
    .proj-bottom{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}
    .proj-techs{display:flex;flex-wrap:wrap;gap:6px}
    .tech-badge{background:rgba(124,58,237,0.1);border:1px solid rgba(124,58,237,0.2);color:#8b5cf6;font-size:10px;padding:3px 10px;border-radius:20px;font-family:'Space Mono',monospace}
    .proj-link{font-size:11px;color:#7c3aed;text-decoration:none;font-weight:600;letter-spacing:0.5px}

    /* SOCIAL */
    .social-section{margin-bottom:2rem}
    .social-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
    .social-btn{display:flex;align-items:center;gap:12px;background:#1a1a2e;border:0.5px solid rgba(255,255,255,0.08);border-radius:12px;padding:14px 16px;text-decoration:none;cursor:pointer;transition:border-color 0.2s;color:inherit}
    .social-btn:hover{border-color:rgba(124,58,237,0.4)}
    .social-icon{width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
    .si-li{background:rgba(37,99,235,0.15)}
    .si-gh{background:rgba(124,58,237,0.15)}
    .si-em{background:rgba(13,148,136,0.15)}
    .si-loc{background:rgba(239,68,68,0.15)}
    .s-name{font-size:13px;font-weight:600;color:#e2e8f0}
    .s-handle{font-size:11px;color:#64748b}

    /* FOOTER */
    .footer-quote{text-align:center;padding:1.5rem;background:#1a1a2e;border-radius:12px;border:0.5px solid rgba(255,255,255,0.08)}
    .fq-text{font-size:15px;color:#94a3b8;font-style:italic;margin-bottom:4px}
    .fq-attr{font-size:11px;color:#7c3aed;font-family:'Space Mono',monospace;letter-spacing:1px}

    @media(max-width:600px){
      .hero-grid{grid-template-columns:1fr}
      .avatar{display:none}
      .skills-grid,.social-grid{grid-template-columns:1fr}
      .hero-name{font-size:2rem}
    }
  </style>
</head>
<body>
<div class="pf">

  <!-- HERO -->
  <div class="hero">
    <div class="hero-grid">
      <div>
        <div class="greeting">// hello, world</div>
        <div class="hero-name">Sajlendra<br>Pandey</div>
        <div class="hero-title">B.Tech CSE (Data Science) · Building things that matter</div>
        <div class="hero-tags">
          <span class="tag">Data Analytics</span>
          <span class="tag">Python</span>
          <span class="tag">DSA</span>
          <span class="tag">SQL</span>
          <span class="tag">Power BI</span>
          <span class="tag">Problem Solving</span>
        </div>
      </div>
      <div class="avatar">SP</div>
    </div>
  </div>

  <!-- STATS -->
  <div class="stats-row">
    <div class="stat-card purple">
      <div class="stat-num" id="dsa-cnt">0</div>
      <div class="stat-label">DSA Problems</div>
    </div>
    <div class="stat-card blue">
      <div class="stat-num">3+</div>
      <div class="stat-label">Projects Built</div>
    </div>
    <div class="stat-card teal">
      <div class="stat-num">4</div>
      <div class="stat-label">Core Skills</div>
    </div>
  </div>

  <!-- SKILLS -->
  <div class="skills-section">
    <div class="section-title">Skills &amp; Proficiency</div>
    <div class="skills-grid">
      <div class="skill-item"><div class="skill-top"><span class="skill-name">Python</span><span class="skill-pct">88%</span></div><div class="skill-bar"><div class="skill-fill s-py" data-w="88"></div></div></div>
      <div class="skill-item"><div class="skill-top"><span class="skill-name">DSA / C++</span><span class="skill-pct">82%</span></div><div class="skill-bar"><div class="skill-fill s-cpp" data-w="82"></div></div></div>
      <div class="skill-item"><div class="skill-top"><span class="skill-name">MySQL</span><span class="skill-pct">80%</span></div><div class="skill-bar"><div class="skill-fill s-sql" data-w="80"></div></div></div>
      <div class="skill-item"><div class="skill-top"><span class="skill-name">Power BI</span><span class="skill-pct">75%</span></div><div class="skill-bar"><div class="skill-fill s-bi" data-w="75"></div></div></div>
      <div class="skill-item"><div class="skill-top"><span class="skill-name">Pandas / NumPy</span><span class="skill-pct">85%</span></div><div class="skill-bar"><div class="skill-fill s-np" data-w="85"></div></div></div>
      <div class="skill-item"><div class="skill-top"><span class="skill-name">Data Visualization</span><span class="skill-pct">78%</span></div><div class="skill-bar"><div class="skill-fill s-dsa" data-w="78"></div></div></div>
    </div>
  </div>

  <!-- CURRENTLY -->
  <div class="currently-section">
    <div class="section-title">What I'm Doing</div>
    <div class="doing-grid">
      <div class="doing-card"><span class="doing-icon">🧠</span><div class="doing-text">Solving DSA problems daily</div></div>
      <div class="doing-card"><span class="doing-icon">📊</span><div class="doing-text">Building real-world analytics projects</div></div>
      <div class="doing-card"><span class="doing-icon">🚀</span><div class="doing-text">Growing problem-solving skills</div></div>
    </div>
  </div>

  <!-- PROJECTS -->
  <div class="projects-section">
    <div class="section-title">Featured Projects</div>
    <div class="proj-card" onclick="window.open('https://github.com/SAJLENDRAPANDEY/retail-sales-analytics','_blank')">
      <div class="proj-accent pa-purple"></div>
      <div class="proj-inner">
        <div class="proj-name">📈 Retail Sales Analytics Pipeline</div>
        <div class="proj-desc">End-to-end data analytics pipeline for retail sales — data cleaning, EDA, trend analysis, and visual storytelling using Python and Seaborn.</div>
        <div class="proj-bottom">
          <div class="proj-techs">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">Pandas</span>
            <span class="tech-badge">Seaborn</span>
            <span class="tech-badge">NumPy</span>
          </div>
          <span class="proj-link">View on GitHub →</span>
        </div>
      </div>
    </div>
    <div class="proj-card">
      <div class="proj-accent pa-teal"></div>
      <div class="proj-inner">
        <div class="proj-name">♻️ Waste Not Management System</div>
        <div class="proj-desc">AI-powered platform for smart waste recycling — classifies waste, suggests recycling pathways, and promotes sustainable practices.</div>
        <div class="proj-techs">
          <span class="tech-badge">AI/ML</span>
          <span class="tech-badge">Python</span>
          <span class="tech-badge">Classification</span>
        </div>
      </div>
    </div>
  </div>

  <!-- SOCIAL -->
  <div class="social-section">
    <div class="section-title">Connect With Me</div>
    <div class="social-grid">
      <a class="social-btn" href="https://www.linkedin.com/in/sajlendra-pandey-37378627b/" target="_blank">
        <div class="social-icon si-li">💼</div>
        <div><div class="s-name">LinkedIn</div><div class="s-handle">sajlendra-pandey</div></div>
      </a>
      <a class="social-btn" href="https://github.com/SAJLENDRAPANDEY" target="_blank">
        <div class="social-icon si-gh">🐙</div>
        <div><div class="s-name">GitHub</div><div class="s-handle">SAJLENDRAPANDEY</div></div>
      </a>
      <a class="social-btn" href="mailto:sajlendrapandey2022@gmail.com">
        <div class="social-icon si-em">✉️</div>
        <div><div class="s-name">Email</div><div class="s-handle">sajlendrapandey2022@gmail.com</div></div>
      </a>
      <div class="social-btn">
        <div class="social-icon si-loc">📍</div>
        <div><div class="s-name">Location</div><div class="s-handle">India · Open to Remote</div></div>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <div class="footer-quote">
    <div class="fq-text">"Consistency is the key to success"</div>
    <div class="fq-attr">— Sajlendra Pandey · CSE Data Science</div>
  </div>

</div>

<script>
  window.addEventListener('load', () => {
    // Animate skill bars
    document.querySelectorAll('.skill-fill').forEach(el => {
      el.style.width = el.dataset.w + '%';
    });
    // Animate DSA counter
    let n = 0, target = 150;
    const el = document.getElementById('dsa-cnt');
    const iv = setInterval(() => {
      n += 4;
      if (n >= target) { n = target; clearInterval(iv); }
      el.textContent = n + '+';
    }, 20);
  });
</script>
</body>
</html>
