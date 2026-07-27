Competencies for Undergraduate Data Science Curricula  
Public Review Copy

## Table of Contents

[**Data Science Competency Schema	2**](#data-science-competency-schema)

[**Competency Areas	21**](#competency-areas)

[**Artificial Intelligence (AI)	21**](#artificial-intelligence-\(ai\))

[**Computing Algorithms (CA)	28**](#computing-algorithms-\(ca\))

[**Computing Fundamentals (CF)	32**](#computing-fundamentals-\(cf\))

[**Data Acquisition (DA)	41**](#data-acquisition-\(da\))

[**Data Storytelling (DS)	48**](#data-storytelling-\(ds\))

[**Exploratory Data Analysis (EDA)	54**](#exploratory-data-analysis-\(eda\))

[**Machine Learning (ML)	59**](#machine-learning-\(ml\))

[**Mathematical Fundamentals (MF)	68**](#mathematical-fundamentals-\(mf\))

[**Probability and Distributions (PD)	74**](#probability-and-distributions-\(pd\))

[**Professionalism and Ethics (PE)	79**](#professionalism-and-ethics-\(pe\))

[**Project Management (PM)	85**](#project-management-\(pm\))

[**Research Methods and Experimental Design (RM)	90**](#research-methods-and-experimental-design-\(rm\))

[**Software Engineering, Programming, Development (SW)	95**](#software-engineering,-programming,-development-\(sw\))

[**Statistical Fundamentals (SF)	101**](#statistical-fundamentals-\(sf\))

[**Statistical Modeling (SM)	108**](#statistical-modeling-\(sm\))

**Acknowledgements:**  
   
This ***Competencies for Undergraduate Data Science Curricula*** release is a continuation of the previously published ***Computing Competencies for Undergraduate Data Science Curricula***. \[ACM\]  As such, portions of this document make liberal use and revision of significant portions of the original work.  
   
\[ACM\] ACM Data Science Task Force. (2021). [*Computing competencies for undergraduate data science curricula*](https://www.google.com/search?client=safari&rls=en&q=Computing+competencies+for+undergraduate+data+science+curricula&ie=UTF-8&oe=UTF-8&ved=2ahUKEwjPrZX6uo6SAxVCHNAFHXPkNt0QgK4QegQIAxAC). Association for Computing Machinery, New York, NY, USA.  
 

# Data Science Competency Schema {#data-science-competency-schema}

**Competencies** are a structured, outcomes-oriented framework to define what learners in a discipline should *know*, *be able to do*, and *value* at various stages of their education and professional development. They are used to guide curriculum design, assessment, accreditation, and program comparison across various fields in data science.

**Definitions**

A **competency** is an integrated statement that combines:

1. **Knowledge** (disciplinary concepts and content),  
2. **Skills** (cognitive and practical abilities), and  
3. **Dispositions** (professional attitudes, behaviors, and ethical orientations)

to describe observable and assessable learner outcomes. These In contrast to content-only knowledge-based guidance, competencies emphasize capability and readiness for practice.  This integrated model can be shown graphically (See Figure 1\) with a competency being the intersection of the application of knowledge and skills using personal dispositions to perform a given task in data science.

![][image1]

Figure 1 – Competency Framework

**Core Components of Competencies**

**Competency Statements**

A **competency statement** for a data science Competency Area is a concise, outcomes-focused declaration that integrates **knowledge, skills, and dispositions** to describe what a graduate can reliably and responsibly do with that knowledge in practice. A data science competency statement is not a topic list. It is a performance claim: a defensible statement that a learner can apply knowledge skillfully, judiciously, and ethically in context.

In this report, a competency statement is a concise, natural-language expression that articulates the abilities and professional capabilities a learner attains through a course of study or is expected to demonstrate when performing data-driven tasks in academic, industry, or societal contexts. The statement summarizes what a data scientist can effectively and responsibly do, using language that is accessible and meaningful to a broad range of stakeholders, including students, educators, employers, and accreditation bodies.

Competency statements are intentionally written in plain, discipline-relevant language that reflects authentic data science practice and resonates with the intended audience. While they favor clarity and accessibility, competency statements are not standalone artifacts; they are structurally supported and elaborated by an associated competency specification that enumerates the underlying knowledge elements, skill levels, and professional dispositions required for successful performance.

Whereas the competency statement communicates outcomes at a high level, the competency specification provides a formal, component-level representation of the competency, detailing the knowledge domains, Bloom-aligned cognitive skills, and moderating dispositions necessary to demonstrate the capability in context. This structured decomposition is essential for curriculum design, assessment alignment, and computational analyses such as program comparison, coverage mapping, and visualization.

A well-formed competency statement typically includes:

1. **Action verb** (aligned with CC2020 / Bloom’s cognitive levels)  
2. **Knowledge domain** (what content area is being addressed)  
3. **Context or application** (where or how the competency is exercised)  
4. **Quality or constraint** (accuracy, ethics, scalability, uncertainty, etc.)  
5. **Professional disposition** (how the work is approached and judged)

**Formula:**  
*A learner can* **\[skill verb\]** *\[knowledge\] to* **\[perform task\]** *in* **\[context\]**, *demonstrating* \*\*\[dispositions/constraints\]\*.

**1\. Competency Areas and Knowledge Units**

**Knowledge** represents the *“know-what”* dimension of competency, encompassing a factual and conceptual understanding of the principles, methods, and theoretical foundations that underpin data-driven work. An element of knowledge identifies a **core concept** that is essential to competent practice in data science, such as statistical reasoning, algorithmic methods, data management principles, or ethical and legal considerations.

This dimension reflects the **disciplinary content** that educators organize as topics within course syllabi, academic units distributed across curricula, accreditation bodies reference in program requirements, and employers articulate in role expectations and job descriptions. In data science education, knowledge elements span multiple contributing disciplines—including statistics, computing, mathematics, and domain knowledge—and provide the conceptual basis upon which analytic and computational skills are developed.

Historically, curriculum guidelines in computing-related fields have emphasized knowledge elements defined as bodies of facts, principles, and models derived from scientific theory, mathematical proof, or empirical validation. In data science, this foundational knowledge remains essential; however, its value is realized most fully when it informs effective analysis, responsible decision-making, and principled application in real-world contexts.

In this model, **Competency Areas** (e.g., Machine Learning or Statistical Modeling) that are further divided into **knowledge units**. These specify the subject matter that learners are expected to master.

**2\. Skills (Cognitive Levels)**

Competencies incorporate **skill levels** aligned with cognitive frameworks such as Bloom’s taxonomy, using verbs articulated in ACM’s CC2020 framework:

* Remembering  
* Understanding  
* Applying  
* Analyzing  
* Evaluating  
* Creating

In data science, **skills** refer to the capacity and strategy for applying knowledge to effectively perform data-driven tasks across the analytic lifecycle. Skills represent the *“know-how”* dimension of competency, encompassing the practical application of statistical, computational, and ethical knowledge to real-world data problems.

Skill development in data science occurs progressively through repeated practice and exposure to increasingly complex scenarios. As such, the acquisition of data science skills typically requires engagement with a hierarchy of higher-order cognitive processes, including analysis, evaluation, and creation. Consistent with the CC2020 competency framework, Bloom’s taxonomy of cognitive processes is used to articulate the *level of skill proficiency* expected for successful task accomplishment in data science contexts. \[See: [https://ccecc.acm.org/assessment/blooms-for-computing](https://ccecc.acm.org/assessment/blooms-for-computing)\]

The skills dimension of a data science competency is often assessed indirectly, through observation of workflows, analytical reasoning, model performance, reproducibility, and the clarity and integrity of communicated results. In practice, the activation of *“know-what”* (conceptual understanding) through *“know-how”* (methodological execution) fuses knowledge and skills into observable professional performance.

Accordingly, the practical value of any data science knowledge element can only be fully understood when it is *applied at an appropriate level of skillfulness*, as specified or demonstrated through a Bloom-aligned cognitive process. For this reason, knowledge elements and skill levels are inherently and inseparably paired in the specification of data science competencies.

Through this integration, the competency model supports a performance-based approach to data science education, in which knowledge is animated through skilled application to accomplish authentic analytic, computational, and ethical tasks.

These verbs clarify the *depth of engagement* expected with the knowledge, distinguishing between recognition, application, and innovation.

This *Competencies* document includes sample *Skills* statements for each level of Bloom’s taxonomy. The Taskforce recognizes that attaining or even covering skills at every level of the taxonomy is not likely nor appropriate in most baccalaureate programs. Therefore, for each knowledge unit we include a recommended Bloom’s level that would be appropriate for all baccalaureate data science programs.

**3\. Dispositions**

Competencies encompass a blend of knowledge, skills, and dispositions. Dispositions are essential because they represent the behaviors and attitudes that enable individuals to effectively apply their knowledge and skills in real-life situations. Dispositions, such as curiosity and resilience, help ensure that skills are not just learned but also utilized effectively when needed.

Dispositions influence how skills are utilized and can significantly impact performance. Here are some key reasons why dispositions are necessary for competencies:

* Behavioral Expression: Dispositions dictate how individuals express their skills in various situations. For example, a person may have the technical skills to perform a task but may struggle without the right mindset or attitude.  
* Facilitating Application: Dispositions such as curiosity and resilience encourage individuals to engage with challenges and adapt to changing circumstances. This adaptability is crucial in dynamic environments.  
* Enhancing Effectiveness: Skills alone are not enough; the right dispositions ensure that individuals can apply their skills effectively. For instance, a growth mindset can motivate someone to persist through difficulties, leading to better outcomes.

Dispositions capture the professional mindset expected of data science graduates. Following ACM's competency-based curriculum model (CC2020 and CCDS2021), this document treats dispositions as a third dimension of competency, complementing knowledge and skills. Whereas knowledge describes what graduates know and skills describe what graduates can do, dispositions describe the habitual attitudes, behaviors, values, and professional tendencies that influence how graduates apply their knowledge and skills in practice.

Dispositions are especially important in data science because practitioners routinely work with uncertainty, incomplete and imperfect data, ethical tradeoffs, interdisciplinary teams, and decisions that may have significant societal impact. They guide professional judgment by helping graduates determine when, why, and how to apply technical knowledge and skills responsibly within legal, organizational, and ethical contexts.

Unlike knowledge and skills, dispositions are not measured through a single examination or assignment. Instead, they are demonstrated through consistent patterns of professional behavior, reflective practice, sound decision making, and adherence to ethical and professional standards over time. Well-developed dispositions distinguish work that is merely technically correct from work that is professionally responsible, trustworthy, and socially accountable.

To promote consistency across the curriculum, this report defines a standardized vocabulary of professional dispositions that is used throughout the Knowledge Areas. Each disposition statement follows the form *"Demonstrates \[Disposition\]by..."* and describes the observable professional behaviors expected of graduates as they apply their knowledge and skills in authentic data science practice.

The **"by"** clause operationalizes each disposition by translating an abstract professional characteristic into specific, observable behaviors that can be demonstrated through coursework, projects, internships, capstone experiences, and other authentic learning activities. Rather than simply stating that graduates should possess qualities such as *Critical Thinking*, *Professional Integrity*, or *Communication Effectiveness*, the accompanying **"by"** clause explains how those qualities are manifested in professional practice. For example, a disposition such as *Critical Thinking* becomes assessable when expressed as *"Demonstrates Critical Thinking by evaluating assumptions, evidence, and limitations before drawing conclusions."* Similarly, *Professional Integrity* is demonstrated through behaviors such as honestly communicating assumptions, documenting limitations, and transparently reporting results.

By emphasizing observable behaviors, the disposition statements support curriculum design, instructional planning, and assessment. Faculty can intentionally design learning experiences that foster these professional behaviors, students gain clearer expectations for professional practice, and programs can assess the development of dispositions using authentic evidence rather than relying solely on examinations or self-assessments. In this way, the disposition statements provide a practical bridge between the abstract qualities expected of professional data scientists and the concrete behaviors through which those qualities are demonstrated, cultivated, and evaluated throughout the curriculum. In effect, the "by" clauses serve as performance indicators for professional dispositions, providing concrete examples of how dispositions are demonstrated in practice while allowing programs the flexibility to develop their own discipline-appropriate assessment methods.

The recommended disposition vocabulary is intended to be:

* Observable through professional behavior  
* Assessable over time through authentic practice  
* Applicable across technologies, domains, and careers  
* Independent of specific programming languages, software, or tools  
* Consistent with ACM's competency-based approach to computing education

The following professional dispositions provide a common vocabulary for describing the professional behaviors expected of graduates throughout this curriculum. They provide a useful mental model for how **data scientists think, act responsibly, work with others, produce quality work, and continue to innovate.**

## Professional Dispositions for Data Science Competencies

| Disposition Category | Disposition | Definition |
| :---- | :---- | :---- |
| 1\. Analytical and Evidence-Based Practice | *These dispositions describe how data scientists reason, evaluate evidence, and draw conclusions from data.* |  |
|  | Analytical Reasoning | Uses logical, quantitative, and systematic reasoning to solve problems. |
|  | Critical Thinking | Questions assumptions, evaluates evidence, and recognizes limitations. |
|  | Statistical Thinking | Reasons appropriately about variability, uncertainty, inference, and data generation processes. |
|  | Evidence-Based Decision Making | Uses data and empirical evidence to support decisions and recommendations. |
|  | Professional Skepticism | Critically evaluates evidence, models, and results before accepting conclusions. |
| 2\. Professional Responsibility | *These dispositions describe the ethical, responsible, and trustworthy conduct expected of data science professionals.* |  |
|  | Accountability | Takes responsibility for decisions, actions, and their consequences. |
|  | Professional Integrity | Acts honestly, transparently, and responsibly in professional practice. |
|  | Ethical Responsibility | Applies ethical principles and professional standards in all aspects of data science practice. |
|  | Data Stewardship | Manages data responsibly with attention to quality, privacy, security, governance, and lifecycle management. |
|  | Responsible AI Use | Uses AI technologies ethically, transparently, safely, and with appropriate human oversight. |
| 3\. Collaboration and Human-Centered Practice | *These dispositions emphasize effective collaboration, communication, accessibility, and consideration of human and societal needs.* |  |
|  | Collaboration | Works effectively with diverse teams and stakeholders. |
|  | Communication Effectiveness | Communicates technical and non-technical information clearly and appropriately. |
|  | Human-Centered Thinking | Designs solutions that consider user needs, accessibility, and societal impacts. |
|  | Inclusiveness | Promotes accessibility, equity, diversity, and respect for all users and stakeholders. |
|  | Social Responsibility | Considers the societal, economic, legal, and environmental impacts of data science. |
|  | Systems Thinking | Understands interactions among data, models, software, people, and organizational systems. |
| 4\. Quality and Continuous Improvement | *These dispositions reflect a commitment to producing high-quality work while continually improving both professionally and the data science profession.* |  |
|  | Attention to Quality | Produces accurate, reliable, maintainable, and reproducible work. |
|  | Continuous Improvement | Continuously refines processes, models, workflows, and solutions through evaluation and feedback. |
|  | Continuous Learning | Pursues ongoing professional growth and adapts to emerging knowledge and technologies. |
|  | Curiosity and Discovery | Seeks new knowledge and explores innovative solutions. |

**Relationship of Professional Dispositions to ABET Data Science Student Outcomes**

The professional dispositions defined in this curriculum complement the ABET Computing Accreditation Commission (CAC) Data Science Student Outcomes by describing the professional attitudes, values, and behaviors that enable students to consistently demonstrate those outcomes in academic and professional practice. Whereas the ABET Student Outcomes define the broad competencies that graduates are expected to achieve by the time of graduation, the professional dispositions describe *how* graduates approach problem solving, decision making, collaboration, ethical practice, communication, and continuous professional development while demonstrating those competencies.

Together with knowledge and skills, these dispositions provide a more complete competency framework for undergraduate data science education. Knowledge describes what graduates understand, skills describe what graduates are able to do, and dispositions describe the professional behaviors and habits of mind that influence how knowledge and skills are applied in practice. As such, dispositions are demonstrated through authentic performance over time rather than through a single examination or assignment.

The relationship between the professional dispositions and the ABET Student Outcomes is intentionally many-to-many. Individual dispositions often support multiple Student Outcomes, and each Student Outcome is reinforced by several complementary dispositions. For example, **Analytical Reasoning** supports problem analysis, solution development, and application of data science methods throughout the data science lifecycle, while **Professional Integrity** contributes to ethical judgment, effective communication, teamwork, and responsible professional practice. Likewise, **Attention to Quality** supports the development of reliable, maintainable, reproducible computing solutions across many aspects of the curriculum.

The first mapping table illustrates how each professional disposition contributes to one or more ABET CAC Data Science Student Outcomes. This perspective demonstrates how individual professional behaviors support the competencies expected of graduates.

The second mapping table presents the complementary view by identifying the collection of professional dispositions that collectively support each ABET Student Outcome. This perspective demonstrates that successful attainment of each outcome depends on multiple professional behaviors rather than a single attribute.

Together, these mappings show that the professional dispositions do not replace the ABET Student Outcomes. Rather, they operationalize the professional behaviors that enable students to achieve those outcomes consistently and effectively. They also provide programs with a useful framework for designing learning experiences, integrating professional expectations throughout the curriculum, and assessing the development of professional competencies using authentic student work.

These competencies are built around **Knowledge, Skills, and Dispositions**.  This diagram maps the development of competencies as they help demonstrate student outcomes leading to professional preparation for practice. 

* **Knowledge \+ Skills \+ Dispositions** are the components of competency.  
* **ABET Student Outcomes** are the observable competencies demonstrated by graduates at the time of graduation.  
* **Program Educational Objectives** describe the longer-term professional accomplishments that graduates are expected to achieve after entering practice.

![][image2]

That hierarchy aligns well with ABET's accreditation model and reinforces the role of dispositions as an integral component of competency rather than an additional or competing set of outcomes.

Mapping **Dispositions** to **ABET Student Outcomes** demonstrates that each professional disposition contributes to one or more accredited student outcomes.

| Professional Disposition | ABET CAC Student Outcome(s) | Rationale |
| :---- | :---- | :---- |
| Analytical Reasoning | SO1. Analyze complex computing problems and identify solutions.,  SO2. Design, implement, and evaluate computing-based solutions.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Applies logical, quantitative, and computational reasoning to analyze problems, design solutions, and apply methods throughout the data science lifecycle. |
| Critical Thinking | SO1. Analyze complex computing problems and identify solutions.,  SO4. Recognize professional responsibilities and make informed judgments based on legal and ethical principles.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Evaluates assumptions, evidence, alternatives, limitations, and risks when solving computing and data science problems. |
| Statistical Thinking | SO1. Analyze complex computing problems and identify solutions.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Reasons about variability, uncertainty, inference, and data generation when analyzing and modeling data. |
| Evidence-Based Decision Making | SO1. Analyze complex computing problems and identify solutions.,  SO4. Recognize professional responsibilities and make informed judgments based on legal and ethical principles.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Uses empirical evidence to support technical decisions and recommendations throughout the data science lifecycle. |
| Professional Skepticism | SO1. Analyze complex computing problems and identify solutions.,  SO4. Recognize professional responsibilities and make informed judgments based on legal and ethical principles.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Critically evaluates evidence, models, and analytical results before accepting conclusions or making recommendations. |
| Accountability | SO4. Recognize professional responsibilities and make informed judgments based on legal and ethical principles.,  SO5. Function effectively as a member or leader of a team. | Accepts responsibility for professional decisions, teamwork, and the consequences of computing practice. |
| Professional Integrity | SO3. Communicate effectively.,  SO4. Recognize professional responsibilities and make informed judgments based on legal and ethical principles.,  SO5. Function effectively as a member or leader of a team. | Acts honestly, transparently, and responsibly while communicating and practicing professionally. |
| Ethical Responsibility | SO4. Recognize professional responsibilities and make informed judgments based on legal and ethical principles. | Applies legal, ethical, and professional principles when developing and applying computing and data science solutions. |
| Data Stewardship | SO4. Recognize professional responsibilities and make informed judgments based on legal and ethical principles.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Manages data responsibly throughout its lifecycle while protecting privacy, security, governance, and quality. |
| Responsible AI Use | SO2. Design, implement, and evaluate computing-based solutions.,  SO4. Recognize professional responsibilities and make informed judgments based on legal and ethical principles., SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Develops and applies AI systems ethically, transparently, safely, and with appropriate human oversight. |
| Collaboration | SO5. Function effectively as a member or leader of a team.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Functions effectively as a member or leader of multidisciplinary teams. |
| Communication Effectiveness | SO3. Communicate effectively.,  SO5. Function effectively as a member or leader of a team. | Communicates technical information, analyses, recommendations, and results effectively to diverse audiences. |
| Human-Centered Thinking | SO2. Design, implement, and evaluate computing-based solutions.,  SO3. Communicate effectively.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Designs computing solutions that satisfy stakeholder needs while considering usability, accessibility, and societal context. |
| Inclusiveness | SO3. Communicate effectively.,  SO4. Recognize professional responsibilities and make informed judgments based on legal and ethical principles.,  SO5. Function effectively as a member or leader of a team. | Promotes accessibility, diversity, equity, and respect when working with users, stakeholders, and teams. |
| Social Responsibility | SO4. Recognize professional responsibilities and make informed judgments based on legal and ethical principles.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Considers the societal, economic, legal, and environmental impacts of data science and computing decisions. |
| Systems Thinking | SO1. Analyze complex computing problems and identify solutions.,  SO2. Design, implement, and evaluate computing-based solutions.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Recognizes interactions among data, software, models, people, and organizational systems throughout the data science lifecycle. |
| Attention to Quality | SO2. Design, implement, and evaluate computing-based solutions.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Produces accurate, reliable, maintainable, reproducible, and well-documented computing solutions. |
| Continuous Improvement | SO2. Design, implement, and evaluate computing-based solutions.,  SO5. Function effectively as a member or leader of a team.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Improves models, software, workflows, and professional practice through evaluation and feedback. |
| Continuous Learning | SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Maintains professional competence by adapting to emerging technologies, tools, and best practices. |
| Curiosity and Discovery | SO1. Analyze complex computing problems and identify solutions.,  SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Explores new ideas, methods, and technologies to improve data science practice and discover new knowledge. |

Mapping ABET Student Outcomes to Dispositions is useful because it shows how this competency framework **expands** each ABET outcome, and provides a richer, more granular interpretation of the broad ABET outcomes.

| ABET CAC Student Outcome | Professional Dispositions that Support the Outcome |
| :---- | :---- |
| SO1. Analyze complex computing problems and identify solutions. | Analytical Reasoning Critical Thinking Statistical Thinking Evidence-Based Decision Making Professional Skepticism Systems Thinking Curiosity and Discovery |
| SO2. Design, implement, and evaluate computing-based solutions. | Analytical Reasoning Systems Thinking Responsible AI Use Human-Centered Thinking Attention to Quality Continuous Improvement |
| SO3. Communicate effectively. | Communication Effectiveness Professional Integrity Human-Centered Thinking Inclusiveness |
| SO4. Recognize professional responsibilities and make informed judgments based on legal and ethical principles. | Ethical Responsibility Professional Integrity Accountability Responsible AI Use Data Stewardship Social Responsibility Critical Thinking |
| SO5. Function effectively as a member or leader of a team. | Collaboration  Communication Effectiveness Accountability Professional Integrity Inclusiveness  Continuous Improvement |
| SO6. Apply theory, techniques, and tools throughout the data science lifecycle to satisfy stakeholder needs. | Analytical Reasoning  Statistical Thinking Evidence-Based Decision Making Systems Thinking Human-Centered Thinking Attention to Quality, Continuous Learning Continuous Improvement  Data Stewardship Curiosity and Discovery |

**Relationship to the AAC\&U VALUE Rubrics**

The professional dispositions defined in this curriculum complement the Association of American Colleges and Universities (AAC\&U) **Valid Assessment of Learning in Undergraduate Education (VALUE) Rubrics** by providing a discipline-specific interpretation of broad undergraduate learning outcomes for data science. Whereas the ABET Data Science Student Outcomes describe the competencies that graduates are expected to demonstrate at the time of graduation, the AAC\&U VALUE Rubrics provide widely recognized frameworks for assessing many of the professional behaviors, attitudes, and habits of mind that contribute to those competencies.

The VALUE Rubrics were developed by faculty across higher education to support authentic assessment of essential undergraduate learning through student work rather than standardized examinations. They address broad educational outcomes such as inquiry and analysis, critical thinking, quantitative literacy, ethical reasoning, teamwork, communication, information literacy, problem solving, integrative learning, and lifelong learning. These outcomes align closely with the professional expectations of contemporary data science practice.

The professional dispositions presented in this curriculum extend these institution-wide learning outcomes by interpreting them within the context of undergraduate data science education. For example, the VALUE Rubric for **Critical Thinking** is reflected through dispositions such as *Critical Thinking* and *Professional Skepticism*, while **Ethical Reasoning** is reflected through *Ethical Responsibility*, *Professional Integrity*, *Responsible AI Use*, and *Data Stewardship*. Likewise, **Teamwork**, **Written and Oral Communication**, **Quantitative Literacy**, **Inquiry and Analysis**, and **Foundations and Skills for Lifelong Learning** are represented throughout the professional disposition framework.

As with the relationship between the professional dispositions and the ABET Student Outcomes, the relationship to the VALUE Rubrics is intentionally many-to-many. Individual dispositions frequently align with multiple VALUE Rubrics, and each VALUE Rubric is supported by several complementary dispositions. Consequently, institutions may use existing VALUE Rubrics, with appropriate discipline-specific adaptations, to assess the development of professional dispositions across the data science curriculum while maintaining consistency with institution-wide assessment practices.

The first mapping table identifies the primary AAC\&U VALUE Rubric(s) associated with each professional disposition and explains the rationale for the alignment. This perspective illustrates how individual professional behaviors contribute to broader undergraduate learning outcomes.

Collectively, these mappings demonstrate that the professional dispositions provide a practical bridge between discipline-specific competencies in data science and broader institutional learning outcomes. They enable programs to integrate professional expectations throughout the curriculum while leveraging well-established assessment frameworks to evaluate student development through authentic assignments, projects, portfolios, presentations, and other evidence of learning.

* Association of American Colleges and Universities. (2009). Inquiry and analysis VALUE rubric. [https://www.aacu.org/initiatives/value-initiative/value-rubrics/value-rubrics-inquiry-and-analysis](https://www.aacu.org/initiatives/value-initiative/value-rubrics/value-rubrics-inquiry-and-analysis)  
* [https://www.aacu.org/value/rubrics](https://www.aacu.org/value/rubrics)

**Alignment of Dispositions to the AAC\&U VALUE Rubrics**

| Disposition Category | Data Science Disposition | Primary AAC\&U VALUE Rubric(s) | Rationale |
| :---- | :---- | :---- | :---- |
| Analytical and Evidence-Based Practice | Analytical Reasoning | Inquiry & Analysis; Problem Solving; Quantitative Literacy | Applies logical, quantitative, and systematic reasoning to solve problems using data. |
|  | Critical Thinking | Critical Thinking | Evaluates assumptions, evidence, limitations, and alternative interpretations. |
|  | Statistical Thinking | Quantitative Literacy; Inquiry & Analysis | Reasons about variability, uncertainty, inference, and data generation. |
|  | Evidence-Based Decision Making | Inquiry & Analysis; Critical Thinking; Problem Solving | Uses empirical evidence to justify conclusions and decisions. |
|  | Professional Skepticism | Critical Thinking | Questions conclusions, validates evidence, and recognizes uncertainty before accepting results. |
| Professional Responsibility | Accountability | Ethical Reasoning; Integrative & Applied Learning | Accepts responsibility for professional decisions and their consequences. |
|  | Professional Integrity | Ethical Reasoning | Acts honestly, transparently, and responsibly in professional practice. |
|  | Ethical Responsibility | Ethical Reasoning | Applies ethical principles and professional standards throughout the data science lifecycle. |
|  | Data Stewardship | Ethical Reasoning; Information Literacy | Manages data responsibly with attention to privacy, security, governance, provenance, and lifecycle management. |
|  | Responsible AI Use | Ethical Reasoning; Integrative & Applied Learning | Applies AI ethically, transparently, safely, and with appropriate human oversight. |
| Collaboration and Human-Centered Practice | Collaboration | Teamwork | Works effectively within multidisciplinary and diverse teams. |
|  | Communication Effectiveness | Written Communication; Oral Communication | Communicates technical and non-technical information clearly and appropriately. |
|  | Human-Centered Thinking | Problem Solving; Integrative & Applied Learning | Designs solutions that consider user needs, accessibility, and societal impacts. |
|  | Inclusiveness | Intercultural Knowledge & Competence; Civic Engagement | Promotes accessibility, equity, diversity, and respect for diverse users and stakeholders. |
|  | Social Responsibility | Civic Engagement; Global Learning; Ethical Reasoning | Considers the societal, economic, legal, and environmental impacts of data science. |
|  | Systems Thinking | Integrative & Applied Learning | Recognizes interactions among data, models, software, people, organizations, and society. |
| Quality and Continuous Improvement | Attention to Quality | Integrative & Applied Learning | Produces accurate, reliable, maintainable, and reproducible work. |
|  | Continuous Improvement | Foundations and Skills for Lifelong Learning; Integrative & Applied Learning | Uses evaluation and feedback to improve processes, models, and workflows. |
|  | Continuous Learning | Foundations and Skills for Lifelong Learning | Pursues ongoing professional growth and adapts to emerging knowledge and technologies. |
|  | Curiosity and Discovery | Inquiry & Analysis; Foundations and Skills for Lifelong Learning | Seeks new knowledge, explores innovative ideas, and investigates unanswered questions. |

**Alignment of AAC\&U VALUE Rubrics to Dispositions**

The Data Science recommended curricular does not claim to address the entire value categories, however the degree program contributes to the values in the following ways:

| AAC\&U Category | AAC\&U VALUE Rubric | Related Data Science Dispositions |
| :---- | :---- | ----- |
| **Intellectual and Analytical Skills** |  **Creative Thinking** | Attention to Quality |
|  |  | Continuous Improvement  |
|  | **Critical Thinking** | Critical Thinking,  |
|  |  | Professional Skepticism, |
|  |  | Evidence-Based Decision Making |
|  | **Inquiry & Analysis** | Analytical Reasoning,  |
|  |  | Statistical Thinking,  |
|  |  |  Evidence-Based Decision Making, |
|  |  | Curiosity and Discovery |
|  | **Problem Solving** | Analytical Reasoning,  |
|  |  | Human-Centered Thinking,  |
|  |  | Evidence-Based Decision Making |
| **Communication Skills** | **Oral Communication** | Communication Effectiveness |
|  | **Reading** |  |
|  | **Written Communication** | Communication Effectiveness |
| **Integrative and Applied Learning** | **Information Literacy** | Data Stewardship, |
|  |  | Critical Thinking |
|  | **Integrative Learning** | Systems Thinking,  |
|  |  | Attention to Quality,  |
|  |  | Accountability,  |
|  |  | Responsible AI Use,  |
|  |  | Human-Centered Thinking,  |
|  |  | Continuous Improvement |
|  | **Quantitative Literacy** | Analytical Reasoning,  |
|  |  | Statistical Thinking |
|  | **Quantitative Literacy 2.0** | Analytical Reasoning,  |
|  |  | Evidence-Based Decision Making,   |
|  |  | Statistical Thinking,   |
|  |  | Human-Centered Thinking |
| **Civic and Intercultural Learning** | **Civic Engagement** | Social Responsibility,  |
|  |  | Inclusiveness |
|  | **Ethical Reasoning** | Ethical Responsibility,   |
|  |  | Professional Integrity, |
|  |  | Accountability |
|  |  | Responsible AI Use,  |
|  |  | Data Stewardship,  |
|  |  | Social Responsibility |
|  | **Global Learning** | Social Responsibility, |
|  |  | Ethical Responsibility,  |
|  |  | Responsible AI Use, |
|  |  | Data Stewardship |
|  | **Intercultural Knowledge & Competence** | Inclusiveness, |
|  |  |  Human-Centered Thinking  |
| **Personal and Collaborative Learning** | **Foundations for Lifelong Learning** | Continuous Learning,  |
|  |  | Continuous Improvement,  |
|  |  | Curiosity and Discovery |
|  | **Teamwork** | Collaboration |

**Competencies in Practice**

In academic and professional contexts, competencies are used to:

* Map courses to program-level outcomes  
* Define graduation requirements  
* Support accreditation and quality assurance  
* Communicate graduate capabilities to employers  
* Guide continuous curriculum improvement

**Summary**

In essence, competencies provide a holistic and future-oriented model for computing education. They move beyond listing topics to articulate what learners should *understand*, *do*, and *embody* as professionals, ensuring graduates are not only technically capable but also ethically grounded and professionally prepared.

# 

# Competency Areas {#competency-areas}

# Artificial Intelligence (AI)  {#artificial-intelligence-(ai)}

Artificial Intelligence (AI) is the field of computing concerned with developing systems that perform tasks requiring human-like intelligence, including reasoning, perception, language understanding, planning, decision making, and autonomous action. Within data science, AI extends traditional statistical and computational approaches by enabling systems to interpret complex data, interact with users, retrieve and reason over information, automate analytical workflows, and generate new content. AI techniques are particularly valuable for working with unstructured and multimodal data, including text, images, audio, video, and knowledge graphs.

As AI capabilities have rapidly evolved, data scientists increasingly rely on intelligent systems throughout the data science lifecycle—from information retrieval and knowledge representation to natural language processing, generative AI, deep learning, and autonomous AI agents. These technologies augment human expertise by improving productivity, supporting decision making, and enabling new forms of data-driven discovery. Equally important is understanding the limitations of AI systems and applying them responsibly through appropriate evaluation, transparency, human oversight, privacy protection, fairness, and governance. Together, these competencies prepare graduates to design, evaluate, and responsibly integrate AI technologies into modern data science practice.

## Competencies 

A data science graduate can select, apply, evaluate, and responsibly integrate artificial intelligence methods and intelligent systems to acquire knowledge, reason, communicate, automate analytical tasks, and support data-driven decision making while recognizing their capabilities, limitations, and ethical implications.

## Dispositions 

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Analytical Reasoning\]** by selecting and applying appropriate AI methods to solve complex data science problems while recognizing their capabilities and limitations.  
* Demonstrates **\[Critical Thinking\]** by evaluating AI-generated outputs, reasoning processes, and model performance before accepting conclusions.  
* Demonstrates **\[Professional Skepticism\]** by recognizing uncertainty, potential bias, and hallucinations in AI systems and validating results using independent evidence.

**Professional Responsibility**

* Demonstrates **\[Responsible AI Use\]** by developing and applying AI systems ethically, legally, transparently, safely, and with appropriate human oversight.  
* Demonstrates **\[Ethical Responsibility\]** by considering fairness, privacy, accountability, and societal impacts throughout the AI lifecycle.  
* Demonstrates **\[Professional Integrity\]** by accurately communicating AI capabilities, limitations, assumptions, and risks.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Human-Centered Thinking\]** by designing AI systems that enhance human decision making while considering user needs and accessibility.  
* Demonstrates **\[Communication Effectiveness\]** by explaining AI models, recommendations, and uncertainty to technical and non-technical audiences.  
* Demonstrates **\[Social Responsibility\]** by considering the broader societal implications of AI-enabled decisions and using AI to solve a given problem

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by validating AI models for robustness, reliability, reproducibility, and trustworthiness.  
* Demonstrates **\[Continuous Learning\]** by adapting to advances in AI methods, tools, standards, and best practices.  
* Demonstrates **\[Continuous Improvement\]** by refining AI systems based on evaluation, feedback, and changing requirements.

## Knowledge Units

* AI \- Agentic AI  
* AI \- Deep learning  
* AI \- Generative AI   
* AI \- Foundational AI  
* AI \- Natural language processing (NLP)  
* AI \- Ethics (See [Professionalism and Ethics (PE)](#professionalism-and-ethics-\(pe\)))

## AI \- Agentic AI (AA)

Agentic AI focuses on intelligent systems that autonomously perceive, reason, plan, act, and adapt in pursuit of user-defined goals. Unlike traditional predictive models or generative AI systems that respond to a single prompt, AI agents can decompose complex tasks, use external tools, retrieve information, interact with software and data sources, maintain memory, and iteratively evaluate their progress. In data science, agentic AI enables automation of complex analytical workflows, decision support, research assistance, and autonomous execution of multi-step processes while requiring careful attention to transparency, safety, human oversight, and governance. Agentic AI is a rapidly evolving area, therefore   
coverage of these topics may vary across data science programs at the time of this publication. 

### Knowledge

#### *Core*

* Foundations of agentic AI and autonomous systems  
* Agents, goals, environments, and tasks  
* Agentic loops  
* Human-AI collaboration and oversight  
* Evaluation and responsible use of AI agents

#### *Specialization / Concentration*

* Agent architectures and workflow orchestration  
* Multi-agent systems  
* Agent evaluation and monitoring  
* Domain-specific AI agents

#### *Electives*

* Reinforcement learning for autonomous agents  
* Agent simulation environments  
* Swarm intelligence  
* Embodied AI and robotics agents

### Skills

Recommended skill level: Understanding

**Remembering:** Identify the fundamental components of AI agents, including goals, planning, memory, tools, environments, and agent workflows.

**Understanding:** Explain how agentic AI differs from traditional machine learning models and generative AI systems, and describe how agents reason, plan, and interact with external resources.

**Applying:** Develop, configure, and evaluate AI agents that integrate language models, external tools, data sources, and retrieval systems to perform multi-step data science tasks.

**Analyzing:** Analyze agent behavior, planning strategies, memory usage, workflow execution, and failure modes to improve effectiveness, efficiency, and reliability.

**Evaluating:** Evaluate AI agents for accuracy, robustness, transparency, safety, security, governance, and appropriate human oversight.

**Creating:** Design, implement, and deploy agentic AI workflows or multi-agent systems that responsibly automate complex data science processes.

## AI \- Deep learning (DL) {#ai---deep-learning-(dl)}

Deep learning systems go beyond the capabilities of machine learning systems and address topics such as the recognition of handwriting. They tend to be large, often very large and their training can absorb huge amounts of resources.

### Knowledge

#### *Core*

* Neural networks  
* Backpropagation  
* Gradient descent modeling (See [SM \- Models](https://docs.google.com/document/d/1T-PROQb83PS7mZS-tzUsoKUOWfOLG7e2/edit#heading=h.3378rz2hh93g))

####  *Specialization / Concentration*

* Convolutional neural networks (NNs)  
* Large language models (LLMs)  
* Transformer architecture  
* Explainable AI  
* Transfer Learning, Fine-tuning NNs

### *Electives*

* Training an LLM  
* Graph neural network applications

### Skills

### Recommended skill level: Applying 

* **Remembering:** Define, core terms, architectures, and pitfalls in Deep Learning (e.g., backprop, overfitting)..  
* **Understanding:** Explain how deep models learn representations and where they fail (e.g., vanishing gradients, data hunger).  
* **Applying:** Train and validate a baseline deep learning model in workflow context (e.g., splits, early stopping) for a defined predictive task.  
* **Analyzing:** Diagnose error patterns and training dynamics (e.g., learning curves, calibration, bias) to improve performance and robustness.  
* **Evaluating:** Judge deep learning choices against criteria (e.g., accuracy,, interpretability, fairness).

**Creating:** Design, train, and validate a deep learning model for a specific application. 

## AI \- Generative AI

Data scientists need to know how generative AI works because it opens up powerful new ways to create, simulate, and enhance data-driven solutions. With generative models like large language models (LLMs) and generative adversarial networks (GANs), data scientists can generate synthetic data for training, automate content creation, simulate scenarios, and build intelligent assistants. Understanding how generative AI works also helps in critically evaluating its outputs, ensuring ethical use, and integrating these models into real-world applications such as chatbots, recommender systems, and data augmentation pipelines.

### Knowledge

####  *Core*

* Generative AI foundations, concepts, common, pitfalls, and theory  
* Trustworthy AI (e.g. interpretability, fairness, privacy-preservation, robustness)  
* Generative AI tools for data science  
* Prompt engineering

####  *Specialization / Concentration* 

* Selected applications of generative AI in a domain

### *Electives*

* N/A

### Skills

Recommended skill level: Analyzing 

* **Remembering:** Define  core generative concepts and identify common pitfalls in Generative AI (e.g., bias and fairness issues, chat drift, hallucination, \-).  
* **Understanding:** Explain generation mechanisms and constraints (e.g., sampling, context limits).  
* **Applying:** Use GenAI tools in DS workflows (e.g., summarization, code assist) with controls (e.g., citations, verification steps).  
* **Analyzing:** Diagnose failure modes (e.g., bias, hallucinations, sensitivity to prompts) using tests and audits.   
* **Evaluating:** Evaluate  GenAI models and outputs against quality/risk criteria (e.g., factuality, privacy, compliance, cost) before adoption.  
* **Creating:** Design a GenAI-enabled workflow (e.g., RAG prototype, evaluation harness) that meets governance and stakeholder needs.

## AI \- Foundational AI

Foundational AI introduces the fundamental concepts and methods that enable intelligent systems to represent knowledge, search for solutions, reason about problems, and make decisions. It provides the conceptual foundations underlying modern AI approaches—including search, knowledge representation, and reasoning—and establishes the basis for understanding contemporary methods such as generative AI, retrieval-augmented systems, and autonomous agents.

### Knowledge

####  *Core*

* Knowledge Representation  
* Search algorithms (e.g., NLP in search, Vector search, Generative AI in search)  
* Search evaluation metrics  
* Search system design  
* Heuristics

####  *Specialization / Concentration*

* Constraint satisfaction problems  
* Logical reasoning and inference  
* Probabilistic reasoning  
* Game playing  
* Planning  
* Representation learning (embeddings, vector representations)

### *Electives*

* Multi-agent systems and game-theoretic reasoning  
* First order logic  
* Inference  
* Unification  
* Robotics and intelligent perception (vision and sensor systems)

### Skills

Recommended skill level: Applying

* **Remembering:** Define standard search algorithms, heuristics, and metrics.  
* **Understanding:** Explain trade-offs between completeness, optimality, and efficiency (e.g., heuristic admissibility)   
* **Applying:** Use search methods for a defined problem (e.g., pathfinding, retrieval) using appropriate constraints and metrics.  
* **Analyzing:** Diagnose performance bottlenecks and failure cases (e.g., branching factor, heuristic quality)   
* **Evaluating:** Assess a search solution against requirements (e.g., latency, optimality, resource limits) and defend design choices.  
* **Creating:** Design a tailored search strategy (e.g., hybrid heuristic \+ pruning) for a novel domain constraint or dataset.

## AI \- Natural Language Processing

Natural language processing (NLP) is necessary for a data scientist because much of the world’s data—like emails, social media posts, customer reviews, and research articles—is in text form. NLP provides the tools to analyze, interpret, and extract meaningful insights from this unstructured data. It enables tasks such as sentiment analysis, topic modeling, text classification, and entity recognition, which are crucial for understanding human language and behavior. By mastering NLP, data scientists can unlock valuable information hidden in text and build smarter, language-aware applications.

Knowledge

####  *Core*

* Syntax  
* Semantics  
* Addressing contexts  
* Language models  
* Large language models (LLMs) (See [AI \- Deep learning (DL)](#ai---deep-learning-\(dl\)))

####  *Specialization / Concentration*

* Transformer LLM  
* Topic Modeling  
* Evolution of AI solutions 

### *Electives*

* N/A

### Skills

Recommended skill level: Applying. 

* **Remembering:** Recall NLP terminology, and pitfalls in NLP (e.g., tokenization, leakage, bias).  
* **Understanding:** Explain linguistic assumptions and model limitations (e.g., context dependence, domain shift).  
* **Applying:** Build an NLP pipeline (e.g., text cleaning → embeddings → model → evaluation) for a defined classification or extraction task.  
* **Analyzing:** Diagnose errors (e.g., minority dialect failure, label noise, drift) using slices and audits to improve validity.  
* **Evaluating:** Assess NLP results using metrics and risks (e.g., F1, harm, privacy) to support deployment decisions.  
* **Creating:** Design a domain-adapted NLP solution (e.g., prompt strategy, fine-tuning plan, monitoring).

## AI \- Ethics

Ethics in Artificial Intelligence refers to the study and application of moral principles, guidelines, and frameworks that govern the development, deployment, and use of AI systems. It focuses on ensuring that AI technologies are designed and used in ways that are fair, transparent, accountable, and aligned with human values. Ethical AI aims to minimize harm, prevent bias and discrimination, respect privacy, and promote trust between humans and intelligent systems. See [Professionalism and Ethics (PE)](#professionalism-and-ethics-\(pe\))

### Knowledge

####  *Core*

* Trustworthy AI  
* Frameworks for evaluating trustworthy AI  
* Algorithmic fairness  
* Explainable AI and ethical transparency  
* Human-AI interaction  
* Generative AI Ethics and Emerging Challenges  
* Economic considerations, including environmental impact of running large compute-intensive projects. \- Sustainability (See CSC 2023 \- [https://csed.acm.org/wp-content/uploads/2023/09/SEP-Version-Gamma.pdf](https://csed.acm.org/wp-content/uploads/2023/09/SEP-Version-Gamma.pdf))  
* 

#### *Specialization / Concentration*

* Legal and regulatory considerations

### *Electives*

* TBA

### Skills 

Recommended skill level: Understanding

* **Remember:** Define the characteristics of trustworthy AI, including fairness, reliability, safety, privacy, transparency, and accountability.  
* **Understand:** Explain how trustworthiness influences the adoption and acceptance of AI systems.  
* **Apply:** Apply established frameworks to evaluate the trustworthiness of an AI application.  
* **Analyze:** Analyze potential risks and failure modes that could undermine trust in an AI system.  
* **Evaluate:** Evaluate the adequacy of safeguards, monitoring mechanisms, and governance practices used to support trustworthy AI.  
* **Create:** Design an AI solution that incorporates principles of trustworthiness throughout the system lifecycle.

# Computing Algorithms (CA)  {#computing-algorithms-(ca)}

Computing algorithms form a critical foundation in data science, enabling students to understand how data is collected, processed, and analyzed through structured computational methods. Algorithms are the engines behind data exploration and model implementation, and their design directly impacts the efficiency, reliability, and scalability of data-driven solutions. Undergraduate students learn to integrate algorithms with existing software tools and systems, while also gaining insight into the computational trade-offs involved—particularly in terms of time and space complexity.  
The scope of this area includes both theoretical and practical aspects of algorithm design and analysis. Students explore fundamental algorithmic techniques such as sorting, searching, recursion, and optimization, as well as specialized approaches for numerical computing and large-scale data processing. Emphasis is placed on evaluating algorithm performance, understanding limitations, and applying algorithms in real-world data science contexts. 

## Competencies 

A data science graduate can select, apply, analyze, and evaluate computational algorithms and data structures to process and analyze data efficiently and reliably, accounting for algorithmic complexity, computational limits, and practical trade-offs in real-world data science contexts.

## Dispositions

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Analytical Reasoning\]** by selecting algorithms and data structures appropriate for solving computational problems efficiently.  
* Demonstrates **\[Critical Thinking\]** by evaluating algorithmic complexity, scalability, correctness, and tradeoffs.  
* Demonstrates **\[Evidence-Based Decision Making\]** by comparing algorithmic alternatives using empirical performance measures.

**Professional Responsibility**

* Demonstrates **\[Professional Integrity\]** by developing algorithmic solutions that are transparent, fair, reproducible, and appropriate for their intended use.  
* Demonstrates **\[Accountability\]** by recognizing the consequences of algorithmic decisions on users and stakeholders.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Communication Effectiveness\]** by explaining algorithmic approaches, assumptions, and performance characteristics clearly to technical and non-technical stakeholders.  
* Demonstrates **\[Human-Centered Thinking\]** by considering user requirements and real-world constraints when selecting computational solutions.

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by producing algorithmic solutions that are correct, efficient, maintainable, and scalable.  
* Demonstrates **\[Continuous Improvement\]** by refining algorithms using feedback, testing, benchmarking, and performance evaluation.

## Knowledge Units

* CA \- Foundational Algorithms   
* CA \- Foundational Data Structures  
* CA \- Complexity Analysis  
* CA \- Computational Limitations


## CA \- Foundational Algorithms

Basic computer algorithms are important for a data scientist to know because they help solve common data problems efficiently and accurately. Algorithms like sorting, searching, and filtering are essential for organizing and retrieving data, while others like recursion or greedy methods help break down complex tasks into manageable steps. Understanding these algorithms allows data scientists to write better code, optimize performance, and make informed choices when working with large datasets or building models. Even simple algorithms form the building blocks of more advanced techniques used in data science.

### Knowledge

####  *Core*

* Iterative procedures  
* Recursion  
* Sorting  
* Searching  
* Tree and graph algorithms  
* Hashing  
* Constrained optimization algorithms (e.g., simplex, branch and bound, network flow algorithms)  
* Big data algorithms (See [Artificial Intelligence (AI)](#public-review-copy), [EDA \- Data Clustering Methods](#skills), [ML \- Unsupervised learning](#skills-1) and [Statistical Modeling (SM)](#skills-2))

#### *Specialization / Concentration*

* Mathematical Programming/Constrained Optimization (See  [Statistical Modeling (SM)](#statistical-modeling-\(sm\)))  
* Dynamic Programming

### *Electives*

* Stochastic Programming  
* Constraint Programming)

### Skills

Recommended skill level: Applying

* **Remembering:** Identify algorithmic patterns and pitfalls .  
* **Understanding:** Explain efficiency trade-offs of different algorithms for solving a given problem .  
* **Applying:** Apply standard algorithms for data science tasks correctly and efficiently.  
* **Analyzing:** Diagnose complexity drivers and bottlenecks to improve scalability.  
* **Evaluating:** Prioritize algorithm choices against constraints to justify their selection.  
* **Creating:** Design a suitable procedure for a given domain requirement.

## CA \- Foundational Data Structures

Foundational data structures are important for a data scientist because they provide the basic ways to organize, store, and access data efficiently. Structures like arrays, lists, dictionaries (hash maps), sets, and trees help manage data in memory and perform operations like searching, sorting, and grouping quickly. Knowing when and how to use the right data structure can significantly improve the performance of data processing tasks, especially when working with large datasets. This foundational knowledge also supports writing cleaner, more efficient code and understanding how data is handled behind the scenes in libraries and algorithms.

### Knowledge

#### *Core*

* Arrays  
* Lists  
* Binary trees  
* Tuples  
* Dictionaries 

####  *Specialization / Concentration*

* Graphs	  
* Heaps  
* N-Node trees

### *Electives*

* Secondary storage data structures (e.g., B/B+-Trees, R-Trees)

### Skills {#skills-10}

Recommended skill level: Applying

* **Remembering:** Recall key data structures and their typical operations (e.g., hash maps, trees).  
* **Understanding:** Explain performance implications (e.g., lookup costs, memory trade-offs) of different structures.   
* **Applying:** Apply an appropriate  structure given task parameters .  
* **Analyzing:** Detect inefficiencies (e.g., repeated scans, poor indexing). **Evaluating:** Critique  structure choices for time and space efficiencies (e.g., update frequency, size, concurrency).  
* **Creating:** Design a software solution for the typical operations of a key data structure..

## CA \- Complexity analysis

Complexity analysis is required by a data scientist because it helps evaluate how efficiently an algorithm or data processing task will perform, especially as the size of the dataset grows. By understanding time and space complexity, data scientists can choose methods that scale well, avoid performance bottlenecks, and make informed decisions when working with large or real-time data. This knowledge ensures that solutions are not only correct but also practical and optimized for speed and resource usage.

### Knowledge

####  *Core*

* Definition of complexity  
* Big O notation and orders of magnitude (See [MF \- Discrete Mathematics](#topics-from-discrete-mathematics,-linear-algebra,-and-calculus-are-critical-pillars-of-the-mathematical-foundation-for-data-science.-discrete-mathematics-equips-data-scientists-with-tools-for-understanding-logic,-set-theory,-combinatorics,-and-graph-theory—essential-for-algorithm-design,-data-structures,-and-modeling-relationships-in-networks-and-databases.-linear-algebra-provides-the-language-for-representing-and-manipulating-data-efficiently,-especially-in-high-dimensional-spaces,-and-is-central-to-machine-learning-algorithms-like-principal-component-analysis,-support-vector-machines,-and-neural-networks.-calculus,-particularly-differential-calculus,-is-vital-for-optimization-tasks,-such-as-training-machine-learning-models-through-gradient-descent-and-understanding-how-small-changes-in-input-affect-output.-together,-these-disciplines-enable-data-scientists-to-build-robust-models,-analyze-complex-systems,-and-derive-insights-from-data-with-mathematical-rigor.))  
* Ways of measuring computational complexitySpace complexityTime complexity

####  *Specialization / Concentration*

* Approximation algorithms  
* Probabilistic methods

### *Electives*

* N/A

### Skills

Recommended skill level: Applying

* **Remembering:** Recognize the distinctions between common complexity classes.   
* **Understanding:** Explain how data size and algorithm design drive complexity (e.g., nested loops,)   
* **Applying:** Measure time and space costs for candidate methods   
* **Analyzing:** Compare  observed performance and. expected complexity (e.g., overhead, data skew)   
* **Evaluating:** Verify an algorithm time/space tradeoffs fit given constraints.   
* **Creating:** Design a lower-complexity approach (e.g., approximation, indexing) to meet scale requirements.

## CA \- Computational Limitations

Data scientists need to understand the limits of computing and computing mathematics because these boundaries define what is feasible when working with data, especially at scale.  Understanding mathematical limits, like numerical precision, rounding errors, and convergence behavior, ensures that models and analyses are accurate and reliable. Additionally, understanding hardware limitations for numeric storage is important for reliable and correct solutions. This awareness helps avoid unrealistic expectations, prevents errors in data interpretation, and guides the selection of appropriate tools and methods for solving complex problems.

### Knowledge

#### *Core*

* The halting problem  
* Implications of limits of computing  
* Machine precision (rounding error)   
* Numerical precision

####   *Specialization / Concentration*

* Variations on the halting problem  
* Convergence behavior  
* Quantization error 

*Electives*

* Error analysis of algorithms

### Skills

Recommended skill level: Understanding

* **Remembering:** Recall key limits (e.g., halting problem, machine precision, numerical precision)   
* **Understanding:** Explain why some problems resist exact solutions (e.g., intractability, numeric limits).  
* **Applying:** Apply practical mitigations (e.g., heuristics, approximations, convergence checks).  
* **Analyzing:** Diagnose when limits are binding (e.g., non-convergence, memory ceilings) and propose alternative formulations.  
* **Evaluating:** Evaluate solution adequacy given limits (e.g., approximate acceptable error) and justify constraints transparently.  
* **Creating:** Design practical mitigations 

# Computing Fundamentals (CF)  {#computing-fundamentals-(cf)}

Computer fundamentals provide the essential groundwork for understanding how modern computing systems operate and support data science applications. A computer system is composed of hardware and software components that work together to execute tasks, manage data, and run analytical tools. As data science increasingly relies on computational power and infrastructure, students must develop a conceptual and practical understanding of how computers process, store, and transmit information. This includes learning how operating systems manage resources, how networks enable secure and scalable data exchange, and how computer architecture influences performance.

The scope of this area spans key topics such as operating systems, computer architecture and organization, communications networks, parallel and distributed systems, and database fundamentals. Students explore how data is stored and retrieved in both relational and non-relational databases, and how system-level design choices impact the efficiency and reliability of data-driven applications. By mastering these fundamentals, students are equipped to leverage computing systems effectively for data analysis, while also laying the foundation for deeper study in computer science or advanced electives. This knowledge is critical for building robust, scalable, and ethical data science solutions in real-world environments.

## Competencies 

A data science graduate can effectively use and evaluate computing systems—including hardware, operating systems, databases, networks, security mechanisms, and high-performance computing environments—to design, deploy, and manage data-driven solutions that are scalable, secure, reliable, and ethically responsible.

## Dispositions

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Critical Thinking\]** by evaluating computing platforms, architectures, and cloud technologies appropriate for data science applications.  
* Demonstrates **\[Analytical Reasoning\]** by selecting computing resources that best support analytical workloads.

**Professional Responsibility**

* Demonstrates **\[Data Stewardship\]** by protecting computing resources, data, privacy, security, and system integrity.  
* Demonstrates **\[Professional Integrity\]** by following responsible computing practices and applicable security standards.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Collaboration\]** by working effectively with all stakeholders including software developers, database administrators, and infrastructure teams.  
* Demonstrates **\[Communication Effectiveness\]** by communicating computing requirements and technical constraints clearly to technical and non-technical stakeholders.

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by applying reliable, secure, scalable, and reproducible computing practices.  
* Demonstrates **\[Continuous Learning\]** by adapting to feedback, evolving computing technologies, architectures, and infrastructure.

## Knowledge Units

* CF \- Computer Architecture and Systems  
* CF \- Computer Security and Privacy  
* CF \- Database Management and Query Languages  
* CF \- Parallel and Distributed Computing   
* CF \- Networking 

## CF \- Computer Architecture and Systems 

A data scientist should understand the basics of computer architecture and systems to work effectively with large and complex data. This includes knowledge of how processors, memory, and storage affect data processing speed and scalability, as well as how operating systems manage resources. Awareness of concepts like parallelism, caching, I/O bottlenecks, and distributed computing helps in writing efficient code and choosing the right tools for analysis. In addition, familiarity with cloud and cluster environments enables data scientists to handle big data workflows beyond a single machine. 

### Knowledge

####  *Core*

* Role and purpose of an Operating System  
* Bits, bytes, and words  
* Computer’s representation of data  
* Computer arithmetic  
* CPUs and GPUs and TPUs  
* Storage systems (Storage systems and their technology, Registers, Cache, RAM, Virtual memory)  
* Importance of backups  
* Virtual systems  (e.g., via cloud services)

####  *Specialization / Concentration*

* Multi-core and multi-processing  
* Basic organization of the von Neumann machine  
* Parallel architectures (e.g., SIMD, MIMD) \- Flynn’s Architecture  
* Knowledge graphs  
* RAID Architecture 

### *Electives*

* Reliability and Availability

### Skills {#skills-4}

Recommended skill level: Applying

* **Remembering:** Define and identify  system components and concepts (e.g., bits, bytes, words, CPU/GPU, cache, I/O, Operating Systems).  
* **Understanding:** Explain the bottlenecks that occur due to hardware architecture when processing data. Recognize which computing resources (e.g., local vs. cloud, CPU vs. GPU) and storage system (memory vs. disk vs. distributed) are required for a given data project.   
* **Applying:** Configure or use computer resources for a defined workload.  
* **Analyzing:** Diagnose bottlenecks (e.g., I/O bound pipelines, memory thrash) using profiling tool evidence to optimize.  
* **Evaluating:** Evaluate  platform choices (e.g., local vs. cloud, CPU vs. GPU) against cost, reliability, and speed criteria for a given data project.  
* **Creating:** Design a compute plan (e.g., scalable batch workflow) aligned to data size, time constraints, and reproducibility.

## CF \- Computer Security and Privacy 

A data scientist needs a solid understanding of computer security and privacy to ensure that data is accessed, stored, and shared safely. This includes knowledge of authentication and authorization, data encryption (at rest and in transit), and secure handling of sensitive or personal data to comply with privacy regulations like GDPR or HIPAA. Awareness of common security threats—such as malware, phishing, and data breaches—as well as best practices for secure coding and access control, helps data scientists protect both the data and the systems they work with. Strong security awareness is essential for maintaining trust and integrity in data-driven projects.  See [Data Acquisition (DA)](#data-acquisition-\(da\)) and [PE \- Data Stewardship](#pe---data-stewardship).  ([CS2023](https://csed.acm.org/) was referenced and repurposed for this section.)

### Knowledge

####  *Core*

* Tensions between security, privacy, and performance  
* Applicability of laws and regulations on security and privacy    
* Standards for management and governance of security processes. 

####  *Specialization / Concentration*

* Software and web vulnerabilities, threats, and attack vectors  
* Denial of Service (DoS) and Distributed Denial of Service (DDoS)   
* Ethical considerations for designing secure systems and maintaining privacy 

### *Electives*

* Internet of Things privacy and security  
* Classical cryptosystems  
* Basic cryptography: symmetric key and public key cryptography   
* Public-key cryptosystems: Diffie-Hellman, RSA   
* Security Analysis  
* Intrusion detection systems   
* Access control

### Skills

Recommended skill level: Understanding.

* **Remembering:** Define  principles and practices of data protection and security and privacy laws and regulations.  
* **Understanding:** Explain the tensions between security, privacy and performance.   
* **Applying:** Apply secure handling practices (e.g., access control, secret management, encrypted storage) in DS workflows.  
* **Analyzing:** Diagnose risks and vulnerabilities (e.g., overbroad permissions, data exfil paths) to reduce exposure.  
* **Evaluating:** Judge systems against security/privacy criteria (e.g., compliance, least privilege) and justify remediation priorities.  
* **Creating:** Design a secure data pipeline architecture (e.g., role-based access, audit logs) appropriate to sensitive data use.

## CF \- Database management and query languages 

Data scientists need a solid understanding of database management and query languages to access, organize, and analyze data efficiently. This includes knowing how relational databases are structured through tables, keys, and relationships, as well as how to design or interpret schemas. Proficiency in SQL is essential for querying, filtering, joining, and aggregating data, while familiarity with advanced features like subqueries, views, and stored procedures is valuable for more complex tasks. Beyond relational systems, data scientists should also understand NoSQL databases for handling semi-structured or unstructured data. Equally important is awareness of performance considerations, indexing, and basic transaction concepts, since these directly affect the scalability and reliability of analyses.

### Knowledge

####  *Core*

* Relational models (tables, keys, relationships)  
* Entity-Relationship modeling  
* Constraints (primary key, foreign keys, integrity rules)  
* Database normalization  
* Query languages (SQL, NOSQL)  
* Query optimization  
* Semi-structured data (XML, JSON)  
* Data Security and Privacy

####  *Specialization / Concentration*

* Distributed databases and cloud data management  
* Emerging database trends  
* Streaming data and real-time querying  
* Security and governance (authentication, encryption, compliance concerns)  
* Object-oriented databases  
* Vector databases   
* Parallel databases 

### *Electives*

* Database architecture, data independence, and data abstraction  
* Use of a declarative query language  
* Approaches for managing large volumes of data  
* Scalability and performance of cloud services  
* Cost awareness of cloud services (See [PM \- Project planning and governance](#pm---project-planning-and-governance))

### Skills

Recommended skill level: Applying 

* **Remembering:** Recall DB structure and query constructs (e.g., joins, indexes).  
* **Understanding:** Explain schema design and query behavior (e.g., normalization, execution plans) to avoid incorrect outputs.  
* **Applying:** Write and optimize queries (e.g., aggregations, window functions) to extract analysis-ready datasets.  
* **Analyzing:** Diagnose performance and correctness issues (e.g., duplicate joins, skew) using plans and validation checks.  
* **Evaluating:** Judge DB technology choices (e.g., SQL vs. NoSQL) against workload, governance, and scalability constraints.  
* **Creating:** Design a data model or ingestion pattern (e.g., star schema, streaming table) for a new analytic product.

## CF \- Parallel and Distributed Computing (PDC) {#cf---parallel-and-distributed-computing-(pdc)}

Parallel and distributed computing enables data scientists to process large-scale datasets and run computationally intensive workloads efficiently, which is critical for tasks such as training machine learning models at scale, executing demanding scientific simulations, or performing analytics across massive data volumes. Working with large-scale data requires understanding how computation can be divided across multiple processors, cores, or machines through concepts such as multithreading, multiprocessing, and message passing, as well as how to design algorithms that scale across distributed systems. This includes proficiency with frameworks for data-parallel operations, as well as familiarity with high-performance computing (HPC) environments, cluster scheduling, GPU acceleration, and optimized numerical libraries. Knowledge of cloud computing platforms further equips data scientists to leverage elastic resources, managed services, and distributed storage for scalable analytics. Awareness of latency, fault tolerance, and load balancing is equally important, as these factors directly shape the performance and reliability of large-scale data workflows, making complex models and massive datasets far more manageable.

The task force believes that all undergraduate data science students should gain exposure to parallel and distributed computing (PDC). However, we recognize that not all institutions have the resources necessary to provide hands-on experience with large-scale data problems in the classroom. For programs unable to offer such opportunities, the committee strongly encourages students to seek relevant experience through internships or other experiential learning opportunities when feasible.

### Knowledge

####  *Core*

* Data Communication/Transfer, Process Coordination, and Computation  
* Concurrency & Parallelism  
* Vectorization ,   
* Multiprocessing/threading  
* Data/task parallelism  (See ML \- Systems)


####  *Specialization / Concentration*

* Distributed computing architectures   
* Distributed file systems.  
* Distributed computing frameworks.  
* GPU computing and acceleration.  
* High-performance computing fundamentals.  
* Containerization and reproducible workflows.  
* Container orchestration.  
* Cloud computing platforms and services.

#### *Electives*

* Federated learning  
* MLOps (serving, monitoring, CI/CD for ML)  
* Networking & APIs (REST, gRPC)  
* Authentication & security   
* Privacy and compliance (GDPR, HIPAA)  
* Energy-aware and green distributed computing

### Skills 

Recommended skill level: Applying.

* **Remembering:** Define the 3 Cs (communication, coordination, computation) in parallel and distributed computing, HPC, and cloud computing, and recall key primitives, protocols, and models in each.  
* **Understanding:** Explain performance trade-offs among messaging styles, consistency models, and decomposition strategies.  
* **Applying:** Decompose data problems into parallel tasks and implement parallel data algorithms. , use synchronization primitives, Use vectorized/parallel libraries. Run jobs on GPUs, Spark/Dask, or cloud. Build Docker containers. Submit SLURM/cloud jobs.  
* **Analyzing:** Profile workloads to diagnose communication bottlenecks, coordination overhead, and load imbalance in distributed workloads.   
* **Evaluating:** Compare scaling strategies in terms of  cost, performance, and reproducibility.  
* **Creating:** Design scalable, reproducible workflows with appropriate compute, storage, and deployment. 

## CF \- Networking 

Data and applications are shared over computer networks. Understanding how they work helps comprehend how data and applications are vulnerable to the introduction of errors, loss of information, or attacks, as well as how data and applications can be protected from these threats. Additionally, knowledge of networks is crucial for understanding cloud systems, Big Data clusters, and performance.

### Knowledge

####  *Core*

* Organization of the Internet: Internet Service Providers , Content Providers, Cloud providers, etc.  
* Components of networks  
* Intranet vs Internet  
* Cloud and web services

####      *Specialization / Concentration*

* HTTPS as an application-layer protocol  
* Layered network structure  
* Naming and address schemes (DNS, IP addresses, Uniform Resource Identifiers, etc.)  
* Basic protocols: TCP, IP  
* Network security (e.g., encryption, proxy servers, intranet vs internet)  
* Network monitoring. 

#### *Electives* 

* Local area networks; LAN topology (e.g., bus)  
* Circuit vs packet-switched networks  
* Network Virtualization (e.g., SDN, Data Center Networks)

### Skills 

Recommended skill level: Understanding

* **Remembering:** Recall networking basics (e.g., TCP/IP, DNS, HTTPS) to communicate and troubleshoot effectively.  
* **Understanding:** Explain how networks affect DS systems (e.g., latency, security, data transfer limits) to select designs.  
* **Applying:** Configure or use networked services safely (e.g., cloud storage access, APIs) for a defined pipeline.  
* **Analyzing:** Measure network performance and diagnose network-related failures (e.g., timeouts, misconfigurations) using logs and monitoring evidence.  
* **Evaluating:** Evaluate networking choices (e.g., public vs. private endpoints) against security, cost, and reliability criteria.  
* **Creating:** Design a secure, reliable data exchange pattern (e.g., VPC \+ TLS \+ monitoring) for a new workflow.

# Data Acquisition (DA)  {#data-acquisition-(da)}

Data acquisition is the foundational process of gathering raw data from appropriate sources to support analysis, modeling, and informed decision-making. As the first step in the data science lifecycle, it involves identifying relevant data sources—such as databases, sensors, APIs, web platforms, and surveys—and applying appropriate methods to collect and organize data. This stage is critical for ensuring that the data is complete, accurate, and representative of the problem being addressed, laying the groundwork for all subsequent data wrangling, analysis, and modeling tasks.

In an undergraduate data science program, students develop the skills to evaluate the relevance and reliability of data sources, apply effective acquisition techniques, and ensure data quality through validation, cleaning, and transformation. They consider the needs of the communities or environments providing the data and concerns regarding data privacy and ownership. They also learn to integrate heterogeneous data into formats suitable for analysis, while understanding the implications of their methodological choices on data integrity and analytical outcomes. The curriculum emphasizes both technical proficiency and critical thinking, preparing students to make informed decisions throughout the data acquisition process and to recognize its impact on the success of data-driven projects.

## Competencies 

A data science graduate can proactively collect, integrate, and manage data from diverse sources while ensuring data quality, provenance, privacy, and regulatory compliance.

## Dispositions

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Analytical Reasoning\]** by selecting appropriate data sources, acquisition methods, and integration strategies for a given problem.  
* Demonstrates **\[Critical Thinking\]** by evaluating data relevance, quality, representativeness, provenance, and potential sources of bias.

**Professional Responsibility**

* Demonstrates **\[Data Stewardship\]** by acquiring, managing, documenting, and protecting data responsibly throughout its lifecycle.  
* Demonstrates **\[Professional Integrity\]** by accurately documenting data provenance, transformations, and limitations.  
* Demonstrates **\[Ethical Responsibility\]** by complying with legal, regulatory, and organizational requirements governing data collection and use.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Communication Effectiveness\]** by documenting data sources, quality, assumptions, and limitations for technical and non-technical stakeholders.  
* Demonstrates **\[Collaboration\]** by coordinating data acquisition activities with domain experts and data providers.

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by ensuring acquired data are accurate, complete, consistent, and fit for analysis.  
* Demonstrates **\[Continuous Improvement\]** by refining data acquisition and integration workflows based on evaluation and feedback.

## Knowledge Units

* DA-  Data Context, Sources and Types  
* DA \- Data Collection: Goals, Methods and Bias  
* DA \- Data Integration and Operability  
* DA \- Data Wrangling and Data Engineering  
* DA \- Responsibility, Ethical and Legal considerations

## DA \- Data Context, Sources and Types {#da---data-context,-sources-and-types}

A data scientist must understand data sources and types because they form the foundation of any analytical or modeling work. Data sources—such as databases, APIs, spreadsheets, web pages, or sensor feeds—determine how data is accessed, its reliability, and its relevance to the problem at hand. Similarly, knowing the types of data—structured, unstructured, semi-structured, time-series, or geospatial—guides how the data should be cleaned, transformed, and analyzed. This knowledge helps data scientists choose appropriate tools and techniques, anticipate challenges in preprocessing, and ensure that insights drawn from the data are valid and actionable. Without a clear grasp of where data comes from and what form it takes, a data scientist risks misinterpreting results, applying unsuitable models, or violating ethical and legal standards.

### Knowledge

#### *Core*

* Structured vs Unstructured Data vs Semi-structured Data (Data Types: Data file formats, e.g., plain text, spreadsheets, etc.)  
* Primary vs Secondary sources (Primary: Observational, Experiments; Secondary: Existing data such as Government data)  
* Data dictionaries and metadata

#### *Specialization / Concentration*

* Processing multi-media files, e.g., image, video, audio, etc.

### *Electives*

* N/A

### Skills

Recommended skill level: Understanding

* **Remembering:** Recall the core source types and formats (e.g., structured vs. unstructured, metadata) to plan acquisition accurately. Define a data dictionary and metadata.   
* **Understanding:** Explain benefits and limitations of core source types and formats.  Explain benefits and limitations  of a data dictionary and metadata.   
* **Applying:** Select and access appropriate sources (e.g., logs, surveys, third-party data) and resources (e.g., metadata and data dictionaries) for a defined data science objective.   
* **Analyzing:** Detect source limitations (e.g., missingness, sampling bias, drift) to mitigate downstream risk.   
* **Evaluating:** Judge fitness-for-purpose (e.g., coverage, legality, cost) and defend inclusion/exclusion decisions.  
* **Creating:** Develop a source strategy (e.g., multi-source blending plan with metadata standards) for a new domain problem.

## DA \- Data Collection Methods

Data collection methods in data science refer to the techniques and tools used to gather raw data from various sources for analysis. Depending on the goals and context, data can be collected manually or automatically through methods such as surveys, sensors, web scraping, database queries, and application programming interfaces (APIs). These methods vary in scale and complexity, from experimental or observational data gathered in research settings to continuous data streams from IoT devices or online systems. Effective data collection ensures that the acquired data is relevant, accurate, and representative, providing a strong foundation for reliable analysis and data-driven decision-making. It also takes into account the needs of the communities or environments providing the data and invests effort to address concerns regarding data privacy and ownership.

### Knowledge

#### *Core*

* APIs  
* Web scraping  
* Database Queries  
* Sensor/IoT Data  
* Experiments (See also [Research Methods and Experimental Design (RM)](#research-methods-and-experimental-design-\(rm\))  
* Surveys

#### *Specialization / Concentration*

* Streaming / real-time data  
* Designing or implementing core methods rather than just using the output.

### *Electives*

* An in-depth course in one of the core topics.

### Skills {#skills-6}

Recommended skill level:  Applying

* **Remembering:** Define standard collection mechanisms (e.g., APIs, scraping, sensors) and pitfalls (e.g., Terms of Service  violations).  
* **Understanding:** Explain how collection choices affect bias, representativeness, and privacy to prevent predictable harm.  
* **Applying:** Execute a collection plan (e.g., API pulls with rate limits, validated surveys) with documentation and controls.  
* **Analyzing:** Diagnose collection errors (e.g., measurement bias, instrumentation issues) and quantify impacts on results. Compare collection methods by efficacy, reliability, ethics, legality, and cost to justify the chosen approach.   
* **Evaluating:** Choose an appropriate collection method and defend that choice according to attributes such as efficacy, reliability, ethics, legality, and cost to justify the chosen approach.   
* **Creating:** Design a robust collection system (e.g., streaming ingestion with validation and monitoring) for new requirements. (again see Research Methods and Experimental Design (RM))

## DA \- Data Integration and Operability

Data integration and operability methods refer to the techniques used to combine data from multiple sources and ensure that systems can work together seamlessly. For a data scientist, understanding these methods is crucial because real-world data is often fragmented across different platforms, formats, and technologies. Data integration involves merging datasets, resolving inconsistencies, and maintaining data quality, while operability focuses on enabling systems—such as databases, analytics tools, and machine learning platforms—to communicate and function cohesively. Mastery of these concepts allows data scientists to build scalable pipelines, automate workflows, and ensure that insights can be shared and applied across departments or applications. Without these skills, data scientists risk working in silos, duplicating efforts, or producing analyses that cannot be operationalized effectively.

### Knowledge

#### *Core*

* Schemas and metadata  
* Joining and merging   
* Data harmonization  
* ETL (Extract, Transform, Load)  
* Data Engineering: batch vs stream, ETL vs ELT

#### *Specialization / Concentration*

* Data warehousing  
* Data Engineering at Scale: data lakes/warehouses/lakehouses, SQL at scale, NoSQL  
* Workflow Orchestration tools Airflow, Prefect, Dagster, Kafka/Flink

### *Electives*

* N/A

### Skills {#skills-7}

Recommended skill level: Understanding

* **Remembering:** Recall integration concepts (e.g., schema matching, ETL/ELT) to coordinate datasets correctly.  
* **Understanding:** Explain interoperability constraints (e.g., identifier consistency, semantic alignment) to avoid incorrect merges.  
* **Applying:** Perform joins/merges and harmonization with validation (e.g., key integrity checks) for analysis readiness.  
* **Analyzing:** Diagnose integration failures (e.g., duplication, schema drift) using reconciliation metrics and audits.  
* **Evaluating:** Critique integration quality (e.g., completeness, correctness) and defend assumptions made during harmonization.  
* **Creating:** Design an integration architecture (e.g., warehouse/lakehouse model) for scalable, governed data reuse.

## DA \- Data Wrangling and Data Engineering

Data wrangling is a foundational skill for data scientists, especially during the data acquisition phase, where raw data may be messy, incomplete, or inconsistently formatted. Before any meaningful analysis can occur, data must be cleaned, transformed, and structured in a way that aligns with analytical goals. This process includes handling missing values, correcting errors, standardizing formats, and integrating data from multiple sources. Without effective data wrangling, even the most sophisticated models can produce misleading or inaccurate results. Moreover, the ability to wrangle data effectively enables data scientists to uncover hidden patterns, ensure data quality, and build trust in their findings.

### Knowledge

#### *Core*

* Data cleaning (e.g., Handle missing values, removing duplicates, correcting errors, text and string manipulation)  
* Data organizing (tidying) and reshaping  
* Data transformation  
* Joining data from various sources

#### *Specialization / Concentration*

* Advanced data transformations for ML such as feature engineering  
* Methods for massive datasets with challenging requirements such as storage and processing speed.

### *Electives*

* N/A

### Skills

Recommended skill level: Applying

* **Remembering:** Identify common cleaning and transformation operations (e.g., imputation, encoding) and pitfalls (e.g., leakage).  
* **Understanding:** Explain how wrangling decisions affect inference and model behavior (e.g., missingness mechanism assumptions).  
* **Applying:** Execute a reproducible wrangling workflow (clean → transform → validate → document) for a defined project.  
* **Analyzing:** Diagnose data-quality issues (e.g., outliers, inconsistent units) and their downstream effects on metrics.  
* **Evaluating:** Assess data readiness using criteria (quality thresholds, governance rules) to decide whether data is fit for purpose.  
* **Creating:** Design a robust wrangling pipeline (e.g., data contracts, automated checks) for reuse and scaling.

## DA \- Ethical and Legal Considerations

Ethical and legal considerations in data science involve ensuring that data is collected, managed, and used responsibly, fairly, and in compliance with laws and societal values. Data scientists must protect individuals’ privacy, obtain proper consent for data use, and safeguard sensitive or personal information against misuse or unauthorized access.  Legally, data work must comply with regulations such as the GDPR, CCPA, or other regional data protection laws. Ethically, it requires transparency, fairness, and accountability in how data and algorithms are applied—avoiding bias, discrimination, or harm. Upholding these principles builds public trust and supports the responsible advancement of data science.

### Knowledge

#### *Core*

* Data Ownership/Provenance  
* Data regulations and code of ethics (See [Professionalism and Ethics (PE)](#skills-3))  
* Data Governance (Policies and processes for data use, Quality, Ethical use of data, identifying any data bias)  
* Data Security and Privacy (See [CF \- Computer Security and Privacy](#skills-4))   
* Ethical considerations for maintaining data privacy     

#### *Specialization / Concentration*

* N/A

### *Electives*

* N/A

### Skills {#skills-14}

Recommended skill level: Understanding

* **Remembering:** Recall key legal/ethical concepts  (e.g., code of ethics, policies and processes) to avoid noncompliant handling.  
* **Understanding:** Explain implications of source properties (e.g., provenance, bias, timeliness) to avoid invalid conclusions.  
* **Applying:** Apply governance and security requirements (e.g., minimization, access control, documentation) in acquisition and analysis.  
* **Analyzing:** Detect ethical risk points (e.g., sensitive attributes, re-identification risk) and propose mitigations.  
* **Evaluating:** Assess decisions against compliance and harm criteria and defend rationale to stakeholders.  
* **Creating:** Design a compliant data practice (e.g., DPIA workflow, retention policy) integrated into DS operations.

# Data Storytelling (DS)  {#data-storytelling-(ds)}

For data science to be effective, its results must be effectively communicated. This requires understanding the audience's communication needs, including language, modality, accessibility, and relatability. Data communication and storytelling can happen in many modes, such as talk, text, charts, images, video, maps, sonification, other visualizations, or physicalization.

Undergraduate students should learn how to identify key findings, tailor messages to diverse audiences, and choose appropriate formats for presenting results. They must also understand the reasoning behind storytelling choices to ensure clarity, accuracy, and ethical communication. This skill set supports informed decision-making and enhances the impact of data science work.

## Competencies 

A data science graduate can design, evaluate, and deliver clear, accurate, and ethically responsible data stories by selecting appropriate narratives, visualizations, and communication modalities that are tailored to diverse audiences and support informed decision-making.

## Dispositions

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Evidence-Based Decision Making\]** by drawing and communicating conclusions that are appropriately supported and analytically sound.  
* Demonstrates **\[Critical Thinking\]** by selecting visualizations and narratives that accurately represent the underlying data while avoiding misleading interpretations.

**Professional Responsibility**

* Demonstrates **\[Professional Integrity\]** by communicating results honestly, transparently, and without distortion.  
* Demonstrates **\[Ethical Responsibility\]** by acknowledging uncertainty, assumptions, limitations, and potential biases in data communications.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Communication Effectiveness\]** by tailoring visualizations, narratives, and presentations to different audiences.  
* Demonstrates **\[Human-Centered Thinking\]** by designing communications that support accessibility, usability, and informed decision making.  
* Demonstrates **\[Inclusiveness\]** by creating data stories that are understandable, accessible, and respectful of diverse audiences and user needs.

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by producing accurate and well-designed visualizations and presentations.  
* Demonstrates **\[Continuous Improvement\]** by refining communication strategies using stakeholder feedback and new information.

## Knowledge Units 

* DS \- Audience awareness  
* DS \- Data communication tools and techniques  
* DS \- Effective narratives and presentations (oral and written)  
* DS \- Data visualization - See also [Specialization / Concentration](#specialization-/-concentration)

## DS \- Audience awareness

Audience awareness is the ability to adapt your message to the specific needs, expectations, and background of the people you're communicating with. For a data scientist, this means recognizing that different audiences—such as executives, technical teams, clients, or the general public—require different levels of detail, language, and emphasis. Executives may want high-level insights tied to business impact, while technical peers might expect methodological rigor and data specifics. Being audience-aware involves choosing the right visualizations, avoiding jargon when necessary, and framing the story in a way that resonates with the audience’s goals and concerns. It ensures that the data story is not only accurate but also engaging, relevant, and actionable for the people receiving it.

### Knowledge

#### *Core*

* Audience and personas identification  
* User-centered design  
* Appropriate detail in messaging   
* Message context  
* Identifying purpose of communication  
* Relevant accessibility requirements (e.g., Americans with Disabilities Act (ADA), European Accessibility Act (EAA))

#### *Specialization / Concentration* 

* N/A

### *Electives*

* N/A

### Skills

Recommended skill level: Understanding

* **Remembering:** Identify types of audiences and their characteristics (e.g., personas, levels of detail) to tailor communication effectively.  
* **Understanding:** Explain how an audience needs shape framing (e.g., executive vs. technical) to choose appropriate narrative depth.  
* **Applying:** Produce audience-appropriate communication (e.g., summary \+ appendix) aligned to purpose and constraints.  
* **Analyzing:** Examine communication effectiveness (e.g., clarity, accessibility, ethics)  
* **Evaluating:** Diagnose misalignment (e.g., jargon overload, unclear justification for decisions, too much detail about process) and revise for comprehension.  
* **Creating:** Design a repeatable audience strategy (e.g., stakeholder briefing template) for a new DS product area.

## DS \- Data communication tools and techniques

Data communication tools and techniques are essential in data storytelling because they enable data scientists to effectively translate complex analyses into clear, engaging, and actionable narratives. These tools—such as visualization platforms (e.g., Tableau, Power BI), programming libraries (e.g., Matplotlib, Seaborn, Plotly), and presentation software—help transform raw data into visual formats that are easier to understand and interpret. Techniques like choosing the right chart type, emphasizing key insights, and structuring the story logically ensure that the message resonates with the intended audience. Without strong communication tools and techniques, even the most sophisticated analysis can fail to make an impact. For data scientists, mastering these skills is crucial to bridge the gap between data and decision-making, ensuring that insights lead to informed actions.

### Knowledge

#### *Core*

* Graphic design principles  
* Data type influence on communication method  
* Styles and flow of data storytelling  
* Short text descriptions as a visualization method  
* Accessibility standards and best practices  
* Small and large group audience storytelling  
* Dashboards  
* Appropriate modalities and tools for different data types   
* Presentations that foster input and/or exploration of data  
* Misleading aspects of communication  
* Use of AI in generating communications (images, words, summaries)  
* Ethical principles in data storytelling and communications.  (See [Professionalism and Ethics (PE)](#professionalism-and-ethics-\(pe\)))  
* User-interface accessibility  
* Communication of underlying assumptions and potential biases  
* Visualization tools (See [DS \- Data visualization types](#skills-5))


#### *Specialization / Concentration* 

* Static versus dynamic visualizations   
* Specialized communication tools (e.g. D3JS or Tableau or PowerBI)  
* Visualization of big data

### *Electives*

* Storyboard or videos to communicate about data  
* Automate processes such as developing alt-text for images

### Skills

Recommended skill level: Applying

* **Remembering:** Define tools and design principles, accessibility standards,  (e.g., chart selection, accessibility) and identify appropriate tools to communicate accurately.  
* **Understanding:** Differentiate between different communication techniques.   
* **Applying:** Produce artifacts  (e.g., dashboards, reports) describing results for specific audience(s).   
* **Analyzing:** Distinguish the effectiveness and/or drawbacks offered by specific tools for given communication goal(s). **Evaluating:** Justify your choice of  methodology for presenting results for specific target audience(s).   
* **Creating:** Design an appropriate end-to-end communication workflow .

## DS \- Effective narratives and presentations

The ability to craft a compelling narrative and deliver effective presentations is just as critical as technical expertise. Data alone rarely speaks for itself; it requires context, interpretation, and storytelling to transform raw numbers into actionable insights. A well-structured narrative helps stakeholders understand not just what the data shows, but why it matters and how it should influence decisions. Presentations serve as the bridge between complex analysis and strategic impact, allowing data scientists to communicate findings clearly, persuade audiences, and drive change. Whether pitching a model to executives or sharing exploratory results with a cross-functional team, the power of narrative ensures that data science is not just informative, but influential.

### Knowledge

#### *Core*

* Interpreting visualizations  
* Static and dynamic visuals  
* Communication to different audiences  
* Use of feedback to improve communication  
* Pacing for the audience(s)

#### *Specialization*

* Effective communication of the limitations of a result  
* Effective communication of highly technical information to a general audience

### *Electives*

* Scrollytelling   
* Analysis of the data 

### Skills {#skills-5}

Recommended skill level: Understanding

* **Remembering:** Recall narrative structures and presentation practices (e.g., problem → evidence → recommendation), including accessibility standards.    
* **Understanding:** Explain how evidence supports claims and where uncertainty belongs to prevent overstatement.  
* **Applying:** Deliver a structured presentation (e.g., findings \+ limitations \+ actions) tailored to a defined decision.  
* **Analyzing:** Diagnose persuasion and comprehension gaps (e.g., missing context, weak causal claim) and correct or strengthen logic.  
* **Evaluating:** Evaluate the trade-offs of communication choices on stakeholders.  Adapt narrative quality (e.g., accuracy, defensibility, stakeholder alignment) using feedback and outcomes.  
* **Creating:** Design a narrative for an appropriate end-to-end communication workflow. 

## DS \- Data visualization 

Understanding different types of data visualizations is essential for data scientists because it enables them to present complex data in clear, intuitive, and impactful ways. Each visualization type—such as bar charts, line graphs, scatter plots, histograms, heatmaps, and box plots—serves a specific purpose, whether it's comparing categories, showing trends over time, revealing distributions, or identifying relationships between variables. Choosing the right visualization helps highlight key insights, supports accurate interpretation, and enhances communication with diverse audiences. Mastery of visualization types ensures that data scientists can effectively translate analytical findings into visual stories that drive understanding and decision-making. Note that for low vision and blind audiences, augmentations such as alternative text and modalities such as sonification may be necessary for people to be able to access information. 

#### *Core*

* Standard visualization types  
* Requirements for visualizations (e.g., axis range, labels, titles, keys, alt text)   
* Scaling   
* Tables or tabular data  
* Choosing an appropriate visualization for a set of data  
* Use of colour and shading   
* Accessibility for visualizations  
* Documentation of visualization processes and choices, such as filtering, missing or removed data

#### *Specialization*

* Dynamic visualizations   
* Topic-specific maps (e.g, weather, disease, choropleth)  
* Tree map  
* Multimedia or animated visualizations

### *Electives*

* Wordcloud

### Skills

Recommended skill level: Applying

* **Remembering:** Identify visualization types and common pitfalls (e.g., truncated axes) to avoid misleading graphics.  
* **Understanding:** Explain encoding choices and constraints (e.g., ordinal vs. nominal) to select correct visual forms.  
* **Applying:** Create accurate visuals with accessibility and labeling best practices.  
* **Analyzing:** Diagnose interpretability problems (e.g., overplotting, confounding scales) and redesign for clarity.  
* **Evaluating:** Judge visuals against criteria (e.g., accuracy, accessibility, ethics, audience fit) to defend design choices.  
* **Creating:** Design a coherent visualization system (e.g., dashboard style guide \+ reusable components) for a domain.

# Exploratory Data Analysis (EDA)  {#exploratory-data-analysis-(eda)}

Exploratory Data Analysis (EDA) is the process of investigating datasets to uncover their key characteristics using summary statistics, visualizations, and basic analytical techniques. It serves as a foundational step in the data science workflow, guiding decisions about data preparation and modeling. The primary goals of EDA are to identify patterns, detect anomalies, test assumptions, and understand the structure and relationships within the data.

Through EDA, data scientists gain insights that inform data cleaning, feature selection, and model development. It also helps reveal potential issues such as missing values, outliers, or inconsistencies that could affect downstream analysis. By interpreting data in context, EDA supports the creation of accurate, reliable, and interpretable models.

Undergraduate students should learn to apply statistical summaries and visual tools to assess data distributions, relationships, and quality. They should also understand how EDA informs the broader analytical process and be able to communicate findings effectively. Developing these skills enables students to approach data critically and make informed decisions throughout the data analysis lifecycle.

## Competencies 

A data science graduate can analyze and evaluate complex datasets using exploratory data analysis techniques to identify patterns, anomalies, and data quality issues, and can communicate findings responsibly and transparently to inform subsequent modeling and decision-making.

## Dispositions

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Statistical Thinking\]** by understanding  data variability, distributions, relationships, and uncertainty before formal modeling.  
* Demonstrates **\[Analytical Reasoning\]** by identifying meaningful patterns, anomalies, trends, and hypotheses in the data. Demonstrates **\[Critical Thinking\]** by evaluating data quality, assumptions, potential sources of bias, and limitations throughout the EDA process.  
* Demonstrates **\[Professional Skepticism\]** by recognizing that findings require validation before being interpreted as evidence or causal conclusions.

**Professional Responsibility**

* Demonstrates **\[Professional Integrity\]** by thoroughly documenting exploratory methods, assumptions, transformations, and limitations transparently.  
* Demonstrates **\[Data Stewardship\]** by responsibly handling data to avoid bias, protect data integrity and security, and meet applicable standards and laws. .

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Communication Effectiveness\]** by clearly communicating findings, uncertainty, and potential implications to technical and non-technical audiences.  
* Demonstrates **\[Collaboration\]** by working with domain experts to interpret preliminary findings  within the appropriate application context.

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by ensuring exploratory analyses are accurate, reproducible, and well documented.  
* Demonstrates **\[Curiosity and Discovery\]** by examining data from multiple perspectives to generate new questions, hypotheses, and opportunities for further investigation.  
* Demonstrates **\[Continuous Improvement\]** by refining analyses as additional data, domain knowledge, and feedback become available.

## Knowledge Units

* EDA \- Data cleaning and data quality assurance  
* EDA \- Data type guided exploration   
* EDA \- Data clustering methods  
* EDA \- Exploratory data visualization

## EDA \- Data Cleaning and Data Quality Assurance

Data cleaning is important at the early stages of data exploration to identify potential problems in the data.  These problems could include typos, missing values, incorrectly entered data, alternative spellings or abbreviations (such as “street” or “st.”), data presented in different units that may have been joined without proper conversion.  Note that this is a good time to also step back to look at the larger context of the data to think about any “missingness” left from the data collection process that could be small or large scale.  See [DA \- Data Integration and Operability](#skills-6) and [DA \- Data Wrangling](https://docs.google.com/document/d/1T-PROQb83PS7mZS-tzUsoKUOWfOLG7e2/edit#heading=h.5oijebjv4mci). 

### Knowledge

#### *Core*

* Data cleaning   
* Data dictionary creation and evaluation  
* Data transformation   
* Harmonizing data elements  
* Quality:  Bias, fairness, and completeness of data (See [DA \- Data Quality](#skills-7) and [Machine Learning (ML)](https://docs.google.com/document/d/1T-PROQb83PS7mZS-tzUsoKUOWfOLG7e2/edit#heading=h.iv576824gp47))

#### *Specialization / Concentration*

* Cleaning data for Time Series  
* Data cleaning for multivariate analysis   
* Advanced anomaly detection techniques  
* Effective and responsible use of predictive/generative AI for EDA  
* Adherence of data to the model 

### *Electives*

* Advanced linear regression  
* Exploratory data analysis for specialized data types  
* Functions in a coding language used for advanced EDA

### Skills

Recommended skill level: Applying

* **Remembering:** Recognize common data-quality checks and pitfalls (e.g., duplicates, leakage) to work reliably.  
* **Understanding:** Explain how quality issues propagate into metrics and downstream models (e.g., bias from missingness) to avoid misuse.  
* **Applying:** Perform  cleaning \+ QA workflows (e.g., transformations, validation rules, summary checks) to prepare data for analysis.  
* **Analyzing:** Detect  root causes (e.g., upstream instrumentation, schema drift) and their impacts on outcomes.  
* **Evaluating:** Assess data readiness against defined thresholds and governance constraints to support go/no-go decisions.  
* **Creating:** Develop an automated QA framework (e.g., tests, alerts, contracts) for scalable reliability.

## EDA \- Data Type Guided Exploration

A data scientist needs to understand how to handle both structured and unstructured data because each type presents unique challenges and opportunities for extracting meaningful insights. Structured data, such as numerical tables or databases, is highly organized and lends itself well to traditional statistical analysis and machine learning models. In contrast, unstructured data—such as text, images, audio, and video—requires specialized techniques, including natural language processing and computer vision, to interpret and analyze. Since real-world data is often messy and diverse, the ability to preprocess, integrate, and model different data types allows data scientists to build more comprehensive and accurate solutions. This versatility not only improves the quality of insights but also enables data-driven decision-making across a wide range of industries and applications. (See [DA \- Data types](#data-acquisition-is-the-foundational-process-of-gathering-raw-data-from-appropriate-sources-to-support-analysis,-modeling,-and-informed-decision-making.-as-the-first-step-in-the-data-science-lifecycle,-it-involves-identifying-relevant-data-sources—such-as-databases,-sensors,-apis,-web-platforms,-and-surveys—and-applying-appropriate-methods-to-collect-and-organize-data.-this-stage-is-critical-for-ensuring-that-the-data-is-complete,-accurate,-and-representative-of-the-problem-being-addressed,-laying-the-groundwork-for-all-subsequent-data-wrangling,-analysis,-and-modeling-tasks.))

### Knowledge

#### *Core*

* Descriptive Statistics (See [SF \- Descriptive Statistics](#skills-8) )  
* Qualitative vs quantitative data  
* Observational vs experimental data  
* Survey data  
* Design awareness (weighting and stratification, cross-tabulations and pivot tables)  
* Textual data  
* Graph/Network data  
* Time Series vs cross-sectional vs longitudinal 

#### *Specialization / Concentration*

* Time Series Data  
* Trend, seasonality, and noise decomposition  
* Lag analysis and autocorrelation  
* Rolling statistics and smoothing  
* Time-based indexing and resampling

### *Electives*

* Geographical Data  
* Genomic or Biological Data  
* Image Data  
* Video Data  
* Audio Data

### Skills {#skills}

Recommended skill level: Understanding

* **Remembering:** Identify exploratory methods by data type (e.g., time series, categorical) to choose appropriate summaries.  
* **Understanding:** Explain how exploratory methods differ by type (e.g., seasonality, sparsity) to avoid invalid comparisons.  
* **Applying:** Conduct appropriate EDA (e.g., segmentation, temporal plots) to generate initial insights.  
* **Analyzing:** Articulate anomalies and patterns (e.g., heterogeneity, subgroup effects) to inform modeling decisions.  
* **Evaluating:** Critique hypotheses and candidate features for plausibility and bias risk using evidence from EDA.  
* **Creating:** Generate an EDA protocol (e.g., checklist \+ notebook template) tuned to a domain’s data modalities.

## EDA \- Data Clustering Methods

Data clustering models are essential in exploratory data analysis because they help uncover hidden patterns and natural groupings within a dataset without requiring prior labels or assumptions. By organizing data into clusters based on similarity, these models enable data scientists to identify meaningful structures, such as customer segments, behavioral trends, or anomalies, that may not be immediately apparent through summary statistics alone. Clustering also aids in simplifying complex datasets, guiding feature selection, and informing subsequent modeling decisions. Ultimately, it provides a powerful way to explore and interpret data, especially when the goal is to understand relationships and variation within large, unlabeled datasets.

### Knowledge

#### *Core*

* Partitioning methods  
* Hierarchical methods  
* Density-based methods  
* When to choose a particular number of clusters  
* electing an appropriate distance metric  
* Sensitivity analysis 

#### *Specialization / Concentration*

* Handling high-dimensional data  
* Specialized visualization tools for clustering  
* Evaluating the effectiveness of clustering  
* Anomaly detection using clustering

### *Electives*

* Clustering of data in particular subjects, such as genetics  
* Unbalanced data or data requiring many cluster sizes  
* Scalability of clustering methods for large or rapidly changing datasets

### Skills {#skills-9}

Recommended skill level: Applying

* **Remembering:** Recall clustering concepts and pitfalls (e.g., k-means assumptions, scaling sensitivity).  
* **Understanding:** Explain distance metrics and structure assumptions (e.g., spherical clusters) to select suitable methods.  
* **Applying:** Perform clustering with preprocessing and validation (e.g., scaling, silhouette) for a defined exploratory goal.  
* **Analyzing:** Diagnose instability and sensitivity (e.g., initialization, parameter choice) using robustness checks.  
* **Evaluating:** Validate clustering appropriateness (e.g., interpretability, actionability, bias risk) before operational use.  
* **Creating:** Design a clustering workflow (e.g., feature pipeline \+ stability evaluation) for a novel segmentation need.

## EDA \- Exploratory Data Visualization

Exploratory data visualization is a vital component of exploratory data analysis, as it enables data scientists to intuitively and efficiently detect patterns, trends, and anomalies that may be difficult to uncover through raw numbers alone. Visual tools such as scatter plots, histograms, box plots, and heatmaps help reveal relationships between variables, distributions, and outliers, offering immediate insights into the structure and behavior of the data. These visualizations not only guide further analysis by highlighting areas of interest or concern but also support more transparent communication of findings to stakeholders who may not be familiar with statistical methods. Ultimately, visualization transforms complex data into accessible, actionable knowledge. See [DS \- Data visualizations](#skills-5) in Data Storytelling for a different use of data visualization.

### Knowledge

#### *Core*

* Univariate visualizations (show distributions, highlight median, quartiles, and outliers, compare frequencies, and show proportions)  
* Bivariate visualizations (show relationships, compare categories)  
* Use of generative AI to get ideas about possible types of visualizations  
* Addressing ADA compliance and other needs of users in communications  
* Initial formulation of hypotheses to be tested

#### *Specialization / Concentration* {#specialization-/-concentration}

* Multivariate visualizations (show correlation and categorical relationships)  
* Interactive visualizations  
* Dimensionality reduction visuals  
* Time Series visualizations (rolling averages, seasonal decomposition and lag plots)

### *Electives*

* Geospatial visualizations 

### Skills

Recommended skill level: Understanding

* **Remembering:** Identify common exploratory plots and pitfalls (e.g., ADA compliance) to explore effectively.  
* **Understanding:** Explain what each visual can and cannot support (e.g., correlation vs. causation) to avoid overclaims.  
* **Applying:** Produce exploratory visuals (possibly with generative AI tools) to inform hypotheses.  
* **Analyzing:** Articulate issues (e.g., skew, heteroscedasticity) to guide transformations and models.  
* **Evaluating:** Critique whether visuals support a hypothesis and what uncertainty remains to guide next steps.  
* **Creating:** Construct an exploratory visualization for rapid DS iteration.

# Machine Learning (ML)  {#machine-learning-(ml)}

Machine learning in data science is the study and application of computational and statistical methods that enable systems to learn patterns, relationships, and structures from data in order to make predictions, classifications, decisions, or discoveries without being explicitly programmed for each task. Within data science, machine learning provides a framework for transforming data into actionable knowledge through predictive modeling, pattern discovery, anomaly detection, recommendation, automation, and intelligent decision support.

Machine learning draws upon statistics, computer science, mathematics, and domain expertise. Statistical learning contributes the theoretical foundations for learning from data, including model selection, generalization, uncertainty, and evaluation. Computer science and mathematics contribute the algorithms, optimization methods, and computational systems needed to train, deploy, and scale machine learning solutions. Domain experts contribute the critical context needed to interpret data, guide feature engineering, and evaluate whether a model's predictions are reliable.  Data science integrates these perspectives within an end-to-end workflow that includes data preparation, model development, evaluation, deployment, monitoring, and continuous improvement.

The Machine Learning Competency Area encompasses foundational principles of learning from data, knowledge discovery and data mining, supervised and unsupervised learning, reinforcement learning, deep learning and generative AI, and the systems required to operationalize machine learning at scale. Graduates should understand how to select appropriate learning approaches, engineer and evaluate models, assess their limitations and biases, communicate results, and deploy and monitor machine learning systems in real-world environments.

## Competencies 

A data science graduate can select, develop, evaluate, deploy, and monitor machine learning models and systems to discover patterns, generate insights, make predictions, support decision-making, and automate data-driven processes. Graduates can apply supervised, unsupervised, reinforcement, and deep learning methods; assess model performance, fairness, robustness, and interpretability; and design scalable, ethical, and responsible machine learning solutions that address real-world problems.

## Dispositions

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Statistical Thinking\]** by selecting, validating, and interpreting machine learning models using sound statistical principles.  
* Demonstrates **\[Analytical Reasoning\]** by identifying machine learning methods appropriate to the problem, data characteristics, and desired outcomes.  
* Demonstrates **\[Critical Thinking\]** by ensuring that model assumptions and evaluation processes are accurate, reasonable, and well justified.   
* Demonstrates **\[Professional Skepticism\]** by critically assessing model predictions, generalizability, uncertainty, and limitations before deployment.  
* Demonstrates **\[Evidence-Based Decision Making\]** by selecting models based on empirical evaluation rather than perceived complexity or popularity.

**Professional Responsibility**

* Demonstrates **\[Responsible AI Use\]** by developing and deploying machine learning systems ethically, transparently, and with appropriate human oversight.  
* Demonstrates **\[Ethical Responsibility\]** by considering fairness, privacy, accountability, and potential unintended consequences throughout the model lifecycle.  
* Demonstrates **\[Professional Integrity\]** by honestly and completely communicating model assumptions, limitations, uncertainty, and appropriate use.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Human-Centered Thinking\]** by developing machine learning solutions that consider user requirements, fairness, and interpretability.  
* Demonstrates **\[Communication Effectiveness\]** by explaining model behavior, evaluation results, and uncertainty to technical and non-technical stakeholders.  
* Demonstrates **\[Collaboration\]** by working effectively with domain experts and other stakeholders throughout model development, evaluation, and deployment.

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by validating, testing, monitoring, and documenting machine learning models for reliability and reproducibility.  
* Demonstrates **\[Continuous Improvement\]** by refining models through evaluation, monitoring, and user feedback regularly throughout the model’s lifecycle.  
* Demonstrates **\[Continuous Learning\]** by adapting to advances in machine learning methods, tools, and best practices.

## Knowledge Units

* ML \- ML foundations  
* ML \- Supervised learning   
* ML \- Unsupervised learning  
* ML \- ML systems  
* ML \- Reinforcement learning


## ML \- ML Foundations

### Machine learning foundations provide the conceptual framework that underlies the development, evaluation, and application of machine learning systems in data science. These foundations encompass the principles of learning from data, including how models are represented, trained, evaluated, and selected. They introduce the concepts of features, training and testing data, hypothesis spaces, optimization, generalization, and model performance. Understanding machine learning foundations enables data scientists to make informed choices about algorithms, data preparation, model evaluation, and deployment strategies rather than treating machine learning as a collection of black-box techniques. These concepts provide the basis for supervised, unsupervised, reinforcement, and deep learning approaches while emphasizing the importance of responsible, reproducible, and evidence-based model development.

### Knowledge

#### *Core*

* Learning paradigms (supervised, unsupervised, reinforcement, semi-supervised) and conditions under which each is appropriate  
* Training, validation, and test sets  
* Data quality, representativeness, and sampling (See [SF \- Study design](#sf---study-design), [RM \- Designing surveys,](#rm---designing-surveys)  and [DA \- Data Context, Sources and Types)](#da---data-context,-sources-and-types)  
* Feature engineering and feature selection  
* Model selection  (See  [SM \- Model selection](#sm---model-selection))  
* Loss functions and objective functions   
* Cross-validation  
* Overfitting and underfitting  
* Bias-variance tradeoff (See [SM \- Model Diagnostics](#sm---model-diagnostics) )  
* Generalizability and scope of inference  
* Model interpretability and explainability (See [SM \- Interpretation of Models](#sm---interpretation-of-models) )  
* Optimization (See [MF \- Calculus](#mf---calculus))  
* Dimension reduction (e.g., principal component analysis, discriminant analysis)


*Specialization / Concentration*

* Statistical learning theory  
* Regularization methods  
* Probabilistic machine learning   
* Bayesian learning (See [PD \- Foundation](#pd---foundation))  
* Causal learning fundamentals  
* Interpretable ML

### *Electives*

* TBA

### Skills

Recommended skill level: Creating

* **Remembering**: Identify common machine learning terminology, workflows, model types, and evaluation metrics used in data science.  
* **Understanding**: Explain how machine learning models learn from data and how factors such as features, training data, and evaluation methods influence model performance.  
* **Applying**: Build a model by preparing data, select features, train models, and apply appropriate evaluation procedures to solve data-driven problems.  
* **Analyzing**: Diagnose issues such as overfitting, underfitting, data leakage, bias, variance, and poor generalization to improve model effectiveness.  
* **Evaluating**: Evaluate the suitability of machine learning approaches, model conditions, performance metrics, and validation strategies for a given problem.  
* **Creating**: Design reproducible machine learning workflows that integrate data preparation, model development, evaluation, and ethical considerations.

## ML \- Supervised learning

Supervised learning is important for data scientists because it provides a structured framework for building predictive models using labeled data, where the outcome or target variable is known. This approach allows data scientists to train algorithms to recognize patterns and relationships between input features and desired outputs, enabling accurate predictions on new, unseen data. Supervised learning is foundational in tasks such as classification (e.g., spam detection, disease diagnosis) and regression (e.g., forecasting sales or prices), making it widely applicable across industries. It also offers clear evaluation metrics, like accuracy or mean squared error, which help assess model performance and guide improvements. By mastering supervised learning, data scientists can develop reliable, interpretable, and scalable solutions to real-world problems.

### Knowledge

#### *Core*

* Distinction between regression and classification  
* Model training  
* Linear and logistic regression  
* Decision trees  
* Random forests ()  
* k-Nearest Neighbors  
* Naive Bayes  
* Evaluation strategies  
* Continuous improvement for supervised learning

#### *Specialization / Concentration*

* Recommender systems  
* Non-parametric models  
* Support vector machines  
* Time series forecasting  
* EnsemblesNeural networks and deep learning (See [AI \- Deep learning (DL)](#ai---deep-learning-\(dl\)))  
* Semi-supervised learning

### *Electives*

* Hyperparameter tuning (grid vs random search)  
* Active learning  
* Bayesian ML 

### Skills {#skills-1}

Recommended skill level: Creating

* **Remembering:** Recall when each supervised learning method is appropriate and what conditions are necessary for its use. .  
* **Understanding:** Interpret model results, describe the application of ML foundational skills (e.g. bias-variance, feature selection, etc.) in context, and recognize the importance of continuous improvement.    
* **Applying:** Implement a supervised pipeline (model choice → features → train → validate → test → interpret).  
* **Analyzing:** Determine ability to generalize results to a research question and translate the results into actionable recommendations.  
* **Evaluating:** Justify and critique selection of model and/or modelling choices.   
* **Creating:** Formulate a feedback loop process to continuously improve model performance. 

## ML \- Unsupervised learning

Unsupervised learning is a type of machine learning where the algorithm analyzes data without predefined labels, outcomes, or research questions, aiming to uncover hidden patterns, groupings, or structures within the dataset. This approach is important for data scientists because it allows them to explore and understand data in situations where labeled examples are unavailable or costly to obtain. Techniques such as clustering, dimensionality reduction, and anomaly detection help identify natural groupings, simplify complex data, and reveal insights that might not be immediately obvious. By mastering unsupervised learning, data scientists can perform exploratory data analysis, data mining, detect unusual behavior, and generate hypotheses that guide further investigation or model development, making it a powerful tool for discovery and innovation. 

### Knowledge

#### *Core*

* Proximity measurements  
* Evaluating decisions with sensitivity, specificity  
* Clustering  
* Cluster hypothesis formulation and testing  
* The role of visualization (See [EDA \- Exploratory Data Visualization](#skills-9))  
* Measuring distance (e.g. nearest neighbor)  
* Bias in and limitations of training data  
* Mining various data types (e.g. such as spatial, temporal, text, image) (See EDA \- Data Type Guided Exploration)


#### *Specialization / Concentration*

* Hierarchical clustering  
* Density-based clustering  
* Scalable data mining and out-of-core algorithms (e.g. large-scale pattern discovery)  
* Streaming algorithms  
* Association rule mining  
* Anomaly detection  
* Sequential pattern mining  
* Similarity search  
* Pattern interestingness measures

### *Electives*

* N/A

### Skills

Recommended skill level: Evaluating

* **Remembering:** Recall when each unsupervised method is appropriate and what conditions are necessary for its use.  
* **Understanding:** Interpret model results in context, and recognize the importance of continual improvement.  
* **Applying:** Implement unsupervised methods for exploration and hypothesis generation.  
* **Analyzing:** Diagnose instability and sensitivity (e.g., preprocessing dependence) using robustness checks and data segmentation (e.g., slicing, sampling) and translate the results into actionable follow-up.  
* **Evaluating:** Justify and critique selection of model and/or modelling choices.  
* **Creating:** Formulate a feedback loop process to continually improve model performance. 

## ML \- ML Systems

Systems refer to the frameworks and processes that enable machines to learn from data and improve their performance over time without being explicitly programmed for every task. These systems are important for data scientists because they provide the foundation for building intelligent applications that can automate decision-making, adapt to new information, and scale across large datasets. Understanding machine learning systems involves not only knowing algorithms but also how to design, deploy, monitor, and maintain models in real-world environments. This includes managing data pipelines, ensuring model fairness and accuracy, handling feedback loops, and integrating models into production systems. For data scientists, mastering machine learning systems is essential to move beyond experimentation and deliver impactful, reliable solutions that solve complex problems across industries.

The environmental and financial costs of running machine learning algorithms is important and covered in [Professionalism and Ethics (PE)](#professionalism-and-ethics-\(pe\)). 

### Knowledge

#### *Core*

* Data/task parallelism (Spark, Hadoop, Dask)  (See [CF \- Parallel and Distributed Computing (PDC)](#cf---parallel-and-distributed-computing-\(pdc\)))  
* Detecting patterns  
* Transfer learning

#### *Specialization / Concentration*

* Recommender systems (See [ML \- Supervised learning](https://docs.google.com/document/d/1T-PROQb83PS7mZS-tzUsoKUOWfOLG7e2/edit#heading=h.kndxx0b2cvui))  
* Online and Offline systems   
* GPUs vs CPUs (See [CF \- Parallel and Distributed Computing (PDC)](#cf---parallel-and-distributed-computing-\(pdc\)))  
* Tensor flow framework

### *Electives*

* N/A

### Skills

Recommended skill level: Understanding

* **Remembering:** Recall ML system components (e.g., pipelines, registries, monitoring) to communicate operational needs.  
* **Understanding:** Explain production constraints (e.g., drift, feedback loops) to avoid “notebook-only” solutions.  
* **Applying:** Deploy or integrate models into a system (e.g., batch scoring, API) with monitoring and retraining triggers.  
* **Analyzing:** Diagnose production failures (e.g., data drift, latency spikes) using logs and telemetry to restore reliability.  
* **Evaluating:** Assess system design against reliability, safety, cost, and compliance constraints to support decisions.  
* **Creating:** Design an end-to-end ML system (e.g., MLOps pipeline) for a new product requirement.


## ML \- Reinforcement learning

Reinforcement learning is a type of machine learning where an agent learns to make decisions by interacting with an environment and receiving feedback in the form of rewards or penalties based on its actions. This approach is important for data scientists because it enables the development of systems that can learn optimal strategies over time, especially in dynamic or complex environments where explicit supervision is not feasible. Reinforcement learning is widely used in areas such as robotics, game playing, recommendation systems, and autonomous vehicles, where decision-making must adapt to changing conditions. By understanding reinforcement learning, data scientists can design models that improve through experience, handle sequential decision problems, and contribute to cutting-edge applications that go beyond traditional supervised or unsupervised learning.

### Knowledge

#### *Core*

* Reinforcement learning concepts and evaluation  
* The concept  of rewards  
* Q-learning fundamentals  
* States, actions, and policies

#### *Specialization / Concentration*

* Agents and environments  
* Exploration versus exploitation  
* Markov decision processes

### *Electives*

* Rewards and value functions  
* Selection of reward functions  
* Model-based reinforcement learning 

### Skills

Recommended skill level: Understanding

* **Remembering:** Recall reinforcement learning concepts.  
* **Understanding:** Explain reward mechanisms.  
* **Applying:** Implement a simple reinforcement learning algorithm (e.g., policy learning in a simulator).  
* **Analyzing:** Examine the balance of exploration and exploitation for a specific algorithm.   
* **Evaluating:** Assess reinforcement learning suitability vs. alternatives (e.g., offline supervised) considering risk, cost, and safety criteria.  
* **Creating:** Design a reward and evaluation protocol (e.g., safety constraints, offline evaluation plan) for a new reinforcement learning use case.

# Mathematical Fundamentals (MF) {#mathematical-fundamentals-(mf)}

Topics from discrete mathematics, linear algebra, and calculus are critical pillars of the mathematical foundation for data science. Discrete mathematics equips data scientists with tools for understanding logic, set theory, combinatorics, and graph theory—essential for algorithm design, data structures, and modeling relationships in networks and databases. Linear algebra provides the language for representing and manipulating data efficiently, especially in high-dimensional spaces, and is central to machine learning algorithms like principal component analysis, support vector machines, and neural networks. Calculus, particularly differential calculus, is vital for optimization tasks, such as training machine learning models through gradient descent and understanding how small changes in input affect output. Together, these disciplines enable data scientists to build robust models, analyze complex systems, and derive insights from data with mathematical rigor.

## Competencies 

A data science graduate can apply topics from discrete mathematics, linear algebra, calculus, and coding theory to model data, analyze algorithmic and statistical behavior, optimize machine learning processes, and reason rigorously about data-driven systems and their limitations.

## Dispositions  \- DRAFT VERSION

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Analytical Reasoning\]** by applying mathematical principles to formulate, analyze, and solve data science problems.  
* Demonstrates **\[Critical Thinking\]** by evaluating mathematical assumptions, approximations, and limitations underlying analytical methods.  
* Demonstrates **\[Evidence-Based Decision Making\]** by selecting mathematical techniques appropriate for the characteristics of the data and analytical objectives.

**Professional Responsibility**

* Demonstrates **\[Professional Integrity\]** by applying mathematical methods accurately while acknowledging assumptions, limitations, and sources of approximation.  
* Demonstrates **\[Accountability\]** by taking responsibility for the mathematical correctness and validity of analytical work.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Communication Effectiveness\]** by explaining mathematical concepts, assumptions, and reasoning clearly to technical and non-technical audiences.  
* Demonstrates **\[Collaboration\]** by working with interdisciplinary teams to translate mathematical concepts into practical data science solutions.

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by applying mathematical methods rigorously and consistently.  
* Demonstrates **\[Continuous Learning\]** by strengthening mathematical knowledge to support emerging analytical methods and technologies

## Knowledge Units

* MF \- Discrete Mathematics  
* MF-  Linear Algebra  
* MF \- Calculus  
* MF \- Coding Theory (Properties of codes and their fitness for their applications.)

## MF \- Discrete Mathematics {#mf---discrete-mathematics}

Discrete mathematics is a vital discipline for data scientists because it provides the theoretical foundation for many core concepts in computing and data analysis. It includes topics such as logic, set theory, combinatorics, graph theory, and probability—all of which are essential for designing algorithms, modeling data relationships, and understanding the structure of datasets. For example, graph theory is used to analyze social networks and recommendation systems, while combinatorics helps in feature selection and understanding the complexity of models. Logical reasoning and Boolean algebra are fundamental in constructing decision trees and rule-based systems. Discrete mathematics also supports the development of efficient data structures and algorithms, which are crucial for handling large-scale data and optimizing performance in machine learning applications.

### Knowledge

#### *Core*

* Mathematical notation in data science  
* Counting, and its relevance to big data (also in Probability. See [Counting (permutations and combinations)](https://docs.google.com/document/d/1T-PROQb83PS7mZS-tzUsoKUOWfOLG7e2/edit#bookmark=id.wzv4f5jcqmi2)  
* Methods of proof (such as induction)  
* Error propagation due to use of discrete numbers in algorithms  
* Graph Theory  
* Logic and truth tables  
* Orders of magnitude, big O notation (See [CA \- Complexity analysis](#skills-10))  
* Moments: central and raw moments (also in [Probability and Distributions (PD)](https://docs.google.com/document/d/1T-PROQb83PS7mZS-tzUsoKUOWfOLG7e2/edit#heading=h.ncdceyipn970). See [Moment generating functions](https://docs.google.com/document/d/1T-PROQb83PS7mZS-tzUsoKUOWfOLG7e2/edit#bookmark=id.ebvggrxfmdb4))  
* Predicate calculus  
* Recurrence relations and their solution  
* Scope of inference  
* Sensitivity analysis  
* Discrete Optimization (e.g., Linear Programming, Integer Programming)  
* Inductive and deductive logic

#### *Specialization / Concentration*

* Hashing  
* NP completeness  
* Approximate algorithms (See [Computing Algorithms (CA)](#computing-algorithms-\(ca\)))

### *Electives*

* Number theory

### Skills

Recommended skill level: Applying

* **Remembering:** Recall discrete concepts (e.g., logic, graphs, induction) to reason and communicate precisely.  
* **Understanding:** Explain how discrete structures support algorithms and DS systems (e.g., graphs in networks) to avoid misuse.  
* **Applying:** Use discrete tools (e.g., proof ideas, graph reasoning) to justify correctness or constraints in DS solutions.  
* **Analyzing:** Diagnose structural properties (e.g., connectivity, recurrence behavior) to improve algorithmic decisions.  
* **Evaluating:** Judge assumptions and proofs for validity and relevance to a DS context (e.g., scalability implications).  
* **Creating:** Design a discrete model (e.g., graph representation, constraint formulation) for a novel data problem.  
   

## MF \- Linear Algebra

Linear algebra is essential for data scientists because it provides the mathematical foundation for representing and manipulating data efficiently. Many machine learning algorithms rely on linear algebra to organize and store information, model relationships, optimize performance, and handle high-dimensional data. For example, linear regression uses matrix operations to estimate coefficients that best fit the data, while principal component analysis (PCA) applies eigenvectors and eigenvalues to reduce dimensionality and uncover patterns. Algorithms like support vector machines (SVMs) and logistic regression use dot products and vector spaces to classify data, and neural networks depend heavily on matrix multiplication to propagate inputs through layers. Recommendation systems use matrix factorization techniques like singular value decomposition (SVD). In short, linear algebra enables data scientists to build scalable, efficient, and interpretable models across a wide range of applications.

### Knowledge

#### *Core*

* Representing data in vectors and matrices  
* Matrix operations (addition, multiplication, transposition, dot product, cross product)  
* Matrix factorization (vector norms, matrix norms, SVD, QR, NMF, Cholesky, LU)  
* Transformations, projections and encoding relationships  
* Eigenvalues and eigenvectors  
* Systems of linear equations  
* Rank and linear independence  
* Norms and distance metrics

#### *Specialization / Concentration*

* Positive definite and semi-definite matrices

### *Electives*

* Parallel Numerical Methods  
* Sparse matrices and compressed representations  
* Universal approximation property  
* Tensor Algebra

### Skills

Recommended skill level: Applying

* **Remembering:** Recall matrix/vector operations and concepts (e.g., eigenvalues, SVD) to work efficiently.  
* **Understanding:** Explain how linear transformations underpin ML (e.g., embeddings, PCA) to choose methods appropriately.  
* **Applying:** Apply matrix methods (e.g., PCA, linear regression formulation) in DS workflows for defined tasks.  
* **Analyzing:** Diagnose numerical issues (e.g., conditioning, rank deficiency) to improve stability and interpretability.  
* **Evaluating:** Judge method suitability (e.g., PCA assumptions, interpretability needs) with clear criteria and rationale.  
* **Creating:** Design a representation or transformation (e.g., feature projection) adapted to a new dataset constraint.


## MF \- Calculus {#mf---calculus}

Topics from the field of Calculus are important for data scientists because it provides the tools for modeling and optimization processes that use data. In particular, differential calculus is used to compute gradients, which are essential for training machine learning models through techniques like gradient descent—a method that adjusts model parameters to minimize error. Partial derivatives help in understanding how changes in individual features affect the output of multivariable functions, which is key in deep learning and optimization. Integral calculus can be useful in probability theory, especially when working with continuous distributions and calculating expected values. Overall, calculus topics enable data scientists to build models that learn efficiently, make accurate predictions, and adapt to complex patterns in data.

### Knowledge

#### *Core*

* Introduction to notation   
* Conceptual approach to differentiation and chain rule  
*  Conceptual and numerical approach to limits and convergence  
* Taylor’s Theorem for iteration and approximation  
* Mathematical modeling using functions  
* Conceptual and numerical approaches to integral Calculus  
* Introduction to the notation and concept of partial derivatives  
* Conceptual and numerical approaches to minimizing and maximizing functions


#### *Specialization / Concentration*

* Partial Derivatives

### Concepts from Real Analysis  (continuity)

### *Electives*

* Continuous Optimization (e.g., Convex, Non-Linear, Genetic Algorithms)


### Skills

Recommended skill level: Understanding

* **Remembering:** Recall situations where derivatives are relevant and what they represent.    
* **Understanding:** Explain how gradients drive machine learning (e.g., loss minimization) and where issues arise (e.g., local minima). Explain how integrals are used in computations with probability density functions.  
* **Applying:** Use gradients conceptually or computationally (e.g., interpret gradient descent behavior) in modeling.  
* **Analyzing:** Diagnose optimization problems (e.g., exploding gradients) and select mitigations (e.g., learning rate schedules).  
* **Evaluating:** Judge performance of optimization algorithms (e.g., convergence vs. compute) using evidence and constraints.  
* **Creating:** Design a training/optimization plan (e.g., objective \+ regularization) for a situation that requires modeling.


## MF \- Coding Theory

This topic is about generating codes for purposes such as minimizing space or attempting to keep information secret. This includes data compression which results in reduced time to transmit files, and reduced storage requirements.

### Knowledge

#### *Core*

* Information theory (coding methods, entropy)  
* Data compression (Lossy/Lossless compression)  
* Cryptography  
* The use of keys in cryptography  
* The concept of public keys and private keys  
* The RSA algorithm

#### *Specialization / Concentration*

* Quantum considerations in cryptography

### *Electives*

* N/A

### Skills

Recommended skill level: Applying

* **Remembering:** Recall compression and cryptography basics (e.g., entropy, Huffman coding) to reason about data handling.  
* **Understanding:** Explain trade-offs across different compression and cryptography  techniques.  
* **Applying:** Apply coding theory in DS practice (e.g., storage efficiency, secure and speedy transfer) using correct configurations.  
* **Analyzing:** Diagnose risks and errors (e.g., compression artifacts, key management issues) to protect integrity and privacy.  
* **Evaluating:** Assess approaches by criteria (e.g., fidelity, security, cost) and defend choices to stakeholders.  
* **Creating:** Design a data handling strategy.

# Probability and Distributions (PD) {#probability-and-distributions-(pd)}

Probability and distributions are essential components of a data scientist’s toolkit, providing the foundation for understanding uncertainty and variability in data. Probability theory enables students to model and reason about uncertain events, which is critical for tasks such as forecasting, risk assessment, and experimental design. Statistical distributions, meanwhile, help characterize data behavior, identify patterns and anomalies, and support the application of appropriate analytical techniques.

In an undergraduate data science curriculum, students learn to apply key concepts such as conditional probability, independence, expectation, variance, and common probability distributions (e.g., normal, binomial, Poisson). They explore how these concepts underpin core data science methods, including hypothesis testing, regression analysis, machine learning algorithms, and Bayesian inference. An undergraduate program should emphasize both theoretical understanding and practical application, ensuring students can interpret probabilistic models, assess assumptions, and make sound data-driven decisions.

## Competencies

A data science graduate can model, analyze, and reason about uncertainty using probability theory and statistical distributions, applying concepts such as random variables, moments, and convergence to support inference, assess risk, and make sound data-driven decisions.

## Dispositions \- DRAFT VERSION

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Statistical Thinking\]** by reasoning appropriately about randomness, variability, probability, and uncertainty.  
* Demonstrates **\[Critical Thinking\]** by evaluating probabilistic assumptions, distributional choices, and limitations of statistical models.  
* Demonstrates **\[Analytical Reasoning\]** by selecting probability models appropriate to the data and research questions.  
* Demonstrates **\[Professional Skepticism\]** by recognizing that probabilistic conclusions always involve uncertainty and should be interpreted cautiously.

**Professional Responsibility**

* Demonstrates **\[Professional Integrity\]** by communicating probabilistic findings honestly while acknowledging uncertainty and assumptions.  
* Demonstrates **\[Ethical Responsibility\]** by avoiding overstatement of confidence or certainty when interpreting probabilistic results.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Communication Effectiveness\]** by explaining probability, risk, and uncertainty clearly to technical and non-technical audiences.  
* Demonstrates **\[Human-Centered Thinking\]** by presenting uncertainty in ways that support informed decision making.

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by validating probabilistic assumptions and applying probability methods rigorously.  
* Demonstrates **\[Curiosity and Discovery\]** by exploring probabilistic behavior to gain deeper insight into complex data.

## Knowledge Units

* PD \- Convergence  
* PD \- Foundation  
* PD \- Moments  
* PD \- Random variables

## PD- Convergence

Convergence in distributions is a crucial concept for data scientists, as it underpins many statistical methods and machine learning algorithms that rely on the behavior of large samples. It describes how the distribution of a sequence of random variables behaves as the sample size grows, often approaching a limiting distribution such as the normal distribution. This is crucial for understanding the Central Limit Theorem, which enables data scientists to make inferences about population parameters using sample statistics, even when the population distribution is unknown.  Convergence also plays a key role in validating model performance, ensuring that estimators become more accurate and stable as more data is collected. Without this knowledge, a data scientist might misinterpret results or apply statistical techniques inappropriately, leading to unreliable conclusions.

### Knowledge

#### *Core*

* Law of Large Numbers  
* Central Limit Theorems 

#### *Specialization / Concentration*

* Convergence in probability  
* Convergence in distribution   
* Unbiasedness  
* Consistency

### *Electives*

* N/A

### Skills

Recommended skill level: Understanding

* **Remembering:** State the Law of Large Numbers (LLN), the Central Limit Theorem (CLT) .  
* **Understanding:** Explain why estimators stabilize with more data and when they do not to avoid invalid inference.     
* **Applying:**  Apply LNN or CLT theorems to simple random sampling.   
* **Analyzing:** Diagnose finite-sample issues (e.g., heavy tails, dependence) that undermine convergence assumptions.  
* **Evaluating:** Assess  whether asymptotic reasoning is appropriate given data conditions and risk constraints.  
* **Creating:** Formulate situations where LLN and CLT apply.

## PD \- Foundation {#pd---foundation}

The foundation of probability and statistics begins with sets and operations, which provide the mathematical language for describing outcomes. Using counting principles, we determine the number of possible arrangements or selections in a given situation. These tools help define sample spaces, the collection of all possible outcomes of an experiment, and events, which are subsets of those outcomes. Building on this, we assign probabilities to events to measure their likelihood, and express them as odds to compare the chance of occurrence versus non-occurrence.  Data scientists need this foundation to understand and use inferential statistics, the basics of probability, and modeling.  

### Knowledge

#### *Core*

* Sets and operations  
* Counting (permutations and combinations)  
* Events  
* Sample spaces  
* Basics of probabilities and odds  
* Conditional probability, Bayes’ Theorem  
* Simpson’s Paradox

#### *Specialization / Concentration*

* N/A

### *Electives*

* N/A

### Skills

Recommended skill level: Understanding

* **Remembering:** Recall sets, counting, events, probabilities and odds to reason precisely about uncertainty.  
* **Understanding:** Explain probability rules and conditioning to avoid common reasoning errors in DS decisions.  
* **Applying:** Compute and apply basic probability in DS contexts (e.g., base rates, sampling plans, Bayes updates).  
* **Analyzing:** Diagnose flawed probabilistic reasoning (e.g., confounding, aggregation artifacts) in reported results.  
* **Evaluating:** Assess assumptions about independence and representativeness to justify conclusions responsibly.  
* **Creating:** Formulate a probabilistic scenario for a decision or experiment. 

## PD- Moments

Moments in distributions are essential tools for data scientists because they summarize key characteristics of data in a compact and interpretable way. These insights guide data preprocessing, feature engineering, and model selection, and they are foundational in statistical inference and diagnostics. Without a grasp of moments, a data scientist may overlook important patterns or misinterpret the underlying structure of the data. 

### Knowledge

#### *Core*

* Expectation  
* Variance  
* Covariance/Correlation

#### *Specialization / Concentration* 

* Higher-order moments (e.g., skewness, kurtosis)  
* Moment generating functions

### *Electives*

* Central Moments   
* Cumulant generating functions

### Skills

Recommended skill level: Understanding

* **Remembering:** Recall expectation/variance and related summaries.  
* **Understanding:** Explain how moments characterize location, variation, and dependence and interpret their implications on risk and distributional shape.   
* **Applying:** Compute and use moments (e.g., variance for uncertainty, covariance for relationships) in DS workflows.  
* **Analyzing:** Detect distributional issues (e.g., heteroscedasticity, outliers) revealed by moment behavior.  
* **Evaluating:** Evaluate whether moment-based summaries are adequate (e.g., heavy tails) and defend reporting choices.  
* **Creating:** Design features or diagnostics (e.g., moment-based anomaly flags) for new modeling tasks.

## PD- Random Variables

By providing the mathematical foundation for modeling and analyzing data that involves uncertainty, the concept of a random variable provides the bridge between abstract probability theory and real-world measurable data, enabling the modeling of uncertainty in phenomena. Random variables have probability distributions, which are essential for statistical inference. They underpin many machine learning models, such as regression, Bayesian methods, and neural networks, and support techniques like Monte Carlo simulation, A/B testing, and reinforcement learning for decision-making under uncertainty. By treating uncertain outcomes as random variables, data scientists can simulate scenarios, quantify risk, and communicate probabilistic insights more effectively, ensuring predictions are interpretable and actionable.

### Knowledge

#### *Core*

* Distribution functions (Probability density function (PDF), Cumulative density function (CDF))  
* Discrete random variables and distributions (Bernoulli distribution, Binomial distribution, Poisson distribution, Uniform distribution)  
* Continuous random variables and distributions  
* Independence

#### *Specialization / Concentration* 

* Fundamental theorems of probability, independence  
* Discrete random variables and distributions:  
* Continuous random variables and distributions

### *Electives*

* N/A

### Skills {#skills-3}

Recommended skill level: Understanding

* **Remembering:** Define commonly used distributions   
* **Understanding:** Explain the properties of commonly used distributions. .  
* **Applying:** Use an appropriate probability distribution to formulate and implement data generating models.   
* **Analyzing:** Examine assumption violations (e.g., non-independence, non-normality) and predict  impacts on results.  
* **Evaluating:** Assess  modeling choices (e.g., distribution family) using fit, interpretability, and risk criteria.  
* **Creating:** Construct a probabilistic model (e.g., Bayesian formulation or simulation framework) for a new domain problem.

# Professionalism and Ethics (PE)  {#professionalism-and-ethics-(pe)}

Professionalism and ethics are vital components of a data science education, equipping students with the principles and practices necessary to navigate the complex social, legal, and ethical dimensions of working with data. As data science increasingly influences decisions in business, healthcare, government, and society at large, professionals in the field must uphold high standards of integrity, transparency, and accountability. Ethical data practices ensure that data is collected, analyzed, and communicated responsibly, with respect for privacy, fairness, and the broader societal impact.

In this area of the curriculum, students explore topics such as data privacy, informed consent, algorithmic bias, fairness, and the ethical implications of automated decision-making. They learn to identify potential risks and unintended consequences of data-driven solutions, and to apply frameworks for ethical reasoning in real-world scenarios. The scope also includes professional standards for collaboration, communication, and responsible conduct in research and industry settings. By developing a strong ethical foundation, students are prepared to make principled decisions, foster public trust, and contribute positively to their organizations and communities.

## Competencies 

A data science graduate can apply ethical reasoning, legal awareness, and professional standards to the responsible acquisition, analysis, deployment, and communication of data-driven solutions, demonstrating accountability, transparency, and respect for individuals, organizations, and society.

## Dispositions

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Critical Thinking\]** by identifying ethical dilemmas with competing stakeholder interests; foreseeing and reflecting on potential consequences of professional decisions.  
* Demonstrates **\[Evidence-Based Decision Making\]** by applying evidence, ethical frameworks, and professional standards to support responsible decision making.

**Professional Responsibility**

* Demonstrates **\[Ethical Responsibility\]** by consistently applying ethical principles, professional standards, and applicable laws throughout data science practice.  
* Demonstrates **\[Professional Integrity\]** by acting honestly, transparently, and responsibly in all professional activities.  
* Demonstrates **\[Accountability\]** by accepting responsibility for professional decisions, analyses, and recommendations.  
* Demonstrates **\[Data Stewardship\]** by protecting privacy, security, confidentiality, intellectual property, and responsible data governance adhering to applicable laws and professional standards.  
* Demonstrates **\[Responsible AI Use\]** by ensuring AI systems are developed and deployed ethically, transparently, and with appropriate human oversight.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Social Responsibility\]** by considering the societal, economic, environmental, and legal impacts in the practice of data science.  
* Demonstrates **\[Inclusiveness\]** by promoting fairness, accessibility, equity, and respect for diverse individuals and communities.  
* Demonstrates **\[Communication Effectiveness\]** by articulating ethical considerations, risks, and tradeoffs with stakeholders.

**Quality and Continuous Improvement**

* Demonstrates **\[Continuous Improvement\]** by incorporating evolving ethical standards, regulations, and professional best practices into professional practice.  
* Demonstrates **\[Continuous Learning\]** by remaining informed about emerging ethical issues, technologies, and societal expectations affecting data science.  
* Demonstrates **\[Attention to Quality\]** by ensuring professional work consistently meets high standards of accuracy, reliability, transparency, and accountability.

## Knowledge Units

* PE \- Data stewardship  
* PE \- Ethical and legal issues  
* PE \- Intellectual Property  
* PE \- Teamwork, leadership, and communications

## PE \- Data Stewardship {#pe---data-stewardship}

Data considerations, including responsible data collection, data privacy, and data governance, are essential for Data Scientists to practice, as these principles ensure that data is sourced and used ethically, legally, and effectively. Responsible data collection involves obtaining data transparently and with consent, which builds trust and ensures compliance with regulations. Data privacy protects individuals from misuse or exposure of sensitive information, which is critical in maintaining public confidence and avoiding legal consequences. Data governance provides the framework for managing data quality, access, and security across its lifecycle, ensuring that data remains accurate, consistent, and protected. Together, these considerations help data scientists uphold professional standards, reduce risk, and contribute to responsible innovation.  See [CF \- Computer Security](#skills-4)

### Knowledge

#### *Core*

* Responsible data collection   
* Data Security  
* Data Governance  
* Data protection regulations and laws  
* Data Bias  
* Principles and practices of data privacy   
* Authentication and authorization    
* Policies for data collection, backups, and retention

####  *Specialization / Concentration*

* Crime related to data science  
* Economic considerations, including environmental impact of running large compute-intensive projects. \- Sustainability (See CSC 2023 \- [https://csed.acm.org/wp-content/uploads/2023/09/SEP-Version-Gamma.pdf](https://csed.acm.org/wp-content/uploads/2023/09/SEP-Version-Gamma.pdf))  
* Freedom of Information Act 

### *Electives*

* N/A

### Skills {#skills-12}

Recommended skill level: Applying

* **Remembering:** Define stewardship terminology, concepts, and pitfalls (e.g., retention, access logging) to operating responsibly.  
* **Understanding:** Justify data governance, privacy, and bias mitigation decisions across the data lifecycle to avoid harm.  
* **Applying:** Apply stewardship practices (e.g., documentation, minimization, controls) in real DS workflows.  
* **Analyzing:** Diagnose stewardship risks (e.g., leakage, improper access) in real DS workflows and propose mitigations based on evidence.  
* **Evaluating:** Judge practices against compliance and trust criteria to defend decisions and prioritize remediations.  
* **Creating:** Design stewardship artifacts (e.g., data dictionaries, policies, controls) for a new dataset or project.

## PE \- Ethical and legal issues

The analysis and use of data has to be governed by attention to legal and ethical frameworks, and these may vary from country to country.  International guidelines can be important in this regard.

### Knowledge

#### *Core*

* Codes of ethics \- their role and applicability  
* Ethical considerations and ethical reasoning as a process.   
* Legal frameworks  
* Legal consideration  
* The role of international standards  
* Research integrity   
* Ethical guidelines from your professional organization(s)  
* Stakeholder engagement  
* Decision framing  
* FAIR and CARE principles   
* Accountability/Transparency  
* Belmont Principle (e.g., Respect, Beneficence, Justice)

#### *Specialization / Concentration*

### *Electives*

* N/A

### Skills

Recommended skill level: Applying

* **Remembering:** Recall ethical frameworks, principles, and legal constraints on the analysis and use of data .  
* **Understanding:** Explain how context changes ethical/legal obligations (e.g., jurisdiction, vulnerable populations) to avoid misuse.  
* **Applying:** Apply ethical reasoning and document legal checks (e.g., consent, fairness review) throughout a DS project lifecycle.  
* **Analyzing:** Detect ethical tensions (e.g., utility vs. privacy) and stakeholder impacts to refine decisions.  
* **Evaluating:** Critique  decisions by harm, compliance, transparency, and accountability criteria to evaluate ethical outcomes.  
* **Creating:** Design governance processes (e.g., review boards, escalation paths) for ethical and inclusive  DS operations.

## PE \- Intellectual Property

In today’s data-driven world, intellectual property (IP) awareness is increasingly essential for data scientists. As professionals who routinely create, use, and share digital assets—such as datasets, algorithms, models, and code—data scientists operate in a landscape where legal and ethical boundaries are shaped by IP laws. Understanding these boundaries helps ensure that their work respects the rights of others, avoids infringement, and contributes responsibly to the broader scientific and technological community.

For example, many datasets and software libraries come with specific licenses that dictate how they can be used, modified, or redistributed. A lack of familiarity with these licenses can lead to unintended violations, which may have legal or reputational consequences. Similarly, when data scientists develop novel algorithms or models, knowing whether these creations can be patented or protected as trade secrets can influence how their work is shared or commercialized.

Moreover, in collaborative environments—whether academic, corporate, or open-source—IP knowledge supports transparency and fairness. It helps data scientists properly attribute contributions, navigate data ownership issues, and understand institutional policies around publishing and sharing. This is especially important when working with proprietary or sensitive data, where misuse could breach confidentiality agreements or ethical standards.

Ultimately, intellectual property literacy empowers data scientists to innovate responsibly, collaborate effectively, and protect both their own work and the work of others. It’s not just a legal safeguard—it’s a cornerstone of professional integrity in the digital age.

### Knowledge

#### *Core*

* Basics of copyright, patents, and trademarks  
* Open-source software licenses  
* Data licensing and usage agreements  
* Institutional IP policies 

#### *Specialization / Concentration*

* N/A

### *Electives*

* N/A

### Skills {#skills-13}

Recommended skill level: Applying

* **Remembering:** Recall IP basics (e.g., copyright, OSS licenses) to avoid infringement.  
* **Understanding:** Explain how licensing affects permissible use and sharing (e.g., copyleft vs. permissive) to prevent violations.  
* **Applying:** Apply ethical IP practices (e.g., attribution, license compliance) when using datasets, code, and models.  
* **Analyzing:** Detect IP risks (e.g., incompatible dependencies) and propose remediation (e.g., replacement, permissions).  
* **Evaluating:** Justify distribution/sharing decisions against legal, reputational, and collaboration criteria.  
* **Creating:** Design an IP-compliant sharing plan (e.g., repository structure, notices) for a new DS deliverable.

## PE \- Teamwork, leadership, and communications

Teamwork, leadership, and communication are critical for data scientists because their work often intersects with multiple disciplines and impacts strategic decision-making. Effective teamwork enables collaboration with engineers, analysts, and business stakeholders, ensuring that data solutions are aligned with organizational goals. Leadership is essential not only for guiding projects and mentoring junior team members but also for championing ethical data practices and driving innovation. Clear communication allows data scientists to translate complex analyses into actionable insights that non-technical audiences can understand and trust. Together, these skills foster a productive, inclusive, and impact-driven data science environment.  (See [PM \- Communication, Documentation, and Team Management](#skills-11))

### Knowledge

#### *Core*

* Collaboration considerations and effective teamwork  
* Transparency   
* Different forms of communication, including effective communication to diverse audiences  
* Ability to advocate a point of view with evidence  
* Methods for anticipating and modeling the impact of work on individuals, communities, economies, and environments  
* Effective leadership qualities, techniques and requirements

#### *Specialization / Concentration* 

* Software support for teamwork and effective communication  
* Different team models  
* Leadership models

### *Electives*

* N/A

### Skills

Recommended skill level: Applying

* **Remembering:** Recall the benefits of collaboration and considerations for working teams. Identify roles (e.g., RACI, review norms) to coordinate effectively.  
* **Understanding:** Explain how communication choices affect trust and adoption (e.g., framing uncertainty) to avoid misalignment.  
* **Applying:** Illustrate collaboration practices in cross-functional settings (e.g., shared specs, review cycles) to deliver DS outcomes.  
* **Analyzing:** Diagnose team process failures (e.g., unclear ownership, mis-scoped tasks) and improve collaboration patterns.  
* **Evaluating:** Judge communication and leadership approaches (e.g., transparency, inclusivity) against project outcomes.  
* **Creating:** Design team processes (e.g., decision logs, review rituals) that improve DS delivery and accountability.

# Project Management (PM)  {#project-management-(pm)}

Project Management in data science involves the strategic planning, coordination, and execution of data-driven initiatives to achieve specific research or business objectives. As data science projects often span multiple disciplines and require collaboration among diverse teams, students must learn how to manage workflows, timelines, resources, and stakeholder expectations effectively. This Competency Area emphasizes the importance of aligning technical efforts with organizational goals, ensuring that data science solutions are not only technically sound but also actionable and impactful.  
The scope of project management in a data science curriculum includes understanding the full data science lifecycle—from problem definition and data acquisition to modeling, evaluation, and deployment. Students learn best practices for organizing team roles, fostering interdisciplinary collaboration, and managing transitions between project phases. They are introduced to tools and methodologies for workflow management, version control, and documentation.  In addition, students should be introduced to effective use of AI for project management topics.

## Competencies 

A data science graduate can plan, coordinate, and manage data science projects across the full analytic lifecycle by organizing workflows, engaging stakeholders, ensuring ethical and regulatory compliance, and delivering reproducible, well-documented, and actionable outcomes.

## Dispositions

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Analytical Reasoning\]** by supporting the evaluation of  project risks, resource requirements, dependencies, and tradeoffs throughout the project lifecycle.  
* Demonstrates **\[Critical Thinking\]** by providing alternative project approaches and identifying potential obstacles based on changing circumstances.

**Professional Responsibility**

* Demonstrates **\[Accountability\]**  by taking responsibility for the accuracy, quality, and timely completion of assigned analyses, models, and deliverables in support of the project.   
* Demonstrates **\[Professional Integrity\]** by communicating project status, risks, assumptions, and limitations honestly and transparently to project managers.  
* Demonstrates **\[Ethical Responsibility\]** by ensuring projects comply with applicable legal, ethical, privacy, and organizational requirements.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Collaboration\]** by working effectively with multidisciplinary teams and diverse stakeholders throughout the project lifecycle.  
* Demonstrates **\[Communication Effectiveness\]** by communicating project objectives, progress, risks, and outcomes clearly to appropriate audiences.  
* Demonstrates **\[Human-Centered Thinking\]** by considering stakeholder needs when planning, prioritizing, and executing project activities.

**Quality and Continuous Improvement**

* Demonstrates **\[Continuous Improvement\]** by refining project processes through evaluation, retrospectives, and lessons learned.  
* Demonstrates **\[Attention to Quality\]** by ensuring project deliverables meet defined requirements, quality standards, and stakeholder expectations.  
* Demonstrates **\[Continuous Learning\]** by adopting improved project management practices, methodologies, and tools.

## Knowledge Units

* PM \- Project planning and governance.  
* PM \- Workflow practices  
* PM \- Communication, Documentation, and Team Management  

## PM \- Project planning and governance {#pm---project-planning-and-governance}

Project planning and governance are critical in data science because they ensure that work stays aligned with business goals, uses resources efficiently, and delivers trustworthy, actionable results. Good planning clarifies objectives, timelines, and dependencies, reducing wasted effort and surprises. Governance provides structure for decision-making, risk management, compliance with regulations, and ethical use of data, which is especially important when models impact people or business processes. Together, they create transparency, accountability, and repeatability—key factors in building stakeholder trust and successfully moving data science solutions from experimentation to production. 

### Knowledge

####  *Core*

* Project scope   
* Project breakdown   
* Project resources  
* Project monitoring (Performance and success metrics, Governance)  
* Legal and ethical compliance (See [PE \- Ethical and legal issues](#skills-12))  
* Bias, privacy, fairness, regulatory (See [Professionalism and Ethics (PE)](#professionalism-and-ethics-\(pe\)))  
* AI tools for project planning, monitoring and success metrics

####  *Specialization / Concentration*

* N/A

### *Electives*

* N/A

### Skills {#skills-15}

Recommended skill level: Understanding

* **Remembering:** Recall planning artifacts and processes (e.g., scope, milestones, metrics) to manage work transparently.  
* **Understanding:** Explain how governance ensures trust (e.g., risk controls, compliance) to prevent unmanaged harm.  
* **Applying:** Build a project plan (e.g., Work Breakdown Structure,, success metrics) aligned to stakeholders and DS lifecycle stages.  
* **Analyzing:** Diagnose plan risks (e.g., dependency fragility, data availability, data security) and adapt the plan with evidence.  
* **Evaluating:** Evaluate a  project plan  against its success criteria (e.g., value, risk, ethics, cost)..  
* **Creating:** Design an improved project plan and governance model (e.g., stage gates, model risk reviews) for a new program context.

## PM \- Workflow Practices

Workflow practices are essential in data science because they bring structure, consistency, and reproducibility to complex, iterative work. Clear workflows—covering data collection, cleaning, modeling, validation, and deployment—help teams collaborate effectively, avoid duplication of effort, and maintain version control of code, data, and models. They also make experiments traceable and results auditable, which is crucial for compliance, debugging, and scaling solutions. Well-defined workflows ultimately accelerate development, improve quality, and ensure that insights can be trusted and acted upon confidently.

### Knowledge

#### *Core*

* Reproducibility  
* Version Control  (See [SW \- Programming Fundamentals](#a-strong-understanding-of-software-engineering-and-programming-is-essential-for-data-science-students-to-develop-effective,-reliable,-and-scalable-solutions.-students-begin-by-learning-core-programming-concepts-such-as-control-structures,-data-types,-and-object-oriented-design.-they-also-explore-software-engineering-practices-including-modular-design,-testing,-version-control,-and-documentation-to-ensure-their-code-is-maintainable-and-collaborative.))  
* Automation  
* AI tools to support automation and version control

#### *Specialization / Concentration*

* N/A

### *Electives*

* N/A

### Skills {#skills-11}

Recommended skill level: Understanding

* **Remembering:** Define workflow fundamentals (e.g., reproducibility, versioning) to execute consistently.  
* **Understanding:** Explain why workflows matter (e.g., auditability, collaboration) to permit validation, review and reproducibility, preventing “one-off” and other failures.  
* **Applying:** Use workflow tools (e.g., Git, pipelines) to make DS experiments reproducible and traceable.  
* **Analyzing:** Diagnose workflow breakdowns (e.g., undocumented changes, brittle pipelines) and strengthen reliability.  
* **Evaluating:** Judge workflow maturity (e.g., repeatability, reviewability) against project needs and constraints.  
* **Creating:** Design an automated workflow (e.g., Continuous Integration checks, scheduled retraining, and deployment) for a new DS product lifecycle.

## PM \- Communication, Documentation, and Team Management

Communication, documentation, and team management are vital in data science because they bridge the gap between technical work and business impact. Clear communication ensures that stakeholders understand goals, progress, and results, enabling better decisions. Thorough documentation preserves knowledge, supports reproducibility, and makes it easier for others to review, maintain, or extend work. Effective team management aligns diverse roles—data scientists, engineers, analysts, and business partners—so efforts are coordinated, deadlines are met, and resources are used efficiently. Together, these practices foster collaboration, transparency, and trust, which are critical for delivering successful data science outcomes.  See also [PE \- Teamwork, leadership, and communications](#skills-13)

### Knowledge

#### *Core*

* Project documentation   
* Project visualizations  
* Project final reports  
* Conflict management with version control systems  
* Communication with internal and external audiences  (See also [*Data Storytelling (DS)*](#skills-14)*)*  
* DevOps  
* AI tools to support documentation


#### *Specialization / Concentration*

* N/A

### *Electives*

* N/A

### Skills

Recommended skill level: Applying

* **Remembering:** Recall documentation best-practices  (e.g., assumptions, data lineage).  
* **Understanding:** Explain how documentation supports reproducibility and stakeholder trust to avoid misinterpretation.  
* **Applying:** Produce usable documentation and status communications (e.g., model cards, reports) for a defined project.  
* **Analyzing:** Diagnose communication gaps (e.g., unclear decisions, missing rationale) and improve alignment and delivery.  
* **Evaluating:** Appraise  documentation quality against criteria (e.g., completeness, clarity, auditability) to support reuse.  
* **Creating:** Design a documentation system (e.g., templates, decision logs) for consistent DS team performance.

# Research Methods and Experimental Design (RM) {#research-methods-and-experimental-design-(rm)}

Research Methods and Experimental Design are essential for ensuring that data science investigations are methodologically sound, reproducible, and capable of generating valid insights. This area equips students with the skills to critically evaluate data sources, formulate testable hypotheses, and design robust experiments or observational studies. Understanding how to structure inquiries and control for confounding variables is key to producing reliable and unbiased results.

The scope of this Competency Area includes foundational concepts such as sampling techniques, randomization, statistical testing, and principles of reproducibility. Students learn to select appropriate research designs—such as controlled experiments, quasi-experiments, and surveys—based on the nature of the data and research questions. Emphasis is placed on the ethical conduct of research, proper documentation, and the interpretation of results in context. By mastering these methods, students are prepared to conduct rigorous analyses, assess the validity of findings, and contribute to evidence-based decision-making in both academic and applied data science settings.

## Competencies 

A data science graduate can design, conduct, document, and evaluate ethical and reproducible empirical investigations by formulating testable hypotheses, selecting appropriate study and experimental designs, applying sound sampling and statistical principles, and interpreting results to support valid, evidence-based conclusions.

## Dispositions

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Evidence-Based Decision Making\]** by designing and conducting investigations that produce valid, reliable, and reproducible evidence.  
* Demonstrates \[**Critical Thinking\]** by formulating and evaluating research questions and study designs, assessing threats to validity, and judging the strength of evidence.  
* Demonstrates **\[Analytical Reasoning\]** by selecting appropriate experimental designs, sampling methods, and analytical techniques.  
* Demonstrates **\[Professional Skepticism\]** by critically evaluating research findings before drawing conclusions or making recommendations.

**Professional Responsibility**

* Demonstrates **\[Professional Integrity\]** by conducting research honestly, transparently, and ethically.  
* Demonstrates **\[Ethical Responsibility\]** by protecting research participants and complying   with applicable legal, regulatory, ethical and professional standards.  
* Demonstrates **\[Accountability\]** by accurately reporting research methods, analyses, findings, and limitations.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Communication Effectiveness\]** by communicating research methods, findings, uncertainty, and limitations clearly to diverse audiences.  
* Demonstrates **\[Collaboration\]** by working effectively with interdisciplinary teams and stakeholders.  
* Demonstrates **\[Human-Centered Thinking\]** by designing studies that consider participant needs, accessibility, and societal impacts.

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by conducting reproducible, well-documented, and methodologically sound research.  
* Demonstrates **\[Curiosity and Discovery\]** by pursuing meaningful research questions and exploring innovative investigative approaches.  
* Demonstrates **\[Continuous Improvement\]** by refining research questions, methods, and analyses through iterative evaluation and feedback.

## Knowledge Units

* RM \- Designing surveys  
* RM \- Reproducibility Experiment version control   
* RM \- Ethics in Research  
* RM \- Principles of Design of Experiments   
* RM \- Scientific Method 

## RM \- Designing surveys {#rm---designing-surveys}

Knowing how to design surveys directly impacts the quality and reliability of the data analyzed by a Data Scientist. A well-designed survey ensures that the questions are clear, unbiased, and aligned with the research objectives, which helps in collecting accurate and meaningful responses. It also involves thoughtful planning around sampling, question types, and data validation, all of which contribute to minimizing errors and maximizing the usefulness of the data. Poor survey design results in misleading results, wasted resources, and flawed conclusions. By mastering survey design, data scientists can gather high-quality data that supports robust statistical analysis, drives informed decision-making, and ultimately leads to more impactful insights. In a case where representativeness is relevant then sampling principles must be applied.  (See [SF \- Study design](#sf---study-design))

### Knowledge

#### *Core*

* Best practices for reliable, reproducible surveys question  
* Survey question formats (multiple choice, Likert scale, ranking, open-ended, demographics)  
* Logical Flow of Surveys  
* Best practices and how to evaluate survey length  
* Plan for missing data defined  
* Threats to validity 

#### *Specialization / Concentration* 

* N/A

### *Electives*

* Skip pattern  
* The procedures for analyzing open-ended survey questions  
* Translate and back-translate if working in a technical survey or foreign language survey

### Skills

Recommended skill level:  Understanding

* **Remembering:** Recall survey formats and validity threats y.  
* **Understanding:** Explain how wording and structure influence bias and measurement error.  
* **Applying:** Design a survey instrument (e.g., flow, missingness plan) aligned to a defined research question.  
* **Analyzing:** Examine and reduce bias risks (e.g., leading questions, nonresponse).  
* **Evaluating:** Evaluate  survey quality using reliability criteria,validity criteria, and stakeholder constraints.  
* **Creating:** Design an improved survey protocol (e.g., pilots, translation plan) for a new population or setting.

## RM \- Ethics in Research  

Data scientists must ensure that data is collected, stored, and analyzed responsibly, respecting privacy, consent, and fairness. Ethical considerations help prevent harm, such as biased algorithms that reinforce discrimination or misuse of personal information. Moreover, transparency and accountability in data practices build trust with stakeholders and the public. As data-driven systems increasingly shape healthcare, finance, education, and governance, ethical awareness empowers data scientists to make decisions that are not only technically sound but also socially responsible and aligned with broader human values.  (See [PE \- Ethical and legal issues](#skills-12))

### Knowledge

#### *Core*

* Codes of ethics  
* Other ethical concerns

#### *Specialization / Concentration* 

* Humane treatment of human and animal subjects  
* Institutional Review Board and participants' rights and welfare  
* Belmont Principle (e.g., Respect, Beneficence and Justice)

#### *Electives* 

* N/A

### Skills

Recommended skill level: Understanding.

* **Remembering:** Recall research code of ethics.  
* **Understanding:** Explain ethical obligations in study contexts (e.g., consent, participant protection).  
* **Applying:** Apply relevant ethical procedures (e.g., IRB workflow, de-identification) .  
* **Analyzing:** Diagnose ethical risks (e.g., sensitive inference, unequal burdens) and implement mitigations.  
* **Evaluating:** Evaluate  study plans against ethical criteria and defend decisions.  
* **Creating:** Design a research ethics protocol (e.g., consent \+ retention \+ transparency plan) for a new study or new context.

## RM \- Principles of Design of Experiments

Principles of experimental design are crucial for data scientists to establish causality, ensure validity and reliability, and control for biases and confounding variables in their findings. A well-designed experiment provides a structured roadmap for data collection and analysis, leading to trustworthy conclusions and saving valuable time and resources by preventing flawed designs that could lead to incorrect and costly decisions. By applying these principles, data scientists can produce more reliable, actionable insights and contribute to evidence-based decision-making.

### Knowledge

#### *Core*

* Analysis of designed experiments \- Analysis of Variance (ANOVA)  
* Common designs of experiments (e.g,full factorial designs, fractional factorial designs, confounding)  
* Experimental Factors (e.g. treatments, blocks, covariates)  
* Local control and bias control   
* Random assignment Replication, reproducibility

####  *Specialization / Concentration* 

* Multiple Comparisons  
* Analysis of Covariance (ANCOVA)  
* Response surface methodology and central composite designs  
* Nested factor designs

### *Electives*

* Multivariate ANOVA  
* Multivariate ANCOVA  
* Split-plot designs  
* Imbalanced designs  
* Optimal Designs

### Skills

### Recommended skill level: Analyzing

* **Remembering:** Recall experimental design components (e.g., random assignment, blocking).  
* **Understanding:** Explain how design choices affect causality and validity.  
* **Applying:** Design an experiment aligned to a defined research  question.  (See [SF \- Study design](#sf---study-design))  
* **Analyzing:** Diagnose design weaknesses (e.g., confounding, insufficient replication).  
* **Evaluating:** Evaluate and justify (e.g., by validity, feasibility, ethics, and efficiency criteria)  a  design methodology.   .  
* **Creating:** Formulate an improved experimental design for a novel constraint or scenario.

## RM \- Scientific Method

The scientific method is a cornerstone of rigorous inquiry. For data scientists, it provides a disciplined approach to solving problems and generating reliable insights. By following its structured steps—formulating hypotheses, designing experiments, collecting data, analyzing results, and drawing conclusions—data scientists ensure that their work is reproducible and logically sound. This method helps guard against confirmation bias, encourages critical thinking, and supports evidence-based decision-making. 

### Knowledge

#### *Core*

* Scientific method principles  
* Steps/Cycle and the inherently iterative nature of the scientific process  
* Control or comparison group (i.e, definition, importance, relevance)  
* Independent versus dependent variables  
* 

####  *Specialization / Concentration* 

* Deductive Logic (See [MF \- Discrete Mathematics](#mf---discrete-mathematics))  
* Inductive Logic  
* Falsifiability (a hypothesis must be disprovable)  
* Verifiability  (experiments must be replicable)

### *Electives*

* Peer Review   
* Replication   
* Reproducibility of results

### Skills

Recommended skill level: Evaluating

* **Remembering:** Define the scientific method.  
* **Understanding:** Explain falsifiability and control logic.  
* **Applying:** Formulate testable hypotheses and run analyses aligned to the method (e.g., pre-specified metrics).  
* **Analyzing:** Diagnose threats to inference (e.g., confounding, p-hacking) and strengthen methodology.  
* **Evaluating:** Judge findings by evidence strength, reproducibility, and limitations to support credible claims.  
* **Creating:** Design a rigorous investigation plan (e.g., preregistration \+ replication strategy) for a new question.

# Software Engineering, Programming, Development (SW) {#software-engineering,-programming,-development-(sw)}

A strong understanding of software engineering and programming is essential for data science students to develop effective, reliable, and scalable solutions. Students begin by learning core programming concepts such as control structures, data types, and object-oriented design. They also explore software engineering practices including modular design, testing, version control, and documentation to ensure their code is maintainable and collaborative.

To support efficient development, students are introduced to essential tools such as code editors, version control systems like Git, and deployment frameworks. These tools help manage workflows and facilitate the transition from prototype to production, enabling data scientists to build robust applications that meet real-world need

## Competencies 

A data science graduate can design, implement, test, document, and maintain reliable and scalable data-driven software by applying sound programming practices, software engineering principles, development tools, and user-centered design considerations to move analytical solutions from prototype to production.

## Dispositions

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Critical Thinking\]** by identifying core programming challenges and solution approaches through problem decomposition.  
* Demonstrates **\[Evidence-Based Decision Making\]** by selecting software technologies, development tools, and implementation strategies based on technical requirements and empirical evaluation.

**Professional Responsibility**

* Demonstrates **\[Responsible AI Use\]** by verifying the quality and correctness of code or software generated using AI-tools  to ensure human oversight and accountability.    
* Demonstrates **\[Professional Integrity\]** by developing software that is transparent, maintainable, and appropriately documented.  
* Demonstrates **\[Accountability\]** by taking responsibility for software reliability, security, and testing. .

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Collaboration\]** by contributing effectively to software development using shared coding standards, version control, and peer review.  
* Demonstrates **\[Communication Effectiveness\]** by producing clear software documentation and by appropriately explaining  technical decisions to different audiences.  
* Demonstrates **\[Human-Centered Thinking\]** by designing software that supports usability, accessibility, and maintainability.

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by writing software tests that are maintainable and demonstrate full coverage for all units. .  
* Demonstrates **\[Continuous Improvement\]** by improving software through testing, automation, refactoring, and continuous integration practices.

## Knowledge Units

* SW \- Programming fundamentals  
* SW \- Software Engineering fundamentals  
* SW \- Support for software development  
* SW \- Human Computer Interaction


## SW \- Programming Fundamentals

Programming is a necessary skill for a data scientist because it provides the tools to collect, clean, analyze, and visualize data efficiently, enabling them to uncover patterns, build predictive models, and communicate insights effectively. It allows automation of repetitive tasks, handling of large datasets, and implementation of statistical and machine learning techniques, all of which are essential for making data-driven decisions in real-world scenarios.

### Knowledge

#### *Core*

* Constructs of imperative programming   
* Software specification  
* Functional decomposition  
* Object-oriented programming  
* Software design principles  
* Testing and debugging   
* Designing for maintainability  
* Software documentation and clean code practices  
* Use of Artificial Intelligence to improve software programming

#### *Specialization / Concentration* 

* Formal specification languages  
* Program verification  
* Security and privacy (See [CF \- Computer Security](#skills-4))  
* Large-scale software development   
* Version control (See [PM \- Workflow Practices](#skills-15))  
* Maturity models 

### *Electives*

* N/A

### Skills

Recommended skill level: Understanding

* **Remembering:** Recall core constructs and pitfalls in software coding choices (e.g., state bugs, off-by-one).  
* **Understanding:** Explain design choices (e.g., OOP vs. functional decomposition) for writing maintainable code.  
* **Applying:** Implement data science workflows (e.g., ETL scripts, model training code) with testing and documentation.  
* **Analyzing:** Diagnose defects and performance issues (e.g., profiling, debugging).  
* **Evaluating:** Evaluate code quality (e.g., readability, test coverage, security) in supporting collaboration and reuse.  
* **Creating:** Design reusable components (e.g., library module, pipeline template) for new data science team needs.

## SW \- Software Engineering Fundamentals

Software engineering is the discipline associated with the development of large, and often critical, software systems. Data scientists may enlist the help of software engineers or collaborate with them. They therefore benefit from an understanding of the basic elements of the discipline.

### Knowledge

#### *Core*

* The role of software engineering and data science  
* The discipline of software engineering  
* Change management to ensure orderly evolution and to include version control

#### *Specialization*

* The software life cycle  
* The different phases of the life cycle, including specification, design and implementation  
* Ensuring high quality at each phase, these characterised by code being robust, yet easy to understand, lack of complexity, visibility these being supported by metrics  
* Harnessing details about tests, reviews, measures, proofs, etc so that they can be available for possible reuse in the event of some change  
* Change management to ensure orderly evolution and to include version control  
* Maintenance, all but inevitable in big projects, is facilitated by the above consideration

### *Electives*

* N/A

### Skills

Recommended skill level: Applying

* **Remembering:** Recall lifecycle concepts (e.g., requirements, QA, change management).  
* **Understanding:** Explain how engineering discipline supports data science products (e.g., reliability, maintainability).  
* **Applying:** Use engineering practices (e.g., reviews, CI checks) moving data science prototypes toward production.  
* **Analyzing:** Diagnose system failures and propose refactoring or process improvements.  
* **Evaluating:** Assess engineering approaches for specific product needs (e.g., safety, scalability) that  justify investment.  
* **Creating:** Design a delivery process (e.g., release workflow, quality gates) suited to a data science product lifecycle.

## SW \- Support for software development

A data scientist, while not a software developer, can leverage tools for software development to more efficiently process data.  

### Knowledge

#### *Core*

* AI tools in software development    
* Data Scientist Programming Language Fundamentals (Python, R, SQL)  
* Data science libraries or Application Programming Interface (APIs)  
* Open-source development  
* Automation and pipelines  
* Quality assurance

#### *Specialization / Concentration* 

* Completeness and representativeness of data  
* Graphical representation  
* Matrix or tensor representation  
* Scripting languages (Shell/Bash, JavaScript)

### *Electives*

* N/A

### Skills

Recommended skill level: Applying

* **Remembering:** Recall DS languages/libraries and common pitfalls (e.g., dependency conflicts).  
* **Understanding:** Explain software tool choice trade-offs (e.g., library choice, API constraints) for quality code development.  
* **Applying:** Use tools (e.g., notebooks, pipelines, APIs) to build reliable data science solutions with automation where appropriate.  
* **Analyzing:** Detect tooling failures (e.g., environment drift, brittle dependencies) and stabilize the stack.  
* **Evaluating:** Assess tooling choices for reproducibility, performance, cost, and maintainability.  
* **Creating:** Construct a development environment standard (e.g., containers, dependency policy) for scalable data science work.

## SW \- Human Computer Interaction

Human-computer interaction (HCI) enables users to interact with computer systems. The quality of that interface significantly affects usability in all its forms. It encompasses a wide range of technologies, including applications developed that use animation, visualization, simulation, speech recognition, video   (of faces, handwriting, etc.), and graphics.  This is important for Data Scientists developing applications to learn how to create and utilize tools for analyzing and presenting data. 

### Knowledge

#### *Core*

* N/A (See Visualization section for data presentation and analysis) 

#### *Specialization / Concentration*

* The various possible roles of an interaction, issues associated with addressing the main possibilities  
* Implications of collaborative activity  
* Characteristics of high-quality interface design  
* Approaches to the evaluation of interfaces, including walkthroughs, experiments, and heuristics  
* Consideration of color, multimedia, speech recognition, animation, touch, and gestures  
* Data-driven applications (with a database back end)  
* Handling failure, help facilities  
* Addressing accessibility considerations with, at a minimum, ADA user standards.  See [DS \- Data communication tools and techniques](https://docs.google.com/document/d/1T-PROQb83PS7mZS-tzUsoKUOWfOLG7e2/edit#heading=h.jsb0f2414cc1)  
* User interaction standards

### *Electives*

* N/A

### Skills

Recommended skill level: Understanding

* **Remembering:** Recall HCI concepts (e.g., usability heuristics, accessibility).  
* **Understanding:** Explain how interface choices influence interpretation (e.g., default views, interaction bias).  
* **Applying:** Build or improve an interface element (e.g., dashboard filters, explanation panel) for a defined user task.  
* **Analyzing:** Diagnose usability issues (e.g., error-prone workflows) using evaluation evidence to improve experience.  
* **Evaluating:** Judge interface quality against accessibility, clarity, and user-success criteria.  
* **Creating:** Develop an interaction model (e.g., exploratory analysis app flow) for a novel data science application need.

# Statistical Fundamentals (SF) {#statistical-fundamentals-(sf)}

Statistical fundamentals play a central role in data science by providing the tools and frameworks needed to make sense of data, draw valid conclusions, and quantify uncertainty. The scope includes core concepts such as probability, sampling, distributions, hypothesis testing, and confidence intervals. Understanding these concepts allows data scientists to design experiments, model relationships, interpret their results, and evaluate the reliability of their findings. Statistical thinking helps distinguish real patterns from noise, avoid biased interpretations, and ensure that data-driven decisions are grounded in evidence rather than coincidence. A solid understanding of these principles is essential for building trustworthy models, performing rigorous analyses, and communicating results with clarity and credibility.

## Competencies 

A data science graduate can design studies, summarize and explore data, quantify uncertainty, and draw valid statistical inferences by applying core statistical principles to evaluate evidence, assess reliability, and support sound, ethical data-driven decisions.

## Dispositions \- DRAFT VERSION

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Statistical Thinking\]** by reasoning appropriately about variability, uncertainty, inference, and study design.  
* Demonstrates **\[Critical Thinking\]** by evaluating assumptions, bias, sampling methods, and limitations of statistical analyses.  
* Demonstrates **\[Analytical Reasoning\]** by selecting statistical methods appropriate to the data, research question, and scope of inference.  
* Demonstrates **\[Professional Skepticism\]** by critically interpreting statistical evidence before drawing conclusions.

**Professional Responsibility**

* Demonstrates **\[Professional Integrity\]** by communicating statistical findings honestly while acknowledging assumptions, limitations, and uncertainty.  
* Demonstrates **\[Ethical Responsibility\]** by avoiding misleading statistical analyses, selective reporting, or unsupported conclusions.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Communication Effectiveness\]** by explaining statistical evidence, uncertainty, and conclusions clearly to technical and non-technical audiences.  
* Demonstrates **\[Human-Centered Thinking\]** by presenting statistical information in ways that support informed decision making by diverse stakeholders.

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by applying sound statistical methods that produce accurate, reliable, and reproducible analyses.  
* Demonstrates **\[Continuous Improvement\]** by refining statistical analyses based on new evidence, peer review, and methodological advances.  
  Demonstrates **\[Continuous Learning\]** by remaining current with evolving statistical methods and best practices.

## Knowledge Units

* SF \- Statistical thinking  
* SF \- Study design  
* SF \- Descriptive statistics  
* SF \- Uncertainty quantification  
* SF \- Inference

## SF \- Statistical thinking 

“Statistical thinking will one day be as necessary for efficient citizenship as the ability to read and write.”  \-- H.G. Wells  
   
Statistical thinking is the ability to understand, interpret, and use data by recognizing that variation exists in all processes, and by applying appropriate methods to draw conclusions and guide decision-making under uncertainty. Statistical thinking ensures that only appropriate or valid inferences from data are made. It helps get the answer to the question being posited, rather than the right answer to the wrong question. Areas of statistical thinking include causation, multivariate thinking, and bias. Causation reminds us that we cannot draw conclusions about cause and effect from measures of correlation in observational studies. Multivariate thinking recognizes the potential impact of confounding variables. When confounders are included, either through multivariable models or through stratification, they change the observed relationships between the explanatory (independent) and response (dependent) variables. Examples include Simpson’s Paradox, etc. Bias is any systematic difference between the true, unknown parameter from a population and a sample statistic that is calculated from the data and used to estimate it. Making decisions using data can be trivial, but making *valid* decisions using data requires statistical thinking.  
 

### Knowledge

#### *Core*

* Potential outcomes  
* Causal conclusions (correlation vs. causation) and generalizability  
* Confounders- identifying, controlling or adjusting  
* Types and causes of bias (e.g., including missing data, non-response bias, selection bias, recall bias, voluntary response bias, etc.)  
* Consequences of bias and possible mitigation  
* Non-differential bias and bias towards the null  
   

#### *Specialization / Concentration*

* Directed acyclic graphs (DAGs)  
* Designing studies that eliminate, or at least minimize, bias (see DoE)  
* Data missing not at random  
* Propensity scores

#### *Electives*

* N/A

 

### Skills

   
Recommended skill level: Evaluate  
 

* **Remembering:** Define statistical thinking, including bias, multivariable thinking, and causation.  
* **Understanding:** Describe the impact of biases and confounding variables on results.  
* **Applying:** Illustrate how an interpretation of a result changes in the presence of bias or confounders.  
* **Analyzing:**  Detect bias and potential confounders in a data-based decision-making context.  
* **Evaluating:** Decide whether the amount of bias or the impact of confounders is sufficient to invalidate findings.  
* **Creating:** Design a study, model, or analysis that is free from bias and in which causation can be established.

 

## SF \- Study design {#sf---study-design}

The process of randomly selecting samples from a population of interest for downstream analysis of collected data. A solid understanding of sampling basics is essential for data scientists because it underpins the validity and generalizability of their analyses. Sampling allows data scientists to draw meaningful conclusions about a larger population without needing to collect data from every individual, saving time and resources. Improper sampling introduces bias, distorts findings, and leads to incorrect decisions. Knowing how to select representative samples, calculate appropriate sample sizes, and account for variability ensures that experiments and models are built on reliable foundations. Whether designing surveys, performing an experiment, or building predictive models, sampling is a critical step that influences the accuracy, fairness, and credibility of the results.

### Knowledge

#### *Core*

* Random sampling and assignment  
* Observational vs. experimental studies  
* Purpose of sampling   
* Sampling methods  (random, stratified, convenience or other to ensure representativeness)  
* Identifying target populations and building a sampling frame  
* Common pitfalls (sampling bias, under coverage, nonresponse bias, overgeneralization)

#### *Specialization / Concentration*

* Sample size calculation   
* A/B testing  
* Sampling weights

### *Electives*

* N/A

### Skills {#skills-8}

Recommended skill level: Evaluating

* **Remembering:** Recall sampling/assignment concepts and limitations to generalizability and causation.  
* **Understanding:** Explain how design choices affect scope of inference and bias.  
* **Applying:** Produce a study plan (e.g., observational vs. experimental) aligned to a defined research question.  
* **Analyzing:** Detect confounding and bias risks and propose mitigation strategies.  
* **Evaluating:** Judge design adequacy by validity, feasibility, ethics, and stakeholder criteria.  
* **Creating:** Create a study protocol (e.g., A/B plan with power considerations).


## SF \- Descriptive Statistics

Descriptive statistics are fundamental for data science.  For example, exploratory data analysis requires statistical knowledge to provide a concise summary of the main characteristics of a dataset, helping data scientists understand its structure, distribution, and potential anomalies before applying more complex models. Measures such as mean, median, standard deviation, and range offer insights into central tendency and variability, while frequency counts and visualizations like histograms or box plots reveal patterns, outliers, and skewness. This initial understanding is crucial for guiding decisions about data cleaning, transformation, and modeling strategies, ensuring that subsequent analysis is both accurate and meaningful. 

### Knowledge

#### *Core*

* Measures of central tendency and dispersion  
* Robust statistics  
* Shapes of distributions (skewness and modality)  
* Summary and visualization methods for numerical data (e.g., percentiles, quartiles, five number summary statistics)  
* Summary and visualization methods for categorical data  
* Multivariate descriptive statistics  
* Impact of missing data and outliers


#### *Specialization / Concentration*

* Smoothing methods  
* Dimensionality reduction  
* Categorical data analysis  
* Summary and visualization methods for time series data  
* Techniques for text or other non-numerical data

### *Electives*

* Use of AI for descriptive statistic ideas for brainstorming

### Skills

Recommended skill level: Creating

* **Remembering:** State descriptive measures and pitfalls (e.g., mean vs. median under skew).  
* **Understanding:** Explain how distributional properties and summary statistics connect .  
* **Applying:** Produce t summaries and visualizations for a dataset.  
* **Analyzing:**  Detect distributional features (e.g., multimodality) and decide on transformations or segmentation.  
* **Evaluating:** Assess whether summaries are adequate (e.g., heavy tails require robust stats) to support defensible reporting.  
* **Creating:** Design a reproducible  reporting workflow  and explanatory narrative for EDA.

## SF \- Uncertainty quantification

Uncertainty quantification (UQ) is the process of identifying, characterizing, and reducing uncertainties in data, models, and predictions. It involves assessing how confident we can be in the results of data-driven analyses, especially when inputs, measurements, or model assumptions are imperfect or incomplete. For data scientists, UQ is crucial because it helps ensure that insights and decisions based on data are robust and reliable. By understanding the range and sources of uncertainty, data scientists can better communicate risks, guide decision-making under uncertainty, and improve model performance and trustworthiness in real-world applications. 

### Knowledge

#### *Core*

* Randomness, probability, and uncertainty  
* Measures of sampling variability  
* Confidence level / coverage rate  
* Margin of error, confidence interval, and prediction interval  
* Bootstrapping  
* Bayesian vs. Frequentist approaches

#### *Specialization / Concentration*

* Credible intervals  
* Simultaneous bands

### *Electives*

* Uncertainty quantification for application area (e.g., biology, time series) 

### Skills

Recommended skill level: Analyzing

* **Remembering:** Define  uncertainty and identify key tools (e.g., confidence intervals, bootstrap) to quantify it.   
* **Understanding:** Explain why  calculating and reporting uncertainty is necessary  (e.g., sampling variability, model assumptions).  
* **Applying:** Identify and compute  appropriate uncertainty measures (given the structure of the data).  
* **Analyzing:** Detect and attribute sources of uncertainty (e.g., small samples, model misspecification).  
* **Evaluating:** Justify decision-making in the presence of the quantified uncertainty.  (e.g., risk tolerance, safety constraints).  
* **Creating:** Develop a plan to minimize uncertainty for a decision based on data (e.g., model, tasks).

## SF \- Inference {#sf---inference}

Inference in data science refers to the process of drawing conclusions about a population or underlying data-generating process based on a sample of data. It involves using statistical methods to estimate parameters, test hypotheses, and make predictions while accounting for uncertainty. Inference is essential for data scientists because it allows them to make informed decisions and generalizations beyond the observed data, ensuring that their models and analyses are not just descriptive but also predictive and explanatory. Understanding inference helps data scientists validate results, avoid misleading conclusions, and communicate findings with appropriate confidence.

### Knowledge

#### *Core*

* Decision-making with hypothesis testing or estimation (confidence intervals)  
* Applicability, assumptions, conditions, and scope of inference  
* Testing using null and alternative hypotheses  Large sample-based vs. simulation-based methods  
* Significance level (size) and power, including Type I and Type II errors  
* P-values and critical values  
* Adjusted error rates for multiple testing  
* Effect size and practical significance  
* Causation (versus correlation)

#### *Specialization / Concentration*

* Power analysis   
* Exact inference  
* Bayesian inference  
* Causal inference

### *Electives*

* N/A

### Skills {#skills-2}

Recommended skill level: Evaluating

* **Remembering:** Name appropriate hypothesis testing methods based on type of data (e.g., numeric, categorical, ordinal)  .  
* **Understanding:** Explain assumptions, scope of inference, and pitfalls for a given inference method.   
* **Applying:** Perform appropriate statistical inference to support making a decision based on data.   
* **Analyzing:** Contextualize inferential claims by strength of evidence, practical significance, and risk constraints.   
* **Evaluating:** Diagnose assumption violations and select alternative methods when appropriate.   
* **Creating:** Design an inference plan for a new study.

# Statistical Modeling (SM)  {#statistical-modeling-(sm)}

Statistical modeling, defined as the process of using mathematical frameworks to represent real-world phenomena through data, is a cornerstone of data science. Modeling allows data scientists to identify and understand relationships among variables, make predictions, and quantify uncertainty in their analyses. By applying models such as regression, data scientists can move beyond descriptive statistics to infer patterns and test hypotheses. This capability is essential for turning raw data into actionable insights, guiding strategic decisions, and building robust machine learning systems. A strong grasp of statistical modeling ensures that data-driven conclusions are not only insightful but also grounded in rigorous analytical reasoning.

## Competencies 

A data science graduate can design, fit, evaluate, and interpret statistical models to support inference and prediction under uncertainty, making defensible decisions based on model assumptions, diagnostics, and limitations.

## Dispositions \- DRAFT VERSION

**Analytical and Evidence-Based Practice**

* Demonstrates **\[Analytical Reasoning\]** by selecting, developing, interpreting, and refining statistical models appropriate to the problem and available data.  
* Demonstrates **\[Statistical Thinking\]** by evaluating model assumptions, uncertainty, variability, and the scope of inference.  
* Demonstrates **\[Critical Thinking\]** by comparing competing models and selecting those that best balance interpretability, predictive performance, and complexity.  
* Demonstrates **\[Evidence-Based Decision Making\]** by using empirical model evaluation and diagnostics to guide model selection and improvement.  
* Demonstrates **\[Professional Skepticism\]** by recognizing that statistical models are approximations of reality and interpreting results cautiously.

**Professional Responsibility**

* Demonstrates **\[Professional Integrity\]** by communicating model assumptions, limitations, uncertainty, and appropriate interpretation honestly and transparently.  
* Demonstrates **\[Ethical Responsibility\]** by considering fairness, bias, and potential consequences when developing and applying statistical models.

**Collaboration and Human-Centered Practice**

* Demonstrates **\[Communication Effectiveness\]** by explaining statistical models, predictions, assumptions, and implications clearly to technical and non-technical audiences.  
* Demonstrates **\[Collaboration\]** by working effectively with domain experts to develop, validate, and interpret statistical models.  
* Demonstrates **\[Human-Centered Thinking\]** by selecting modeling approaches that support stakeholder understanding, transparency, and informed decision making.

**Quality and Continuous Improvement**

* Demonstrates **\[Attention to Quality\]** by validating, diagnosing, documenting, and refining statistical models to improve reliability and reproducibility.  
* Demonstrates **\[Continuous Improvement\]** by improving models through iterative evaluation, validation, and feedback.  
* Demonstrates **\[Continuous Learning\]** by adopting advances in statistical modeling techniques, software, and best practices.

## Knowledge Units

* SM \- Models  
* SM \- Model Selection  
* SM \- Model Diagnostics  
* SM \- Interpretation of Modeling results

## SM \- Models

Knowledge of statistical and optimization models is crucial for data scientists because these models form the backbone of analytical reasoning and decision-making in data-driven environments. Statistical models allow data scientists to understand relationships within data, make predictions, and quantify uncertainty, while optimization models help identify the best possible solutions under given constraints. Optimization, in particular, is essential for tasks such as resource allocation, model tuning, and improving algorithm performance. Together, these models enable data scientists to not only interpret data but also to act on it efficiently and effectively. By mastering both, data scientists can build robust, scalable solutions that are grounded in mathematical rigor and tailored to real-world challenges. See ML \- ML foundations for additional models. 

### Knowledge

#### *Core*

* Linear Regression  
* Logistic Regression  
* Lasso and ridge regression  
* Ensemble Models (Bagging, Boosting, Stacking  
* Generalized linear model   
* Deterministic Models

#### *Specialization / Concentration*

* Queueing and M/M  
* Decision Analysis (Influence Diagrams, Payoff Tables, Decision Making without Probabilities, Decision Making with Probabilities, Decision Trees, Multicriteria Decision Making)

### *Electives*

* Stochastic Processes  
* Nonlinear Models   
* Natural Language Processing  
* Named Entity Recognition and Sentiment Analysis  
* Hierarchical Modeling  
* Domain-specific models (healthcare, finance or education)  
* Optimization algorithms

### Skills

Recommended skill level: Evaluating

* **Remembering:** Define common models  and assumptions.  
* **Understanding:** Explain how model formulation affects interpretation and prediction (e.g., choice of link function, inclusion of interactions or nonlinear terms).  
* **Applying**Apply a model for a given data set.  Specifically, fit and validate models (e.g., regression with diagnostics) for a defined DS use case.  
* **Analyzing:** Diagnose lack-of-fit and condition  failures (e.g., residual patterns) and improve model specification.  
* **Evaluating:** Assess the suitability of models using  criteria such as predictive utility, interpretability, uncertainty, fairness, and efficiency.  
* **Creating:** Design an appropriate feedback loop to refine the modeling approach once in production.  

## SM \- Model selection {#sm---model-selection}

Knowledge of model selection is essential for data scientists because choosing the right model directly impacts the accuracy, interpretability, and efficiency of data-driven solutions. Model selection refers to the process of evaluating and comparing different statistical or machine learning models to identify the one that best fits the data and meets the objectives of the analysis. This involves balancing trade-offs between complexity and performance, avoiding overfitting or underfitting, and considering factors such as data size, feature types, and computational resources. A well-chosen model can reveal meaningful insights and make reliable predictions, while a poorly chosen one can lead to misleading conclusions and wasted effort. Data scientists should recognize that no single model is universally best and should balance predictive performance, interpretability, robustness, fairness, and resource constraints when making selection decisions. Therefore, understanding model selection is key to building robust, trustworthy, and impactful data science applications.

### Knowledge

#### *Core*

* Information criteria: Akaike Information Criterion (AIC), Bayes Information Criterion (BIC), and other metrics  
* Prediction error metrics (e.g. specificity/sensitivity, MSE)  
* Model complexity control (e.g. overfitting, underfitting)  
* Cross-validation,,   
* Inference (See [SF \- Inference](#sf---inference)) 

#### *Specialization / Concentration*

* Hyperparameter tuning   
* Variable importance metrics  (e.g, SHAP)

### *Electives*

* BDBayesian

### Skills

Recommended skill level:  Evaluating

* **Remembering:** Recognize common model selection approaches (e.g. AIC, cross-validation),   and their common pitfalls.  
* **Understanding:** Explain trade-offs in selection criteria (e.g., bias-variance, parsimony vs. accuracy).  
* **Applying:** Use appropriate selection procedures (e.g., k-fold CV, regularization)  given the model objective(s).  
* **Analyzing:** Compare competing models and examine selection outcomes across metrics.  
* **Evaluating:** Choose and justify the selected model.  
* **Creating:** Design a selection framework and workflow for a new application.

## SM \- Model Diagnostics {#sm---model-diagnostics}

Knowledge of model diagnostics is critically important for data scientists because it ensures that the models they build are not only accurate but also reliable and interpretable. Model diagnostics refers to the process of evaluating a model’s performance, conditions, and potential limitations through statistical tests, residual analysis, and validation techniques. This helps identify issues such as overfitting, multicollinearity, or violations of underlying assumptions that could compromise the validity of the results. By conducting thorough diagnostics, data scientists can refine models, improve predictive power, and build trust in their findings.

### Knowledge

#### *Core*

* Multicollinearity checks  
* Residual analysis  
* Goodness of fit metrics  
* Variance-bias tradeoff  
* Condition validation

#### *Specialization / Concentration*

* Diagnostics for Generalized Linear Models

### *Electives*

* Diagnostics for advanced models (see SM-Model Electives)

### Skills

Recommended skill level: Evaluating

* **Remembering:** Recall diagnostic checks and typical issues (e.g., heteroscedasticity) to validate models.  
* **Understanding:** Explain what each diagnostic implies about model validity (e.g., condition violations) e.  
* **Applying:** Run diagnostics (e.g., residual plots, influence measures) and document findings for a fitted model.  
* **Analyzing:** Diagnose root causes of failed condition checks (e.g., nonlinear relationships, interactions, outliers) .  
* **Evaluating:**  Test alternate model formulations to address failed conditions.  
* **Creating:** Design automated diagnostic checks for deployed models.

## SM \- Interpretation of Models {#sm---interpretation-of-models}

Knowledge of model interpretation is critically important for data scientists because it ensures that the insights derived from models are understandable, trustworthy, and actionable. Model interpretation refers to the process of explaining how a model makes its predictions or decisions, including identifying which features are most influential and how they interact. This is especially vital when communicating results to non-technical stakeholders or when working in regulated industries where transparency is required. Interpretable models help build confidence in data-driven solutions, reveal potential biases, and support ethical decision-making. Without the ability to interpret models, even highly accurate predictions can be rendered useless if their rationale cannot be understood or justified.

### Knowledge

#### *Core*

* Decision making   
* Prediction  
* Interpretation of model parameters

#### *Specialization / Concentration*

* Model Card

### *Electives*

* Decision Theory

### Skills

Recommended skill level: Applying

* **Remembering:** Recall definitions of model components (e.g., coefficients, parameters/features).  
* **Understanding:** Explain how model limitations (e.g., data bias, conditions, uncertainty, and the non-causal nature) affect the validity and scope of interpretations.  
* **Applying:** Translate model outputs into insights (e.g., effect sizes, predictions) for a defined stakeholder decision.  
* **Analyzing:** Diagnose interpretability risks (e.g., confounded features, unstable explanations).  
* **Evaluating:** Assess whether interpretations are valid and  support a decision given uncertainty and model constraints.  
* **Creating:** Create communication artifacts (e.g., model cards, decision briefs) that convey results, limits, and risks.

  

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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NaIGM1Aj0jADNaIGM1Aj0jADNaIGM1Aj0jADNaIGM1Aj0jADNSKac+fOudOnT4tSp04t2rNnj7w+e/ZscHfDiFfMQI2IZs2aNS5RokTuhhtuOE+fffZZcHfDiFfMQI2I54UXXjjPPB988EGJTg3jWmIGakQ8ZqBGpGIGakQ8oabxNn03IgEzUCMq8EehFn0akYIZqBEVaBSKLPo0IgUzUCNq6N69u8iiTyNSMAM1ogYzUCPSMAM1DMMIEzNQwzCMMDEDNQzDCBMzUMMwjDAxAzUMwwgTM1DDMIwwMQM1DMMIEzNQwzCMMIl6Az127Jj77bffYoht1zOrVq1y8+bNC26OF5YuXSr68MMP3c6dO4Nve+zfv98dPnw4uDlkfR46dOi8h+ePHz9+3n6qgwcPevvt27fvvPdVf/zxh++MMdm9e7eUI+IPN+/YsSO4y2VDRxs/frz8Qej44NSpU2716tVu5cqV8geojatP1Bvohg0bXPHixd3NN9/sGjZsKKpbt67LlSuXq1GjRlSY6ZkzZ0R06nDYtWtXjNcffPCBa9u2bYxt8cHw4cNdly5dRN26dXPZsmUL7uLx+uuvu969ewc3u/Xr17unnnpKlCJFCtehQwf34osvusyZM7uBAweKYNOmTe7ZZ591t9xyi/eZqGnTpq5QoULe+fgL9vXq1XPlypVzN910k2vRooWI188884y3nx/aT4MGDVyPHj1EOXPmlPMqDAwXGhxiY/To0XINy5cvD751WVysrXz66aeirFmzupYtW7pGjRq5e++9102dOlV0KVxpm7xeiHoDhSFDhkgD8UN08fjjj7tHH33UnTx5UhSpYDzo3//+d/CtS6J06dLBTdeExx57zC1atEgERH+hIHrE2O6//36J7oJfzUF9But05syZ3l9jIiqEkSNHujRp0nj7KJSlfg2IGu706dPd3//+9xj79evXL8ZrWLt2rcuQIcN521577TX5mcGqVq1aonC44447rthAL9RWFixY4JIlSybasmWLt517oJOjS/n8K22T1wtmoBHAlTZWM9CYmIGagcYXCcJAP/roo/MMFPgTaHS4b775RgRMvZjq9erVy8uF7d271/Xs2VM6aefOnUVM2TCAYcOGudq1a0suCSmTJ092jRs39vbHsCnIcePGuf79+7sJEyaI6tSp4x3366+/irp27SpTK/b9/PPPJf2AnnvuOflTbeTJ6NxMcRH5RPJmffv2laklmjRpkpyT6Sn32L59exEpDYxl6NCh3rWC/3q51lDXy7X6rzcUoc4DlF/y5MmlrNC0adMCR/4/1BdT48SJE8t+wX15P1inTNnVQL/++mvZNmbMmPMMFAMJZdyhDDQUmDOf8eabb3qdA2bNmiV50Dx58siUHvGHTagT6hNGjRolIu1AjhdISbRq1UrEPadMmTKGgQXbI7lXRAqENtupUydJOWgQoO2FthKq7EqVKuXKli0rCvLkk0+KeG/GjBlynT/99JNoxYoV8prcebBN6mewj6ZAGOA0KPnxxx9du3btRAw033//vbc/IoVAX6StMqBpu3njjTekH5w4cUL213sk1UH/0/NAsN9ECgnaQIE82ltvvSU6cOCANB4ioCZNmrjy5cuLqCiioaJFi7ovv/xSVKBAAffII4+4sWPHuldeecU98cQTIsBUaQwUnEYjHEtnqFy5srvrrrukMSLysMWKFZPjKlWqJMLkaFBcA+cgSkZ0vq1bt7qXXnrJpUqVyr399tuid955x1WsWFEarRo5fxfzyJEjnrEcPXpUxPHk9/hcvdbg9XKtoa6XY/zXGyS28wALQmnTpnVz5swRaacIRcmSJeUc/JHkp59+WuRHDRSzeffdd8XM7rvvPlehQgURuTnAQIm0dPAgr5o9e3a3bdu2GOeDSzVQ6Nixo7vxxhslh4gYWIFImQFN2w3tCIPgGoB7RgwMGzdulDK5++67vYGTdkZdYaC0xVDtkfdQ+vTpXf78+d3HH3/ssmTJIgMi0vZCW/EbvEK7adasmSiItlXtK+SV/SZM2WLcwTbJa0wNI2RhCnEs7ZH29vDDD3umOGXKFCkP7peBH3HPmCuDL0ZTs2ZNEXWSI0cON2jQIPl82gMictZIWs8b7DeRQoI3UKIiFlQQUxJGaCIHIgI1DFZ4GZlHjBjhHUcnUhPCEDBYBHnz5pVRGnTKSiOh4xKRMGorRC50AFADzZ07t2zXjv7Pf/5TpNMlIsJgBEG90Hh0YYPP++WXX8QE+dkP0aFeO9cavF6N5ILXyzX5rzfIhc4D99xzj7cKHxtEOAwGCxculKhV/0gyA4GiBsr56EwcU716dXfnnXeK9PwYKK+1k/F98dTzlRoofPfdd/KX75FG+MDMgOtHgFGqgSosbLEd0wkODkTMGKROkYPtkbaISIcwEwFmBQwiCPxtJQhlhtGhIAx+SBf3qE+/gWJqGCgE2yQD5eLFi/880f+gjImy2Z+68ZMuXToZ9JkJIMqPQQJY3PV/JrMpBj4Gk4wZM4ooD85LX9EBJVS/iQQStIESHVB5uvpI+E90p2gUQINl1ddvoFSimhCjIefXzyB/x+gLmmujAOfOnSvm5zdQOn+mTJnkZ/08VnkxjT59+sj2YGNlmkM04IfOSITCNBKxmhubgdL49Nr1u9T916u5sOD1cq3+6w1yofPApRholSpVJKrBHBCdGVE3SqgpPGgHq1q1qrwONYXnESYaNNE5Ui7VQNetWyfmB7oSTcTDfWICl2OgGF+ZMmVivEeUvmzZMrnfUO1RDbRw4cKegZIyadOmjQguZKDkw/UphiC6XT8zlIFqOiLYJilnTRsppBrq169/3owFs8PAtb37DZQByf+ZlG3r1q3FnCk3pLMXykHPEarfRAIJwkAHDx58Xmdj5CtYsKArUaKEtw1zYEo/ceJEqRCd6lBRNAIiAgUD1ZF1/vz5XueFl19+Waa+QISEOC+NhIjOb358pkauzZs3FwGGzoICFClSRMTnk48dMGDAeREokRa5P83b0pB4vo9FDRoo00XEfZNT02vnWoPXy7WGul41UL3eIBc6D9DJGGxQEKZfyG8YwOcjpp6aN6Q+g3W6fft2MUCkRoIRaxn6IUdGjg8pTC0ZdEItWvnh/rWOFKJtpvIcR91gUoiIl6kqdUG5c42IzkQuFfPBENgPcTzXS/loWQfboz8CJX0EmBFRGgJ/W0F+iNZIISB/rpXrUYP6+eefZRuPe+mCHQMiUSZTbQi2SQYDTJ3oD3EPDOoMTGp6anxM6Zmu631rigny5csnsxidyZAzZSChbBhcEDlW2gLtgsUvFKrfRAJmoGagZqA+zEDNQC+HqDdQpukku5lGaU7z1VdflQZOjs3/GxhUEtOAJEmSyDR19uzZIqYPdH4ezOb+EY2HqSU/s6qsnZcGw/SMJDoNngUbxEIDxsZxdHxMF+mxdGYMHTFVwgQwOtCVTR6fIenOLwZgmN9++60IOIZrZPqKeJ9pJPfH59HhENNnOgYdnobHtQavl2sNdb26gq7XGyS28wAP77PwgsEinQYDHY4FOUQnZeFB0bwcnYz75nxaTtRptWrV5EH6hx56yHtKgIGCfDCLUXwmdYqY6rIvCze62AGsMrOv5jJRbI+1YWrkgJmG6soyD9xrhyd3q48J0flpUyz20FaYjiLaF20Q03j++ee9NAqDedKkSWUgYtBBwfaoAxALaBxLvWA6LGoiyk7bij7pEURz2bQBFkC5X8xvyZIlIoUg4bbbbhNxj/rYH3Xnb5N8BuVNnag501doe5QxCz/UHaJMOA50EZRyZzGQxdlbb71V0jiIPDP3RvkxIGPIiBwqpsw6hBKq30QCUW+g4cDodqEo5FIgSiAHebGIxo+O0ozKRBxBNJKLDX6lUfH/hhWNWHOxseG/3ivhap0nUqFc6RAsShGpabTmR81PIU/q/80kcoN+9NEk6if4HoTTHi/WVhSuKxil+tHfquIe2I/69RP8HJ0BBdHt/rxzuNCe/W0dLtRvriXXpYEahmFcDcxADcMwwsQM1DAMI0zMQA3DMMLEDNQwDCNMzECNqIBf9eSxG2QYkYIZqBEV0C71WVfDiBTMQI2owAzUiETMQI2owAzUiETMQI2owAzUiETMQI2owAzUiETMQI2owAzUiETMQI2owAzUiETMQI2owAzUiETMQI2owAzUiETMQI2owAzUiETMQI2owAzUiETMQI2owAzUiETMQI2I5r333pMvueMrk/nuIMTrHDlyyFc8GMa1xAzUiGjMQI1IxgzUiGj4ojK+oZFvdvSrfv36wV0NI94xAzUintatW8cwT752me9jN4xrjRmoEfEEo1CLPo1IwQzUiAqIQok8Lfo0IgkzUCMqIApt2bKlyDAiBTNQIyowAzUiETNQI2o4e/asyDAiBTNQwzCMMDEDNQzDCBMzUMMwjDAxAzUMwwgTM1DDMIwwMQM1DMMIEzNQwzCMMDEDNQzDCBMz0P+xf/9++U0XdOzYMdHVYunSpe7DDz90O3fuDL4VFqtWrRLNmzcv+NZV48yZM27KlClu8+bNwbekbLSs+Huc6NSpU8HdIp64LsOrUe+nT5/2ylp19OjR4G5xQny0s4SAGej/mDZtmkudOrXLly+fq1mzpog/2jt06NDgrpfM8OHDRV26dHHdunVz2bJlC+4SFh988IGobdu2wbeuGlOnTnXJkyd306dPD77l1q9f75566il5v2HDhqLs2bO7atWqucOHDwd3jxh27doV43VcluHVqnfKs0OHDvIXqCpVqiQqXry4y5s3r1u5cmVw9yvGX0bx0c4SAmagzgw0iBnolXG16t0MNPIxA/2LJ554wrVp08Z7jXkmSpTI/fLLL769Lp3H/voCtEWLFsnrffv2BfaIbHLmzBnSQGHQoEEuU6ZM3us9e/ZIA+rTp49vr8iidOnSwU1xxtWsd6btGOiKFStEgInGRR+NzzJKKJiB/gWN0m+gs2bNkoZLeYwfP97169dP1Lt3b8ltweTJk13jxo1FnTt3dn/88Yds79mzp0RoqHbt2hLhAp0KNWnSxE2YMEFyXGjIkCGi5s2bu7feekv25W9edu3aVcRfIBo3bpw7ceKEGzlypMgfHYe6DiqVY/r37y/i8+rUqeNWr17tHYfx9e3b1zVo0MBNmjTJ2w558uSJ1UCJTPwGSs6UCL5Zs2aS+0NEprNnz3aNGjWSayEXiIjMevXqJcawe/du16NHD9H8+fPlPgcOHOiOHz8ugiVLlkgUxrmJfhHn0zrR+kDB+9F7qlevntRl+/bt3YYNG0ShylDL0V+G/nL0l6G/HBXqXeveX+8XOnfwPoIcOHDgPAPl3OnSpZPyQ927d/fO/8MPP0iZBcvND+dp0aKFtLmTJ0+KgmUUqp3pcf5jQevVX7fXC2agf4GB1q1b10ueFy1aVMqBxvHSSy+5VKlSid5++233zjvvuGHDhkmj0wKsVauWHANMvdKmTSuaM2eOGN+IESPEHNCRI0dclixZ3JgxY6STq1FynlKlSsk5mK5pZ1+zZo2YLtFwuXLlRDVq1JD9YrsOrrty5crurrvuEtGZOKZYsWLePVesWFE6AmZAtM11IbiYgaZPn95t2bJFRKdLliyZW7dunXv//fdFdEYMETPbvn27K1u2rAhj5F7Kly8vCxRarkWKFJFyvfPOO+VaEeWIGbFQxWcQISF/nWh9oOD96D1t2rRJrocFmK1bt4pClaGWo78M/eXoL0N/OSpcr9a91vvFzh28jyBqoJ9//rlI000Y7rJly0QZM2aUqJfBl4FfB29/ucHo0aNFDGos/GXOnNkbvINlFGxn/uP8x3J9Wq/+ur1eMAP9Cwy0TJkynsktXLjQnTt3Tt4j+lADUMhD0aAVIksa4LZt2+Q13yKJiMYAY9S/Z0nEgFkzFZ44caLX4JkCY5iAgebOnVtEp9DzEsEgbdgXug6iseeee04EnAfjVqhrzJkIkGMwaE1ZXMxA06RJ40V+RGa6OkweDXE+GhaQE+T+EffeqlUruX7Kl/wp+uqrr2Rfcm65cuUSAYaxePFi6cyPPvqoCLRO/ATvR+8Jo+JnP6HKUMvRX4b+cgQtQ385BvHX+8XOHeo+/KiB6qBC2WtbUAoVKuQ++eQT7zVlFiw3wLgR24Hz8AQKCpZRsJ35jwM9VuuWeg3W7fWAGehfmIGagcZmcmagZqCxYQb6F8EcqB8MtUKFCiKFaRRTGIVcJoU4d+5ceR000AwZMni5MIUGCKNGjRJxTjocZkTHwWQRU1FdoGFlF2nDvtB10Dn9BsqU2Z+7ZFrGdGvHjh3upptuuiwD9Z/HD3lIRGckNwoMGkxVkcL9+Q3066+/lu0zZsyQ6SFiqsjqPtPbsWPHuoIFC4pA68RP8H70noLmAKHKUMvRX4b+cgQtw9juH/z1frFzh7oPP6FyoEFIf1A+oGUWLDdg0EP+fLfmUYNlFGxnweOA47Ru/WjdXg+Ygf7F448/Los4oRgwYMB5EejLL78suTGFXGCKFCm8xQ9trAsWLJDX5I8oV7R27VrJs2KKdE7NJbJiy+IACyr+a+GxojvuuEN+1mR99erV5fWFroPIyW/8dH4ez1LIN2JcJP0xaR6NQTT+Bx54wH3xxRfevn6InMmBhkI7JJ1RFxn4XK4JEXHTwVjc8BsoD+4Dnb5du3aib7/9VgyI/QYPHuzy588vOnjwoFcnfoL3o/ekETH5ScoYhSpDLUd/GfrLEbQM/eUYxF/vFzt3qPvws3fvXrl2+iUKBQbK4AFaZsFyo8xYAEOFCxeWCJJr1Lyo1pmWUbCd+Y/zH6t1S70G6/Z6wAzU/bmIkDJlSnlmj5VjpNCwiE7pnIgGChs3bpQoicaCmCrNnDlT3iNCu/HGG0V0HPZlJZSGjujYJUqUkMbGYkCBAgVEdFQ6E19bQdSgz6QSGdOYWYxhuoayZs0qRhzbdWAifNa9994rwpRZveVbLYnyEOems1etWlXujUUYxAIIXyNcpUoV78kCZfny5XJtGhUHH13q1KmTiM7YsWNH2cb9aDSdJEkSid60jNVAmWZSFhiORsKHDh2SaC5HjhwSCSVNmlTEqrXWidYHBO9H74mojzJgoUWfEghVhlqO/jL0l6O/DLUc/eizk/56j+3cOtCEug+F9sEiHGWpz4H6v5EU80IMrrQnIm8ts2C5MdUmvYGov8SJE7tnn33WexKEOvKXUbCd+Y/zH6t1S70G6/Z6wAz0CmCU1c5+Od/V43/MgyiN1VqEQSq81l+VpCNdiHCvA+hwcDV/ffVCkLbwX6MaKOkCDCAInVSvjdTGxX6V0X8//ntiasu5YoMy1HK83DK8GHF57lCoKfrLLUioR40uVkagg0oQzaXGx/1FEmagxjWFR3CQfyHMMKIFM1DjmmIGakQzZqDGNYMnEpo2bSrikRkWOgwjmjADNQzDCBMzUMMwjDAxAzUMwwgTM1DDMIwwMQM1DMMIEzNQwzCMMDEDNQzDCBMzUMMwjDAxAzUMwwgTM1DDMIwwMQM1DMMIEzNQwzCMMDEDNQzDCBMzUMMwjDA5z0D50/18hYB+i6LJZDKZQqtkyZIi/UI+M1CTyWS6RJ1noPyzbNky+eIrk8lkMl1cmzdv/n8DNQzDMC6f/wPqzaY3fXAw0wAAAABJRU5ErkJggg==>