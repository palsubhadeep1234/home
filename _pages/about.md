---
layout: faculty
title: "Mechanics, Materials & AI"
permalink: /
home: true
redirect_from:
  - /about/
  - /about.html
description: "Subhadeep Pal develops multiscale mechanics and traceable AI for reliable materials design. Postdoctoral Associate at MIT."
---


<section class="hero">
<div><p class="eyebrow">Multiscale mechanics · Materials design · Scientific AI</p><h1>From molecular mechanisms<br>to resilient materials.</h1><p class="lede">I connect molecular simulation, fracture mechanics, and AI to understand how materials deform and fail—and to turn that understanding into reliable design rules.</p><p class="affiliation"><strong>Subhadeep Pal</strong> · Postdoctoral Associate<br>Department of Civil & Environmental Engineering, MIT</p><div class="actions"><a class="button primary" href="{{ '/projects/' | relative_url }}">Current research</a><a class="button" href="{{ '/future-research/' | relative_url }}">Future research</a></div></div>
<div class="hero-portrait"><img class="portrait" src="{{ '/images/headshot.jpeg' | relative_url }}" alt="Subhadeep Pal" width="270" height="325"><p class="portrait-caption">Molecular insight.<br>Predictive mechanics.<br>Evidence-grounded discovery.</p></div>
</section>
<section class="section"><div class="section-head"><h2>A connected research program</h2><a href="{{ '/future-research/' | relative_url }}">Future research plan →</a></div><p class="lede">How can we design materials that carry load, dissipate energy, and resist failure under realistic conditions?</p>{% include faculty-themes.html %}</section>
<section class="section"><div class="section-head"><h2>Selected work</h2><a href="{{ '/publications/' | relative_url }}">All publications →</a></div><div class="selected-list">{% for pub in site.data.publications %}{% if pub.selected %}<article class="selected-paper"><div class="paper-meta">{{ pub.venue }} · {{ pub.year }}{% if pub.group == 'accepted' %} · In press{% endif %}</div><h3><a href="{{ pub.url }}">{{ pub.title }}</a></h3><p>{{ pub.summary }}</p></article>{% endif %}{% endfor %}</div></section>
<section class="section two-col"><div><h2>Recent news</h2><ul class="news-list"><li><time>Fall 2026</time><p>Teaching assistant for MIT’s graduate course <strong>Atomistic Modeling and Simulation</strong>.</p></li><li><time>2026</time><p>Our study of fresh cement paste rheology appears in <em>Journal of Applied Physics</em> as an <a href="https://doi.org/10.1063/5.0332157">Editor’s Pick</a>.</p></li><li><time>2026</time><p>Co-organized the <strong>ScienceClaw Hackathon</strong> at MIT, bringing together 100 participants from academia and industry.</p></li><li><time>Jan 2026</time><p>Joined MIT as a Postdoctoral Associate in the Laboratory for Atomistic and Molecular Mechanics.</p></li></ul><a class="small-link" href="{{ '/linkedin/' | relative_url }}">Earlier research updates & outreach →</a></div><div class="bio-copy"><h2>About me</h2><p>I am a Postdoctoral Associate in the <a href="https://lamm.mit.edu/">Laboratory for Atomistic and Molecular Mechanics</a> at MIT, working with Professor Markus Buehler. I earned my PhD in Mechanics, Materials, and Structures at Northwestern University with Professor Sinan Keten.</p><p>My work brings together polymer physics, multiscale modeling, active learning, and scientific AI. Across computational and experimental collaborations, I aim to connect physical mechanisms to predictions that can be tested.</p><p>I previously completed an integrated BTech and MTech in Civil & Structural Engineering at IIT Kharagpur.</p><a class="small-link" href="{{ '/contact/' | relative_url }}">Get in touch →</a></div></section>
