from fpdf import FPDF

def facture():
    pdf= FPDF()
    pdf.add_page()


    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 25)
    pdf.cell(0, 0, 'An den Arbeitgeber (genaue Bezeichnung +Adresse)')

    # Insérer une image
    # Syntaxe : Image(nom_de_fichier, coordonnée_x, coordonnée_y, largeur, hauteur)
    pdf.image("kapverLOGO.jpg", x=160, y=2, w=47, h=25)

    pdf.set_font('ARIAL', 'B', 15)
    pdf.set_xy(86, 52)
    pdf.cell(0, 0, 'Urlaubsantrag')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 60)
    pdf.cell(0, 0, 'Name, Vorname: ')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(45, 60)
    pdf.cell(0, 0, ' ...............................')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 68)
    pdf.cell(0, 0, 'Geb. am: ')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(33, 68)
    pdf.cell(0, 0, ' ..................................')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 75)
    pdf.cell(0, 0, 'Personalnummer: ')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(45, 75)
    pdf.cell(0, 0, ' ............................')

    pdf.set_font('ARIAL', 'B', 11)
    pdf.set_xy(15, 82)
    pdf.cell(0, 0, 'Betreff: ')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(29, 82)
    pdf.cell(0, 0, '  Urlaubsantrag')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 97)
    pdf.cell(0, 0, 'Hiermit beantrage ich Urlaub vom')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(73, 97)
    pdf.cell(0, 0, ' ................')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(92, 97)
    pdf.cell(0, 0, '[Datum] bis ')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(112, 97)
    pdf.cell(0, 0, ' ...............')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(130, 97)
    pdf.cell(0, 0, '[Datum].')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 103)
    pdf.cell(0, 0, 'Bei meinen Urlaubstagen handelt es sich um')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(92, 103)
    pdf.cell(0, 0, ' ..................')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(112, 103)
    pdf.cell(0, 0, 'Tage aus dem Vorjahr (Resturlaub)')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 110)
    pdf.cell(0, 0, ' ......................')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(41, 110)
    pdf.cell(0, 0, 'und um')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(54, 110)
    pdf.cell(0, 0, ' ..................................')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(92, 110)
    pdf.cell(0, 0, 'Tage aus diesem Jahr.')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 137)
    pdf.cell(0, 0, '...................')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 142)
    pdf.cell(0, 0, '[Datum des Antrags]')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 155)
    pdf.cell(0, 0, '...................................')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 160)
    pdf.cell(0, 0, '(Unterschrift des Arbeitnehmers)')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 175)
    pdf.cell(0, 0, ' ..................................................................................................................................................................................')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 178)
    pdf.cell(0, 0, ' ..................................................................................................................................................................................')

    pdf.set_font('ARIAL', 'B', 11)
    pdf.set_xy(92, 200)
    pdf.cell(0, 0, 'Antwort des Arbeitgebers')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 210)
    pdf.cell(0, 0, 'Der beantragte Urlaub wird bewilligt /abgelehnt, weil')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(105, 210)
    pdf.cell(0, 0, '............................................')

    pdf.set_font('ARIAL', 'B', 11)
    pdf.set_xy(15, 218)
    pdf.cell(0, 0, '[Begründung des Arbeitgebers].')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 245)
    pdf.cell(0, 0, '..................................')

    pdf.set_font('ARIAL', '', 11)
    pdf.set_xy(15, 252)
    pdf.cell(0, 0, '(Unterschrift des Arbeitgebers)')


     #enregistrer le pdf
    pdf.output('factur1.pdf', 'F')


if __name__=="__main__":
    facture()
