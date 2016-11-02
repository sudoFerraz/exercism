

def to_rna(dna):
   rna = list(dna)
   for i in xrange(0, len(rna)):
       """a cada i checa qual o nucleotidio."""
       if str(rna[i]) == 'G':
           rna[i] = 'C'           
       elif str(rna[i]) == 'C':
           rna[i] = 'G'
       elif str(rna[i]) == 'T':
           rna[i] = 'A'
       elif str(rna[i]) == 'A':
           rna[i] = 'U'
   rna2 = ''.join(rna)
   return rna2
