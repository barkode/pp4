
# Testing

Return back to the [README.md](README.md) file.

![Main Image]()

# Contents

- [Responsiveness Tests](#responsiveness-tests)
- [Code Validation](#code-validation)
    * [HTML](#html)
    * [CSS](#css)
    * [JavaScript](#javascript)
    * [Python](#python)
    * [Python (Unit Testing)](#python--unit-testing-)
- [Manual Testing](#manual-testing)
- [Role-based Restrictions](#role-based-restrictions)
- [Bugs](#bugs)
- [Browser Compatibility](#browser-compatibility)
- [User Story Testing](#user-story-testing)
- [Lighthouse Testing](#lighthouse-testing)
- [Accessibility Testing](#accessibility-testing)


## Responsiveness Tests


[Back to top](#contents)


## Code Validation

### HTML

The recommended [HTML W3C Validator](https://validator.w3.org) to validate all of the project's HTML files.

This is the process which was followed of validating an HTML file by direct input:

1. **Access the Validator**: Visit the [W3C Markup Validation Service](https://validator.w3.org/).
2. **Choose Direct Input**: Select the "Validate by Direct Input" tab.
3. **Paste Your HTML Code**: Copy HTML code and paste it into the text box.
4. **Validate**: Click the "Check" button to validate HTML.

<details>

<summary>HTML Validation Results</summary>

</details>


[Back to top](#contents)

### CSS

The [W3C Jigsaw](https://jigsaw.w3.org/css-validator/) tool, provided by the W3C, enables to validate and verify the correctness of CSS code. It ensures that your web pages adhere to W3C standards, promoting interoperability and accessibility.

### JavaScript

No major errors were found when validating JavaScript through [Jshint](https://jshint.com/).
<details>

<summary>Jshint</summary>

![Jshint]()
</details>

### Python

The python files have all been passed through [PEP8 CI Online](https://pep8ci.herokuapp.com/)

<details><summary><b>PEP8 Test Results</b></summary>

</details><br/>

[Back to top](#contents)

### Python (Unit Testing)

Python's `unittest` framework offers a robust and flexible testing solution.
Ideally, every part of the project should be put through the robust automated testing. Due to time constraints I have utilized automated tests for Insights application concentrating on CRUD related functionality views, models and forms.

The automated tests highlighted a redundant view and non existent html file. Although these issues did not affect the functionality of the application, the quality and maintainability of the code are equally important.

![Unittest]()

[Back to top](#contents)

## Manual Testing

In addition to using `unittest`, extensive manual testing was performed on the application. Each feature was verified against success criteria. Where applicable, negative testing was conducted by providing invalid or unexpected inputs to assess the application's robustness in handling errors and exceptions.

<details><summary><b>Manual Testing Results</b></summary>

</details><br/>

[Back to top](#contents)



## Role-based Restrictions

The user role based restrictions were tested to ensure that view and functionality reflects the scope of the project.

[Back to top](#contents)

## Bugs
## Browser Compatibility

The deployed project was tested on the most popular browsers for compatibility issues.
No major issues identified.

[Browser Testing Results]()

## User Story Testing


## Lighthouse Testing


<details><summary><b>Lighthouse Test Results</b></summary>

</details><br/>

[Back to top](#contents)


## Accessibility Testing

Although, accessibility scores were high on Lighthouse, I have retested the page.
[WAVE](https://wave.webaim.org/) online tool was used to check terminal colour contrast. All tests were passed. However, it should be noted that logo may return contrast error depending on browser and operating system.

While building the application, the general principles of accessibility were adhered to:

- Using clear instructions
- Validating inputs before moving on to the next step
- Testing the page to make sure it does not affect performance from user input
- Using ARIA labels

![WAVE]()

[Back to top](#contents)