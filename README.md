## TCFD Report Analysis using a Local Large Language Model (LLM) and Retrieval Augmented Generation (RAG)

![Example Image](./Assets/Images/llama_smart_5.jpeg  "Imagine a futuristic scene set in the year 2050, where a llama, outfitted with sleek and advanced smart goggles, stands confidently with lots of document pages and charts behind him. The goggles display complex holographic data visualizations, projecting intricate patterns and graphs in the air around the llama. The llama exudes an air of intelligence and sophistication, blending seamlessly with the technologically advanced world it inhabits. Capture the essence of this futuristic llama and its technologically enhanced appearance in your vivid artwork.")
<sup>Hover over image to see prompt used to generate it.</sup> 

### Summary
For this project I wanted to explore running an LLM locally to analyse a set of locally hosted documents and answer a series of questions. This implementation allows one to use sophisticated AI models privately, without having to use APIs or send data outside your local network. To ground it a practical use case, I built a Streamlit web app to automate analysis of TCFD (Task Force on Climate-related Financial Disclosures) Reports. I used [Meta's Llama2 model](https://ai.meta.com/llama/) and RAG to analyse the TCFD reports through answering a set of 11 predefined questions. The app also displays the source text from the TCFD report (including the page number) that was passed to the LLM to answer each of the questions, thereby increasing the level of confidence in the accuracy of the answers.

### TCFD
The TCFD provides a framework to help companies disclose climate-related information to their stakeholders. TCFD reports are pivotal tools that allow organizations to transparently convey their climate-related risks, opportunities, and strategies to stakeholders. Analysing these reports helps in comprehending a company's climate impact, sustainability efforts, and overall readiness to navigate the challenges posed by climate change.

### RAG
![Example Image](./Assets/Images/RAG.png)
RAG is a framework for improving the quality of LLM generated responses by grounding the LLM in a private knowledge base (Embedding Model and Vector DB in the diagram above). Two of the main advantages of RAG are:
1. Users can ingest the most authoritative and current source documents to deliver better factual consistency and improve the reliability of the generated responses.
2. Users have access to the model's sources (Retrieval QA Chain in the diagram above), ensuring that the LLM responses can be checked for accuracy against the source documents.

## TCFD Report Analysis Questions
In order to determine the questions used to analyse the reports I utilised the [TCFD’s disclosure recommendations](https://assets.bbhub.io/company/sites/60/2020/10/FINAL-2017-TCFD-Report-11052018.pdf) (across the four topics of governance, strategy, risk management, and metrics and targets) which were summarised in this [Deloitte article](https://www2.deloitte.com/ch/en/pages/risk/articles/tcfd-and-why-does-it-matter.html) into the following 11 items:
![image](https://github.com/WIVIV/TCFD_Local_LLM/assets/22553721/eb349ad1-97b5-4f42-86b1-f84882d23efd)

### Testing the App on AGL's FY23 TCFD Report
To practially test the app I used AGL's FY23 TCFD Report. [AGL is Australia's largest Scope 1 emitter](https://www.cleanenergyregulator.gov.au/NGER/National%20greenhouse%20and%20energy%20reporting%20data/Data-highlights/2021-22-published-data-highlights) (Scope 1 greenhouse gas emissions are the emissions released to the atmosphere as a direct result of an activity).

[<img width="200px" src="./Assets/Images/AGL_TCFD_Report.png" />](https://www.agl.com.au/content/dam/digital/agl/documents/about-agl/investors/2023/230810-agl-energy-tcfd-report-2023-5-5.pdf])

#### TCFD Web App - Responses to the first two questions (Users upload the pdf of the TCFD Report then hit the "Generate TCFD Responses" button.
![Example Image](./Assets/Images/TCFD_Demo_1.png)

#### TCFD Web App - Question 1: Answers and Source Text Used
![Example Image](./Assets/Images/TCFD_Demo_Q1_sources.png)

#### TCFD Web App - Question 2: Answers and Source Text Used
![Example Image](./Assets/Images/TCFD_Demo_Q2_sources.png)

#### TCFD Web App - Users Also Have the Ability to Ask Custom Questions
![Example Image](./Assets/Images/TCFD_Demo_Custom_Questions.png)

### Conclusion
By leveraging a local LLM and RAG, this project successfully analysed AGL's TCFD report by answering 11 preset questions. The quality of the repsonses and the quoting of the sources used, clearly demostrates the utility and effiecincy gain that this implementation of LLMs provides. 

#### Key Libraries and Resources Used:
- [LangChain🦜️🔗](https://www.langchain.com/)
- [Meta - Llama2](https://huggingface.co/meta-llama)
- [Streamlit](https://streamlit.io/)
- [HuggingFace🤗](https://huggingface.co/)
- [TheBloke - HuggingFace](https://huggingface.co/TheBloke)


