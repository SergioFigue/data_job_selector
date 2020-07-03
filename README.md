# Data Job Selector (DJS)
---

##Overview
**Data Job Selector** is a simple tool created to **help people looking for a job in the blooming field of data**. By introducing a country and a job title, user will find out whether or not is entering a busy market.

##How it works

Starting with a stratified sample of annonimized survey respondents from different countries around Europe, Data Job Selector strip down raw data for the user to show a clean, easy to read report about said countries labour market. It operates in two steps: first, DJS filters by the job title selected by the user; second, DJS filters by country if the user selects this option or return a comprehensive list, including quantity of professional workers in the sample and the proportion of this kind of job out of the total employed respondants. 

###Running DJS

*For a right use of the program, please do not forget to download the main database [here](http://www.potacho.com/files/ironhack/raw_data_project_m1.db)*

Select one of the participant countries from the list:

* 'Austria'
* 'Belgium'
* 'Bulgaria'
* 'Cyprus'
* 'Czechia'
* 'Germany'
* 'Denmark'
* 'Estonia'
* 'Spain'
* 'Finland'
* 'France'
* 'United Kingdom'
* 'Greece'
* 'Croatia'
* 'Hungary'
* 'Ireland'
* 'Italy'
* 'Lithuania'
* 'Luxembourg'
* 'Latvia'
* 'Malta'
* 'Netherlands'
* 'Poland'
* 'Portugal'
* 'Romania'
* 'Sweden'
* 'Slovenia'
* 'Slovakia'

Insert the desired job title and run DJS.

###Reading the outcome

Congratulations! In less than one minute the proccess is completed. Find out in your results folder a short and simple to read report composed of a regular table and a bar chart.


##Status and development
Data Job Selector is in **pre-alpha** stages of development. Please, report any error to DataJobSelector@datajobselector.com. Feedback is always appreciated.

### Technology stack
DJS is a standalone software developed in Python. Requires common Phyton libraries such as Pandas, Beautifoulsoup, regex, requests and matplotlib.

### **Folder structure**
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   ├── acquisition.ipynb
    │   └── wrangling.ipynb
    |   ├── analyze.ipynb
    │   └── report.ipynb
    |
    ├── package1
    │   ├── module1.py
    │   └── module2.py
    └── data
        ├── raw
        ├── processed
        └── results


### Next steps
DJS is a work-in-progress tool. Future versions will conect to a job aggregator API to cross info with the number of vacancies in selected working field.

## **Contact info**
Simple, fast, useful. To improve your company pipeline efficiency, get in touch.

---

> Here you have some repo examples:
- [Mamba (OCR-Translator-Assistant)](https://github.com/YonatanRA/OCR-translator-assistant-project)
- [Art Classification](https://github.com/serguma/art_classification)
- [OSNet-IBN (width x 1.0) Lite](https://github.com/RodMech/OSNet-IBN1-Lite)
- [Movie Founder](https://github.com/Alfagu/final-project-Ironhack-0419mad)
- [Convolutional Neural Network to detect Pneumonia](https://github.com/jmolins89/final-project)
- [Brain tumor detection project](https://github.com/alonsopdani/brain-tumor-detection-project)
- [Policy-Gradient-Methods](https://github.com/cyoon1729/Policy-Gradient-Methods)

> Here you have some tools and references:
- [Make a README](https://www.makeareadme.com/)
- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

