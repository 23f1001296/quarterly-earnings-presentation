---
marp: true
theme: custom
paginate: true
_paginate: false
---

<!-- Theme definition -->
<style>
section {
  font-family: "Segoe UI", sans-serif;
}
h1, h2, h3 {
  color: #004aad;
}
.custom-box {
  padding: 20px;
  border: 3px solid #004aad;
  border-radius: 10px;
  background: #f0f6ff;
}
</style>

# Product Documentation  
### (Marp Presentation)

**Author:** 23f1001296@ds.study.iitm.ac.in  
**Role:** Technical Writer — Software Engineering

---

# Overview

- Written using **Marp Markdown**
- Version-controlled in GitHub
- Exportable to PDF / PPTX / HTML
- Custom styles + theme  
- Page numbers enabled

---

<!-- Slide with background image -->
![bg](https://images.unsplash.com/photo-1527443224154-9f1a03845f5c)

# Architecture Summary

System consists of:

- API Gateway  
- Authentication Service  
- Documentation Generator  
- CI/CD Pipeline  

---

# Custom-Styled Content

<div class="custom-box">
This slide demonstrates **custom styling** using Marp CSS inside the Markdown file.

Use these to highlight warnings, notes, or important product concepts.
</div>

---

# Mathematical Equation Example

For algorithmic performance:

\[
T(n) = 3n^2 + 2n + 1
\]

Dominant term:

\[
T(n) = O(n^2)
\]

---

# Background with Text Overlay

![bg opacity:.25](https://images.unsplash.com/photo-1518770660439-4636190af475)

# API Workflow

1. Client sends request  
2. Request validated  
3. Service layer processes data  
4. Response returned as JSON  

---

# Code Sample (Syntax Highlighting)

```python
def generate_docs(api_list):
    """Generate markdown-based documentation."""
    docs = []
    for api in api_list:
        docs.append(f"# {api['name']}\n{api['description']}")
    return "\n\n".join(docs)
```

---

# Conclusion

- Fully Marp-compliant  
- Includes theme, styling, background images  
- Contains math, code, email  
- Ready for GitHub Pages & raw link submission  

**Email:** 23f1001296@ds.study.iitm.ac.in

