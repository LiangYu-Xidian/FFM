import time
import pandas as pd
from selenium import webdriver


driver = webdriver.Chrome("D:/driver/chromedriver.exe")

for j in range(17):
    print(str(j+2) + "----------------------------------------------------------------------------------")
    file_in = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\\all_target_' + str(j+2) + '.csv')
    # file_in = file_in.head(5)
    SMILES = []
    CID = []

    for i in range(file_in.shape[0]):
        print(i)
        url = "https://pubchem.ncbi.nlm.nih.gov/#query=" + str(file_in.iloc[i][0]) + " human&tab=gene&input_type=text"
        # url = "https://pubchem.ncbi.nlm.nih.gov/#query=Ephrin receptor human&tab=gene&input_type=text"
        driver.get(url)
        time.sleep(10)

        try:
            elem = driver.find_element_by_xpath('//*[@id="collection-results-container"]/div/div/div[2]/ul/li[1]/div/div/div/div/div[2]/div[1]/span/a/span/span')
            id = driver.find_element_by_xpath('//*[@id="collection-results-container"]/div/div/div[2]/ul/li[1]/div/div/div/div/div[2]/div[1]/span/span')
        except:
            smile = "NULL"
            # cid = "null"
        else:
            try:
                smile = elem.text
                name = id.text
                if name != "Gene ID:":
                    smile = "NULL"
                print(name)
            except:
                smile = "NULL"
                # cid = "null"
        finally:
            SMILES.append(smile)
            print(smile)
            # CID.append(cid)

        
    file_in["SMILES"] = SMILES
    # file_in["CID"] = CID
    file_in.to_csv('D:\TASK3\Data\CancerDC\DrugComb\\all_target_new' + str(j+2) + '.csv')
    

