# GnomAD-Gene-List-Scraper
A lightweight automated GnomAD gene information extraction from a list of genes using Python 3.8, Selenium, and Pandas. 

This is a lightweight compact GnomAD Gene scraper for a list of genes in CSV format. 
Website URL: (https://gnomad.broadinstitute.org/)

The script is written in Python 3.8

Python Packages used:
- Pandas
- Selenium
- csv
- time

SETUP INSTRUCTIONS AND RUNNING THE SCRIPT:

1) Download the script from Github - https://github.com/screadore/GnomAD-Gene-List-Scraper/

2) Check your version of Google Chrome -
  - Click on the Menu icon in the upper right corner of the screen.
  - Click on Help, and then About Google Chrome.
  - Your Chrome browser version number can be found here.

3) Download the version of Chromedriver that matches your browser version here - https://chromedriver.chromium.org/downloads

4) Place the chromedriver in a directory where you can easily access it because you'll need to get the path or absolute path to grant the script access to it. I recommend placing it in the same folder as this script to make things easier.

5) Take your list of genes and open a CSV file then copy and paste them into Column A in the vertical direction (downward).

6) Save the CSV file as a .csv (comma-deliminated file) and place it into the same folder as the script. (The folder name should be GnomAD_Gene_list_Data_Extraction)

7) Then create another CSV file .csv (comma-deliminated file) and name it output_gene_info.csv and keep it completely empty and save it to the GnomAD_Gene_list_Data_Extraction folder where the script is.

8) Now you want to open your CMD/Terminal. 

9) Create a virtual environment python -m venv /path/to/new/virtual/env.

10) Run the virtual environment.

11) pip install pandas

12) pip install selenium

13) Now you can run the script by typing Python run Gnom_AD_extract.py in your CMD/terminal and it will execute the script succesfully.

14) Your output data will be in the blank csv file you created named output_gene_info.csv.


Have fun and don't abuse the GnomAD website please this is for educational use only. I claim no rights or responsibility to any misuse of this script nor do I claim any ownership of GnomAD or it's websites database.

Author - Stefan G. Creadore
Lead Bioinformatics Scientist - Shriners Hospital for Children

If you need assistance message me on LinkedIN - https://www.linkedin.com/in/stefan-creadore/
