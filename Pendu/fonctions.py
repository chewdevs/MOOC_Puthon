
def import_score(fichier_scores):
    with open('fichier_scores', 'rb') as fichier:
        pickler = pickle.Unpickler(fichier)
        scores_recup = pickler.load()
    return scores_recup


# def sauve_score():
#
# def affiche_score():
