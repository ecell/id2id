import json

brenda=json.load(open("brenda_2022_2.json"))

data = brenda['data']
ecnumbers = data.keys()

f = open('brenda.csv', 'w')
f.write('identifiersorgprefix1,id1,identifiersorgprefix2,id2\n')
for ecnumber in ecnumbers:
    if ecnumber != 'spontaneous':
        if 'proteins' in b[ecnumber]:
            proteins = b[ecnumber]['proteins']
            for protein in proteins.values():
                # if len(protein) > 1:
                #     print(protein)
                # print(protein[0])
                for accession in protein[0]['accessions']:
                    # if protein[0]['source'] != 'uniprot':
                    #     print(accession)
                    #     print(protein[0]['source'])
                    # print('brenda,' + ecnumber + ',' + protein[0]['source'] + ',' + accession)
                    f.write('brenda,' + ecnumber + ',' + protein[0]['source'] + ',' + accession + '\n')
f.close()
