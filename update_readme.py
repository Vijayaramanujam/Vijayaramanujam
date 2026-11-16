with open(r'c:\Users\dell\Downloads\TENSORFLOW\README.md', 'r', encoding='utf-8') as f:
    text = f.read()

marker = '### 🛠️ Technical Stack & Skills'
new_section = '''### 📊 Skills & Proficiency Breakdown

<div align="center">
  <img src="assets/skills-master.svg" width="100%" alt="Technologies I Master"/>
</div>

<br/>

### 🛠️ Technical Stack & Frameworks'''

if marker in text:
    text = text.replace(marker, new_section, 1)
    with open(r'c:\Users\dell\Downloads\TENSORFLOW\README.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Inserted successfully')
else:
    print('Marker not found')
