import base64

with open(r'c:\Users\dell\Downloads\TENSORFLOW\assets\photo_b64.txt', 'r') as f:
    photo_b64 = f.read().strip()

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="520" viewBox="0 0 850 520">
  <defs>
    <!-- Background Canvas Gradient -->
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#070913"/>
      <stop offset="50%" style="stop-color:#0a0d1e"/>
      <stop offset="100%" style="stop-color:#050711"/>
    </linearGradient>

    <!-- Purple Glow Orb behind Avatar -->
    <radialGradient id="purpleSphere" cx="45%" cy="45%" r="55%">
      <stop offset="0%" style="stop-color:#9d62ff;stop-opacity:1"/>
      <stop offset="55%" style="stop-color:#6336e4;stop-opacity:0.95"/>
      <stop offset="85%" style="stop-color:#3b189f;stop-opacity:0.8"/>
      <stop offset="100%" style="stop-color:#1c0b5c;stop-opacity:0"/>
    </radialGradient>

    <radialGradient id="ambientCyan" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#00f5d4;stop-opacity:0.25"/>
      <stop offset="100%" style="stop-color:#00f5d4;stop-opacity:0"/>
    </radialGradient>

    <!-- Glowing Drop Shadow for Code Card -->
    <filter id="shadow3D" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000000" flood-opacity="0.75"/>
    </filter>

    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="avatarShadow">
      <feDropShadow dx="-8" dy="12" stdDeviation="14" flood-color="#000000" flood-opacity="0.6"/>
    </filter>

    <!-- Avatar Clip: organic rounded arch matching Alex banner -->
    <clipPath id="avatarArch">
      <ellipse cx="640" cy="245" rx="155" ry="175"/>
    </clipPath>

    <!-- Button Gradient -->
    <linearGradient id="btnGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#6366f1"/>
      <stop offset="100%" style="stop-color:#4f46e5"/>
    </linearGradient>
  </defs>

  <style>
    @keyframes pulseGlow {{ 0%, 100% {{ opacity: 0.85; }} 50% {{ opacity: 1; }} }}
    @keyframes floatCard {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-8px); }} }}
    @keyframes floatBadge {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(6px); }} }}
    @keyframes orbitRotate {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
    @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}

    .pulse {{ animation: pulseGlow 3s ease-in-out infinite; }}
    .float-code {{ animation: floatCard 4.5s ease-in-out infinite; }}
    .float-pill {{ animation: floatBadge 3.5s ease-in-out infinite; }}
    .orbit {{ animation: orbitRotate 22s linear infinite; transform-origin: 640px 225px; }}
    .cursor {{ animation: blink 1s step-end infinite; }}

    .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    .font-mono {{ font-family: 'Consolas', 'Courier New', monospace; }}
  </style>

  <!-- Deep Midnight Canvas -->
  <rect width="850" height="520" rx="16" fill="url(#bg)"/>

  <!-- Subtle ambient cyan beam bottom-left -->
  <circle cx="100" cy="450" r="180" fill="url(#ambientCyan)"/>

  <!-- Background decorative dot grid (top right like CodeCraft) -->
  <g opacity="0.18" fill="#6366f1">
    <circle cx="750" cy="70" r="1.5"/><circle cx="765" cy="70" r="1.5"/><circle cx="780" cy="70" r="1.5"/><circle cx="795" cy="70" r="1.5"/><circle cx="810" cy="70" r="1.5"/>
    <circle cx="750" cy="85" r="1.5"/><circle cx="765" cy="85" r="1.5"/><circle cx="780" cy="85" r="1.5"/><circle cx="795" cy="85" r="1.5"/><circle cx="810" cy="85" r="1.5"/>
    <circle cx="750" cy="100" r="1.5"/><circle cx="765" cy="100" r="1.5"/><circle cx="780" cy="100" r="1.5"/><circle cx="795" cy="100" r="1.5"/><circle cx="810" cy="100" r="1.5"/>
    <circle cx="750" cy="115" r="1.5"/><circle cx="765" cy="115" r="1.5"/><circle cx="780" cy="115" r="1.5"/><circle cx="795" cy="115" r="1.5"/><circle cx="810" cy="115" r="1.5"/>
  </g>

  <!-- ═════════════════ TOP NAVBAR (CodeCraft Style) ═════════════════ -->
  <g transform="translate(35, 32)">
    <!-- Logo -->
    <text x="0" y="16" class="font-sans" font-size="16" font-weight="800" fill="#ffffff" letter-spacing="0.5">
      <tspan fill="#6366f1">&lt;/&gt;</tspan> Vijayaramanujam
    </text>

    <!-- Nav Links -->
    <g transform="translate(290, 4)">
      <text x="0" y="12" class="font-sans" font-size="12" font-weight="600" fill="#ffffff">Home</text>
      <line x1="0" y1="18" x2="32" y2="18" stroke="#6366f1" stroke-width="2" rx="1"/>
      <text x="65" y="12" class="font-sans" font-size="12" font-weight="500" fill="#94a3b8">About</text>
      <text x="130" y="12" class="font-sans" font-size="12" font-weight="500" fill="#94a3b8">Skills</text>
      <text x="190" y="12" class="font-sans" font-size="12" font-weight="500" fill="#94a3b8">Projects</text>
      <text x="265" y="12" class="font-sans" font-size="12" font-weight="500" fill="#94a3b8">Awards</text>
      <text x="335" y="12" class="font-sans" font-size="12" font-weight="500" fill="#94a3b8">Contact</text>
    </g>

    <!-- Top CTA Pill Button -->
    <g transform="translate(685, -2)">
      <rect width="92" height="32" rx="16" fill="url(#btnGrad)" filter="url(#glow)"/>
      <text x="46" y="20" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">Hire Me ↗</text>
    </g>
  </g>

  <!-- Horizontal divider -->
  <line x1="35" y1="68" x2="815" y2="68" stroke="#ffffff" stroke-width="0.5" opacity="0.08"/>

  <!-- ═════════════════ RIGHT: 3D THREE.JS SPHERE & AVATAR ═════════════════ -->
  <!-- 3D Luminous Sphere Backdrop -->
  <circle cx="640" cy="245" r="160" fill="url(#purpleSphere)" class="pulse"/>
  
  <!-- Subtle 3D Orbit rings orbiting around the user photo -->
  <g class="orbit">
    <ellipse cx="640" cy="245" rx="172" ry="172" fill="none" stroke="#a855f7" stroke-width="1.2" stroke-dasharray="14 24" opacity="0.5"/>
    <circle cx="812" cy="245" r="4.5" fill="#38bdf8" filter="url(#glow)"/>
    <circle cx="468" cy="245" r="3" fill="#a855f7"/>
  </g>

  <!-- Clipped Portrait Photo with Arch Frame -->
  <g clip-path="url(#avatarArch)" filter="url(#avatarShadow)">
    <image href="data:image/jpeg;base64,{photo_b64}" x="480" y="70" width="320" height="427" preserveAspectRatio="xMidYMin slice"/>
  </g>

  <!-- Arch Frame Border -->
  <ellipse cx="640" cy="245" rx="155" ry="175" fill="none" stroke="#6366f1" stroke-width="2.5" opacity="0.6"/>

  <!-- Hand-drawn vector swirl (matching Alex's photo decoration) -->
  <path d="M 475,270 Q 455,290 475,310 T 495,330" fill="none" stroke="#ffffff" stroke-width="1.4" opacity="0.35" stroke-linecap="round"/>

  <!-- ═════════════════ FLOATING 3D GLASS CODE CARD (Alex Signature) ═════════════════ -->
  <g transform="translate(620, 160)" class="float-code" filter="url(#shadow3D)">
    <!-- Card Frame -->
    <rect width="195" height="150" rx="12" fill="#0b0f24" fill-opacity="0.92" stroke="#6366f1" stroke-width="1" stroke-opacity="0.4"/>
    <!-- Terminal header -->
    <rect width="195" height="24" rx="12" fill="#131938" fill-opacity="0.6"/>
    <text x="14" y="16" class="font-mono" font-size="9" fill="#94a3b8">&lt;/&gt; Developer.ai</text>
    <circle cx="178" cy="12" r="3" fill="#22c55e" filter="url(#glow)"/>
    
    <!-- Code Content -->
    <text x="14" y="44" class="font-mono" font-size="9" fill="#6366f1">const <tspan fill="#38bdf8">engineer</tspan> = {{</text>
    <text x="22" y="60" class="font-mono" font-size="9" fill="#94a3b8">name: <tspan fill="#34d399">"Vijayaramanujam"</tspan>,</text>
    <text x="22" y="76" class="font-mono" font-size="9" fill="#94a3b8">role: <tspan fill="#34d399">"AI Developer"</tspan>,</text>
    <text x="22" y="92" class="font-mono" font-size="9" fill="#94a3b8">college: <tspan fill="#34d399">"CIT Chennai"</tspan>,</text>
    <text x="22" y="108" class="font-mono" font-size="9" fill="#94a3b8">cgpa: <tspan fill="#f59e0b">9.52</tspan>,</text>
    <text x="22" y="124" class="font-mono" font-size="9" fill="#94a3b8">passion: <tspan fill="#ec4899">"Multi-Agent AI"</tspan></text>
    <text x="14" y="140" class="font-mono" font-size="9" fill="#6366f1">}};</text>
  </g>

  <!-- ═════════════════ LEFT: HERO HEADLINE & ACTIONS ═════════════════ -->
  <g transform="translate(45, 100)">
    <!-- Badge -->
    <g transform="translate(0, 0)">
      <rect width="168" height="26" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="0.8" stroke-opacity="0.5"/>
      <text x="12" y="17" class="font-mono" font-size="10" font-weight="700" fill="#a5b4fc" letter-spacing="1">
        I'M AN AI DEVELOPER
      </text>
    </g>

    <!-- Main Headline -->
    <text x="0" y="65" class="font-sans" font-size="44" font-weight="900" fill="#ffffff" letter-spacing="-0.5">
      Hi, I'm Vijay
    </text>
    <text x="0" y="112" class="font-sans" font-size="38" font-weight="800" fill="#ffffff" letter-spacing="-0.5">
      I build <tspan fill="#6366f1">intelligent AI</tspan>
    </text>
    <text x="0" y="154" class="font-sans" font-size="38" font-weight="800" fill="#ffffff" letter-spacing="-0.5">
      for the future.
    </text>

    <!-- Subtitle -->
    <text x="0" y="188" class="font-sans" font-size="13" font-weight="400" fill="#94a3b8">
      Computer Science student specializing in building production-ready
    </text>
    <text x="0" y="206" class="font-sans" font-size="13" font-weight="400" fill="#94a3b8">
      multi-agent platforms, RAG pipelines, and full-stack software.
    </text>

    <!-- CTA Buttons (View My Work + Download CV) -->
    <g transform="translate(0, 230)">
      <!-- Primary Button -->
      <g>
        <rect width="138" height="42" rx="10" fill="url(#btnGrad)" filter="url(#glow)"/>
        <text x="69" y="26" class="font-sans" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">
          View Projects ↗
        </text>
      </g>
      <!-- Secondary Button -->
      <g transform="translate(150, 0)">
        <rect width="138" height="42" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1"/>
        <text x="69" y="26" class="font-sans" font-size="12" font-weight="600" fill="#cbd5e1" text-anchor="middle">
          Resume / CV ⬇
        </text>
      </g>
    </g>

    <!-- "TECHNOLOGIES I WORK WITH" Row -->
    <g transform="translate(0, 310)">
      <text x="0" y="0" class="font-mono" font-size="9" font-weight="700" fill="#64748b" letter-spacing="1.5">
        TECHNOLOGIES I WORK WITH
      </text>

      <!-- Tech Icon Badges (React, Python, FastAPI, Docker, Gemini, MongoDB) -->
      <g transform="translate(0, 14)">
        <!-- Python -->
        <g transform="translate(0, 0)">
          <rect width="36" height="36" rx="8" fill="#131b34" stroke="#1e293b" stroke-width="1"/>
          <text x="18" y="23" font-size="16" text-anchor="middle">🐍</text>
        </g>
        <!-- React -->
        <g transform="translate(44, 0)">
          <rect width="36" height="36" rx="8" fill="#131b34" stroke="#1e293b" stroke-width="1"/>
          <text x="18" y="23" font-size="16" text-anchor="middle">⚛️</text>
        </g>
        <!-- FastAPI / Lightning -->
        <g transform="translate(88, 0)">
          <rect width="36" height="36" rx="8" fill="#131b34" stroke="#1e293b" stroke-width="1"/>
          <text x="18" y="23" font-size="16" text-anchor="middle">⚡</text>
        </g>
        <!-- AI Brain -->
        <g transform="translate(132, 0)">
          <rect width="36" height="36" rx="8" fill="#131b34" stroke="#1e293b" stroke-width="1"/>
          <text x="18" y="23" font-size="16" text-anchor="middle">🧠</text>
        </g>
        <!-- Docker -->
        <g transform="translate(176, 0)">
          <rect width="36" height="36" rx="8" fill="#131b34" stroke="#1e293b" stroke-width="1"/>
          <text x="18" y="23" font-size="16" text-anchor="middle">🐳</text>
        </g>
        <!-- Database -->
        <g transform="translate(220, 0)">
          <rect width="36" height="36" rx="8" fill="#131b34" stroke="#1e293b" stroke-width="1"/>
          <text x="18" y="23" font-size="16" text-anchor="middle">🍃</text>
        </g>
      </g>
    </g>
  </g>

  <!-- External Frame Accent -->
  <rect x="2" y="2" width="846" height="516" rx="14" fill="none" stroke="#6366f1" stroke-width="0.6" opacity="0.3"/>
</svg>'''

with open(r'c:\Users\dell\Downloads\TENSORFLOW\assets\codecraft-hero.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
print('Successfully generated assets/codecraft-hero.svg!')
