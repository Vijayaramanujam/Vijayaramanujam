import base64

with open(r'c:\Users\dell\Downloads\TENSORFLOW\assets\photo_b64.txt', 'r') as f:
    photo_b64 = f.read().strip()

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="340" viewBox="0 0 850 340">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#030712"/>
      <stop offset="40%" style="stop-color:#080d22"/>
      <stop offset="80%" style="stop-color:#0d1117"/>
      <stop offset="100%" style="stop-color:#050714"/>
    </linearGradient>

    <!-- Glowing Orbs -->
    <radialGradient id="haloCyan" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#00f5d4;stop-opacity:0.6"/>
      <stop offset="60%" style="stop-color:#00f5d4;stop-opacity:0.15"/>
      <stop offset="100%" style="stop-color:#00f5d4;stop-opacity:0"/>
    </radialGradient>
    <radialGradient id="haloPurple" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#7b61ff;stop-opacity:0.6"/>
      <stop offset="60%" style="stop-color:#7b61ff;stop-opacity:0.2"/>
      <stop offset="100%" style="stop-color:#7b61ff;stop-opacity:0"/>
    </radialGradient>

    <!-- Name & Accent Gradients -->
    <linearGradient id="nameGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00f5d4"/>
      <stop offset="45%" style="stop-color:#38bdf8"/>
      <stop offset="80%" style="stop-color:#818cf8"/>
      <stop offset="100%" style="stop-color:#c084fc"/>
    </linearGradient>

    <!-- Avatar clip circle -->
    <clipPath id="avatarClip">
      <circle cx="145" cy="170" r="105"/>
    </clipPath>

    <!-- Filters -->
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="glowStrong">
      <feGaussianBlur stdDeviation="7" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes pulse {{ 0%, 100% {{ opacity: 0.4; }} 50% {{ opacity: 0.95; }} }}
    @keyframes spinOrbit {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
    @keyframes cursorBlink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    @keyframes floatCard {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-5px); }} }}
    
    .orbit-ring {{ animation: spinOrbit 25s linear infinite; transform-origin: 145px 170px; }}
    .orbit-ring-rev {{ animation: spinOrbit 18s linear infinite reverse; transform-origin: 145px 170px; }}
    .status-dot {{ animation: pulse 2s ease-in-out infinite; }}
    .cursor {{ animation: cursorBlink 1s step-end infinite; }}
    .float-badge {{ animation: floatCard 4s ease-in-out infinite; }}
    
    .tag-text {{ font-family: 'Consolas', 'Courier New', monospace; font-size: 11px; }}
    .meta-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
  </style>

  <!-- Dark Cosmic Canvas -->
  <rect width="850" height="340" rx="14" fill="url(#bg)"/>

  <!-- Subtle Cyber Grid -->
  <g opacity="0.035" stroke="#00f5d4" stroke-width="0.5">
    <line x1="0" y1="70" x2="850" y2="70"/>
    <line x1="0" y1="170" x2="850" y2="170"/>
    <line x1="0" y1="270" x2="850" y2="270"/>
    <line x1="300" y1="0" x2="300" y2="340"/>
    <line x1="580" y1="0" x2="580" y2="340"/>
  </g>

  <!-- ══════════════ LEFT: 3D CYBERNETIC AVATAR ══════════════ -->
  <!-- Back Glow Halos -->
  <circle cx="145" cy="170" r="125" fill="url(#haloPurple)"/>
  <circle cx="145" cy="170" r="115" fill="url(#haloCyan)"/>

  <!-- Outer Orbit Rings -->
  <g class="orbit-ring">
    <circle cx="145" cy="170" r="118" fill="none" stroke="#00f5d4" stroke-width="1" stroke-dasharray="12 18" opacity="0.6" filter="url(#glow)"/>
    <circle cx="263" cy="170" r="4" fill="#00f5d4" filter="url(#glow)"/>
    <circle cx="27" cy="170" r="3" fill="#38bdf8"/>
  </g>
  <g class="orbit-ring-rev">
    <circle cx="145" cy="170" r="112" fill="none" stroke="#7b61ff" stroke-width="0.8" stroke-dasharray="25 15" opacity="0.5"/>
    <circle cx="145" cy="58" r="3.5" fill="#c084fc" filter="url(#glow)"/>
    <circle cx="145" cy="282" r="2.5" fill="#ff61d4"/>
  </g>

  <!-- Solid border under avatar -->
  <circle cx="145" cy="170" r="106" fill="none" stroke="#00f5d4" stroke-width="2" filter="url(#glow)"/>

  <!-- User Photo (Clipped) -->
  <g clip-path="url(#avatarClip)">
    <image href="data:image/jpeg;base64,{photo_b64}" x="40" y="45" width="210" height="280" preserveAspectRatio="xMidYMin slice"/>
  </g>

  <!-- Floating 3D Badge on Avatar (Bottom right) -->
  <g transform="translate(195, 245)" class="float-badge">
    <rect width="90" height="26" rx="13" fill="#0a1128" stroke="#00f5d4" stroke-width="1" filter="url(#glow)"/>
    <circle cx="14" cy="13" r="4" fill="#00f5d4" class="status-dot"/>
    <text x="25" y="17" font-family="'Consolas',monospace" font-size="9" fill="#00f5d4" font-weight="bold">AI DEV</text>
  </g>

  <!-- ══════════════ RIGHT: MODERN HERO CONTENT ══════════════ -->
  <g transform="translate(305, 0)">
    <!-- Terminal Prompt Pill -->
    <g transform="translate(0, 42)">
      <rect width="200" height="24" rx="12" fill="#0d152a" stroke="#38bdf8" stroke-width="0.6" stroke-opacity="0.4"/>
      <circle cx="12" cy="12" r="3" fill="#ff5f57" opacity="0.85"/>
      <circle cx="22" cy="12" r="3" fill="#febc2e" opacity="0.85"/>
      <circle cx="32" cy="12" r="3" fill="#28c840" opacity="0.85"/>
      <text x="44" y="16" class="tag-text" fill="#38bdf8" font-size="10">~/vijayaramanujam $</text>
    </g>

    <!-- Greeting and Name -->
    <text x="0" y="102" class="meta-text" font-size="15" font-weight="500" fill="#94a3b8" letter-spacing="1">
      HELLO WORLD, I'M
    </text>
    <text x="0" y="145" class="meta-text" font-size="42" font-weight="900" fill="url(#nameGrad)" letter-spacing="2" filter="url(#glowStrong)">
      VIJAYARAMANUJAM
    </text>
    <!-- Typing Cursor -->
    <rect x="440" y="116" width="3" height="32" fill="#00f5d4" class="cursor" filter="url(#glow)"/>

    <!-- Role and Engineering Tagline -->
    <text x="0" y="178" class="tag-text" font-size="14" fill="#e2e8f0">
      Computer Science Engineer <tspan fill="#7b61ff">//</tspan> <tspan fill="#00f5d4" font-weight="bold">Aspiring AI Developer</tspan>
    </text>

    <!-- Bio Summary -->
    <text x="0" y="206" class="meta-text" font-size="12" fill="#94a3b8">
      Chennai Institute of Technology &#x2022; CGPA: 9.52/10 &#x2022; 564+ LeetCode Solved
    </text>

    <!-- Interactive Glassmorphic Stats Chips -->
    <g transform="translate(0, 230)">
      <!-- Chip 1: AI / Multi-Agent -->
      <g>
        <rect width="125" height="36" rx="8" fill="#0b142c" stroke="#00f5d4" stroke-width="0.8" stroke-opacity="0.5"/>
        <text x="14" y="16" font-size="10" font-family="'Consolas',monospace" fill="#94a3b8">SPECIALTY</text>
        <text x="14" y="29" font-size="11" class="meta-text" fill="#00f5d4" font-weight="bold">Agentic AI &amp; RAG</text>
      </g>
      <!-- Chip 2: Hackathon Trophy -->
      <g transform="translate(135, 0)">
        <rect width="145" height="36" rx="8" fill="#110f2e" stroke="#7b61ff" stroke-width="0.8" stroke-opacity="0.5"/>
        <text x="14" y="16" font-size="10" font-family="'Consolas',monospace" fill="#94a3b8">GLOBAL RECORD</text>
        <text x="14" y="29" font-size="11" class="meta-text" fill="#c084fc" font-weight="bold">&#x1F948; 1st Runner-Up / 5K+</text>
      </g>
      <!-- Chip 3: Competitive Programming -->
      <g transform="translate(290, 0)">
        <rect width="125" height="36" rx="8" fill="#1e0d28" stroke="#ff61d4" stroke-width="0.8" stroke-opacity="0.5"/>
        <text x="14" y="16" font-size="10" font-family="'Consolas',monospace" fill="#94a3b8">LEETCODE</text>
        <text x="14" y="29" font-size="11" class="meta-text" fill="#ff90e8" font-weight="bold">1738 Peak Rating</text>
      </g>
    </g>

    <!-- Social Status Bar (Bottom) -->
    <g transform="translate(0, 286)">
      <circle cx="6" cy="6" r="4" fill="#00f5d4" class="status-dot" filter="url(#glow)"/>
      <text x="18" y="10" class="tag-text" fill="#64748b" font-size="10">
        OPEN FOR AI ENGINEERING COLLABORATIONS &amp; RESEARCH INTERNSHIPS
      </text>
    </g>
  </g>

  <!-- Outer Neon Border Frame -->
  <rect x="2" y="2" width="846" height="336" rx="12" fill="none" stroke="#00f5d4" stroke-width="0.6" opacity="0.3"/>
</svg>'''

with open(r'c:\Users\dell\Downloads\TENSORFLOW\assets\hero-portfolio.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
print('Successfully generated assets/hero-portfolio.svg!')
