rule download_data:
    output:
        biggm="bigg_models_metabolites.txt"
    shell:
        """
        wget http://bigg.ucsd.edu/static/namespace/bigg_models_metabolites.txt
        """

rule bigg_metabolite:
    input:
        bmm=rules.download_data.output.biggm
    output:
        tsv="bigg.metabolite.tsv"
    script: "bigg.metabolite/bigg.metabolite.py"

rule all:
    input:
        rules.bigg_metabolite.output
