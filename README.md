Environment Setup:

    _ Programming Language: Python, HTML
    
    _ IDE: Visual Studio Code (with the virtual environmemt of python (env))
    
    _ Install Selenium WebDriver in VS Code
    
    _ Browser: Chrome Browser with the Chrome Driver, and choosing chromedriver version which is suitable with your device in https://googlechromelabs.github.io/chrome-for-testing/

How to run code:

    _ Firstly, run VS Code

    _ Installing and running Xampp, then starting "Apache" and "MySQL"
    
    _ Ensuring that you had installed the relating modules (e.g., pytest, webdriver, etc)
    
    _ About Execution:
        + For Batch execution:
            * Save all codes in a folder
            * Right click -> Choose "Run Tests"

            * If you want a detailed report:
                + Run tests with HTML report generation
                        pytest --html=report.html

                + After the tests finish running, a report.html file will be generated.
                + Open it in any web browser to see a detailed, color-coded report of your test results.
        
        + For Individual execution:
            * Save all codes in a folder
            * In each python file, first press the key combination "CTRL + S"
            * A play symbol appear next to the name of each function
            * Click that symbol of the function which you want to run test
