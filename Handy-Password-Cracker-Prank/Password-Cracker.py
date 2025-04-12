import sys
import time
import hashlib


def crack():
    print("Starting password-cracker...")
    time.sleep(2)
    print("Cracking passwords...")
    counter = 0
    while True:
        for word in lib:
            counter += 1
            hash = hashlib.sha256(word.encode("utf-8")).hexdigest() * 3
            sys.stdout.write("\r" + str(hash) + f"\nTried passwords: {str(counter)}")
            sys.stdout.flush()
            # time.sleep(0.01)
    print(f"Password found: {str(hash)}")


lib = ['Der', 'Zeitungsbericht', 'von', 'dem', 'Herausgeber', '"Die', 'Presse', '"', 'am', '6', 'Dezember', '2015',
       'mit', 'dem', 'Titel', '"Geschlechtsstereotype', 'gibt', 'es', 'ja', 'nicht', 'nur', 'in', 'der', 'Schule"',
       'setzt', 'sich', 'mit', 'Geschlechtertrennung', 'an', 'Schule', 'auseinander.', 'Ist', 'Geschlechtstrennung',
       'im', 'Unterricht', 'sinnvoll?', 'Christiane', 'Spiel,', 'Bildungspsychologin,', 'meint,', 'ein',
       '"Science"-Artikel', 'habe', 'über', 'viele', 'Studien', 'hinweg', 'analysiert,', 'ob', 'Monoedukation',
       'besser', 'sei', 'als', 'gemeinsame', 'Erziehung.', 'Es', 'sei', 'klar', 'herausgekommen,', 'dass', 'man',
       'diese', 'Aussage', 'nicht', 'treffen', 'könne.', 'Es', 'sei', 'auch', 'schwierig,', 'ein', 'gutes',
       'Studiendesign', 'zu', 'diesem', 'Thema', 'zu', 'machen.', 'Denn', 'die', 'Eltern,', 'die', 'ihre', 'Töchter',
       'in', 'einer', 'monoedukative', 'Schule', 'geben,', 'seien', 'nicht', 'repräsentativ', 'für', 'alle', 'anderen.',
       'Das', 'gleiche', 'gälte', 'auch', 'für', 'die', 'Lehrer', 'an', 'solchen', 'Schulen.', 'Die', 'Verfasserin',
       'erläutert', 'das', 'Stereotyp', 'der', 'Geschlechter,', 'dass', 'Knaben', 'faul', 'aber', 'begabt', 'sind',
       'und', 'dass', 'Mädchen', 'zwar', 'in', 'gewissen', 'Fächern', 'nicht', 'gut,', 'aber', 'dafür', 'überall',
       'fleißig', 'sind.', 'Dieses', 'Geschlechterbild', 'wird', 'übergeben.', 'Die', 'Folge', 'dieser', 'Vorstellung',
       'ist,', 'dass', 'jene', 'bei', 'Buben', 'und', 'Mädchen', 'hängen', 'bleibt', 'und', 'sie', 'danach', 'leben.',
       'Nach', 'Angabe', 'der', 'Bildungspsychologin', 'tauchen', 'jene', 'Geschlechtsstereotype', 'schon', 'im',
       'Kindergarten,', 'bei', 'Eltern', 'oder', 'in', 'Medien', 'auf.', 'Wenn', 'man', 'aufhöre', 'an', 'die',
       'Sinnhaftigkeit', 'der', 'Geschlechtertrennung', 'zu', 'glauben,', 'wäre', 'man', 'das', 'Problem', 'los.',
       'Der', 'Zeitungsbericht', 'von', 'Susanne', 'Amann', 'mit', 'dem', 'Titel', '"jung', 'und', 'unfair"',
       'thematisiert', 'das', 'Problem', 'beim', 'Kaufverhalten', 'von', 'Kleidern.', 'Immer', 'mehr', 'Menschen',
       'sind', 'sich', 'den', 'Folgen', 'vom', 'Kauf', 'neuer', 'und', 'nicht', 'fair', 'produzierter',
       'Kleidungsstücke', 'bewusst,', 'dennoch,', 'obwohl', 'es', 'mittlerweile', 'viele', 'Alternativen', 'gibt,',
       'ändert', 'sich', 'bei', 'der', 'Nachfrage', 'fast', 'nichts.', 'Junge', 'Konsumenten', 'haben', 'zwar',
       'meistens', 'eine', 'Vorstellung', 'von', 'den', 'schlechten', 'Arbeitsbedingungen', 'der', 'Angestellten,',
       'auch', 'wie', 'das', 'Kleid', 'produziert', 'wird,', 'dennoch', 'ändert', 'sich', 'ihr', 'Kaufverhalten',
       'nicht,', 'so', 'Kirsten', 'Broddle,', 'Textilexpertin', 'bei', 'Greenpeace.', 'Um', 'dies', 'zu', 'ändern,',
       'müssten', 'nachhaltige', 'Kleider', 'erst', 'in', 'Mode', 'kommen,', 'um', 'von', 'den', 'Menschen', 'gekauft',
       'zu', 'werden,', 'auch', 'sollte', 'das', 'ohne', 'Kaufreize', 'und', 'Kompromisse', 'funktionieren,', 'die',
       'Kunden', 'sollten', 'aber', 'keinen', 'übermäßigen', 'Komfort', 'oder', 'niedrigere', 'Preise', 'erwarten.',
       'Die', 'Mode', 'in', 'Richtung', '"Grün', 'denken,', 'verantwortungsvoll', 'kaufen"', 'zu', 'lenken,', 'wird',
       'aber', 'noch', 'ein', 'langer', 'Weg']

if __name__ == '__main__':
    crack()
