
prompt = f"""
Je vais te fournir des offres d'emploi. Certaines sont en Français et d'autres et Anglais. Pour chacun de ces offres, tu devras extraire uniquement:
- Les missions à effectuer(réduites, courtes)
- les compétences techniques(décomposées en un mot-clé par ligne si possible) requises
- les compétences techniques(décomposées en un mot-clé par ligne si possible) souhaitables ou appréciées sans être requises
- les compétences non techniques(décomposées en un mot-clé par ligne si possible) attendues requises
- Outils et technologies à maîtriser

J'ai besoin de pouvoir structure et sauvegarder ces informations dans une base de données, d'avoir des libellés communs pour plusieurs façons d'exprimer une compétences, etc..
Il est donc très important de les réduire aux maximum(pas de phrases).
Les missions peuvent contenir des verbes d'actions mais rester très court et décomposés(une compétence à la fois par ligne, pas de "et")
Les compétences et outils doivent être des mots clés dans la mesure du possible avec un mot-clé par ligne. Il faut gérer la séparation de mots clés si dans un annonce on en trouve plusieurs su la même ligne
J'aimerais que le résultat soit sous la forme d'un JSON avec les clés: missions, required_technical_skills, desirable_technical_skills, required_non_technical_skills, tools_and_technologies.
"""
