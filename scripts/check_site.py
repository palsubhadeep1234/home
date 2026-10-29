"""Audit built HTML links, image alternatives, headings, and template leftovers."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import sys,json
root=Path(sys.argv[1]);errors=[];count=0
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=set();self.h1=0;self.canonical=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='img' and 'alt' not in a:errors.append(f'{file}: image lacks alt')
  for attr in ['href','src']:
   if attr in a:self.refs.append(a[attr])
  if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href')
pages={}
for file in root.rglob('*.html'):
 p=Page();text=file.read_text();p.feed(text);pages[file]=p
 if any(s in text for s in ['Paper Title Number','Relevant Topic in Your Field','Your Name, You.']):errors.append(f'{file}: template text')
 if '/assets/' not in str(file) and 'http-equiv="refresh"' not in text:
  if p.h1!=1:errors.append(f'{file}: {p.h1} H1 headings')
for file,p in pages.items():
 for url in p.refs:
  parsed=urlsplit(url)
  if parsed.scheme or parsed.netloc:continue
  if parsed.path.startswith('/home/'):
   target=root/unquote(parsed.path[len('/home/'):])
  elif parsed.path.startswith('/'):
   errors.append(f'{file}: URL escapes /home/: {url}');continue
  elif parsed.path:target=file.parent/unquote(parsed.path)
  else:target=file
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{file.relative_to(root)}: missing {url}');continue
  if parsed.fragment and target.suffix=='.html':
   dest=pages.get(target)
   if dest and unquote(parsed.fragment) not in dest.ids:errors.append(f'{file.relative_to(root)}: missing anchor {url}')
  count+=1
print(f'Checked {len(pages)} HTML pages and {count} local references.')
for e in errors:print(e)
raise SystemExit(bool(errors))
