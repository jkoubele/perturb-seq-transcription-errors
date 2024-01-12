import pandas as pd
import GEOparse
from pathlib import Path

metadata_folder_path = Path("./metadata")

if __name__ == "__main__":
    sra_run_table = pd.read_csv(metadata_folder_path / 'SraRunTable.txt')

    gse_series = GEOparse.get_GEO(geo="GSE213511", destdir=metadata_folder_path / "GEOparse_data")
    gsm_samples = list(gse_series.gsms.values())

    geo_metadata_titles = {sample.name: sample.metadata['title'][0] for sample in gsm_samples}
    geo_metadata_source_names = {sample.name: sample.metadata['source_name_ch1'][0] for sample in gsm_samples}

    sra_run_table['sample_title'] = [geo_metadata_titles[gsm_id].split()[0] for gsm_id in
                                     sra_run_table['GEO_Accession (exp)']]
    sra_run_table['RNA_type'] = [geo_metadata_titles[gsm_id].split()[1] for gsm_id in
                                 sra_run_table['GEO_Accession (exp)']]
    sra_run_table['geo_metadata_source_name'] = [geo_metadata_source_names[gsm_id] for gsm_id in
                                                 sra_run_table['GEO_Accession (exp)']]
    sra_run_table.to_csv(metadata_folder_path / 'SRR_combined_metadata.csv')
