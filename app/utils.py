from scipy.stats import f_oneway, kruskal

def run_anova(Data_merged, metric="GHI"):
    groups = [Data_merged[Data_merged["country"] == c][metric] for c in Data_merged["country"].unique()]
    return f_oneway(*groups)

def run_kruskal(Data_merged, metric="GHI"):
    groups = [Data_merged[Data_merged["country"] == c][metric] for c in Data_merged["country"].unique()]
    return kruskal(*groups)
