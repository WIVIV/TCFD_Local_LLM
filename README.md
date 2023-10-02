## TCFD Report Analysis Web Application using Retrieval Augmented Generation![image](https://github.com/WIVIV/TCFD_Local_LLM/assets/22553721/ac561917-0915-4ef6-9ed5-bacea21f8123)

![Example Image](./Assets/Images/llama_smart_5.jpeg)

### Summary
In this project, I conducted a geospatial analysis of the 2011 Queensland Flood to determine the extent of the flood and identify the properties impacted by this natural disaster. The analysis utilised the following datasets:
- [2011 Queensland Flood Extent](https://qldspatial.information.qld.gov.au/catalogue/custom/detail.page?fid={C3F4BC07-88B3-410C-904B-957933079AA8)
- [GNAF Core](https://geoscape.com.au/data/g-naf-core/)
- [Local government area boundaries - Queensland](https://qldspatial.information.qld.gov.au/catalogue/custom/detail.page?fid={3F3DBD69-647B-4833-B0A5-CC43D5E70699})
- [Cadastral data weekly - whole of State Queensland - GDA2020](https://qldspatial.information.qld.gov.au/catalogue/custom/detail.page?fid={FF9596F2-7387-4159-96AF-9ED6573ADD10})

### Background
The 2011 Queensland Flood was a devastating natural disaster that occurred in the state of Queensland, Australia. It was triggered by heavy rainfall associated with a monsoon trough and a tropical low-pressure system, resulting in widespread flooding across several regions. The flood, which lasted from late December 2010 to early 2011, caused significant damage to infrastructure, homes, and agricultural land.

### Methodology
To conduct the analysis, I utilised a combination of geospatial datasets. The 2011 flood extent shapefile provided information about the geographic extent of the flood. The GNAF Core dataset, which contains detailed geocoded addresses, enabled me to associate properties with their respective locations. The Queensland Cadastral dataset provided information on property boundaries, while the Local Government dataset contained administrative boundaries for LGAs.

By intersecting the flood extent shapefile with the cadastral dataset, I identified the properties within the flood-affected areas. Using the addresses from the GNAF Core dataset (joined on Land Parcel ID), I determined the LGAs, suburbs, and postcodes associated with these properties. This allowed me to quantify the impact of the flood at a per property level and identify the most affected areas.

### Findings
The 2011 Queensland Flood impacted a significant number of properties across multiple LGAs, postcodes and suburbs. 

#### Pie Chart of Impacted LGAs
![Example Image](./Assets/Images/count_by_lga_pie.png)

#### Impacted LGAs
![Example Image](./Assets/Images/count_by_lga_bar.png)

#### Impacted Postcodes
![Example Image](./Assets/Images/count_by_postcode_bar.png)

#### Impacted Suburbs
![Example Image](./Assets/Images/count_by_suburb_bar.png)

#### Impacted Properties in Postcode 4064
![Example Image](./Assets/Images/map_4064.png)


#### [Raw Data by LGA, Postcode and Suburb](./Assets/Excel/lga_postcode_suburb_counts.xlsx)

### Conclusion
By leveraging geospatial analysis and utilising diverse datasets, this project successfully assessed the impact of the 2011 Queensland Flood. The findings highlight the most affected LGAs, suburbs, and postcodes. This analysis can serve as a foundation for further studies on climate risk and inform decision-making processes aimed at reducing the impact of future floods in Queensland.


### Attribution
- © State of Queensland (Department of Resources) 2023. Updated data available at http://qldspatial.information.qld.gov.au/catalogue// .
- © PSMA Australia Limited trading as Geoscape Australia. ABN 23 089 912 710. Data available at https://geoscape.com.au/data/g-naf-core/ 
- OpenStreetMap® is open data, licensed under the Open Data Commons Open Database License (ODbL) by the OpenStreetMap Foundation (OSMF).
