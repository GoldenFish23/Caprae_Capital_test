# Caprae Capital: Lead Generation Platform
### Author: Vijay Bahadur Vishwakarma
### Date: [Today’s Date]

## Rationale
The goal was to simulate a scalable, ethical, and business-relevant pipeline for enriching company data. The approach focused on:

- Compliance: No live scraping of restricted sources (e.g., LinkedIn); all data is simulated or cached.
- Business Value: Extracting actionable insights (company info, services, contact details) to support lead scoring and segmentation.
- Technical Depth: Demonstrating scraping, enrichment, and UI/UX best practices within a time-bound challenge.
## Approach
1. Simulated Scraping & Data Structure
Used local HTML files and prebuilt datasets to mimic real-world scraping.
Extracted key fields: company name, website, industry, specialties, headquarters, overview, quick links, and contact info.
Saved enriched data to a CSV for easy analysis and downstream use.
2. Data Enrichment & Extraction
Quick Links: Used Selenium to parse company websites and extract main navigation links (About, Contact, Blog, etc.), selecting the shortest/broadest URLs for each section.
Contact Info: Regex-based extraction of emails, phone numbers, and locations from contact pages, with filters to avoid false positives (e.g., images, dates).
Overview: Pulled company descriptions for potential NLP-based summarization.
3. User Interface (Streamlit)
Built a fast, interactive GUI for searching companies by name, industry, or specialties.
Displayed results in a table with clickable quick links and readable contact info.
Provided detailed company views with all enriched fields.
## Model Selection
- Selenium: Chosen for its ability to handle dynamic web content and simulate real scraping scenarios.
- Regex: Used for lightweight, robust extraction of emails and phone numbers.
- Streamlit: Selected for rapid prototyping of business-facing dashboards.
- (Optional) NLP: Considered for overview summarization using Hugging Face transformers (e.g., BART), but not implemented due to time constraints.
## Key Decisions & Trade-offs
- Simulated Data: Ensured ethical compliance and reproducibility.
- Focus on Quality: Prioritized clean, actionable data and user experience over raw data volume.
- Extensible Pipeline: Designed functions to be easily adapted for real-world scraping or further enrichment (e.g., NLP, validation).