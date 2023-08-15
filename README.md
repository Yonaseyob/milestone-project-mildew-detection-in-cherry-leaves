
![pmd](https://github.com/Yonaseyob/milestone-project-mildew-detection-in-cherry-leaves/assets/112119971/9a406ffa-cb96-457f-b411-efd1bfd36b72)

A powdery mildew detector is an ML system that helps the user to detect a powdery mildew fungus on a given leaf.

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* We suspect powdery mildew leaves have clear marks/signs, typically in the tip of the leaf, differentiating them from healthy leaves.

    A average image study can help to investigate it


## The rationale to map the business requirements to the Data Visualisations and ML tasks
 * Business Requirement 1: Data Visualization
     - We will display the "mean" and "standard deviation" images for powdery mildew and healthy leaves.
     - We will display the difference between an average powdery mildew leaf and an average healthy leaf.
     - We will display an image montage for either powdery mildew or healthy leaves.

 * Business Requirement 2: Classification
     - We want to predict if a given leaf is infected or not with powdery mildew.
     - We want to build a binary classifier and generate reports.
.

## ML Business Case

### Powdery MildewClf

- We want an ML model to predict if a leaf is infected with powdery mildew or not, based on Farmy & Foods. It is a supervised model, a 2-class, single-label, classification model.
- Our ideal outcome is to provide the client a faster and more reliable diagnostic for powdery mildew detection.
- The model success metrics are
  - Accuracy of 65% or above on the test set.
- The model output is defined as a flag, indicating if the cell has powdery mildew or not and the associated probability of being infected or not. The client will take an image of leaves and upload the picture to the App. The prediction is made on the fly (not in batches).
- Heuristics: The current diagnostic needs an experienced staff and detailed inspection to distinguish infected and not infected leaves. 
- The training data to fit the model come from Farmy & Foods, taken from their crops. This dataset contains about 4+ thousand images. We have extracted a subset of 5643 images from this dataset and saved it to [Kaggle dataset directory](https://www.kaggle.com/codeinstitute/cherry-leaves/) for quicker model training.
  - Train data - target: infected or not; features: all images


## Dashboard Design
### Page 1: Quick Project Summary
![pmdps](https://github.com/Yonaseyob/milestone-project-mildew-detection-in-cherry-leaves/assets/112119971/63b39baa-0b97-4eb7-ac8a-8f43361162a2)

- Quick project summary
  - General Information
    - powdery mildew is a fungus that attacks cherry leaves.
    - The process is manual verification if a given cherry tree contains powdery mildew. 
  - Project Dataset
    - The available dataset contains 5643 out of +4 thousand images taken from the client's crop fields.
  - Link to additional information
  - Business requirements
    - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
    - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Page 2: Leaves Visualizer
![pmdlv](https://github.com/Yonaseyob/milestone-project-mildew-detection-in-cherry-leaves/assets/112119971/7aba1c6b-c25c-4e2c-a231-af935b6c2af4)

- It will answer business requirement 1
  - Checkbox 1 - Difference between average and variability image
  - Checkbox 2 - Differences between average Powdery Mildew and average healthy leaf.
  - Checkbox 3 - Image Montage

### Page 3: Powdery Mildew Detector
![pmdp](https://github.com/Yonaseyob/milestone-project-mildew-detection-in-cherry-leaves/assets/112119971/44e2e18d-611b-4e65-bf09-db95dc3d5770)

- Business requirement 2 information  
- Link to download a set of powdery mildew-contained and healthy leaves images for live prediction.
- User Interface with a file uploader widget. The user should upload multiple cherry leaves images. It will display the image and a prediction statement, indicating if the leaf is infected or not with powdery mildew and the probability associated with this statement.
- Table with the image name and prediction results.
- Download button to download table.

### Page 4: Project Hypothesis and Validation
![pmdph](https://github.com/Yonaseyob/milestone-project-mildew-detection-in-cherry-leaves/assets/112119971/76f7a685-d241-4efd-b2df-b744b463fa99)

- Block for each project hypothesis, describe the conclusion and how you validated it.

### Page 5: ML Performance Metrics
![pmdpm](https://github.com/Yonaseyob/milestone-project-mildew-detection-in-cherry-leaves/assets/112119971/6c883e0c-0146-4f52-ac80-860b1d57629e)

- Label Frequencies for Train, Validation and Test Sets
- Model History - Accuracy and Losses
- Model evaluation result

### Unfixed Bugs
- I could not find any unfixed bugs.
  
## Deployment
### Heroku
* The App live link is: https://powdery-mildew-detector2-ff6fa6cf58a7.herokuapp.com/
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process doesn't happen smoothly because of the slug size so I add large files not required for the app to the .slugignore file.
6. After that deployment goes smoothly, and by clicking the button Open App on the top of the page to access the App.
 
## Main Data Analysis and Machine Learning Libraries
* Here are the main libraries used in the project.
* numpy
* pandas
* matplotlib
* seaborn
* plotly
* streamlit
* scikit-learn
* tensorflow-cpu
* keras
* protobuf

## Credits 
### Content 

- All the project ideas and structure is adopted from the code institute walkthrough01 project.

## Acknowledgements (optional)
I would like to thank the slack team at project-portfolio-5-predictive-analytics.
