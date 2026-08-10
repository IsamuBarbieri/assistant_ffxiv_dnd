"""Rigenera 01_Manual.md dai quattro manuali. 01-04 sono la SORGENTE; 01_Manual e' DERIVATO.
Uso:  python build_manual.py        (dopo ogni modifica a 01, 02, 03 o 04)

Serve per gli host che accettano pochi file (OpenAI Projects: max 5). Sui Gemini si allegano i
quattro separati e questo file si ignora. In 06 i riferimenti sono NUMERI (01/02/03/04), che
risolvono in entrambe le configurazioni: nessuna versione di 06 da mantenere in doppio.

Non modificare 01_Manual.md a mano: verrebbe sovrascritto, e due copie della stessa cosa che
divergono in silenzio sono il guasto piu' caro di questo progetto.
"""
import io, re
from collections import Counter

SRC = [('01_Races.md', '01', 'RAZZE', 'Razze'),
       ('02_Classes.md', '02', 'JOB E CLASSI', 'Job'),
       ('03_Spells.md', '03', 'INCANTESIMI', 'Incantesimi'),
       ('04_Bestiary.md', '04', 'BESTIARIO', 'Bestiario')]

# Un titolo presente in due manuali diventa indistinguibile una volta uniti: prende un suffisso.
seen = Counter()
for f, *_ in SRC:
    for h in re.findall(r'^#{1,3} (.+)$', io.open(f, encoding='utf-8').read(), re.M):
        seen[h.strip()] += 1
dup = {h for h, n in seen.items() if n > 1}

out = ["# 01_MANUAL — Razze, Job, Incantesimi, Bestiario (quattro manuali in un file)",
       "GENERATO da build_manual.py — non modificare a mano: la sorgente sono 01/02/03/04.",
       "Ogni manuale e' una PARTE. I titoli che comparivano identici in due manuali portano un",
       "suffisso di parte, perche' due sezioni omonime nello stesso file non sono distinguibili",
       "in fase di recupero.", ""]
fixed = 0
for f, num, title, suffix in SRC:
    body = []
    for line in io.open(f, encoding='utf-8').read().split('\n'):
        m = re.match(r'^(#{1,3}) (.+)$', line)
        if m and m.group(2).strip() in dup:
            body.append('%s %s — %s' % (m.group(1), m.group(2).strip(), suffix))
            fixed += 1
        else:
            body.append(line)
    out.append('\n\n# PARTE %s — %s\n' % (num, title))
    out.append('\n'.join(body))

io.open('01_Manual.md', 'w', encoding='utf-8', newline='').write('\n'.join(out))

src_bytes = sum(len(io.open(f, encoding='utf-8').read()) for f, *_ in SRC)
built = len(io.open('01_Manual.md', encoding='utf-8').read())
assert not {h for h, n in Counter(re.findall(r'^#{1,3} (.+)$', io.open('01_Manual.md', encoding='utf-8').read(), re.M)).items() if n > 1}, \
    'collisioni di intestazione residue: la fusione non e\' sicura'
print('01_Manual.md rigenerato — %d KB, %d titoli disambiguati, sorgente %d B -> %d B'
      % (built // 1024, fixed, src_bytes, built))
