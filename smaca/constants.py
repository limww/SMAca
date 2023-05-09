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
 "avg_cov_DBT_0\t" \
 "avg_cov_SLC26A2_2\t" \
 "avg_cov_MCPH1_13\t" \
 "avg_cov_FKTN_10\t" \
 "avg_cov_COL4A4_0\t" \
 "avg_cov_RAD50_24\t" \
 "avg_cov_MMAA_6\t" \
 "avg_cov_ATM_62\t" \
 "avg_cov_MMACHC_3\t" \
 "avg_cov_ARSB_0\t" \
 "avg_cov_EARS2_0\t" \
 "avg_cov_FRAS1_73\t" \
 "avg_cov_PKHD1_0\t" \
 "avg_cov_CYP7B1_0\t" \
 "avg_cov_TMEM237_0\t" \
 "avg_cov_KIAA0586_30\t" \
 "avg_cov_AMACR_0\t" \
 "avg_cov_LINS1_0\t" \
 "avg_cov_RPGRIP1L_0\t" \
 "avg_cov_MMAB_0\t"  
 

POSITIONS = {
    REF_HG19: {
        "SMN": {
            "SMN1": [5, 70220767, 70249769],
            "SMN2": [5, 69345349, 69374349]
        },
        "GENES": {
             "CYP11B1": [8, 143953771, 143961262],
            "IQCB1": [3, 121488609, 121553926]
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
            "DBT_0": [1, 100186908, 100196432], 
            "SLC26A2_2": [5, 149980282, 149987410], 
            "MCPH1_13": [8, 6642983, 6648518], 
            "FKTN_10": [9, 105635040, 105641128], 
            "COL4A4_0": [2, 227002705, 227007598], 
            "RAD50_24": [5, 132642167, 132646357], 
            "MMAA_6": [4, 145655136, 145660043], 
            "ATM_62": [11, 108365314, 108369112], 
            "MMACHC_3": [1, 45508785, 45513392], 
            "ARSB_0": [5, 78777200, 78780672], 
            "EARS2_0": [16, 23520743, 23524464], 
            "FRAS1_73": [4, 78540520, 78544279], 
            "PKHD1_0": [6, 51615288, 51619530], 
            "CYP7B1_0": [8, 64590840, 64596939], 
            "TMEM237_0": [2, 201620175, 201624332], 
            "KIAA0586_30": [14, 58547770, 58551307], 
            "AMACR_0": [5, 33986154, 33989512], 
            "LINS1_0": [15, 100566913, 100570127], 
            "RPGRIP1L_0": [16, 53598142, 53602198], 
            "MMAB_0": [12, 109553705, 109557146]
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
