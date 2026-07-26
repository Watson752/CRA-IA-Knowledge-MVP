# CRA-IA-Knowledge-MVP

A local-first knowledge-management prototype that organizes publicly available Canada Revenue Agency information into a structured Obsidian knowledge base.

The current phase focuses on documentation structure, metadata, relationships, and navigation. A Graph Retrieval-Augmented Generation system is planned as the next major phase and will be added in the near future.

## Overview

`CRA-IA-Knowledge-MVP` explores how publicly available CRA information can be organized into a connected and searchable knowledge base.

The project uses Obsidian and Markdown to document topics such as publicly described programs, services, responsibilities, processes, policies, and organizational concepts. Notes are connected through links, tags, properties, and reusable templates.

The project is intended to demonstrate a possible knowledge-management use case for teams working in large organizations. It is an independent personal project and is not based on any internal CRA project, system, repository, dataset, documentation, or implementation.

All information used in the project comes from publicly accessible CRA or Government of Canada sources, or from synthetic examples created specifically for demonstration purposes.

## Current Scope

The current MVP focuses on:

* Building a structured Obsidian vault
* Organizing public CRA information into clear topics
* Defining consistent note templates
* Adding Markdown metadata and properties
* Connecting related programs, processes, services, policies, and concepts
* Improving navigation through backlinks, tags, and internal links
* Preparing the documentation for future automated ingestion and retrieval

Graph RAG is not yet implemented. It is a planned near-term extension of the project.

## Objectives

* Demonstrate how Obsidian can support organizational knowledge management
* Convert public information into structured and reusable Markdown documentation
* Define relationships between related organizational concepts
* Create a maintainable documentation architecture
* Improve information discovery and navigation
* Prepare the knowledge base for semantic search
* Develop a Graph RAG proof of concept in a future phase
* Produce grounded answers with references to public source material
* Evaluate retrieval quality, traceability, and answer relevance

## Project Roadmap

### Phase 1 — Obsidian Knowledge Base

* Define folder and naming conventions
* Create reusable note templates
* Add tags, aliases, and Markdown properties
* Organize publicly available CRA information
* Link related notes and concepts
* Document source URLs and retrieval dates

### Phase 2 — Document Processing

* Parse Markdown documents
* Extract headings, links, tags, and properties
* Validate required metadata
* Divide documents into retrieval-friendly sections
* Build a searchable document catalogue

### Phase 3 — Semantic Search

* Generate document embeddings
* Add a local vector store
* Implement semantic and keyword search
* Return relevant source documents and sections
* Evaluate retrieval relevance

### Phase 4 — Knowledge Graph

* Identify entities and relationships
* Represent concepts as graph nodes and edges
* Support relationship traversal
* Connect graph entities to source documents
* Visualize relationships between topics

### Phase 5 — Graph RAG

* Combine semantic retrieval with graph traversal
* Retrieve related documents, entities, and relationships
* Generate grounded answers from the retrieved context
* Include references to the original public sources
* Evaluate answer quality, traceability, and hallucination risk

## Proposed Architecture

```text
Public CRA and Government of Canada Sources
                    |
                    v
         Obsidian Markdown Knowledge Base
                    |
                    v
       Document Parsing and Validation
                    |
          +---------+---------+
          |                   |
          v                   v
   Semantic Index       Knowledge Graph
          |                   |
          +---------+---------+
                    |
                    v
         Hybrid Retrieval Layer
                    |
                    v
          Future Graph RAG System
                    |
                    v
       Grounded Answers with Sources
```

## Planned Repository Structure

```text
CRA-IA-Knowledge-MVP/
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   ├── architecture/
│   ├── decisions/
│   ├── security/
│   └── evaluation/
├── vault/
│   ├── concepts/
│   ├── programs/
│   ├── processes/
│   ├── services/
│   ├── policies/
│   ├── systems/
│   ├── templates/
│   └── examples/
├── src/
│   ├── ingestion/
│   ├── extraction/
│   ├── graph/
│   ├── retrieval/
│   └── evaluation/
├── scripts/
├── tests/
├── data/
│   ├── public/
│   ├── synthetic/
│   └── processed/
└── config/
```

## Example Knowledge Model

Possible node types include:

* Program
* Service
* Process
* Organization
* Role
* Policy
* Procedure
* Publication
* Dataset
* Form
* Document
* Concept

Possible relationships include:

* `PROGRAM_PROVIDES_SERVICE`
* `ORGANIZATION_MANAGES_PROGRAM`
* `POLICY_GOVERNS_PROCESS`
* `PROCESS_REQUIRES_FORM`
* `DOCUMENT_DESCRIBES_PROGRAM`
* `SERVICE_SUPPORTS_CLIENT`
* `PUBLICATION_EXPLAINS_POLICY`
* `CONCEPT_RELATES_TO_CONCEPT`

These relationships are modelling choices created for this prototype. They do not represent an official CRA data model.

## Information Sources

The knowledge base may use:

* Public CRA webpages
* Public Government of Canada webpages
* Public reports and publications
* Public departmental plans and results reports
* Public forms and guidance documents
* Open Government datasets
* Synthetic examples created for testing

Each note should include source information where applicable so that content can be traced back to its original public publication.

## Data and Security Principles

This repository must not contain:

* Taxpayer information
* Employee information
* Protected or classified information
* Internal CRA documents
* Internal source code
* Internal screenshots
* Internal system information
* Internal organizational discussions
* Credentials, tokens, certificates, or private keys
* Production datasets
* Information obtained through internal CRA access
* Material copied or adapted from internal CRA work

Only publicly available information and synthetic demonstration data should be committed.

## Technology Candidates

The technology stack will evolve as the project develops.

Current and potential technologies include:

* Obsidian
* Markdown
* Python
* Pydantic
* DuckDB
* NetworkX
* Neo4j
* Chroma or FAISS
* LangChain or LlamaIndex
* Local or approved hosted language models
* pytest

Technology decisions will be recorded as the MVP develops.

## Project Status

* [x] Project concept defined
* [x] Local Obsidian vault started
* [x] Repository structure created
* [ ] Documentation conventions finalized
* [ ] Public CRA source catalogue created
* [ ] Initial public-information notes added
* [ ] Note templates finalized
* [ ] Markdown ingestion implemented
* [ ] Metadata validation implemented
* [ ] Semantic search implemented
* [ ] Knowledge graph implemented
* [ ] Graph RAG implemented
* [ ] Evaluation framework implemented

## Independence and Disclaimer

This repository is an independent personal project created on personal equipment.

It is not part of the author's internal work at the Canada Revenue Agency. It was not created using internal CRA data, documents, source code, systems, tools, repositories, or protected information.

The project is not an official Canada Revenue Agency or Government of Canada product, initiative, prototype, publication, or endorsed system.

The repository demonstrates a possible knowledge-management use case for organizational teams using only publicly available CRA and Government of Canada information, together with synthetic demonstration content.

The structure, architecture, entity model, relationships, code, and technical decisions in this repository are independently designed for learning and portfolio purposes.

## Author

Srivathsan Murali
