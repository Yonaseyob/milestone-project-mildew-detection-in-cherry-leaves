![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Codeanywhere Template Instructions

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Codeanywhere Template Instructions section of this README.md file,  and modify the remaining paragraphs for your own project. Please do read the Codeanywhere Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use. 

## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into <a href="https://app.codeanywhere.com/" target="_blank" rel="noreferrer">CodeAnywhere</a> with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and <code>pip3 install -r requirements.txt</code>

1. In the terminal type <code>pip3 install jupyter</code>

1. In the terminal type <code>jupyter notebook --NotebookApp.token='' --NotebookApp.password=''</code> to start the jupyter server.

1. Open port 8888 preview or browser

1. Open the jupyter_notebooks directory in the jupyter webpage that has opened and click on the notebook you want to open.

1. Click the button Not Trusted and choose Trust.

Note that the kernel says Python 3. It inherits from the workspace so it will be Python-3.8.12 as installed by our template. To confirm this you can use <code>! python --version</code> in a notebook code cell.


## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


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

- It will answer business requirement 1
  - Checkbox 1 - Difference between average and variability image
  - Checkbox 2 - Differences between average Powdery Mildew and average healthy leaf.
  - Checkbox 3 - Image Montage

### Page 3: Powdery Mildew Detector

- Business requirement 2 information  
- Link to download a set of powdery mildew-contained and healthy leaves images for live prediction.
- User Interface with a file uploader widget. The user should upload multiple cherry leaves images. It will display the image and a prediction statement, indicating if the leaf is infected or not with powdery mildew and the probability associated with this statement.
- Table with the image name and prediction results.
- Download button to download table.

### Page 4: Project Hypothesis and Validation

- Block for each project hypothesis, describe the conclusion and how you validated it.

### Page 5: ML Performance Metrics

- Label Frequencies for Train, Validation and Test Sets
- Model History - Accuracy and Losses
- Model evaluation result


## Unfixed Bugs

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.
