# ICP Document Generation Flow

## Overview
This document outlines the flow of the Individualized Care Plan (ICP) document generation process in the Django application. The process consists of multiple views that capture essential information about the student’s educational needs, strengths, and support requirements. Each view corresponds to a specific section of the ICP document.

## Flow Steps

1. **Home View**
   - The process begins at the home view where users can navigate to create a new student record.

2. **Student Creation View**
   - Users fill out the **Student Creation Form** which includes:
     - Student Name
     - ID Card Number
     - Inclusive Education (IE) Program
     - Date of Document
   - Upon successful submission, the user is redirected to the **General Information View** for the newly created student.

3. **General Information View**
   - Users complete the **General Information Form** which includes:
     - Parent Concerns
     - Medical Alerts
   - After submission, the user is redirected to the **Learning Profile View**.

4. **Learning Profile View**
   - Users fill out the **Learning Profile Form** which includes various learning disabilities and strengths.
   - Upon successful submission, the user is redirected to the **Developmental Areas View**.

5. **Developmental Areas View**
   - Users complete the **Developmental Areas Form** to specify developmental areas of focus.
   - After submission, the user is redirected to the **Skills & Strengths View**.

6. **Skills & Strengths View**
   - Users fill out the **Skills & Strengths Form** to capture the student's skills and strengths.
   - Upon successful submission, the user is redirected to the **Accessible Learning Support View**.

7. **Accessible Learning Support View**
   - Users complete the **Accessible Learning Support Form** to specify the support required.
   - After submission, the user is redirected to the **Measurable Goals View**.

8. **Measurable Goals View**
   - Users fill out the **Measurable Goals Form** to set annual goals for the student.
   - Upon successful submission, the user is redirected to the **Intervention Services View**.

9. **Intervention Services View**
   - Users complete the **Intervention Services Form** to specify the services required.
   - After submission, the user is redirected to the **Supplementary Services View**.

10. **Supplementary Services View**
    - Users fill out the **Supplementary Services Form** to specify additional support services.
    - Upon successful submission, the user is redirected to the **Generate ICP View**.

11. **Generate ICP View**
    - The final view generates the ICP document based on all the information collected from previous views.
    - The document is then made available for download.

## Conclusion
This flow ensures that all necessary information is captured efficiently and accurately, leading to the generation of a comprehensive ICP document for each student.
