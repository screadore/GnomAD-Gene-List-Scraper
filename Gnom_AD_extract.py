# This is a GnomAd Gene list data scraper aka data extraction.
# Just do pip install selenium and add your csv file with the name of "genes.csv" then you can run the script.

import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

print('Your script is now initializing the run time is typically 10-60 minutes until the data scraping is completed.')
print('Author of the script - Stefan G. Creadore')

driver = webdriver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(5)  # gives an implicit wait for 20 seconds needed for it to not give an error

df = pd.DataFrame(columns=['gene_symbol', 'ensembl_symbol', 'chromosome_number'])
# ---------------------------------------------------------------------------------

# This opens the CSV file we want to use that contains our Genes list. Make sure the list is in column A going in the vertical direction down.

# ---------------------------------------------------------------------------------
with open('genes.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)
# ---------------------------------------------------------------------------------


# We loop for each line in our csv file for the genes we want to search for.

# ---------------------------------------------------------------------------------

    driver.get('https://gnomad.broadinstitute.org/gene/ENSG00000197386?dataset=gnomad_r2_1')
    time.sleep(10)

    for line in csv_reader:


        gnomad_data = []
        # ----------------------------------------------------------------------------

        # Input of gene into top search bar on GnomAD.

        # ----------------------------------------------------------------------------
        search_bar = driver.find_element_by_xpath('//*[@id="navbar-search"]')
        search_bar.click()
        time.sleep(5)
        search_bar.send_keys(line[0])
        time.sleep(2)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)

        # ----------------------------------------------------------------------------

        # Start of Scraping the GnomAD page data.

        # ----------------------------------------------------------------------------

        genes_id = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/section/div[1]/div[1]")

        gnomad_data = []

        for id in genes_id:
            gnomad_data.append(id.get_attribute('id'))

        for data in gnomad_data:
            gene_symbol_element = driver.find_element_by_xpath('/html/body/div[1]/div[3]/section/div[1]/div[1]')
            gene_symbol = gene_symbol_element.text
            print(gene_symbol)



            ensembl_symbol_element = driver.find_element_by_xpath('/html/body/div[1]/div[3]/section/div[2]/dl/div[2]/dd')
            ensembl_symbol = ensembl_symbol_element.text
            print(ensembl_symbol)


            chromosome_number_element = driver.find_element_by_xpath('/html/body/div[1]/div[3]/section/div[2]/dl/div[5]/dd/a')
            chromosome_number = chromosome_number_element.text
            print(chromosome_number)

        # ------------------------------------------------------------------------------

        # End of Scraping GnomAD page data.

        # ------------------------------------------------------------------------------

            df2 = pd.DataFrame([[gene_symbol,ensembl_symbol,chromosome_number]],columns=['gene_symbol','ensembl_symbol','chromosome_number'])
            df = df.append(df2,ignore_index=True)
            df.to_csv('output_gene_info.csv', encoding='utf-8')
            print(df)

print('Your genes have been queried')
print('Author - Stefan G. Creadore - Bioinformatics Scientist')
print('You can reach me via LinkedIN - https://www.linkedin.com/in/stefan-creadore/')
