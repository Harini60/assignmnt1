import pandas as pd
Title= """
    <title>Exon classes</title>
    <center><h2 >Exon classes</h2>
    <p >Exons contain different combinations of coding and non-coding regions.Statistics for the 12 classes of exnons in the human genome are shown</p></center>
   
"""
element = pd.DataFrame({

    "": ["5'Exons", "5'Exons", "5'Exons", 'Internal Exons', 'Internal Exons', 'Internal Exons',
         'Internal Exons', 'Internal Exons', "3'Exons", "3'Exons", "3'Exons", 'intronless genes'],
    "Class": ['5 Untranslated exon', '5 Untranslated translated exon', '5 Untranslated translated Untranslated exon',
              'Internal Untranslated exon', 'Internal Untranslated translated exon',
              'Internal untranslated translated untranslated exon', 'Internal translated untranslated exon',
              'Internal translated exon', '3 untranslated translated untranslated exon',
              '3 translated untranslated exon', '3 untranslated exon', '5-3 untranslated translated untranslated exon'],
    "image": ["""<img src="https://charts.genome.com/UTRImages/exon_class_img/5'U.svg" />""",
            '''<img src="https://charts.genome.com/UTRImages/exon_class_img/5'UT.svg" />''',
            '''<img src="https://charts.genome.com/UTRImages/exon_class_img/5'UTU.svg" />''',
            '''<img src="https://charts.genome.com/UTRImages/exon_class_img/IU.svg" />''',
            '''<img src="https://charts.genome.com/UTRImages/exon_class_img/IUT.svg" />''',
            '''<img src="https://charts.genome.com/UTRImages/exon_class_img/5'-3'IUTU.svg" />''',
            '''<img src="https://charts.genome.com/UTRImages/exon_class_img/ITU.svg" />''',
            '''<img src="https://charts.genome.com/UTRImages/exon_class_img/IT.svg" />''',
            '''<img src="https://charts.genome.com/UTRImages/exon_class_img/3'UTU.svg" />''',
            '''<img src="https://charts.genome.com/UTRImages/exon_class_img/3'TU.svg" />''',
            '''<img src="https://charts.genome.com/UTRImages/exon_class_img/3'U.svg" />''',
            '''<img src="https://charts.genome.com/UTRImages/exon_class_img/5'-3'UTU.svg" />'''],
    "Genes": [7831, 11410, 810, 2587, 6914, 24, 1134, 15952, 1594, 16335, 1223, 776],
    "Transcripts": [14874, 17768, 813, 4474, 13223, 31, 1785, 29915, 2134, 29847, 1907, 776],
    "Exons": [14898, 17783, 813, 6956, 13280, 31, 1794, 286783, 2139, 29887, 1910, 776],
    "Non-redundant exons": [10432, 12530, 813, 4578, 8066, 26, 1182, 157680, 1650, 18215, 1289, 776]})


Table = element.to_html()
r=Title+Table
f = open("svgdata.html", "w")
f.write(r)
f = open("svgdata.html", "r+")
content = f.read()
f.truncate(0)
re = content.replace('&lt;', '<').replace('&gt;', '>') 
f.write(re)

f.close()