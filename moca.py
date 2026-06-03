
import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    p, label {
        font-size: 20px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.header("Montréal Cognitive Assessment (MoCA)")

st.write("Le Montreal cognitive assessment (MoCA) a été conçu pour l’évaluation des dysfonctions cognitives légères. Il évalue les fonctions suivantes : l’attention, la concentration, les fonctions exécutives, la mémoire, le langage, les capacités visuoconstructives, les capacités d’abstraction, le calcul et l’orientation. Le temps d’exécution est de dix minutes approximativement. Le nombre de points maximum est de 30 ; un score de 26 et plus est considéré normal.")

score_total = 0
score_nsc = 0
score_visuospatial = 0
score_horloge = 0
score_denomination = 0
score_attention = 0
score_calcul = 0
score_langage = 0
score_phrase = 0
score_abstraction = 0
score_memoire = 0
score_rappel_libre = 0
score_rappel_indice = 0
score_rappel_choix = 0
memory_index_score = 0
score_orientation = 0

reponses_fausses_visuospatial = []
reponses_fausses_attention = []
reponses_fausses_langage = []
reponses_fausses_memoire = []
reponses_fausses_orientation = []

atteinte = "aucune atteinte"

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "Niveau de scolarité",
    "Visuospatial",
    "Dénomination",
    "Mémoire",
    "Attention",
    "Langage",
    "Abstraction",
    "Rappel",
    "Orientation",
    "Résultat"
])

# ==== NIVEAU DE SCOLARITE ====
with tab1:
    st.header("Niveau de scolarité")
    nsc = st.radio("Nombre d'années de scolarité", options=["≤ 12 ans de scolarité", "> 12 ans de scolarité"], index=None)
    if nsc == "≤ 12 ans de scolarité":
        score_nsc = score_nsc + 1

# ==== VISUOSPATIAL EXECUTIF ====
with tab2:
    st.header("Visuospatial")
    st.subheader("TMT B")
    st.write("Donner les instructions suivantes, en indiquant l’endroit approprié sur la feuille : *Je veux que vous traciez une ligne en alternant d’un chiffre à une lettre, tout en respectant l’ordre chronologique et l’ordre de l’alphabet. Commencez ici (indiquez le 1) et tracez la ligne vers la lettre A, ensuite vers le 2, etc. Terminez ici (indiquez le E).*")

    vrai = st.checkbox("1 point", key="tmtb_vrai")
    faux = st.checkbox("0 point", key="tmtb_faux")

    if vrai:
        score_visuospatial = score_visuospatial + 1
    elif faux:
        reponses_fausses_visuospatial.append("TMT B")

    st.write("N’allouez aucun point si une erreur n’est pas immédiatement corrigée par le sujet.")
    st.subheader("Cube")
    st.write("L’examinateur donne les instructions suivantes, indiquant cube : *Je veux que vous copiez ce dessin le plus précisément possible.*")

    critere1 = st.checkbox("Le dessin est tridimensionnel")
    critere2 = st.checkbox("Toutes les arêtes sont présentes")
    critere3 = st.checkbox("Il n’y a pas d’arête supplémentaire")
    critere4 = st.checkbox(
        "Les arêtes sont relativement parallèles et de même longueur approximative (les prismes rectangulaires sont acceptables)")

    if critere1 and critere2 and critere3 and critere4:
        score_visuospatial = score_visuospatial + 1
    elif critere1 or critere2 or critere3 or critere4:
        reponses_fausses_visuospatial.append("cube")

# ==== HORLOGE ====

    st.subheader("Horloge")
    st.write("Indiquant l’espace approprié, l’examinateur donne les instructions suivantes : *Maintenant je veux que vous dessiniez une horloge en plaçant tous les chiffres et indiquant l’heure à 11h10.*")

    horloge_cercle = st.checkbox(
        "Le contour est un cercle avec peu de déformation (e.g. déformation mineure de la fermeture du cercle)")
    horloge_nb1 = st.checkbox(
        "Tous les chiffres sont présents sans aucun chiffre en surplus (les chiffres romains sont acceptés)")
    horloge_nb2 = st.checkbox("Les chiffres doivent être dans le bon ordre")
    horloge_nb3 = st.checkbox(
        "Les chiffres sont bien positionnés (les chiffres inscrits à l’extérieur du contour sont acceptés)")
    aiguille_nb1 = st.checkbox("Les deux aiguilles indiquent la bonne heure")
    aiguille_nb2 = st.checkbox("L’aiguille de l’heure est clairement plus petite que l’aiguille des minutes")
    aiguille_nb3 = st.checkbox("La jonction des aiguilles est proche du centre de l’horloge")

    if horloge_cercle:
        score_visuospatial = score_visuospatial + 1
        score_horloge = score_horloge + 1

    if horloge_nb1 and horloge_nb2 and horloge_nb3:
        score_visuospatial = score_visuospatial + 1
        score_horloge = score_horloge + 1

    if aiguille_nb1 and aiguille_nb2 and aiguille_nb3:
        score_visuospatial = score_visuospatial + 1
        score_horloge = score_horloge + 1

    if score_horloge < 3 and (
            horloge_cercle or horloge_nb1 or horloge_nb2 or horloge_nb3 or aiguille_nb1 or aiguille_nb2 or aiguille_nb3):
        reponses_fausses_visuospatial.append("horloge")

# === DENOMINATION ===
with tab3:
    st.header("Dénomination")
    st.write("Demander au sujet de nommer le nom de chacun des animaux, de la gauche vers la droite.")

    lion = st.checkbox("Lion")
    rhino = st.checkbox("Rhinocéros")
    dromadaire = st.checkbox("Dromadaire")

    if lion:
        score_denomination = score_denomination + 1

    if rhino:
        score_denomination = score_denomination + 1

    if dromadaire:
        score_denomination = score_denomination + 1

# ==== MEMOIRE ====
with tab4:
    st.header("Mémoire")
    st.write("Donner les instructions suivantes : *Ceci est un test de mémoire. Je vais vous lire une liste de mots que vous aurez à retenir. Écoutez attentivement et quand j’aurai terminé, je veux que vous me redisiez le plus de mots possible dont vous pouvez vous rappeler, dans l’ordre que vous voulez.*")
    st.write("Lire la liste de mots une première fois et noter chacun des mots énoncés par le sujet.")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        visage1 = st.checkbox("Visage", key="memoire_visage1")
    with col2:
        velours1 = st.checkbox("Velours", key="memoire_velours1")
    with col3:
        eglise1 = st.checkbox("Eglise", key="memoire_eglise1")
    with col4:
        marguerite1 = st.checkbox("Marguerite", key="memoire_marguerite1")
    with col5:
        rouge1 = st.checkbox("Rouge", key="memoire_rouge1")

    st.write("Lorsque le sujet a terminé (s’est souvenu de tous les mots), ou s’il ne peut se rappeler davantage de mots, relire la liste de mots après avoir donné les instructions suivantes : *Maintenant je vais lire la même liste de mots une seconde fois. Essayez de vous rappeler du plus grand nombre de mots possible, y compris ceux que vous avez énoncés la première fois. *")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        visage2 = st.checkbox("Visage", key="memoire_visage2")
    with col2:
        velours2 = st.checkbox("Velours", key="memoire_velours2")
    with col3:
        eglise2 = st.checkbox("Eglise", key="memoire_eglise2")
    with col4:
        marguerite2 = st.checkbox("Marguerite", key="memoire_marguerite2")
    with col5:
        rouge2 = st.checkbox("Rouge", key="memoire_rouge2")

    st.write("Informer le sujet qu’il devra retenir ces mots car il aura à les redire à la fin du test.")

# ===== ATTENTION =====
with tab5:
    st.header("Attention")
    st.subheader("Empans")
    st.write("Lire une séquence de 5 chiffres à un rythme de 1 par seconde, après avoir donné les instructions suivantes : *Je vais vous dire une série de chiffres, et lorsque j’aurai terminé, je veux que vous répétiez ces chiffres dans le même ordre que je vous les ai présentés.*")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("**Empan endroit**")
    with col2:
        st.write("**2 - 1 - 8 - 5 - 4**")
    with col3:
        vrai = st.checkbox("Vrai", key="endroit_vrai")
    with col4:
        faux = st.checkbox("Faux", key="endroit_faux")

    if vrai:
        score_attention = score_attention + 1
    elif faux:
        reponses_fausses_attention.append("empan endroit")

    st.write("Lire ensuite une séquence de 3 chiffres à un rythme de 1 par seconde, après avoir donné les instructions suivantes : *Je vais vous dire une série de chiffres, et lorsque j’aurai terminé, je veux que vous répétiez ces chiffres dans l’ordre inverse que je vous les ai présentés.*")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("**Empan inverse**")
    with col2:
        st.write("**7 - 4 - 2**")
    with col3:
        vrai = st.checkbox("Vrai", key="envers_vrai")
    with col4:
        faux = st.checkbox("Faux", key="envers_faux")

    if vrai:
        score_attention = score_attention + 1
    elif faux:
        reponses_fausses_attention.append("empan inverse")

    st.subheader("Attention sélective")
    st.write("L’examinateur lit une série de lettres à un rythme de 1 par seconde, après avoir donné les instructions suivantes : *Je vais vous lire une série de lettres. Chaque fois que je dirai la lettre A, vous devrez taper de la main une fois. Lorsque je dirai une lettre différente du A, vous ne taperez pas de la main.*")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("**F -  B  - A  - C  - M  - N  - A  - A  - J  - K -  L  - B  - A  - F -  A -  K  - D  - E  - A -  A  - A -  J -  A -  M  - O  - F  - A -  A  - B**")
        st.write("Noter à droite le nombre d'erreur commise (e.g. tape sur une mauvaise lettre ou omet de taper sur une lettre A).")
    with col2:
        erreurs = st.number_input("Erreurs", min_value=-1, max_value=30, value=-1, step=1)

    if erreurs == -1:
        st.warning("⚠️ Pensez à saisir le nombre d'erreurs (même si la personne ne fait aucune erreur)")

    if erreurs >= 0 and erreurs < 2:
        score_attention = score_attention + 1
    elif erreurs >= 2:
        reponses_fausses_attention.append("attention sélective")

    st.subheader("Calcul")
    st.write("L’examinateur donne les instructions suivantes : *Maintenant je veux que vous calculiez 60 - 7, et ensuite, continuez de soustraire 7 de votre réponse, jusqu’à ce que je vous dise d'arrêter.*")
    st.write("L’examinateur peut répéter les instructions une deuxième fois si nécessaire.")

    calcul1_vrai = False
    calcul2_vrai = False
    calcul3_vrai = False
    calcul4_vrai = False
    calcul5_vrai = False

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.write("**1.**")
    with col2:
        st.write("60 - 7")
    with col3:
        st.write("= **53**")
    with col4:
        vrai = st.checkbox("Vrai", key="calcul1_vrai")
    with col5:
        faux = st.checkbox("Faux", key="calcul1_faux")
    with col6:
        resultat1 = st.number_input("", min_value=0, max_value=1000, value=53, step=1, label_visibility="collapsed")

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.write("**2.**")
    with col2:
        st.write(f"{resultat1} - 7")
    with col3:
        st.write(f"= **{resultat1 - 7}**")
    with col4:
        vrai = st.checkbox("Vrai", key="calcul2_vrai")
    with col5:
        faux = st.checkbox("Faux", key="calcul2_faux")
    with col6:
        resultat2 = st.number_input("", min_value=0, max_value=1000, value=46, step=1, label_visibility="collapsed")

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.write("**3.**")
    with col2:
        st.write(f"{resultat2} - 7")
    with col3:
        st.write(f"= **{resultat2 - 7}**")
    with col4:
        vrai = st.checkbox("Vrai", key="calcul3_vrai")
    with col5:
        faux = st.checkbox("Faux", key="calcul3_faux")
    with col6:
        resultat3 = st.number_input("", min_value=0, max_value=1000, value=39, step=1, label_visibility="collapsed")

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.write("**4.**")
    with col2:
        st.write(f"{resultat3} - 7")
    with col3:
        st.write(f"= **{resultat3 - 7}**")
    with col4:
        vrai = st.checkbox("Vrai", key="calcul4_vrai")
    with col5:
        faux = st.checkbox("Faux", key="calcul4_faux")
    with col6:
        resultat4 = st.number_input("", min_value=0, max_value=1000, value=33, step=1, label_visibility="collapsed")

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.write("**5.**")
    with col2:
        st.write(f"{resultat4} - 7")
    with col3:
        st.write(f"= **{resultat4 - 7}**")
    with col4:
        vrai = st.checkbox("Vrai", key="calcul5_vrai")
    with col5:
        faux = st.checkbox("Faux", key="calcul5_faux")
    with col6:
        resultat5 = st.number_input("", min_value=0, max_value=1000, value=26, step=1, label_visibility="collapsed")

    nb_vrai = sum([calcul1_vrai, calcul2_vrai, calcul3_vrai, calcul4_vrai, calcul5_vrai])

    if nb_vrai >= 4:
        score_calcul = 3
        score_attention = score_attention + 3
    elif nb_vrai >= 2:
        score_calcul = 2
        score_attention = score_attention + 2
    elif nb_vrai == 1:
        score_calcul = 1
        score_attention = score_attention + 1
    else:
        score_calcul = 0

# ==== LANGAGE ====
with tab6:
    st.header("Langage")
    st.subheader("Répétition de phrase")
    st.write("*Maintenant je vais vous lire une phrase et je veux que vous la répétiez après moi.*")

    col1, col2, col3 = st.columns([2,1,3])
    with col1:
        st.write("**Le colibri a déposé ses oeufs sur le sable**")
    with col2:
        vrai = st.checkbox("Vrai", key="phrase1_vrai")
    with col3:
        faux = st.checkbox("Faux", key="phrase1_faux")

    if vrai:
        score_langage = score_langage + 1
    elif faux :
        reponses_fausses_langage.append("répétition de phrase")

    col1, col2, col3 = st.columns([2, 1, 3])
    with col1:
        st.write("**L’argument de l’avocat les a convaincus**")
    with col2:
        vrai = st.checkbox("Vrai", key="phrase2_vrai")
    with col3:
        faux = st.checkbox("Faux", key="phrase2_faux")

    if vrai:
        score_langage = score_langage + 1
    elif faux:
        reponses_fausses_langage.append("répétition de phrase")

    st.write("Un point est alloué pour chaque phrase correctement répétée. La répétition doit être exacte. L’examinateur sera vigilant pour les erreurs d’omission, de substitution et d’addition.")

    st.subheader("Fluidité verbale")
    st.write("L’examinateur donne les instructions suivantes : *Je veux que vous me disiez le plus de mots possible qui débutent par une lettre de l’alphabet que je vais vous dire. Vous pouvez dire n’importe quelle sorte de mot, sauf les noms propres, des chiffres, les conjugaisons de verbe (e.g. mange, mangerons, mangerez) et les mots de même famille (e.g. pomme, pommette, pommier). Je vais vous dire d’arrêter après une minute. Êtes-vous prêt ? Maintenant, dites le plus de mots possible qui commencent par la lettre F.*")

    col1, col2= st.columns([2, 1])
    with col1:
        st.text_area("**Notez les mots ci-dessous**", height=150)
    with col2:
        mots = st.number_input("**Nombre total de mots**", min_value=0, max_value=100, value=0, step=1)

    if mots > 10:
        score_langage = score_langage + 1
    elif mots >= 0:
        reponses_fausses_langage.append("fluidité verbale")

# ==== ABSTRACTION ====
with tab7:
    st.header("Abstraction")
    st.write("L’examinateur demande au sujet de donner le point commun entre deux items présentés, en illustrant par l’exemple suivant.")

    col1, col2, col3 = st.columns([2, 1, 3])
    with col1:
        st.write("**En quoi une orange et une banane sont-elles semblables ?**")
    with col2:
        vrai = st.checkbox("Ce sont des fruits", key="sim1_vrai")
    with col3:
        faux = st.checkbox("Toute autre réponse", key="sim1_faux")

    st.write("Si le sujet fournit une réponse concrète, l’examinateur demande à une seule autre reprise : *Donnez-moi une autre raison pour laquelle une orange et une banane se ressemblent*")
    st.write("Si le sujet ne donne pas la bonne réponse, dites : *Oui, et elles sont toutes les deux des fruits.*")
    st.write("Ne pas donner d’autres instructions ou explications.")

    col1, col2, col3, col4= st.columns([2,1,1,1])
    with col1:
        st.write("**En quoi le train et la bicyclette sont-ils semblables ?**")
    with col2:
        sim1_vrai1  = st.checkbox("Moyen de transport/locomotion", key="sim2_vrai")
    with col3:
        sim1_vrai2  = st.checkbox("Pour voyager", key="sim22_vrai")
    with col4:
        faux = st.checkbox("Toute autre réponse", key="sim2_faux")

    if sim1_vrai1 or sim1_vrai2:
        score_abstraction = score_abstraction + 1

    col1, col2, col3, col4 = st.columns([2,1,1,1])
    with col1:
        st.write("**En quoi la montre et la règle sont-elles semblables ?**")
    with col2:
        sim2_vrai1 = st.checkbox("Instrument de mesure", key="sim3_vrai")
    with col3:
        sim2_vrai2 = st.checkbox("Pour mesurer", key="sim31_vrai")
    with col4:
        faux = st.checkbox("Toute autre réponse", key="sim3_faux")

    if sim2_vrai1 or sim2_vrai2:
        score_abstraction = score_abstraction + 1

# ==== RAPPEL ====
with tab8:
    st.header("Rappel")
    st.subheader("Rappel libre")
    st.write("L’examinateur donne les instructions suivantes : *Je vous ai lu une série de mots plus tôt dont je vous ai demandé de vous rappeler. Maintenant, dites-moi tous les mots dont vous vous rappelez*")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        visage3 = st.checkbox("Visage", key="memoire_visage3")
    with col2:
        velours3 = st.checkbox("Velours", key="memoire_velours3")
    with col3:
        eglise3 = st.checkbox("Eglise", key="memoire_eglise3")
    with col4:
        marguerite3 = st.checkbox("Marguerite", key="memoire_marguerite3")
    with col5:
        rouge3 = st.checkbox("Rouge", key="memoire_rouge3")

    st.write("Un point est alloué pour chacun des mots rappelés spontanément, sans indice.")

    score_rappel_libre = sum([visage3, velours3, eglise3, marguerite3, rouge3])
    score_memoire = score_rappel_libre

    if score_rappel_libre < 5:
        reponses_fausses_memoire.append(f"difficulté de rappel libre ({score_rappel_libre}/5)")

    st.subheader("Rappel indicé")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        visage4 = st.checkbox("Partie du corps", key="memoire_visage4")
    with col2:
        velours4 = st.checkbox("Tissu", key="memoire_velours4")
    with col3:
        eglise4 = st.checkbox("Bâtiment", key="memoire_eglise4")
    with col4:
        marguerite4 = st.checkbox("Fleur", key="memoire_marguerite4")
    with col5:
        rouge4 = st.checkbox("Couleur", key="memoire_rouge4")

    score_rappel_indice = sum([visage4, velours4, eglise4, marguerite4, rouge4])

    if score_rappel_libre < 5 and score_rappel_indice + score_rappel_libre == 5 and score_rappel_indice != 0:
        reponses_fausses_memoire.append(f"compensation par l'indiçage ({score_rappel_indice}/5)")
    elif score_rappel_libre < 5 and score_rappel_indice + score_rappel_libre < 5 and score_rappel_indice != 0:
        reponses_fausses_memoire.append(f"compensation partielle par l'indiçage ({score_rappel_indice}/5)")
    elif score_rappel_libre < 5 and score_rappel_indice == 0:
        reponses_fausses_memoire.append(f"difficulté de rappel indicé ({score_rappel_indice}/5)")

    st.subheader("Rappel par choix de réponse")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        nez = st.checkbox("Nez", key="memoire_nez")
        visage5 = st.checkbox("Visage", key="memoire_visage5")
        main = st.checkbox("Main", key="memoire_main")
    with col2:
        denim = st.checkbox("Denim", key="memoire_denim")
        coton = st.checkbox("Coton", key="memoire_coton")
        velours5 = st.checkbox("Velours", key="memoire_velours5")
    with col3:
        eglise5 = st.checkbox("Eglise", key="memoire_eglise5")
        ecole = st.checkbox("Ecole", key="memoire_ecole")
        hopital = st.checkbox("Hôpital", key="memoire_hopital")
    with col4:
        rose = st.checkbox("Rose", key="memoire_rose")
        marguerite5 = st.checkbox("Marguerite", key="memoire_marguerite5")
        tulipe = st.checkbox("Tulipe", key="memoire_tulipe")
    with col5:
        rouge5 = st.checkbox("Rouge", key="memoire_rouge5")
        bleu = st.checkbox("Bleu", key="memoire_bleu")
        vert = st.checkbox("Vert", key="memoire_vert")

    score_rappel_choix = sum([visage5,velours5,eglise5,marguerite5,rouge5])
    memory_index_score = score_rappel_libre * 3 + score_rappel_indice * 2 + score_rappel_choix

    if score_rappel_indice + score_rappel_libre < 5 and score_rappel_choix > 1:
        reponses_fausses_memoire.append(f"compensation par reconnaissance ({score_rappel_choix}/5)")
    elif score_rappel_indice + score_rappel_libre < 5 and score_rappel_choix == 0:
        reponses_fausses_memoire.append(f"difficulté de reconnaissance ({score_rappel_choix}/5)")

# ==== ORIENTATION ====
with tab9:
    st.header("Orientation")
    st.write("Un point est alloué pour chacune des réponses exactement énoncées. Le sujet doit dire la date exacte et l’endroit exact (hôpital, clinique, bureau, etc.). Aucun point n’est alloué si le sujet se trompe d’une seule journée pour la date et le jour. ")

    questions_orientation = [
        {"label": "Quelle est la date aujourd'hui ?", "key": "date", "erreur": "date"},
        {"label": "Quel est le mois ?", "key": "mois", "erreur": "mois"},
        {"label": "Quelle est l'année ?", "key": "année", "erreur": "année"},
        {"label": "Quel est le jour de la semaine ?", "key": "jour", "erreur": "jour"},
        {"label": "Dans quelle ville sommes-nous ?", "key": "ville", "erreur": "ville"},
        {"label": "Dans quel lieu ?", "key": "lieu", "erreur": "lieu"},
    ]

    for q in questions_orientation:
        col1, col2, col3 = st.columns([2, 1, 4])
        with col1:
            st.write(f"**{q['label']}**")
        with col2:
            vrai = st.checkbox("Vrai", key=f"{q['key']}_vrai")
        with col3:
            faux = st.checkbox("Faux", key=f"{q['key']}_faux")

    if vrai:
        score_orientation = score_orientation + 1
    elif faux:
        reponses_fausses_orientation.append(q["erreur"])

# ==== RESULTATS ====
with tab10:
    st.header("Résultat")

    score_total = score_nsc + score_visuospatial + score_denomination + score_memoire + score_attention + score_langage + score_abstraction + score_orientation

    if score_total >= 26:
        atteinte = "aucune atteinte"
    elif score_total >= 23:
        atteinte = "atteinte légère"
    elif score_total >= 18:
        atteinte = "atteinte modéré"
    elif score_total > 0:
        atteinte = "atteinte sévère"

    if nsc == "≤ 12 ans de scolarité":
        st.write(f"MoCA ({score_total}/30) {atteinte} (+1 point car niveau d'éducation ≤ 12 ans)")
    else:
        st.write(f"MoCA ({score_total}/30) {atteinte}")

    # Score équivalent pour le MMSE : 7/30

    if len(reponses_fausses_visuospatial) == 0:
        st.write(f"\- Visuo-spatial/exécutif ({score_visuospatial}/5)")
    else:
        st.write(
            f"\- Visuo-spatial/exécutif ({score_visuospatial}/5) : difficulté pour {', '.join(reponses_fausses_visuospatial)}")

    st.write(f"\- Dénomination ({score_denomination}/3)")

    if len(reponses_fausses_attention) == 0:
        st.write(f"\- Attention ({score_attention}/6)")
    else:
        st.write(f"\- Attention ({score_attention}/6) : difficulté pour {', '.join(reponses_fausses_attention)}")

    if len(reponses_fausses_langage) == 0:
        st.write(f"\- Langage ({score_langage}/3)")
    else:
        st.write(f"\- Langage ({score_langage}/3) : difficulté pour {', '.join(reponses_fausses_langage)}")

    st.write(f"\- Abstraction ({score_abstraction}/2)")

    if len(reponses_fausses_memoire) == 0:
        st.write(f"\- Mémoire ({score_memoire}/5)")
    else:
        st.write(f"\- Mémoire ({score_memoire}/5) : difficulté pour {', '.join(reponses_fausses_memoire)}")

    st.write(f"*Memory Index Score (MIS) : {memory_index_score}/15*")

    if len(reponses_fausses_orientation) == 0:
        st.write(f"\- Orientation temporo-spatiale ({score_orientation}/6)")
    else:
        st.write(
            f"\- Orientation temporo-spatiale ({score_orientation}/6) : difficulté pour {', '.join(reponses_fausses_orientation)}")