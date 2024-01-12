# perturb-seq-transcription-errors

- The perturb-seq data are from the GEO
  series [GSE213511](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE213511).

- The perturb-seq annotation
  metadata ([GSE213511_CellAnnotation_exvivo.tsv](metadata/GSE213511_CellAnnotation_exvivo.tsv),
  [GSE213511_CellAnnotation_invivo.tsv](metadata/GSE213511_CellAnnotation_invivo.tsv)
  and [GSE213511_CellAnnotation_leukemia.tsv](metadata/GSE213511_CellAnnotation_leukemia.tsv) were downloaded from the
  [GSE213511](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE213511) site. The files with runs
  info [SraRunTable.txt](metadata/SraRunTable.txt) and [SRR_Acc_List.txt](metadata/SRR_Acc_List.txt) were
  obtained from the [SRA Run Selector](https://www.ncbi.nlm.nih.gov/Traces/study/?acc=PRJNA881278&o=acc_s%3Aa).
- The metadata in [SRR_Acc_List.txt](metadata/SRR_Acc_List.txt) are enhanced by GEO metadata obtained via GEOparse
  package (a wrapper around eutils).This is done by a script
  [combine_metadata.py](combine_metadata.py), and the result is saved to
  file [SRR_combined_metadata.csv](metadata/SRR_combined_metadata.csv). 