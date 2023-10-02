## TCFD Report Analysis using a Local Large Language Model (LLM) and Retrieval Augmented Generation (RAG)

![Example Image](./Assets/Images/llama_smart_5.jpeg)

### Summary
For this project I built a StreamLit web application to automate TCFD (Task Force on Climate-related Financial Disclosures) Report Analysis. I used [Meta's Llama2 model](https://ai.meta.com/llama/) and RAG to analyse the TCFD reports through answering a set of 11 predefined questions. The app also displays the source text from the TCFD report (including the page number) that was passed to the LLM to answer each of the questions, thereby increasing the level of confidence in the veracity of the answers.

### TCFD Overview
The Task Force on Climate-related Financial Disclosures (TCFD) provides a framework to help companies disclose climate-related information to their stakeholders. TCFD reports are pivotal tools that allow organizations to transparently convey their climate-related risks, opportunities, and strategies to stakeholders. Analyzing these reports helps in comprehending a company's climate impact, sustainability efforts, and overall readiness to navigate the challenges posed by climate change.

### RAG
![Example Image](./Assets/Images/RAG.png)
Retrieval Augmented Generation (RAG) is an framework for improving the quality of LLM generated responses by grounding the LLM in a private knowledge base (Embedding Model and Vectore DB in the diagram above). Two main advatedges of RAG are:
1. Users can ingest the most authoritative and current source documents to deliver better factual consistency and improve the reliability of the generated responses.
2. Users have access to the model's sources (Retreival QA Chain in the diagram above), ensuring that the LLM responses can be checked for accuracy against the source documnets.

### Methodology
To conduct the analysis, I utilised a combination of geospatial datasets. The 2011 flood extent shapefile provided information about the geographic extent of the flood. The GNAF Core dataset, which contains detailed geocoded addresses, enabled me to associate properties with their respective locations. The Queensland Cadastral dataset provided information on property boundaries, while the Local Government dataset contained administrative boundaries for LGAs.

By intersecting the flood extent shapefile with the cadastral dataset, I identified the properties within the flood-affected areas. Using the addresses from the GNAF Core dataset (joined on Land Parcel ID), I determined the LGAs, suburbs, and postcodes associated with these properties. This allowed me to quantify the impact of the flood at a per property level and identify the most affected areas.

### Example
To test the application I used AGL's FY23 TCFD Report

[<img width="200px" src="./Assets/Images/AGL_TCFD_Report.png" />](https://www.agl.com.au/content/dam/digital/agl/documents/about-agl/investors/2023/230810-agl-energy-tcfd-report-2023-5-5.pdf])

#### TCFD Web App - UI
![Example Image](./Assets/Images/TCFD_Demo_1.png)

#### TCFD Web App - 11 Questions
![Example Image](./Assets/Images/TCFD_Demo_11_Questions.png)

#### TCFD Web App - Question 1: Answers and Source Text Used
![Example Image](./Assets/Images/TCFD_Demo_Q1_sources.png)

#### TCFD Web App - Question 2: Answers and Source Text Used
![Example Image](./Assets/Images/TCFD_Demo_Q2_sources.png)

#### TCFD Web App - Custom Questions
![Example Image](./Assets/Images/TCFD_Demo_Custom_Questions.png)

### Conclusion
By leveraging geospatial analysis and utilising diverse datasets, this project successfully assessed the impact of the 2011 Queensland Flood. The findings highlight the most affected LGAs, suburbs, and postcodes. This analysis can serve as a foundation for further studies on climate risk and inform decision-making processes aimed at reducing the impact of future floods in Queensland.

### Attribution
- © State of Queensland (Department of Resources) 2023. Updated data available at http://qldspatial.information.qld.gov.au/catalogue// .
- © PSMA Australia Limited trading as Geoscape Australia. ABN 23 089 912 710. Data available at https://geoscape.com.au/data/g-naf-core/ 
- OpenStreetMap® is open data, licensed under the Open Data Commons Open Database License (ODbL) by the OpenStreetMap Foundation (OSMF).
