# Grade app


## Overview
- The Grading App is a comprehensive solution for students and educators to track and manage academic performance throughout the semester. It allows users to scan rubrics by taking pictures, tracks overall expectations for classes, and calculates current grades. Additionally, it provides insights into what needs to be done to improve grades for quizzes and other assessments.

## Features
### Scan Rubrics

1. Users can take pictures of rubrics to input grading metrics.
2. The app uses OCR (Optical Character Recognition) to extract data from the images.

### Track Class Expectations

1. The app allows users to input and track class expectations and goals.
2. Users can see a summary of what is expected in each class for the semester.

### Calculate Current Grades

1. Users can input their grades for various assessments.
2. The app calculates the current grade based on the input data.
3. Users can see a breakdown of their performance in different assessments.

### Grade Improvement Insights

1. The app provides insights into what needs to be done to improve grades.
2. Users can see the required scores for upcoming quizzes and assignments to reach their target grade.
Installation


To run the Grading App locally, follow these steps:

Clone the repository

```bash

git clone https://github.com/yourusername/grading-app.git
cd grading-app

```

Install dependencies

``` bash
pip install -r requirements.txt

```
Run the app
```bash
python main.py
```

Usage
Scanning Rubrics

Navigate to the "Scan Rubrics" section.
Take a picture of the rubric or upload an image file.
The app will process the image and extract grading metrics.
Tracking Class Expectations

Go to the "Class Expectations" section.
Input the expectations and goals for each class.
The app will display a summary of the expectations.
Calculating Current Grades

Navigate to the "Current Grades" section.
Input your grades for various assessments (e.g., quizzes, assignments, exams).
The app will calculate and display your current grade.
Grade Improvement Insights

Go to the "Grade Insights" section.
The app will show what scores are needed on upcoming assessments to improve your grades.
Project Structure
/app - Contains routes and main application logic.
/models - Defines data models for users and grades.
/services - Includes OCR service and other utility functions.
/db - Handles database operations.
requirements.txt - Lists the dependencies required to run the app.
main.py - The main entry point for the application.
Contributing
We welcome contributions from the community! If you have any suggestions or find any bugs, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.