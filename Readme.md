# **LegalAI Crew**: Automated Legal Research, Writing, and Editing Agent

## **Overview**

**LegalAI Crew** is a robust AI-powered system designed for comprehensive legal research, analysis, writing, and review. Using state-of-the-art large language models (LLMs) and custom tools, it automates the workflow of legal research professionals, ensuring efficient, accurate, and high-quality outputs.

---

## **Key Features**

- **Multiple Specialized Agents**: 
  - **Legal Research Analyst**: Performs in-depth research on legal topics.  
  - **Legal Content Writer**: Generates detailed legal analysis.  
  - **Legal Editor**: Reviews and ensures the accuracy of legal documents.

- **Task Automation**: Streamlined task execution for research, writing, and editing, with predefined goals and outputs.

- **Advanced Search Integration**: Utilizes the **TavilySearchResults** tool for precise and advanced internet-based legal research.

- **LLM-Driven**: Powered by **Ollama LLM** (`llama3:8b`) for high-quality language understanding and generation.

- **Collaborative Workflow**: Agents work together in a structured pipeline to deliver a finalized legal analysis document.

---

## **System Workflow**

### **Agents and Their Roles**
1. **Legal Research Analyst**:
   - **Goal**: Research laws and regulations.
   - **Tool**: Tavily Internet Search.
   - **LLM**: Ollama LLM.

2. **Legal Content Writer**:
   - **Goal**: Create a comprehensive legal document.
   - **LLM**: Ollama LLM.

3. **Legal Editor**:
   - **Goal**: Review and finalize legal documentation.
   - **LLM**: Ollama LLM.

### **Tasks**
1. **Research Task**:
   - **Description**: Gather information on the specified legal topic in the target country.
   - **Output**: Detailed research report.

2. **Writing Task**:
   - **Description**: Draft a legal analysis document with citations.
   - **Output**: Comprehensive legal analysis.

3. **Editing Task**:
   - **Description**: Review and validate the analysis for accuracy and compliance.
   - **Output**: Finalized legal document.

---

## **Installation**

### **Prerequisites**
- **Python 3.8+**
- Required Libraries:  
  - `crewai`  
  - `langchain_community`  
  - `pydantic`  

### **Setup**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/srishrachamalla7/LegalAI-Crew.git
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Code**:
   ```bash
   python main.py
   ```

---

## **Usage**

1. **Set Up the LLM**:
   Ensure the Ollama LLM is running on `http://localhost:11434`.

2. **Add Tavily API Key**:
   Replace `tvly-xxxxxx` with your own **Tavily API Key** in the code.

3. **Customize Inputs**:
   Modify the `inputs` in `crew.kickoff()` for the desired country and query.

4. **Run the Crew**:
   Execute the tasks to generate a comprehensive legal document.

---

## **Example Execution**

### Input:
```python
crew.kickoff(
    inputs={
        "country": "United States",
        "query": "Data Privacy Regulations"
    }
)
```

### Output:
- A finalized legal analysis document saved to `Legal Research\md_files\legal_analysis.md`.
## Demo
![Untitled video - Made with Clipchamp (4) (1)](https://github.com/user-attachments/assets/ca655b0c-1f93-4dcd-9207-5f0cba0a5fbd)


---

## **Recommended Name**: **LegalAI Crew**

The name reflects the collaborative nature of the system and its focus on legal research and document generation using AI agents.

---

## **Contributing**

We welcome contributions to enhance this project. Please fork the repository and create a pull request for review.

---


## **Disclaimer**

This tool is designed for educational and research purposes. Users must ensure compliance with local laws and regulations when using the system for legal analysis.
