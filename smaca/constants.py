# coding: utf-8
"""
author: Daniel López
email: daniel.lopez.lopez@juntadeandalucia.es

author: Carlos Loucera
email: carlos.loucera@juntadeandalucia.es

SMA carrier Test samtools constants file. Genomic ranges are 0-based, stop-excluded
"""

REF_HG19 = "hg19"
REF_HG38 = "hg38"

HEADER_FILE = \
 "id|" \
 "Pi_a|" \
 "Pi_b|" \
 "Pi_c|" \
 "cov_SMN1_a|" \
 "cov_SMN1_b|" \
 "cov_SMN1_c|" \
 "cov_SMN2_a|" \
 "cov_SMN2_b|" \
 "cov_SMN2_c|" \
 "avg_cov_SMN1|" \
 "avg_cov_SMN2|" \
 "scale_factor|" \
 "std_control|" \
 "g.27134T>G|" \
 "g.27706_27707delAT|" \
 "avg_cov_CYP11B1|" \
 "avg_cov_IQCB1|" \
 

POSITIONS = {
    REF_HG19: {
        "SMN": {
            "SMN1": [5, 70220767, 70249769],
            "SMN2": [5, 69345349, 69374349]
        },
        "GENES": {
             "CYP11B1": [8, 142872353, 142879846],
            "IQCB1": [3, 121769760, 121835079]
        },
        "SMN1_POS": {
            "SMN1_a": [5, 70247723, 70247724],
            "SMN1_b_e7": [5, 70247772, 70247773],
            "SMN1_c": [5, 70247920, 70247921]
        },
        "SMN2_POS": {
            "SMN2_a": [5, 69372303, 69372304],
            "SMN2_b_e7": [5, 69372352, 69372353],
            "SMN2_c": [5, 69372500, 69372501]
        },
        "DUP_MARK": {
            "g.27134T>G": [5, 70247900, 70247901],
            "g.27706_27707delAT": [5, 70248472, 70248474]
        }
    },
    REF_HG38: {
        "SMN": {
            "SMN1": [5, 70924940, 70953942],
            "SMN2": [5, 70049523, 70078522]
        },
        "GENES": {
            "CYP11B1": [8, 142872353, 142879846],
            "IQCB1": [3, 121769760, 121835079]
        },
        "SMN1_POS": {
            "SMN1_a": [5, 70951895, 70951897],
            "SMN1_b_e7": [5, 70951944, 70951946],
            "SMN1_c": [5, 70952092, 70952094]
        },
        "SMN2_POS": {
            "SMN2_a": [5, 70076475, 70076477],
            "SMN2_b_e7": [5, 70076524, 70076526],
            "SMN2_c": [5, 70076672, 70076674]
        },
        "DUP_MARK": {
            "g.27134T>G": [5, 70952072, 70952074],
            "g.27706_27707delAT": [5, 70952644, 70952647]
        }
    }
}
