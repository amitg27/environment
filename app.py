from flask import Flask, render_template, abort

app = Flask(__name__)

# All certification data extracted from the document
CERTIFICATIONS = {
    "green-business": {
        "title": "Green Business Certification",
        "category": "product",
        "icon": "leaf",
        "short": "Demonstrate commitment to environmental responsibility, sustainability, and efficient resource management.",
        "applicable": "Green Business Certification is applicable to organizations that want to demonstrate their commitment towards environmental responsibility, sustainability, and efficient resource management.",
        "suitable_for": [
            "Manufacturing Companies", "MSMEs & Industrial Units", "Corporate Offices",
            "IT & Service Companies", "Export-Oriented Units", "Real Estate & Infrastructure Projects",
            "Hospitality & Retail Businesses", "Warehouses & Logistics Firms",
            "Startups adopting sustainable practices"
        ],
        "applicable_note": "Any business seeking to improve ESG performance, reduce environmental impact, or enhance brand credibility can apply.",
        "criteria": [
            {
                "title": "Environmental Criteria",
                "items": ["Energy consumption & renewable adoption", "Carbon emissions monitoring",
                          "Water conservation practices", "Waste management & recycling systems",
                          "Pollution control measures", "Sustainable sourcing of materials"]
            },
            {
                "title": "Social Responsibility Criteria",
                "items": ["Employee health & safety measures", "Fair labour practices",
                          "Community engagement initiatives", "Diversity & inclusion practices"]
            },
            {
                "title": "Governance Criteria",
                "items": ["Sustainability policies in place", "Compliance with environmental laws",
                          "ESG reporting & transparency", "Ethical supply chain practices"]
            }
        ],
        "criteria_note": "Each parameter is scored using a standardized assessment model, leading to certification levels such as Bronze, Silver, Gold, or Platinum.",
        "process": [
            {"step": "Application", "desc": "The organization submits an online application along with preliminary business details."},
            {"step": "Documentation Review", "desc": "Submission of environmental policies, compliance records, energy/water data, and operational information."},
            {"step": "Sustainability Assessment", "desc": "Our expert auditors conduct document verification, management interviews, site inspection (if required), and operational evaluation."},
            {"step": "Scoring & Gap Analysis", "desc": "The organization is evaluated against defined sustainability benchmarks and receives a detailed performance scorecard."},
            {"step": "Certification Issuance", "desc": "Upon successful evaluation, the organization is awarded Green Business Certification along with Certification Seal, Digital Badge, and Public Listing on certification registry."},
            {"step": "Renewal & Monitoring", "desc": "Certification remains valid for a defined period subject to annual compliance review."}
        ],
        "benefits": [
            {"title": "Environmental Benefits", "items": ["Reduction in energy and resource consumption", "Lower carbon footprint and environmental impact", "Improved waste management and recycling practices", "Adoption of renewable and sustainable technologies"]},
            {"title": "Business & Financial Benefits", "items": ["Improved operational efficiency and cost savings", "Better access to ESG-focused investors and funds", "Competitive advantage in tenders and global markets", "Eligibility for sustainability-linked incentives and programs"]},
            {"title": "Brand & Market Benefits", "items": ["Enhanced corporate reputation and trust", "Stronger positioning with international buyers and partners", "Differentiation from competitors", "Increased customer confidence"]},
            {"title": "Compliance & Risk Benefits", "items": ["Alignment with environmental regulations and ESG norms", "Preparedness for future compliance requirements", "Reduced environmental and regulatory risks"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "Bronze Certification", "score": "40 - 54", "focus": "Compliance, basic monitoring, initial improvements", "desc": "Awarded to organizations that demonstrate foundational sustainability practices and compliance with basic environmental norms."},
            {"name": "Silver", "label": "Silver Certification", "score": "55 - 69", "focus": "Efficiency improvements, reporting systems, policy integration", "desc": "Awarded to organizations implementing structured sustainability initiatives and measurable improvements in resource efficiency."},
            {"name": "Gold", "label": "Gold Certification", "score": "70 - 84", "focus": "Renewable adoption, supply chain responsibility, ESG integration", "desc": "Awarded to organizations demonstrating strong sustainability leadership and advanced environmental management systems."},
            {"name": "Platinum", "label": "Platinum Certification", "score": "85+", "focus": "Net-zero initiatives, circular economy practices, innovation leadership", "desc": "Awarded to organizations that set industry benchmarks in sustainability and demonstrate measurable long-term environmental impact."}
        ],
        "faq": [
            {"q": "What is Green Business Certification?", "a": "It is an independent assessment that evaluates an organization's environmental practices, sustainability initiatives, and ESG performance against defined benchmarks."},
            {"q": "Is certification mandatory?", "a": "No, it is voluntary. However, many companies pursue certification to enhance credibility, attract investors, and prepare for ESG disclosures."},
            {"q": "How long does the certification process take?", "a": "Typically 4-8 weeks depending on the size of the organization, data availability, and audit requirements."},
            {"q": "Does the certification require a site visit?", "a": "In many cases yes, especially for manufacturing or infrastructure projects. For service organizations, virtual audits may be sufficient."},
            {"q": "What documents are required?", "a": "Basic business details, environmental compliance records, energy and water data, waste management practices, and internal sustainability policies."},
            {"q": "How long is the certification valid?", "a": "Certification is usually valid for one year, subject to periodic review or surveillance audit."},
            {"q": "Can a company improve its rating after certification?", "a": "Yes. Organizations may reapply after implementing improvements to achieve a higher certification level."},
            {"q": "Does certification help with ESG reporting or IPO readiness?", "a": "Yes. Certification supports ESG disclosures, investor confidence, and sustainability reporting requirements often expected from growth-stage and public companies."}
        ]
    },
    "carbon-neutral": {
        "title": "Carbon Neutral Certification",
        "category": "environmental",
        "icon": "globe",
        "short": "Measure, reduce, and offset greenhouse gas emissions to demonstrate climate responsibility.",
        "applicable": "Carbon Neutral Certification is applicable to organizations that wish to measure, reduce, and offset their greenhouse gas emissions and demonstrate their commitment to climate responsibility.",
        "suitable_for": [
            "Manufacturing Companies", "Export-Oriented Businesses", "Corporates with ESG goals",
            "IT & Service Organizations", "Real Estate & Infrastructure Projects",
            "Hospitality & Tourism Businesses", "Logistics & Transportation Firms",
            "Startups seeking sustainability positioning", "Companies preparing for ESG disclosures or public listing"
        ],
        "applicable_note": "Any organization seeking to reduce climate impact and enhance sustainability credibility can apply.",
        "criteria": [
            {"title": "Carbon Footprint Assessment", "items": ["Measurement of Scope 1 emissions (direct fuel usage)", "Measurement of Scope 2 emissions (electricity consumption)", "Assessment of relevant Scope 3 emissions (supply chain, travel, logistics)"]},
            {"title": "Emission Reduction Initiatives", "items": ["Energy efficiency improvements", "Renewable energy adoption", "Sustainable procurement practices", "Process optimization"]},
            {"title": "Carbon Offset Strategy", "items": ["Use of verified carbon credits", "Investment in environmental projects", "Tree plantation or carbon removal initiatives"]},
            {"title": "Monitoring & Reporting", "items": ["Carbon tracking system", "Reduction targets and timelines", "Sustainability reporting transparency"]}
        ],
        "criteria_note": "Organizations are evaluated using a standardized scoring methodology before certification is issued.",
        "process": [
            {"step": "Application", "desc": "Organization submits an application with operational and energy usage details."},
            {"step": "Carbon Footprint Calculation", "desc": "Experts assess emissions across energy, operations, logistics, and supply chain using accepted carbon accounting methods."},
            {"step": "Reduction Strategy Review", "desc": "The organization's emission reduction measures are evaluated, and improvement opportunities are identified."},
            {"step": "Offset Verification", "desc": "Unavoidable emissions are neutralized through verified carbon offset projects."},
            {"step": "Certification Review", "desc": "The assessment report is reviewed by the certification committee."},
            {"step": "Certification Issuance", "desc": "Upon approval, the organization receives Carbon Neutral Certificate, Digital Badge, and Public listing in registry."},
            {"step": "Annual Monitoring", "desc": "Periodic review ensures continued carbon neutrality compliance."}
        ],
        "benefits": [
            {"title": "Environmental Benefits", "items": ["Clear measurement of carbon impact", "Structured reduction roadmap", "Contribution to global climate goals", "Support for renewable adoption"]},
            {"title": "Business & Financial Benefits", "items": ["Attracts ESG-focused investors", "Enhances eligibility for green finance", "Competitive advantage in global markets", "Improves sustainability reporting credibility"]},
            {"title": "Brand Benefits", "items": ["Demonstrates climate leadership", "Builds stakeholder trust", "Differentiates brand from competitors", "Supports export and multinational partnerships"]},
            {"title": "Compliance Benefits", "items": ["Preparedness for carbon disclosure norms", "Alignment with global sustainability frameworks", "Reduced regulatory and reputational risk"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "Carbon Aware Organization", "score": "", "focus": "Baseline assessment and monitoring", "desc": "Organizations that have measured their emissions and begun tracking carbon impact."},
            {"name": "Silver", "label": "Carbon Managed Organization", "score": "", "focus": "Efficiency improvements, reduction targets", "desc": "Organizations implementing measurable emission reduction initiatives."},
            {"name": "Gold", "label": "Carbon Neutral Organization", "score": "", "focus": "Emission reduction + offsetting", "desc": "Organizations that have reduced emissions and offset remaining carbon footprint through verified projects."},
            {"name": "Platinum", "label": "Climate Positive Organization", "score": "", "focus": "Net-positive climate contribution and long-term decarbonization strategy", "desc": "Organizations that remove or offset more carbon than they emit."}
        ],
        "faq": [
            {"q": "What is Carbon Neutral Certification?", "a": "It validates that an organization has measured, reduced, and offset its carbon emissions to achieve net-zero impact."},
            {"q": "Is carbon neutrality only for large companies?", "a": "No. Businesses of all sizes, including MSMEs and startups, can pursue carbon neutrality."},
            {"q": "How are emissions calculated?", "a": "Emissions are calculated using standardized carbon accounting methods covering fuel use, electricity consumption, logistics, and operations."},
            {"q": "Do companies need to reduce emissions before offsetting?", "a": "Yes. Reduction is prioritized, and offsets are used only for unavoidable emissions."},
            {"q": "What types of projects qualify for carbon offsets?", "a": "Examples include renewable energy projects, afforestation initiatives, methane capture, and other verified environmental projects."},
            {"q": "How long is the certification valid?", "a": "Typically one year, subject to periodic review or monitoring."},
            {"q": "Can certification help with ESG reporting?", "a": "Yes. Carbon neutrality strengthens ESG disclosures, sustainability reports, and investor confidence."}
        ]
    },
    "water-neutral": {
        "title": "Water Neutral Certification",
        "category": "environmental",
        "icon": "droplet",
        "short": "Measure, reduce, and balance water consumption through conservation and replenishment initiatives.",
        "applicable": "Water Neutral Certification is designed for organizations that want to measure, reduce, and balance their water consumption through conservation, efficiency improvements, and replenishment initiatives.",
        "suitable_for": [
            "Manufacturing and Industrial Units", "Real Estate & Infrastructure Projects",
            "Hotels & Hospitality Businesses", "Food & Beverage Companies",
            "Textile & Processing Industries", "Agriculture & Agro-Processing Units",
            "IT Parks & Corporate Campuses", "Educational Institutions & Hospitals"
        ],
        "applicable_note": "Any organization seeking responsible water stewardship and sustainable resource management can apply.",
        "criteria": [
            {"title": "Water Footprint Assessment", "items": ["Measurement of water consumption across operations", "Identification of high-usage processes", "Source mapping (groundwater, municipal, recycled water)"]},
            {"title": "Water Efficiency Measures", "items": ["Water-saving technologies and processes", "Recycling and reuse systems", "Rainwater harvesting implementation", "Leak detection and control mechanisms"]},
            {"title": "Water Replenishment Initiatives", "items": ["Groundwater recharge projects", "Watershed development activities", "Community water restoration programs", "Plantation and ecological restoration efforts"]},
            {"title": "Monitoring & Governance", "items": ["Water tracking and reporting systems", "Reduction targets and conservation policies", "Compliance with local water regulations"]}
        ],
        "criteria_note": "Organizations receive a water sustainability score based on these parameters.",
        "process": [
            {"step": "Application", "desc": "Organization submits water usage details, operational data, and sustainability practices."},
            {"step": "Water Footprint Calculation", "desc": "Experts evaluate water consumption patterns and operational dependence."},
            {"step": "Efficiency & Conservation Review", "desc": "Assessment of water-saving measures and reuse systems in place."},
            {"step": "Replenishment Verification", "desc": "Validation of water offset initiatives such as recharge or restoration projects."},
            {"step": "Certification Review", "desc": "Findings are evaluated by the certification committee."},
            {"step": "Certification Issuance", "desc": "Successful organizations receive Water Neutral Certificate, Digital Badge, and Listing in public registry."},
            {"step": "Periodic Monitoring", "desc": "Annual review ensures continued compliance with water neutrality goals."}
        ],
        "benefits": [
            {"title": "Environmental Benefits", "items": ["Reduces freshwater consumption", "Encourages water recycling and conservation", "Supports groundwater recharge and ecosystem restoration"]},
            {"title": "Business Benefits", "items": ["Reduces long-term water costs", "Improves operational sustainability", "Enhances ESG performance metrics", "Strengthens resilience against water scarcity risks"]},
            {"title": "Brand & Market Benefits", "items": ["Demonstrates responsible water stewardship", "Improves reputation among investors and stakeholders", "Supports sustainability reporting and disclosures"]},
            {"title": "Compliance Benefits", "items": ["Preparedness for water regulations and audits", "Reduced environmental and operational risks"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "Water Aware Organization", "score": "", "focus": "Baseline measurement and tracking", "desc": "Organizations that have measured water usage and begun monitoring consumption."},
            {"name": "Silver", "label": "Water Managed Organization", "score": "", "focus": "Recycling systems, reduction initiatives", "desc": "Organizations implementing efficiency improvements and conservation measures."},
            {"name": "Gold", "label": "Water Neutral Organization", "score": "", "focus": "Efficiency + replenishment balance", "desc": "Organizations balancing water consumption through replenishment or offset projects."},
            {"name": "Platinum", "label": "Water Positive Organization", "score": "", "focus": "Net-positive water impact and ecosystem restoration", "desc": "Organizations replenishing more water than they consume and demonstrating leadership in water sustainability."}
        ],
        "faq": [
            {"q": "What is Water Neutral Certification?", "a": "It validates that an organization has measured, reduced, and balanced its water consumption through conservation and replenishment initiatives."},
            {"q": "Is water neutrality relevant for service companies?", "a": "Yes. Offices, campuses, and IT parks can also measure and offset water consumption."},
            {"q": "What counts as water replenishment?", "a": "Recharge structures, watershed development, restoration projects, and community water initiatives can contribute to water neutrality."},
            {"q": "Does certification require a site visit?", "a": "For industrial or infrastructure projects, site inspection is typically conducted. Service organizations may undergo remote assessment."},
            {"q": "How long is the certification valid?", "a": "Typically one year subject to periodic monitoring."},
            {"q": "Can certification support ESG reporting?", "a": "Yes. Water neutrality strengthens environmental disclosures, sustainability reports, and investor perception."}
        ]
    },
    "esg-compliance": {
        "title": "ESG Compliance Certification",
        "category": "esg",
        "icon": "shield-check",
        "short": "Validate your organization's Environmental, Social, and Governance compliance across all operational areas.",
        "applicable": "ESG Compliance Certification is designed for organizations that want to validate their adherence to Environmental, Social, and Governance standards across operations.",
        "suitable_for": [
            "Listed & Pre-IPO Companies", "Large Corporates & Conglomerates",
            "Manufacturing & Industrial Units", "Financial Institutions & NBFCs",
            "Real Estate Developers", "IT & Service Companies", "Export-Oriented Businesses"
        ],
        "applicable_note": "Any organization seeking structured ESG compliance and investor readiness can apply.",
        "criteria": [
            {"title": "Environmental Compliance", "items": ["Environmental policy implementation", "Resource efficiency and emissions monitoring", "Waste and pollution management", "Regulatory compliance verification"]},
            {"title": "Social Compliance", "items": ["Labour practices and worker welfare", "Health and safety systems", "Community engagement programs", "Diversity and inclusion practices"]},
            {"title": "Governance Compliance", "items": ["Board-level ESG oversight", "Ethical business practices", "Anti-corruption policies", "Transparency and disclosure systems"]}
        ],
        "criteria_note": "Organizations are scored across ESG parameters using a standardized framework.",
        "process": [
            {"step": "Application", "desc": "Organization submits operational details and ESG-related documentation."},
            {"step": "Documentation Review", "desc": "Evaluation of policies, compliance records, and governance frameworks."},
            {"step": "ESG Assessment", "desc": "Expert assessment of environmental, social, and governance practices."},
            {"step": "Scoring & Gap Analysis", "desc": "Organization receives ESG performance scorecard with recommendations."},
            {"step": "Certification Issuance", "desc": "Approved organizations receive ESG Compliance Certificate, Digital Badge, and Registry listing."},
            {"step": "Annual Review", "desc": "Periodic monitoring ensures continued ESG compliance."}
        ],
        "benefits": [
            {"title": "Environmental Benefits", "items": ["Structured environmental management", "Improved resource efficiency", "Regulatory compliance assurance"]},
            {"title": "Business Benefits", "items": ["Attracts ESG-focused investors", "Improves IPO and funding readiness", "Competitive advantage in global markets"]},
            {"title": "Brand Benefits", "items": ["Demonstrates corporate responsibility", "Builds stakeholder confidence", "Enhances market positioning"]},
            {"title": "Compliance Benefits", "items": ["Alignment with SEBI, global ESG norms", "Reduced regulatory risk", "Preparedness for mandatory disclosures"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "ESG Aware", "score": "", "focus": "Basic compliance and monitoring", "desc": "Organizations with foundational ESG policies and compliance measures."},
            {"name": "Silver", "label": "ESG Managed", "score": "", "focus": "Structured ESG systems and reporting", "desc": "Organizations with integrated ESG management and reporting systems."},
            {"name": "Gold", "label": "ESG Leader", "score": "", "focus": "Advanced ESG integration across operations", "desc": "Organizations demonstrating strong ESG leadership and measurable impact."},
            {"name": "Platinum", "label": "ESG Champion", "score": "", "focus": "Industry-leading ESG performance", "desc": "Organizations setting industry benchmarks in ESG performance and innovation."}
        ],
        "faq": [
            {"q": "What is ESG Compliance Certification?", "a": "It validates that an organization meets defined Environmental, Social, and Governance standards."},
            {"q": "Is ESG certification mandatory?", "a": "While not always mandatory, ESG compliance is increasingly expected by investors, regulators, and stakeholders."},
            {"q": "How long does certification take?", "a": "Typically 4-8 weeks depending on organization size and data readiness."},
            {"q": "How long is certification valid?", "a": "Usually one year, subject to periodic review."}
        ]
    },
    "esg-rating": {
        "title": "ESG Rating & Scorecard",
        "category": "esg",
        "icon": "bar-chart",
        "short": "Get a comprehensive ESG performance rating and detailed scorecard for stakeholder reporting.",
        "applicable": "ESG Rating & Scorecard service provides organizations with a structured evaluation of their Environmental, Social, and Governance performance.",
        "suitable_for": [
            "Listed Companies & IPO-bound Firms", "Large Corporates", "Financial Institutions",
            "Real Estate & Infrastructure Companies", "Manufacturing Units", "Export Businesses"
        ],
        "applicable_note": "Any organization seeking transparent ESG performance measurement can apply.",
        "criteria": [
            {"title": "Environmental Score", "items": ["Carbon footprint and emissions", "Energy and water efficiency", "Waste management practices", "Environmental compliance"]},
            {"title": "Social Score", "items": ["Employee welfare and safety", "Community impact", "Diversity and labour practices", "Stakeholder engagement"]},
            {"title": "Governance Score", "items": ["Board oversight and ethics", "Transparency and reporting", "Risk management systems", "Anti-corruption measures"]}
        ],
        "criteria_note": "Organizations receive a detailed scorecard with ratings across all ESG dimensions.",
        "process": [
            {"step": "Application", "desc": "Organization submits ESG data and operational information."},
            {"step": "Data Analysis", "desc": "Experts analyze environmental, social, and governance data points."},
            {"step": "Assessment & Scoring", "desc": "Structured scoring across ESG parameters using standardized methodology."},
            {"step": "Scorecard Generation", "desc": "Detailed ESG scorecard with ratings, benchmarks, and recommendations."},
            {"step": "Report Issuance", "desc": "Organization receives ESG Rating Report and Digital Badge."},
            {"step": "Annual Update", "desc": "Rating can be updated annually to reflect improvements."}
        ],
        "benefits": [
            {"title": "Transparency Benefits", "items": ["Clear ESG performance measurement", "Standardized benchmarking", "Stakeholder-ready reporting"]},
            {"title": "Business Benefits", "items": ["Investor confidence and readiness", "Competitive positioning", "Access to ESG-focused capital"]},
            {"title": "Brand Benefits", "items": ["Demonstrates ESG commitment", "Market differentiation", "Enhanced credibility"]},
            {"title": "Compliance Benefits", "items": ["Supports BRSR and ESG disclosures", "Regulatory preparedness", "Risk identification"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "Basic Rating", "score": "", "focus": "Initial ESG measurement", "desc": "Foundational ESG assessment and baseline scoring."},
            {"name": "Silver", "label": "Standard Rating", "score": "", "focus": "Structured ESG evaluation", "desc": "Comprehensive ESG analysis with benchmarking."},
            {"name": "Gold", "label": "Advanced Rating", "score": "", "focus": "Detailed multi-dimensional scoring", "desc": "In-depth ESG assessment with sector comparisons."},
            {"name": "Platinum", "label": "Premium Rating", "score": "", "focus": "Full ESG intelligence report", "desc": "Complete ESG rating with strategic recommendations and roadmap."}
        ],
        "faq": [
            {"q": "What is the ESG Rating & Scorecard?", "a": "It is a structured evaluation that rates an organization's Environmental, Social, and Governance performance."},
            {"q": "How is it different from ESG Certification?", "a": "The rating provides a performance score, while certification validates compliance with defined standards."},
            {"q": "Can ratings be improved?", "a": "Yes. Organizations can improve scores by implementing recommended ESG initiatives."},
            {"q": "How often should ratings be updated?", "a": "Annually, to reflect current ESG performance and improvements."}
        ]
    },
    "brsr-compliance": {
        "title": "BRSR Compliance Certification",
        "category": "esg",
        "icon": "file-text",
        "short": "Business Responsibility and Sustainability Reporting compliance for Indian regulatory requirements.",
        "applicable": "BRSR Compliance Certification helps organizations prepare for and comply with SEBI's Business Responsibility and Sustainability Reporting requirements.",
        "suitable_for": [
            "Top 1000 Listed Companies (by market cap)", "Companies preparing for listing",
            "Large Corporates with ESG goals", "Companies in SEBI-regulated sectors",
            "Organizations seeking investor transparency"
        ],
        "applicable_note": "Any organization required or aspiring to comply with BRSR framework can apply.",
        "criteria": [
            {"title": "Environmental Disclosures", "items": ["Energy consumption and conservation", "Emissions and waste management", "Water stewardship", "Biodiversity impact"]},
            {"title": "Social Disclosures", "items": ["Employee well-being and safety", "Human rights practices", "Community development", "Consumer responsibility"]},
            {"title": "Governance Disclosures", "items": ["Ethical conduct and transparency", "Regulatory compliance", "Stakeholder engagement", "Policy implementation"]}
        ],
        "criteria_note": "Assessment is aligned with SEBI BRSR framework and nine principles of responsible business conduct.",
        "process": [
            {"step": "Application", "desc": "Organization provides business details and existing reporting practices."},
            {"step": "Gap Assessment", "desc": "Experts evaluate current disclosures against BRSR requirements."},
            {"step": "Data Collection & Review", "desc": "Structured data gathering across all BRSR parameters."},
            {"step": "Report Preparation Support", "desc": "Assistance in preparing BRSR-compliant disclosures."},
            {"step": "Certification Issuance", "desc": "Organization receives BRSR Compliance Certificate and verification report."},
            {"step": "Annual Review", "desc": "Periodic review for continued compliance."}
        ],
        "benefits": [
            {"title": "Regulatory Benefits", "items": ["SEBI BRSR compliance readiness", "Structured disclosure framework", "Reduced regulatory risk"]},
            {"title": "Business Benefits", "items": ["Investor confidence", "IPO and listing readiness", "Competitive positioning"]},
            {"title": "Brand Benefits", "items": ["Demonstrates transparency", "Stakeholder trust", "Market credibility"]},
            {"title": "Operational Benefits", "items": ["Improved data management", "ESG integration across operations", "Better governance practices"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "BRSR Aware", "score": "", "focus": "Initial gap assessment", "desc": "Organization has begun assessing BRSR readiness."},
            {"name": "Silver", "label": "BRSR Prepared", "score": "", "focus": "Structured data collection", "desc": "Organization has structured BRSR data and reporting systems."},
            {"name": "Gold", "label": "BRSR Compliant", "score": "", "focus": "Full BRSR compliance", "desc": "Organization meets BRSR reporting requirements."},
            {"name": "Platinum", "label": "BRSR Leader", "score": "", "focus": "Beyond compliance - leadership reporting", "desc": "Organization exceeds BRSR requirements with advanced disclosures."}
        ],
        "faq": [
            {"q": "What is BRSR?", "a": "BRSR (Business Responsibility and Sustainability Reporting) is a SEBI-mandated disclosure framework for listed companies in India."},
            {"q": "Is BRSR mandatory?", "a": "Yes, for top 1000 listed companies by market capitalization. It is voluntary for others but recommended."},
            {"q": "How does certification help?", "a": "It validates that your organization's disclosures are comprehensive, accurate, and aligned with BRSR requirements."},
            {"q": "How long does the process take?", "a": "Typically 4-8 weeks depending on data readiness."}
        ]
    },
    "csr-impact": {
        "title": "CSR Impact Certification",
        "category": "esg",
        "icon": "heart",
        "short": "Validate the effectiveness and impact of your Corporate Social Responsibility initiatives.",
        "applicable": "CSR Impact Certification validates the effectiveness, transparency, and social impact of an organization's Corporate Social Responsibility programs.",
        "suitable_for": [
            "Companies with mandatory CSR obligations", "Corporates running CSR programs",
            "NGOs and implementation partners", "CSR foundations and trusts",
            "Companies seeking CSR credibility"
        ],
        "applicable_note": "Any organization seeking to validate and enhance the impact of its CSR programs can apply.",
        "criteria": [
            {"title": "Program Design & Alignment", "items": ["CSR policy and strategy", "Alignment with SDGs and national priorities", "Stakeholder needs assessment", "Program planning and budgeting"]},
            {"title": "Implementation Quality", "items": ["Execution effectiveness", "Community engagement", "Partner management", "Resource utilization"]},
            {"title": "Impact Measurement", "items": ["Outcome tracking and reporting", "Beneficiary feedback systems", "Social impact metrics", "Long-term sustainability of initiatives"]},
            {"title": "Governance & Transparency", "items": ["CSR committee oversight", "Financial transparency", "Compliance with Section 135", "Public reporting and disclosures"]}
        ],
        "criteria_note": "CSR programs are evaluated for design quality, implementation effectiveness, and measurable social impact.",
        "process": [
            {"step": "Application", "desc": "Organization submits CSR program details and impact data."},
            {"step": "Documentation Review", "desc": "Evaluation of CSR policies, budgets, and program documentation."},
            {"step": "Impact Assessment", "desc": "Expert evaluation of program outcomes, beneficiary impact, and social value."},
            {"step": "Scoring & Review", "desc": "Program receives impact score and evaluation report."},
            {"step": "Certification Issuance", "desc": "Approved organizations receive CSR Impact Certificate and Digital Badge."},
            {"step": "Annual Review", "desc": "Periodic review ensures continued CSR effectiveness."}
        ],
        "benefits": [
            {"title": "Social Benefits", "items": ["Validates community impact", "Encourages effective CSR programs", "Supports sustainable development goals"]},
            {"title": "Business Benefits", "items": ["Enhances stakeholder trust", "Improves CSR reporting credibility", "Demonstrates social commitment"]},
            {"title": "Brand Benefits", "items": ["Positive public perception", "Differentiates from competitors", "Attracts socially conscious partners"]},
            {"title": "Compliance Benefits", "items": ["Section 135 compliance support", "Improved CSR governance", "Transparent impact reporting"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "CSR Compliant", "score": "", "focus": "Basic CSR implementation", "desc": "Organization meets mandatory CSR requirements."},
            {"name": "Silver", "label": "CSR Effective", "score": "", "focus": "Structured programs with measurable outcomes", "desc": "Organization demonstrates structured and effective CSR programs."},
            {"name": "Gold", "label": "CSR Leader", "score": "", "focus": "High-impact sustainable programs", "desc": "Organization shows strong social impact and community engagement."},
            {"name": "Platinum", "label": "CSR Champion", "score": "", "focus": "Transformative social impact", "desc": "Organization sets benchmarks in CSR effectiveness and innovation."}
        ],
        "faq": [
            {"q": "What is CSR Impact Certification?", "a": "It validates that an organization's CSR programs are well-designed, effectively implemented, and create measurable social impact."},
            {"q": "Is CSR certification mandatory?", "a": "No, but it enhances credibility and transparency of CSR programs."},
            {"q": "Can NGOs apply?", "a": "Yes. NGOs and CSR implementation partners can also seek certification for their programs."},
            {"q": "How long does certification take?", "a": "Typically 4-6 weeks depending on program complexity."}
        ]
    },
    "green-manufacturing": {
        "title": "Green Manufacturing Certification",
        "category": "industry",
        "icon": "factory",
        "short": "Reduce environmental impact, improve resource efficiency, and adopt sustainable manufacturing practices.",
        "applicable": "Green Manufacturing Certification is designed for industrial units and production facilities that aim to reduce environmental impact, improve resource efficiency, and adopt sustainable manufacturing practices.",
        "suitable_for": [
            "Small, Medium, and Large Manufacturing Units", "Engineering & Industrial Plants",
            "Textile & Garment Manufacturers", "Food Processing Units",
            "Chemical & Pharmaceutical Plants", "Automotive & Component Manufacturers",
            "Packaging & Plastic Units", "Electronics & Electrical Manufacturers"
        ],
        "applicable_note": "Any manufacturing organization seeking efficient, compliant, and sustainable operations can apply.",
        "criteria": [
            {"title": "Environmental Performance", "items": ["Energy consumption and efficiency", "Renewable energy adoption", "Emission control systems", "Waste generation and disposal practices", "Water consumption and recycling"]},
            {"title": "Production Efficiency", "items": ["Resource utilization efficiency", "Process optimization", "Lean manufacturing practices", "Material waste reduction", "Sustainable procurement policies"]},
            {"title": "Pollution & Compliance", "items": ["Air, water, and soil pollution control", "Hazardous waste handling systems", "Compliance with environmental regulations", "Environmental monitoring and reporting"]},
            {"title": "Workplace Sustainability", "items": ["Worker health and safety systems", "Occupational safety compliance", "Training and awareness programs", "Responsible supply chain practices"]}
        ],
        "criteria_note": "Facilities receive a sustainability score based on structured evaluation benchmarks.",
        "process": [
            {"step": "Application", "desc": "Submission of plant details, production processes, and environmental compliance information."},
            {"step": "Documentation Review", "desc": "Evaluation of energy data, environmental permits, safety policies, and waste management practices."},
            {"step": "Plant Sustainability Audit", "desc": "Experts conduct site inspection, process evaluation, resource efficiency assessment, and compliance verification."},
            {"step": "Scoring & Gap Analysis", "desc": "The facility receives a sustainability performance report with improvement recommendations."},
            {"step": "Certification Review", "desc": "Independent certification committee validates findings."},
            {"step": "Certification Issuance", "desc": "Successful facilities receive Green Manufacturing Certificate, Digital Badge, and authorization to use certification seal."},
            {"step": "Periodic Monitoring", "desc": "Annual review or surveillance audit ensures continued compliance."}
        ],
        "benefits": [
            {"title": "Environmental Benefits", "items": ["Reduced energy, water, and resource consumption", "Lower emissions and environmental impact", "Improved waste recycling and pollution control"]},
            {"title": "Business Benefits", "items": ["Cost savings through efficiency improvements", "Better eligibility for global supply chains", "Increased attractiveness to ESG investors", "Improved tender qualification"]},
            {"title": "Brand Benefits", "items": ["Demonstrates responsible manufacturing practices", "Builds trust with customers and stakeholders", "Enhances export competitiveness"]},
            {"title": "Compliance Benefits", "items": ["Strengthens environmental compliance systems", "Reduces regulatory risks and penalties", "Preparedness for future sustainability regulations"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "Compliant Facility", "score": "", "focus": "Regulatory compliance and monitoring", "desc": "Facility meets basic environmental compliance requirements."},
            {"name": "Silver", "label": "Efficient Facility", "score": "", "focus": "Efficiency, waste reduction, monitoring systems", "desc": "Facility demonstrates resource efficiency improvements and structured sustainability practices."},
            {"name": "Gold", "label": "Sustainable Manufacturing Facility", "score": "", "focus": "Renewable adoption, optimized processes, environmental leadership", "desc": "Facility integrates strong sustainability measures across energy, water, and processes."},
            {"name": "Platinum", "label": "Green Leader Facility", "score": "", "focus": "Innovation, circular production, long-term sustainability strategy", "desc": "Facility demonstrates industry-leading sustainable manufacturing practices and measurable environmental impact reduction."}
        ],
        "faq": [
            {"q": "What is Green Manufacturing Certification?", "a": "It validates that a manufacturing facility operates using environmentally responsible, efficient, and compliant production practices."},
            {"q": "Does certification require a plant visit?", "a": "Yes. Site inspection is usually required to assess operational practices and environmental controls."},
            {"q": "Can small factories apply?", "a": "Yes. MSMEs can benefit significantly by improving efficiency and compliance."},
            {"q": "Will certification help with exports?", "a": "Yes. Many international buyers prefer certified sustainable manufacturing partners."},
            {"q": "How long does certification take?", "a": "Typically 4-8 weeks depending on facility size and data availability."},
            {"q": "How long is certification valid?", "a": "Usually one year, subject to periodic review."}
        ]
    },
    "sustainable-supply-chain": {
        "title": "Sustainable Supply Chain Certification",
        "category": "industry",
        "icon": "link",
        "short": "Ensure responsible sourcing, ethical procurement, and environmentally conscious logistics.",
        "applicable": "Sustainable Supply Chain Certification is designed for organizations that want to ensure responsible sourcing, ethical procurement, and environmentally conscious logistics across their supplier network.",
        "suitable_for": [
            "Manufacturing Companies with multi-tier suppliers", "Export-Oriented Businesses",
            "Retail Chains & Consumer Brands", "Infrastructure & Construction Companies",
            "FMCG & Apparel Companies", "E-commerce and Logistics Firms",
            "Automotive & Electronics Supply Networks", "Corporates with ESG reporting requirements"
        ],
        "applicable_note": "Any organization seeking to improve transparency, reduce risk, and build resilient supply chains can apply.",
        "criteria": [
            {"title": "Environmental Responsibility", "items": ["Sustainable sourcing policies", "Supplier environmental compliance", "Carbon footprint monitoring across logistics", "Packaging and material sustainability", "Transport efficiency initiatives"]},
            {"title": "Social & Ethical Standards", "items": ["Labour compliance across suppliers", "Workplace safety in supply chain operations", "Ethical sourcing and anti-child labour practices", "Fair wage and diversity policies", "Supplier code of conduct implementation"]},
            {"title": "Governance & Risk Controls", "items": ["Supplier due diligence processes", "ESG risk screening mechanisms", "Transparency in procurement practices", "Anti-corruption and ethical procurement policies", "Supply chain traceability systems"]}
        ],
        "criteria_note": "Organizations receive a structured score reflecting supply chain sustainability maturity.",
        "process": [
            {"step": "Application", "desc": "Organization submits procurement structure, supplier network overview, and sourcing policies."},
            {"step": "Documentation Review", "desc": "Evaluation of supplier policies, ESG guidelines, procurement contracts, and logistics data."},
            {"step": "Supply Chain Assessment", "desc": "Experts conduct supplier governance evaluation, procurement policy review, logistics sustainability analysis, and supplier sampling."},
            {"step": "Risk & Gap Analysis", "desc": "The organization receives a supply chain sustainability scorecard with improvement recommendations."},
            {"step": "Certification Committee Review", "desc": "Independent panel validates the findings."},
            {"step": "Certification Issuance", "desc": "Approved organizations receive Sustainable Supply Chain Certificate, Digital Badge, and Listing in public registry."},
            {"step": "Periodic Monitoring", "desc": "Annual review ensures continued compliance and supplier governance."}
        ],
        "benefits": [
            {"title": "Environmental Benefits", "items": ["Encourages eco-friendly sourcing", "Reduces logistics-related emissions", "Promotes sustainable material usage"]},
            {"title": "Business Benefits", "items": ["Reduces supplier-related operational risks", "Improves supply chain resilience", "Enhances vendor credibility in global markets", "Strengthens eligibility for international contracts"]},
            {"title": "Brand Benefits", "items": ["Demonstrates ethical sourcing commitment", "Builds trust with customers and investors", "Supports sustainability reporting"]},
            {"title": "Compliance Benefits", "items": ["Alignment with ESG supply chain requirements", "Preparedness for international due diligence norms", "Reduced reputational and legal risks"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "Responsible Supply Chain", "score": "", "focus": "Foundational governance and monitoring", "desc": "Basic supplier policies and compliance checks in place."},
            {"name": "Silver", "label": "Managed Supply Chain", "score": "", "focus": "Supplier audits, traceability, sustainability reporting", "desc": "Structured ESG criteria applied to supplier selection and monitoring."},
            {"name": "Gold", "label": "Sustainable Supply Chain", "score": "", "focus": "Responsible sourcing, carbon tracking, supplier engagement", "desc": "Strong ESG integration across procurement, sourcing, and logistics."},
            {"name": "Platinum", "label": "Supply Chain Leader", "score": "", "focus": "End-to-end traceability and strategic ESG integration", "desc": "Industry-leading transparency, ethical sourcing systems, and sustainable logistics innovation."}
        ],
        "faq": [
            {"q": "What is Sustainable Supply Chain Certification?", "a": "It validates that an organization manages its sourcing, procurement, and logistics responsibly using ESG-aligned practices."},
            {"q": "Does certification require supplier audits?", "a": "In some cases yes. Supplier sampling or documentation verification may be conducted."},
            {"q": "Is certification useful for exporters?", "a": "Yes. Many global buyers expect ethical sourcing and transparent supply chains."},
            {"q": "Can small companies apply?", "a": "Yes. Even MSMEs with limited suppliers can benefit by implementing structured procurement policies."},
            {"q": "How long does certification take?", "a": "Typically 4-8 weeks depending on supply chain complexity."}
        ]
    },
    "green-real-estate": {
        "title": "Green Real Estate Certification",
        "category": "industry",
        "icon": "building",
        "short": "Construct, operate, or manage buildings in an environmentally responsible and resource-efficient manner.",
        "applicable": "Green Real Estate Certification is designed for developers, builders, and property owners who aim to construct, operate, or manage buildings in an environmentally responsible and resource-efficient manner.",
        "suitable_for": [
            "Residential Real Estate Projects", "Commercial Buildings & Office Parks",
            "IT Parks & Business Campuses", "Shopping Malls & Retail Complexes",
            "Hotels & Hospitality Projects", "Industrial Parks & Warehouses",
            "Educational Institutions & Hospitals", "Government & Infrastructure Projects"
        ],
        "applicable_note": "Any project seeking sustainable design, efficient operations, and enhanced environmental performance can apply.",
        "criteria": [
            {"title": "Environmental Design & Planning", "items": ["Energy-efficient building design", "Natural lighting and ventilation planning", "Renewable energy integration (solar, etc.)", "Heat island reduction strategies"]},
            {"title": "Water Management", "items": ["Rainwater harvesting systems", "Water-efficient fixtures", "Wastewater treatment and reuse", "Landscape water conservation"]},
            {"title": "Resource & Material Sustainability", "items": ["Use of eco-friendly construction materials", "Waste reduction during construction", "Recyclable and low-impact materials", "Sustainable procurement practices"]},
            {"title": "Indoor Environmental Quality", "items": ["Air quality standards", "Natural ventilation systems", "Low-emission construction materials", "Occupant health and comfort measures"]},
            {"title": "Governance & Compliance", "items": ["Environmental approvals and compliance", "Sustainable facility management practices", "Monitoring and reporting systems"]}
        ],
        "criteria_note": "Projects receive a sustainability score reflecting overall green performance.",
        "process": [
            {"step": "Application", "desc": "Developer submits project details, architectural plans, and sustainability features."},
            {"step": "Design Review", "desc": "Assessment of building plans, energy design, water systems, and material specifications."},
            {"step": "Construction/Operational Assessment", "desc": "Experts evaluate implementation of sustainability measures during construction or operation."},
            {"step": "Site Inspection", "desc": "Physical verification of systems, infrastructure, and environmental controls."},
            {"step": "Scoring & Certification Review", "desc": "Project receives sustainability score and evaluation report."},
            {"step": "Certification Issuance", "desc": "Successful projects receive Green Real Estate Certificate, Digital Badge for marketing, and authorization to use certification mark."},
            {"step": "Periodic Monitoring", "desc": "Operational projects may undergo periodic review to maintain certification validity."}
        ],
        "benefits": [
            {"title": "Environmental Benefits", "items": ["Reduced energy and water consumption", "Lower operational carbon footprint", "Sustainable resource utilization"]},
            {"title": "Business & Financial Benefits", "items": ["Increased property valuation and market appeal", "Higher occupancy and tenant preference", "Operational cost savings through efficiency", "Improved eligibility for green financing"]},
            {"title": "Brand & Market Benefits", "items": ["Demonstrates commitment to sustainable development", "Strengthens developer reputation", "Enhances attractiveness to global investors and tenants"]},
            {"title": "Compliance Benefits", "items": ["Supports environmental approvals and sustainability disclosures", "Reduces regulatory risks", "Preparedness for future green building norms"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "Green Compliant Project", "score": "", "focus": "Regulatory compliance and initial sustainability practices", "desc": "Project meets basic environmental compliance and efficiency measures."},
            {"name": "Silver", "label": "Efficient Green Project", "score": "", "focus": "Energy, water, and material efficiency", "desc": "Project demonstrates structured sustainability systems and measurable efficiency improvements."},
            {"name": "Gold", "label": "Sustainable Green Project", "score": "", "focus": "Renewable adoption, resource optimization, environmental leadership", "desc": "Project integrates strong green design and operational sustainability measures."},
            {"name": "Platinum", "label": "Green Landmark Project", "score": "", "focus": "Net-zero potential, smart infrastructure, long-term sustainability strategy", "desc": "Project demonstrates industry-leading sustainability performance and innovation."}
        ],
        "faq": [
            {"q": "What is Green Real Estate Certification?", "a": "It validates that a building or real estate project is designed, constructed, and operated using environmentally responsible practices."},
            {"q": "Can existing buildings apply?", "a": "Yes. Both new and operational buildings can be assessed and certified."},
            {"q": "Does certification require site inspection?", "a": "Yes. Site inspection is typically conducted to verify sustainability measures."},
            {"q": "Will certification improve property value?", "a": "Yes. Certified green buildings often attract higher occupancy, better tenants, and improved investor interest."},
            {"q": "How long does certification take?", "a": "Usually 6-10 weeks depending on project size and documentation readiness."}
        ]
    },
    "green-hospitality": {
        "title": "Green Hospitality Certification",
        "category": "industry",
        "icon": "hotel",
        "short": "Operate hotels, resorts, and hospitality businesses in an environmentally responsible manner.",
        "applicable": "Green Hospitality Certification is designed for hotels, resorts, restaurants, and hospitality businesses that aim to operate in an environmentally responsible, resource-efficient, and socially responsible manner.",
        "suitable_for": [
            "Hotels & Resorts", "Boutique Hotels & Homestays", "Restaurants & Cafes",
            "Banquet & Event Venues", "Tourism & Eco-Resorts", "Cruise & Travel Hospitality Operators",
            "Corporate Guest Houses", "Wellness Retreats & Spas"
        ],
        "applicable_note": "Any hospitality business seeking to reduce environmental impact and enhance sustainability credibility can apply.",
        "criteria": [
            {"title": "Energy & Environmental Management", "items": ["Energy-efficient lighting and equipment", "Renewable energy adoption (solar, etc.)", "Carbon footprint monitoring", "Sustainable building operations"]},
            {"title": "Water Management", "items": ["Water-efficient fixtures", "Laundry water optimization", "Rainwater harvesting systems", "Wastewater treatment and reuse"]},
            {"title": "Waste & Resource Management", "items": ["Food waste reduction practices", "Recycling and composting systems", "Sustainable procurement policies", "Reduction of single-use plastics"]},
            {"title": "Social Responsibility & Guest Awareness", "items": ["Staff sustainability training", "Community sourcing and local employment", "Guest awareness initiatives (towel reuse, etc.)", "Ethical sourcing of food and materials"]},
            {"title": "Governance & Compliance", "items": ["Environmental compliance and monitoring", "Sustainability reporting systems", "Health and safety standards"]}
        ],
        "criteria_note": "Hotels receive a sustainability score reflecting operational and environmental performance.",
        "process": [
            {"step": "Application", "desc": "Hospitality business submits operational details, infrastructure information, and sustainability practices."},
            {"step": "Documentation Review", "desc": "Evaluation of energy use, procurement practices, waste management, and compliance records."},
            {"step": "Sustainability Assessment", "desc": "Experts conduct operational evaluation, infrastructure review, and guest service sustainability practices assessment."},
            {"step": "Site Inspection", "desc": "Physical verification of systems, waste handling, water management, and energy efficiency measures."},
            {"step": "Scoring & Certification Review", "desc": "The establishment receives a sustainability performance score."},
            {"step": "Certification Issuance", "desc": "Approved establishments receive Green Hospitality Certificate, Digital Badge, and authorization to display certification seal."},
            {"step": "Periodic Monitoring", "desc": "Annual review ensures continued sustainability compliance."}
        ],
        "benefits": [
            {"title": "Environmental Benefits", "items": ["Reduced energy and water consumption", "Lower waste generation and environmental impact", "Improved sustainable sourcing practices"]},
            {"title": "Business Benefits", "items": ["Cost savings from efficient resource use", "Increased appeal to eco-conscious travelers", "Higher corporate and international bookings", "Better eligibility for sustainable tourism programs"]},
            {"title": "Brand Benefits", "items": ["Demonstrates responsible tourism practices", "Enhances reputation and trust", "Differentiates property from competitors"]},
            {"title": "Compliance Benefits", "items": ["Supports environmental and safety compliance", "Reduces operational risks", "Strengthens ESG reporting credibility"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "Responsible Hospitality Property", "score": "", "focus": "Compliance and monitoring", "desc": "Basic sustainability practices and compliance measures in place."},
            {"name": "Silver", "label": "Sustainable Hospitality Property", "score": "", "focus": "Resource efficiency, waste reduction, guest engagement", "desc": "Structured sustainability initiatives implemented with measurable efficiency improvements."},
            {"name": "Gold", "label": "Green Hospitality Leader", "score": "", "focus": "Renewable adoption, responsible sourcing, environmental leadership", "desc": "Strong sustainability integration across operations and infrastructure."},
            {"name": "Platinum", "label": "Eco-Leader Hospitality Property", "score": "", "focus": "Net-zero potential, circular operations, sustainability innovation", "desc": "Industry-leading sustainable hospitality practices and measurable environmental impact reduction."}
        ],
        "faq": [
            {"q": "What is Green Hospitality Certification?", "a": "It validates that a hospitality establishment operates using environmentally responsible, efficient, and sustainable practices."},
            {"q": "Can small hotels or homestays apply?", "a": "Yes. Certification is suitable for businesses of all sizes."},
            {"q": "Does certification require site inspection?", "a": "Yes. Physical inspection is typically conducted to verify sustainability measures."},
            {"q": "Will certification help attract international guests?", "a": "Yes. Many travelers and corporate clients prefer environmentally responsible accommodations."},
            {"q": "How long does certification take?", "a": "Usually 4-8 weeks depending on property size and documentation readiness."}
        ]
    },
    "sustainable-agriculture": {
        "title": "Sustainable Agriculture Certification",
        "category": "industry",
        "icon": "wheat",
        "short": "Adopt environmentally responsible, resource-efficient, and socially ethical farming practices.",
        "applicable": "Sustainable Agriculture Compliance Certification is designed for farms, agribusinesses, and agricultural supply chains that aim to adopt environmentally responsible, resource-efficient, and socially ethical farming practices.",
        "suitable_for": [
            "Individual Farmers & Farmer Producer Organizations (FPOs)", "Commercial Farms & Plantation Owners",
            "Agri-Exporters & Food Processing Companies", "Organic & Natural Farming Units",
            "Dairy, Poultry & Livestock Operations", "Agri-Cooperatives & Contract Farming Networks",
            "Seed Producers & Input Companies", "Agritech & Sustainable Farming Startups"
        ],
        "applicable_note": "Any agricultural entity seeking to improve soil health, resource efficiency, and market credibility can apply.",
        "criteria": [
            {"title": "Environmental Sustainability", "items": ["Soil health management practices", "Responsible fertilizer and pesticide usage", "Water conservation and irrigation efficiency", "Biodiversity protection and ecosystem care", "Climate-resilient farming practices"]},
            {"title": "Resource Efficiency", "items": ["Efficient water usage and irrigation systems", "Renewable energy usage where applicable", "Waste management and composting systems", "Sustainable crop rotation and land use"]},
            {"title": "Social & Ethical Practices", "items": ["Fair labour practices and worker welfare", "Safe handling of agro-chemicals", "Community engagement and rural development", "Traceability and ethical sourcing"]},
            {"title": "Compliance & Governance", "items": ["Compliance with agricultural and environmental regulations", "Record-keeping and farm monitoring systems", "Traceability and supply chain transparency"]}
        ],
        "criteria_note": "Farms receive a sustainability score reflecting their environmental and operational performance.",
        "process": [
            {"step": "Application", "desc": "Farm or agribusiness submits operational details, crop information, and farming practices."},
            {"step": "Documentation Review", "desc": "Evaluation of farm records, input usage, irrigation methods, and compliance documents."},
            {"step": "Field Assessment", "desc": "Experts conduct farm visit and land assessment, soil and water management evaluation, review of chemical usage, and worker safety assessment."},
            {"step": "Scoring & Gap Analysis", "desc": "The farm receives a sustainability performance scorecard with improvement recommendations."},
            {"step": "Certification Committee Review", "desc": "Independent panel validates findings and approves certification."},
            {"step": "Certification Issuance", "desc": "Approved farms receive Sustainable Agriculture Certificate, Digital Badge, and authorization to use certification mark."},
            {"step": "Periodic Monitoring", "desc": "Annual review ensures continued compliance with sustainable farming practices."}
        ],
        "benefits": [
            {"title": "Environmental Benefits", "items": ["Improves soil fertility and long-term farm productivity", "Reduces water consumption and chemical impact", "Protects biodiversity and local ecosystems"]},
            {"title": "Business Benefits", "items": ["Enhances export credibility and buyer trust", "Improves access to sustainable and premium markets", "Strengthens eligibility for agri-financing and sustainability programs"]},
            {"title": "Brand & Market Benefits", "items": ["Builds trust with consumers and global buyers", "Demonstrates responsible farming practices", "Supports traceability and sustainable sourcing claims"]},
            {"title": "Compliance Benefits", "items": ["Strengthens regulatory compliance and documentation", "Reduces environmental and reputational risks", "Supports ESG reporting for agri-supply chains"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "Responsible Farm", "score": "", "focus": "Regulatory compliance and record-keeping", "desc": "Farm meets basic compliance and monitoring standards."},
            {"name": "Silver", "label": "Sustainable Farm", "score": "", "focus": "Efficiency, reduced chemical impact, conservation", "desc": "Farm implements structured soil, water, and resource management practices."},
            {"name": "Gold", "label": "Advanced Sustainable Farm", "score": "", "focus": "Biodiversity protection, renewable inputs, traceability", "desc": "Farm integrates strong ecological and resource-efficient farming practices."},
            {"name": "Platinum", "label": "Regenerative Agriculture Leader", "score": "", "focus": "Soil restoration, ecosystem enhancement, climate-positive farming", "desc": "Farm demonstrates industry-leading sustainable and regenerative practices."}
        ],
        "faq": [
            {"q": "What is Sustainable Agriculture Compliance Certification?", "a": "It validates that a farm or agribusiness follows environmentally responsible, resource-efficient, and ethical farming practices."},
            {"q": "Is this certification the same as organic certification?", "a": "No. Organic certification focuses on chemical-free farming, while sustainable agriculture certification evaluates broader environmental, social, and operational sustainability."},
            {"q": "Can small farmers apply?", "a": "Yes. Individual farmers, cooperatives, and FPOs can all apply."},
            {"q": "Does certification require farm inspection?", "a": "Yes. Field visits are usually conducted to verify farming practices and compliance."},
            {"q": "Can certification help with exports?", "a": "Yes. Many international buyers prefer sustainably sourced agricultural products."}
        ]
    },
    "sustainable-product": {
        "title": "Sustainable Product Certification",
        "category": "product",
        "icon": "package",
        "short": "Demonstrate that products are environmentally responsible, ethically sourced, and resource-efficient.",
        "applicable": "Sustainable Product Certification is designed for manufacturers, brands, and exporters who want to demonstrate that their products are environmentally responsible, ethically sourced, and resource-efficient throughout their lifecycle.",
        "suitable_for": [
            "Manufacturing Companies", "Consumer Goods Brands", "Export-Oriented Units",
            "Packaging Manufacturers", "Textile & Apparel Companies", "FMCG & Retail Brands",
            "Construction Material Producers", "Furniture & Home Product Manufacturers",
            "Startups launching eco-friendly products"
        ],
        "applicable_note": "Any business that wants to showcase product-level sustainability and gain market credibility can apply.",
        "criteria": [
            {"title": "Environmental Impact", "items": ["Raw material sourcing practices", "Use of recycled or renewable materials", "Energy efficiency in manufacturing", "Waste generation and recyclability", "Packaging sustainability"]},
            {"title": "Production Practices", "items": ["Resource efficiency in production", "Pollution control measures", "Water usage management", "Compliance with environmental norms"]},
            {"title": "Ethical & Social Responsibility", "items": ["Ethical sourcing of materials", "Safe working conditions in production", "Compliance with labour regulations", "Responsible supply chain practices"]},
            {"title": "Product Lifecycle & End-of-Life", "items": ["Durability and product life", "Recyclability or biodegradability", "Circular economy compatibility", "Disposal impact"]}
        ],
        "criteria_note": "Products receive a sustainability score based on standardized evaluation benchmarks.",
        "process": [
            {"step": "Application", "desc": "Manufacturer submits product details, materials information, and production process overview."},
            {"step": "Documentation Review", "desc": "Evaluation of sourcing records, production practices, environmental compliance, and packaging details."},
            {"step": "Product Sustainability Assessment", "desc": "Experts review material composition, manufacturing impact, supply chain practices, and product lifecycle sustainability."},
            {"step": "Testing & Validation", "desc": "Independent lab tests or supplier verification may be conducted where necessary."},
            {"step": "Scoring & Review", "desc": "Product receives a sustainability score and evaluation report."},
            {"step": "Certification Issuance", "desc": "Approved products receive Sustainable Product Certificate, Eco Product Label/Badge, and authorization to use certification mark on packaging."},
            {"step": "Periodic Review", "desc": "Certification remains valid for a defined period subject to compliance checks."}
        ],
        "benefits": [
            {"title": "Environmental Benefits", "items": ["Encourages responsible production practices", "Promotes resource-efficient manufacturing", "Reduces environmental footprint of products"]},
            {"title": "Market & Brand Benefits", "items": ["Builds consumer trust and transparency", "Differentiates product in competitive markets", "Supports eco-conscious branding and packaging claims", "Enhances export acceptance"]},
            {"title": "Business Benefits", "items": ["Improves access to sustainability-focused retailers", "Supports ESG reporting at product level", "Increases attractiveness to global buyers"]},
            {"title": "Compliance Benefits", "items": ["Supports environmental labelling requirements", "Preparedness for future product sustainability regulations", "Reduces greenwashing risks through independent validation"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "Responsible Product", "score": "", "focus": "Compliance and initial sustainability efforts", "desc": "Product meets basic environmental and compliance requirements."},
            {"name": "Silver", "label": "Sustainable Product", "score": "", "focus": "Resource efficiency and responsible sourcing", "desc": "Product demonstrates measurable improvements in materials, packaging, or manufacturing efficiency."},
            {"name": "Gold", "label": "Advanced Sustainable Product", "score": "", "focus": "Circular design, recyclable materials, reduced emissions", "desc": "Product integrates strong lifecycle sustainability practices and reduced environmental footprint."},
            {"name": "Platinum", "label": "Eco-Leader Product", "score": "", "focus": "Innovation-driven sustainability leadership", "desc": "Product sets industry benchmark in sustainability, circular economy design, and environmental impact reduction."}
        ],
        "faq": [
            {"q": "What is Sustainable Product Certification?", "a": "It validates that a product meets defined environmental, ethical, and lifecycle sustainability standards."},
            {"q": "Is certification applicable to all products?", "a": "Yes, provided sufficient data on materials, manufacturing, and lifecycle impact is available."},
            {"q": "Does certification require lab testing?", "a": "Testing may be required for certain materials, environmental claims, or compliance verification."},
            {"q": "Can certification help with exports?", "a": "Yes. Sustainability certification improves acceptance in international markets where eco-standards are increasingly required."},
            {"q": "Can companies certify multiple products?", "a": "Yes. Each product or product line can be certified separately."},
            {"q": "Can the certification mark be used on packaging?", "a": "Yes. Certified products receive permission to display the certification logo on packaging and marketing materials."}
        ]
    },
    "sustainable-packaging": {
        "title": "Sustainable Packaging Certification",
        "category": "product",
        "icon": "box",
        "short": "Reduce environmental impact through responsible material selection and lifecycle-conscious packaging.",
        "applicable": "Sustainable Packaging Certification is designed for manufacturers, brands, and packaging suppliers that aim to reduce environmental impact through responsible material selection, efficient design, and lifecycle-conscious packaging solutions.",
        "suitable_for": [
            "FMCG & Consumer Product Brands", "Food & Beverage Manufacturers",
            "E-commerce & Retail Companies", "Packaging Manufacturers & Converters",
            "Pharmaceutical & Cosmetic Companies", "Export-Oriented Businesses",
            "Logistics & Distribution Companies", "Startups launching eco-friendly products"
        ],
        "applicable_note": "Any organization seeking to improve packaging sustainability and reduce waste footprint can apply.",
        "criteria": [
            {"title": "Material Sustainability", "items": ["Use of recyclable or biodegradable materials", "Use of recycled content", "Reduction of virgin plastic usage", "Sustainable sourcing of packaging materials"]},
            {"title": "Design Efficiency", "items": ["Lightweight packaging design", "Minimal material usage", "Space-efficient logistics design", "Reusability or refillability options"]},
            {"title": "Waste & Circularity", "items": ["Ease of recyclability", "Compostability where applicable", "Reverse logistics or take-back programs", "Compatibility with circular economy practices"]},
            {"title": "Compliance & Labelling", "items": ["Environmental labelling accuracy", "Compliance with packaging regulations", "Waste management and disposal guidance", "Traceability of packaging materials"]}
        ],
        "criteria_note": "Packaging receives a sustainability score based on structured evaluation benchmarks.",
        "process": [
            {"step": "Application", "desc": "Organization submits packaging specifications, material composition, and supply chain information."},
            {"step": "Documentation Review", "desc": "Evaluation of material sourcing, recyclability data, compliance records, and packaging design details."},
            {"step": "Packaging Sustainability Assessment", "desc": "Experts review material lifecycle impact, production footprint, logistics efficiency, and end-of-life recyclability."},
            {"step": "Testing & Validation", "desc": "Independent lab tests or supplier verification may be conducted for material claims."},
            {"step": "Scoring & Certification Review", "desc": "Packaging system receives a sustainability score and evaluation report."},
            {"step": "Certification Issuance", "desc": "Approved organizations receive Sustainable Packaging Certificate, Eco Packaging Label/Badge, and authorization to display certification mark."},
            {"step": "Periodic Review", "desc": "Certification remains valid for a defined period subject to compliance verification."}
        ],
        "benefits": [
            {"title": "Environmental Benefits", "items": ["Reduces packaging waste and landfill impact", "Encourages recyclable and circular packaging solutions", "Lowers material and transport emissions"]},
            {"title": "Business Benefits", "items": ["Improves efficiency in logistics and storage", "Supports compliance with global packaging regulations", "Enhances attractiveness to sustainability-focused retailers", "Strengthens eligibility for export markets"]},
            {"title": "Brand Benefits", "items": ["Builds consumer trust and transparency", "Supports eco-friendly product positioning", "Differentiates brand in competitive markets"]},
            {"title": "Compliance Benefits", "items": ["Preparedness for extended producer responsibility (EPR) norms", "Reduced regulatory risks", "Supports ESG and sustainability reporting"]}
        ],
        "levels": [
            {"name": "Bronze", "label": "Responsible Packaging", "score": "", "focus": "Compliance and initial sustainability measures", "desc": "Packaging meets basic environmental compliance and recyclability standards."},
            {"name": "Silver", "label": "Sustainable Packaging", "score": "", "focus": "Reduced plastic use, recyclable design", "desc": "Packaging demonstrates improved material efficiency and recyclability."},
            {"name": "Gold", "label": "Advanced Sustainable Packaging", "score": "", "focus": "Reusable, compostable, or low-carbon materials", "desc": "Packaging integrates circular economy principles and significant environmental impact reduction."},
            {"name": "Platinum", "label": "Circular Packaging Leader", "score": "", "focus": "Closed-loop systems, zero-waste design, material innovation", "desc": "Packaging demonstrates industry-leading innovation in circular design and minimal environmental footprint."}
        ],
        "faq": [
            {"q": "What is Sustainable Packaging Certification?", "a": "It validates that packaging systems are environmentally responsible, efficient, and aligned with lifecycle sustainability standards."},
            {"q": "Can individual products be certified?", "a": "Yes. Packaging for specific products or product lines can be assessed separately."},
            {"q": "Does certification require lab testing?", "a": "Testing may be required where environmental claims or material properties need verification."},
            {"q": "Can certification help with exports?", "a": "Yes. Many global markets require sustainable packaging compliance."},
            {"q": "How long does certification take?", "a": "Typically 3-6 weeks depending on packaging complexity."},
            {"q": "Can the certification label be used on packaging?", "a": "Yes. Certified packaging systems can display the certification mark."}
        ]
    }
}

# Category groupings for the certifications page
CERT_CATEGORIES = [
    {
        "id": "esg",
        "title": "ESG & Compliance Certifications",
        "desc": "Environmental, Social, and Governance compliance and reporting certifications.",
        "certs": ["esg-compliance", "esg-rating", "brsr-compliance", "csr-impact"]
    },
    {
        "id": "environmental",
        "title": "Environmental Certifications",
        "desc": "Certifications focused on carbon, water, and environmental impact management.",
        "certs": ["carbon-neutral", "water-neutral"]
    },
    {
        "id": "industry",
        "title": "Industry Certifications",
        "desc": "Sector-specific sustainability certifications for manufacturing, real estate, hospitality, agriculture, and supply chains.",
        "certs": ["green-manufacturing", "sustainable-supply-chain", "green-real-estate", "green-hospitality", "sustainable-agriculture"]
    },
    {
        "id": "product",
        "title": "Product & Resource Certifications",
        "desc": "Product-level and resource-focused sustainability certifications.",
        "certs": ["sustainable-product", "sustainable-packaging", "green-business"]
    }
]

INDUSTRIES = [
    {"name": "Manufacturing", "icon": "factory", "desc": "Green Manufacturing Certification helps industrial units reduce environmental impact, improve resource efficiency, and adopt sustainable production practices."},
    {"name": "Real Estate", "icon": "building", "desc": "Green Real Estate Certification supports developers and property owners in building and operating environmentally responsible, energy-efficient structures."},
    {"name": "Hospitality", "icon": "hotel", "desc": "Green Hospitality Certification enables hotels, resorts, and restaurants to operate sustainably while enhancing guest experience."},
    {"name": "Agriculture", "icon": "wheat", "desc": "Sustainable Agriculture Certification helps farms and agribusinesses adopt resource-efficient, ethical, and climate-resilient farming practices."},
    {"name": "Logistics & Supply Chain", "icon": "truck", "desc": "Sustainable Supply Chain Certification ensures responsible sourcing, ethical procurement, and environmentally conscious logistics."},
    {"name": "Corporates & Services", "icon": "briefcase", "desc": "ESG and Green Business Certifications help corporate offices and service companies demonstrate sustainability commitment and compliance readiness."},
    {"name": "Export Businesses", "icon": "globe", "desc": "Sustainability certifications strengthen export credibility, meet international buyer expectations, and open access to global green markets."}
]


@app.route("/")
def home():
    return render_template("home.html", certifications=CERTIFICATIONS, categories=CERT_CATEGORIES, industries=INDUSTRIES)


@app.route("/certifications")
def certifications():
    return render_template("certifications.html", certifications=CERTIFICATIONS, categories=CERT_CATEGORIES)


@app.route("/certification/<slug>")
def certification_detail(slug):
    cert = CERTIFICATIONS.get(slug)
    if not cert:
        abort(404)
    return render_template("certification_detail.html", cert=cert, slug=slug)


@app.route("/industries")
def industries():
    return render_template("industries.html", industries=INDUSTRIES, certifications=CERTIFICATIONS)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
