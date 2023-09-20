use Rfam;

##How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger? (hint: use the biological name of the tiger)

select count(distinct species) as tiger_count
from taxonomy where species like '%Tiger%';

select ncbi_id,species from taxonomy where species = 'Panthera tigris sumatrae';

## Which type of rice has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables)

select ncbi_id,description,max(length) from rfamseq group by description limit 1;

##We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)

select rfamseq_acc, accession,mol_type, length, description from rfamseq where length > 1000000
order by length desc limit 15 offset 120; 

