import random

# En lista med 500 slumpmässigt valda ord
words = [
    'Abstrakt', 'Akronym', 'Ambivalent', 'Analogi', 'Anarki', 'Anomali', 'Antites', 'Axiom', 'Bifogad', 'Bravur', 'Byråkrati', 'Cirkumvention', 'Cognitiv', 'Delegera', 'Denotation', 'Didaktik', 'Dogmatisk', 'Dynamik', 'Eklatant', 'Eklektisk', 'Empiri', 'Epifani', 'Eufemism', 'Exklusiv', 'Faktor', 'Förfalska', 'Generell', 'Hedonist', 'Hermeneutik', 'Homogen', 'Hypotes', 'Idiosynkrasi', 'Implikation', 'Inferens', 'Juxtaposition', 'Kognitiv', 'Konflikt', 'Konnotation', 'Konvention', 'Korrelation', 'Kritik', 'Kvasi', 'Legitim', 'Logistik', 'Maximal', 'Metamorfos', 'Minimal', 'Missuppfattning', 'Mångfald', 'Neologism', 'Nostalgi', 'Obsolet', 'Okonventionell', 'Optimal', 'Oratorisk', 'Paradigm', 'Paradox', 'Periferi', 'Perspektiv', 'Plausibel', 'Polaritet', 'Postulat', 'Pragmatisk', 'Predikament', 'Prioritera', 'Proaktiv', 'Profil', 'Prospektiv', 'Provokation', 'Pseudonym', 'Relevans', 'Retorik', 'Rudimentär', 'Sanktion', 'Sekvens', 'Semantik', 'Signifikant', 'Sinnebild', 'Spekulativ', 'Stagnera', 'Statistisk', 'Subjektiv', 'Sublim', 'Subversiv', 'Suggestiv', 'Superficiell', 'Syntes', 'Systematisk', 'Teoretisk', 'Terminologi', 'Transcendens', 'Trivial', 'Universal', 'Validitet', 'Varierad', 'Verifiera', 'Virtuell', 'Vital', 'Ytterlighet', 'Övergång']

# Skapa ett dictionary med 500 ord och deras respektive listor av 5 ord
ord_dictionary = {word: random.sample(words, 5) for word in words}

# Testutskrift för att se om dictionaryn har skapats korrekt
for key, value in ord_dictionary.items():
    print(f"{key} : {value}")
