# Module-2-Challenge (Loan Qualifier)

The main goal of this project is to create a loan qualifier application that allows users to see which loans (from an [existing_list](data/daily_rate_sheet.csv)) they qualify for.

---

## Technologies

This application uses **python version 3.7** and two libraries: **fire** and **questionary**.  

---

## Installation Guide

To run the application on your local terminal you need to install both fire and questionary onto your python environment. Once you activated the python environment under which you want to install the libraries type `pip install fire` and `pip install questionary`. If you want to confirm whether already installed in your environment type into your terminal `pip show fire` and `pip show questionary`.

---

## Usage

To use application navigate in your terminal to the folder where you have saved **app.py**. Once you are there you will follow the below steps:

> 1. Type `python app.py`
> 2. The CLI will ask you where the loan data is saved. In this repo it is in the following directory [./data/daily_rate_sheet.csv](data/daily_rate_sheet.csv).
> 3. The CLI will ask you to input your credit score, monthly debt, monthly income, desired loan amount, and home value.
> 4. Your monthly debt to income and loan to value ratio will print. If you qualify for any loans you will then be asked whether you would like to save the loan data.
> 5. You can then decide where to save the csv file containing the information of the loans you qualifed for. 

Please see below for a sample of interaction with the application:

![screenshot_of_terminal_using_app.py](code_screenshots/Terminal_ss.jpg)

The newest feature in this application is the function which allows the user to save the loans they qualify for in a separate csv file. The code for that function lies in the [fileio.py](qualifier/utils/fileio.py) module:

```python
def save_csv(csvpath, data, header):
        """Saves the CSV file in the path provided.

    Args:
        csvpath (Path): The desired csv file path.
        data: the information desired to be stored in the path.
        header: inputs for the first row of the csv file labeling the information in each column.

    Returns:
        A csv file saved in the specified path.
    """
        with open(csvpath, 'w', newline='') as csvfile:
             csvwriter = csv.writer(csvfile)
             csvwriter.writerow(header)
             for row in data:
                  csvwriter.writerow(row)
                  
        return print("Your File Has Saved")
```

---

## Contributors

[Moises Coriat](https://www.linkedin.com/in/moises-coriat)

---

## License

MIT
