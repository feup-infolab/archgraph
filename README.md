# archgraph

[![Build Status](https://travis-ci.com/feup-infolab/archgraph.svg?branch=master)](https://travis-ci.com/feup-infolab/archgraph)
[![Coverage Status](https://coveralls.io/repos/github/feup-infolab/archgraph/badge.svg?branch=master)](https://coveralls.io/github/feup-infolab/archgraph?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f3070810a6f946de93967d5a78acbfc0)](https://app.codacy.com/manual/feup-infolab/archgraph?utm_source=github.com&utm_medium=referral&utm_content=feup-infolab/archgraph&utm_campaign=Badge_Grade_Dashboard)
[![](https://images.microbadger.com/badges/image/feupinfolab/archgraph.svg)](https://microbadger.com/images/feupinfolab/archgraph "Get your own image badge on microbadger.com")

## Project context

Over the years the National Archive of Torre do Tombo has been acquiring a unique collection of historical and contemporary objects. In his possession he has original documents from the 9th century to the present day. This institution has, over the years, been describing all the cultural objects it has in its possession, and this is one of the tasks that has the most human resources allocated.
Torre do Tombo has used the ISAD (G) and ISAAR (CPF) standards for the description of its cultural objects, however these have been showing some limitations that need to be overcome. Taking into account these limitations, the EPISA (Entity and Property Inference for Semantic Archives) project was created, a project that has as partners INESC TEC, DGLAB (General Direction of the Book, Archives and Libraries) and the University of Évora , and a duration of three years, 2019-2021.
This project aims, among other objectives, to develop a prototype for an open source knowledge graph platform, adopting the data model for archival description used by DGLAB. This project is also dedicated to finding ways to ensure the effective migration of content stored according to ICA standards to an ontology-based model, requiring the use of cross-walks and the inference of new relationships with semi-automated methods. (Almeida and Runa 2018)
For the development of the knowledge graph, the model CIDOC-CRM, a model created in the context of museums and which is already stable, has been taken into account.

## ArchOnto

New ontology for the domain of the files that imports the model CIDOC-CRM, in the version 6.2, and the Ontologia Data Object, explained further below. In this ontology there is also the creation of classes and properties to be able to represent the fields of ISAD (G) that CIDOC-CRM is not capable, since this was created for the museum area and does not include everything that is necessary to represent the domain of the files.
Most Data Properties were created, since there were almost no such properties in CIDOC-CRM and it was necessary to create properties that would allow the description of fields with a larger amount of text, such as the case of Administrative History and Custodial and the scope and Content.
Object Properties were also created to represent the existing levels of archival description in ISAD (G) and a class to represent these same levels.
In common, all properties and classes created for this model have an "A" prefix, which aims to differentiate the CIDOC-CRM model. Whenever the creation of a class this has the prefix "AE", while in the properties has the prefix "AP".

Data Object
In order to have a data validation and a cleaner implementation code, an ontology was created where the data hierarchy to be validated is present. In this hierarchy, the different typologies of data necessary for the elaboration of validation are taken into account.


Both Ontologies, EXT and Data Object, are not the final versions, but are both in active development.

## Docker Installation

```
git clone https://github.com/feup-infolab/archgraph.git
cd archgraph
docker-compose up
# Access http://localhost:4200 on your browser
```


## Mac and Linux (Ubuntu) Installation

Open The command line and enter:

```
git clone https://github.com/feup-infolab/archgraph.git
cd archgraph
./conf/install.sh
```

The setup should automatically detect your operating system (Mac or Linux) and run the appropriate commands.

## Running the program

```
./conf/run.sh
```

To exit, press Ctrl+C, and both the API server and the frontend server should be terminated.
