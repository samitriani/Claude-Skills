#!/usr/bin/env python3
"""Contrôles de cohérence du diagnostic financier en 8 étapes (SKILL.md).

Usage :
    python verifier_coherence.py donnees-financieres.json

Sans dépendance externe (bibliothèque standard uniquement) — aucun
`pip install` requis pour utiliser ce skill.

Lit un fichier JSON structuré par exercice (voir
scripts/donnees-financieres.exemple.json) et exécute les identités
comptables C1 à C6 de SKILL.md, plus un test de plausibilité sectorielle.
Sort un tableau PASS / FAIL / WARN / N.A. par exercice et retourne un
code de sortie non nul si un contrôle échoue ou si trop de contrôles
sont inexécutables faute de données.

Un statut N.A. n'est pas un feu vert : si trop de contrôles ne peuvent
pas s'exécuter, c'est un signal pour escalader vers la source primaire
(§0.5 de SKILL.md) avant de rédiger la restitution, pas une excuse pour
avancer sans eux.
"""

import json
import sys

# Les consoles Windows (cp1252) plantent sur certains caractères Unicode
# (signe moins mathématique, ≥, etc.) sans ce garde-fou.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except AttributeError:
        pass  # Python < 3.7, ignorer : cas non supporté par ce script

TOLERANCE_C1 = 0.05     # actif économique vs capitaux employés : 5 %
TOLERANCE_C2 = 0.01     # réconciliation du bilan : 1 %
TOLERANCE_C3 = 0.02     # EBITDA - D&A vs EBIT : 2 %
TOLERANCE_C4_PTS = 0.5  # ROE recalculé vs publié : 0,5 point
IS_MIN, IS_MAX = 0.10, 0.40  # fourchette usuelle du taux d'IS effectif en France
SEUIL_NA = 0.5           # au-delà de 50 % de contrôles N.A., on bloque


def valeur(champ):
    """Un champ peut être un nombre brut ou {"valeur": ..., "statut": ..., "source": ...}."""
    if champ is None:
        return None, None
    if isinstance(champ, dict):
        return champ.get("valeur"), champ.get("statut", "non-precise")
    return champ, "non-structure"


def get(ex, nom):
    return valeur(ex.get(nom))


def check_c1(ex):
    bfr, _ = get(ex, "bfr_total")
    immo, _ = get(ex, "immobilisations_nettes")
    cp, _ = get(ex, "capitaux_propres")
    prov, _ = get(ex, "provisions")
    dette, _ = get(ex, "dette_financiere")
    tresorerie, _ = get(ex, "tresorerie")
    prov = prov or 0
    if None in (bfr, immo, cp, dette, tresorerie):
        return "N.A.", "bfr_total, immobilisations_nettes, capitaux_propres, dette_financiere ou tresorerie manquant(s)"
    actif_eco = bfr + immo
    capitaux_employes = cp + prov + (dette - tresorerie)
    base = max(abs(actif_eco), abs(capitaux_employes), 1)
    ecart = abs(actif_eco - capitaux_employes) / base
    msg = f"Actif éco (BFR+immo) = {actif_eco:,.0f} | Capitaux employés (CP+dette nette) = {capitaux_employes:,.0f} | écart = {ecart:.1%}"
    return ("PASS" if ecart <= TOLERANCE_C1 else "FAIL"), msg


def check_c2(ex):
    cp, _ = get(ex, "capitaux_propres")
    prov, _ = get(ex, "provisions")
    total_dettes, _ = get(ex, "total_dettes")
    total_bilan, _ = get(ex, "total_bilan")
    prov = prov or 0
    if None in (cp, total_dettes, total_bilan) or total_bilan == 0:
        return "N.A.", "capitaux_propres, total_dettes ou total_bilan manquant(s)"
    reconstitue = cp + prov + total_dettes
    ecart = abs(reconstitue - total_bilan) / abs(total_bilan)
    msg = f"CP+provisions+dettes = {reconstitue:,.0f} | Total bilan déclaré = {total_bilan:,.0f} | écart = {ecart:.1%}"
    return ("PASS" if ecart <= TOLERANCE_C2 else "FAIL"), msg


def check_c3(ex):
    ebitda, _ = get(ex, "ebitda")
    dot, _ = get(ex, "dotations_amortissements")
    ebit, _ = get(ex, "ebit")
    if None in (ebitda, dot, ebit):
        return "N.A.", "ebitda, dotations_amortissements ou ebit manquant(s)"
    ebit_recalcule = ebitda - dot
    base = max(abs(ebit), 1)
    ecart = abs(ebit_recalcule - ebit) / base
    msg = f"EBITDA - D&A = {ebit_recalcule:,.0f} | EBIT déclaré = {ebit:,.0f} | écart = {ecart:.1%}"
    return ("PASS" if ecart <= TOLERANCE_C3 else "FAIL"), msg


def check_c4(ex):
    rn, _ = get(ex, "resultat_net")
    cp, _ = get(ex, "capitaux_propres")
    roe_publie, _ = get(ex, "roe_publie")
    if None in (rn, cp, roe_publie) or cp == 0:
        return "N.A.", "resultat_net, capitaux_propres ou roe_publie manquant(s)"
    roe_calcule = rn / cp
    ecart_pts = abs(roe_calcule - roe_publie) * 100
    msg = f"ROE recalculé = {roe_calcule:.1%} | ROE publié = {roe_publie:.1%} | écart = {ecart_pts:.2f} pt"
    return ("PASS" if ecart_pts <= TOLERANCE_C4_PTS else "FAIL"), msg


def check_c5(ex):
    dette, _ = get(ex, "dette_financiere")
    charges_fin, _ = get(ex, "charges_financieres")
    ebit, _ = get(ex, "ebit")
    if dette is None:
        return "N.A.", "dette_financiere manquant"
    if charges_fin is None:
        return "N.A.", "charges_financieres manquant — ne peut pas confirmer la cohérence avec la dette déclarée"
    if dette == 0 and ebit:
        seuil = 0.02 * abs(ebit)
        if charges_fin > seuil:
            return "WARN", (f"Dette financière déclarée = 0 mais charges financières = {charges_fin:,.0f} "
                             f"(> 2 % de l'EBIT) — une dette financière a peut-être été omise ou mal classée")
    if dette > 0:
        if charges_fin == 0:
            return "WARN", "Dette financière > 0 mais charges financières nulles — à confirmer (prêt intragroupe à taux zéro possible, mais à vérifier, pas à supposer)"
        taux_implicite = charges_fin / dette
        if taux_implicite < 0.005:
            return "FAIL", (f"Taux d'intérêt implicite = {taux_implicite:.2%} (charges financières {charges_fin:,.0f} "
                             f"/ dette {dette:,.0f}) — implausible pour une dette financière réelle. "
                             f"Le montant déclaré en dette_financiere est probablement une autre ligne du bilan "
                             f"mal classée (voir le piège TOTAL DETTES, §0.2 de SKILL.md)")
        if taux_implicite > 0.15:
            return "WARN", f"Taux d'intérêt implicite = {taux_implicite:.2%} — inhabituellement élevé, à vérifier"
    return "PASS", f"Dette financière = {dette:,.0f} | Charges financières = {charges_fin:,.0f} — cohérent"


def check_c6(ex):
    impot, _ = get(ex, "impot")
    rcai, _ = get(ex, "resultat_avant_impot")
    if None in (impot, rcai) or rcai == 0:
        return "N.A.", "impot ou resultat_avant_impot manquant"
    taux = impot / rcai
    msg = f"Taux d'IS effectif = {taux:.1%}"
    if taux < 0:
        return "WARN", msg + " (négatif — crédit d'impôt net constaté, à documenter)"
    if IS_MIN <= taux <= IS_MAX:
        return "PASS", msg
    return "WARN", msg + f" (hors fourchette usuelle {IS_MIN:.0%}-{IS_MAX:.0%} — à expliquer : CIR, intégration fiscale, déficits reportables ?)"


def check_plausibilite_masse_salariale(ex):
    ca, _ = get(ex, "ca")
    masse, _ = get(ex, "masse_salariale")
    dettes_fs, _ = get(ex, "dettes_fiscales_sociales")
    if None in (ca, masse, dettes_fs) or not ca:
        return "N.A.", "ca, masse_salariale ou dettes_fiscales_sociales manquant(s)"
    ratio_masse = masse / ca
    seuil_min = masse / 12  # a minima l'équivalent d'un mois de charges dues
    msg = f"Masse salariale/CA = {ratio_masse:.1%} | Dettes fiscales et sociales = {dettes_fs:,.0f} (attendu ≥ {seuil_min:,.0f})"
    if ratio_masse > 0.30 and dettes_fs < seuil_min:
        return "FAIL", msg + " — activité à forte masse salariale mais dettes sociales quasi nulles : la ventilation du passif est probablement fausse (voir le piège TOTAL DETTES, §0.2 de SKILL.md)"
    return "PASS", msg


CHECKS = [
    ("C1", "Actif économique = Capitaux employés", check_c1),
    ("C2", "CP + provisions + dettes = Total bilan", check_c2),
    ("C3", "EBITDA - D&A = EBIT", check_c3),
    ("C4", "ROE recalculé = ROE publié", check_c4),
    ("C5", "Cohérence dette financière / charges financières", check_c5),
    ("C6", "Taux d'IS effectif plausible", check_c6),
    ("PLAUS.", "Masse salariale vs dettes fiscales et sociales", check_plausibilite_masse_salariale),
]


def run(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    exercices = data.get("exercices", {})
    if not exercices:
        print('Aucun exercice trouvé (clé "exercices" attendue dans le JSON).')
        return 2

    entreprise = data.get("entreprise", "(nom non renseigné)")
    print(f"Contrôles de cohérence — {entreprise}")

    has_fail = False
    total_na = 0
    total_applicables = 0

    for annee in sorted(exercices.keys(), reverse=True):
        ex = exercices[annee]
        print(f"\n=== Exercice {annee} ===")
        for code, titre, fn in CHECKS:
            statut, msg = fn(ex)
            print(f"[{statut:6}] {code} — {titre}")
            print(f"         {msg}")
            if statut == "FAIL":
                has_fail = True
            if statut == "N.A.":
                total_na += 1
            else:
                total_applicables += 1

    total_checks = total_na + total_applicables
    ratio_na = (total_na / total_checks) if total_checks else 1.0

    print(f"\n{'=' * 70}")
    print(f"Contrôles exécutables : {total_applicables}/{total_checks} ({1 - ratio_na:.0%})")

    blocking = False
    if has_fail:
        print("ÉCHEC — au moins un contrôle a échoué.")
        print("Ne pas documenter l'écart dans le rapport : escalader vers la source primaire (§0.5) et corriger la donnée.")
        blocking = True
    if ratio_na > SEUIL_NA:
        print(f"ATTENTION — plus de {SEUIL_NA:.0%} des contrôles n'ont pas pu s'exécuter faute de données.")
        print("Ce n'est pas un feu vert : compléter donnees-financieres.json avant de rédiger la restitution.")
        blocking = True
    if not blocking:
        print("Tous les contrôles exécutables sont au vert.")

    return 1 if blocking else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python verifier_coherence.py <fichier-donnees.json>")
        sys.exit(2)
    sys.exit(run(sys.argv[1]))
