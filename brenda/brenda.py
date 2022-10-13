import json

brenda=json.load(open("brenda_2022_2.json"))

data = brenda['data']
ecnumbers = data.keys()

f = open('brenda.tsv', 'w')
f.write('identifiersorgprefix1\tid1\tidentifiersorgprefix2\tid2\n')
for ecnumber in ecnumbers:
    if ecnumber != 'spontaneous':
        if 'proteins' in data[ecnumber]:
            proteins = data[ecnumber]['proteins']
            for protein in proteins.values():
                # if len(protein) > 1:
                #     print(protein)
                # print(protein[0])
                for accession in protein[0]['accessions']:
                    # if protein[0]['source'] != 'uniprot':
                    #     print(accession)
                    #     print(protein[0]['source'])
                    # print('brenda,' + ecnumber + ',' + protein[0]['source'] + ',' + accession)
                    f.write('brenda\t' + ecnumber + '\t' + protein[0]['source'] + '\t' + accession + '\n')
f.close()
