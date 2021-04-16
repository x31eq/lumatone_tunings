import os
from collections import defaultdict
from glob import glob

try:
    from html import escape
except ImportError:
    from cgi import escape

if not os.path.exists('web'):
    os.mkdir('web')

files_by_period = defaultdict(list)

for filename in glob('*.scl'):
    with open(filename) as scl:
        lines = [line.strip() for line in scl.readlines()]

    non_blank = iter(line for line in lines if not line.startswith('!'))

    description = next(non_blank)
    period = int(next(non_blank))
    files_by_period[period].append((filename, description))

    with open(os.path.join('web', filename), 'w') as dos_scl:
        dos_scl.write('\r\n'.join(lines) + '\r\n')

params = {}
for n_notes, files in files_by_period.items():
    items = '\n'.join(
        sorted(
            '    <li><a href="{}">{}</a></li>\n'
                .format(filename, escape(description))
            for filename, description in files))
    section = '<ul>\n{}\n</ul>\n'.format(items)
    params['tunings' + str(n_notes)] = section

with open('template.html') as template:
    markup = template.read()

with open('web/tunings.html', 'w') as index:
    index.write(markup.format(**params))
