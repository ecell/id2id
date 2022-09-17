import pybiopax
model = pybiopax.model_from_owl_file('biopax-level3.owl')
objs = model.objects

f = open('a.tsv', 'w')
for key in objs:
    if hasattr(objs[key], 'xref'):
        if len(objs[key].xref) > 0:
            if type(objs[key].xref[0]) != str:
                #print(objs[key].xref[0])
                theid = objs[key].xref[0].id
                if hasattr(objs[key], 'entity_reference'):
                    eref = objs[key].entity_reference
                    if hasattr(eref, 'xref'):
                        xrefs = eref.xref
                        for xref in xrefs:
                            tmp = []
                            tmp.append(theid)
                            # print("ECOCYC ID: " + theid)
                            if hasattr(xref, 'id'):
                                if type(xref.id) == str:
                                    tmp.append(xref.id)
                                    # print("XREF ID: " + xref.id)
                            if hasattr(xref, 'db'):
                                if type(xref.db) == str:
                                    tmp.append(xref.db)
                                    # print("XREF DB: " + xref.db)
                            f.write('\t'.join(tmp) + '\n')
                            # print(",".join(tmp))
f.close()
