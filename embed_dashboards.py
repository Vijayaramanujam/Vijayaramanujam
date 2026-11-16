with open(r'c:\Users\dell\Downloads\TENSORFLOW\README.md', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '### 🚀 Featured Engineering Projects'
end_marker = '### 🏆 Honors & Key Achievements'

new_projects_section = '''### 🚀 Featured Engineering Projects & Dashboards

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/Vijayaramanujam">
        <img src="assets/project-carboniq.png" width="100%" style="border-radius: 8px; border: 1px solid #30363d;" alt="CarbonIQ SME Carbon Intelligence Dashboard"/>
      </a>
      <h3>🌍 <a href="https://github.com/Vijayaramanujam">CarbonIQ</a></h3>
      <p><b>AI-Powered Carbon Accounting & Decarbonization Platform</b></p>
      <ul>
        <li>Automates SME carbon accounting across Scope 1, 2, and 3 emissions.</li>
        <li>Groq Vision invoice OCR with 149 CEA 2024 emission factors.</li>
        <li>Deterministic statutory ledger & decarbonization roadmap generator.</li>
      </ul>
      <p><code>Python</code> <code>FastAPI</code> <code>React.js</code> <code>Groq Vision</code> <code>EEIO-LCA</code></p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Vijayaramanujam">
        <img src="assets/project-medical.jpg" width="100%" style="border-radius: 8px; border: 1px solid #30363d;" alt="Agentic Medical Analyser AI-Powered Diagnostic System"/>
      </a>
      <h3>🏥 <a href="https://github.com/Vijayaramanujam">Agentic Medical Analyser</a></h3>
      <p><b>Multi-Agent AI Healthcare Diagnostic Platform</b></p>
      <ul>
        <li>Intelligent clinical triage, cardiovascular anomaly detection & risk prediction.</li>
        <li>Context-aware RAG pipelines using transformer models with FastAPI backend.</li>
        <li>Automates clinical evidence synthesis, risk stratification, and patient insights.</li>
      </ul>
      <p><code>Python</code> <code>FastAPI</code> <code>Transformers</code> <code>NLP</code> <code>RAG</code></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/Vijayaramanujam">
        <img src="assets/project-analyst.png" width="100%" style="border-radius: 8px; border: 1px solid #30363d;" alt="Business Analyst Financial & Operational Dashboard"/>
      </a>
      <h3>📊 <a href="https://github.com/Vijayaramanujam">Business Analyst Agent</a></h3>
      <p><b>Enterprise AI Business & Financial Intelligence Engine</b></p>
      <ul>
        <li>Generates automated BRDs, use cases, Gantt charts, and financial analytics.</li>
        <li>Leverages Google Agent Development Kit (ADK) & Gemini LLM APIs.</li>
        <li>Automates corporate operational decision support and metric forecasting.</li>
      </ul>
      <p><code>Python</code> <code>Google ADK</code> <code>Gemini</code> <code>Streamlit</code></p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Vijayaramanujam">
        <img src="assets/stats-3d.svg" width="100%" style="border-radius: 8px; border: 1px solid #30363d;" alt="Industrial Vision QC & Competitive Metrics"/>
      </a>
      <h3>🔍 <a href="https://github.com/Vijayaramanujam">Industrial Vision QC System</a></h3>
      <p><b>Defect Detection System @ SmartScope Automation</b></p>
      <ul>
        <li>Computer vision defect identification pipeline on industrial product imagery.</li>
        <li>Dataset preprocessing, geometric augmentation, and CNN model training.</li>
        <li>Supported automated quality inspection and production-line verification.</li>
      </ul>
      <p><code>Python</code> <code>OpenCV</code> <code>CNN</code> <code>Deep Learning</code></p>
    </td>
  </tr>
</table>

---

'''

idx1 = text.find(start_marker)
idx2 = text.find(end_marker)

if idx1 != -1 and idx2 != -1:
    new_text = text[:idx1] + new_projects_section + text[idx2:]
    with open(r'c:\Users\dell\Downloads\TENSORFLOW\README.md', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Updated project section with dashboard previews!')
else:
    print('Could not find markers!')
