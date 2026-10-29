"""Build a public CV from the website's publication data (ReportLab required)."""
from pathlib import Path
import json
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.enums import TA_LEFT
ROOT=Path(__file__).resolve().parents[1]
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='NameCV',fontName='Times-Bold',fontSize=27,leading=31,spaceAfter=9))
styles.add(ParagraphStyle(name='SectionCV',fontName='Helvetica-Bold',fontSize=13,leading=18,spaceBefore=15,spaceAfter=9,textColor=colors.HexColor('#962b3c')))
styles.add(ParagraphStyle(name='BodyCV',fontName='Helvetica',fontSize=9.5,leading=13.5,spaceAfter=7))
styles.add(ParagraphStyle(name='SmallCV',parent=styles['BodyCV'],fontSize=8.6,leading=12,textColor=colors.HexColor('#53616c')))
story=[]
def clean(t):
 for a,b in [('–','-'),('—','-'),('’',"'"),('“','"'),('”','"'),('α','alpha'),('↗','')]:t=t.replace(a,b)
 return t

def p(t,style='BodyCV'): return Paragraph(clean(t),styles[style])
def add(t,style='BodyCV'):story.append(p(t,style))
def heading(t):add(t,'SectionCV')
def item(title,body):story.append(KeepTogether([p('<b>'+title+'</b>'),p(body)]))
def nextpage(title):story.append(PageBreak());add('Subhadeep Pal','NameCV');heading(title)
def paper(pub):
 title=escape(pub['title']);authors=escape(pub['authors']).replace('Pal, S.','<b>Pal, S.</b>')
 label=escape(pub['venue'])+' · '+str(pub['year'])
 if pub['note']:label+=' · '+escape(pub['note'])
 if pub['url']:title='<link href="'+escape(pub['url'])+'" color="#962b3c">'+title+'</link>'
 story.append(KeepTogether([p('<b>'+title+'</b>'),p(authors,'SmallCV'),p('<i>'+label+'</i>','SmallCV'),Spacer(1,7)]))
add('Subhadeep Pal','NameCV')
add('Postdoctoral Associate · Massachusetts Institute of Technology')
add('Cambridge, Massachusetts · <link href="mailto:spu8516@mit.edu">spu8516@mit.edu</link><br/><link href="https://palsubhadeep1234.github.io/home/">palsubhadeep1234.github.io/home</link> · Updated October 2026','SmallCV')
heading('Academic appointments')
item('Massachusetts Institute of Technology · Jan 2026-present','Postdoctoral Associate, Civil &amp; Environmental Engineering<br/>Laboratory for Atomistic and Molecular Mechanics · Advisor: Markus Buehler')
heading('Education')
item('Northwestern University · 2020-2025','PhD in Mechanics, Materials, and Structures, Civil &amp; Environmental Engineering<br/>Advisor: Sinan Keten')
item('Indian Institute of Technology Kharagpur · 2015-2020','Integrated BTech and MTech in Civil &amp; Structural Engineering')
heading('Research interests')
add('Multiscale fracture mechanics; polymer nanocomposites and networks; molecular simulation; active learning and inverse design; traceable scientific AI.')
heading('Honors and research support')
for text in ['2025 · Padden Award Symposium Finalist, APS Division of Polymer Physics','2023-2025 · Ryan Fellowship, International Institute of Nanotechnology, Northwestern','2023-2025 · NSF ACCESS computational allocation: 400,000 compute hours; proposal author and Computational Investigator','2025 · NSF Student Travel Award, Society of Engineering Science','2025 · Student Travel Award, USNCCM18','2024 · Graduate School Spotlight, Northwestern','2020-2021 · Murphy Fellowship, Northwestern','2019 · UTSIP Scholarship, University of Tokyo']:add(text)
pubs=json.loads((ROOT/'_data/publications.json').read_text());published=[x for x in pubs if x['group']=='published']
nextpage('Published journal articles · 2024-2026')
for x in published[:8]:paper(x)
nextpage('Published journal articles · continued')
for x in published[8:]:paper(x)
heading('Accepted / in press')
for x in pubs:
 if x['group']=='accepted':paper(x)
nextpage('Preprints and manuscripts under review')
for x in pubs:
 if x['group']=='preprint':paper(x)
heading('Conference and workshop contributions')
for x in pubs:
 if x['group']=='conference':paper(x)
add('Publication status follows the October 2026 faculty-application CV. * denotes equal contribution.','SmallCV')
nextpage('Teaching, mentoring and service')
item('MIT · Atomistic Modeling and Simulation · Fall 2026','Graduate Teaching Assistant; taught sessions, held office hours, evaluated problem sets, and advised 30 students.')
item('Northwestern · Finite Element Methods in Mechanics · Fall 2022','Graduate Teaching Assistant; coordinated TA work, evaluated assignments, and supported 36 students during office hours.')
item('Northwestern · Structural Analysis - Dynamics · Fall 2021','Grader; assessed assignments and examinations and advised students on course projects.')
heading('Research mentoring')
add('MIT: graduate and undergraduate mentoring (2026-present), alongside high-school research mentoring through the Research Science Institute. Northwestern: doctoral mentoring in civil and mechanical engineering across 2022-2025.')
heading('Leadership')
item('ScienceClaw Hackathon · MIT · 2026','Co-organized a hackathon with 100 academic and industry participants; helped secure $200,000 in sponsorship. Supported by the E14 Seed Fund and industry partners.')
item('Graduate International Student Association · Northwestern · 2021-2025','Treasurer and event organizer; managed budgets and secured $16,000 in funding from the Office of Student Life.')
item('Bengalis in Chicago · UIC · 2021-2024','Event organizer; coordinated volunteers and logistics for cultural events with more than 500 attendees.')
heading('Peer-review service')
add('Nature Chemistry; International Journal of Impact Engineering; Journal of Chemical Physics; Soft Matter; Nanoscale Advances; Journal of Physical Chemistry; npj Computational Materials; Journal of the Mechanical Behavior of Biomedical Materials; Journal of Chemical Information and Modeling.')
add('Conference presentations and detailed research summaries: <link href="https://palsubhadeep1234.github.io/home/cv/">palsubhadeep1234.github.io/home/cv/</link>','SmallCV')
def footer(canvas,doc):
 canvas.saveState();canvas.setStrokeColor(colors.HexColor('#deded8'));canvas.line(48,43,564,43);canvas.setFont('Helvetica',8);canvas.setFillColor(colors.HexColor('#53616c'));canvas.drawString(48,30,'Subhadeep Pal | Curriculum Vitae | October 2026');canvas.drawRightString(564,30,str(doc.page));canvas.restoreState()
doc=SimpleDocTemplate(str(ROOT/'files/Subhadeep_CV.pdf'),pagesize=(612,792),rightMargin=48,leftMargin=48,topMargin=42,bottomMargin=55,title='Subhadeep Pal - Public Curriculum Vitae',author='Subhadeep Pal')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print('Created',ROOT/'files/Subhadeep_CV.pdf')
